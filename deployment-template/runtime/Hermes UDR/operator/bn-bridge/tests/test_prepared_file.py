"""Real local artifact I/O and HMAC boundaries; only Telegram is a fake transport."""
from pathlib import Path
from types import SimpleNamespace
import copy
import hashlib
import hmac
import importlib.util
import json
import os
import sys

import pytest

STAGE = Path(__file__).resolve().parent.parent
SDK = Path(__file__).resolve().parents[3] / 'profile/plugins/hermes-foundation-bridge/src'
sys.path.insert(0, str(SDK))
from hermes_foundation_bridge.artifacts import ArtifactService


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def env(tmp_path, monkeypatch):
    prepared = load('prepared_file', STAGE / 'prepared_file.py')
    delivery = load('delivery_stage', STAGE / 'report_delivery.py')
    monkeypatch.setitem(sys.modules, 'prepared_file', prepared)
    root = tmp_path / 'Hermes UDR'; here = root / 'operator/bn-bridge';here.mkdir(parents=True)
    (root / 'state/authority').mkdir(parents=True)
    (root / 'state/authority/bn-bridge.key').write_bytes(b'k' * 32)
    workspace = tmp_path / 'Hermes BN/workspace'; directory = workspace / 'research/project';directory.mkdir(parents=True)
    file = directory / 'Результат.md';raw = 'Оригинал\r\n20 → 30\n'.encode();file.write_bytes(raw)
    digest = lambda value: hashlib.sha256(value).hexdigest()
    canonical = lambda value: json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    objects = {}
    class State:
        def get(self, query):
            obj = objects.get(query['object_id'])
            return {'status':'found','object':copy.deepcopy(obj)} if obj else {'status':'not_found'}
    class Runtime:
        def __init__(self):self.operations = {}
        def begin_external(self, kind, key, input_hash, target):
            old = self.operations.get(key)
            if old:return {'status':old['status']}
            self.operations[key] = {'status':'reserved','input_hash':input_hash}
            return {'status':'owned','operation_id':key,'owner':'synthetic-owner'}
        def finish_external(self, operation, owner, outcome):
            self.operations[operation]['status'] = 'already_succeeded' if outcome else 'unknown'
    artifacts = ArtifactService(root / 'foundation');artifacts.prepare(dry_run=False)
    runtime = Runtime();state = State();checks = []
    session = SimpleNamespace(state=state, runtime=runtime, check=lambda:checks.append(True))
    body = {'run_id':'r-test','phase':'running','project':'P-test','work_ref':'W-test','host_run':'H-test'}
    backend = SimpleNamespace(ROOT=root,HERE=here,canonical=canonical,digest=digest,
        saved=lambda sid:body if sid=='session' else None,session=lambda body:(session,artifacts),
        put=lambda state,obj,project,oid,run:objects.__setitem__(oid,copy.deepcopy(obj)))
    monkeypatch.setitem(sys.modules,'backend',backend)
    tokenfile = tmp_path / 'Hermes BN/data/.env';tokenfile.parent.mkdir();tokenfile.write_text('TELEGRAM_BOT_TOKEN=synthetic\n')
    transport = SimpleNamespace(sends=0,raw=None,filename=None,wrong_bot=False,wrong_readback=False,timeout=False)
    class Bot:
        def __init__(self, token):pass
        async def __aenter__(self):return self
        async def __aexit__(self,*args):pass
        async def get_me(self):return SimpleNamespace(username='wrong' if transport.wrong_bot else 'owner_bot')
        async def send_document(self,**kwargs):
            transport.sends+=1;transport.raw=kwargs['document'].read();transport.filename=kwargs['filename']
            if transport.timeout:raise TimeoutError('synthetic uncertain outcome')
            return SimpleNamespace(message_id=123,document=SimpleNamespace(file_id='synthetic-file'))
        async def get_file(self,file_id):
            async def download():return b'wrong' if transport.wrong_readback else transport.raw
            return SimpleNamespace(download_as_bytearray=download)
    import telegram
    monkeypatch.setattr(telegram,'Bot',Bot)
    return SimpleNamespace(prepared=prepared,delivery=delivery,b=backend,body=body,workspace=workspace,
        file=file,raw=raw,sha=digest(raw),artifacts=artifacts,objects=objects,runtime=runtime,transport=transport,checks=checks)


def adopt(e):return e.prepared.adopt('session','r-test',str(e.file),e.sha)


def grant(e, reference=None, **changes):
    import time
    gid='a'*32
    body={'sid':'session','run_id':'r-test','sha256':e.sha,'expires_at':time.time()+300,
          'chat_id':12345,'bot_name':'owner_bot','authorization_source':'owner-authorized:synthetic-test'}
    if reference:body['artifact_id']=reference
    body.update(changes)
    key=(e.b.ROOT/'state/authority/bn-bridge.key').read_bytes()
    mac=hmac.new(key,e.b.canonical(body),hashlib.sha256).hexdigest()
    path=e.b.HERE/'owner-grants';path.mkdir(exist_ok=True)
    (path/(gid+'.json')).write_text(json.dumps({'body':body,'mac':mac}))
    return gid


def test_intake_preserves_all_bytes_and_repeats_without_state_change(env):
    first=adopt(env);snapshot=copy.deepcopy(env.objects);again=adopt(env)
    assert first['sha256']==env.sha and first['bytes']==len(env.raw)
    assert (env.artifacts.originals/env.sha).read_bytes()==env.raw
    assert first['claims_accepted'] is False and first['delivery_authorized'] is False
    assert again['idempotent'] is True and env.objects==snapshot
    assert env.body['phase']=='running' and 'completion' not in env.body
    assert not list(env.artifacts.quarantine.glob('bn-prepared-*'))


@pytest.mark.parametrize('kind',['outside','parent','hidden','file_symlink','parent_symlink','directory','fifo','wrong_hash'])
def test_unsafe_sources_never_create_artifacts(env,kind,tmp_path):
    path=env.file;sha=env.sha
    if kind=='outside':path=tmp_path/'external.md';path.write_bytes(env.raw)
    elif kind=='parent':path=env.workspace/'research/project/../project/Результат.md'
    elif kind=='hidden':path=env.file.parent/'.secret.md';path.write_bytes(env.raw)
    elif kind=='file_symlink':path=env.file.parent/'link.md';path.symlink_to(env.file)
    elif kind=='parent_symlink':(env.workspace/'research/link').symlink_to(env.file.parent);path=env.workspace/'research/link/Результат.md'
    elif kind=='directory':path=env.file.parent
    elif kind=='fifo':path=env.file.parent/'pipe';os.mkfifo(path)
    else:sha='0'*64
    with pytest.raises((ValueError,PermissionError,OSError)):
        env.prepared.adopt('session','r-test',str(path),sha)
    assert env.objects=={} and not list(env.artifacts.originals.iterdir())


@pytest.mark.parametrize('field',['native_child','managed_worker'])
def test_children_cannot_adopt(env,field):
    env.body[field]=True
    with pytest.raises(PermissionError,match='own_root_research_required'):adopt(env)


def test_inactive_lease_blocks_before_source_copy(env):
    def deny():raise PermissionError('lease inactive')
    env.b.session=lambda body:(SimpleNamespace(check=deny),env.artifacts)
    with pytest.raises(PermissionError,match='lease inactive'):adopt(env)
    assert env.objects=={}


def test_hash_change_and_oversize_are_refused(env,monkeypatch):
    monkeypatch.setattr(env.prepared,'MAX_BYTES',len(env.raw)-1)
    with pytest.raises(ValueError,match='bounded_regular'):adopt(env)
    assert env.objects=={}


def test_exact_authorized_delivery_and_duplicate_suppression(env):
    item=adopt(env);gid=grant(env,item['artifact_id'])
    one=env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    two=env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert one['state']=='delivered' and one['readback_verified']
    assert two['status']=='already_delivered' and env.transport.sends==1
    assert env.transport.raw==env.raw and env.transport.filename==env.file.name
    assert not one['claims_accepted'] and env.body['phase']=='running'


@pytest.mark.parametrize('kind',['expired','session','artifact','mac','missing'])
def test_bad_delivery_grants_never_send(env,kind):
    import time
    item=adopt(env);changes={}
    if kind=='expired':changes['expires_at']=time.time()-1
    if kind=='session':changes['sid']='another-session'
    if kind=='artifact':changes['artifact_id']='BNAF-'+'0'*32
    gid=grant(env,item['artifact_id'],**changes)
    if kind=='mac':
        path=env.b.HERE/'owner-grants'/(gid+'.json');v=json.loads(path.read_text());v['body']['chat_id']=999;path.write_text(json.dumps(v))
    if kind=='missing':gid='b'*32
    with pytest.raises((PermissionError,FileNotFoundError)):
        env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert env.transport.sends==0


def test_canonical_corruption_and_wrong_run_are_refused(env):
    item=adopt(env);gid=grant(env,item['artifact_id'])
    (env.artifacts.originals/env.sha).write_bytes(b'corrupt')
    with pytest.raises(PermissionError,match='canonical_artifact_bytes'):
        env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert env.transport.sends==0
    with pytest.raises(PermissionError,match='own_root'):env.prepared.registered('session','other-run',item['artifact_id'],env.sha)


@pytest.mark.parametrize('failure',['timeout','readback','bot'])
def test_uncertain_or_wrong_target_never_resends(env,failure):
    item=adopt(env);gid=grant(env,item['artifact_id'])
    if failure=='timeout':env.transport.timeout=True
    elif failure=='readback':env.transport.wrong_readback=True
    else:env.transport.wrong_bot=True
    with pytest.raises((TimeoutError,PermissionError)):
        env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    calls=env.transport.sends
    with pytest.raises(PermissionError,match='no_resend'):
        env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert env.transport.sends==calls


def test_legacy_draft_grant_still_works(env):
    item=adopt(env);env.body['completion']={'draft_ref':'DRAFT'}
    env.objects['DRAFT']={'artifacts':[{'path':'report.md','sha256':env.sha}]}
    gid=grant(env)
    result=env.delivery.deliver('session','r-test',env.sha,gid)
    assert result['readback_verified'] and env.transport.sends==1


def test_real_foundation_delivery_ledger_survives_reopen(env):
    from hermes_foundation_bridge.runtime import RuntimeCoordinator
    real = RuntimeCoordinator(env.b.ROOT/'foundation')
    env.b.session=lambda body:(SimpleNamespace(state=SimpleNamespace(get=lambda q:{'status':'found','object':copy.deepcopy(env.objects[q['object_id']])} if q['object_id'] in env.objects else {'status':'not_found'}),runtime=real,check=lambda:None),env.artifacts)
    item=adopt(env);gid=grant(env,item['artifact_id'])
    first=env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert first['readback_verified']
    real=RuntimeCoordinator(env.b.ROOT/'foundation')
    repeated=env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert repeated['status']=='already_delivered' and env.transport.sends==1


def test_changed_source_after_intake_does_not_change_preserved_delivery(env):
    item=adopt(env);gid=grant(env,item['artifact_id'])
    env.file.write_bytes(b'changed later')
    result=env.delivery.deliver('session','r-test',env.sha,gid,item['artifact_id'])
    assert result['readback_verified'] and env.transport.raw==env.raw


@pytest.mark.parametrize('independent',[False,True])
@pytest.mark.parametrize('child',[False,True])
def test_native_delivery_gate_is_root_only_in_both_profiles(env,independent,child):
    plugin=load('host_policy_stage',STAGE/'plugin/__init__.py')
    host=plugin.Host(env.b.ROOT,independent=independent)
    host.rpc=lambda *args,**kw:{'status':'active','native_child':child}
    decision=host.tool_control({'tool_name':'bn_deliver_report','args':{}},session_id='session')
    assert decision.allow is (not child)
