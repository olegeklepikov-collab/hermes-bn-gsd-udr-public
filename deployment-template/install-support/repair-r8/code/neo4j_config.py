"""Plan an explicit ASCII Neo4j config route; never changes data location or starts services."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,time

def digest(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def plan(u):
 service=u/'state/services/neo4j.json'
 if service.is_symlink() or not service.is_file():raise ValueError('Owned Neo4j service definition required')
 cfg=json.loads(service.read_text());home=u/'software/neo4j-community-5.26.31';source=Path(cfg.get('env',{}).get('NEO4J_CONF',str(home/'conf')))
 if not source.is_dir() or source.is_symlink():raise ValueError('Regular Neo4j configuration directory required')
 conf=source/'neo4j.conf'
 if not conf.is_file() or conf.is_symlink():raise ValueError('neo4j.conf missing')
 text=conf.read_text()
 if '__HERMES_' in text or '/ABSOLUTE' in text:raise ValueError('Finish owned Neo4j configuration before starting services')
 files=[]
 for p in source.iterdir():
  if p.is_symlink():raise ValueError('Configuration symlink requires separate review')
  if p.is_file():files.append({'name':p.name,'sha256':digest(p.read_bytes())})
 target=source if str(source).isascii() else Path('/Users/Shared')/('HermesBN-'+str(os.getuid())+'-'+digest(str(u).encode())[:16])/'neo4j-conf'
 if not str(target).isascii():raise ValueError('ASCII config path is required')
 return {'udr_root':str(u),'service':str(service),'before_sha256':digest(service.read_bytes()),'source':str(source),'target':str(target),'files':files,'needs_change':cfg.get('env',{}).get('NEO4J_CONF')!=str(target),'data_paths_unchanged':True,'services_started':False}
def apply(p):
 u=Path(p['udr_root']);ps=subprocess.run(['ps','-axo','args='],capture_output=True,text=True,check=True).stdout.splitlines()
 # Match Java itself, not a shell containing the command text.
 if any(line.lstrip().startswith(str(u/'software/java21.jdk')) and 'org.neo4j.' in line for line in ps):raise ValueError('Stop only this owned Neo4j service before changing its route')
 service=Path(p['service']);source=Path(p['source']);target=Path(p['target'])
 if digest(service.read_bytes())!=p['before_sha256']:raise ValueError('Service changed since plan')
 for f in p['files']:
  if digest((source/f['name']).read_bytes())!=f['sha256']:raise ValueError('Neo4j config changed since plan')
 if target!=source:
  parent=target.parent
  if parent.exists() and (parent.is_symlink() or parent.stat().st_uid!=os.getuid()):raise ValueError('Unsafe ASCII service directory')
  parent.mkdir(mode=0o700,exist_ok=True);parent.chmod(0o700)
  if target.exists() and (target.is_symlink() or target.stat().st_uid!=os.getuid()):raise ValueError('Unsafe target config directory')
  target.mkdir(mode=0o700,exist_ok=True)
  for f in p['files']:
   dst=target/f['name']
   if dst.exists() and (dst.is_symlink() or digest(dst.read_bytes())!=f['sha256']):raise ValueError('Existing target config differs; no overwrite')
   if not dst.exists():shutil.copyfile(source/f['name'],dst);dst.chmod(0o600)
 backup=u/'state/services/repair-r8';backup.mkdir(mode=0o700,exist_ok=True)
 saved=backup/('neo4j-'+str(time.time_ns())+'.json');shutil.copyfile(service,saved);saved.chmod(0o600)
 cfg=json.loads(service.read_text());cfg.setdefault('env',{})['NEO4J_CONF']=str(target)
 cfg['env'].setdefault('LANG','en_US.UTF-8');cfg['env'].setdefault('LC_ALL','en_US.UTF-8')
 raw=json.dumps(cfg,ensure_ascii=False,indent=2).encode();tmp=service.with_suffix('.repair-r8.tmp')
 with tmp.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
 tmp.chmod(0o600);os.replace(tmp,service)
 return {'status':'configured','backup':str(saved),'service':str(service),'after_sha256':digest(raw),'NEO4J_CONF':str(target),'data_paths_changed':False,'services_started':False,'next':'Render the exact owned service definition and verify Neo4j effective home/config before starting.'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--udr-root',type=Path,required=True);p.add_argument('--apply',action='store_true');p.add_argument('--expected-plan-sha256');a=p.parse_args();v=plan(a.udr_root.resolve(strict=True));h=digest(canonical(v))
 if a.apply:
  if a.expected_plan_sha256!=h:raise ValueError('Explicit current plan hash required')
  result=apply(v)
 else:result={'plan_sha256':h,**v}
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
