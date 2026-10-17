"""A fresh native root turn can renew its expired, unchanged UDR ownership.

The pinned Foundation SDK does not expose why a lease is inactive. An explicit
read-only schema adapter distinguishes expiry from release/ownership change;
all writes still use the SDK and canonical compare-and-swap.
"""
import contextlib,fcntl,json,sqlite3,time
from datetime import datetime,timezone
import backend as b

def lease_snapshot(runtime,work_id):
 path=runtime.database
 if path.is_symlink() or not path.is_file():raise PermissionError('lease_snapshot_unavailable')
 with contextlib.closing(sqlite3.connect(path.as_uri()+'?mode=ro',uri=True,timeout=5)) as db:
  db.row_factory=sqlite3.Row
  row=db.execute('SELECT holder_id,revision,status,expires_at FROM leases WHERE work_id=?',(work_id,)).fetchone()
 if not row:raise PermissionError('lease_snapshot_missing')
 return dict(row)

def owned_work(body,stored,issue,lease):
 work=stored.get('object',{})
 expected={'contract':'ResearchWorkContractV1','status':'active','project_id':body['project'],'profile_id':'hermes-bn','host_run_id':body['host_run'],'holder_id':body['holder'],'bead_id':body['bead_id']}
 scope=work.get('memory_scope',{})
 if stored.get('status')!='found' or stored.get('object_ref',{}).get('schema_id')!='ResearchWorkContractV1' or any(work.get(k)!=v for k,v in expected.items()) or scope.get('project_id')!=body['project'] or scope.get('profile_id')!='hermes-bn':raise PermissionError('resume_work_or_scope_changed')
 if issue.get('id')!=body['bead_id'] or issue.get('status')!='in_progress' or issue.get('assignee')!=body['holder']:raise PermissionError('resume_bead_ownership_changed')
 if lease.get('holder_id')!=body['holder'] or lease.get('revision')!=work['lease_revision'] or lease.get('status')!='active':raise PermissionError('resume_lease_ownership_changed')
 if datetime.fromisoformat(lease['expires_at'])>datetime.now(timezone.utc):raise PermissionError('resume_requires_actual_expiry')
 return work

def reconcile_workers(body,allow_live=False):
 from team_backend import load,save,locked
 import psutil
 root=b.root_for(body['run_id'])/'teams';changes=[]
 if not root.exists():return changes
 for path in root.glob('*.json'):
  with locked(path):
   wave=load(path)
   for task in wave['tasks'].values():
    pending=task['state'] in {'launch_reserved','running','product_saved'} or (task.get('receipt') or {}).get('terminal_state')=='UNKNOWN'
    if not pending or task.get('recovery',{}).get('local_executor_gone'):continue
    rules=task.get('input',{}).get('mandatory_rules',[])
    if not {'read_only','no_delegation','no_external_delivery'}<=set(rules):raise PermissionError('recovery_requires_readonly_worker_contract')
    owner=task.get('executor_owner');started=task.get('started_at',0)
    gone=bool(started and started<psutil.boot_time())
    if owner:
     try:gone=abs(psutil.Process(owner['pid']).create_time()-owner['created_at'])>0.01
     except psutil.NoSuchProcess:gone=True
    if not gone:raise PermissionError('resume_workers_require_reconciliation')
    proof={'local_executor_gone':True,'basis':'recorded_process_identity_or_previous_os_boot','at':time.time(),'external_outcome':'unknown','product_accepted':False,'automatic_replay':False}
    _,_,_,beads,_,_=b.adapters()
    beads._run(['update',task['bead_id'],'--status','blocked','--append-notes','Recovery: local executor is gone; partial evidence retained; external outcome unknown; no automatic replay'],actor='bn-udr-recovery')
    task.update(state='blocked',recovery=proof,error='local_executor_gone_no_automatic_replay');save(path,wave);changes.append(task['id'])
 return changes

def _prepare_turn(sid):
 body=b.saved(sid)
 if not body or body.get('phase')!='running':return b.check(sid)
 if body.get('native_child'):return b.check(sid)
 lock=b.HERE/('resume-'+b.digest(body['run_id'])+'.lock')
 with open(lock,'a') as f:
  lock.chmod(0o600);fcntl.flock(f,fcntl.LOCK_EX)
  try:return b.check(sid)
  except Exception as exc:
   if getattr(exc,'code',None) not in {'research_lease_inactive','research_context_mismatch','research_admission_missing','research_work_changed'}:raise
  body=b.saved(sid);runtime,artifacts,state,beads,memory,graph=b.adapters()
  q={'schema_version':1,'database':'kw_core','project_id':body['project'],'object_id':body['work_ref']};stored=state.get(q)
  issue=beads.get({'schema_version':1,'issue_id':body['bead_id']})['issue'];current=lease_snapshot(runtime,body['bead_id']);work=stored.get('object',{})
  expected={'contract':'ResearchWorkContractV1','status':'active','project_id':body['project'],'profile_id':'hermes-bn','host_run_id':body['host_run'],'holder_id':body['holder'],'bead_id':body['bead_id']}
  if stored.get('status')!='found' or stored.get('object_ref',{}).get('schema_id')!='ResearchWorkContractV1' or any(work.get(k)!=v for k,v in expected.items()):raise PermissionError('resume_work_or_scope_changed')
  if issue.get('status')!='in_progress' or issue.get('assignee')!=body['holder'] or issue.get('id')!=body['bead_id']:raise PermissionError('resume_bead_ownership_changed')
  if current.get('holder_id')!=body['holder'] or current.get('status')!='active' or current.get('revision') not in {work['lease_revision'],work['lease_revision']+1}:raise PermissionError('resume_lease_ownership_changed')
  binding=body['binding'];old_revision=int(binding['lease_ref'].rsplit(':',1)[1]);old_work={**work,'lease_revision':old_revision}
  admission=state.get({'schema_version':1,'database':'kw_context','project_id':body['project'],'object_id':'RAD-'+b.sha256_json(binding)[:24]})
  if admission.get('status')!='found' or admission.get('object_ref',{}).get('schema_id')!='ResearchAdmissionV1' or admission.get('object',{}).get('host_context')!=binding or admission['object'].get('work_contract_sha256')!=b.sha256_json(old_work):raise PermissionError('resume_previous_admission_changed')
  if old_revision!=work['lease_revision'] or current['revision']!=work['lease_revision']:
   previous=b.HERE/('resume-'+b.digest(sid)+'-'+str(old_revision)+'.json')
   if not previous.is_file() or previous.is_symlink():raise PermissionError('resume_transition_journal_required')
   prior=json.loads(previous.read_text())
   if prior.get('bead_id')!=body['bead_id'] or prior.get('run_id')!=body['run_id'] or prior.get('old_lease',{}).get('revision')!=old_revision:raise PermissionError('resume_transition_journal_mismatch')
  recovered=reconcile_workers(body)
  event={'trigger':'fresh_native_root_turn','bead_id':body['bead_id'],'run_id':body['run_id'],'old_lease':{**current,'revision':old_revision},'same_holder':True,'same_scope':True,'new_research':False,'at':time.time(),'stage':'validated','workers_reconciled':recovered}
  journal=b.HERE/('resume-'+b.digest(sid)+'-'+str(old_revision)+'.json')
  def record():
   tmp=journal.with_suffix('.tmp');tmp.write_bytes(b.canonical(event));tmp.chmod(0o600);tmp.replace(journal)
  record()
  decision=runtime.acquire_lease({'schema_version':1,'work_id':body['bead_id'],'holder_id':body['holder'],'expected_revision':current['revision'],'ttl_seconds':7200})
  event.update(stage='lease_decision',decision=decision);record()
  if decision.get('status') not in {'acquired','idempotent_active'} or not decision.get('lease_active'):raise PermissionError('resume_lease_race_denied')
  new_work={**work,'lease_revision':decision['current_revision']}
  if new_work!=work:
   written=state.put({**q,'expected_revision':stored['object_ref']['revision'],'schema_id':'ResearchWorkContractV1','object':new_work,'content_hash':b.sha256_json(new_work),'operation_id':'BN-resume-'+b.digest(sid+':'+str(decision['current_revision']))[:24],'run_id':body['host_run']})
   if written.get('status') not in {'committed','no_op'}:raise PermissionError('resume_work_cas_failed')
  else:written={'status':'no_op'}
  event.update(stage='work_committed',canonical_write=written);record()
  s=b.ResearchSession(state,runtime,beads,memory,graph,project_id=body['project'],profile_id='hermes-bn',host_run_id=body['host_run'],work_contract_ref=body['work_ref'],holder_id=body['holder'])
  prepared=s.prepare(body['question']);s.check()
  context=json.dumps({'memory':prepared['memory_context'],'graph':prepared['graph_results']},ensure_ascii=False)
  run_path=b.root_for(body['run_id'])/'run.json'
  run=json.loads(run_path.read_text())
  if run.get('host_context') not in (binding,prepared['host_context']):raise PermissionError('resume_workspace_binding_mismatch')
  if run.get('host_context')!=prepared['host_context']:
   run.setdefault('host_context_history',[]).append({'context':run['host_context'],'replaced_at':time.time()})
   run['host_context']=prepared['host_context'];temp=run_path.with_suffix('.resume.tmp');temp.write_bytes(b.canonical(run));temp.chmod(0o600);temp.replace(run_path)
  body.update(binding=prepared['host_context'],admission_ref=prepared['admission_ref'],context='<UDR_REQUIRED_CONTEXT sha256="'+b.digest(context)+'">\n'+context+'\n</UDR_REQUIRED_CONTEXT>',context_delivered=False,last_lease_heartbeat=time.time(),last_lease_resume={'previous_revision':old_revision,'current_revision':decision['current_revision'],'journal':journal.name,'new_research':False,'at':time.time()})
  b.save(sid,body);result=b.check(sid);event.update(stage='complete',new_admission_ref=prepared['admission_ref']);record()
  return result


def prepare_turn(sid):
 result=_prepare_turn(sid)
 if result.get('status')=='active' and not result.get('native_child'):
  b.pin_continuity(sid)
  result={**result,'continuity':b.continuity_policy(b.saved(sid),sid)}
 return result
