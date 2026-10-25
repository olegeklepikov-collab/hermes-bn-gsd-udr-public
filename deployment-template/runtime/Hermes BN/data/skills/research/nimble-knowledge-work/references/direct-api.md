# Программная работа

Оболочка собственного профиля:
`__HERMES_BN_ROOT__/bin/nimble-bn`

```bash
nimble-bn search --input search.json --output .nimble/search.json
nimble-bn extract --input extract.json --output .nimble/page.json
nimble-bn agent-list --params list-params.json --output .nimble/agents.json
nimble-bn agent-run-start --ids agent-id.json --input research.json --output .nimble/started.json
nimble-bn agent-run-get --ids run-ids.json --output .nimble/status.json
nimble-bn agent-run-result --ids run-ids.json --output .nimble/result.json
nimble-bn agent-events --ids run-ids.json --output .nimble/events.json
nimble-bn mcp --server nimble --tool nimble_search --input mcp-search.json --output .nimble/result.json
nimble-bn mcp --server docs --tool search_nimble_docs --input docs-query.json --output .nimble/docs.json
nimble-bn cli -- search --query "official research sources" --search-depth standard --max-results 3
```

Input — тело JSON; ids — значения параметров пути, например {agent_id,run_id}; params — параметры GET. --input - читает стандартный ввод. --output сохраняет ответ с правами 600. Ключ загружается из собственного профиля; в аргументах процесса его нет. Данные REST находятся в response, отдельно сохраняются rate_headers. HTTP 200 сам по себе не подтверждает полноту содержания.

Доступны Search; Extract обычный/async/batch; Map; Crawl создание/состояние/список/остановка; Templates каталог/схема/запуск/async/batch/версии/генерация; Agents каталог/создание/изменение/запуски/состояние/результат/события; Tasks/Batches; Domain Knowledge/Health; SERP/Fast SERP/async/batch; Media; Jobs и их артефакты. Список и сопоставление со схемой находятся в Nimble/api.py и Nimble/источники/operations.json.

Идентификаторы, параметры и неизвестные поля проверяются локально. Исключение — устаревшая отметка format:uuid у параметров пути: она не должна отвергать возвращённые сервисом wsa_.../task_run_.... Прямой REST не выполняет автоматических повторов. Вызовы официальной библиотеки при самостоятельной программной работе задавай с max_retries=0.

MCP-схема читается перед вызовом. Собственная оболочка добавляет неперсональное назначение context и повторяет conversation_id из прежнего ответа сервиса. Она не придумывает идентификатор. Для строгого контроля параметров последнего API предпочитай REST или Nimble Python. Поиск библиотеки поддерживает текущие lite/standard; часть справки CLI остаётся старой.

Библиотека:

```python
from nimble_python import Nimble, AsyncNimble
from hermes_cli.env_loader import load_hermes_dotenv
from agent.secret_scope import get_secret

load_hermes_dotenv()
client = Nimble(api_key=get_secret('NIMBLE_API_KEY'), client_source='hermes', max_retries=0)
result = client.search(query='official sources for the research question', search_depth='standard', max_results=3)
```

Не пользуйся login/logout или --api-key для передачи ключа через историю команд. Полная официальная программа установлена в Nimble/runtime; собственная оболочка загружает ей ключ через среду. Остальные клиенты и общие настройки компьютера при установке не менялись.

Не загружай изображения или видео для обхода ограничений их показа. --binary-output применяй к конкретному разрешённому документу. Доставка в внешнее хранилище, частные cookies, webhooks и расписания требуют отдельного запроса на данные и назначение.
