"""Exact owner-authorized draft copy. No scientific acceptance or arbitrary target."""
import asyncio,hashlib,hmac,json,time,logging
from pathlib import Path

def verify_grant(sid,run_id,expected_sha256,grant_id):
 import backend as b
 if not __import__('re').fullmatch('[a-f0-9]{32}',grant_id):raise PermissionError('operator_delivery_grant_required')
 path=b.HERE/'owner-grants'/(grant_id+'.json')
 if path.is_symlink():raise PermissionError('unsafe_delivery_grant')
 envelope=json.loads(path.read_text());grant=envelope['body'];key=(b.ROOT/'state/authority/bn-bridge.key').read_bytes()
 if not hmac.compare_digest(envelope['mac'],hmac.new(key,b.canonical(grant),hashlib.sha256).hexdigest()):raise PermissionError('delivery_grant_authentication_failed')
 if grant['sid']!=sid or grant['run_id']!=run_id or grant['sha256']!=expected_sha256 or grant['expires_at']<time.time():raise PermissionError('exact_delivery_grant_mismatch')
 if type(grant['chat_id']) is not int or not grant['authorization_source'].startswith('owner-authorized:'):raise PermissionError('owner_delivery_authority_required')
 return grant

def deliver(sid,run_id,expected_sha256,grant_id):
 import backend as b
 grant=verify_grant(sid,run_id,expected_sha256,grant_id);body=b.saved(sid)
 if not body or body.get('native_child') or body.get('managed_worker') or body['run_id']!=run_id or not body.get('completion'):raise PermissionError('completed_own_draft_required')
 s,artifacts=b.session(body);s.check()
 draft=s.state.get({'schema_version':1,'database':'kw_core','project_id':body['project'],'object_id':body['completion']['draft_ref']})['object']
 item=next(x for x in draft['artifacts'] if x['path']=='report.md');path=artifacts.originals/expected_sha256
 if path.is_symlink() or item['sha256']!=expected_sha256 or hashlib.sha256(path.read_bytes()).hexdigest()!=expected_sha256:raise PermissionError('canonical_delivery_bytes_mismatch')
 target=b.digest(b.canonical({'platform':'telegram','chat_id':grant['chat_id'],'bot':grant['bot_name']}));operation_key=b.digest(b.canonical({'run_id':run_id,'sha256':expected_sha256,'target':target}))
 receipt_path=b.HERE/'delivery-receipts'/(operation_key+'.json');receipt_path.parent.mkdir(mode=0o700,exist_ok=True)
 reserved=s.runtime.begin_external('bn_owner_draft_copy',operation_key,b.digest(b.canonical(grant)),target)
 if reserved['status']=='already_succeeded':return {'status':'already_delivered','automatic_resend':False,'receipt':json.loads(receipt_path.read_text())}
 if reserved['status']!='owned':raise PermissionError('delivery_outcome_requires_reconciliation_no_resend:'+reserved['status'])
 async def send():
  from dotenv import dotenv_values
  from telegram import Bot
  env=dotenv_values(b.ROOT.parent/'Hermes BN/data/.env');token=env.get('TELEGRAM_BOT_TOKEN') or env.get('HERMES_TELEGRAM_BOT_TOKEN')
  if not token:raise PermissionError('bot_credential_unavailable')
  logging.getLogger('httpx').setLevel(logging.CRITICAL);logging.getLogger('httpcore').setLevel(logging.CRITICAL)
  async with Bot(token) as bot:
   identity=await bot.get_me()
   if identity.username!=grant['bot_name']:raise PermissionError('wrong_owner_bot')
   with path.open('rb') as file:msg=await bot.send_document(chat_id=grant['chat_id'],document=file,filename='Hermes-BN-UDR-document-check.md',caption='Синтетическая проверка: сохранённый черновик, научная приёмка не заявлена.',read_timeout=40,write_timeout=40,connect_timeout=20)
   observed={'message_id':msg.message_id,'file_id':msg.document.file_id,'sha256':expected_sha256,'state':'observed_sent'}
   receipt_path.write_text(json.dumps(observed));receipt_path.chmod(0o600)
   remote=await bot.get_file(msg.document.file_id);raw=await remote.download_as_bytearray()
   if hashlib.sha256(raw).hexdigest()!=expected_sha256:raise PermissionError('telegram_copy_hash_mismatch')
   return {**observed,'state':'delivered','readback_verified':True,'claims_accepted':False,'messages_sent':1,'second_poller_started':False,'target_hash':target,'grant_id':grant_id}
 try:
  proof=asyncio.run(send());receipt_path.write_text(json.dumps(proof));receipt_path.chmod(0o600);s.runtime.finish_external(reserved['operation_id'],reserved['owner'],b.digest(b.canonical(proof)));return proof
 except BaseException:
  s.runtime.finish_external(reserved['operation_id'],reserved['owner'],None)
  raise
