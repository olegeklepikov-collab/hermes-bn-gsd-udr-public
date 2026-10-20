"""Host-owned parser integration. Signed SDK functions remain unchanged."""
from pathlib import Path
import hashlib,json,os,re,shutil,time

def digest(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  while b:=f.read(4*1024*1024):h.update(b)
 return h.hexdigest()
def atomic(p,v):
 tmp=p.with_name(p.name+'.pending');tmp.write_text(json.dumps(v,ensure_ascii=False,sort_keys=True));tmp.chmod(0o600);os.replace(tmp,p)
def receipt(original_id,source_path,source_sha,fmt,execution,index,reference):
 from hermes_research_report.intake import record_parse_runs
 original={'artifact_id':original_id,'intake_id':'BNI-'+source_sha[:24],'content_hash':source_sha,'byte_size':Path(source_path).stat().st_size,
  'detected_type':'pdf' if fmt=='pdf' else 'zip' if fmt in {'docx','xlsx','ods','pptx','odt','odp','epub'} else 'binary' if fmt in {'xls','sqlite','parquet'} else 'xml' if fmt=='xml' else 'json' if fmt=='json' else 'utf8_text',
  'detected_mime':'application/pdf' if fmt=='pdf' else 'application/octet-stream','storage_ref':str(source_path),
  'source':{'kind':'host_authorized_intake','reference':reference,'acquired_at':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())},
  'rights':{'status':'allowed','reference':'Processing within the existing host session scope; no redistribution right inferred'},
  'immutable':True,'readback_verified':True,'content_embedded':False}
 # Every observed step is retained. Native schema sets are grouped at 1000 entries, never truncated.
 receipts=Path(execution['execution_receipt_ref']).parent;sets=receipts.parent/'sdk-parse-records';sets.mkdir(exist_ok=True,mode=0o700)
 batch=[];setrefs=[];runs=0
 def persist(group):
  value=record_parse_runs({'schema_version':1,'original_artifact':original,'parser_runs':group})
  path=sets/('set-'+str(len(setrefs))+'.json');atomic(path,value);setrefs.append({'reference':str(path),'sha256':digest(path),'parse_count':len(group)})
 for path in sorted(receipts.glob('*.json')):
  item=json.loads(path.read_text())
  if item.get('original_sha256')!=source_sha or not item.get('sandbox_enforced') or item.get('status') not in {'partial','extracted'}:continue
  delta=Path(item.get('derived_delta_ref',index));expected=item.get('derived_delta_sha256')
  if delta.is_symlink() or (expected and digest(delta)!=expected):raise ValueError('parse_step_artifact_changed')
  batch.append({'parse_id':path.stem,'parser_id':'bn-deterministic-parser','parser_version':item['parser_version'],
   'parser_binary_hash':item['parser_binary_hash'],'configuration_hash':item['configuration_hash'],'resource_limits':item['resource_limits'],
   'elapsed_ms':item['elapsed_ms'],'warnings':['Extraction is not model reading or scientific acceptance'],
   'derived_representations':[{'kind':'addressed_unit_delta','reference':str(delta),'content_hash':digest(delta)}],'quality_ref':str(path)})
  runs+=1
  if len(batch)==1000:persist(batch);batch=[]
 if batch:persist(batch)
 if not runs:raise ValueError('no_observed_successful_parser_step')
 manifest=sets/'manifest.json';atomic(manifest,{'contract':'BNParseRunSetManifestV1','sets':setrefs,'runs':runs})
 return {'contract':'BNHostParseReceiptV1','original_artifact':original,'sdk_record_sets_ref':str(manifest),'sdk_record_sets_sha256':digest(manifest),
  'observed_parser_steps':runs,'native_recorder_performs_execution':False,'host_executor_invoked':True,'profile_id':'parser',
  'execution_receipt_ref':execution['execution_receipt_ref'],'sandbox_enforced':execution['sandbox_enforced'],'claims_accepted':False}

def register_parts(root,state_path,index,unit_dir,origin_id,parse_ref,source_url,title,source,limit=32):
 state=json.loads(state_path.read_text()) if state_path.exists() else {'index_offset':0,'registered_units':0,'complete':False}
 ids=[]
 with Path(index).open('rb') as f:
  f.seek(state['index_offset'])
  for _ in range(limit):
   line=f.readline()
   if not line:state['complete']=True;break
   unit=json.loads(line);p=Path(unit_dir)/(str(unit['index'])+'.txt')
   if p.is_symlink() or digest(p)!=unit['text_sha256']:raise ValueError('derived_source_integrity_failed')
   text=p.read_bytes().decode('utf-8')
   extent='excerpt'
   if not text.strip():text=json.dumps({'source_unit':unit['index'],'locator':unit['locator'],'visual_required':unit.get('visual_required',False),'text_unavailable':True});extent='metadata'
   result=source({'run_id':root.name,'url':source_url,'title':title+' — '+json.dumps(unit['locator'],ensure_ascii=False),'text':text,'extent':extent,'origin_ref':origin_id,'parse_receipt_ref':parse_ref})
   ids.append(result['source_id']);state['registered_units']+=1;state['index_offset']=f.tell();atomic(state_path,state)
 atomic(state_path,state)
 return {'status':'sources_registered' if state['complete'] else 'registration_partial','registered_units':state['registered_units'],'source_ids':ids,'registration_complete':state['complete'],'meaning_verified':False,'claims_accepted':False}

def web_step(sid,body,args,artifacts,put,state,source,root_for,config):
 from bn_memory.parser_host import run_step
 from bn_memory.documents import FORMATS
 root=root_for(body['run_id']);identifier=args['retrieval_id']
 if not re.fullmatch('[a-f0-9]{32}',identifier):raise ValueError('invalid_retrieval_id')
 folder=root/'retrievals'/identifier
 if folder.is_symlink() or not folder.resolve().is_relative_to(root.resolve()):raise PermissionError('retrieval_outside_run')
 raw=folder/'original.bin';meta=json.loads((folder/'metadata.json').read_text())
 if raw.is_symlink() or digest(raw)!=meta['original_sha256']:raise ValueError('raw_original_integrity_failed')
 originals=folder/'host-original';originals.mkdir(exist_ok=True,mode=0o700);frozen=originals/(meta['original_sha256']+'.bin')
 if not frozen.exists():
  shutil.copyfile(raw,frozen);frozen.chmod(0o400)
 if frozen.is_symlink() or digest(frozen)!=meta['original_sha256']:raise ValueError('host_original_intake_readback_failed')
 suffix=Path(__import__('urllib.parse',fromlist=['urlsplit']).urlsplit(meta['final_url']).path).suffix.lower();fmt='pdf' if raw.open('rb').read(8).startswith(b'%PDF') else FORMATS.get(suffix,'html' if 'html' in meta['content_type'] else 'xml' if 'xml' in meta['content_type'] else 'text')
 execution=run_step({'path':str(frozen),'format':fmt,'output':str(folder/'host-parser'),'expected_sha256':meta['original_sha256'],'xls_java':config.get('xls_java')},config['document_python'],config.get('parser_limits'))
 result={'retrieval_id':identifier,**execution,'parser_complete':execution['status']=='extracted','next_action':'parse' if execution['status']=='partial' else None}
 if execution['status']!='extracted':return result
 receipt_file=folder/'host-parse-receipt.json'
 if receipt_file.exists():proof=json.loads(receipt_file.read_text())
 else:
  proof=receipt('BNORIG-'+meta['original_sha256'][:24],frozen,meta['original_sha256'],fmt,execution,execution['unit_index'],meta['final_url']);atomic(receipt_file,proof)
 oid='BNP-'+hashlib.sha256(json.dumps(proof,sort_keys=True).encode()).hexdigest()[:24];put(state,proof,body['project'],oid,body['host_run'])
 reg=register_parts(root,folder/'registration.json',execution['unit_index'],execution['output_directory'],proof['original_artifact']['artifact_id'],oid,meta['final_url'],args.get('title',meta['final_url']),source)
 return {**result,**reg,'parse_receipt_ref':oid,'host_parse_receipt':str(receipt_file),'next_action':None if reg['registration_complete'] else 'parse'}

def document_step(sid,body,args,docs,put,state,source,root_for):
 did=args['doc_id'];cid=args['corpus_id']
 if not docs.membership(sid,cid,did):raise PermissionError('document_not_in_corpus')
 row=docs.source(sid,did)
 if row['status']!='extracted':return {'status':'document_extract_required','doc_id':did,'corpus_id':cid}
 meta=row['metadata'];root=root_for(body['run_id']);folder=root/'document-intakes'/did;folder.mkdir(parents=True,exist_ok=True,mode=0o700)
 raw=Path(meta['snapshot'])
 if digest(raw)!=row['sha256']:raise ValueError('document_original_changed')
 receipt_file=folder/'host-parse-receipt.json'
 if receipt_file.exists():proof=json.loads(receipt_file.read_text())
 else:
  proof=receipt(did,raw,row['sha256'],row['format'],meta,meta['unit_index'],'document:'+did);atomic(receipt_file,proof)
 oid='BNP-'+hashlib.sha256(json.dumps(proof,sort_keys=True).encode()).hexdigest()[:24];put(state,proof,body['project'],oid,body['host_run'])
 registered=register_parts(root,folder/'registration.json',meta['unit_index'],meta['parse_output'],did,oid,'https://local.invalid/bn-document/'+row['sha256'],'Owner-provided document',source)
 return {**registered,'doc_id':did,'parse_receipt_ref':oid,'host_parse_receipt':str(receipt_file),'next_action':None if registered['registration_complete'] else 'intake'}
