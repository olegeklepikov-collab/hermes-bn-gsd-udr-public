"""Bound native RPC to its controller deadline and preserve observed evidence."""
from contextvars import ContextVar
from functools import wraps
from pathlib import Path
import hashlib
import hmac
import json
import os
import re
import signal
import subprocess
import tempfile
import time

_deadline = ContextVar('udr_native_rpc_deadline', default=None)


def bounded_controller(callback):
    @wraps(callback)
    def run(*args, **kwargs):
        token = _deadline.set(kwargs.get('execution_control_deadline'))
        try:
            return callback(*args, **kwargs)
        finally:
            _deadline.reset(token)
    return run


def call(worker, operation, sid, extra):
    budget = 90 if operation in {'team', 'prepare_turn', 'deliver_report'} else 45
    deadline = _deadline.get()
    if deadline is not None:
        budget = min(budget, deadline - time.time() - .25)
    if budget <= 0:
        raise TimeoutError('UDR_RPC_DEADLINE_EXHAUSTED operation=' + operation + ' before executor')
    started = time.monotonic()
    process = subprocess.Popen([str(worker)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        stdout, _ = process.communicate(json.dumps({'operation': operation, 'sid': sid, **extra}), timeout=budget)
    except BaseException as exc:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.communicate()
        if isinstance(exc, subprocess.TimeoutExpired):
            raise TimeoutError('UDR_RPC_TIMEOUT operation=' + operation + ' elapsed=' +
                               str(round(time.monotonic() - started, 2)) + 's; native process group stopped; result requires reconciliation') from exc
        raise
    value = json.loads(stdout)
    if not isinstance(value,dict):raise RuntimeError('UDR_RPC_INVALID_RESPONSE operation='+operation)
    if process.returncode or 'error' in value:
        raise RuntimeError('UDR_RPC_REJECTED operation=' + operation + ': ' + str(value.get('code', 'no valid result')))
    return value


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def atomic_write(path, value):
    descriptor, name = tempfile.mkstemp(prefix='.evidence-', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(canonical(value))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def preserve(root, sid, call_id, event):
    text = event['text']
    if re.search(r'(?i)(?:(?<![A-Za-z0-9_-])sk-[A-Za-z0-9_-]{20,}|Bearer\s+[A-Za-z0-9_-]{16,}|[0-9]{8,}:[A-Za-z0-9_-]{30,})', text):
        raise PermissionError('sensitive_worker_evidence_refused')
    body = {'contract': 'UDRObservedToolEvidenceV1', 'sid': sid, 'tool_call_id': call_id,
            'event': event, 'reading_level': 'tool_result_only', 'truth_accepted': False}
    digest = hashlib.sha256(canonical(body)).hexdigest()
    directory = Path(root) / 'state/native-evidence-outbox' / hashlib.sha256(sid.encode()).hexdigest()
    directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    destination = directory / (digest + '.json')
    key = (Path(root) / 'state/authority/bn-bridge.key').read_bytes()
    envelope = {'body': body, 'mac': hmac.new(key, canonical(body), hashlib.sha256).hexdigest()}
    if destination.exists():
        if json.loads(destination.read_text()) != envelope:
            raise PermissionError('observed_evidence_changed')
    else:
        atomic_write(destination, envelope)
    return destination


def settled(path, receipt):
    atomic_write(path.with_suffix('.receipt.json'), {'status': 'registered', 'receipt': receipt})
