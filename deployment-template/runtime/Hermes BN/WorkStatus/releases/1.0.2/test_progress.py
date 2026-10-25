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
    assert 'Подготовлен запуск: Агент G' in out[-1][1]
    p.begin(session_id='child',parent_session_id='root',platform='subagent');assert 'Исполнитель начал обработку' in out[-1][1]
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


def test_parallel_steps_are_visible_when_one_finishes(p):
    out=begin(p)
    p.prepared(session_id='root',turn_id='t1',tool_name='read_file',tool_call_id='a')
    p.prepared(session_id='root',turn_id='t1',tool_name='write_file',tool_call_id='b')
    assert 'Активные шаги:' in out[-1][1] and 'Чтение файла' in out[-1][1] and 'Запись файла' in out[-1][1]
    p.finished(session_id='root',turn_id='t1',tool_call_id='a',result={'ok':True})
    assert 'Активные шаги: Запись файла' in out[-1][1]

def test_native_execution_denial_closes_progress_without_executor_or_heartbeat(p,monkeypatch):
    from hermes_cli import middleware,plugins,execution_control
    out=begin(p);calls=[]
    manager=SimpleNamespace(_middleware={'llm_execution':[p.execution]},_report_hook_failure=lambda *a,**k:None)
    monkeypatch.setattr(plugins,'_delivery_manager',lambda:manager)
    denial=execution_control.ExecutionControlDenied('Synthetic request bound')
    def deny(*args,**kw):raise denial
    monkeypatch.setattr(execution_control,'authorize',deny)
    with pytest.raises(execution_control.ExecutionControlDenied) as caught:
        middleware.run_llm_execution_middleware({'input':[]},lambda req:calls.append(req),session_id='root',turn_id='t1')
    assert caught.value is denial and not calls and 'root' not in p.active
    assert p.ctx.state.get(p.key('root'))['phase']=='blocked'
    count=len(out);p.pulse();p.done(session_id='root',turn_id='t1');assert len(out)==count
    assert 'остановлена' in out[-1][1]

def test_execution_observer_does_not_close_another_turn_or_transient_failure(p):
    from hermes_cli.execution_control import ExecutionControlDenied
    begin(p)
    def deny(req):raise ExecutionControlDenied('test')
    with pytest.raises(ExecutionControlDenied):p.execution({},deny,session_id='root',turn_id='old')
    assert 'root' in p.active
    def transient(req):raise TimeoutError('provider retry may be handled natively')
    with pytest.raises(TimeoutError):p.execution({},transient,session_id='root',turn_id='t1')
    assert p.active['root']['phase']=='working'
