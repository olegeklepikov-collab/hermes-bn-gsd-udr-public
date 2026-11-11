"""Opt-in mandatory execution controls, separate from fail-open observers.

Controls inspect the final payload immediately before its executor. A configured
controller must exist, finish, and explicitly allow; it cannot mutate the payload.
The file is operator state and is scoped through get_hermes_home on every call.
"""
from __future__ import annotations

import contextvars
import copy
import json
import math
import threading
import time
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

CONTRACT_VERSION = 1
KINDS = frozenset({"tool", "tool_result", "llm", "auxiliary"})
_lock = threading.RLock()
_callbacks: dict[tuple[str, str, str], Callable] = {}
_required_homes: set[str] = set()
_slots = threading.BoundedSemaphore(8)
_pool = None


class ExecutionControlDenied(PermissionError):
    status_code = 403
    non_retryable = True


@dataclass(frozen=True)
class ExecutionDecision:
    allow: bool
    reason: str = ""
    reservation_id: str | None = None
    on_abort: Callable[[str], None] | None = field(default=None,repr=False,compare=False)


def _abort_decision(decision, reason):
    if isinstance(decision,ExecutionDecision) and callable(decision.on_abort):
        try:decision.on_abort(reason)
        except Exception:
            logging.getLogger(__name__).exception('Execution admission cleanup failed; dependent path remains closed')


def _home() -> Path:
    from hermes_constants import get_hermes_home
    return get_hermes_home().resolve()


def _policy() -> tuple[str, dict] | None:
    home = _home()
    key = str(home)
    path = home / "execution-controls.json"
    if not path.exists():
        with _lock:
            if key in _required_homes:
                raise ExecutionControlDenied("Required execution control policy disappeared")
        try:
            manager=home/"runtime-manager.json"
            if manager.exists():
                value=json.loads(manager.read_text())
                if value.get("execution_policy_required") is True:
                    raise ExecutionControlDenied("Managed runtime requires its execution control policy before startup")
            config=home/"config.yaml"
            if config.exists():
                import yaml
                value=yaml.safe_load(config.read_text()) or {}
                if value.get("execution_controls_required") is True:
                    raise ExecutionControlDenied("Configured mandatory execution policy is missing")
        except ExecutionControlDenied:
            raise
        except Exception as exc:
            raise ExecutionControlDenied("Cannot verify whether execution policy is required") from exc
        return None
    with _lock:
        _required_homes.add(key)
    try:
        if path.is_symlink() or path.stat().st_size > 65536:
            raise ValueError("Unsafe execution control policy")
        def unique(items):
            d = {}
            for k, v in items:
                if k in d:
                    raise ValueError("Duplicate policy key")
                d[k] = v
            return d
        value = json.loads(path.read_text(), object_pairs_hook=unique)
        if set(value) != {"version", "required", "timeout_seconds"} or type(value["version"]) is not int or value["version"] != CONTRACT_VERSION:
            raise ValueError("Unsupported execution control policy")
        required = value["required"]
        if not isinstance(required, dict) or not set(required) <= KINDS:
            raise ValueError("Invalid execution control kinds")
        for controllers in required.values():
            if not isinstance(controllers, list) or not controllers or any(
                not isinstance(x, str) or not x.strip() or x != x.strip() for x in controllers
            ) or len(set(controllers)) != len(controllers):
                raise ValueError("Invalid required controllers")
        timeout = value["timeout_seconds"]
        if isinstance(timeout, bool) or not isinstance(timeout, (float, int)) or not math.isfinite(timeout) or not 0 < timeout <= 60:
            raise ValueError("Invalid execution control timeout")
        return key, value
    except Exception as exc:
        raise ExecutionControlDenied("Required execution control policy is unreadable or invalid") from exc


def register_control(plugin_id: str, kind: str, callback: Callable) -> Callable[[], None]:
    if kind not in KINDS or not plugin_id or not callable(callback):
        raise ValueError("Invalid execution control registration")
    key = (str(_home()), kind, plugin_id)
    with _lock:
        if key in _callbacks:
            raise ValueError("Execution controller already registered")
        _callbacks[key] = callback
    def remove():
        with _lock:
            if _callbacks.get(key) is callback:
                _callbacks.pop(key)
    return remove


def _callback_stack(identity: dict) -> str:
    # File/function/line only: never payloads, local variables, source text or secrets.
    import sys
    frame = sys._current_frames().get(identity.get("thread_id"))
    frames = []
    while frame is not None and len(frames) < 24:
        frames.append(f"{frame.f_code.co_filename}:{frame.f_lineno}:{frame.f_code.co_name}")
        frame = frame.f_back
    return " | ".join(frames) or "worker_not_started"


def _bounded(callback: Callable, payload: dict, timeout: float, *, controller="", kind="") -> Any:
    global _pool
    label = f"Required {kind or payload.get('execution_kind', 'unknown')} execution controller '{controller or 'unknown'}'"
    operation = (payload.get("payload") or {}).get("tool_name") or "model"
    if not _slots.acquire(blocking=False):
        raise ExecutionControlDenied(label + " cannot start: execution controllers are still busy")
    context = contextvars.copy_context()
    deadline = time.time() + timeout
    started = time.monotonic()
    identity = {}
    def invoke():
        identity["thread_id"] = threading.get_ident()
        try:
            return context.run(callback, **{**payload, 'execution_control_deadline': deadline})
        finally:
            _slots.release()
    with _lock:
        if _pool is None:
            from tools.daemon_pool import DaemonThreadPoolExecutor
            _pool = DaemonThreadPoolExecutor(max_workers=8, thread_name_prefix="execution-control")
        future = _pool.submit(invoke)
    try:
        result = future.result(timeout=timeout)
    except BaseException as exc:
        elapsed = time.monotonic() - started
        finished_failure = future.done() and not future.cancelled() and future.exception() is exc
        failure = "callback_failed" if finished_failure else "deadline_exceeded"
        logging.getLogger(__name__).error(
            "Execution controller failure controller=%s kind=%s operation=%s failure=%s error_type=%s elapsed_seconds=%.3f timeout_seconds=%.3f worker_stack=%s",
            controller, kind, operation, failure, type(exc).__name__, elapsed, timeout, _callback_stack(identity))
        # A late admission never starts an executor. Its exact reservation is closed
        # only when that callback actually returns the matching abort receipt.
        def discard_late(done):
            try:
                context.run(_abort_decision, done.result(), 'controller_wait_aborted_before_executor')
            except BaseException:
                pass
        future.add_done_callback(discard_late)
        detail = f" failed ({type(exc).__name__})" if finished_failure else f" timed out after {timeout:g}s"
        raise ExecutionControlDenied(label + detail) from exc
    elapsed = time.monotonic() - started
    logging.getLogger(__name__).log(
        logging.INFO if elapsed >= 1 else logging.DEBUG,
        "Execution controller completed controller=%s kind=%s operation=%s elapsed_seconds=%.3f allowed=%s",
        controller, kind, operation, elapsed, isinstance(result, ExecutionDecision) and result.allow is True)
    return result


def authorize(kind: str, payload: dict, **identity: Any) -> tuple[ExecutionDecision, ...]:
    policy = _policy()
    if policy is None:
        return ()
    home, settings = policy
    decisions = []
    for controller in settings["required"].get(kind, []):
        with _lock:
            callback = _callbacks.get((home, kind, controller))
        if callback is None:
            for earlier in decisions:_abort_decision(earlier,'required_controller_unavailable_before_executor')
            raise ExecutionControlDenied(f"Required {kind} execution controller '{controller}' is unavailable")
        try:
            detached = copy.deepcopy(payload)
            data = {**identity, "execution_kind": kind, "payload": detached,
                    "execution_control_version": CONTRACT_VERSION}
            decision = _bounded(callback, data, settings["timeout_seconds"], controller=controller, kind=kind)
        except ExecutionControlDenied:
            for earlier in decisions:_abort_decision(earlier,'admission_rejected_before_executor')
            raise
        except BaseException as exc:
            for earlier in decisions:_abort_decision(earlier,'admission_failed_before_executor')
            raise ExecutionControlDenied("Required execution controller could not inspect the payload") from exc
        if not isinstance(decision, ExecutionDecision) or decision.allow is not True:
            _abort_decision(decision,'admission_rejected_before_executor')
            for earlier in decisions:_abort_decision(earlier,'admission_rejected_before_executor')
            reason = decision.reason if isinstance(decision, ExecutionDecision) else "No explicit execution decision"
            raise ExecutionControlDenied(reason or "Execution denied by required controller")
        decisions.append(decision)
    return tuple(decisions)
