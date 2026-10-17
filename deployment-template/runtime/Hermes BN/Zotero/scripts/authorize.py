"""Request a native Zotero grant. Persist the result privately; never print a key."""
import json,os,sys
from pathlib import Path
import httpx
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'config/identity.json').read_text())
with httpx.Client(timeout=1800,trust_env=False,follow_redirects=False) as client:
    r=client.post(c['base_url']+'local/authorize',json={'appName':'Hermes BN — AgentRuntime2'},
                  headers={'Zotero-Server-ID':c['server_id'],'Zotero-API-Version':'3'})
if r.status_code!=200:
    print(json.dumps({'ok':False,'http_status':r.status_code}));sys.exit(2)
data=r.json()
if not data.get('remember'):
    print(json.dumps({'ok':False,'error':'Persistent authorization was not selected'}));sys.exit(2)
data.update(server_id=c['server_id'],app_name='Hermes BN — AgentRuntime2')
path=ROOT/'config/authorization.json'
fd=os.open(path,os.O_CREAT|os.O_WRONLY|os.O_EXCL,0o600)
with os.fdopen(fd,'w') as f:json.dump(data,f)
print(json.dumps({'ok':True,'persistent_key_saved':True,'server_id':c['server_id']}))
