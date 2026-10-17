#!/usr/bin/env python3
"""Activate the supplied GSD with fresh local keys; no provider sign-in or inherited state."""
from pathlib import Path
import json,subprocess,sys,os,importlib.util
B=Path(__file__).resolve().parents[1];R=B/'runtime/Hermes BN';P=R/'GSD/releases/0.2.13-hermes-0.22.2-r3';RR=Path(sys.argv[1]).resolve();PY=R/'hermes-agent/venv/bin/python'
if (R/'GSD/operator/settings.json').exists() or (R/'GSD/state/state.sqlite3').exists():raise SystemExit('Existing GSD state: refuse reset or key replacement')
args=[str(PY),str(P/'configure_profile.py'),'--home',str(R/'data'),'--core',str(R/'hermes-agent'),'--bundle',str(R/'GSD/vendor/1.1.0'),'--operator',str(R/'GSD/operator'),'--state',str(R/'GSD/state'),'--workspace',str(R/'workspace'),'--runtime-root',str(R),'--r-runtime',str(RR),'--provider','openai-codex','--model','gpt-6.1-sol','--apply']
env=os.environ.copy();env['HERMES_HOME']=str(R/'data');env['PYTHONDONTWRITEBYTECODE']='1'
for name in list(env):
 if name.endswith(('_API_KEY','_ACCESS_TOKEN','_REFRESH_TOKEN')) or name in ['OPENAI_BASE_URL','HERMES_PROFILE','HERMES_SHARED_AUTH_DIR']:env.pop(name,None)
p=subprocess.run(args,env=env,capture_output=True,text=True);assert p.returncode==0,p.stderr
decoder=json.JSONDecoder();rest=p.stdout.strip();objects=[]
while rest:
 obj,end=decoder.raw_decode(rest);objects.append(obj);rest=rest[end:].lstrip()
result=next(x for x in reversed(objects) if isinstance(x,dict) and 'snapshot' in x);snapshot=Path(result['snapshot']);spec=importlib.util.spec_from_file_location('fresh_rollback',R/'GSD/operations/guarded_rollback.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);pin=m.seal(snapshot,R/'data',P/'rollback_profile.py')
q=R/'GSD/operator/rollback-0.2.3-pin.json';q.write_text(json.dumps({'snapshot':str(snapshot),'manifest_sha256':pin,'operator_entry':str(R/'bin/hermes-bn-gsd-rollback'),'scope':'fresh installation only; no old owner data or accounting'},indent=2));q.chmod(0o600)
(B/'deployment/GSD-prepared.json').write_text(json.dumps({'engine':'3.0.3','adapter':'0.2.13','fresh_keys':True,'new_state':True,'mandatory_controls':['tool','tool_result','llm','auxiliary'],'model_signin':False,'services_started':False},indent=2))
print('Fresh GSD keys/state and required controls prepared; account sign-in remains the new owner action.')
