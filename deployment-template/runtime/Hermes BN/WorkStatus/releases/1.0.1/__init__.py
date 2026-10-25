"""Thin observer over native hooks and the documented agent status callback.

No new executor, model call, task store, permission, or injected conversation turn.
"""
import contextvars
import hashlib
import json
import logging
import os
import re
import threading
import time

POLICY = ('Сообщай краткий полный статус работы. До первого действия назови цель и ближайшие этапы. '
          'При каждом смысловом переходе: «Завершено: … Сейчас: … Следующее: …». '
          'Новый этап, сервис или дочернего агента объявляй перед запуском; после шага назови фактический результат. '
          'План и запущенное выполнение различай. Если работа остановилась, укажи причину и необходимый следующий шаг. '
          'Не называй цель завершённой по одному успешному вызову. Без служебных аргументов, секретов и внутренних рассуждений.')
PREPARATION = {'tool_search','tool_describe','skills_list','skill_view'}
LABELS = {'gsd_research':'Анализ G/S/D','gsd_analyze':'Анализ G/S/D','gsd_work':'Адресная операция GSD',
          'gsd_runtime_status':'Проверка состояния GSD','gsd_status':'Проверка установленного движка GSD','read_file':'Чтение файла','write_file':'Запись файла',
          'patch':'Изменение файла','terminal':'Выполнение команды','clarify':'Ожидание ответа пользователя',
          'memory':'Работа с памятью','todo':'Учёт шагов'}
SERVICES = {'context':'Общая память','udr':'UDR','beads':'Beads','beads-dolt':'Связь задач и данных','dolt':'Dolt',
 'firecrawl':'Firecrawl','tavily':'Tavily','exa':'Exa','keenable':'Keenable','nimble':'Nimble','parallel':'Parallel',
 'consensus':'Consensus','scite':'Scite','undermind':'Undermind','alphaxiv':'AlphaXiv','openalex':'OpenAlex',
 'pubmed':'PubMed','crossref':'Crossref','semantic_scholar':'Semantic Scholar','zotero':'Zotero','r':'R',
 'wolfram':'Wolfram','asreview':'ASReview'}

def label(name,args=None):
    if name in PREPARATION:return 'Подготовка контекста и инструментов'
    if name in LABELS:return LABELS[name]
    if name.startswith('mcp__'):
        parts=name.split('__');service=SERVICES.get(parts[1], 'Подключённый сервис')
        request=(args or {}).get('request')
        action=request.get('action') if parts[1]=='udr' and isinstance(request,dict) else None
        return {'start':'UDR: открытие исследования','search':'UDR: поиск','document':'UDR: чтение оригинала',
                'note':'UDR: сохранение заметки','finish':'UDR: сохранение результата'}.get(action,service+': выполнение операции')
    return 'Выполнение операции'

def error_result(result,status=None):
    if status in {'error','failed','cancelled','interrupted','blocked','timeout'}:return True
    if isinstance(result,str):
        if len(result)>524288:return False
        try:result=json.loads(result)
        except (ValueError,TypeError):return result.lstrip().startswith(('Error','Execution blocked'))
    if isinstance(result,dict):
        if result.get('ok') is False or result.get('isError') is True or result.get('error'):return True
        nested=result.get('structuredContent') or result.get('result')
        if isinstance(nested,dict):return nested.get('ok') is False or nested.get('isError') is True or bool(nested.get('error'))
    return False

class Progress:
    def __init__(self,ctx):
        self.ctx=ctx;self.lock=threading.RLock();self.active={};self.stop=threading.Event()
        self.interval=60
        self.thread=threading.Thread(target=self.waiting,daemon=True,name='bn-work-status')
        self.thread.start()
    @staticmethod
    def key(sid):return 'session.'+hashlib.sha256(sid.encode()).hexdigest()[:32]
    def save(self,sid,row):
        safe={k:v for k,v in row.items() if k not in {'callback','context'}}
        self.ctx.state.set(self.key(sid),safe);self.ctx.state.set('latest',self.key(sid))
    def emit(self,sid,text):
        row=self.active.get(sid)
        if not row:return
        from collections import Counter
        activities=Counter([v['label'] for v in row['pending'].values()]+list(row['children'].values()))
        if activities and (sum(activities.values())>1 or row['current'] not in activities):
            text+='\nАктивные шаги: '+', '.join(name+(' ×'+str(count) if count>1 else '') for name,count in activities.items())+'.'
        row['sequence']+=1;row['last_notice']=time.time();row['notice']=text
        self.save(sid,row)
        callback=row.get('callback')
        if callable(callback):
            # Unique native status key retains transitions in chat instead of
            # repeatedly editing away the preceding completed step.
            try:
                callback('bn_work_'+hashlib.sha256(row['turn_id'].encode()).hexdigest()[:12]+'_'+str(row['sequence']),text)
            except Exception:
                logging.getLogger(__name__).warning('Work status delivery callback failed; durable state retained',exc_info=True)
    def begin(self,session_id='',turn_id='',parent_session_id='',platform='',**kw):
        if parent_session_id:
            with self.lock:
                row=self.active.get(parent_session_id)
                if row and session_id in row['children']:
                    row['current']=row['children'][session_id];row['updated_at']=time.time()
                    self.emit(parent_session_id,'Исполнитель начал обработку: '+row['current']+'.')
            return
        if platform=='subagent' or not session_id:return
        from agent.subagent_lifecycle import get_active_subagent_parent
        agent=get_active_subagent_parent()
        if agent is None or str(getattr(agent,'session_id',''))!=session_id:return
        callback=getattr(agent,'status_callback',None)
        if not callable(callback) and platform=='cli' and not getattr(agent,'quiet_mode',False):
            callback=lambda kind,text:print(text,flush=True)
        with self.lock:
            old=self.ctx.state.get(self.key(session_id),{})
            row={'turn_id':turn_id,'phase':'working','current':'Подготовка запроса','last_completed':'',
                 'pending':{},'children':{},'sequence':0,'last_notice':time.time(),'updated_at':time.time(),
                 'pid':os.getpid(),'callback':callback,'context':contextvars.copy_context()}
            self.active[session_id]=row
            prefix='Прежний ход остался незавершённым; его результаты требуют проверки. ' if old.get('phase')=='working' else ''
            self.emit(session_id,prefix+'Запрос принят. Сейчас: подготовка работы.')
        return {'context':POLICY}
    def prepared(self,tool_name='',args=None,session_id='',tool_call_id='',turn_id='',**kw):
        with self.lock:
            row=self.active.get(session_id)
            if not row or row['turn_id']!=turn_id:return
            name=label(tool_name,args);key=tool_call_id or 'unidentified'
            if key in row['pending']:return
            row['pending'][key]={'label':name,'preparation':tool_name in PREPARATION}
            previous=row['current'];row['current']=name;row['updated_at']=time.time()
            if tool_name in PREPARATION and previous==name:self.save(session_id,row);return
            prefix=('Предыдущий шаг: '+row['last_completed']+'. ') if row['last_completed'] else ''
            self.emit(session_id,prefix+'Начинаю: '+name+'.')
    def finished(self,tool_name='',args=None,result=None,status=None,session_id='',tool_call_id='',turn_id='',**kw):
        with self.lock:
            row=self.active.get(session_id)
            if not row or row['turn_id']!=turn_id:return
            item=row['pending'].pop(tool_call_id or 'unidentified',None)
            if item is None:return
            failed=error_result(result,status);name=item['label']
            row['last_completed']=name+(' — отказ или ошибка' if failed else ' — вызов завершён, ответ получен')
            row['current']='Разбор ошибки; зависимый результат не подтверждён' if failed else 'Обработка полученного результата';row['updated_at']=time.time()
            if item['preparation'] and not failed:self.save(session_id,row);return
            self.emit(session_id,('Шаг не выполнен: ' if failed else 'Получен ответ: ')+name+
                ('. Сейчас: проверка причины; зависимый результат не подтверждён.' if failed else '. Сейчас: проверка результата и следующего этапа.'))
    def child_start(self,parent_session_id='',parent_turn_id='',child_session_id='',child_goal='',**kw):
        with self.lock:
            row=self.active.get(parent_session_id)
            if not row or row['turn_id']!=parent_turn_id:return
            m=re.match(r'^GSD_NATIVE_JOB:J\.[0-9a-f]{32}\nYou are the actual GSD component ([GSD])\.',child_goal)
            name='Агент '+m.group(1) if m else 'Дочерний исполнитель'
            row['children'][child_session_id]=name
            row['current']=name;row['updated_at']=time.time()
            self.emit(parent_session_id,'Подготовлен запуск: '+name+'. Ожидаю начало обработки и фактический результат.')
    def child_stop(self,parent_session_id='',parent_turn_id='',child_session_id='',child_status='',**kw):
        with self.lock:
            row=self.active.get(parent_session_id)
            if not row or row['turn_id']!=parent_turn_id:return
            name=row['children'].pop(child_session_id,None)
            if name is None:return
            row['last_completed']=name+(' — ответ получен' if child_status=='completed' else ' — исполнение не завершено успешно')
            row['current']='Проверка продукта исполнителя';row['updated_at']=time.time()
            self.emit(parent_session_id,row['last_completed']+'. Сейчас: проверка продукта; принятие вывода не подтверждено.')
    def done(self,session_id='',turn_id='',**kw):
        with self.lock:
            row=self.active.get(session_id)
            if not row or row['turn_id']!=turn_id:return
            unfinished=bool(row['pending'] or row['children']);row['phase']='interrupted_unverified' if unfinished else 'turn_finished'
            row['current']='Выполнение остановлено; требуется проверка' if unfinished else 'Итоговый ответ подготовлен'
            row['updated_at']=time.time()
            self.emit(session_id,'Текущий ход '+('прерван; незавершённые шаги требуют проверки.' if unfinished else 'завершён. Итог и ограничения — в ответе.'))
            self.active.pop(session_id,None)
    def pulse(self):
        with self.lock:
            for sid,row in list(self.active.items()):
                if time.time()-row['last_notice']>=self.interval:
                    row['context'].copy().run(self.emit,sid,'Статус: '+row['current']+'. Нового завершённого результата пока нет.')
    def waiting(self):
        while not self.stop.wait(5):
            try:self.pulse()
            except Exception:logging.getLogger(__name__).warning('Work status heartbeat failed',exc_info=True)
    def status(self,raw=''):
        key=self.ctx.state.get('latest','');row=self.ctx.state.get(key,{}) if key else {}
        if not row:return 'Сохранённого статуса пока нет.'
        return 'Состояние: '+row['phase']+'\nПоследний шаг: '+(row.get('last_completed') or 'ещё нет завершённого шага')+'\nСейчас: '+row['current']
    def close(self):self.stop.set();self.thread.join(timeout=1)

def register(ctx):
    p=Progress(ctx)
    ctx.register_hook('pre_llm_call',p.begin)
    ctx.register_hook('pre_tool_call',p.prepared)
    ctx.register_hook('post_tool_call',p.finished)
    ctx.register_hook('subagent_start',p.child_start)
    ctx.register_hook('subagent_stop',p.child_stop)
    ctx.register_hook('post_llm_call',p.done)
    ctx.on_unload(p.close)
