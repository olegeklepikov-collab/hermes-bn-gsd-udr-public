import os
from pathlib import Path
import json,sys,time
W=Path(__file__).resolve().parents[1];B=Path(os.environ['HERMES_BN_ROOT']);sys.path.insert(0,str(B/'hermes-agent'))
from hermes_cli.config import load_config_readonly
from tools.mcp_tool_discovery import register_mcp_servers
from hermes_cli.lifecycle import invoke_hook
import model_tools
x=json.loads((W/'evidence/native-e2e-latest.json').read_text());prior=json.loads(Path(x['result']).read_text());sid='bn-repair-restart-'+str(time.time_ns())
c=load_config_readonly();register_mcp_servers({n:c['mcp_servers'][n] for n in ['udr','context']});invoke_hook('on_session_start',session_id=sid,platform='cli');invoke_hook('pre_llm_call',user_message='Повторно прочитать завершённый учебный отчёт после перезапуска.',session_id=sid,platform='cli',turn_id=sid)
def call(action,**kw):
 r=json.loads(model_tools.handle_function_call('mcp__udr__udr_research',{'request':{'action':action,**kw}},session_id=sid,tool_call_id=sid+'-'+str(time.time_ns())))
 if 'error' in r:raise RuntimeError(r)
 v=r.get('result',r);return json.loads(v) if isinstance(v,str) else v
resumed=call('resume',run_id=prior['run_id']);read=call('read',path='report.md');state=call('status')
assert read['sha256']==prior['readback']['sha256']
assert state['run_id']==prior['run_id'] and state['bead_id']==prior['native_state']['bead_id']
proof={'passed':True,'run_id_preserved':True,'bead_id_preserved':True,'report_sha256':read['sha256'],'new_session':sid,'model_calls':0,'run_phase':state.get('phase'),'resume_after_gateway_restart':True}
(W/'evidence/restart-readback.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps(proof,ensure_ascii=False),flush=True)
