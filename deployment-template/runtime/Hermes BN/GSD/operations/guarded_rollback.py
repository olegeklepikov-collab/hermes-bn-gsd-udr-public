"""Independent operator rollback: pinned backup bytes are checked before any protected copy."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

def sha(raw):return hashlib.sha256(raw).hexdigest()

def seal(snapshot,home,runner):
 snapshot=Path(snapshot).resolve();home=Path(home).resolve();runner=Path(runner).resolve();files={}
 for p in sorted(snapshot.rglob('*')):
  if p.is_symlink():raise ValueError('Symlink in recovery snapshot')
  if p.is_file() and p.name!='backup-manifest.json':files[str(p.relative_to(snapshot))]=sha(p.read_bytes())
 if 'installation.json' not in files:raise ValueError('No installation receipt')
 body={'version':1,'home':str(home),'runner':str(runner),'runner_sha256':sha(runner.read_bytes()),'files':files}
 raw=json.dumps(body,sort_keys=True,separators=(',',':')).encode();(snapshot/'backup-manifest.json').write_bytes(raw);return sha(raw)

def verified_bytes(snapshot,home,pin):
 snapshot=Path(snapshot).resolve();raw=(snapshot/'backup-manifest.json').read_bytes()
 if len(pin)!=64 or sha(raw)!=pin:raise ValueError('Independent backup manifest pin mismatch')
 m=json.loads(raw)
 if m['version']!=1 or Path(m['home']).resolve()!=Path(home).resolve():raise ValueError('Recovery scope mismatch')
 runner=Path(m['runner'])
 if runner.is_symlink() or sha(runner.read_bytes())!=m['runner_sha256']:raise ValueError('Recovery executor integrity mismatch')
 out={}
 for name,expected in m['files'].items():
  rel=Path(name)
  if rel.is_absolute() or '..' in rel.parts:raise ValueError('Recovery path outside snapshot')
  p=snapshot/rel
  if p.is_symlink() or not p.resolve().is_relative_to(snapshot):raise ValueError('Recovery path alias')
  data=p.read_bytes()
  if sha(data)!=expected:raise ValueError('Recovery backup file mismatch: '+name)
  out[name]=data
 return m,out

def stage_verified(buffers,destination):
 for name,data in buffers.items():
  p=Path(destination)/name;p.parent.mkdir(parents=True,exist_ok=True,mode=0o700);p.write_bytes(data);p.chmod(0o600)

def restore(snapshot,home,pin,apply=False):
 m,buffers=verified_bytes(snapshot,home,pin)
 with tempfile.TemporaryDirectory(prefix='gsd-verified-recovery-') as stage:
  stage_verified(buffers,stage)
  args=[sys.executable,m['runner'],'--home',str(Path(home).resolve()),'--snapshot',stage]
  if apply:args.append('--apply')
  result=subprocess.run(args,capture_output=True,text=True,timeout=30)
  if result.returncode:raise RuntimeError('Verified rollback refused: '+result.stderr.strip())
  return {'verified_backup_before_action':True,'staged_from_verified_bytes':True,'apply':apply,'rollback':json.loads(result.stdout),'manifest_sha256':pin}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--snapshot',required=True);p.add_argument('--home',required=True);p.add_argument('--manifest-sha256');p.add_argument('--seal-with-runner');p.add_argument('--apply',action='store_true');a=p.parse_args()
 if a.seal_with_runner:print(json.dumps({'manifest_sha256':seal(a.snapshot,a.home,a.seal_with_runner)}))
 else:
  if not a.manifest_sha256:p.error('An independently recorded manifest SHA-256 is required')
  print(json.dumps(restore(a.snapshot,a.home,a.manifest_sha256,a.apply)))
