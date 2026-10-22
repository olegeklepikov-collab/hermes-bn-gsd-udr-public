"""Instance adapter to the signed public SDK. No model, no second agent loop."""
from pathlib import Path
import hashlib
import hmac
import json
import os
import sqlite3
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
HOME = ROOT / 'profile'
sys.path[:0] = [str(ROOT / 'software/hermes'),
    str(HOME / 'plugins/hermes-foundation-bridge/src'),
    str(HOME / 'plugins/ultra-deep-research/src')]
from hermes_foundation_bridge.bridge import services
from local_beads import LocalBeadsAdapter as BeadsAdapter
from portable_reads import compare_rates, read_page, report_from_file
from hermes_foundation_bridge.agentmemory_adapter import AgentMemoryAdapter
from hermes_foundation_bridge.graphiti_adapter import GraphitiAdapter
from hermes_foundation_bridge.research_session import ResearchSession
from hermes_foundation_bridge.research_lifecycle import complete
from hermes_foundation_bridge.canonical import sha256_json
from hermes_foundation_bridge.fragments import record_fragment
from hermes_research_report.research_workspace import workspace, source, note, finish, root_for, write_json
from hermes_research_report.research_modes import instructions

def canonical(v):
    return json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()

def digest(v):
    return hashlib.sha256(v.encode() if isinstance(v, str) else v).hexdigest()

def db():
    c = sqlite3.connect(HERE / 'host-state.sqlite', timeout=5)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA journal_mode=WAL')
    c.execute('CREATE TABLE IF NOT EXISTS sessions (sid TEXT PRIMARY KEY, body TEXT NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS attachments (sid TEXT, path TEXT, body TEXT, PRIMARY KEY(sid,path))')
    c.execute('CREATE TABLE IF NOT EXISTS research_runs (run_id TEXT PRIMARY KEY, original_sid TEXT NOT NULL, current_sid TEXT NOT NULL, body TEXT NOT NULL, revision INTEGER NOT NULL)')
    c.execute("INSERT OR IGNORE INTO research_runs SELECT json_extract(body,'$.run_id'),sid,sid,body,1 FROM sessions WHERE json_extract(body,'$.run_id') IS NOT NULL AND COALESCE(json_extract(body,'$.native_child'),0)=0")
    c.commit()
    return c

def saved(sid):
    with db() as c:
        r = c.execute('SELECT body FROM sessions WHERE sid=?', (sid,)).fetchone()
        body=json.loads(r[0]) if r else None
        if body and body.get('run_id') and not body.get('native_child'):
            run=c.execute('SELECT * FROM research_runs WHERE run_id=?',(body['run_id'],)).fetchone()
            if run:
                body=json.loads(run['body']);body['registry_revision']=run['revision'];body['original_native_sid']=run['original_sid']
                if run['current_sid']!=sid:body['phase']='detached';body['attached_native_sid']=run['current_sid']
    return body

def save(sid, body):
    with db() as c:
        c.execute('BEGIN IMMEDIATE')
        if body.get('run_id') and not body.get('native_child'):
            old=c.execute('SELECT * FROM research_runs WHERE run_id=?',(body['run_id'],)).fetchone()
            if old and body.get('registry_revision',old['revision'])!=old['revision']:raise ValueError('research_registry_revision_conflict')
            next_revision=old['revision']+1 if old else 1
            clean={k:v for k,v in body.items() if k not in {'registry_revision','attached_native_sid'}}
            c.execute('INSERT INTO research_runs VALUES(?,?,?,?,?) ON CONFLICT(run_id) DO UPDATE SET current_sid=excluded.current_sid,body=excluded.body,revision=research_runs.revision+1',
                (body['run_id'],old['original_sid'] if old else sid,sid,json.dumps(clean,ensure_ascii=False),1))
        c.execute('INSERT INTO sessions VALUES (?,?) ON CONFLICT(sid) DO UPDATE SET body=excluded.body',
            (sid, json.dumps(body, ensure_ascii=False)))

    if body.get('run_id') and not body.get('native_child'):body['registry_revision']=next_revision

def research_list(sid):
    current=saved(sid)
    if current and current.get('native_child'):raise PermissionError('root_research_registry_required')
    with db() as c:rows=c.execute('SELECT run_id,original_sid,current_sid,body,revision FROM research_runs ORDER BY rowid DESC').fetchall()
    return {'researches':[{'run_id':r['run_id'],'question':json.loads(r['body']).get('question'),
        'phase':json.loads(r['body']).get('phase'),'bead_id':json.loads(r['body']).get('bead_id'),
        'revision':r['revision'],'attached_to_current_session':r['current_sid']==sid} for r in rows]}

def resume_research(sid,run_id):
    current=saved(sid)
    if current and (current.get('native_child') or current.get('phase')=='running' and current.get('run_id')!=run_id):raise PermissionError('current_research_must_be_preserved')
    with db() as c:row=c.execute('SELECT * FROM research_runs WHERE run_id=?',(run_id,)).fetchone()
    if not row:raise ValueError('research_run_not_found')
    if row['current_sid']==sid:return saved(sid)
    origin=row['current_sid'];body=json.loads(row['body']);body['registry_revision']=row['revision']
    if body['phase']=='running':
        from lease_resume import prepare_turn,reconcile_workers
        prepare_turn(origin);body=saved(origin)
        reconcile_workers(body,allow_live=False)
    body['original_native_sid']=row['original_sid'];body['previous_native_sid']=origin
    save(sid,body)
    return saved(sid)

def put(state, body, project, oid, run):
    q = {'schema_version': 1, 'database': 'kw_core', 'project_id': project, 'object_id': oid}
    old = state.get(q)
    r = state.put({**q, 'expected_revision': old['object_ref']['revision'] if old['status'] == 'found' else 0,
        'schema_id': body['contract'], 'object': body, 'content_hash': sha256_json(body),
        'operation_id': oid + '-' + sha256_json(body)[:16], 'run_id': run})
    if r['status'] not in ('committed', 'no_op'):
        raise RuntimeError('canonical_write_failed')
    return r

def adapters():
    root = HOME / 'foundation'
    runtime, artifacts, state = services(root)
    return runtime, artifacts, state, BeadsAdapter(root), AgentMemoryAdapter(root), GraphitiAdapter(root)

def session(body):
    runtime, artifacts, state, beads, memory, graph = adapters()
    s = ResearchSession(state, runtime, beads, memory, graph,
        project_id=body['project'], profile_id='hermes-bn', host_run_id=body['host_run'],
        work_contract_ref=body['work_ref'], holder_id=body['holder'])
    s.restore(body['binding'])
    return s, artifacts

def document_store():
    config=ROOT.parent/'Hermes BN/Memory/settings.json'
    settings=json.loads(config.read_text())
    sys.path.insert(0,settings['package_root'])
    from bn_memory.broker import Broker
    from bn_memory.documents import Documents
    return Documents(Broker(settings))

def bind_document_corpus_by_operator(sid,corpus_id,reason,expected_previous=None):
    # Operator-only additive binding of a real registered corpus, never a model bypass.
    if not isinstance(reason,str) or not reason.strip():raise ValueError('operator_corpus_binding_reason_required')
    body=saved(sid)
    if not body or body.get('native_child') or body.get('phase')!='running':raise PermissionError('active_root_research_required')
    check(sid);body=saved(sid)
    if not body or body.get('phase')!='running' or body.get('native_child'):raise PermissionError('research_changed_during_corpus_binding')
    docs=document_store();corpus=docs.corpus(sid,corpus_id);phases=set(json.loads(corpus['phases']))
    if not {'plan','collect','analyse','verify','report'}<=phases:raise ValueError('all_UDR_document_phases_required')
    previous=body.get('corpus_id')
    if previous==corpus_id:return {'run_id':body['run_id'],'corpus_id':corpus_id,'idempotent':True}
    if previous!=expected_previous:raise PermissionError('document_corpus_binding_revision_changed')
    with docs.store.db() as db:
        columns={row[1] for row in db.execute('PRAGMA table_info(document_sources)')}
        if not {'corpus','path','sha256'}<=columns:raise PermissionError('unsupported_document_binding_schema')
        current={(r[0],r[1]) for r in db.execute('SELECT path,sha256 FROM document_sources WHERE corpus=?',(corpus_id,))}
        if not current or any(not digest_value for _,digest_value in current):raise ValueError('complete_original_snapshot_required')
        if previous:
            old=docs.corpus(sid,previous);original={(r[0],r[1]) for r in db.execute('SELECT path,sha256 FROM document_sources WHERE corpus=?',(previous,))}
            if not original<=current or not set(json.loads(old['phases']))<=phases:raise PermissionError('required_originals_or_phases_cannot_be_dropped')
    event={'previous':previous,'corpus_id':corpus_id,'reason':reason,'sources':len(current),'inventory_sha256':digest(canonical(sorted(current))),'at':time.time(),'budget_reset':False}
    body.setdefault('document_corpus_history',[]).append(event);body.update(corpus_id=corpus_id,document_phase='plan');save(sid,body)
    return {'run_id':body['run_id'],**event}

def continuity_policy(body,sid):
    return {'contract':'ResearchContinuityPolicyV1','run_id':body['run_id'],
        'bead_id':body['bead_id'],'native_session_id':sid,
        'maximum_idle_seconds':None,'auto_close_on_idle':False,'auto_delete_on_idle':False,
        'resume_transport':'versioned_run_registry','resume_command':'udr_research action=resume run_id='+body['run_id'],
        'lease_is_execution_authority_not_research_lifetime':True,
        'completed_products_are_not_automatically_repeated':True}

def pin_continuity(sid):
    body=saved(sid)
    if not body or body.get('native_child') or body.get('phase')!='running':return
    policy=continuity_policy(body,sid)
    if body.get('continuity')==policy:return
    check(sid)
    _,_,state,*_=adapters();ref='BNCN-'+digest(body['host_run'])[:24]
    put(state,policy,body['project'],ref,body['host_run'])
    body=saved(sid);body.update(continuity=policy,continuity_ref=ref);save(sid,body)

def start(sid, request):
    if request.get('corpus_id'):
        corpus=document_store().corpus(sid,request['corpus_id'])
        if not {'plan','collect','analyse','verify','report'}<=set(json.loads(corpus['phases'])):raise ValueError('udr_corpus_requires_all_five_phases')
    old = saved(sid)
    rid = request['request_id']
    if old and old['request_id'] == rid:
        if old['question'] != request['question'] or old['mode'] != request.get('mode', 'research'):
            raise ValueError('idempotency_input_conflict')
        return old
    if old and old['phase'] == 'running':
        raise ValueError('active_work_requires_finish_or_stop')
    runtime, artifacts, state, beads, memory, graph = adapters()
    key = digest(sid + ':' + rid)[:24]
    project, host, holder = 'BN-' + key, 'BNH-' + key, 'BN-host-' + key
    issue = beads.create({'schema_version': 1, 'title': ('Hermes BN: ' + request['question'])[:160],
        'description': 'Managed research; BN host identity ' + digest(sid), 'priority': 2,
        'issue_type': 'task', 'operation_key': host})['issue_id']
    beads.claim({'schema_version': 1, 'issue_id': issue, 'worker_id': holder})
    lease = runtime.acquire_lease({'schema_version': 1, 'work_id': issue, 'holder_id': holder,
        'expected_revision': 1, 'ttl_seconds': 7200})
    if lease['status'] != 'acquired':
        raise RuntimeError('lease_not_acquired')
    work = {'contract': 'ResearchWorkContractV1', 'status': 'active', 'project_id': project,
        'profile_id': 'hermes-bn', 'host_run_id': host, 'holder_id': holder, 'bead_id': issue,
        'lease_revision': 1, 'memory_scope': {'tenant_id': 'BN-owner', 'project_id': project,
            'profile_id': 'hermes-bn', 'work_kind': 'research'}}
    ref = 'BNW-' + key
    put(state, work, project, ref, host)
    s = ResearchSession(state, runtime, beads, memory, graph, project_id=project,
        profile_id='hermes-bn', host_run_id=host, work_contract_ref=ref, holder_id=holder)
    ctx = s.prepare(request['question'])
    result = workspace({'action': 'start', 'question': request['question'],
        'mode': request.get('mode', 'research'), 'host_context': ctx['host_context']})
    context = json.dumps({'memory': ctx['memory_context'], 'graph': ctx['graph_results']}, ensure_ascii=False)
    body = {'phase': 'running', 'question': request['question'], 'mode': request.get('mode', 'research'),
        'request_id': rid, 'project': project, 'host_run': host, 'holder': holder,
        'work_ref': ref, 'binding': ctx['host_context'], 'run_id': result['run_id'], 'bead_id': issue,
        'context': '<UDR_REQUIRED_CONTEXT sha256="' + digest(context) + '">\n' + context + '\n</UDR_REQUIRED_CONTEXT>',
        'depth': instructions(request.get('mode', 'research')), 'admission_ref': ctx['admission_ref'],
        'context_delivered': False, 'completion': None, 'claims_accepted': False, 'delivery_authorized': False}
    if request.get('corpus_id'):
        body.update(corpus_id=request['corpus_id'],document_phase='collect')
    save(sid, body)
    with db() as c:
        incoming = c.execute('SELECT body FROM attachments WHERE sid=?', (sid,)).fetchall()
    body['incoming_documents'] = [json.loads(row[0]) for row in incoming]
    save(sid, body)
    pin_continuity(sid)
    return saved(sid)

def attachment(sid, path):
    p=Path(path);cache=ROOT.parent/'Hermes BN/data/cache/documents'
    if p.is_symlink() or not p.resolve().is_relative_to(cache.resolve()) or not p.is_file():raise PermissionError('native_document_cache_required')
    st=p.stat();body={'file_stat':[st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns,st.st_ctime_ns],'sha256':None,'content_hash_pending':True,'path':str(p),'filename':p.name,'bytes':st.st_size,'mtime_ns':st.st_mtime_ns,'status':'awaiting_addressed_corpus',
      'corpus_path':'attachment:'+str(p.relative_to(cache)),'full_original_ingested':False,'reading_level':'metadata_only','text':'','source_truth_verified':False}
    with db() as c:c.execute('INSERT INTO attachments VALUES(?,?,?) ON CONFLICT(sid,path) DO UPDATE SET body=excluded.body',(sid,str(p),json.dumps(body,ensure_ascii=False)))
    return body

def active_lease_heartbeat(body,session):
    # Lease authority was checked immediately before this call. A throttle is
    # operational metadata, not a research-registry revision or a new grant.
    import fcntl
    directory=ROOT/'state/bn-bridge-heartbeats';directory.mkdir(mode=0o700,exist_ok=True)
    key=digest(body['run_id']);path=directory/(key+'.json');lock=directory/(key+'.lock')
    with lock.open('a') as handle:
        lock.chmod(0o600);fcntl.flock(handle,fcntl.LOCK_EX)
        old=json.loads(path.read_text()) if path.exists() else {}
        identity={'run_id':body['run_id'],'holder':body['holder'],'lease_ref':body['binding']['lease_ref']}
        if all(old.get(k)==value for k,value in identity.items()) and 0<=time.time()-old.get('at',0)<300:return
        work=session._work()
        heartbeat=session.runtime.acquire_lease({'schema_version':1,'work_id':body['bead_id'],'holder_id':body['holder'],'expected_revision':work['lease_revision'],'ttl_seconds':7200})
        if heartbeat['status']!='idempotent_active' or heartbeat['current_revision']!=work['lease_revision']:raise PermissionError('research_lease_changed_during_heartbeat')
        temporary=path.with_suffix('.tmp');temporary.write_bytes(canonical({**identity,'at':time.time()}));temporary.chmod(0o600);temporary.replace(path)

def check(sid):
    body = saved(sid)
    if body and body.get('managed_worker'):
        import team_backend
        return team_backend.check(sid)
    if body and body.get('native_child'):
        if not body.get('requires_udr'):return {'status':'idle','native_child':True}
        parent=saved(body['parent_sid'])
        if not parent or parent['phase']!='running':raise PermissionError('parent_research_no_longer_active')
        s,_=session(parent);s.check()
        return {'status':'active','context':parent['context'],'run_id':parent['run_id'],'native_child':True}
    if not body or body['phase'] != 'running':
        return {'status': 'idle', 'body': body}
    s, _ = session(body)
    s.check()
    # Active native work renews its existing ownership lease; an expired or
    # conflicting lease fails above and is never silently reacquired here.
    active_lease_heartbeat(body,s)
    return {'status': 'active', 'context': body['context'], 'run_id': body['run_id'],'continuity_origin_sid':body.get('original_native_sid',sid)}

def capture(sid, event):
    body = saved(sid)
    if body and body.get('managed_worker'):
        import team_backend
        return team_backend.evidence(sid,event)
    if not body or body['phase'] != 'running':
        return {'status': 'inactive'}
    s, _ = session(body)
    s.check()
    text = event['text']
    # No credential value is ever retained in the research corpus.
    import re
    if re.search(r'(?i)(?:(?<![A-Za-z0-9_-])sk-[A-Za-z0-9_-]{20,}|Bearer\s+[A-Za-z0-9_-]{16,}|[0-9]{8,}:[A-Za-z0-9_-]{30,})', text):
        raise ValueError('sensitive_tool_output_refused')
    key = digest(canonical(event))
    path = root_for(body['run_id']) / 'host-fragments'
    path.mkdir(exist_ok=True, mode=0o700)
    dest = path / (key + '.txt')
    if not dest.exists():
        dest.write_text(text); dest.chmod(0o600)
    receipts = []
    # Retain all bytes, split ledger chunks rather than clip obligatory content.
    for i, offset in enumerate(range(0, len(text), 64000)):
        part = text[offset:offset + 64000]
        fid = 'BNF-' + key[:24] + '-' + str(i)
        f = {'fragment_id': fid, 'run_id': body['host_run'], 'source_system': event.get('family', 'tool'),
            'source_ref': event.get('source_ref', 'native-tool-return:' + event['tool']),
            'source_version': event.get('source_version', key),
            'locator': f'host-fragments/{key}.txt#chars={offset}:{offset+len(part)}',
            'exact_fragment': part, 'content_hash': digest(part), 'transformation_refs': [],
            'retrieval_query': event.get('query', ''), 'rank_or_score': None}
        receipts.append(record_fragment({'schema_version': 1, 'event_key': fid, 'fragment': f}, s.runtime))
    write_json(path / (key + '.json'), {'tool': event['tool'], 'sha256': digest(text),
        'reading_level': event.get('reading_level', 'tool_return_only'), 'receipts': receipts,
        'claims_accepted': False, 'original_source_read': False})
    return {'status': 'recorded', 'sha256': digest(text), 'chunks': len(receipts), 'path': str(dest)}

def research(sid, request):
    action = request.get('action')
    if action=='list':return research_list(sid)
    if action=='resume':return resume_research(sid,request['run_id'])
    if (saved(sid) or {}).get('native_child') and action not in {'status','read'}:
        raise PermissionError('native_research_child_is_read_only')
    if action == 'start':
        return start(sid, request)
    if action == 'status':
        body=saved(sid)
        if body and not body.get('native_child'):
            return {**body,'continuity':continuity_policy(body,sid)}
        return body or {'phase':'idle'}
    body = saved(sid)
    if not body:
        raise ValueError('research_not_started')
    if body.get('native_child'):
        if action!='status' and action!='read':raise PermissionError('native_research_child_is_read_only')
        parent=saved(body['parent_sid'])
        if not parent:raise PermissionError('parent_research_missing')
        body=parent
    if action == 'adopt_file':
        from prepared_file import adopt
        return adopt(sid, request['run_id'], request['source_path'], request['expected_sha256'])
    if action == 'finish' and 'report_path' in request:
        request=report_from_file(root_for(body['run_id']),request)
    if action == 'read':
        from urllib.parse import quote
        authority=check(sid)
        rel=request['path']
        page=read_page(root_for(body['run_id']),rel,request.get('offset',0),request.get('max_chars',4096))
        if authority.get('managed_worker') and authority.get('read_sha256',{}).get(rel)!=page['sha256']:raise PermissionError('assigned_input_version_changed')
        source_ref='https://local.invalid/bn-udr/'+body['run_id']+'/'+quote(rel,safe='/')
        provenance=capture(sid,{'tool':'udr_workspace_read','family':'file','source_ref':source_ref,
            'source_version':page['sha256'],'text':page['text'],'reading_level':'exact_preserved_text_page'})
        return {**page,'source_ref':source_ref,'capture_receipt':provenance}
    if body['phase'] != 'running':
        if action == 'finish' and body['completion']:
            incoming={k:v for k,v in request.items() if k!='action'}
            incoming['run_id']=body['run_id']
            if sha256_json(incoming)!=body.get('finish_request_hash'):
                raise ValueError('finish_retry_requires_identical_report')
            return body['completion']
        raise ValueError('work_not_running')
    s, artifacts = session(body)
    s.check()
    if action=='phase':
        phase=request['phase']
        if phase not in {'plan','collect','analyse','verify','report'}:raise ValueError('invalid_document_phase')
        body['document_phase']=phase;save(sid,body);return {'phase':phase,'corpus_id':body.get('corpus_id'),'scope_preserved':True}
    if action=='finish' and body.get('corpus_id') and request.get('status')=='complete':
        coverage=document_store().status(sid,{'corpus_id':body['corpus_id']})
        if not coverage['model_delivery_complete']:raise ValueError('required_document_coverage_incomplete:'+json.dumps(coverage['phases']))
    args = {k: v for k, v in request.items() if k != 'action'}
    args['run_id'] = body['run_id']
    if action=='finish':
        import team_backend
        team_backend.assert_finishable(sid,allow_partial=request.get('status')=='partial')
    if action == 'source':
        result = source(args)
        capture(sid, {'tool': 'research_source', 'family': 'web', 'source_ref': args['url'],
            'source_version': result['sha256'], 'text': Path(result['path']).read_text(),
            'reading_level': args['extent']})
        return result
    if action == 'document':
        documents = body.get('incoming_documents', [])
        item = documents[request.get('index', 0)]
        if item.get('status')=='awaiting_addressed_corpus':
            return {**item,'next':'document_catalogue(path=corpus_path), then document_extract and addressed document_read; attach corpus_id to the research; extraction is not model reading'}
        if item['text'] is None: raise ValueError('document_parser_unavailable')
        result = source({'run_id': body['run_id'], 'url': 'https://local.invalid/bn-inbound/'+item['sha256'],
            'title': 'Owner-provided local document (not a web page)', 'text': item['text'],
            'extent': 'full_text', 'origin_ref': item['artifact']['artifact_id']})
        capture(sid, {'tool': 'document', 'family': 'file', 'source_ref': item['artifact']['artifact_id'],
            'source_version': item['sha256'], 'text': item['text'], 'reading_level': 'extracted_local_text'})
        return result
    if action == 'note':
        return note(args)
    if action == 'plan':
        from hermes_research_report.research_modes import profile
        # SDK inspects the plan before attaching the run's depth profile. Supply
        # that exact canonical profile up front, so Search does not inherit the
        # deeper default requirements and provoke repeated ceremonial planning.
        if not isinstance(args.get('plan'),dict):raise ValueError('plan must be an object')
        args['plan']={**args['plan'],'mode':body['mode'],'depth_profile':profile(body['mode'])}
        return workspace({'action': 'plan', **args})
    if action == 'method':
        from hermes_research_report.research_methods import method
        args['action'] = args.pop('method_action', 'catalogue')
        args.pop('run_id', None)
        return method(args)
    if action in {'fetch','parse','intake'}:
        from parser_intake import web_step,document_step
        config=json.loads((ROOT.parent/'Hermes BN/Memory/settings.json').read_text())
        sys.path.insert(0,config['package_root'])
        if action=='intake':return document_step(sid,body,args,document_store(),put,s.state,source,root_for)
        if action=='fetch':
            from hermes_research_report.research_fetch import fetch
            from hermes_research_report.research_integration import settings as intake_settings
            if intake_settings()['integration_mode']!='foundation':raise PermissionError('safe_host_intake_requires_foundation_mode')
            acquired=fetch(args);args['retrieval_id']=Path(acquired['original_path']).parent.name
        return web_step(sid,body,args,artifacts,put,s.state,source,root_for,config)
    if action == 'compare':
        from hermes_research_report.comparison import compare_periods
        return compare_periods(args['observations'],args['before'],args['after'])
    if action == 'build_report':
        from hermes_research_report.report import build_report
        return build_report(request['input'])
    if action == 'workspace':
        args['action']=args.pop('workspace_action','status')
        if args['action']=='start':raise PermissionError('host_admission_required')
        return workspace(args)
    if action == 'finish':
        request_hash = sha256_json(args)
        if body.get('finish_request_hash') not in (None, request_hash):
            # An invalid/unpublished request may be corrected. Once SDK intake has
            # prepared an immutable package, its bytes must remain identical.
            lifecycle = 'RLC-'+sha256_json({'host':body['binding'],'run_id':body['run_id']})[:24]
            frozen = s.state.get({'schema_version':1,'database':'kw_context','project_id':body['project'],'object_id':lifecycle})
            if body.get('finish_locked') or frozen['status']=='found':
                raise ValueError('finish_retry_requires_identical_report')
        result = finish(args)
        if result['status'] != 'complete' or result['structural_citation_check'] != 'pass':
            return result
        body['finish_request_hash'], body['finish_locked'] = request_hash, True
        save(sid, body)
        completion = complete(s, artifacts, body['run_id'])
        body['completion'], body['phase'] = completion, 'draft'
        save(sid, body)
        return {**result, **completion}
    if action == 'stop':
        body['phase'] = 'stopped'; save(sid, body)
        return {'phase': 'stopped', 'materials_preserved': True}
    raise ValueError('unsupported_action')

def recall(sid, request):
    body = saved(sid)
    if not body:
        raise ValueError('project_scope_required')
    runtime, _, state, _, memory, graph = adapters()
    work = state.get({'schema_version': 1, 'database': 'kw_core', 'project_id': body['project'],
        'object_id': body['work_ref']})['object']
    query = request['query']
    result = {'memory': memory.context({'schema_version': 1, 'scope': work['memory_scope'], 'query': query, 'limit': 5}),
        'graph': graph.search({'schema_version': 1, 'project_id': body['project'], 'query': query, 'limit': 5})}
    from hermes_foundation_bridge.zvec_index import ZvecIndexer
    result['zvec'] = ZvecIndexer(HOME / 'foundation').query({'schema_version': 1, 'query': query, 'limit': 3})
    for family, value in result.items():
        capture(sid, {'family': {'memory': 'agentmemory', 'graph': 'graphiti', 'zvec': 'zvec'}[family],
            'tool': 'udr_recall_' + family, 'text': json.dumps(value, ensure_ascii=False), 'query': query})
    return result

def verify_host(name, args):
    args = dict(args); host = args.pop('_host', None)
    if not isinstance(host, dict) or set(host) != {'sid', 'expires', 'signature'}:
        raise PermissionError('trusted_host_identity_required')
    signed = {'tool': name, 'args': args, 'sid': host['sid'], 'expires': host['expires']}
    key = (ROOT / 'state/authority/bn-bridge.key').read_bytes()
    expected = hmac.new(key, canonical(signed), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, host['signature']) or not time.time() <= host['expires'] <= time.time() + 120:
        raise PermissionError('forged_or_expired_host_identity')
    return host['sid'], args

def dispatch(name, args):
    sid, clean = verify_host(name, args)
    if name == 'udr_research':
        return research(sid, clean['request'])
    if name == 'udr_workspace':
        return research(sid,{**clean['request'],'action':'read'})
    if name == 'udr_compare_rates':
        if set(clean)!={'before','after'}:raise ValueError('only_before_after_allowed')
        return compare_rates(clean['before'],clean['after'])
    if name == 'udr_recall':
        return recall(sid, clean)
    if name == 'udr_status':
        from hermes_foundation_bridge.bridge import health
        acceptance=HERE/'production-acceptance.json'
        verdict=json.loads(acceptance.read_text()) if acceptance.exists() else {'status':'not_accepted','production_activation_allowed':False}
        return {'host_session': digest(sid), 'state': saved(sid), 'health': health({'schema_version': 1}),
            'instance_acceptance':{'status':verdict['status'],'scope':verdict.get('scope'),
                'production_activation_allowed':verdict['production_activation_allowed'],
                'scientific_universal_acceptance':False}}
    raise ValueError('unknown_tool')

def rpc(data):
    op, sid = data['operation'], data.get('sid', '')
    if op=='deliver_report':
        from report_delivery import deliver
        return deliver(sid,data['run_id'],data['expected_sha256'],data['grant_id'],data.get('artifact_id'))
    if op=='document_phase':
        body=saved(sid);authority=check(sid)
        if body and body.get('managed_worker'):return {'phase':authority['document_phase'],'corpus_id':authority.get('corpus_id')}
        if body and body.get('native_child'):body=saved(body['parent_sid'])
        return {'phase':body.get('document_phase') if body else None,'corpus_id':body.get('corpus_id') if body else None}
    if op == 'team':
        import team_backend
        return team_backend.rpc(sid,{k:v for k,v in data.items() if k not in {'operation','sid'}})
    if op == 'prepare_turn':
        from lease_resume import prepare_turn
        return prepare_turn(sid)
    if op == 'check':
        return check(sid)
    if op == 'bind_child':
        parent=data['parent_sid'];body=saved(parent)
        previous=saved(sid)
        if previous and previous.get('parent_sid') not in (None,parent):raise PermissionError('child_parent_changed')
        if previous and previous.get('managed_worker'):
            return check(sid)
        save(sid,{'phase':'child','native_child':True,'parent_sid':parent,
            'requires_udr':bool(body and body.get('phase')=='running')})
        return check(sid)
    if op == 'capture':
        return capture(sid, data['event'])
    if op == 'delivered':
        body = saved(sid)
        child=bool(body and body.get('native_child'))
        if child:body=saved(body['parent_sid'])
        if body and body['phase'] == 'running':
            if not child:body['context_delivered'] = True; save(sid, body)
            _, _, state, *_ = adapters()
            put(state, {'contract': 'ResearchContextDeliveryV1', 'run_id': body['run_id'],
                'host_context': body['binding'], 'context_sha256': digest(body['context']),
                'final_provider_arguments_verified': True, 'meaning_verified': False,'native_session_hash':digest(sid),
                'native_child':child},
                body['project'], 'BNCD-' + digest(body['run_id']+sid)[:24], body['host_run'])
        return {'status': 'recorded'}
    if op == 'dispatch':
        return dispatch(data['tool'], data['args'])
    if op == 'attachment':
        result = attachment(sid, data['path'])
        return {k:v for k,v in result.items() if k != 'text'}
    if op == 'attachment_check':
        with db() as c:
            old = c.execute('SELECT body FROM attachments WHERE sid=? AND path=?', (sid,data['path'])).fetchone()
        if not old: raise PermissionError('original_not_registered')
        result = json.loads(old[0])
        p=Path(data['path']);cache=ROOT.parent/'Hermes BN/data/cache/documents'
        if p.is_symlink() or not p.resolve().is_relative_to(cache.resolve()) or not p.is_file():raise PermissionError('native_document_cache_required')
        st=p.stat();current=[st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns,st.st_ctime_ns]
        if result.get('content_hash_pending'):
            if current!=result.get('file_stat'):raise PermissionError('original_changed_before_immutable_intake')
            return {'status':'verified_acquisition_metadata_only','sha256':None,'content_hash_checked':False,'next':'document_catalogue creates the immutable hashed original; only isolated document_read material may reach a model'}
        from parser_intake import digest as file_digest
        if file_digest(p)!=result['sha256']:raise PermissionError('original_changed')
        return {'status':'verified','sha256':result['sha256'],'content_hash_checked':True}
    if op == 'trace':
        body = saved(sid)
        if body and body.get('native_child'):body=saved(body['parent_sid'])
        if not body: return {'status': 'inactive'}
        from hermes_foundation_bridge.observability import ObservabilityService
        event = data['event']
        return ObservabilityService(HOME / 'foundation').record({'schema_version':1,
            'trace_id':'BNT-'+digest(event['id'])[:24], 'project_id':body['project'],
            'run_id':body['host_run'], 'bead_id':body['bead_id'], 'profile_id':'hermes-bn',
            'session_hash':digest(sid), 'operation_id':'BNO-'+digest(event['id'])[:24], 'attempt':1,
            'model_ref':event.get('model') or 'gpt-6.1-sol', 'tool_ref':event.get('tool'),
            'context_refs':[body['admission_ref']], 'evidence_link_refs':[], 'commit_refs':[],
            'latency_ms':event['latency_ms'], 'cost_microunits':0,
            'outcome_status':'failed' if event.get('error') else 'success', 'priority':'P0',
            'collector_available':True, 'sampling_decision':'keep', 'ttl_seconds':3600,
            'attributes':{'provider':'openai-codex','reasoning':data['event'].get('reasoning'),'billing':'ChatGPT subscription; API cash charge not reported',
                'raw_contents_logged':False,'latency_available':event['latency_available'],
                'backfilled_from_native_logger':event.get('backfilled',False)}})
    raise ValueError('unknown_rpc')

if __name__ == '__main__':
    try:
        print(json.dumps(rpc(json.load(sys.stdin)), ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({'error': type(exc).__name__, 'code': getattr(exc, 'code', str(exc))}, ensure_ascii=False))
        sys.exit(1)
