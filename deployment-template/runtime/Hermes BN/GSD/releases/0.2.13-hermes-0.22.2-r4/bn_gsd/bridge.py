"""Only fixed, operator-configured subprocesses can enter the supplied engine."""
from pathlib import Path
import json
import subprocess
import contextvars
import time
from functools import wraps
from .codec import canonical, read_json


_control_deadline = contextvars.ContextVar("bn_gsd_control_deadline", default=None)
_READ_ONLY = frozenset({"lookup", "family_status", "job_get", "job_context", "component_inventory"})


class GSDControlError(ValueError):
    pass


def bounded_controller(callback):
    @wraps(callback)
    def invoke(*args, **kwargs):
        token = _control_deadline.set(kwargs.get("execution_control_deadline"))
        try:
            return callback(*args, **kwargs)
        except GSDControlError as exc:
            from hermes_cli.execution_control import ExecutionDecision
            return ExecutionDecision(False, str(exc))
        finally:
            _control_deadline.reset(token)
    return invoke


class Bridge:
    def __init__(self, settings_path):
        self.settings_path = Path(settings_path).resolve()
        self.settings = read_json(self.settings_path.read_text())
        self.worker = Path(__file__).resolve().parents[1] / "worker.py"

    def call(self, operation, arguments=None):
        deadline = _control_deadline.get()
        expires_at = deadline - .5 if deadline is not None else None
        remaining = expires_at - time.time() if expires_at is not None else 180
        if remaining <= 0:
            raise GSDControlError("GSD_CONTROL_DEADLINE_EXHAUSTED operation=" + operation + " before worker")
        body = {"operation": operation, "arguments": arguments or {}}
        if expires_at is not None:
            body["expires_at"] = expires_at
        payload = canonical(body)
        if len(payload) > 24 * 1024 * 1024:
            raise ValueError("Input exceeds contract; split the task without trimming required data")
        from tools.environments.local import served_profile_child_env
        from hermes_constants import get_hermes_home
        env = served_profile_child_env(target_home=get_hermes_home(), inherit_credentials=False)
        env.update(PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
        # Read-only workers may be terminated at the admission deadline. Mutating
        # transactions retain their receipt/late-abort path; never guess their outcome.
        try:
            result = subprocess.run([self.settings["python"], "-I", "-B", str(self.worker),
                                     "--settings", str(self.settings_path)], input=payload,
                                    capture_output=True, timeout=min(180, remaining) if operation in _READ_ONLY else 180,
                                    env=env, cwd=self.settings["state_dir"])
        except subprocess.TimeoutExpired as exc:
            raise GSDControlError("GSD_READ_CONTROL_TIMEOUT operation=" + operation + "; read-only worker stopped") from exc
        if len(result.stdout) > 24 * 1024 * 1024:
            raise ValueError("Worker output exceeds contract; it was not truncated")
        value = read_json(result.stdout)
        if result.returncode or value.get("ok") is not True:
            error = value.get("error", {})
            if error.get("code") == "TimeoutError":
                raise GSDControlError(error.get("message", "GSD worker deadline expired"))
            raise ValueError(error.get("message", "GSD host worker failed"))
        return value["result"]

    def engine(self, tool, arguments, provider_config=None, sid=None):
        return self.call("model_engine" if sid else "engine", {"tool": tool, "arguments": arguments,
                                    "provider_config": provider_config, **({"sid": sid} if sid else {})})
