"""Real native state and binding; callbacks are simulated presentation, not delivery proof."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import time
import pytest
from hermes_cli.plugins_state import PluginState
from agent.subagent_lifecycle import bind_subagent_parent
spec=importlib.util.spec_from_file_location('work_status',Path(__file__).with_name('__init__.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

@pytest.fixture
def p(tmp_path,monkeypatch):
    monkeypatch.setenv('HERMES_HOME',str(tmp_path))
    value=m.Progress(SimpleNamespace(state=PluginState('bn-work-status')))
    yield value
    value.close()

def begin(p,sid='root',turn='t1'):
    notices=[];agent=SimpleNamespace(session_id=sid,status_callback=lambda kind,text:notices.append((kind,text)))
    with bind_subagent_parent(agent):assert p.begin(session_id=sid,turn_id=turn,platform='telegram')['context']==m.POLICY
    return notices

def test_each_step_start_result_and_next_step_are_factual_and_private(p):
    out=begin(p)
    p.prepared(tool_name='gsd_runtime_status',args={'secret':'never_publish'},session_id='root',turn_id='t1',tool_call_id='a')
    p.finished(session_id='root',turn_id='t1',tool_call_id='a',result={'ok':True},status='ok')
    p.prepared(tool_name='mcp__udr__udr_research',args={'request':{'action':'document','password':'never_publish'}},session_id='root',turn_id='t1',tool_call_id='b')
    assert any('ответ получен' in text for _,text in out)
    assert 'UDR: чтение оригинала' in out[-1][1] and 'Предыдущий шаг' in out[-1][1]
    assert 'never_publish' not in repr(out)
    p.finished(session_id='root',turn_id='t1',tool_call_id='b',result={'ok':False,'error':'SECRET'},status='ok')
    assert 'не выполнен' in out[-1][1] and 'SECRET' not in repr(out)

def test_stale_duplicate_and_child_results_do_not_invent_success(p):
    out=begin(p);goal='GSD_NATIVE_JOB:J.'+'a'*32+'\nYou are the actual GSD component G. Typed instruction.'
    p.child_start(parent_session_id='root',parent_turn_id='t1',child_session_id='child',child_goal=goal)
    assert 'Запущен Агент G' in out[-1][1]
    count=len(out);p.child_stop(parent_session_id='root',parent_turn_id='old',child_session_id='child',child_status='completed');assert len(out)==count
    p.child_stop(parent_session_id='root',parent_turn_id='t1',child_session_id='child',child_status='completed')
    assert 'принятие вывода не подтверждено' in out[-1][1]
    count=len(out);p.child_stop(parent_session_id='root',parent_turn_id='t1',child_session_id='child',child_status='completed');assert len(out)==count
    p.prepared(session_id='root',turn_id='t1',tool_name='terminal',tool_call_id='a')
    p.done(session_id='root',turn_id='t1');saved=p.ctx.state.get(p.key('root'));assert saved['phase']=='interrupted_unverified'
    out2=begin(p,turn='t2');assert 'незаверш' not in out2[0][1]  # prior stop is already explicit, not a false running claim
    assert out[0][0]!=out2[0][0]

def test_durable_state_profile_scope_and_heartbeat_do_not_spawn_work(p,tmp_path,monkeypatch):
    out=begin(p);p.active['root']['last_notice']=time.time()-65;p.pulse();assert len(out)==2;p.pulse();assert len(out)==2
    home=tmp_path;key=p.key('root');assert p.ctx.state.get(key)['phase']=='working'
    monkeypatch.setenv('HERMES_HOME',str(tmp_path/'B'));assert p.ctx.state.get(key) is None
    monkeypatch.setenv('HERMES_HOME',str(home));assert p.ctx.state.get(key)['phase']=='working'
    fresh=m.Progress(SimpleNamespace(state=PluginState('bn-work-status')))
    try:out2=begin(fresh,turn='new');assert 'Прежний ход' in out2[0][1]
    finally:fresh.close()
