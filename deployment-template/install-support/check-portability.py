import os
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[1])
from pathlib import Path
import tempfile,subprocess,json,sys,hashlib
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp);(p/'deployment').mkdir();(p/'deployment/prepared.json').write_text('{}');bn=p/'runtime/Hermes BN';home=bn/'data';home.mkdir(parents=True);policy=p/'policy.json';policy.write_text(json.dumps({'version':1,'entries':{'x':{'server':'tavily'}}}));settings=p/'settings.json';old={}
 for n in ['Crossref','OpenAlex','PubMed','SemanticScholar']:
  q=bn/n/'api.py';q.parent.mkdir();q.write_text("TZ='__TIMEZONE__'\n");old[str(q)]=hashlib.sha256(q.read_bytes()).hexdigest()
 server={'command':'python','enabled':False,'env':{'PYTHONPATH':'/old/Tavily'}};h=lambda x:hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest();settings.write_text(json.dumps({'tool_policy':str(policy),'tool_policy_sha256':hashlib.sha256(policy.read_bytes()).hexdigest(),'mcp_transport_digests':{'tavily':h(server)},'local_adapter_sha256':old,'limits':{'unchanged':True}}));cfg={'mcp_servers':{'tavily':server},'plugins':{'version':1,'entries':{'bn-gsd':{'enabled':True,'settings':{'settings_file':str(settings)}}}}};(home/'config.yaml').write_text(json.dumps(cfg));cmd=[sys.executable,'install-support/configure-search-portability.py','--root',str(p),'--timezone','UTC'];r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,r.stderr;plan=json.loads(r.stdout);assert len(plan['changes'])==6
 r=subprocess.run(cmd+['--apply','--expected-plan-sha256',plan['plan_sha256']],capture_output=True,text=True);assert r.returncode==0,r.stderr
 for n in ['Crossref','OpenAlex','PubMed','SemanticScholar']:assert "'UTC'" in (bn/n/'api.py').read_text()
 assert json.loads(settings.read_text())['limits']=={'unchanged':True}
 r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0 and not json.loads(r.stdout)['changes']
 r=subprocess.run(cmd+['--apply','--expected-plan-sha256',plan['plan_sha256']],capture_output=True,text=True);assert r.returncode!=0
 # Fresh alternate GSD profile has no settings until finalize-prepared.py.
 alt=bn/'data/profiles/bn-gsd-only';alt.mkdir(parents=True);cfg['plugins']['entries']['bn-gsd']['settings']['settings_file']=str(p/'not-created-yet.json');(alt/'config.yaml').write_text(json.dumps(cfg));r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,r.stderr
print('PASS: known timezone/profile changes, matching code/transport admissions, preserved limits, no-op repeat, stale plan rejected')
