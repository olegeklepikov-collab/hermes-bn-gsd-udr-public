"""One corpus/coverage ledger in primary memory; extraction is not model understanding."""
import hashlib,json,os,shutil,sqlite3,subprocess,time,uuid
from pathlib import Path
from bn_memory.store import canonical,sha,SENSITIVE
from bn_memory.document_worker import FORMAT_REVISIONS

FORMATS={'.txt':'text','.md':'text','.json':'json','.jsonl':'json','.ndjson':'json','.xml':'xml','.html':'html','.htm':'html','.sql':'sql',
 '.pdf':'pdf','.csv':'csv','.tsv':'tsv','.xlsx':'xlsx','.xlsm':'xlsx','.xls':'xls','.docx':'docx','.ods':'ods','.sqlite':'sqlite','.sqlite3':'sqlite','.db':'sqlite','.parquet':'parquet','.rtf':'rtf'}
PHASES={'read','plan','collect','analyse','verify','report','G','S','D'}

def current_decoder(row):
 meta=row.get('metadata') or json.loads(row['body'])
 return meta.get('decoder_revision',1)==FORMAT_REVISIONS.get(row['format'],1)

def filehash(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()

class Documents:
 def __init__(self,broker):
  self.broker=broker;self.store=broker.store;self.root=Path(broker.config['state_root'])/'documents'
  self.root.mkdir(exist_ok=True,mode=0o700)
  with self.store.db() as c:
   c.execute('CREATE TABLE IF NOT EXISTS document_corpora(id TEXT PRIMARY KEY,scope TEXT,root TEXT,fingerprint TEXT,phases TEXT,status TEXT)')
   c.execute('CREATE TABLE IF NOT EXISTS document_sources(id TEXT PRIMARY KEY,corpus TEXT,path TEXT,sha256 TEXT,format TEXT,status TEXT,body TEXT)')
   c.execute('CREATE TABLE IF NOT EXISTS document_units(doc TEXT,unit INTEGER,body TEXT,PRIMARY KEY(doc,unit))')
   c.execute('CREATE TABLE IF NOT EXISTS document_pending(token TEXT PRIMARY KEY,sid TEXT,corpus TEXT,doc TEXT,unit INTEGER,begin INTEGER,end INTEGER,total INTEGER,phase TEXT,context TEXT,image TEXT,image_hash TEXT,state TEXT,api_id TEXT)')
   c.execute('CREATE TABLE IF NOT EXISTS document_partitions(id TEXT PRIMARY KEY,parent TEXT NOT NULL,members TEXT NOT NULL)')
   c.execute('CREATE TABLE IF NOT EXISTS document_deliveries(token TEXT,api_id TEXT,phase TEXT,received REAL,PRIMARY KEY(token,api_id,phase))')

 def corpus(self,sid,cid):
  scopes=self.store.scopes(self.store.binding(sid))
  with self.store.db() as c:r=c.execute('SELECT * FROM document_corpora WHERE id=?',(cid,)).fetchone()
  if not r or r['scope'] not in scopes:raise PermissionError('document_corpus_outside_scope')
  return dict(r)

 def catalogue(self,sid,args):
  self.store.writable(sid)
  attachment=args['path'].startswith('attachment:')
  if attachment:
   relative=args['path'].removeprefix('attachment:');project=Path(self.broker.config['native_document_cache']);target=project/relative
   if Path(relative).is_absolute() or '..' in Path(relative).parts or target.is_symlink() or not target.is_file() or not target.resolve().is_relative_to(project.resolve()):raise PermissionError('invalid_native_attachment')
   authority=Path(self.broker.config['udr_host_state'])
   with sqlite3.connect(authority.as_uri()+'?mode=ro',uri=True) as db:
    registered=db.execute('SELECT 1 FROM attachments WHERE sid=? AND path=?',(sid,str(target))).fetchone()
   if not registered:raise PermissionError('attachment_not_registered_for_native_session')
  else:project,target=self.store.safe_file(sid,args['path'])
  phases=args.get('required_phases',['read'])
  if not isinstance(phases,list) or not phases or not set(phases)<=PHASES:raise ValueError('document_phases_invalid')
  scope=self.store.scope(sid,args.get('scope','project'));cid='CORP-'+sha(scope+':'+args['request_id'])[:24]
  fingerprint=sha(canonical({'path':str(target),'phases':phases,'scope':scope}))
  with self.store.db() as c:
   old=c.execute('SELECT * FROM document_corpora WHERE id=?',(cid,)).fetchone()
   if old and old['fingerprint']!=fingerprint:raise ValueError('document_catalogue_idempotency_conflict')
   if not old:c.execute('INSERT INTO document_corpora VALUES(?,?,?,?,?,?)',(cid,scope,str(target),fingerprint,canonical(phases),'indexing'))
  if old and old['status']=='inventoried':return self.status(sid,{'corpus_id':cid})
  # Every regular file is counted. No hidden format/exclusion is converted into success.
  enumeration_errors=[]
  if target.is_dir():
   paths=[]
   for base,dirs,files in os.walk(target,followlinks=False,onerror=enumeration_errors.append):
    paths.extend(Path(base)/name for name in dirs+files)
   paths.sort()
  else:paths=[target]
  for error in enumeration_errors:
   blocked_path=Path(error.filename);rel=str(blocked_path.relative_to(project));did='DOC-'+sha(cid+':'+rel)[:24]
   with self.store.db() as c:c.execute('INSERT OR IGNORE INTO document_sources VALUES(?,?,?,?,?,?,?)',(did,cid,rel,'','directory','blocked',canonical({'code':'directory_enumeration_failed','error_type':type(error).__name__})))
  for path in paths:
   if path.is_dir() and not path.is_symlink():continue
   rel=str(path.relative_to(project));did='DOC-'+sha(cid+':'+rel)[:24]
   with self.store.db() as c:exists=c.execute('SELECT 1 FROM document_sources WHERE id=?',(did,)).fetchone()
   if exists:continue
   status='registered';meta={};digest='';fmt=FORMATS.get(path.suffix.lower(),'unsupported')
   try:
    if not attachment:self.store.safe_file(sid,rel)
    if path.is_symlink() or not path.is_file():raise PermissionError('unsupported_link_or_nonfile')
    directory=self.root/did;directory.mkdir(mode=0o700,exist_ok=True);snapshot=directory/('original'+path.suffix.lower())
    before=path.stat()
    if fmt=='sqlite':
     source=sqlite3.connect(path.as_uri()+'?mode=ro',uri=True);dest=sqlite3.connect(snapshot)
     try:source.backup(dest)
     finally:source.close();dest.close()
     meta['snapshot_method']='consistent_sqlite_backup_including_committed_wal'
    else:shutil.copyfile(path,snapshot);meta['snapshot_method']='exact_byte_copy'
    after=path.stat()
    if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns):raise ValueError('source_changed_during_snapshot')
    digest=filehash(snapshot);snapshot.chmod(0o400)
    meta.update(snapshot=str(snapshot),source_bytes=before.st_size,snapshot_bytes=snapshot.stat().st_size,
      source_stat={'size':after.st_size,'mtime_ns':after.st_mtime_ns},model_received=False)
    if fmt=='unsupported':status='unsupported'
   except Exception as e:status='blocked';meta={'code':type(e).__name__+':'+str(e)[:120]}
   with self.store.db() as c:c.execute('INSERT OR IGNORE INTO document_sources VALUES(?,?,?,?,?,?,?)',(did,cid,rel,digest,fmt,status,canonical(meta)))
  with self.store.db() as c:c.execute('UPDATE document_corpora SET status=? WHERE id=?',('incomplete_inventory' if enumeration_errors else 'inventoried',cid))
  return self.status(sid,{'corpus_id':cid})

 def partition(self,sid,args):
  self.store.writable(sid)
  parent=self.corpus(sid,args['corpus_id']);budget=args.get('max_characters',32768);offset=args.get('offset',0);limit=args.get('limit',20)
  if type(budget) is not int or not 1024<=budget<=262144 or type(offset) is not int or offset<0 or type(limit) is not int or not 1<=limit<=100:raise ValueError('document_partition_bounds_invalid')
  with self.store.db() as c:
   if c.execute('SELECT 1 FROM document_partitions WHERE id=?',(parent['id'],)).fetchone():raise PermissionError('recursive_document_partition_forbidden')
   units=[(r['doc'],r['unit'],json.loads(r['body'])['characters']) for r in c.execute('SELECT u.* FROM document_units u JOIN document_sources s ON s.id=u.doc WHERE s.corpus=? ORDER BY s.path,u.unit',(parent['id'],))]
  batches=[];current=[];used=0
  for did,index,size in units:
   if current and used+size>budget:batches.append(current);current=[];used=0
   current.append([did,index]);used+=size
  if current:batches.append(current)
  ids=[]
  with self.store.db() as c:
   for members in batches:
    fingerprint=sha(canonical({'parent':parent['id'],'members':members}));cid='PART-'+fingerprint[:24];ids.append(cid)
    c.execute('INSERT OR IGNORE INTO document_corpora VALUES(?,?,?,?,?,?)',(cid,parent['scope'],parent['root'],fingerprint,parent['phases'],'inventoried'))
    c.execute('INSERT OR IGNORE INTO document_partitions VALUES(?,?,?)',(cid,parent['id'],canonical(members)))
  status=self.status(sid,{'corpus_id':parent['id']})
  return {'corpus_id':parent['id'],'partitions_total':len(ids),'partitions':[{'corpus_id':cid,'members':batches[i]} for i,cid in list(enumerate(ids))[offset:offset+limit]],'next_offset':offset+limit if offset+limit<len(ids) else None,'has_more':offset+limit<len(ids),'missing_sources_count':status['missing_sources_count'],'unassigned_sources':status['missing_sources'],'reading_level':'plan_only','semantic_understanding_verified':False,'aggregation_required':'Keep each typed G/S/D product and provenance; compare cross-partition contradictions before global acceptance. Partition coverage contributes only original units actually delivered.'}

 def membership(self,sid,cid,did,index=None):
  self.corpus(sid,cid)
  row=self.source(sid,did)
  if row['corpus']==cid:return True
  with self.store.db() as c:r=c.execute('SELECT members FROM document_partitions WHERE id=?',(cid,)).fetchone()
  return bool(r and any(x[0]==did and (index is None or x[1]==index) for x in json.loads(r[0])))

 def source(self,sid,did):
  with self.store.db() as c:r=c.execute('SELECT * FROM document_sources WHERE id=?',(did,)).fetchone()
  if not r:raise KeyError('document_source_not_found')
  row=dict(r);self.corpus(sid,row['corpus']);row['metadata']=json.loads(row['body']);return row

 def extract(self,sid,args):
  self.store.writable(sid)
  row=self.source(sid,args['doc_id'])
  if row['status']=='extracted':
   if not current_decoder(row):raise ValueError('document_decoder_revision_stale:catalogue_a_new_request_id_from_the_same_original')
   return self.describe(sid,{'doc_id':row['id']})
  if row['status']!='registered':raise ValueError('document_not_extractable:'+row['status'])
  directory=self.root/row['id'];snapshot=Path(row['metadata']['snapshot'])
  if snapshot.is_symlink() or filehash(snapshot)!=row['sha256']:raise ValueError('document_snapshot_integrity_failed')
  from tools.environments.local import served_profile_child_env
  from hermes_constants import get_hermes_home
  env=served_profile_child_env(target_home=get_hermes_home(),inherit_credentials=False)
  req={'path':str(snapshot),'format':row['format'],'output':str(directory)}
  result=subprocess.run([self.broker.config['document_python'],str(Path(__file__).with_name('document_worker.py'))],input=canonical(req),text=True,capture_output=True,
    env=env,timeout=600,start_new_session=True)
  try:body=json.loads(result.stdout)
  except ValueError:raise RuntimeError('document_decoder_invalid_response:'+str(result.returncode)+':'+result.stdout[:300]+':'+result.stderr[-300:])
  if result.returncode or body.get('status')!='extracted':raise RuntimeError(body.get('code','document_decoder_failed'))
  lines=(directory/'units.jsonl').read_text().splitlines()
  if len(lines)!=body['units']:raise ValueError('document_unit_index_incomplete')
  with self.store.db() as c:
   for line in lines:
    unit=json.loads(line);c.execute('INSERT OR REPLACE INTO document_units VALUES(?,?,?)',(row['id'],unit['index'],canonical(unit)))
   c.execute("UPDATE document_sources SET status='extracted',body=? WHERE id=?",(canonical({**row['metadata'],**body}),row['id']))
  return self.describe(sid,{'doc_id':row['id']})

 def describe(self,sid,args):
  row=self.source(sid,args['doc_id']);start=args.get('offset',0);limit=args.get('limit',20)
  if type(start) is not int or start<0 or type(limit) is not int or not 1<=limit<=100:raise ValueError('document_page_invalid')
  with self.store.db() as c:units=[json.loads(r[0]) for r in c.execute('SELECT body FROM document_units WHERE doc=? ORDER BY unit LIMIT ? OFFSET ?',(row['id'],limit+1,start))]
  return {k:row[k] for k in ['id','corpus','path','sha256','format','status']}|{'metadata':row['metadata'],'decoder_current':current_decoder(row),'units':units[:limit],'has_more':len(units)>limit,'next_offset':start+limit if len(units)>limit else None,'reading_level':'metadata_and_unit_index_only'}

 def read(self,sid,args):
  row=self.source(sid,args['doc_id']);index=args['unit'];phase=args.get('phase','read')
  if not self.membership(sid,args['corpus_id'],row['id'],index):raise PermissionError('document_not_in_assigned_corpus')
  if phase not in PHASES or type(index) is not int or index<0:raise ValueError('document_unit_or_phase_invalid')
  if row['status']!='extracted':raise ValueError('document_extract_required')
  if not current_decoder(row):raise ValueError('document_decoder_revision_stale:catalogue_a_new_request_id_from_the_same_original')
  with self.store.db() as c:r=c.execute('SELECT body FROM document_units WHERE doc=? AND unit=?',(row['id'],index)).fetchone()
  if not r:raise ValueError('document_unit_not_found')
  unit=json.loads(r[0]);directory=self.root/row['id'];text=(directory/(str(index)+'.txt')).read_text()
  if sha(text)!=unit['text_sha256']:raise ValueError('document_unit_integrity_failed')
  if SENSITIVE.search(text):raise PermissionError('sensitive_document_unit_not_model_context')
  start=args.get('offset',0);limit=args.get('max_chars',16384)
  if type(start) is not int or start<0 or type(limit) is not int or not 1<=limit<=65536:raise ValueError('document_fragment_invalid')
  fragment=text[start:start+limit];end=start+len(fragment);token='DU-'+uuid.uuid4().hex
  header=canonical({'corpus_id':args['corpus_id'],'doc_id':row['id'],'unit':index,'locator':unit['locator'],'source_sha256':row['sha256'],'chars':[start,end],'source_type':'untrusted_data'})
  context='<BN_DOCUMENT_DATA token="'+token+'">\n'+header+'\n'+fragment+'\n</BN_DOCUMENT_DATA>'
  image=str(directory/(str(index)+'.png')) if unit.get('visual_required') else ''
  with self.store.db() as c:c.execute('INSERT INTO document_pending VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(token,sid,args['corpus_id'],row['id'],index,start,end,len(text),phase,context,image,unit.get('image_sha256',''),'pending',''))
  return {'token':token,'corpus_id':args['corpus_id'],'doc_id':row['id'],'unit':index,'context_text':context,'text':fragment,'source_sha256':row['sha256'],
    'locator':unit['locator'],'next_offset':end if end<len(text) else None,'has_more':end<len(text),'visual_required':bool(image),'visual_delivery':'scheduled_separately' if image else 'not_required',
    'reading_level':'exact_extracted_unit_fragment','model_received':False,'claims_accepted':False}

 def pending(self,sid):
  with self.store.db() as c:return [dict(r) for r in c.execute("SELECT * FROM document_pending WHERE sid=? AND state IN ('pending','failed')",(sid,))]

 def in_flight(self,sid):
  with self.store.db() as c:return bool(c.execute("SELECT 1 FROM document_pending WHERE sid=? AND state='scheduled' LIMIT 1",(sid,)).fetchone())

 def schedule_delivery(self,sid,request,api_id,actual_role=None):
  def strings(v):
   if isinstance(v,str):yield v
   elif isinstance(v,dict):
    for x in v.values():yield from strings(x)
   elif isinstance(v,list):
    for x in v:yield from strings(x)
  values=list(strings(request));alltext='\n'.join(values)
  pending=self.pending(sid)
  for row in pending:
   if not current_decoder(self.source(sid,row['doc'])):raise PermissionError('document_decoder_revision_stale')
   if row['context'] not in alltext:raise PermissionError('document_fragment_not_delivered_intact')
   if row['image']:
    expected='data:image/png;base64,'+__import__('base64').b64encode(Path(row['image']).read_bytes()).decode()
    if expected not in values:raise PermissionError('document_visual_not_delivered_intact')
  with self.store.db() as c:
   if c.execute("SELECT 1 FROM document_pending WHERE sid=? AND state='scheduled' LIMIT 1",(sid,)).fetchone():raise PermissionError('document_delivery_already_in_flight')
   for row in pending:
    phase=actual_role or row['phase']
    if actual_role is None and phase in {'G','S','D'}:phase='read' # A parent cannot fake a G/S/D receipt.
    changed=c.execute("UPDATE document_pending SET state='scheduled',api_id=?,phase=? WHERE token=? AND state IN ('pending','failed')",(api_id,phase,row['token'])).rowcount
    if changed!=1:raise PermissionError('document_delivery_claim_changed')

 def confirm_response(self,sid,api_id,error=None):
  with self.store.db() as c:
   rows=c.execute("SELECT token,phase FROM document_pending WHERE sid=? AND api_id=? AND state='scheduled'",(sid,api_id)).fetchall()
   if not error:
    for r in rows:c.execute('INSERT OR IGNORE INTO document_deliveries VALUES(?,?,?,?)',(r['token'],api_id,r['phase'],time.time()))
   c.execute('UPDATE document_pending SET state=? WHERE sid=? AND api_id=? AND state=\'scheduled\'',('failed' if error else 'received',sid,api_id))

 def status(self,sid,args):
  cid=args['corpus_id'];corpus=self.corpus(sid,cid);phases=json.loads(corpus['phases'])
  with self.store.db() as c:
   partition=c.execute('SELECT * FROM document_partitions WHERE id=?',(cid,)).fetchone();original=partition['parent'] if partition else cid;members={tuple(x) for x in json.loads(partition['members'])} if partition else None
   sources=[dict(r) for r in c.execute('SELECT id,path,sha256,format,status,body FROM document_sources WHERE corpus=? ORDER BY path',(original,))]
   expected=[(u['doc'],u['unit'],json.loads(u['body'])) for u in c.execute('SELECT u.* FROM document_units u JOIN document_sources s ON s.id=u.doc WHERE s.corpus=? ORDER BY u.doc,u.unit',(original,))]
   deliveries=[dict(r) for r in c.execute('SELECT p.* FROM document_pending p JOIN document_deliveries d ON d.token=p.token JOIN document_sources s ON s.id=p.doc WHERE s.corpus=?',(original,))]
   if members is not None:
    expected=[x for x in expected if (x[0],x[1]) in members];sources=[r for r in sources if any(x[0]==r['id'] for x in members)]
  stale={r['id'] for r in sources if r['status']=='extracted' and not current_decoder(r)}
  missing_sources=[{'id':r['id'],'path':r['path'],'status':'decoder_revision_stale' if r['id'] in stale else r['status']} for r in sources if r['status']!='extracted' or r['id'] in stale]
  by_phase={}
  for delivery in deliveries:by_phase.setdefault((delivery['phase'],delivery['doc'],delivery['unit']),[]).append((delivery['begin'],delivery['end']))
  phase_status={}
  for phase in phases:
   complete=0;gaps=[]
   for did,index,meta in expected:
    spans=sorted(by_phase.get((phase,did,index),[]))
    end=0
    for a,b in spans:
     if a>end:break
     end=max(end,b)
    has_receipt=bool(spans)
    ok=has_receipt and end>=meta['characters'] and not meta.get('unhandled_visuals') and did not in stale
    if ok:complete+=1
    elif len(gaps)<20:gaps.append({'doc_id':did,'unit':index,'covered_characters':end,'required':meta['characters'],'unhandled_visuals':meta.get('unhandled_visuals',False),'decoder_current':did not in stale})
   phase_status[phase]={'units_received_completely':complete,'units_expected':len(expected),'complete':bool(sources) and bool(expected) and not missing_sources and complete==len(expected),'gap_examples':gaps}
  start=args.get('offset',0);limit=args.get('limit',20)
  if type(start) is not int or start<0 or type(limit) is not int or not 1<=limit<=100:raise ValueError('document_page_invalid')
  view=[{k:r[k] for k in ['id','path','sha256','format','status']} for r in sources[start:start+limit]]
  return {'corpus_id':cid,'inventory_complete':corpus['status']=='inventoried','files_total':sum(r['format']!='directory' for r in sources),'entries_total':len(sources),'blocked_directories_count':sum(r['format']=='directory' for r in sources),'files_extracted':sum(r['status']=='extracted' and r['id'] not in stale for r in sources),'stale_decoder_sources_count':len(stale),
    'missing_sources_count':len(missing_sources),'missing_sources':missing_sources[:20],'sources':view,'has_more':start+limit<len(sources),'next_offset':start+limit if start+limit<len(sources) else None,
    'phases':phase_status,'model_delivery_complete':all(v['complete'] for v in phase_status.values()),'semantic_understanding_verified':False,'scientific_acceptance':False}
