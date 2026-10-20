#!/usr/bin/env python3
"""Initialize neutral memory locally; no services, accounts or controllers activated."""
from pathlib import Path
import os,json,sys,secrets,uuid,hashlib,subprocess
A=Path(__file__).resolve().parents[1];B=A/'runtime/Hermes BN';U=A/'runtime/Hermes UDR';M=B/'Memory';C=B/'Cognee'
if (M/'settings.json').exists() or (M/'state/memory.sqlite').exists():raise SystemExit('Existing memory: refuse replacement. Extract a fresh copy.')
if not (A/'deployment/prepared.json').exists() or not (A/'deployment/UDR-prepared.json').exists():raise SystemExit('Prepare BN and UDR first, including relocation of their interpreters.')
cfg=json.loads((M/'settings.template.json').read_text());sub={'__HERMES_BN_ROOT__':str(B),'__HERMES_UDR_ROOT__':str(U),'__USER_HOME__':str(Path.home())}
def convert(v):
 if isinstance(v,str):
  for a,b in sub.items():v=v.replace(a,b)
  return v
 if isinstance(v,list):return [convert(x) for x in v]
 if isinstance(v,dict):return {k:convert(x) for k,x in v.items()}
 return v
cfg=convert(cfg)
for p in [M/'state',C/'state',C/'state/engine',C/'state/lesson-engines',C/'state/originals']:p.mkdir(mode=0o700,parents=True,exist_ok=True);p.chmod(0o700)
fd=os.open(cfg['host_key'],os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(secrets.token_bytes(32))
sys.path.insert(0,cfg['package_root']);from bn_memory.store import Store
Store(cfg['state_root'],cfg).initialize()
(C/'state/instance.json').write_text(json.dumps({'instance_id':str(uuid.uuid4())}));(C/'state/instance.json').chmod(0o600)
(M/'settings.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2));(M/'settings.json').chmod(0o600)
subprocess.run([sys.executable,str(A/'deployment/configure-parser.py')],check=True)
# Refresh substituted package integrity, preserving provider wheels and their signatures.
manifest=Path(cfg['package_root'])/'manifest.json'
if manifest.exists():
 d=json.loads(manifest.read_text())
 if isinstance(d,dict):
  for k,v in list(d.items()):
   p=manifest.parent/k
   if isinstance(v,str) and len(v)==64 and p.is_file():d[k]=hashlib.sha256(p.read_bytes()).hexdigest()
  manifest.write_text(json.dumps(d,indent=2))
(A/'deployment/Memory-prepared.json').write_text(json.dumps({'fresh_state':True,'fresh_key':True,'fresh_cognee_instance':True,'services_started':False,'controllers_connected':False,'remote_calls':0},indent=2))
print('Fresh SQLite, authority and Cognee namespace created; own service credentials and controller activation remain required.')
