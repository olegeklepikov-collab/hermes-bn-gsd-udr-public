import os
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[1])
from pathlib import Path
import tempfile,json,hashlib,subprocess,sys
sys.path.insert(0,'install-support');import importlib.util
spec=importlib.util.spec_from_file_location('admission','install-support/admit-mcp-transport.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp);home=p/'profile';home.mkdir();policy=p/'policy.json';policy.write_text(json.dumps({'version':1,'entries':{'mcp__tavily__tavily_search':{'server':'tavily'}}}));settings=p/'settings.json';s={'tool_policy':str(policy),'tool_policy_sha256':m.sha(policy.read_bytes()),'mcp_transport_digests':{'tavily':'old','unrelated':'retain'},'limits':{'budget_mode':'observe'},'state_dir':'unchanged','local_adapter_sha256':{}};settings.write_text(json.dumps(s));cfg={'plugins':{'version':1,'entries':{'bn-gsd':{'enabled':True,'settings':{'settings_file':str(settings)}}}},'mcp_servers':{'tavily':{'command':'/own/python','enabled':True}}};(home/'config.yaml').write_text(json.dumps(cfg));cmd=[sys.executable,'install-support/admit-mcp-transport.py','--home',str(home),'--server','tavily'];original=settings.read_bytes()
 def run(extra=(),ok=True):
  r=subprocess.run(cmd+list(extra),capture_output=True,text=True);assert (r.returncode==0)==ok,r.stderr;return json.loads(r.stdout) if ok else None
 plan=run();assert settings.read_bytes()==original
 run(['--apply'],False);assert settings.read_bytes()==original
 flags=['--apply','--expected-config-sha256',plan['config_sha256'],'--expected-settings-sha256',plan['settings_sha256']];applied=run(flags);after=json.loads(settings.read_text());assert after['state_dir']==s['state_dir'] and after['limits']==s['limits'] and after['mcp_transport_digests']['unrelated']=='retain';assert Path(applied['backup']).read_bytes()==original
 plan=run();run(['--apply','--expected-config-sha256',plan['config_sha256'],'--expected-settings-sha256',plan['settings_sha256']]);assert len(list((p/'transport-admissions').glob('*.receipt.json')))==1
 cfg['mcp_servers']['tavily']['url']='https://changed.invalid';(home/'config.yaml').write_text(json.dumps(cfg));run(flags,False)
 policy.write_text('{}');run([],False)
print('PASS: read-only plan, explicit hashes, narrow update and backup, no-op repeat, stale plan rejected, corrupt policy rejected')
