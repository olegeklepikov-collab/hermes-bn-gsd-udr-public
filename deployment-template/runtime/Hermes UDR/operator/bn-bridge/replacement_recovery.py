"""Complete operator-registered recovery only after genuine replacement products exist."""
from pathlib import Path
import hashlib
import hmac
import json


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def register(sid, old_request_id, new_request_id, mapping, reason, recipe_path):
    import backend as b
    import team_backend as team
    body = team.parent(sid)
    wave = team.get(sid, old_request_id)
    for old_key, new_key in mapping.items():
        task = wave['tasks'][old_key]
        if task['state'] not in {'blocked', 'planned'}:
            raise PermissionError('only_incomplete_tasks_may_have_replacements')
        if task['state'] == 'blocked' and (task.get('receipt') or {}).get('terminal_state') not in {'FAILED', 'CANCELLED'}:
            raise PermissionError('unsettled_attempt_requires_reconciliation')
    record = {'run_id': body['run_id'], 'parent_bead': body['bead_id'], 'old_request_id': old_request_id,
              'new_request_id': new_request_id, 'mapping': mapping, 'reason': reason,
              'recipe_path':recipe_path,'authority': 'operator-confirmed-controller-repair', 'failed_products_accepted': False}
    key = (b.ROOT / 'state/authority/bn-bridge.key').read_bytes()
    envelope = {'body': record, 'mac': hmac.new(key, canonical(record), hashlib.sha256).hexdigest()}
    directory = b.HERE / 'replacement-recovery'
    directory.mkdir(mode=0o700, exist_ok=True)
    path = directory / (hashlib.sha256(canonical(record)).hexdigest() + '.json')
    if path.exists():
        if json.loads(path.read_text()) != envelope: raise PermissionError('recovery_plan_changed')
    else:
        from control_transport import atomic_write
        atomic_write(path, envelope)
    return {'plan_id': path.stem, 'run_id': record['run_id'], 'automatic_launch': False}


def reconcile(sid):
    import backend as b
    import team_backend as team
    body = b.saved(sid)
    if not body or body.get('native_child'): return []
    folder = b.HERE / 'replacement-recovery'
    if not folder.exists(): return []
    key = (b.ROOT / 'state/authority/bn-bridge.key').read_bytes()
    completed = []
    for path in folder.glob('*.json'):
        envelope = json.loads(path.read_text()); plan = envelope['body']
        if path.is_symlink() or not hmac.compare_digest(envelope['mac'], hmac.new(key, canonical(plan), hashlib.sha256).hexdigest()):
            raise PermissionError('replacement_plan_authentication_failed')
        if plan['run_id'] != body['run_id'] or plan['parent_bead'] != body['bead_id']: continue
        target = team.path_for(body, plan['new_request_id'])
        if not target.exists(): continue
        replacement = team.get(sid, plan['new_request_id'])
        if not all(replacement['tasks'].get(new_key,{}).get('state')=='succeeded' and
                   (replacement['tasks'][new_key].get('receipt') or {}).get('terminal_state')=='SUCCEEDED'
                   for new_key in plan['mapping'].values()):continue
        previous=team.get(sid,plan['old_request_id'])
        pending=dict(plan['mapping']);ordered=[]
        while pending:
            ready=[key for key in pending if not set(previous['tasks'][key].get('depends_on',[])).intersection(pending)]
            if not ready:raise PermissionError('replacement_dependency_cycle')
            for key in ready:ordered.append((key,pending.pop(key)))
        for old_key,new_key in ordered:
            team.supersede_failed_attempt(sid,plan['old_request_id'],old_key,
                           [{'request_id':plan['new_request_id'],'key':new_key}],plan['reason'])
            completed.append(old_key)
    return completed


def pending_continuations(sid):
    import backend as b
    body=b.saved(sid)
    if not body or body.get('native_child'):return []
    folder=b.HERE/'replacement-recovery'
    if not folder.exists():return []
    key=(b.ROOT/'state/authority/bn-bridge.key').read_bytes();result=[]
    for path in folder.glob('*.json'):
        envelope=json.loads(path.read_text());plan=envelope['body']
        if path.is_symlink() or not hmac.compare_digest(envelope['mac'],hmac.new(key,canonical(plan),hashlib.sha256).hexdigest()):
            raise PermissionError('replacement_plan_authentication_failed')
        if plan['run_id']==body['run_id'] and plan['parent_bead']==body['bead_id']:
            result.append({'request_id':plan['new_request_id'],'recipe_path':plan['recipe_path'],
                           'same_research':True,'automatic_launch':False,'failed_products_accepted':False})
    return result
