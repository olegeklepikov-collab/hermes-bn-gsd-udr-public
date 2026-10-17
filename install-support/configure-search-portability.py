#!/usr/bin/env python3
"""Plan/apply four known timezone placeholders and profile-scoped Tavily paths; no service starts or credentials."""
import argparse,hashlib,json,os,tempfile
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import yaml

def sha(b):return hashlib.sha256(b).hexdigest()
def canon(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def main():
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--timezone',required=True);p.add_argument('--apply',action='store_true');p.add_argument('--expected-plan-sha256');a=p.parse_args();ZoneInfo(a.timezone)
 root=a.root.expanduser().resolve();bn=root/'runtime/Hermes BN'
 if not (root/'deployment/prepared.json').is_file():raise ValueError('Prepare the independent BN first')
 changes={};code_changes={}
 def offer(path,new):
  if path.is_symlink():raise ValueError('Refuse symlink file')
  old=path.read_bytes()
  if old!=new:changes[path]=(old,new)
 for service in ['Crossref','OpenAlex','PubMed','SemanticScholar']:
  path=bn/service/'api.py';old=path.read_bytes()
  if b'__TIMEZONE__' in old:
   new=old.replace(b'__TIMEZONE__',a.timezone.encode());offer(path,new);code_changes[str(path)]=(sha(old),sha(new))
 homes=[bn/'data',bn/'data/profiles/bn-gsd-only',bn/'data/profiles/bn-udr-only']
 for home in homes:
  path=home/'config.yaml'
  if not path.is_file():continue
  cfg=yaml.safe_load(path.read_bytes()) or {};server=cfg.get('mcp_servers',{}).get('tavily');changed=False
  if server:
   if server.get('url') or not server.get('command'):raise ValueError('Expected bundled local Tavily; review a custom transport separately')
   env=server.setdefault('env',{});values={'HERMES_HOME':str(home),'HERMES_BN_ROOT':str(bn),'PYTHONPATH':str(bn/'hermes-agent')+':'+str(bn/'Tavily')}
   for k,v in values.items():
    if env.get(k)!=v:env[k]=v;changed=True
   if changed:offer(path,yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False).encode())
  entry=cfg.get('plugins',{}).get('entries',{}).get('bn-gsd',{})
  if not entry.get('enabled',False):continue
  settingspath=Path(entry['settings']['settings_file'])
  if not settingspath.exists():
   if (root/'deployment/FINALIZED.json').exists():raise ValueError('Missing settings in finalized profile')
   continue # Independent fresh profiles receive settings during finalization.
  s=json.loads(settingspath.read_bytes());dirty=False
  for code,(old_hash,new_hash) in code_changes.items():
   if code not in s.get('local_adapter_sha256',{}):continue
   if s['local_adapter_sha256'][code]!=old_hash:raise ValueError('Existing code admission mismatch; no blind repair')
   s['local_adapter_sha256'][code]=new_hash;dirty=True
  if changed:
   policy=Path(s['tool_policy']);raw=policy.read_bytes()
   if sha(raw)!=s['tool_policy_sha256']:raise ValueError('Policy integrity failed')
   policy_body=json.loads(raw)
   if policy_body.get('version')!=1:raise ValueError('Unsupported tool policy version')
   if not any(x.get('server')=='tavily' for x in policy_body['entries'].values()):raise ValueError('Tavily is not an admitted existing server')
   oldcfg=yaml.safe_load(path.read_bytes())['mcp_servers']['tavily'];admitted=s.get('mcp_transport_digests',{}).get('tavily')
   if admitted!=sha(canon(oldcfg)):raise ValueError('Review pending Tavily changes with admit-mcp-transport.py before path relocation')
   s['mcp_transport_digests']['tavily']=sha(canon(server));dirty=True
  if dirty:offer(settingspath,json.dumps(s,ensure_ascii=False,indent=2).encode()+b'\n')
 changes=dict(sorted(changes.items()))
 plan={'timezone':a.timezone,'changes':[{'path':str(q),'backup_file':str(i)+'.before','before_sha256':sha(v[0]),'after_sha256':sha(v[1])} for i,(q,v) in enumerate(changes.items())],'credentials_changed':False,'states_or_keys_created':False,'services_started':False}
 plan_hash=sha(canon(plan));print(json.dumps({'plan_sha256':plan_hash,**plan},ensure_ascii=False,indent=2))
 if not a.apply:return
 if a.expected_plan_sha256!=plan_hash:raise ValueError('Explicit current plan hash required')
 if not changes:print('No changes required');return
 for q,(old,new) in changes.items():
  if q.read_bytes()!=old:raise ValueError('Concurrent change; no mutation started')
 backup=root/'deployment/search-portability-checkpoints'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');backup.mkdir(mode=0o700,parents=True)
 for i,(q,(old,new)) in enumerate(changes.items()):
  f=backup/(str(i)+'.before');f.write_bytes(old);f.chmod(0o600)
 (backup/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2));(backup/'plan.json').chmod(0o600)
 # Checkpoint is complete before the first write. A partial OS failure is recovered from that exact checkpoint.
 for q,(old,new) in changes.items():
  if q.read_bytes()!=old:raise ValueError('Concurrent change; restore exact checkpoint before retry')
  mode=q.stat().st_mode&0o777;fd,name=tempfile.mkstemp(prefix='.search-config-',dir=q.parent)
  try:
   with os.fdopen(fd,'wb') as f:f.write(new);f.flush();os.fsync(f.fileno());os.fchmod(f.fileno(),mode)
   os.replace(name,q)
  finally:
   if os.path.exists(name):os.unlink(name)
 print(json.dumps({'applied':True,'checkpoint':str(backup),'changed_files':len(changes)}))
if __name__=='__main__':main()
