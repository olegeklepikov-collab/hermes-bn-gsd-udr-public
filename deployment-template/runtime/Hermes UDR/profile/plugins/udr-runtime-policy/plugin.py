"""Trusted role boundaries through native Hermes tools; no agent loop."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import fcntl
import contextlib
import signal

@contextlib.contextmanager
def one_writer(workspace):
    lock = workspace / '.udr-writer.lock'
    fd = os.open(lock, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise PermissionError('workspace_writer_busy')
        yield
    finally:
        os.close(fd)

def context():
    from hermes_constants import get_hermes_home, get_default_hermes_root
    home = get_hermes_home()
    base = get_default_hermes_root()
    role = home.name if home.parent == base / 'profiles' else 'default'
    if role not in {'default', 'engineering', 'quantitative', 'review', 'operator'}:
        raise PermissionError('profile_not_qualified')
    root = base.parent
    policy = root / 'operator/qualification/role-policy.json'
    if policy.is_symlink() or not policy.is_file() or policy.stat().st_mode & 0o077:
        raise PermissionError('required_role_policy_unavailable')
    definition = json.loads(policy.read_text())['roles'][role]
    workspace = Path(definition['workspace']).resolve(strict=True)
    return root, role, workspace, definition

def path_in(workspace, value):
    path = Path(value)
    if not path.is_absolute():
        path = workspace / path
    path = path.absolute()
    path.relative_to(workspace)
    for item in (path, *path.parents):
        if item == workspace:
            break
        if item.is_symlink():
            raise PermissionError('symlink_denied')
    resolved = path.resolve()
    resolved.relative_to(workspace)
    return resolved

def workspace_tool(args, **_):
    _, role, workspace, policy = context()
    action = args['action']
    path = path_in(workspace, args.get('path', '.'))
    if action == 'read':
        if not path.is_file() or path.stat().st_size > 262144:
            raise PermissionError('bounded_regular_file_required')
        text = path.read_text()
        return json.dumps({'path': str(path), 'text': text, 'sha256': hashlib.sha256(text.encode()).hexdigest()})
    if action == 'list':
        return json.dumps({'paths': sorted(x.name for x in path.iterdir())[:200]})
    if action == 'write':
        if policy['read_only'] or role == 'operator':
            raise PermissionError('writer_authority_denied')
        content = args['content']
        if len(content.encode()) > 262144:
            raise ValueError('content_limit')
        with one_writer(workspace):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        return json.dumps({'written': str(path), 'sha256': hashlib.sha256(content.encode()).hexdigest()})
    raise ValueError('action_unknown')

def command_tool(args, **_):
    root, role, workspace, policy = context()
    if role not in {'engineering', 'quantitative', 'default'} or policy['read_only']:
        raise PermissionError('command_authority_denied')
    sandbox = Path('/usr/bin/sandbox-exec')
    if not sandbox.is_file():
        raise PermissionError('required_native_sandbox_unavailable')
    argv = args['argv']
    if not isinstance(argv, list) or not argv or any(not isinstance(x, str) or len(x) > 32768 for x in argv):
        raise ValueError('bounded_argv_required')
    timeout = min(max(int(args.get('timeout', 60)), 1), 180)
    with tempfile.TemporaryDirectory(prefix='command-', dir=workspace) as temp:
        rules = ['(version 1)', '(allow default)', '(deny network*)',
            '(deny process-info* (target others))', '(deny signal (target others))']
        # Public system libraries remain readable; private homes and other runtime
        # workspaces do not. Darwin's loader requires reads outside /System and /usr.
        rules += ['(deny file-read-data (subpath ' + json.dumps(str(Path.home())) + '))',
            '(deny file-read-data (subpath "/private/var/folders"))']
        rules += ['(deny file-read-data (require-all (subpath ' + json.dumps(str(root.parent)) +
            ') (require-not (subpath ' + json.dumps(str(root / 'software')) +
            ')) (require-not (subpath ' + json.dumps(str(workspace)) +
            ')) (require-not (subpath "__HERMES_UDR_R_RUNTIME__"))))']
        rules += ['(deny file-write* (require-all (require-not (subpath ' + json.dumps(str(workspace)) +
            ')) (require-not (subpath "/dev"))))']
        git = root / 'workspace/engineering-project/.git'
        rules += ['(deny file-write* (subpath ' + json.dumps(str(git)) + '))']
        env = {'PATH': str(root / 'software/R-runtime/bin') + ':' + str(root / 'software/bin') + ':/opt/homebrew/bin:/usr/bin:/bin',
            'HOME': str(Path.home()), 'TMPDIR': '.', 'TZ': '__TIMEZONE__', 'LANG': 'C.UTF-8',
            'R_LIBS_USER': str(root / 'software/R-runtime/lib/R/library'), 'PYTHONDONTWRITEBYTECODE': '1',
            'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'}
        with one_writer(workspace):
            process = subprocess.Popen([str(sandbox), '-p', '\n'.join(rules), *argv], cwd=workspace,
                env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
            try:
                stdout, stderr = process.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                return json.dumps({'status': 'unknown_outcome', 'reason': 'command_deadline',
                    'resumption_requires_readback': True, 'native_sandbox': True})
            finally:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            result = subprocess.CompletedProcess(argv, process.returncode, stdout, stderr)
    overflow = len(result.stdout) > 65536 or len(result.stderr) > 65536
    full_path = None
    if overflow:
        payload = json.dumps({'stdout': result.stdout, 'stderr': result.stderr})
        full_path = workspace / ('command-output-' + hashlib.sha256(payload.encode()).hexdigest() + '.json')
        full_path.write_text(payload)
    return json.dumps({'exit_code': result.returncode, 'stdout': result.stdout[-65536:],
        'stderr': result.stderr[-65536:], 'role': role, 'native_sandbox': True,
        'output_complete': not overflow, 'full_output_path': str(full_path) if full_path else None})

def effect_tool(args, **_):
    root, role, workspace, _ = context()
    if role != 'operator':
        raise PermissionError('operator_profile_required')
    effect_id = args['effect_id']
    if not effect_id.replace('-', '').isalnum():
        raise PermissionError('effect_id_invalid')
    grant = root / 'operator/qualification/approved-effects' / (effect_id + '.json')
    if grant.is_symlink() or not grant.is_file() or grant.stat().st_mode & 0o077:
        raise PermissionError('approved_decision_missing')
    decision = json.loads(grant.read_text())
    if decision.get('status') != 'approved' or decision.get('effect') != 'copy_reviewed_artifact':
        raise PermissionError('approved_effect_mismatch')
    import sys
    sys.path.insert(0, str(root / 'profile/plugins/hermes-foundation-bridge/src'))
    from hermes_foundation_bridge.bridge import services
    from hermes_foundation_bridge.external_operations import guarded_external
    from hermes_foundation_bridge.canonical import receipt
    _, _, state = services(root / 'profile/foundation')
    def canonical(ref):
        return state.get({'schema_version':1, 'database':'kw_core',
            'project_id':decision['project_id'], 'object_id':ref})
    accepted = canonical(decision['acceptance_ref'])
    released = canonical(decision['release_ref'])
    if (accepted.get('status') != 'found' or accepted['object'].get('status') != 'accepted'
            or released.get('status') != 'found' or released['object'].get('status') != 'approved'
            or released['object'].get('artifact_sha256') != decision['sha256']
            or released['object'].get('acceptance_ref') != decision['acceptance_ref']):
        raise PermissionError('canonical_decision_not_verified')
    source = Path(decision['source']).resolve(strict=True)
    if source.is_symlink() or source.stat().st_size > 262144:
        raise PermissionError('source_invalid')
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != decision['sha256']:
        raise PermissionError('approved_bytes_changed')
    target = path_in(workspace, decision['target'])
    def perform():
        with one_writer(workspace):
            if target.exists():
                if target.read_bytes() != data:
                    raise PermissionError('effect_conflict')
                return receipt({'status': 'already_succeeded', 'sha256': decision['sha256'], 'readback_verified':True})
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as file:
                file.write(data)
            assert target.read_bytes() == data
            return receipt({'status': 'succeeded', 'sha256': decision['sha256'], 'readback_verified': True})
    return json.dumps(guarded_external(root / 'profile/foundation', 'udr_approved_effect',
        {'effect_id':effect_id}, decision, perform, {'succeeded','already_succeeded'}))

def guarded(handler):
    def invoke(args, **kwargs):
        try:
            return handler(args, **kwargs)
        except (PermissionError, ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
            return json.dumps({'status': 'blocked', 'error': str(exc) if isinstance(exc, (PermissionError, ValueError)) else type(exc).__name__})
    return invoke

def register(ctx):
    definitions = [
        ('udr_workspace', workspace_tool, {'action': {'enum': ['read', 'list', 'write']}, 'path': {'type': 'string'}, 'content': {'type': 'string'}}, ['action']),
        ('udr_command', command_tool, {'argv': {'type': 'array', 'items': {'type': 'string'}}, 'timeout': {'type': 'integer'}}, ['argv']),
        ('udr_effect', effect_tool, {'effect_id': {'type': 'string'}}, ['effect_id']),
    ]
    for name, handler, properties, required in definitions:
        ctx.register_tool(name=name, toolset='udr_role', schema={'name': name,
            'description': 'Native UDR role operation; missing policy or authorization blocks before action.',
            'parameters': {'type': 'object', 'additionalProperties': False, 'properties': properties, 'required': required}},
            handler=guarded(handler), check_fn=lambda: True)
