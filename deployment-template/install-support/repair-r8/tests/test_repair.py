import os
import importlib.util,json,hashlib,shutil,sys
from pathlib import Path
import pytest,yaml
CODE=Path(__file__).resolve().parents[1]/'code';sys.path.insert(0,str(CODE))
import repair

def fixture(root):
 b=root/'Проверка BN';u=root/'Проверка UDR';p=b/'Memory/releases/1.4.0';(p/'bn_memory').mkdir(parents=True)
 for n in ['parser_host.py','document_worker.py']:(p/'bn_memory'/n).write_text('# prior owned source\n')
 repair.KNOWN_BASELINES={n:{repair.sha(p/'bn_memory'/n)} for n in ['parser_host.py','document_worker.py']}
 (p/'parser-runtime.json').write_text('{}');(p/'manifest.json').write_text(json.dumps({'bn_memory/'+n:repair.sha(p/'bn_memory'/n) for n in ['parser_host.py','document_worker.py']}))
 (b/'Memory/settings.json').write_text(json.dumps({'package_root':str(p),'state_root':str(b/'Memory/state')}))
 u.mkdir();(b/'Memory/state').mkdir();(b/'Memory/state/retained.txt').write_text('owner state must remain')
 for h in repair.homes(b):
  h.mkdir(parents=True);settings=h/'gsd-settings.json';settings.write_text(json.dumps({'limits':{'budget_mode':'observe','spent':17},'local_adapter_sha256':{},'mcp_transport_digests':{}}))
  plugins={'bn-common-memory':{'enabled':False,'settings':{'config_file':str(b/'Memory/settings.json')}}}
  mcp={'context':{'command':'python','args':[str(p/'bn_memory/server.py')],'enabled':False}}
  if h.name!='bn-gsd-only':
   plugins['bn-udr-host']={'enabled':False,'settings':{'udr_root':'__HERMES_UDR_ROOT__'}};mcp['udr']={'command':'__HERMES_UDR_ROOT__/operator/bn-bridge/serve','enabled':False}
  if h.name!='bn-udr-only':plugins['bn-gsd']={'enabled':True,'settings':{'settings_file':str(settings)}}
  c={'plugins':{'entries':plugins,'enabled':['bn-gsd'],'disabled':['bn-common-memory','bn-udr-host']},'mcp_servers':mcp,'execution_controls_required':True}
  (h/'execution-controls.json').write_text(json.dumps({'version':1,'required':{k:['bn-common-memory'] for k in ['tool','tool_result','llm','auxiliary']},'timeout_seconds':60}));(h/'config.yaml').write_text(yaml.safe_dump(c));(h/'auth.json').write_text('{"sentinel":"owner auth unchanged"}')
 for h in repair.homes(b):
  q=h/'gsd-settings.json';v=json.loads(q.read_text());v['config_semantic_sha256']={str(z/'config.yaml'):hashlib.sha256(repair.canonical(yaml.safe_load((z/'config.yaml').read_text()))).hexdigest() for z in repair.homes(b)};q.write_text(json.dumps(v))
 return b,u

def test_real_profile_repair_and_guarded_rollback(tmp_path):
 b,u=fixture(tmp_path);before={p:p.read_bytes() for p in b.rglob('*') if p.is_file()}
 plan=repair.plan(b,u);result=repair.apply(plan);assert result['status']=='applied'
 for h in repair.homes(b):
  c=yaml.safe_load((h/'config.yaml').read_text());assert '__HERMES_UDR_ROOT__' not in (h/'config.yaml').read_text();assert c['execution_controls_required']
  if h.name=='bn-gsd-only':assert 'udr' not in c['mcp_servers']
  if h.name!='bn-udr-only':assert json.loads((h/'gsd-settings.json').read_text())['limits']['spent']==17
  assert (h/'auth.json').read_bytes()==before[h/'auth.json']
 assert (b/'Memory/state/retained.txt').read_text()=='owner state must remain'
 repair.rollback(Path(result['application']))
 for p,v in before.items():assert p.read_bytes()==v
 assert (b/'Memory/releases/1.4.2').is_dir()

def test_concurrent_change_refused_before_apply(tmp_path):
 b,u=fixture(tmp_path);plan=repair.plan(b,u);(b/'data/config.yaml').write_text('changed: true')
 with pytest.raises(ValueError,match='Concurrent'):repair.apply(plan)
 assert json.loads((b/'Memory/settings.json').read_text())['package_root'].endswith('1.4.0')

def test_tampered_source_refused(tmp_path):
 b,u=fixture(tmp_path);(b/'Memory/releases/1.4.0/bn_memory/parser_host.py').write_text('unexpected')
 with pytest.raises(ValueError,match='integrity'):repair.plan(b,u)

def test_later_change_blocks_rollback(tmp_path):
 b,u=fixture(tmp_path);result=repair.apply(repair.plan(b,u));(b/'data/config.yaml').write_text('user later edit')
 with pytest.raises(ValueError,match='Later change'):repair.rollback(Path(result['application']))
 assert (b/'data/config.yaml').read_text()=='user later edit'

def test_repeat_preserves_authority_and_state(tmp_path):
 b,u=fixture(tmp_path);repair.apply(repair.plan(b,u));result=repair.apply(repair.plan(b,u));assert result['status']=='applied'
 assert json.loads((b/'data/gsd-settings.json').read_text())['limits']['spent']==17
 assert (b/'Memory/state/retained.txt').read_text()=='owner state must remain'

def test_connect_only_after_dependencies(tmp_path,monkeypatch):
 import foundation_setup
 b,u=fixture(tmp_path);monkeypatch.setattr(foundation_setup,'describe',lambda root:{'missing':['native-runtime']})
 with pytest.raises(ValueError,match='not ready'):repair.apply(repair.plan(b,u),connect=True)
 assert json.loads((b/'Memory/settings.json').read_text())['package_root'].endswith('1.4.0')

def test_known_profile_connections_after_readiness(tmp_path,monkeypatch):
 import foundation_setup
 b,u=fixture(tmp_path);monkeypatch.setattr(foundation_setup,'describe',lambda root:{'missing':[]});monkeypatch.setattr(foundation_setup,'verify',lambda root:{'status':'healthy'})
 for h in repair.homes(b):
  path=h/'config.yaml';c=yaml.safe_load(path.read_text());c['execution_controls_required']=False
  if 'bn-gsd' in c['plugins']['entries']:c['plugins']['entries']['bn-gsd']['enabled']=False;c['plugins']['disabled'].append('bn-gsd')
  path.write_text(yaml.safe_dump(c))
 for h in repair.homes(b):
  q=h/'gsd-settings.json';s=json.loads(q.read_text());s['config_semantic_sha256']={str(z/'config.yaml'):hashlib.sha256(repair.canonical(yaml.safe_load((z/'config.yaml').read_text()))).hexdigest() for z in repair.homes(b)};q.write_text(json.dumps(s))
 repair.apply(repair.plan(b,u,connect=True),connect=True)
 for h in repair.homes(b):
  c=yaml.safe_load((h/'config.yaml').read_text());assert c['mcp_servers']['context']['enabled']
  assert c['plugins']['entries']['bn-common-memory']['enabled'];assert c['execution_controls_required']
  mandatory=json.loads((h/'execution-controls.json').read_text())['required']['llm'];assert 'bn-common-memory' in mandatory
  if h.name!='bn-gsd-only':assert 'bn-udr-host' in mandatory
  if h.name!='bn-gsd-only':assert c['mcp_servers']['udr']['enabled']
  if h.name!='bn-udr-only':assert c['plugins']['entries']['bn-gsd']['enabled'] and 'bn-gsd' not in c['plugins']['disabled']


def test_semantic_config_admission_preserved(tmp_path):
 b,u=fixture(tmp_path);repair.apply(repair.plan(b,u))
 s=json.loads((b/'data/gsd-settings.json').read_text())
 for name,digest in s['config_semantic_sha256'].items():
  v=yaml.safe_load(Path(name).read_text());v.pop('command_allowlist',[])
  assert hashlib.sha256(repair.canonical(v)).hexdigest()==digest


def test_locally_changed_but_self_manifested_parser_not_overwritten(tmp_path):
 b,u=fixture(tmp_path);p=b/'Memory/releases/1.4.0/bn_memory/parser_host.py';p.write_text('# separately modified and locally admitted parser')
 manifest=p.parents[1]/'manifest.json';m=json.loads(manifest.read_text());m['bn_memory/parser_host.py']=repair.sha(p);manifest.write_text(json.dumps(m))
 with pytest.raises(ValueError,match='Unreviewed local parser'):repair.plan(b,u)


def test_profiles_only_preserves_existing_local_ocr_fix(tmp_path):
 b,u=fixture(tmp_path);p=b/'Memory/releases/1.4.0/bn_memory/parser_host.py';p.write_text('# locally tested OCR change')
 manifest=p.parents[1]/'manifest.json';v=json.loads(manifest.read_text());v['bn_memory/parser_host.py']=repair.sha(p);manifest.write_text(json.dumps(v))
 before=p.read_bytes();r=repair.apply(repair.plan(b,u,profiles_only=True));assert r['status']=='applied'
 assert p.read_bytes()==before
 assert json.loads((b/'Memory/settings.json').read_text())['package_root'].endswith('1.4.0')
 assert '__HERMES_UDR_ROOT__' not in (b/'data/config.yaml').read_text()

def test_neo4j_ascii_config_preserves_data_and_source(tmp_path):
 import neo4j_config as nc
 u=tmp_path/'udr';source=u/'настройки';source.mkdir(parents=True)
 text='server.directories.data=/owned/persistent/data\nserver.default_listen_address=127.0.0.1\nserver.bolt.listen_address=127.0.0.1:62487\n'
 (source/'neo4j.conf').write_text(text)
 d=u/'state/services';d.mkdir(parents=True);service=d/'neo4j.json';service.write_text(json.dumps({'env':{'NEO4J_CONF':str(source)}}))
 plan=nc.plan(u);assert plan['data_paths_unchanged'] and plan['needs_change']
 plan['target']=str(tmp_path/'ascii-config'/'neo4j-conf')
 result=nc.apply(plan);assert not result['data_paths_changed'] and not result['services_started']
 assert (source/'neo4j.conf').read_text()==text
 assert (Path(plan['target'])/'neo4j.conf').read_text()==text
 assert json.loads(service.read_text())['env']['NEO4J_CONF']==plan['target']

def test_neo4j_changed_source_is_not_applied(tmp_path):
 import neo4j_config as nc
 u=tmp_path/'udr';source=u/'настройки';source.mkdir(parents=True);conf=source/'neo4j.conf';conf.write_text('server.directories.data=/owned/data\n')
 d=u/'state/services';d.mkdir(parents=True);service=d/'neo4j.json';service.write_text(json.dumps({'env':{'NEO4J_CONF':str(source)}}))
 plan=nc.plan(u);conf.write_text('changed')
 with pytest.raises(ValueError,match='changed'):nc.apply(plan)
 assert json.loads(service.read_text())['env']['NEO4J_CONF']==str(source)
