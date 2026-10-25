from pathlib import Path
import argparse,os,json,subprocess,shutil,sys
B=Path(__file__).resolve().parents[1];U=B/'runtime/Hermes UDR';BN=B/'runtime/Hermes BN'
p=argparse.ArgumentParser();p.add_argument('--r-runtime',required=True);p.add_argument('--timezone',default='UTC');p.add_argument('--contact-email',default='');p.add_argument('--host-bootstrap',default=str(Path.home()/'Library/Application Support/HermesUDR-New'));a=p.parse_args()
flag=B/'deployment/UDR-prepared.json'
if flag.exists():raise SystemExit('Already prepared; use another clean extraction for another location')
r=Path(a.r_runtime).expanduser().absolute()
if r.exists():raise SystemExit('New UDR R directory must not exist')
records=json.loads((B/'deployment/udr-r-prefix-records.json').read_text())
if records and len(str(r).encode())>len(records[0]['placeholder'].encode()):raise SystemExit('Choose a shorter UDR R path for these binary packages')
shutil.move(str(B/'runtime/hermes-udr-r'),r)
sys.path.insert(0,str(B/'deployment'));from conda_pack.prefixes import update_prefix
for rec in json.loads((B/'deployment/udr-r-prefix-records.json').read_text()):
 q=r/rec['path']
 if q.is_file() and not q.is_symlink():update_prefix(str(q),str(r),rec['placeholder'],rec['mode'])
host=Path(a.host_bootstrap).expanduser().absolute()
if host.exists():raise SystemExit('Host bootstrap directory must be new; no overwrite of another instance')
host.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(B/'host-template/HermesUDR',host,symlinks=True)
sub={'__HERMES_BN_ROOT__':str(BN),'__HERMES_UDR_ROOT__':str(U),'__HERMES_UDR_R_RUNTIME__':str(r),'__USER_HOME__':str(Path.home()),'__CONTACT_EMAIL__':a.contact_email,'__TIMEZONE__':a.timezone,'__UDR_HOST_BOOTSTRAP__':str(Path(a.host_bootstrap).expanduser().absolute())}
for root in [U,r,host,BN/'data/plugins/bn-udr-host',BN/'data/profiles',BN/'bin/hermes-bn-module-mode.py']:
 paths=[root] if root.is_file() else root.rglob('*')
 for q in paths:
  if q.is_symlink():
   old=os.readlink(q);new=old
   for k,v in sub.items():new=new.replace(k,v)
   if new!=old:q.unlink();q.symlink_to(new)
   continue
  if not q.is_file():continue
  with q.open('rb') as f:head=f.read(8192)
  if b'\0' in head:continue
  try:old=q.read_text()
  except (OSError,UnicodeError):continue
  new=old
  for k,v in sub.items():new=new.replace(k,v)
  if new!=old:
   mode=q.stat().st_mode & 0o777;q.chmod(mode|0o200);q.write_text(new);q.chmod(mode)
# Fresh authority never copies prior acceptance, leases, passwords, keys or model identity.
authority=U/'state/authority';authority.mkdir(parents=True,exist_ok=True,mode=0o700)
key=authority/'bn-bridge.key'
if key.exists():raise SystemExit('Refuse authority overwrite')
key.write_bytes(os.urandom(32));key.chmod(0o600)
bridge=U/'operator/bn-bridge';profile=bridge/'profile';profile.mkdir(mode=0o700)
import hashlib
(profile/'config.yaml').write_text(json.dumps({'research':{'integration_mode':'foundation','workspace_root':str(U/'workspace/bn-research-runs')}},indent=2))
manifest={name:hashlib.sha256((bridge/name).read_bytes()).hexdigest() for name in json.loads((bridge/'source-manifest.json').read_text())};(bridge/'source-manifest.json').write_text(json.dumps(manifest,indent=2))
(U/'operator/qualification').mkdir(parents=True,exist_ok=True)
roles={name:{'workspace':str(U/'workspace'/folder),'read_only':name in ['review','operator']} for name,folder in [('default','default'),('engineering','engineering-worktree'),('quantitative','quantitative'),('review','review'),('operator','operator')]}
(U/'operator/qualification/role-policy.json').write_text(json.dumps({'schema_version':1,'roles':roles},indent=2));(U/'operator/qualification/role-policy.json').chmod(0o600)
# Only local empty coordinator/artifact migrations. All account and service enabling stays explicit.
env={k:v for k,v in os.environ.items() if not k.endswith(('_API_KEY','_ACCESS_TOKEN','_REFRESH_TOKEN'))}
env.update(HERMES_HOME=str(U/'profile'),HERMES_FOUNDATION_ROOT=str(U/'profile/foundation'),PYTHONDONTWRITEBYTECODE='1')
code="from pathlib import Path; from hermes_foundation_bridge.bridge import services; r,a,s=services(Path(__import__('os').environ['HERMES_FOUNDATION_ROOT'])); r.migration_receipt(apply=True); a.prepare(dry_run=False); print('Fresh empty coordinator and artifact directories prepared')"
env['PYTHONPATH']=str(U/'profile/plugins/hermes-foundation-bridge/src')
subprocess.run([str(U/'software/hermes/.venv/bin/python'),'-c',code],env=env,check=True)
flag.write_text(json.dumps({'prepared':True,'old_accounts_present':False,'old_state_present':False,'fresh_bridge_key':True,'services_started':False,'production_accepted':False,'root':str(U),'r_runtime':str(r),'next_steps':'Configure fresh native services, SQL privileges, embeddings/model access, then explicitly enable and validate the BN host bridge'},indent=2))
print('Independent UDR prepared. No model login, remote call, auto-start or inherited acceptance.')

# Local compatibility override, separate from the unchanged signed SDK baseline.
_bd=U/'software/bin/bd'
_lock=U/'state/adapters/beads-runtime.json';_lock.parent.mkdir(parents=True,exist_ok=True)
_lock.write_text(json.dumps({'schema_version':1,'executable':str(_bd),'sha256':__import__('hashlib').sha256(_bd.read_bytes()).hexdigest(),'version':'1.3.1','dolt_root':str(U/'state/beads-local'),'supplier_baseline':'1.1.0','signed_SDK_modified':False},indent=2));_lock.chmod(0o600)

