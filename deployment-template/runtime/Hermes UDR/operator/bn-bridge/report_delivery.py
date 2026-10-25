"""Exact owner-authorized draft copy. No scientific acceptance or arbitrary target."""
import asyncio,hashlib,hmac,json,time,logging,io,os,tempfile,re
from pathlib import Path

def verify_grant(sid,run_id,expected_sha256,grant_id,artifact_id=None):
 import backend as b
 if not re.fullmatch('[a-f0-9]{64}',expected_sha256):raise PermissionError('exact_artifact_sha256_required')
 if not re.fullmatch('[a-f0-9]{32}',grant_id):raise PermissionError('operator_delivery_grant_required')
 path=b.HERE/'owner-grants'/(grant_id+'.json')
 if path.is_symlink():raise PermissionError('unsafe_delivery_grant')
 envelope=json.loads(path.read_text());grant=envelope['body'];key=(b.ROOT/'state/authority/bn-bridge.key').read_bytes()
 if not hmac.compare_digest(envelope['mac'],hmac.new(key,b.canonical(grant),hashlib.sha256).hexdigest()):raise PermissionError('delivery_grant_authentication_failed')
 if grant['sid']!=sid or grant['run_id']!=run_id or grant['sha256']!=expected_sha256 or grant['expires_at']<time.time():raise PermissionError('exact_delivery_grant_mismatch')
 if grant.get('artifact_id')!=artifact_id:raise PermissionError('exact_prepared_artifact_grant_required')
 if type(grant['chat_id']) is not int or not grant['authorization_source'].startswith('owner-authorized:'):raise PermissionError('owner_delivery_authority_required')
 return grant

def write_receipt(path,value):
 descriptor,name=tempfile.mkstemp(prefix='.delivery-',dir=path.parent)
 try:
  with os.fdopen(descriptor,'wb') as f:
   os.fchmod(f.fileno(),0o600);f.write(json.dumps(value,ensure_ascii=False).encode());f.flush();os.fsync(f.fileno())
  os.replace(name,path)
 finally:
  Path(name).unlink(missing_ok=True)

def deliver(sid,run_id,expected_sha256,grant_id,artifact_id=None):
 import backend as b
 grant=verify_grant(sid,run_id,expected_sha256,grant_id,artifact_id)
 if artifact_id:
  from prepared_file import registered
  body,s,item,raw=registered(sid,run_id,artifact_id,expected_sha256)
  filename=item['filename'];caption='Копия подготовленного файла. Научная приёмка не заявлена.'
 else:
  body=b.saved(sid)
  if not body or body.get('native_child') or body.get('managed_worker') or body['run_id']!=run_id or not body.get('completion'):raise PermissionError('completed_own_draft_required')
  s,artifacts=b.session(body);s.check()
  draft=s.state.get({'schema_version':1,'database':'kw_core','project_id':body['project'],'object_id':body['completion']['draft_ref']})['object']
  item=next(x for x in draft['artifacts'] if x['path']=='report.md');path=artifacts.originals/expected_sha256
  if path.is_symlink() or item['sha256']!=expected_sha256 or path.stat().st_size>64*1024*1024:raise PermissionError('canonical_delivery_bytes_mismatch')
  raw=path.read_bytes()
  if hashlib.sha256(raw).hexdigest()!=expected_sha256:raise PermissionError('canonical_delivery_bytes_mismatch')
  filename=grant.get('filename','Hermes-BN-UDR-document-check.md');caption='Копия сохранённого черновика. Научная приёмка не заявлена.'
 if not filename or len(filename)>240 or '/' in filename or '\\' in filename or any(ord(c)<32 for c in filename):raise PermissionError('safe_delivery_filename_required')
 target=b.digest(b.canonical({'platform':'telegram','chat_id':grant['chat_id'],'bot':grant['bot_name']}))
 identity={'run_id':run_id,'sha256':expected_sha256,'target':target}
 if artifact_id:identity['artifact_id']=artifact_id
 operation_key=b.digest(b.canonical(identity))
 receipt_path=b.HERE/'delivery-receipts'/(operation_key+'.json');receipt_path.parent.mkdir(mode=0o700,exist_ok=True)
 kind='bn_owner_prepared_file_copy' if artifact_id else 'bn_owner_draft_copy'
 input_hash=b.digest(b.canonical(identity)) if artifact_id else b.digest(b.canonical(grant))
 reserved=s.runtime.begin_external(kind,operation_key,input_hash,target)
 if reserved['status']=='already_succeeded':return {'status':'already_delivered','automatic_resend':False,'receipt':json.loads(receipt_path.read_text())}
 if reserved['status']!='owned':raise PermissionError('delivery_outcome_requires_reconciliation_no_resend:'+reserved['status'])
 async def send():
  from dotenv import dotenv_values
  from telegram import Bot
  home=Path(grant.get('transport_home') or b.ROOT.parent/'Hermes BN/data').resolve()
  bn=b.ROOT.parent/'Hermes BN';profiles=bn/'data/profiles'
  allowed=[bn/'data',*[p for p in profiles.iterdir() if p.is_dir()]] if profiles.is_dir() else [bn/'data']
  if home not in [p.resolve() for p in allowed]:raise PermissionError('configured_delivery_transport_required')
  env=dotenv_values(home/'.env');token=env.get('TELEGRAM_BOT_TOKEN') or env.get('HERMES_TELEGRAM_BOT_TOKEN')
  if not token:raise PermissionError('bot_credential_unavailable')
  logging.getLogger('httpx').setLevel(logging.CRITICAL);logging.getLogger('httpcore').setLevel(logging.CRITICAL)
  async with Bot(token) as bot:
   bot_identity=await bot.get_me()
   if bot_identity.username!=grant['bot_name']:raise PermissionError('wrong_owner_bot')
   msg=await bot.send_document(chat_id=grant['chat_id'],document=io.BytesIO(raw),filename=filename,caption=caption,read_timeout=40,write_timeout=40,connect_timeout=20)
   observed={'message_id':msg.message_id,'file_id':msg.document.file_id,'sha256':expected_sha256,'state':'observed_sent','filename':filename,'bytes':len(raw),'target_hash':target,'grant_id':grant_id,'artifact_id':artifact_id}
   write_receipt(receipt_path,observed)
   remote=await bot.get_file(msg.document.file_id);received=await remote.download_as_bytearray()
   if hashlib.sha256(received).hexdigest()!=expected_sha256:raise PermissionError('telegram_copy_hash_mismatch')
   return {**observed,'state':'delivered','readback_verified':True,'claims_accepted':False,'messages_sent':1,'second_poller_started':False}
 try:
  proof=asyncio.run(send());write_receipt(receipt_path,proof);s.runtime.finish_external(reserved['operation_id'],reserved['owner'],b.digest(b.canonical(proof)));return proof
 except BaseException:
  s.runtime.finish_external(reserved['operation_id'],reserved['owner'],None)
  raise
