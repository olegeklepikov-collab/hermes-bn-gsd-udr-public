"""Beads is the task authority; signed files map native executions and products."""
import hashlib,hmac,json,re,time,fcntl,contextlib
from pathlib import Path
import backend as b
from worker_policy import READ_TOOLS

def valid_plan(request):
 tasks=request.get('tasks');rid=request.get('request_id')
 if not isinstance(rid,str) or not re.fullmatch(r'[A-Za-z0-9_.-]{1,100}',rid):raise ValueError('stable_request_id_required')
 if not isinstance(tasks,list) or not 1<=len(tasks)<=8:raise ValueError('split_into_1_to_8_tasks')
 keys=[]
 for task in tasks:
  if not isinstance(task,dict) or set(task)-{'key','title','goal','role','depends_on','input_refs','corpus_id'}:raise ValueError('invalid_task_fields')
  key=task.get('key');goal=task.get('goal');title=task.get('title')
  if not isinstance(key,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,40}',key) or key in keys:raise ValueError('unique_task_keys_required')
  if task.get('role') not in {'collector','reviewer'} or not isinstance(goal,str) or not 1<=len(goal)<=16000 or not isinstance(title,str) or not 1<=len(title)<=120:raise ValueError('invalid_role_or_task_text')
  if task.get('corpus_id') is not None and (not isinstance(task['corpus_id'],str) or not task['corpus_id'].startswith('CORP-')):raise ValueError('registered_corpus_id_required')
  if not isinstance(task.get('depends_on',[]),list) or not isinstance(task.get('input_refs',[]),list):raise ValueError('invalid_task_references')
  keys.append(key)
 deps={t['key']:t.get('depends_on',[]) for t in tasks};done=set()
 while len(done)<len(keys):
  ready=[k for k in keys if k not in done and all(d in done for d in deps[k])]
  if not ready:raise ValueError('cycle_or_missing_dependency')
  done.update(ready)
 if any(not isinstance(c,str) for c in request.get('constraints',[])):raise ValueError('invalid_constraints')
 if any(not isinstance(d,str) or not re.fullmatch(r'[a-zA-Z0-9.-]+',d) for d in request.get('source_domains',[])):raise ValueError('invalid_source_domains')
 return tasks

def parent(sid):
 body=b.saved(sid)
 if not body or body.get('native_child') or body.get('phase')!='running':raise PermissionError('active_root_research_required')
 b.check(sid);return body

def path_for(body,rid):
 root=b.root_for(body['run_id'])/'teams';root.mkdir(mode=0o700,exist_ok=True)
 return root/(b.digest(body['host_run']+':'+rid)+'.json')

def load(path):
 value=json.loads(path.read_text());key=(b.ROOT/'state/authority/bn-bridge.key').read_bytes()
 if path.is_symlink() or not hmac.compare_digest(value['mac'],hmac.new(key,b.canonical(value['body']),hashlib.sha256).hexdigest()):raise PermissionError('team_state_authentication_failed')
 return value['body']

def save(path,body):
 key=(b.ROOT/'state/authority/bn-bridge.key').read_bytes();value={'body':body,'mac':hmac.new(key,b.canonical(body),hashlib.sha256).hexdigest()}
 tmp=path.with_suffix('.tmp');tmp.write_bytes(b.canonical(value));tmp.chmod(0o600);tmp.replace(path)

@contextlib.contextmanager
def locked(path):
 with open(path.with_suffix('.lock'),'a') as f:
  fcntl.flock(f,fcntl.LOCK_EX);yield

def graph_note(beads,issue,text):return beads._run(['update',issue,'--append-notes',text],actor='bn-udr-team')
def validated_refs(body,task):
 root=b.root_for(body['run_id']).resolve();refs=[]
 for rel in task.get('input_refs',[]):
  if not isinstance(rel,str):raise ValueError('invalid_scoped_input_ref')
  try:page=b.read_page(root,rel,0,1)
  except (ValueError,PermissionError,OSError,UnicodeError) as exc:raise ValueError('invalid_scoped_input_ref') from exc
  refs.append({'path':rel,'sha256':page['sha256']})
 return refs

def plan(sid,request):
 tasks=valid_plan(request);body=parent(sid);rid=request['request_id'];docs=None;document_ids={}
 for task in tasks:
  cid=task.get('corpus_id')
  if not cid:document_ids[task['key']]=[];continue
  if docs is None:docs=b.document_store()
  corpus=docs.corpus(sid,cid)
  required_phase='verify' if task['role']=='reviewer' else 'collect'
  if required_phase not in set(json.loads(corpus['phases'])):raise ValueError('assigned_worker_document_phase_required')
  with docs.store.db() as db:
   partition=db.execute('SELECT parent,members FROM document_partitions WHERE id=?',(cid,)).fetchone()
   document_ids[task['key']]=sorted({member[0] for member in json.loads(partition['members'])}) if partition else [r[0] for r in db.execute('SELECT id FROM document_sources WHERE corpus=?',(cid,))]
  if not document_ids[task['key']]:raise ValueError('assigned_corpus_has_no_documents')
 refs_by_key={task['key']:validated_refs(body,task) for task in tasks};p=path_for(body,rid);fingerprint=b.digest(b.canonical(request));_,_,_,beads,_,_=b.adapters()
 with locked(p):
  if p.exists():
   wave=load(p)
   if wave['fingerprint']!=fingerprint:raise ValueError('team_request_id_conflict')
   if wave['planned']:return wave
  else:
   wave={'contract':'UDRNativeTeamV1','sid':sid,'request_id':rid,'fingerprint':fingerprint,'parent_bead':body['bead_id'],'run_id':body['run_id'],'project':body['project'],'planned':False,'tasks':{},'created_at':time.time()};save(p,wave)
  for task in tasks:
   key=task['key'];tid='UT.'+b.digest(body['host_run']+':'+rid+':'+key)[:32]
   if key in wave['tasks']:continue
   refs=refs_by_key[key]
   created=beads.create({'schema_version':1,'title':task['title'],'description':'UDR parent '+body['bead_id']+'; '+task['role']+'; native '+tid,'priority':2,'issue_type':'task','operation_key':tid})
   if created.get('status')!='created':raise RuntimeError('canonical_child_bead_not_created')
   issue=created['issue_id'];beads._run(['update',issue,'--parent',body['bead_id']],actor='bn-udr-team')
   item={'id':tid,'key':key,'bead_id':issue,'worker_id':'BNW-'+tid[3:],'role':task['role'],'goal':task['goal'],'depends_on':task.get('depends_on',[]),'input_refs':refs,'constraints':request.get('constraints',[]),'source_domains':request.get('source_domains',[]),'corpus_id':task.get('corpus_id'),'document_ids':document_ids[key],'document_phase':'verify' if task['role']=='reviewer' else 'collect','state':'planned','child_sid':None,'handle':None,'result':None,'receipt':None,'evidence':[]}
   wave['tasks'][key]=item;save(p,wave)
  for task in tasks:
   item=wave['tasks'][task['key']]
   for dep in task.get('depends_on',[]):
    beads._run(['dep','add',item['bead_id'],wave['tasks'][dep]['bead_id'],'--type','blocks'],actor='bn-udr-team')
  wave['planned']=True;save(p,wave);graph_note(beads,body['bead_id'],'Native UDR team '+rid+'; '+', '.join(t['bead_id'] for t in wave['tasks'].values()))
 return wave

def get(sid,rid):
 body=b.saved(sid)
 if not body or body.get('native_child'):raise PermissionError('root_research_record_required')
 return load(path_for(body,rid))
def find(parent_sid,tid):
 body=parent(parent_sid)
 for p in (b.root_for(body['run_id'])/'teams').glob('*.json'):
  wave=load(p)
  for key,task in wave['tasks'].items():
   if task['id']==tid:return body,p,key
 raise PermissionError('unknown_scoped_native_task')

def begin(sid,rid,key,executor_owner=None):
 body=parent(sid);p=path_for(body,rid);_,_,_,beads,_,_=b.adapters()
 with locked(p):
  wave=load(p);task=wave['tasks'][key]
  if task['state']=='succeeded':return task
  if task['state']!='planned':raise PermissionError('task_requires_recovery_not_automatic_replay')
  if any(wave['tasks'][d]['state']!='succeeded' for d in task['depends_on']):raise PermissionError('task_dependencies_unsettled')
  if validated_refs(body,{'input_refs':[ref['path'] for ref in task['input_refs']]})!=task['input_refs']:raise PermissionError('assigned_input_version_changed')
  issue=beads.get({'schema_version':1,'issue_id':task['bead_id']})['issue']
  if issue['status']!='open':raise PermissionError('canonical_task_not_open')
  claim=beads.claim({'schema_version':1,'issue_id':task['bead_id'],'worker_id':task['worker_id'],'operation_key':task['id']+'-claim'})
  if claim.get('status')!='claimed':raise PermissionError('canonical_task_not_claimed')
  task['input']={'task_id':task['id'],'role':task['role'],'goal':task['goal'],'scope':{'run_id':body['run_id'],'project':body['project'],'parent_bead':body['bead_id'],'child_bead':task['bead_id']},'question':body['question'],'profile':body['depth'],'constraints':task['constraints'],'source_domains':task.get('source_domains',[]),'input_refs':task['input_refs'],'corpus_id':task.get('corpus_id'),'document_ids':task.get('document_ids',[]),'document_phase':task.get('document_phase','collect'),'dependency_products':{d:wave['tasks'][d]['result'] for d in task['depends_on']},'mandatory_rules':['read_only','no_delegation','no_scientific_acceptance','no_external_delivery']}
  if executor_owner is not None:
   if not isinstance(executor_owner,dict) or type(executor_owner.get('pid')) is not int or not isinstance(executor_owner.get('created_at'),(float,int)):raise ValueError('invalid_executor_owner')
   task['executor_owner']=executor_owner
  task['input_sha256']=b.digest(b.canonical(task['input']));task['state']='launch_reserved';task['started_at']=time.time();save(p,wave)
  return task

def bind(child_sid,parent_sid,tid):
 body,p,key=find(parent_sid,tid);_,_,_,beads,_,_=b.adapters()
 with locked(p):
  wave=load(p);task=wave['tasks'][key]
  if task['state'] not in {'launch_reserved','running'} or task['child_sid'] not in (None,child_sid):raise PermissionError('native_task_binding_mismatch')
  issue=beads.get({'schema_version':1,'issue_id':task['bead_id']})['issue']
  if issue['status']!='in_progress' or issue['assignee']!=task['worker_id']:raise PermissionError('worker_does_not_own_child_bead')
  task['child_sid']=child_sid;task['state']='running';save(p,wave)
 b.save(child_sid,{'phase':'child','native_child':True,'requires_udr':True,'managed_worker':True,'parent_sid':parent_sid,'task_id':tid})
 return check(child_sid)

def check(child_sid):
 child=b.saved(child_sid);body,p,key=find(child['parent_sid'],child['task_id']);wave=load(p);task=wave['tasks'][key]
 if task['child_sid']!=child_sid or task['state']!='running':raise PermissionError('native_worker_not_running')
 _,_,_,beads,_,_=b.adapters();issue=beads.get({'schema_version':1,'issue_id':task['bead_id']})['issue']
 if issue['status']!='in_progress' or issue['assignee']!=task['worker_id']:raise PermissionError('native_worker_claim_changed')
 context=body['context']+'\n<UDR_NATIVE_TASK_INPUT sha256="'+task['input_sha256']+'">\n'+b.canonical(task['input']).decode()+'\n</UDR_NATIVE_TASK_INPUT>'
 return {'status':'active','native_child':True,'managed_worker':True,'context':context,'run_id':body['run_id'],'task_id':task['id'],'read_paths':[r['path'] for r in task['input_refs']],'read_sha256':{r['path']:r['sha256'] for r in task['input_refs']},'corpus_id':task.get('corpus_id'),'document_ids':task.get('document_ids',[]),'document_phase':task.get('document_phase','collect'),'source_domains':task.get('source_domains',[])}

def update(sid,rid,key,fields):
 p=path_for(parent(sid),rid)
 if set(fields)-{'handle','state','result','receipt','error','completed_at'}:raise PermissionError('invalid_host_task_update')
 with locked(p):
  wave=load(p);task=wave['tasks'][key];task.update(fields);save(p,wave);return task

def evidence(sid,event):
 child=b.saved(sid);checked=check(sid);body,p,key=find(child['parent_sid'],child['task_id'])
 text=event['text']
 if re.search(r'(?i)(?:(?<![A-Za-z0-9_-])sk-[A-Za-z0-9_-]{20,}|Bearer\s+[A-Za-z0-9_-]{16,}|[0-9]{8,}:[A-Za-z0-9_-]{30,})',text):raise PermissionError('sensitive_worker_evidence_refused')
 record={'task_id':checked['task_id'],'native_sid':sid,'tool':event['tool'],'source_version':event['source_version'],'source_ref':event.get('source_ref',''),'text':text,'reading_level':'tool_result_only','truth_accepted':False};sha=b.digest(b.canonical(record));folder=p.parent/checked['task_id'];folder.mkdir(mode=0o700,exist_ok=True);file=folder/(sha+'.json')
 if not file.exists():file.write_bytes(b.canonical(record));file.chmod(0o600)
 with locked(p):
  wave=load(p);task=wave['tasks'][key]
  if sha not in task['evidence']:task['evidence'].append(sha);save(p,wave)
 return {'status':'recorded','task_id':checked['task_id'],'sha256':sha}

def output(sid,rid,key,text,receipt,origin='native_summary'):
 p=path_for(parent(sid),rid)
 with locked(p):
  wave=load(p);task=wave['tasks'][key]
  if task['child_sid'] is None or receipt.get('handle',{}).get('correlation_id')!=task['id'] or receipt.get('handle',{}).get('parent_session_id')!=sid:raise PermissionError('output_receipt_scope_mismatch')
  if not isinstance(text,str) or len(text.encode())>8*1024*1024:raise ValueError('invalid_native_output')
  folder=p.parent/task['id'];folder.mkdir(mode=0o700,exist_ok=True)
  raw=text.encode();sha=b.digest(raw);file=folder/(sha+'.output.txt')
  if not file.exists():file.write_bytes(raw);file.chmod(0o600)
  record={'sha256':sha,'path':str(file.relative_to(p.parent)),'origin':origin}
  if task.get('native_output') and task['native_output']!=record:raise PermissionError('saved_native_output_is_immutable')
  task['native_output']=record;save(p,wave)
  return record

def recover_saved_product(sid,rid,key,text,message_id):
 # Local operator only, deliberately absent from the model-facing RPC dispatch.
 # Restore a stored visible assistant product after a serialization failure,
 # with the already signed successful receipt. Do not repeat the executor.
 from team_runner import parse_product
 wave=get(sid,rid);task=wave['tasks'][key];receipt=task.get('receipt') or {}
 if task['state']!='blocked' or not (task.get('error') or '').startswith('Invalid control character') or receipt.get('terminal_state')!='SUCCEEDED':raise PermissionError('serialization_recovery_only')
 result=parse_product(text)
 record=output(sid,rid,key,text,receipt,origin='native_assistant_content')
 recovery={'previous_error':task['error'],'source':record,'message_id':message_id,'child_sid':task['child_sid'],'new_executors':0}
 return finish(sid,rid,key,result,receipt,_recovery=recovery)

def finish(sid,rid,key,result,receipt,_recovery=None):
 body=parent(sid);p=path_for(body,rid);_,_,_,beads,_,_=b.adapters()
 with locked(p):
  wave=load(p);task=wave['tasks'][key]
  if task['state']=='succeeded':
   if task['result']!=result:raise PermissionError('completed_product_is_immutable')
   return task
  recovering=_recovery is not None and task['state']=='blocked' and (task.get('error') or '').startswith('Invalid control character') and task.get('receipt')==receipt
  if (task['state'] not in {'running','product_saved'} and not recovering) or receipt.get('terminal_state')!='SUCCEEDED':raise PermissionError('actual_successful_worker_required')
  if not isinstance(result,dict) or set(result)!={'task_id','role','status','sources','findings','limitations'} or result['task_id']!=task['id'] or result['role']!=task['role'] or result['status']!='unreviewed' or any(not isinstance(result[k],list) for k in ['sources','findings','limitations']):raise ValueError('invalid_typed_worker_product')
  if any(not isinstance(x,str) for x in result['limitations']) or any(not isinstance(x,dict) or set(x)!={'claim','assessment','evidence_refs'} or not isinstance(x['claim'],str) or not isinstance(x['assessment'],str) or not isinstance(x['evidence_refs'],list) or any(not isinstance(ref,str) for ref in x['evidence_refs']) for x in result['findings']):raise ValueError('invalid_typed_findings')
  if task['role']=='collector' and not task['evidence']:raise PermissionError('collector_has_no_actual_tool_evidence')
  if task.get('corpus_id'):
   coverage=b.document_store().status(sid,{'corpus_id':task['corpus_id'],'_recipient_sid':task['child_sid']})
   phase=task.get('document_phase','collect')
   if not coverage['phases'].get(phase,{}).get('complete'):raise PermissionError('required_worker_document_coverage_incomplete')
   receipt={**receipt,'document_coverage':coverage['phases'][phase],'document_recipient_sid':task['child_sid']}
  records=[json.loads((p.parent/task['id']/(sha+'.json')).read_text()) for sha in task['evidence']]
  pool='\n'.join(r['text']+'\n'+r.get('source_ref','') for r in records)+b.canonical(task['input']['dependency_products']).decode()
  from urllib.parse import urlsplit
  for source in result['sources']:
   if not isinstance(source,dict) or set(source)!={'url','title','reading_level','text'} or source['reading_level']!='tool_result_only' or any(not isinstance(source[field],str) for field in ['url','title','text']) or source['url'] not in pool:raise PermissionError('source_provenance_not_found')
   domains=task.get('source_domains',[])
   hostname=urlsplit(source['url']).hostname or ''
   if domains and not any(hostname==d or hostname.endswith('.'+d) for d in domains):raise PermissionError('source_outside_task_domains')
  native=receipt.get('handle',{})
  if native.get('correlation_id')!=task['id'] or native.get('parent_session_id')!=sid:raise PermissionError('native_receipt_scope_mismatch')
  if recovering:task['recovery']=_recovery;task.pop('error',None)
  task.update(state='product_saved',result=result,receipt=receipt,completed_at=time.time());save(p,wave)
  graph_note(beads,task['bead_id'],'Typed unreviewed product saved; input sha256 '+task['input_sha256']+'; actual native '+task['child_sid']+'; evidence '+str(len(task['evidence'])))
  beads.close({'schema_version':1,'issue_id':task['bead_id'],'reason_code':'native-product-saved-unreviewed','worker_id':task['worker_id']})
  task['state']='succeeded';save(p,wave)
  return task

def block(sid,rid,key,reason,receipt=None):
 task=update(sid,rid,key,{'state':'blocked','error':reason,'receipt':receipt,'completed_at':time.time()});_,_,_,beads,_,_=b.adapters();beads._run(['update',task['bead_id'],'--status','blocked','--append-notes',reason[:1000]],actor='bn-udr-team');return task

def public(wave):
 _,_,_,beads,_,_=b.adapters();tasks=[]
 for item in wave['tasks'].values():
  view={k:item.get(k) for k in ['id','key','bead_id','role','depends_on','state','child_sid','result','receipt','error','input_sha256','evidence','native_output','recovery','corpus_id','document_ids','document_phase'] if item.get(k) is not None}
  if view.get('receipt'):
   view['receipt']={k:v for k,v in view['receipt'].items() if v is not None}
  view['beads_status']=beads.get({'schema_version':1,'issue_id':item['bead_id']})['issue']['status'];tasks.append(view)
 return {'request_id':wave['request_id'],'parent_bead':wave['parent_bead'],'run_id':wave['run_id'],'tasks':tasks}

def read_evidence(sid,rid,key,evidence_id,offset=0,max_chars=4096):
 wave=get(sid,rid)
 if key not in wave['tasks']:raise PermissionError('unknown_scoped_task')
 task=wave['tasks'][key]
 if not isinstance(evidence_id,str) or not re.fullmatch(r'[a-f0-9]{64}',evidence_id) or evidence_id not in task['evidence']:raise PermissionError('evidence_not_assigned_to_task')
 if type(offset) is not int or type(max_chars) is not int or offset<0 or not 1<=max_chars<=4096:raise ValueError('evidence_page_bounds_invalid')
 body=b.saved(sid);file=path_for(body,rid).parent/task['id']/(evidence_id+'.json')
 if file.is_symlink() or not file.is_file():raise PermissionError('evidence_file_unavailable')
 raw=file.read_bytes()
 if b.digest(raw)!=evidence_id:raise PermissionError('evidence_integrity_failed')
 record=json.loads(raw)
 if record['task_id']!=task['id'] or record['native_sid']!=task['child_sid']:raise PermissionError('evidence_scope_mismatch')
 text=record['text']
 if offset>len(text):raise ValueError('evidence_offset_outside_text')
 end=min(offset+max_chars,len(text));fragment=text[offset:end]
 return {'request_id':rid,'task_key':key,'task_id':task['id'],'native_sid':task['child_sid'],'evidence_id':evidence_id,
  'tool':record['tool'],'source_ref':record.get('source_ref',''),'source_version':record['source_version'],
  'text':fragment,'text_sha256':b.digest(text),'fragment_sha256':b.digest(fragment),'offset':offset,'end_offset':end,
  'next_offset':end if end<len(text) else None,'complete':end==len(text),'total_characters':len(text),
  'offset_unit':'Unicode code points','reading_level':'preserved_tool_result_fragment','truth_accepted':False,
  'executor_repeated':False,'operator_bookkeeping_exposed':False}


def read_product(sid,rid,key,offset=0,max_chars=4096):
 wave=get(sid,rid)
 if key not in wave['tasks']:raise PermissionError('unknown_scoped_task')
 task=wave['tasks'][key]
 if task['state']!='succeeded' or (task.get('receipt') or {}).get('terminal_state')!='SUCCEEDED' or task.get('result') is None:raise PermissionError('successful_product_unavailable')
 if type(offset) is not int or type(max_chars) is not int or offset<0 or not 1<=max_chars<=4096:raise ValueError('product_page_bounds_invalid')
 original=task.get('native_output') or {}
 if not original.get('path') or not original.get('sha256'):raise PermissionError('original_product_source_unavailable')
 folder=path_for(b.saved(sid),rid).parent
 file=folder/original['path']
 if file.is_symlink() or not file.is_file() or not file.resolve().is_relative_to((folder/task['id']).resolve()):raise PermissionError('product_source_scope_failed')
 if b.digest(file.read_bytes())!=original['sha256']:raise PermissionError('product_integrity_failed')
 text=json.dumps(task['result'],ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)
 if offset>len(text):raise ValueError('product_offset_outside_text')
 end=min(offset+max_chars,len(text));fragment=text[offset:end]
 return {'request_id':rid,'task_key':key,'task_id':task['id'],'bead_id':task['bead_id'],'native_sid':task['child_sid'],
  'representation':'parsed_visible_product_pretty_JSON','original_product_sha256':original['sha256'],
  'text':fragment,'text_sha256':b.digest(text),'fragment_sha256':b.digest(fragment),'offset':offset,'end_offset':end,
  'next_offset':end if end<len(text) else None,'complete':end==len(text),'total_characters':len(text),
  'offset_unit':'Unicode code points','truth_accepted':False,'executor_repeated':False,'operator_bookkeeping_exposed':False}


def supersede_failed_attempt(sid,rid,key,replacements,reason):
 # Operator-only recovery, deliberately absent from the model-facing RPC.
 # Keep the old failed/unexecuted state and receipts; require actual replacements.
 if not isinstance(reason,str) or not reason.strip() or not isinstance(replacements,list) or not replacements:raise ValueError('operator_recovery_reason_and_replacements_required')
 body=parent(sid);p=path_for(body,rid)
 with locked(p):
  wave=load(p);task=wave['tasks'][key];receipt=task.get('receipt') or {}
  if task['state'] not in {'blocked','planned'}:raise PermissionError('only_failed_or_unexecuted_attempt_can_be_superseded')
  if task['state']=='planned' and (task.get('child_sid') or task.get('handle')):raise PermissionError('planned_executor_requires_reconciliation')
  if task['state']=='blocked' and receipt.get('terminal_state') not in {'FAILED','CANCELLED','SUCCEEDED'}:raise PermissionError('unknown_executor_cannot_be_superseded')
  accepted=[]
  for ref in replacements:
   if not isinstance(ref,dict) or set(ref)!={'request_id','key'}:raise ValueError('invalid_replacement_reference')
   replacement=get(sid,ref['request_id']);item=replacement['tasks'][ref['key']]
   if replacement['parent_bead']!=wave['parent_bead'] or replacement['run_id']!=wave['run_id'] or item['id']==task['id'] or item['role']!=task['role'] or item['state']!='succeeded' or (item.get('receipt') or {}).get('terminal_state')!='SUCCEEDED':raise PermissionError('actual_same_work_same_role_replacement_required')
   accepted.append({**ref,'task_id':item['id'],'bead_id':item['bead_id'],'receipt_sha256':b.digest(b.canonical(item['receipt']))})
  fingerprint=b.digest(b.canonical({'old_task':task['id'],'replacements':accepted,'reason':reason}))
  old=task.get('recovery')
  if old and old.get('fingerprint')!=fingerprint:raise PermissionError('operator_recovery_is_immutable')
  if old and old.get('state')=='complete':return old
  recovery={'type':'operator_confirmed_replacement','state':'pending','fingerprint':fingerprint,'reason':reason,'replacements':accepted,'original_state':task['state'],'original_result_accepted':False,'scientific_acceptance':False,'at':time.time()}
  task['recovery']=recovery;save(p,wave)
  _,_,_,beads,_,_=b.adapters()
  # An interrupted close is not blindly replayed. Only an observed closed target
  # may be reconciled under a distinct operation identity; historical receipts remain.
  close_key='supersede-'+fingerprint
  if old and old.get('state')=='pending':
   observed=beads.get({'schema_version':1,'issue_id':task['bead_id']})
   if observed['issue']['status']!='closed':raise PermissionError('pending_supersession_requires_observed_close_not_retry')
   recovery['prior_pending_recovery']=old
   recovery['observed_canonical_close']=observed
   close_key='supersede-observed-'+fingerprint
  closed=beads.close({'schema_version':1,'issue_id':task['bead_id'],'reason_code':'operator-superseded-'+fingerprint[:24],'worker_id':task['worker_id'],'operation_key':close_key})
  if closed.get('status')!='closed':raise PermissionError('canonical_supersession_unconfirmed')
  recovery.update(state='complete',canonical_close_receipt=closed);task['recovery']=recovery;save(p,wave);return recovery


def replacement_complete(sid,wave,task):
 recovery=task.get('recovery') or {}
 if recovery.get('type')!='operator_confirmed_replacement' or recovery.get('state')!='complete' or recovery.get('original_result_accepted') is not False or not recovery.get('replacements') or (recovery.get('canonical_close_receipt') or {}).get('status')!='closed':return False
 _,_,_,beads,_,_=b.adapters()
 if beads.get({'schema_version':1,'issue_id':task['bead_id']})['issue']['status']!='closed':return False
 for ref in recovery['replacements']:
  replacement=get(sid,ref['request_id']);item=replacement['tasks'][ref['key']]
  if replacement['parent_bead']!=wave['parent_bead'] or replacement['run_id']!=wave['run_id'] or item['id']!=ref['task_id'] or item['state']!='succeeded' or item['role']!=task['role'] or (item.get('receipt') or {}).get('terminal_state')!='SUCCEEDED' or b.digest(b.canonical(item['receipt']))!=ref['receipt_sha256']:return False
 return True

def rpc(sid,data):
 action=data['action']
 if action=='plan':return public(plan(sid,data['request']))
 if action=='get':return public(get(sid,data['request_id']))
 if action=='read_product':return read_product(sid,data['request_id'],data['key'],data.get('offset',0),data.get('max_chars',4096))
 if action=='read_evidence':return read_evidence(sid,data['request_id'],data['key'],data['evidence_id'],data.get('offset',0),data.get('max_chars',4096))
 if action=='begin':return begin(sid,data['request_id'],data['key'],data.get('executor_owner'))
 if action=='bind':return bind(sid,data['parent_sid'],data['task_id'])
 if action=='update':return update(sid,data['request_id'],data['key'],data['fields'])
 if action=='output':return output(sid,data['request_id'],data['key'],data['text'],data['receipt'])
 if action=='finish':return finish(sid,data['request_id'],data['key'],data['result'],data['receipt'])
 if action=='block':return {'task':block(sid,data['request_id'],data['key'],data['reason'],data.get('receipt'))}
 raise PermissionError('unknown_managed_team_operation')


def assert_finishable(sid,allow_partial=False):
 body=parent(sid);root=b.root_for(body['run_id'])/'teams'
 if not root.exists():return
 for p in root.glob('*.json'):
  wave=load(p)
  for task in wave['tasks'].values():
   if task['state']=='succeeded' or replacement_complete(sid,wave,task):continue
   if allow_partial and task['state'] in {'planned','blocked'} and (task.get('receipt') or {}).get('terminal_state')!='UNKNOWN':continue
   raise PermissionError('managed_tasks_require_completion_or_explicit_recovery')
