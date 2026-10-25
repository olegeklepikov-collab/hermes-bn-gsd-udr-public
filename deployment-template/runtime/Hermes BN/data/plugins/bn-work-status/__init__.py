"""Subject-matter progress uses native assistant commentary, not tool notifications.

The observer records that commentary without generating messages, model calls,
timers, task state or permissions. Native warnings and approvals are untouched.
"""
import hashlib
import logging
import threading
import time

POLICY = (
    'Промежуточные сообщения пользователю — содержательный ход решения, а не журнал инструментов. '
    'Используй обычные промежуточные сообщения ассистента. Перед первым существенным действием '
    'кратко назови предметную цель и ближайшую проверку. При смысловом переходе сообщай в 1–3 '
    'предложениях: что конкретно установлено или подготовлено; какой вопрос сейчас решаешь; '
    'что проверишь следующим и зачем. Не обязательно повторять все поля, если изменилось только одно. '
    'Например: «У двух предложений одинаковая цена, но разные условия скидки. Сверяю, сохранится ли '
    'она после первого месяца». Упоминай числа, документы и выводы только из фактически полученных '
    'данных; различай найденное, прочитанное и проверенное. План не выдавай за результат. '
    'Работу нескольких исполнителей объясняй предметными направлениями и новыми результатами, '
    'а не именами ролей, запусков или служб. При препятствии назови затронутую часть задачи, '
    'что остаётся возможным и необходимое действие для продолжения. '
    'Не объявляй поиск описаний инструментов, чтение навыков, обращения к памяти, каждую команду, '
    'каждый источник и получение технического ответа самостоятельными этапами. '
    'Не отправляй пустые сообщения «подготовка контекста», «вызов завершён», «проверка продукта», '
    '«нового результата пока нет» и повторяющиеся уведомления по таймеру. Если новых выводов или '
    'изменений плана нет, продолжай работу без отдельного сообщения. Итог дай один раз с фактическим '
    'результатом и ограничениями. Скрытые рассуждения, служебные аргументы и секреты не публикуй.'
)


class Progress:
    def __init__(self, ctx):
        self.ctx = ctx
        self.lock = threading.RLock()
        self.active = {}

    @staticmethod
    def key(sid):
        return 'session.' + hashlib.sha256(sid.encode()).hexdigest()[:32]

    def save(self, sid, row):
        saved = {k:v for k,v in row.items() if k not in {'agent','callback','wrapper'}}
        try:
            self.ctx.state.set(self.key(sid), saved)
            self.ctx.state.set('latest', self.key(sid))
        except Exception:
            logging.getLogger(__name__).warning('Cannot save commentary status; native delivery remains active', exc_info=True)

    @staticmethod
    def restore(row):
        agent = row['agent']
        if row.get('wrapper') is not None and getattr(agent,'interim_assistant_callback',None) is row['wrapper']:
            agent.interim_assistant_callback = row['callback']

    def begin(self, session_id='', turn_id='', parent_session_id='', platform='', **kw):
        if not session_id or parent_session_id or platform == 'subagent':
            return None
        from agent.subagent_lifecycle import get_active_subagent_parent
        agent = get_active_subagent_parent()
        if agent is None or str(getattr(agent,'session_id','')) != session_id:
            return None
        with self.lock:
            previous = self.active.pop(session_id, None)
            if previous:
                self.restore(previous)
            callback = getattr(agent,'interim_assistant_callback',None)
            row = {'turn_id':turn_id, 'phase':'working', 'sequence':0,
                   'last_update':'', 'updated_at':time.time(),
                   'agent':agent, 'callback':callback, 'wrapper':None}
            self.active[session_id] = row
            if callable(callback):
                def commentary(text, **metadata):
                    with self.lock:
                        if self.active.get(session_id) is not row:
                            return None
                    result = callback(text, **metadata)
                    with self.lock:
                        if self.active.get(session_id) is row and isinstance(text,str) and text.strip():
                            row.update(last_update=text, sequence=row['sequence']+1, updated_at=time.time())
                            self.save(session_id, row)
                    return result
                row['wrapper'] = commentary
                agent.interim_assistant_callback = commentary
            self.save(session_id, row)
        return {'context':POLICY}

    def finish(self, session_id, turn_id=None, phase='turn_finished'):
        with self.lock:
            row = self.active.get(session_id)
            if row is None or (turn_id is not None and row['turn_id'] != turn_id):
                return
            row.update(phase=phase, updated_at=time.time())
            self.save(session_id, row)
            self.restore(row)
            self.active.pop(session_id, None)

    def done(self, session_id='', turn_id='', **kw):
        self.finish(session_id, turn_id)

    def end(self, session_id='', completed=False, interrupted=False, **kw):
        self.finish(session_id, phase='turn_finished' if completed and not interrupted else 'interrupted_unverified')

    def close(self):
        with self.lock:
            for sid in list(self.active):
                self.finish(sid, phase='interrupted_unverified')


def register(ctx):
    progress = Progress(ctx)
    ctx.register_hook('pre_llm_call', progress.begin)
    ctx.register_hook('post_llm_call', progress.done)
    ctx.register_hook('on_session_end', progress.end)
    ctx.on_unload(progress.close)
