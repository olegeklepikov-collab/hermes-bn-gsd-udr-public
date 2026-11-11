"""One fresh public Beads read for one mandatory RPC, never a cross-call cache."""
from contextlib import contextmanager
from contextvars import ContextVar
import copy
import re

_snapshot = ContextVar('udr_control_beads_snapshot', default=None)


def lookup(arguments):
    rows = _snapshot.get()
    if rows is not None and len(arguments) == 2 and arguments[0] == 'show' and arguments[1] in rows:
        return [copy.deepcopy(rows[arguments[1]])]
    return None


def issue_ids(sid):
    import backend as b
    body = b.saved(sid)
    if not body:
        return []
    child = body if body.get('native_child') else None
    if child:
        if not child.get('requires_udr'):
            return []
        body = b.saved(child['parent_sid'])
    if not body or body.get('phase') != 'running':
        return []
    ids = [body['bead_id']]
    if child and child.get('managed_worker'):
        from team_backend import load
        found = []
        for path in (b.root_for(body['run_id']) / 'teams').glob('*.json'):
            wave = load(path)
            if wave['sid'] != child['parent_sid'] or wave['run_id'] != body['run_id']:
                continue
            found.extend(t['bead_id'] for t in wave['tasks'].values() if t['id'] == child['task_id'])
        if len(found) != 1:
            raise PermissionError('unique_native_child_bead_required')
        ids.extend(found)
    if any(not re.fullmatch('KWF-[a-z0-9]+', value) for value in ids):
        raise PermissionError('invalid_control_bead_id')
    return list(dict.fromkeys(ids))


@contextmanager
def fresh(sid, operation):
    if operation not in {'check', 'capture', 'document_phase'} or _snapshot.get() is not None:
        yield
        return
    ids = issue_ids(sid)
    if not ids:
        yield
        return
    import backend as b
    beads = b.adapters()[3]
    result = beads._run(['show', *ids, '--readonly'])
    if not isinstance(result, list):
        raise PermissionError('invalid_control_beads_snapshot')
    rows = {row['id']: row for row in result}
    if set(rows) != set(ids):
        raise PermissionError('incomplete_control_beads_snapshot')
    token = _snapshot.set(rows)
    try:
        yield
    finally:
        _snapshot.reset(token)
