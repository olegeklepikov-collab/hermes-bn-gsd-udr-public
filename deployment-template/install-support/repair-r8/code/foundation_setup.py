"""Owner-operated Foundation preparation; signed SDK and existing databases stay intact."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,shutil,time,socket

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(argv,env,cwd=None):
 r=subprocess.run(list(map(str,argv)),env=env,cwd=cwd,capture_output=True,text=True,timeout=180)
 if r.returncode:raise RuntimeError('local_command_failed:'+str(argv[0])+':'+r.stderr[-400:])
 return r.stdout

def describe(u):
 root=u/'profile/foundation';plugin=u/'profile/plugins/hermes-foundation-bridge'
 config=root/'native-runtime.json';lock=u/'state/adapters/beads-runtime.json'
 result={'root':str(root),'native_runtime_exists':config.is_file(),'beads_lock_exists':lock.is_file(),'services':{},'missing':[]}
 if not plugin.is_dir():result['missing'].append('signed_foundation_plugin')
 if not config.is_file():result['missing'].append('native-runtime.json: supply --node, --graph-python, --neo4j-password-file')
 if not lock.is_file():result['missing'].append('beads-runtime.json: run independent UDR preparation first')
 else:
  l=json.loads(lock.read_text());p=Path(l['executable'])
  if not p.is_file() or p.is_symlink() or sha(p)!=l['sha256']:result['missing'].append('owned_beads_binary_integrity')
 if config.is_file():
  c=json.loads(config.read_text())
  for key in ['node_path','python_path','neo4j_password_file']:
   if not Path(c[key]).is_file():result['missing'].append(key)
  from urllib.parse import urlsplit
  for key in ['agentmemory_url','neo4j_uri']:
   a=urlsplit(c[key]);ready=False
   if a.hostname not in {'127.0.0.1','::1'}:result['missing'].append('non_loopback_'+key);continue
   try:
    with socket.create_connection((a.hostname,a.port),timeout=2):ready=True
   except OSError:pass
   owned=False
   if ready:
    try:
     import psutil
     ids=subprocess.run(['/usr/sbin/lsof','-nP','-t','-iTCP:'+str(a.port),'-sTCP:LISTEN'],capture_output=True,text=True,timeout=5)
     pids={int(v) for v in ids.stdout.split() if v.isdigit()}
     owned=bool(pids) and all(any(str(u)+'/' in arg for arg in psutil.Process(pid).cmdline()) for pid in pids)
    except Exception:owned=False
   result['services'][key]={'host':a.hostname,'port':a.port,'listening':ready,'owned_process_verified':owned}
   if not ready:result['missing'].append('start_owned_'+key)
   elif not owned:result['missing'].append('verify_service_ownership_'+key)
 # A missing native file is not evidence of a broken service. Never overwrite a valid binding.
 return result

def verify_pair(u):
 import zipfile
 expected={'foundation':('hermes-foundation-bridge','0.14.0b1','f847454509d608e4f5ff2013e66da1469b804f9bef6053fbb18785ea1f402337'),'research':('hermes-research-report','0.44.0b2','61e15b459878d5f6ffe77849c5fe98d233aeb2fb91655be161c2cbaf2fa5fefa')}
 mini=shutil.which('minisign')
 if not mini:raise ValueError('Trusted minisign is required; install the pinned dependency first')
 results={}
 for kind,(name,version,want) in expected.items():
  folder=u/'software'/(kind+'-release');archive=folder/(name+'-'+version+'.zip');signature=Path(str(archive)+'.minisig');key=folder/'release-signing.pub'
  if not archive.is_file() or archive.is_symlink() or sha(archive)!=want:raise ValueError('Signed archive SHA mismatch: '+kind)
  if not key.is_file() or sha(key)!='2295aaab3cb418c4f81a867a701a8187e8cdd0f73105a1f318c1faf981dfdb1a':raise ValueError('Trusted public key mismatch')
  r=subprocess.run([mini,'-V','-q','-m',str(archive),'-x',str(signature),'-p',str(key)],capture_output=True,timeout=30)
  if r.returncode:raise ValueError('Signed release verification failed: '+kind)
  installed=u/'profile/plugins'/('hermes-foundation-bridge' if kind=='foundation' else 'ultra-deep-research')
  with zipfile.ZipFile(archive) as z:
   m=json.loads(z.read('bundle-manifest.json'))
   for row in m['files']:
    name=row['path'];q=installed/name
    if Path(name).is_absolute() or '..' in Path(name).parts or q.is_symlink() or not q.is_file() or sha(q)!=row['sha256']:raise ValueError('Installed signed SDK differs: '+kind+':'+name)
  results[kind]={'version':version,'archive_sha256':want,'signature_verified':True,'installed_source_matches':True,'source_commit':m.get('source_commit'),'archive':str(archive)}
 return results

def verify(u,foundation_root=None):
 root=Path(foundation_root) if foundation_root else u/'profile/foundation';sdk=u/'profile/plugins/hermes-foundation-bridge';bridge=u/'operator/bn-bridge';py=u/'software/hermes/.venv/bin/python'
 env=dict(os.environ,HERMES_HOME=str(u/'profile'),HERMES_FOUNDATION_ROOT=str(root),PYTHONPATH=str(sdk/'src')+os.pathsep+str(bridge),PATH=str(u/'software/bin')+os.pathsep+os.environ.get('PATH',''),DO_NOT_TRACK='1')
 env['DOLT_ROOT_PATH']=str(u/'state/beads-local');env['HERMES_REPAIR_BD_LOCK']=str(u/'state/adapters/beads-runtime.json')
 code="""from pathlib import Path
import os,json
from hermes_foundation_bridge.native_runtime import load_native_runtime
from hermes_foundation_bridge.bridge import services
from hermes_foundation_bridge.release import release_verified
from hermes_foundation_bridge.agentmemory_adapter import AgentMemoryAdapter
from hermes_foundation_bridge.graphiti_adapter import GraphitiAdapter
from local_beads import LocalBeadsAdapter
root=Path(os.environ['HERMES_FOUNDATION_ROOT']);load_native_runtime(root)
r,a,s=services(root)
release_ok,_=release_verified(root)
results={'runtime':r.health(),'beads':LocalBeadsAdapter(root,lock_path=Path(os.environ['HERMES_REPAIR_BD_LOCK'])).health({'schema_version':1}),'agentmemory':AgentMemoryAdapter(root).health({'schema_version':1}),'graphiti':GraphitiAdapter(root).health({'schema_version':1}),'release':{'status':'healthy' if release_ok else 'unverified'}}
if hasattr(s,'health'):results['dolt']=s.health()
else:
 for name in ['kw_core','kw_context','kw_quant','kw_registry']:s._run(s.root/name,'sql','-q','SELECT 1 AS ok')
 results['dolt']={'status':'healthy','mode':'owned_cli','actual_read_checked':True,'database_count':4}
print(json.dumps({'status':'healthy' if all(x.get('status') in ['healthy','ready'] for x in results.values()) else 'blocked','components':results},ensure_ascii=False))
"""
 value=json.loads(run([py,'-c',code],env));value['scope']='native research path; not every Foundation feature';value['signed_pair']=verify_pair(u);engine=run([u/'software/bin/iii','--version'],env).strip();value['actual_iii_version']=engine
 if '0.11.2' not in engine:raise ValueError('Actual iii version mismatch')
 return value

def infer(u):
 result={}
 candidates=[u.parent/'Hermes BN/runtime/node/bin/node',Path(shutil.which('node') or '/nonexistent')]
 result['node']=next((str(p) for p in candidates if p.is_file()),None)
 graph=u/'software/foundation-graph/bin/python';result['graph_python']=str(graph) if graph.is_file() else None
 result['password_file']=str(u/'state/authority/neo4j.password')
 am=u/'state/services/agentmemory.json'
 port=json.loads(am.read_text()).get('env',{}).get('III_REST_PORT') if am.is_file() else None
 result['agentmemory_url']='http://127.0.0.1:'+str(port) if port else None
 service=u/'state/services/neo4j.json';result['neo4j_uri']=None
 if service.is_file():
  cfg=json.loads(service.read_text());conf=Path(cfg.get('env',{}).get('NEO4J_CONF',str(u/'software/neo4j-community-5.26.31/conf')))/'neo4j.conf'
  if conf.is_file():
   import re
   m=re.search(r'^server[.]bolt[.]listen_address\s*=\s*(?:127[.]0[.]0[.]1)?:([0-9]+)\s*$',conf.read_text(),re.M)
   if m:result['neo4j_uri']='bolt://127.0.0.1:'+m[1]
 return result

def apply(u,node=None,graph=None,password=None,am=None,neo=None,foundation_root=None):
 root=Path(foundation_root) if foundation_root else u/'profile/foundation';sdk=u/'profile/plugins/hermes-foundation-bridge';py=u/'software/hermes/.venv/bin/python';bridge=u/'operator/bn-bridge';key=u/'state/adapters/beads-runtime.json'
 if not root.resolve().is_relative_to(u.resolve()):raise ValueError('Foundation root must belong to the owned UDR')
 pair=verify_pair(u)
 env=dict(os.environ,HERMES_HOME=str(u/'profile'),HERMES_FOUNDATION_ROOT=str(root),PYTHONPATH=str(sdk/'src')+os.pathsep+str(bridge),PATH=str(u/'software/bin')+os.pathsep+os.environ.get('PATH',''),DO_NOT_TRACK='1')
 env['DOLT_ROOT_PATH']=str(u/'state/beads-local');env['HERMES_REPAIR_BD_LOCK']=str(key)
 if not (root/'native-runtime.json').exists():
  detected=infer(u);node=node or detected['node'];graph=graph or detected['graph_python'];password=password or detected['password_file'];am=am or detected['agentmemory_url'];neo=neo or detected['neo4j_uri']
  if not am or not neo:raise ValueError('Owned service endpoints are not configured; finish AgentMemory and Neo4j first')
  if not all([node,graph,password]):raise ValueError('native_runtime_missing: exact native paths and private Neo4j password file required; configure own services first')
  args=[py,sdk/'scripts/configure_native_runtime.py','--foundation-root',root,'--node',node,'--graph-python',graph,'--neo4j-password-file',password,'--agentmemory-url',am,'--neo4j-uri',neo]
  # configure_native_runtime uses getpass if needed; keep the terminal, do not capture a secret.
  subprocess.run(list(map(str,args)),env=env,check=True)
 check=describe(u)
 if not check['missing']:
  try:
   known=verify(u,root)
   if known['status']=='healthy':return {'status':'already_ready','verification':known,'existing_state_preserved':True}
  except Exception:pass
 if check['missing']:raise ValueError('foundation_dependencies_not_ready:'+','.join(check['missing']))
 # Initialize only the selected owned workspace, never an ancestor-detected Beads database.
 lock=json.loads(key.read_text());ws=root/'beads-workspace'
 if not (ws/'.beads').is_dir():
  ws.mkdir(mode=0o700,parents=True,exist_ok=True)
  if any(ws.iterdir()):raise ValueError('beads_target_not_empty; inspect before init')
  e=dict(env,BEADS_DIR=str(ws/'.beads'),DOLT_ROOT_PATH=lock['dolt_root'],BD_NON_INTERACTIVE='1',BD_DISABLE_METRICS='1',BD_DISABLE_EVENT_FLUSH='1')
  run([lock['executable'],'init','--prefix','KWF','--stealth','--non-interactive','--skip-agents','--skip-hooks'],e,ws)
 # Record a fresh SDK verification receipt from the immutable signed artifacts, never an owner's old receipt.
 release=root/'releases/hermes-foundation-bridge-0.14.0b1';release.mkdir(parents=True,mode=0o700,exist_ok=True)
 for name in ['hermes-foundation-bridge-0.14.0b1.zip','hermes-foundation-bridge-0.14.0b1.zip.minisig','release-signing.pub']:
  src=u/'software/foundation-release'/name;dst=release/name
  if dst.exists() and (dst.is_symlink() or sha(dst)!=sha(src)):raise ValueError('Existing release artifact differs; no overwrite')
  if not dst.exists():shutil.copy2(src,dst)
 env['HERMES_REPAIR_RELEASE_COMMIT']=pair['foundation']['source_commit']
 # SDK migrations are versioned and idempotent; apply only missing canonical manifests.
 code='''from pathlib import Path
import json,os
from hermes_foundation_bridge.bridge import migrate,services
from hermes_foundation_bridge.release import verify_release
from hermes_foundation_bridge.native_runtime import load_native_runtime
from hermes_foundation_bridge.agentmemory_adapter import AgentMemoryAdapter
from hermes_foundation_bridge.graphiti_adapter import GraphitiAdapter
from local_beads import LocalBeadsAdapter
root=Path(os.environ['HERMES_FOUNDATION_ROOT']);load_native_runtime(root)
release=verify_release({'schema_version':1,'expected_version':'0.14.0b1','expected_commit':os.environ['HERMES_REPAIR_RELEASE_COMMIT']},root)
r=migrate({'schema_version':1,'apply':True})
beads=LocalBeadsAdapter(root,lock_path=Path(os.environ['HERMES_REPAIR_BD_LOCK']));memory=AgentMemoryAdapter(root);graph=GraphitiAdapter(root)
for adapter in [beads,memory,graph]:
 if not adapter.manifest_path.exists():adapter.migrate({'schema_version':1,'apply':True})
checks={'beads':beads.health({'schema_version':1}),'agentmemory':memory.health({'schema_version':1}),'graphiti':graph.health({'schema_version':1})}
print(json.dumps({'migration':r,'release_verification':release,'adapters':checks},ensure_ascii=False))
'''
 result=json.loads(run([py,'-c',code],env));result['dependencies']=check;result['signed_pair']=pair;return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--udr-root',type=Path,required=True);p.add_argument('--apply',action='store_true');p.add_argument('--verify',action='store_true');p.add_argument('--node');p.add_argument('--graph-python');p.add_argument('--neo4j-password-file');p.add_argument('--agentmemory-url');p.add_argument('--neo4j-uri');p.add_argument('--output',type=Path)
 a=p.parse_args();u=a.udr_root.resolve(strict=True)
 result=apply(u,a.node,a.graph_python,a.neo4j_password_file,a.agentmemory_url,a.neo4j_uri) if a.apply else verify(u) if a.verify else describe(u)
 if a.output:
  if a.output.exists():raise FileExistsError('Use a new result filename')
  a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2));a.output.chmod(0o600)
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
