"""Plan, apply and roll back a bounded BN parser/profile repair without resetting state."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,time
import yaml
VERSION='2026-11-11-r8';PACKAGE='1.4.2'
KNOWN_BASELINES={'parser_host.py':{'a65b0249537fa6bc08b937e503a142984456d37e6b25041b58e14883a36e1575'},'document_worker.py':{'54ae0ffe42cd79fb21f86b21c055bfb45e3f2ce0cc0b58f891e711552f1b539d'}}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def atom(path,raw,mode=0o600):
 p=Path(path);tmp=p.with_name(p.name+'.repair.tmp')
 fd=os.open(tmp,os.O_WRONLY|os.O_CREAT|os.O_EXCL,mode)
 with os.fdopen(fd,'wb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
def homes(b):return [b/'data',b/'data/profiles/bn-gsd-only',b/'data/profiles/bn-udr-only']
def replace(v,sub):
 if isinstance(v,str):
  for a,b in sub.items():v=v.replace(a,b)
  return v
 if isinstance(v,list):return [replace(x,sub) for x in v]
 if isinstance(v,dict):return {k:replace(x,sub) for k,x in v.items()}
 return v

def plan(b,u,profiles_only=False,connect=False):
 settings=b/'Memory/settings.json'
 if settings.is_symlink():raise ValueError('Symlink settings need separate review')
 if not settings.is_file():raise ValueError('Prepare the independent instance before repairing an installed copy')
 cfg=json.loads(settings.read_text());old=Path(cfg['package_root']).resolve();new=old if profiles_only else b/'Memory/releases'/PACKAGE
 if old.name not in {'1.4.0','1.4.1',PACKAGE} or not old.is_relative_to((b/'Memory/releases').resolve()):raise ValueError('Unsupported memory package; do not overwrite unrelated revision')
 expected=json.loads((old/'manifest.json').read_text())
 for name,h in expected.items():
  if Path(name).is_absolute() or '..' in Path(name).parts or not isinstance(h,str) or len(h)!=64:raise ValueError('Invalid package manifest path or digest')
  if sha(old/name)!=h:raise ValueError('Existing memory integrity mismatch: '+name)
 if old!=new and not profiles_only:
  for name,known in KNOWN_BASELINES.items():
   if sha(old/'bn_memory'/name) not in known:raise ValueError('Unreviewed local parser revision; merge separately rather than overwrite: '+name)
 if old==new and not profiles_only:
  for name in ['parser_host.py','document_worker.py']:
   if sha(new/'bn_memory'/name)!=sha(Path(__file__).parent/name):raise ValueError('Repair version exists with different code')
 changes=[{'path':str(settings),'sha256':sha(settings)}]
 for home in homes(b):
  p=home/'config.yaml'
  if not p.is_file():continue
  if p.is_symlink():raise ValueError('Symlink profile configuration requires separate review')
  changes.append({'path':str(p),'sha256':sha(p)})
  controls=home/'execution-controls.json'
  if controls.is_file() and not controls.is_symlink():changes.append({'path':str(controls),'sha256':sha(controls)})
  elif connect:raise ValueError('Required execution-controls.json missing; finish or restore the owned profile first')
  d=yaml.safe_load(p.read_text());entry=d.get('plugins',{}).get('entries',{}).get('bn-gsd',{})
  if entry:
   q=Path(entry['settings']['settings_file'])
   if not q.is_file():raise ValueError('Missing GSD preparation; finish independent profile preparation first')
   changes.append({'path':str(q),'sha256':sha(q)})
   g=json.loads(q.read_text())
   for name,expected_hash in g.get('config_semantic_sha256',{}).items():
    native=yaml.safe_load(Path(name).read_text());approvals=native.pop('command_allowlist',[])
    if not isinstance(approvals,list) or any(not isinstance(v,str) for v in approvals):raise ValueError('Invalid existing command approvals')
    if hashlib.sha256(canonical(native)).hexdigest()!=expected_hash:raise ValueError('Existing native configuration admission mismatch; reconcile prior change first')
   if g.get('tool_policy'):
    policy=Path(g['tool_policy'])
    if sha(policy)!=g['tool_policy_sha256']:raise ValueError('Existing tool policy integrity mismatch')
    changes.append({'path':str(policy),'sha256':sha(policy)})
 changes=list({row['path']:row for row in changes}.values())
 return {'connect_requested':connect,'profiles_only':profiles_only,'release':VERSION,'bn_root':str(b),'udr_root':str(u),'old_package':str(old),'new_package':str(new),'files':changes,'payload':{n:sha(Path(__file__).parent/n) for n in ['parser_host.py','document_worker.py']},'preserves':['auth','secrets','all SQLite/Dolt data','GSD accounting and required controllers','other user tool rights; exact owned document transports only'],'services_started':False}

def apply(p,connect=False):
 b=Path(p['bn_root']);u=Path(p['udr_root']);old=Path(p['old_package']);new=Path(p['new_package'])
 for row in p['files']:
  if sha(row['path'])!=row['sha256']:raise ValueError('Concurrent configuration change; build a new plan')
 if connect:
  from foundation_setup import describe,verify
  readiness=describe(u)
  if readiness['missing']:raise ValueError('Foundation not ready; run foundation_setup.py first: '+','.join(readiness['missing']))
  if verify(u)['status']!='healthy':raise ValueError('Foundation typed verification failed; connections remain disabled')
 stamp=str(time.time_ns());backup=b/'operator'/('repair-'+VERSION)/stamp;backup.mkdir(mode=0o700,parents=True)
 records=[]
 for i,row in enumerate(p['files']):
  q=Path(row['path']);f=backup/(str(i)+'.before');shutil.copy2(q,f);f.chmod(0o600);records.append({'path':str(q),'backup':str(f),'before_sha256':row['sha256'],'mode':q.stat().st_mode&0o777})
 (backup/'plan.json').write_bytes(canonical(p))
 application={'status':'prepared','records':records,'new_package':str(new),'previous_package':str(old),'connect_requested':connect}
 atom(backup/'application.json',canonical(application))
 def write_owned(path,raw):
  row=next(x for x in records if x['path']==str(path))
  expected=row.get('after_sha256',row['before_sha256'])
  if sha(path)!=expected:raise ValueError('Concurrent change during apply')
  row['pending_sha256']=hashlib.sha256(raw).hexdigest();application['status']='applying';atom(backup/'application.json',canonical(application))
  atom(path,raw,row['mode']);row['after_sha256']=row.pop('pending_sha256');atom(backup/'application.json',canonical(application))
 if not new.exists():
  shutil.copytree(old,new,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
  for name in ['parser_host.py','document_worker.py']:shutil.copy2(Path(__file__).parent/name,new/'bn_memory'/name)
  manifest=json.loads((new/'manifest.json').read_text())
  for name in manifest:manifest[name]=sha(new/name)
  atom(new/'manifest.json',canonical(manifest))
 elif not p.get('profiles_only'):
  for name in ['parser_host.py','document_worker.py']:
   if sha(new/'bn_memory'/name)!=p['payload'][name]:raise ValueError('Existing package differs; no overwrite')
 cfg=json.loads((b/'Memory/settings.json').read_text());cfg['package_root']=str(new)
 write_owned(b/'Memory/settings.json',canonical(cfg))
 gsd_paths=[]
 for h in homes(b):
  path=h/'config.yaml'
  if not path.is_file():continue
  c=yaml.safe_load(path.read_text());c=replace(c,{'__HERMES_UDR_ROOT__':str(u),'__HERMES_BN_ROOT__':str(b),str(old):str(new)})
  if h.name=='bn-gsd-only' and (c.get('mcp_servers',{}).get('udr') or c.get('plugins',{}).get('entries',{}).get('bn-udr-host',{}).get('enabled')):raise ValueError('GSD-only scope contains UDR; inspect independently')
  if connect:
   plugins=c.setdefault('plugins',{});entries=plugins.setdefault('entries',{})
   names=['bn-common-memory']+(['bn-gsd'] if h.name!='bn-udr-only' else [])+(['bn-udr-host'] if h.name!='bn-gsd-only' else [])
   for name in names:
    if name not in entries:raise ValueError('Expected existing local plugin missing: '+name)
    entries[name]['enabled']=True
    plugins['enabled']=list(dict.fromkeys(plugins.get('enabled',[])+[name]))
    plugins['disabled']=[x for x in plugins.get('disabled',[]) if x!=name]
   c['execution_controls_required']=True
   controls=h/'execution-controls.json';policy=json.loads(controls.read_text())
   if policy.get('version')!=1 or not isinstance(policy.get('required'),dict):raise ValueError('Unsupported required-control policy')
   mandatory=['bn-common-memory']+(['bn-udr-host'] if h.name!='bn-gsd-only' else [])+(['bn-gsd'] if entries.get('bn-gsd',{}).get('enabled') else [])
   for kind in ['tool','tool_result','llm','auxiliary']:
    current=policy['required'].get(kind,[])
    if not isinstance(current,list) or any(not isinstance(x,str) for x in current):raise ValueError('Invalid required controller list')
    policy['required'][kind]=list(dict.fromkeys(current+mandatory))
   write_owned(controls,canonical(policy))
   for name in ['context']+(['udr'] if h.name!='bn-gsd-only' else []):
    if name not in c.get('mcp_servers',{}):raise ValueError('Expected existing MCP missing: '+name)
    c['mcp_servers'][name]['enabled']=True
  write_owned(path,yaml.safe_dump(c,allow_unicode=True,sort_keys=False).encode())
  entry=c.get('plugins',{}).get('entries',{}).get('bn-gsd')
  if entry:gsd_paths.append((Path(entry['settings']['settings_file']),c))
 # Exact admissions for changed memory files and known transports. No policy/tool expansion.
 for q,c in gsd_paths:
  s=json.loads(q.read_text());pins=s.setdefault('local_adapter_sha256',{})
  if s.get('tool_policy'):
   policy=json.loads(Path(s['tool_policy']).read_text());entries=policy.get('entries',{})
   needed={'mcp__context__'+name:{'server':'context','mode':'audited_adapter'} for name in ['document_catalogue','document_extract','document_describe','document_read','document_status','document_partition']}
   if 'udr' in c.get('mcp_servers',{}):needed['mcp__udr__udr_research']={'server':'udr','mode':'audited_adapter'}
   missing={k:v for k,v in needed.items() if k not in entries}
   for name,row in needed.items():
    if name in entries and entries[name]!=row:raise ValueError('Custom existing document policy needs explicit review: '+name)
   if missing:
    entries.update(missing);new_policy=backup/('policy-'+hashlib.sha256(str(q).encode()).hexdigest()[:12]+'.json')
    atom(new_policy,canonical(policy));s['tool_policy']=str(new_policy);s['tool_policy_sha256']=sha(new_policy);pins[str(new_policy)]=sha(new_policy)

  for path in [b/'Memory/settings.json',new/'manifest.json']+[new/name for name in json.loads((new/'manifest.json').read_text())]:
   pins[str(path)]=sha(path)
  # Respect the post-r7 semantic admission: permanent command approvals remain mutable.
  for name in list(s.get('config_semantic_sha256',{})):
   path=Path(name)
   if path in [h/'config.yaml' for h in homes(b)]:
    native=yaml.safe_load(path.read_text());approvals=native.pop('command_allowlist',[])
    if not isinstance(approvals,list) or any(not isinstance(v,str) for v in approvals):raise ValueError('Invalid command approvals')
    s['config_semantic_sha256'][name]=hashlib.sha256(canonical(native)).hexdigest()
  for name in ['context','udr']:
   if name in c.get('mcp_servers',{}):s.setdefault('mcp_transport_digests',{})[name]=hashlib.sha256(canonical(c['mcp_servers'][name])).hexdigest()
  # Preserve native config approval semantics introduced after r7, updating only an already pinned config.
  for path in homes(b):
   for name in ['config.yaml','execution-controls.json']:
    f=path/name
    if str(f) in pins:pins[str(f)]=sha(f)
  write_owned(q,canonical(s))
 for row in records:row['after_sha256']=sha(row['path'])
 application.update(status='applied',records=records,verification_required=True,old_package_retained=True)
 atom(backup/'application.json',canonical(application));return {'status':'applied','application':str(backup/'application.json'),'restart_owned_gateway_required':True,'verification_required':True}

def rollback(path):
 app=json.loads(path.read_text())
 for row in app['records']:
  if sha(row['path']) not in {row['before_sha256'],row.get('after_sha256'),row.get('pending_sha256')}:raise ValueError('Later change detected; no rollback overwrite')
  if sha(row['backup'])!=row['before_sha256']:raise ValueError('Backup integrity failed')
 for row in app['records']:atom(Path(row['path']),Path(row['backup']).read_bytes(),row['mode'])
 return {'status':'rolled_back','data_deleted':False,'new_package_retained':True,'restart_owned_gateway_required':True}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bn-root',type=Path);p.add_argument('--udr-root',type=Path);p.add_argument('--apply',action='store_true');p.add_argument('--connect',action='store_true');p.add_argument('--profiles-only',action='store_true');p.add_argument('--expected-plan-sha256');p.add_argument('--rollback',type=Path)
 a=p.parse_args()
 if a.rollback:print(json.dumps(rollback(a.rollback.resolve()),ensure_ascii=False));return
 if not a.bn_root or not a.udr_root:p.error('Provide both roots')
 v=plan(a.bn_root.resolve(strict=True),a.udr_root.resolve(strict=True),a.profiles_only,a.connect);h=hashlib.sha256(canonical(v)).hexdigest()
 if a.apply:
  if a.expected_plan_sha256!=h:raise ValueError('Explicit current plan hash required')
  r=apply(v,a.connect)
 else:r={'plan_sha256':h,**v}
 print(json.dumps(r,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
