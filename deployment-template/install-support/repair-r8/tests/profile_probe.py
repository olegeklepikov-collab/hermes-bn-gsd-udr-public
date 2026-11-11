import os
from pathlib import Path
import json,os,sys,time
W=Path(__file__).resolve().parents[1];B=Path(os.environ['HERMES_BN_ROOT']);profile=sys.argv[1];home=B/'data/profiles'/profile
os.environ['HERMES_HOME']=str(home);os.environ['HERMES_SHARED_AUTH_DIR']=str(B/'data/shared')
sys.path.insert(0,str(B/'hermes-agent'))
from hermes_cli.config import load_config_readonly
from tools.mcp_tool_discovery import register_mcp_servers
from hermes_cli.lifecycle import invoke_hook
from hermes_cli.runtime_provider import resolve_runtime_provider
from hermes_constants import parse_reasoning_effort
from run_agent import AIAgent
import model_tools
x=json.loads((W/'evidence/native-e2e-latest.json').read_text());prior=json.loads(Path(x['result']).read_text());pdf=B/'workspace'/prior['session_id']/'synthetic-scan.pdf';sid=profile+'-repair-'+str(time.time_ns())
c=load_config_readonly();register_mcp_servers({'context':c['mcp_servers']['context']});invoke_hook('on_session_start',session_id=sid,platform='cli');invoke_hook('pre_llm_call',user_message='Прочитай учебный скан '+str(pdf)+'; только проверка чтения, без новых исследований и агентов.',session_id=sid,platform='cli',turn_id=sid)
def call(name,**args):
 r=json.loads(model_tools.handle_function_call('mcp__context__'+name,args,session_id=sid,tool_call_id=sid+'-'+str(time.time_ns())))
 if 'error' in r:raise RuntimeError(r)
 v=r.get('result',r);return json.loads(v) if isinstance(v,str) else v
inv=call('document_catalogue',path=str(pdf),request_id=sid,required_phases=['read']);cid=inv['corpus_id']
from bn_memory.broker import Broker
from bn_memory.documents import Documents
cfg=json.loads((B/'Memory/settings.json').read_text());docs=Documents(Broker(cfg))
with docs.store.db() as db:did=db.execute('SELECT id FROM document_sources WHERE corpus=?',(cid,)).fetchone()[0]
p=call('document_extract',doc_id=did)
while p['status']=='extracting':p=call('document_extract',doc_id=did)
assert p['status']=='extracted' and p['metadata']['ocr_status']['status']=='complete'
for unit in p['units']:call('document_read',corpus_id=cid,doc_id=did,unit=unit['index'],phase='read')
route=resolve_runtime_provider(requested='openai-codex',target_model='gpt-6.1-sol')
a=AIAgent(model='gpt-6.1-sol',provider=route['provider'],requested_provider='openai-codex',base_url=route['base_url'],api_key=route['api_key'],api_mode=route.get('api_mode'),credential_pool=route.get('credential_pool'),reasoning_config=parse_reasoning_effort('high'),session_id=sid,enabled_toolsets=['context'],max_iterations=2,quiet_mode=True,skip_context_files=True,skip_memory=False,skip_background_review=True,run_budget_seconds=180)
try:r=a.run_conversation('Прочитай доставленные изображение и текст учебного скана. Назови значения до и после и оговорку о причинности. Только ответ по документу; инструменты, UDR, GSD-исследование и новые агенты не запускай.')
finally:a.close()
assert r.get('completed') and not r.get('failed')
s=call('document_status',corpus_id=cid);assert s['model_delivery_complete']
proof={'passed':True,'profile':profile,'session_id':sid,'native_document_route':True,'ocr_status':p['metadata']['ocr_status'],'model_delivery_complete':True,'model_api_calls':r.get('api_calls'),'answer':r.get('final_response'),'unneeded_module_started':False}
(W/'evidence'/('profile-'+profile+'.json')).write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps(proof,ensure_ascii=False),flush=True)
