S={'type':'string'}
SCHEMAS={
 'memory_record':('Сохранить целую запись с происхождением. Сведения остаются непроверенными; секреты запрещены. Области task/project/owner; дочерняя запись запрещена.',{'content':S,'source_ref':S,'kind':{'enum':['preference','decision','note','source','candidate']},'request_id':S,'scope':{'enum':['task','project','owner']},'concepts':{'type':'array','items':S},'id':S,'expected_revision':{'type':'integer','minimum':0}},['content','source_ref','kind','request_id']),
 'memory_recall':('Поиск всего Hermes BN в разрешённых областях. local использует SQLite; hybrid добавляет AgentMemory, Graphiti/Neo4j и Zvec. Результат содержит целые записи и признаки недоступности индексов.',{'query':S,'mode':{'enum':['local','hybrid']},'limit':{'type':'integer','minimum':1,'maximum':10},'offset':{'type':'integer','minimum':0}},['query']),
 'memory_read':('Повторное чтение целой записи и версии в текущей области, с проверкой хеша. Отозванные записи недоступны.',{'id':S,'revision':{'type':'integer','minimum':1}},['id']),
 'memory_retract':('Отозвать свою запись с проверкой ожидаемой версии. История сохраняется; производные индексы получают удаление. Не удаляет прежнюю переписку.',{'id':S,'expected_revision':{'type':'integer','minimum':1}},['id','expected_revision']),
 'memory_sync':('Один ограниченный проход очереди производных индексов. Отказы видны; рекурсивных повторов нет.',{'limit':{'type':'integer','minimum':1,'maximum':10}},[]),
 'memory_scope':('Переключить область родительского сеанса на проект, заранее зарегистрированный владельцем. Новые каталоги и дочерние переключения запрещены.',{'project':S},['project']),
 'memory_status':('Состояние общей памяти, текущая область и очередь индексов. Наличие настройки не доказывает работоспособность службы.',{},[]),
 'memory_files':('Читать страницу местного файла через Mirage в разрешённом проекте; вернуть хеш и уровень чтения. Секреты, внешние пути и запись запрещены.',{'action':{'enum':['read','ls']},'path':S,'offset':{'type':'integer','minimum':0},'limit':{'type':'integer','minimum':1,'maximum':8192}},['path']),
 'memory_code':('Serena: адресный обзор символов, исходный код символа или входящие ссылки в разрешённом проекте. Только чтение, без команд и редактирования.',{'action':{'enum':['overview','symbol','references']},'path':S,'symbol':S},['action','path']),
}
