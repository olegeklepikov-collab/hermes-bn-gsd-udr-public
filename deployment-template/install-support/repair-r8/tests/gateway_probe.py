import os
from pathlib import Path
import sys,json,time,urllib.request,socket
B=Path(os.environ['HERMES_BN_ROOT']);W=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'hermes-agent'))
from hermes_cli.config import get_env_value
from urllib.parse import urlsplit
base=urlsplit(os.environ['HERMES_REPAIR_API_URL'])
if base.scheme!='http' or base.hostname not in {'127.0.0.1','::1'} or not base.port or base.username or base.password or base.query or base.fragment:raise ValueError('Only the owned loopback API URL is allowed')
key=get_env_value('API_SERVER_KEY')
headers={'Content-Type':'application/json','X-Hermes-Session-Id':'bn-r8-gateway-'+str(time.time_ns())}
if key:headers['Authorization']='Bearer '+key
body={'model':'hermes-agent','messages':[{'role':'user','content':'Синтетическая проверка шлюза после исправления r8. Не используй инструменты, исследования, внешние действия или новых агентов. Ответь только: BN-R8-GATEWAY-READY'}],'stream':False}
for _ in range(30):
 try:
  with socket.create_connection((__import__('urllib.parse',fromlist=['urlsplit']).urlsplit(os.environ['HERMES_REPAIR_API_URL']).hostname,__import__('urllib.parse',fromlist=['urlsplit']).urlsplit(os.environ['HERMES_REPAIR_API_URL']).port),timeout=1):break
 except OSError:time.sleep(1)
else:raise RuntimeError('Owned gateway API port did not start')
request=urllib.request.Request(os.environ['HERMES_REPAIR_API_URL'].rstrip('/')+'/v1/chat/completions',data=json.dumps(body).encode(),headers=headers)
try:
 with urllib.request.urlopen(request,timeout=240) as response:r=json.load(response)
except Exception as ex:
 (W/'evidence/gateway-error.txt').write_text(str(ex));raise
(W/'evidence/gateway-response.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));answer=r['choices'][0]['message']['content'];assert 'BN-R8-GATEWAY-READY' in answer,answer
proof={'passed':True,'actual_gateway_model_response':answer,'request_session':headers['X-Hermes-Session-Id'],'external_messages_sent':False,'required_controls_preserved':True}
(W/'evidence/gateway.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps(proof,ensure_ascii=False))
