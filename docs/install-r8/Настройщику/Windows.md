# Hermes BN r8 — установка и интеграция на Windows x64

Это техническое руководство адресовано агенту-настройщику. Сначала прочитайте [порядок работы и объяснение компонентов](<00 — Порядок работы.md>). Пользователю не нужно самостоятельно выполнять приведённые команды.

Далее идут сведения о составе, условия применимости, подготовка, подключение и проверки. Блоки команд — точные записи для программы: названия, регистр, кавычки и параметры нельзя заменять русскими словами. Описания объясняют, зачем выполняется шаг и что считается результатом.

Дата редакции: 11 ноября 2026 года. Выпуск **r8**, тег `public-2026-11-11-gsd-udr-full-r8`.

[Репозиторий](https://github.com/olegeklepikov-collab/hermes-bn-gsd-udr-public) · [Файлы выпуска](https://github.com/olegeklepikov-collab/hermes-bn-gsd-udr-public/releases/tag/public-2026-11-11-gsd-udr-full-r8). Предназначено для нового владельца и новой установки. Аккаунты, пароли, история, исследовательские корпуса, прежние разрешения и результаты приёмки не переносятся.

В r8 используется **один самостоятельный архив**. Основа clean-r2 и обновления r2/r4/r5/r6 больше не нужны. Не накладывайте их на r8. Сам архив обезличен, не зашифрован и не требует ключа.

| Файл | Размер | SHA-256 |
|---|---:|---|
| `Hermes-BN-GSD-and-UDR-new-user-20261111-r8.tar.zst` | 18 371 819 515 байт | `96a069fe07eae1098e2f9741e4e54a191f3fdc39ba77bed9a1f0d7c77b9ec948` |

Архив опубликован десятью частями, порядок и суммы — в `recovery-set.json` выпуска. Программа `restore.py` собирает и проверяет их. Исходники из `git clone` не заменяют эти дистрибутивы.

Состав, версии, ограничения и команды в этой редакции сопоставлены с файлами r8. Обновление документации не является новой проверкой всей платформы на другой ОС. Не используйте текущую ветку `main` поставщика вместо закреплённой версии без отдельной проверки совместимости.

| Компонент | Закрепление r8 |
|---|---|
| Основной Hermes BN | 0.22.2; исходная основа `d923a5eb487a17c0a68801bba9ef0f56c81040a8` плюс местные изменения поставки |
| Вспомогательный Hermes UDR | 0.21.3; commit `2034126e0d1f397b4612782156097243dbbdc819` плюс отдельно учтённый адаптер Telegram |
| Python BN / Node | 3.14.6 / 24.18.0; остальным средам — свои версии по `distribution/environments.json` |
| GSD | Engine 3.0.3; адаптер 0.2.13, совместимость Hermes 0.22.2 r4 |
| UDR | Research 0.44.0b2 + Foundation 0.14.0b1; местный узел и транспорт 0.3.1 |
| Общая память / Identity / Cognee | 1.4.2 / 0.1.0 / 1.6.4 |
| Beads | действующий исполнитель 1.3.1; исходное закрепление подписанного SDK 1.1.0 не переписывается |
| Dolt | BN 2.4.2; отдельно закреплённый Foundation 2.2.1 не подменяется через общий PATH |
| Graphiti / Neo4j | Foundation Graphiti 0.30.2; отдельный MCP по собственному закреплению / Neo4j 5.26.31 |
| Zvec / AgentMemory / Serena / Mirage | 0.7.0 / 0.9.29 / 1.7.0 / 0.0.6 |
| Наблюдаемость | Phoenix 20.16.0; Collector по платформенному реестру |
| R | BN 4.6.1; отдельный UDR 4.5.3; languageserver 0.3.20 |
| Zotero | 10.0.6, новый собственный профиль и библиотека |
| Новая модель / эмбеддинги | `openai-codex`, `gpt-6.1-sol`, `high` / OpenRouter, модель и размерность проверяются на целевой машине |


## Стандарт новой установки — уточнение от 11 ноября 2026 года

Первичное подключение фиксировано: **OpenAI Codex, OAuth собственного аккаунта ChatGPT, Sol 6.1 (`gpt-6.1-sol`), `high`**. Настройщик сам обследует машину, выбирает безопасные пути и совместимую техническую конфигурацию. Пользователь выполняет только необходимые входы и принимает существенные решения; технические анкеты и ручные команды от него не требуются.

Это стандарт новой установки r8; в личном резерве сохраняется фактический выбор его владельца. На новой копии настройщик до окончательного согласования задаёт `agent.reasoning_effort: high`, сохраняет `model.provider: openai-codex` и `model.default: gpt-6.1-sol`, проверяет переопределения нужных профилей/исполнителей и согласует местные допуски. Применение подтверждается реальным запросом. Без решения пользователя поставщик, модель и режим не заменяются. Действующие чужие экземпляры и архивные манифесты не изменяются.

## Навигация

Что можно установить из r8 на этой ОС → 1. Проверить Windows и подготовить каталоги → 2. Скачать самостоятельный r8 → 3. Извлечь исходники и платформенные дистрибутивы → 4. Подготовить отдельную нативную UDR → Последовательная настройка компонентов UDR → Подписи и установка согласованной пары.

Далее: поисковые и научные службы, общая память, GSD/UDR, документы, Zotero/R/Telegram, приёмка и восстановление. Выполняйте только команды своей ОС; слова ПРОФИЛЬ, SOURCE_URI и подобные обозначения заменяются фактическими значениями, а не копируются буквально.

## Что можно установить из r8 на этой ОС

**Статус:** нативные компоненты и исходники предоставлены; единая подготовка полного BN r8 на этой ОС не проверена и не автоматизирована. `deployment/prepare.py` прямо допускает только Darwin arm64; `configure-parser.py` требует `sandbox-exec`. Не удаляйте эти проверки.

Есть два разных результата:

- **Нативная UDR-платформа:** Hermes UDR, подписанная пара Research/Foundation и службы по включённым `docs/setup/ru`. Этот путь имеет команды для данной ОС и собственную приёмку.
- **Полный Hermes BN r8:** дополнительно основной изменённый Hermes, GSD, Memory 1.4.2, Cognee, Identity, местный узел UDR, транспорт файлов, профильная маршрутизация, безопасный разбор и целевые допуски. Для них требуется перенос местной подготовки и испытания. Готовность первой части не является готовностью второй.

Ниже приведены выполнимые действия и точные точки остановки. Путь не использует Docker или WSL. Установка новейшего стандартного Hermes вместо поставленного исходника не восстанавливает местные исправления BN.

## 1. Проверить Windows и подготовить каталоги

Цель — Windows 11 x64, PowerShell; Windows ARM64 и эмуляция x64 не подтверждены для полного комплекта. Рабочие базы — на местном NTFS, не exFAT и не синхронизируемая папка. Практический запас диска150ГБ — ориентир, не измеренное минимальное требование. Не заменяйте действующие установки.

```powershell
$ErrorActionPreference = 'Stop'
[System.Runtime.InteropServices.RuntimeInformation]::OSDescription
[System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture
Get-Command git,py,uv,node,java,tar -ErrorAction SilentlyContinue
$BNDownload = Join-Path $env:USERPROFILE 'Downloads\Hermes-BN-r8'
$BNKit = Join-Path $env:LOCALAPPDATA 'HermesBN-r8-supply'
$BNNative = Join-Path $env:LOCALAPPDATA 'HermesBN-r8-native'
if (Test-Path -LiteralPath $BNDownload) { throw 'Выберите новый каталог загрузки' }
New-Item -ItemType Directory -Path $BNDownload | Out-Null
Set-Location $BNDownload
```

Установите недостающие Git for Windows, Python 3.13/3.14, uv, Node 24.18.0, JDK 21, zstd, tar/7-Zip. Источники: [Git](https://git-scm.com/download/win), [Python](https://www.python.org/downloads/windows/), [uv](https://docs.astral.sh/uv/getting-started/installation/), [Node 24.18.0](https://nodejs.org/dist/v24.18.0/), [Temurin21](https://adoptium.net/temurin/releases/?version=21), [zstd](https://github.com/facebook/zstd/releases), [7-Zip](https://www.7-zip.org/).

Нативные дистрибутивы имеются и в `distribution/native/windows-x86_64` r8. До их извлечения нужен работающий инструмент распаковки; пакет не устанавливает сам Windows и системные обновления. `winget` разрешён для отсутствующих программ, но плавающая последняя версия не заменяет закрепление. После установки откройте новый PowerShell. Для npm используйте `npm.cmd`, если npm.ps1 запрещён; глобально ExecutionPolicy не ослабляйте.

Проверьте `Get-AuthenticodeSignature -LiteralPath ПУТЬ_УСТАНОВЩИКА`; издательская подпись и SHA-256 — разные проверки. В своих каталогах секретов ограничьте ACL текущим владельцем, SYSTEM и при необходимости администраторами через свойства безопасности; не переносите chmod как доказательство защиты NTFS.

## 2. Скачать самостоятельный r8

```powershell
Invoke-WebRequest -Uri 'https://github.com/olegeklepikov-collab/hermes-bn-gsd-udr-public/releases/download/public-2026-11-11-gsd-udr-full-r8/restore.py' -OutFile restore.py
Invoke-WebRequest -Uri 'https://github.com/olegeklepikov-collab/hermes-bn-gsd-udr-public/releases/download/public-2026-11-11-gsd-udr-full-r8/recovery-set.json' -OutFile recovery-set.json
if ((Get-FileHash -Algorithm SHA256 -LiteralPath .\restore.py).Hash.ToLower() -ne '1868474bbc48e4099303cf02dc57a5e7b9b1b19abbea8166017c36480d602eea') { throw 'SHA restore.py' }
if ((Get-FileHash -Algorithm SHA256 -LiteralPath .\recovery-set.json).Hash.ToLower() -ne 'b1c7090916059f381c8f6a1617ba587fedd9fb4d445cdb6967249429b298f4cf') { throw 'SHA recovery-set.json' }
py -3.13 .\restore.py --manifest .\recovery-set.json --parts-dir .\parts --output-dir .\archives --download
if ($LASTEXITCODE -ne 0) { throw 'Сборка архива не прошла' }
```

Для открытого выпуска вход GitHub не требуется. Проверьте итоговый файл через `Get-FileHash`; сумма должна быть `96a069fe07eae1098e2f9741e4e54a191f3fdc39ba77bed9a1f0d7c77b9ec948`. Никаких clean-r2 или обновлений сюда не добавлять.

## 3. Извлечь исходники и платформенные дистрибутивы

Не запускайте Mac venv и не распаковывайте целиком Mac-дерево как готовую Windows-установку. Для выборочного извлечения сначала получите TAR нативным zstd. Пример выполняется после проверки `Get-Command zstd.exe,tar.exe`:

```powershell
$BNArchive = Join-Path $BNDownload 'archives\Hermes-BN-GSD-and-UDR-new-user-20261111-r8.tar.zst'
$BNTar = Join-Path $BNDownload 'Hermes-BN-r8-source.tar'
if (Test-Path -LiteralPath $BNTar) { throw 'Выберите новый путь TAR' }
& zstd.exe -d $BNArchive -o $BNTar
if ($LASTEXITCODE -ne 0) { throw 'Ошибка распаковки zstd' }
if (Test-Path -LiteralPath $BNKit) { throw 'Каталог поставки уже существует' }
New-Item -ItemType Directory -Path $BNKit | Out-Null
& tar.exe -xf $BNTar -C $BNKit distribution DISTRIBUTIONS.json CURRENT-VERSIONS.json MANIFEST.jsonl MANIFEST.sha256 CROSS-PLATFORM-SOURCES.zip 'runtime/Hermes UDR/source' documentation install-support
if ($LASTEXITCODE -ne 0) { throw 'Не все исходные материалы извлечены' }
```

Если имена в TAR имеют начальное `./`, сначала выполните `tar.exe -tf $BNTar` и используйте ровно соответствующие имена; не игнорируйте ошибку отсутствия члена. Основной исходник BN/GSD/Memory для полного переноса извлекается отдельно из `runtime/Hermes BN` с исключением Mac-сред и только после просмотра состава.

Не применяйте `zstd | tar` через старый PowerShell: двоичный поток может преобразоваться в текст. Временный TAR занимает дополнительное место; удалять его допустимо после успешного извлечения/проверки, исходный архив сохраняйте. `verify.py` для полного Mac-дерева и его xattrs не является Windows-проверкой. Целостность поставки здесь подтверждается внешней SHA архива, затем SHA выбранных исходников из MANIFEST; ACL и нативные файлы проверяются отдельно.

## 4. Подготовить отдельную нативную UDR

```powershell
$env:UDR_SETUP_DIR = Join-Path $BNKit 'runtime\Hermes UDR\source\docs\setup'
$env:UDR_SOFTWARE = Join-Path $BNNative 'software'
$env:UDR_STATE = Join-Path $BNNative 'state'
$env:UDR_WORKSPACE = Join-Path $BNNative 'workspace'
$env:HERMES_HOME = Join-Path $BNNative 'profile-udr'
$env:HERMES_FOUNDATION_ROOT = Join-Path $env:HERMES_HOME 'foundation'
if (Test-Path -LiteralPath $BNNative) { throw 'Нативный корень уже существует' }
New-Item -ItemType Directory -Path $env:UDR_SOFTWARE,$env:UDR_STATE,$env:UDR_WORKSPACE,$env:HERMES_HOME | Out-Null
git clone --filter=blob:none https://github.com/NousResearch/hermes-agent.git "$env:UDR_SOFTWARE\hermes"
if ($LASTEXITCODE -ne 0) { throw 'git clone' }
git -C "$env:UDR_SOFTWARE\hermes" checkout --detach 2034126e0d1f397b4612782156097243dbbdc819
if ($LASTEXITCODE -ne 0) { throw 'git checkout' }
Set-Location "$env:UDR_SOFTWARE\hermes"
uv sync --frozen --python 3.13 --extra mcp --extra messaging --extra otlp
if ($LASTEXITCODE -ne 0) { throw 'uv sync' }
$env:HERMES_PYTHON = "$env:UDR_SOFTWARE\hermes\.venv\Scripts\python.exe"
$env:PATH = "$env:UDR_SOFTWARE\hermes\.venv\Scripts;$env:PATH"
hermes --version
```

Переменные задаются вновь при новом терминале либо штатной собственной конфигурацией запуска. Не переопределяйте USERPROFILE/HOME. Используется вспомогательная версия подписанной UDR, а не основной BN0.22.2. Если установка из включённого точного исходника нужна без Git, используйте его закреплённые зависимости и режим `-e`, не Mac .venv.

Для будущего основного BN заведите отдельный `profile-bn` и нативную среду. Функция запуска после её фактической сборки:

```powershell
function bn_profile {
  param([string]$Profile, [Parameter(ValueFromRemainingArguments=$true)][string[]]$CliArgs)
  if (-not $script:BNPython -or -not (Test-Path -LiteralPath $script:BNPython)) { throw 'Сначала соберите нативный Python BN' }
  $savedHome = $env:HERMES_HOME
  $savedAuth = $env:HERMES_SHARED_AUTH_DIR
  try {
    $env:HERMES_HOME = $Profile
    $env:HERMES_SHARED_AUTH_DIR = Join-Path $Profile 'shared'
    & $script:BNPython -m hermes_cli.main @CliArgs
    if ($LASTEXITCODE -ne 0) { throw 'Команда BN завершилась ошибкой' }
  } finally {
    $env:HERMES_HOME = $savedHome
    $env:HERMES_SHARED_AUTH_DIR = $savedAuth
  }
}
```

`$script:BNPython` задаётся полным путём к **реально собранному Windows Python BN**, не к Mac `venv/bin/python` и не к вспомогательной UDR. Пока BN не перенесён, используйте `hermes` только в явно заданном profile-udr. Для `save-key.py` запускайте нужный Python непосредственно с тем же временно выбранным профилем.

## Последовательная настройка компонентов UDR

Следующая таблица задаёт порядок зависимостей. Сначала нужны программы и базы, затем клиенты и только после них исполнение исследования. Положительный ответ одного сервера не заменяет проверку остальных.

Базовый каталог руководств — `UDR_SETUP_DIR`, равный `runtime/Hermes UDR/source/docs/setup` из проверенного r8. Сначала прочитайте README и три исходных документа: `HERMES_KNOWLEDGE_WORK_PLATFORM_SPEC.md`, `HERMES_ZERO_TO_DEPLOYMENT_ROADMAP.md`, `HERMES_DEPLOYMENT_AGENT_HANDOFF_PROMPT.md`.

Исполняйте соответствующие вашей ОС блоки `ru/01`–`ru/11` по порядку, но применяйте следующие уточнения r8. Это обязательная последовательность действий, а не перечень необязательных ссылок:

| Шаг | Руководство и действия | Критерий готовности |
|---:|---|---|
| 1 | `01-platform-and-hermes.md`: свои каталоги, нативные интерпретаторы, Node; вспомогательный Hermes commit 2034126… | CLI запускается в отдельном профиле, действующий BN не затронут |
| 2 | `02-sqlite.md`: проверить SQLite через Python и CLI; отдельная база/Backup API | Запись, чтение, `PRAGMA integrity_check`, восстановленная запись совпадают |
| 3 | `03-agentmemory.md`: Node пакет 0.9.29 и iii; свой файловый каталог; три loopback-порта | iii запущен раньше обработчика; `/agentmemory/health` healthy; запись и поиск своей области |
| 4 | `04-graphiti-neo4j.md`: JDK 21, Neo4j 5.26.31, Graphiti; собственная база и пароль | `RETURN 1`, добавление эпизода → обработка → поиск факта после перезапуска |
| 5 | `05-zvec.md`: Python 3.13, Zvec 0.7.0, MCP 0.3.0, новая коллекция | Проба vector/FTS/reopen; отдельно настоящий вектор нужной размерности |
| 6 | `06-engineering.md`: Serena 1.7.0, Node/uv, языковые серверы, R, DuckDB, Semgrep/ast-grep | Свой проект; найден и прочитан символ; вычисление; отсутствие права чужой записи |
| 7 | `07-observability.md`: Phoenix 20.16.0 из r8 и Collector, свои каталоги и loopback | Реальное событие доходит; секретов/полных документов в трассах нет |
| 8 | `08-services-and-recovery.md`: сначала прямой запуск, затем штатная регистрация своей службы | После повторного входа/перезапуска нужные службы доступны без дубликатов |
| 9 | `09-dolt-beads.md`: новые отдельные БД/задачи, SQL-права и история | Фактический Beads1.3.1; ветвь/commit/повторное чтение; Foundation использует свою область |
| 10 | `10-research-and-verification.md`: подписи, установка пары, native-runtime, миграция, health | Каждый включённый адаптер подтверждён, не только схема MCP |
| 11 | `11-mirage.md`: Python 3.12, Mirage0.0.6+MCP1.30.0, READ/VFS и один каталог | `read` собственного файла, отказ записи; Hermes получает только разрешённые методы |

Не объединяйте все Python-зависимости в одну среду. Mirage требует MCP1.x; основной Hermes — закреплённый MCP2.0.0. Для Graphiti Foundation и MCP среды различаются. SQLite включён в Python; отдельный сервер SQLite не нужен. Zvec — встроенная библиотека, отдельный сервер нужен лишь выбранному MCP/адаптеру.

AgentMemory также читает `~/.agentmemory/.env`: один `HERMES_HOME` не изолирует эту внешнюю настройку. Проверьте её или используйте отдельную учётную запись ОС. Его очередь в выбранной конфигурации находится в памяти; перед остановкой дождитесь завершения работ. Новая установка не импортирует чужой SNAPSHOT_DIR или AGENT_ID.

Для Graphiti различайте: граф FoundationFact и эпизодический граф MCP. Группа проекта и модель извлечения задаются явно; пароль Neo4j вводится скрыто. OAuth основного Hermes не является ключом Graphiti. Если переносите местный посредник r8 к OAuth, сначала испытайте его ограниченный интерфейс и обновление входа; без него выберите подтверждённый API-поставщик отдельно. Не подставляйте OAuth-токен в `GRAPHITI_API_KEY`.

Для Zvec перед индексированием закрепите модель, размерность, разбиение и нормализацию. Пишущий процесс один; читатели открывают read_only. При смене модели новое поколение индекса. Учебный трёхмерный тест не доказывает работу поиска с выбранной моделью и её настоящей размерностью.

В старом `ru/09` сохранён Beads1.1.0 как исходное закрепление подписанного SDK. Для BN r8 нужен **1.3.1** и местный совместимый адаптер `state/adapters/beads-runtime.json`: абсолютный путь, версия, SHA-256 и свой каталог Dolt. Не меняйте подписанный SDK и не выдавайте старый исполнитель базе новой схемы. Файлы 1.3.1 и SHA присутствуют в `DISTRIBUTIONS.json`; Linux amd64 SHA `3219443a9734b89b93fb16ee8d65844759fa1b3cd3cf139c606b7353cfb0715c`, Windows amd64 SHA `48cd82e1d3e311c9bf9a5d6d67ad1a8542ae13d4e20c5bfb527656c5e666af76`. Проверяйте имя и размер тоже.

Dolt BN 2.4.2 и Foundation 2.2.1 находятся в разных каталогах. Нельзя заменить оба одним первым найденным `dolt`. CLI-писатель и SQL-писатель не открывают одну БД одновременно. SQL слушает loopback, для Foundation создаются именованные учётные записи и четыре базы по его `DOLT_SQL.md`; безпарольный root не означает готовность.

Mirage READ и фильтры MCP ограничивают операции этого интерфейса, но не являются полной изоляцией пользователя ОС. Выделите ровно разрешённые каталоги; старые проекты добавляйте по согласованным корням без копирования и без открытия всего домашнего каталога.

### Явная замена старого шага Beads на 1.3.1

Не исполняйте команды скачивания 1.1.0 из исторического ru/09. Для нового нативного UDR используйте актуальный файл:

```powershell
$bdDownloads = Join-Path $env:UDR_SOFTWARE 'beads-1.3.1-download'
New-Item -ItemType Directory -Path $bdDownloads | Out-Null
$bdArchive = Join-Path $bdDownloads 'beads_1.3.1_windows_amd64.zip'
Invoke-WebRequest -Uri 'https://github.com/gastownhall/beads/releases/download/v1.3.1/beads_1.3.1_windows_amd64.zip' -OutFile $bdArchive
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $bdArchive).Hash.ToLower() -ne '48cd82e1d3e311c9bf9a5d6d67ad1a8542ae13d4e20c5bfb527656c5e666af76') { throw 'SHA Beads' }
& $env:HERMES_PYTHON "$env:UDR_SETUP_DIR\scripts\install_binary.py" $bdArchive bd.exe "$env:UDR_SOFTWARE\bin"
if ($LASTEXITCODE -ne 0) { throw 'Установка Beads' }
& "$env:UDR_SOFTWARE\bin\bd.exe" --version
```

Можно взять тот же файл из проверенных дистрибутивов r8 вместо загрузки. Если целевой bd.exe уже отличается, штатное средство откажет: не обходите отказ перезаписью другой установки. В новом изолированном Git-каталоге и явно выбранном BEADS_DIR используйте параметры актуального `bd init --help`; проверенная команда BN 1.3.1: `init --prefix hbn --stealth --non-interactive --skip-agents --skip-hooks`. Старый `--sandbox` из 1.1.0 не переносите вслепую. Префикс нового экземпляра можно выбрать свой.

## Подписи и установка согласованной пары

Точное закрепление: Research `0.44.0b2`, Foundation `0.14.0b1`, исходный выпуск `v0.44.0-beta.2`. Файлы и ключ выбираются из `UDR_SETUP_DIR/reference/native-tools.lock.json`. SHA публичного ключа подписи:
`2295aaab3cb418c4f81a867a701a8187e8cdd0f73105a1f318c1faf981dfdb1a`.

SHA Research ZIP: `61e15b459878d5f6ffe77849c5fe98d233aeb2fb91655be161c2cbaf2fa5fefa`.
SHA Foundation ZIP: `f847454509d608e4f5ff2013e66da1469b804f9bef6053fbb18785ea1f402337`.

`prepare_research_source.py` проверяет SHA, Minisign и внутренний манифест, затем создаёт точный местный Git-источник. Из его результата используйте **фактические** `source_uri` и `local_install_commit`; не подставляйте случайный последний commit. Установите сначала Research, затем Foundation с `--no-enable`. При ошибке подписи путь закрыт. Локальный SHA не называется подписью издателя; подпись исходного commit Hermes не подтверждена.

После установки: зависимости Foundation в выделенной среде Hermes (`zvec==0.7.0`, `PyMySQL==1.1.2`, `psutil==7.2.2`), отдельный Python Foundation Graphiti (`graphiti-core==0.30.2`, `httpx==0.28.1`). Выполните `configure_native_runtime.py` с собственным Foundation-root, Node, graph-python и приватным путём пароля Neo4j по `ru/10`. Он не меняет пароль самой базы и не заменяет существующую конфигурацию.

Далее `plugins doctor ultra-deep-research --ci`, `plugins doctor hermes-foundation-bridge --ci`, включение через `plugins enable ИМЯ --no-allow-tool-override`. В новой сессии получите фактическую схему `foundation_bridge_migrate`, сначала план `apply=false`, затем проверенное `apply=true`; `foundation_bridge_health` должен подтвердить каждый включённый нативный адаптер.

`integration_mode: standalone` позволяет самостоятельное исследование. `integration_mode: foundation` требует вызывающего узла с настоящими задачей Beads, владельцем, арендой и контрактом (`ResearchSession → run_in_host → complete`). Одно изменение YAML не создаёт этот узел и не подключает полный Hermes BN.

### Команды проверки пары на Windows

```powershell
& $env:HERMES_PYTHON "$env:UDR_SETUP_DIR\scripts\get_asset.py" minisign-0.12-win64.zip "$env:UDR_SOFTWARE\downloads"
if ($LASTEXITCODE -ne 0) { throw 'Minisign asset' }
Expand-Archive "$env:UDR_SOFTWARE\downloads\minisign-0.12-win64.zip" "$env:UDR_SOFTWARE\minisign"
$minisign = "$env:UDR_SOFTWARE\minisign\minisign-win64\x86_64\minisign.exe"
& $env:HERMES_PYTHON "$env:UDR_SETUP_DIR\scripts\prepare_research_source.py" "$env:UDR_SOFTWARE\research-release" --component research --minisign $minisign
if ($LASTEXITCODE -ne 0) { throw 'Research signature' }
& $env:HERMES_PYTHON "$env:UDR_SETUP_DIR\scripts\prepare_research_source.py" "$env:UDR_SOFTWARE\foundation-release" --component foundation --minisign $minisign
if ($LASTEXITCODE -ne 0) { throw 'Foundation signature' }
```

После изучения двух результатов отдельно выполните `hermes plugins install SOURCE_URI --ref LOCAL_INSTALL_COMMIT --no-enable` с их фактическими значениями. Команды настройки native-runtime и служб берутся из поставленных `ru/10` и `ru/08`; не заменяйте ими пользовательские состояния существующей установки.

## Модель, эмбеддинги, права и профили

Новый владелец проходит свой `hermes setup` в точном профиле. Для новой установки используйте фиксированный стандарт: OpenAI Codex, OAuth, `gpt-6.1-sol`, `high`. Исторический выбор снимка xhigh не является настройкой новой копии. Название в YAML не даёт доступа; требуется настоящий запрос. При недоступности запросите необходимое решение пользователя, не выбирая замену автоматически. Получите новый код/ссылку от Hermes; старые коды входа и чужие auth.json не копируйте. Подготовка и локальная окончательное согласование новой BN-конфигурации должны предшествовать авторизации модели; готовую рабочую UDR не переподготавливайте как пустую.

В новой установке векторная модель подключается через **OpenRouter**. Векторное представление — набор чисел, по которому индекс ищет близкие по смыслу записи. Конкретную модель выбирает настройщик из актуального каталога; размерность, правила обработки текста и все использующие модель клиенты должны совпадать с принятым договором индекса.

Подготовьте скрытый ввод отдельного ключа через [кабинет OpenRouter](https://openrouter.ai/settings/keys). Проверьте получение вектора, поиск записи другими словами и точное чтение оригинала после перезапуска. В исходном r8 сохранён Voyage; переход на OpenRouter является настройкой новой копии и, где необходимо, отдельным адаптером. Если клиент не поддерживает нужный интерфейс, реализуйте и испытайте переходник либо оставьте этот участок незавершённым. Одна замена адреса и ключа не считается интеграцией. Не смешивайте прежние векторы с новыми; создайте новое поколение индекса и проверьте его до переключения. Подписка ChatGPT не заменяет ключ OpenRouter.

Graphiti/Cognee должны использовать свой подтверждённый клиент извлечения и свой клиент эмбеддингов. Передача текста стороннему сервису задаётся владельцем. Не вставляйте токен OAuth как обычный API key. Указанные в старом примере Graphiti 1536 измерений — пример, а не требование новой установки. Сопоставьте его с фактической размерностью выбранной модели OpenRouter.

Для обычного BN, GSD-only, UDR-only и самостоятельного UDR явно проверьте `config path`. У них разные полномочия; общий владелец не означает копирование всей конфигурации. Перед длительной работой проверьте обновление входа, паузу и учёт неопределённого исхода. Содержательные статусы: что получено, что выясняется сейчас и какой результат ожидается следующим.

## Доведение нативной UDR до полного Hermes BN r8

Это отдельная инженерная часть. Работающая UDR на данной ОС ещё не означает перенос местных контроллеров, памяти и безопасного разбора BN. Ниже перечислены требуемые изменения и условия завершения; готового общего установщика r8 для этой ОС нет.

Этот этап требует исполнителя с доступом к целевой машине. В r8 нет готовой общей команды, корректно создающей полный BN на Windows/Linux. Не подменяйте её непроверенным пересохранением путей.

1. Создайте отдельную рабочую копию **текущих исходников r8**. `CROSS-PLATFORM-SOURCES.zip` и документы 14–20 октября могут содержать более ранние адаптеры; приоритет у дерева `runtime`, `CURRENT-VERSIONS.json` r8 и его манифеста. Зафиксируйте SHA каждого перенесённого исходника. Исторический архив не накладывается поверх нового дерева.
2. Для каждого окружения `distribution/environments.json` создайте новую нативную среду с указанной версией Python, установите закрепления из `distribution/requirements`. Mac wheels/библиотеки/node_modules/venv не переносятся. Наличие исходного пакета не гарантирует готовый Windows/Linux wheel; отсутствие фиксируется до включения функции. Для BN нужен совместимый 3.14.6, для Mirage3.12, для Cognee и Graphiti свои закрепления. Зависимости основного Hermes сначала проверяются `uv.lock`; дополнительные адаптеры — отдельно. Не делайте неподконтрольный общий `pip install -U`.
3. Установите изменённый Hermes из r8 в режиме разработки (`-e`), сохранив местные исправления ядра. В репозитории запрещена обычная сборка wheel/sdist; не используйте фиктивный `HERMES_NIX_BUILD`. Установка из одного upstream commit потеряет исправления маршрутизации и контроллеров. Для сравнения используйте исходный commit d923a5… плюс манифест файлов r8, не утверждайте совпадение с upstream.
4. Перенесите подготовку по смысловым контрактам `prepare.py`, `prepare-udr.py`, `prepare-memory.py`, `activate-gsd.py`, `finalize-prepared.py`: новые пути, пустые состояния, новые ключи, собственные роли, версия Beads, точные программы. Сначала реализуйте платформенные замены для сигналов/процессов, блокировок/прав, путей и оболочек; исходные macOS-скрипты целиком не исполняйте. `chmod` не заменяет ACL Windows.
5. Cognee 1.6.4 установите в отдельную среду по её перечню; создайте новый instance_id, пустые SQLite/LanceDB/Ladybug и каталог оригиналов. Подключите **местный адаптер BN** и общую очередь памяти. Один `cognee.add/cognify` не заменяет весь договор Memory 1.4.2 и разрешения. Проверьте запись → извлечение → оригинал; отдельное повторное подтверждение полноты PDF обязательно.
6. Не запускайте исторический `Memory/activate.py` (он закрепляет1.0.3) и не выдавайте его за текущую подготовку. Подключите `Memory/releases/1.4.0` и настройте все пути/исполнители под ОС. Общая SQLite, ключ, корни проектов, проекции, доставка контекста, контрольные точки, обратное чтение и границы делегирования должны проверяться вместе. Не создавайте только сервер с похожим именем инструментов.
7. Настройте Identity 0.1.0 по `Identity/GUIDE.md`: собственный SOUL, идентификаторы и наблюдаемые версии. Сохранение capture не означает активацию. Настройте GSD 3.0.3 и канонический каталог операций, роли/типизированные передачи, общее состояние/учёт и неизменяемые ограничения.
8. Адаптируйте местный `operator/bn-bridge`0.3.1: запуск/RPC, права, идемпотентное завершение, паузу, Beads, доставку точного готового файла и журнал происхождения. Сохраните источник версии и SHA всех 18 текущих файлов; не переносите старый неполный перечень17 как действующий. Подключите BN к согласованной паре, не переписывая её подписи.
9. Реализуйте платформенную изоляцию парсера по следующему разделу; без неё не включайте недоверенные PDF и зависимые пути. Установка Poppler/pdfplumber сама по себе не реализует приём `original.bin → parser → research_source`.
10. Создайте заново допуски для текущих нативных путей/байтов и рассмотренных MCP. Основной профиль, GSD-only и UDR-only проверяются отдельно. Ни один отказ обязательного контроля не превращается в «неизвестную команду» или успешную обработку. Выполните всю матрицу приёмки и восстановление.

До завершения этих пунктов корректное обозначение — «нативная UDR установлена; перенос полного BN продолжается». Инструкция не выдаёт отсутствующий адаптер за готовый. Для немедленной установки полного готового r8 используйте macOS Apple Silicon и соответствующее руководство.

## Подключение поисковых и научных служб ко всему Hermes BN

Подключения входят в `mcp_servers` **основного профиля BN**. Они доступны обычному агенту и управляемому UDR в пределах выбранных методов и прав. GSD получает только нужные инструменты роли. Самостоятельный UDR и независимые профили имеют отдельные конфигурации/входы. Установка лишь в профиль UDR не подключает службу ко всему BN.

Для каждого сервиса выполняются четыре отдельные проверки: собственный доступ → фактическая схема MCP/API → допуск контроллера → настоящий поиск/чтение/сохранение. Ключ не доказывает подключение, `mcp test` не доказывает качество исследования.

| Сервер r8 | Адрес или местный исполнитель | Доступ и действия |
|---|---|---|
| firecrawl | `https://mcp.firecrawl.dev/v2/mcp` | [Ключ](https://www.firecrawl.dev/app/api-keys), `FIRECRAWL_API_KEY`; Bearer |
| exa | `https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa,agent_run` | [Ключ](https://dashboard.exa.ai/api-keys), `EXA_API_KEY`; заголовок `x-api-key` |
| tavily | `Tavily/mcp_server.py` в собственном Python BN | [Ключ](https://app.tavily.com/home), `TAVILY_API_KEY`; проверить `HERMES_HOME` и `PYTHONPATH` |
| keenable / keenable-select | `https://api.keenable.ai/mcp` / `https://select.keenable.ai/mcp` | [Ключ](https://app.keenable.ai/console/api-keys), `KEENABLE_API_KEY`; `X-API-Key` |
| nimble / nimble-docs | `https://mcp.nimbleway.com/mcp` / `https://docs.nimbleway.com/mcp` | [Ключ](https://online.nimbleway.com/settings/api-keys), `NIMBLE_API_KEY`; основной сервер Bearer |
| parallel-search / parallel-task | `https://search.parallel.ai/mcp?mode=fast` / `https://task-mcp.parallel.ai/mcp` | [Кабинет](https://platform.parallel.ai/), `PARALLEL_API_KEY`; Bearer или отдельный поддержанный OAuth |
| consensus | `https://mcp.consensus.app/mcp` | [Аккаунт/API](https://consensus.app/), `MCP_CONSENSUS_API_KEY`; предусмотренный Bearer-доступ |
| scite | `https://api.scite.ai/mcp` | Собственный [Scite](https://scite.ai/) OAuth и принятие условий |
| undermind | `https://mcp.undermind.ai/mcp` | Собственный [Undermind](https://www.undermind.ai/) OAuth и возможности плана |
| alphaxiv | `https://api.alphaxiv.org/mcp/v1` | [Свой вход](https://www.alphaxiv.org/signin), OAuth |
| pendar | `https://pendar.ai/mcp` | [Pendar](https://pendar.ai/), OAuth; проверить фактический остаток вызовов |
| openalex | `https://mcp.openalex.org/mcp` | OAuth своего аккаунта; исправления профиля в исследовательской роли не включать |
| openalex-api | `OpenAlex` и местный сервер из r8 | [Свой ключ](https://openalex.org/settings/api); отдельно от OAuth, сохранять штатным вводом адаптера |
| scholarsidekick | `https://scholar-sidekick.com/api/mcp` | Проверить доступный публичный режим; возможности по текущей схеме |
| semanticscholar | местный сервер `SemanticScholar` | [Ключ](https://www.semanticscholar.org/product/api) после одобрения; режим без ключа только если реально отвечает, при 429 остановиться |
| crossref | местный сервер `Crossref` | [Инструкция](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/); свой разрешённый контакт, бесплатный режим |
| pubmed | местный сервер `PubMed` | [NCBI](https://www.ncbi.nlm.nih.gov/); свой технический контакт; необязательный собственный API key |
| russianresearch | местный переходник | eLIBRARY, DisserCat, КиберЛенинка: внешнее обнаружение и свои файлы; прямой доступ не включён автоматически |
| webofscience | местная заготовка доступа | [Clarivate](https://developer.clarivate.com/); собственные лицензия/ключ и разрешение использования с языковой моделью; без них исследовательские запросы выключены |
| wolfram | `https://agenttools.wolfram.com/mcp` | Context → Alpha / LanguageEvaluator; проверить текущий доступ |
| TinyFish | фактического подключения в локальном r8 нет | Получить свой адрес/SDK/ключ по [официальной документации](https://docs.tinyfish.ai/), отдельный допуск и приёмка; не придумывать контракт |

Это адреса и имена поставки r8, а не обещание доступности каждого сервиса вашему аккаунту. Перед выдачей ключа проверьте официальный адрес и схему выбранного сервера; исторические лимиты/тарифы не переносите.

Включайте существующую запись, не заменяйте весь YAML. Пример части файла:

```yaml
mcp_servers:
  firecrawl:
    url: https://mcp.firecrawl.dev/v2/mcp
    headers:
      Authorization: "Bearer ${FIRECRAWL_API_KEY}"
    enabled: true
    lazy: true
    connect_timeout: 60
    timeout: 180
```

`${FIRECRAWL_API_KEY}` остаётся буквальной ссылкой; значение хранится в собственном защищённом файле профиля. Для Exa нужен `x-api-key`, для Keenable — `X-API-Key`: общий Bearer-диалог не подходит автоматически. Сохраните фильтры методов поставки; неизвестные новые методы не включаются через `*` ради полноты.

Для HTTP OAuth существующая запись имеет `enabled: true`, `auth: oauth` и свой адрес. Выполните `mcp auth ИМЯ` в **точном профиле**; войдите в свой аккаунт в новом браузерном окне и проверьте предоставляемые права. Пароли, коды и ссылки с токенами в документы/переписку не копировать. После подключения — `mcp list`, `mcp test ИМЯ`, `tools list --platform cli`; Telegram проверяется отдельно. Точные команды вызываются через функцию профиля из этой инструкции.

Ключи сохраняются локально через `hermes setup` / штатную форму конкретного адаптера. Если требуется собственный ввод, создайте локальный `save-key.py` и запустите **интерпретатором BN с выбранным HERMES_HOME**:

```python
import getpass, re
from hermes_cli.config import save_env_value, get_env_value
allowed = {'FIRECRAWL_API_KEY','EXA_API_KEY','TAVILY_API_KEY',
           'KEENABLE_API_KEY','NIMBLE_API_KEY','PARALLEL_API_KEY',
           'MCP_CONSENSUS_API_KEY'}
name = input('Имя переменной: ').strip()
if name not in allowed:
    raise SystemExit('Неизвестная переменная')
if get_env_value(name):
    raise SystemExit('Ключ уже задан; сохранён существующий')
value = getpass.getpass('Ключ, ввод скрыт: ').strip()
if not value or re.search(r'[\s\x00-\x1f\x7f]', value):
    raise SystemExit('Некорректный ключ')
save_env_value(name, value)
print('Сохранено без вывода значения')
```

Запускайте как файл из интерактивного терминала. Не передавайте секрет в командной строке, адресе URL, глобальной среде пользователя или файле службы. Для OpenAlex, эмбеддингов и других адаптеров используйте их собственный формат, а не неподтверждённое имя переменной.

### Полный набор операций и соответствующие ограничения

#### Firecrawl

Подключите `firecrawl`, проверьте поиск, чтение и карту. Основные методы: `firecrawl_search`, `firecrawl_scrape`, `firecrawl_map`; для корпуса — `firecrawl_crawl` и `firecrawl_check_crawl_status`. Дополнительно доступны задания `firecrawl_agent`/`firecrawl_agent_status`, разбор `firecrawl_parse`, инструменты научного поиска/чтения, браузерные действия и наблюдение за изменениями, если они возвращаются текущей схемой.

API/CLI `$BN_ROOT/bin/firecrawl-bn` дополняет MCP форматами и пакетными операциями. Создание браузерного сеанса, исполнение действий, создание/изменение наблюдения и отправка содержимого — отдельные действия, которым не следует давать автоматическое разрешение только ради поиска. Чтение каждой страницы проверяйте по ошибкам и полноте; успешное задание не означает успешные все страницы. [Официальная справка](https://docs.firecrawl.dev/mcp-server).

#### Exa

Включите все четыре нужных метода **в одном параметре `tools`** адреса: `web_search_exa`, `web_fetch_exa`, `web_search_advanced_exa`, `agent_run`. Параметр заменяет набор по умолчанию, поэтому указание только расширенного поиска может убрать обычный поиск/чтение. Расширенный поиск нужен для точных доменов, дат, типа материала и фрагментов; чтение выполняется отдельно по найденным URL.

`agent_run` — отдельный исследовательский процесс поставщика, не роль G/S/D и не локальный сборщик UDR. Прямой API `$BN_ROOT/bin/exa-bn` предусмотрен для дополнительных операций, структурированных заданий, обогащения и пакетной работы по поставленной схеме. Сохраняйте ID, состояние и фактический расход; результат модели поставщика не считается независимо проверенным. [Официальный каталог MCP](https://github.com/exa-labs/exa-mcp-server).

#### Tavily

Основной вариант комплекта — **местный полный MCP**, а не только удалённый сервер. Он даёт `tavily_search`, `tavily_extract`, `tavily_map`, `tavily_crawl`, `tavily_research`, `tavily_get_research`, `tavily_research_stream`, `tavily_usage`, `tavily_logs`. Для поиска доступны `general`/`news`/`finance`, глубина, даты, домены и дополнительные поля по текущей схеме.

Проверяйте `failed_results` извлечения. Для обзора сайта используйте карту, затем ограниченный обход; для исследовательского задания сохраняйте `request_id` и опрашивайте прежнее задание, а не создавайте повтор при каждом ожидании. Расход/журналы доступны владельцу и не равны источникам исследования. Удалённый Tavily MCP — альтернативный транспорт с собственным набором; его подключение не доказывает наличие всех девяти методов местного переходника. [Официальный MCP](https://docs.tavily.com/documentation/mcp).

#### Keenable и SELECT

`keenable` предоставляет поиск `search_web_pages`, чтение `fetch_page_content` и другие заявленные текущей схемой операции. `keenable-select` — отдельное подключение для табличного извлечения через SELECT; это не доступ к вашим местным SQLite/Dolt и не разрешение произвольного SQL.

Прямой API/CLI `$BN_ROOT/bin/keenable-bn` дополняет MCP. Проверьте поиск, точное чтение, затем одну таблицу по двум публичным страницам с сохранёнными URL. Публикация отчёта/ссылки, если доступна, является отдельным внешним действием; в обычную проверку чтения не входит. Официальные варианты MCP/CLI/REST: [справка Keenable](https://docs.keenable.ai/). Не запускайте `configure-mcp --all`, меняющий чужие обнаруженные клиенты, ради отдельной установки BN.

#### Nimble

Основное подключение `nimble` даёт веб-поиск, извлечение, шаблоны и исследовательские задания по текущей схеме и своему доступу. `nimble-docs` ищет **только справку Nimble**. Не представляйте второй сервер как альтернативный поисковик по сети.

Поиск и полный текст различаются: поля/уровни результата берутся из действующей схемы, полный текст запрашивается отдельно, когда это требуется. У задания сохраняйте идентификаторы и конечное состояние; постановка в очередь не является завершением. Создание/изменение шаблона, удаление агента и другие изменяющие методы остаются выключенными до отдельной потребности. Прямой `$BN_ROOT/bin/nimble-bn` дополняет MCP; перед использованием шаблона проверьте его актуальную схему и выход. [Официальная документация](https://docs.nimbleway.com/).

#### Parallel Search и Task

Подключения разные: `parallel-search` — поисковая выдача и доступные операции чтения; `parallel-task` — задания глубокого исследования/обогащения и их результаты. Search имеет отдельный публичный вариант, Task требует собственного доступа. Не считайте успешный Search подтверждением Task. [Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp), [Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp).

Комплект также содержит `$BN_ROOT/bin/parallel-bn`: собственный ключ, изолированное состояние CLI и профили для дополнительных API. Наборы заданий, структурированное исследование, FindAll, наблюдения и другие семейства выбираются по поставленной версии/схеме. Они не становятся инструментами модели только потому, что есть команда CLI. Для доступного модели MCP проверьте реальный список; для CLI вызова — отдельный допуск команды и области файлов. Асинхронное задание продолжается по прежнему ID; продолжение UDR хранит эту связь после перерыва.

#### Consensus

Подключите `consensus`, проверьте метод `search`, затем фильтры по годам, типу исследования, области и рецензированию, которые действительно возвращает схема. Название, DOI и год сопоставляйте с Crossref/PubMed/издателем. Аннотация, выдержки и полный текст — разные уровни чтения; отсутствие выдержек полного текста фиксируется прямо.

`$BN_ROOT/bin/consensus-bn` использует собственные профили и параметры API. Для прямого API требуется собственный `Consensus/config/access.json` с реальным `credential_env` и пределами вашего плана; наличие ключа MCP само по себе его не создаёт. При отсутствии этих подтверждённых данных используйте проверенный MCP и отмечайте прямой путь как не настроенный. [Документация Consensus](https://docs.consensus.app/).

#### Scite

OAuth подключает `scite`. Исследовательское ядро: `search_literature`, `read_fulltext`, `citation_graph`, `bibliography`, `report_citations`, `citation_report`. Дополнительные семейства поставки: патенты, гранты, клинические исследования, препараты, медицинские устройства, сообщения о безопасности, коллекции/заметки/файлы.

Доступность каждого семейства проверяется отдельно; библиотека/коллекции и загрузка файлов не включаются молча вместе с поиском. После чтения полезно зарегистрировать использованные записи через `report_citations` и проверить `citation_report`. Категории `supporting`/`contrasting`/`mentioning` описывают классификацию контекста Scite, не научную приёмку. Переход на MCP не исправляет недоступный тариф и не подтверждает REST API. [Сервис](https://scite.ai/), точные выбранные методы — `Scite/config/mcp-selected.json`.

#### Undermind

После OAuth выберите/создайте **своё** рабочее пространство. Инструменты обнаружения: `search_papers`, `find_papers_by_author`, `lookup_papers_by_metadata`, `get_paper_info`. Целевое чтение PDF — `read_pdfs`, ссылки на доступные PDF — `get_pdf_download_links`.

Глубокий поиск: `launch_deep_search`, `inspect_deep_searches`, `display_deep_search_results`, `display_references`. Операции папок, файлов, добавления/перемещения/отметки работ отделяются от чтения. Pro в браузере не доказывает доступность каждого режима MCP; проверьте выбранный режим своим аккаунтом. Полнотекстовый поиск и вопрос к PDF не означают чтения всей статьи. [Сервис](https://www.undermind.ai/), контракт — `Undermind/config/mcp-selected.json`.

#### AlphaXiv

После OAuth подключите `discover_papers`, `get_paper_content`, `answer_pdf_queries`, поиск/разрешение исследователей и доступные операции чтения библиотеки/заметок. Для ответов по статье фиксируйте arXiv ID, версию, страницы и источник: `get_paper_content(fullText=false)` может возвращать обзор ИИ, который нельзя выдавать за исходный текст.

Папки, сохранение/перемещение работ, личные метаданные и подписки доступны владельцу отдельно от исследовательского чтения. Создайте свою закрытую исследовательскую папку, если нужна библиотека; не переносите чужие её ID. [Вход](https://www.alphaxiv.org/signin), набор методов — `AlphaXiv/config/mcp-selected.json`.

#### Crossref

Местный `crossref` подключается без обязательного ключа. Основной набор: `works_search`, `work_get`, `works_batch`, `bibliographic_match`, `doi_agency`, `doi_exists`, ссылки/отношения/исправления, финансирование и лицензии, поиск сущностей и сводные поля. Дополнительный набор — преобразование метаданных, стили и экспорт, XML/OpenURL и справочное обнаружение наборов/OAI по схеме.

Проверьте точный DOI и отличайте `published`, `published-online`, `published-print`, `created`, `deposited`, `indexed`. Метаданные издателя не являются доказательством прочитанного полного текста или достоверности научного вывода. [Правила API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/).

#### OpenAlex: два дополняющих варианта

Официальный `openalex` после своего OAuth: `search_works`, `get_work`, `resolve_references`, `list_citations`, сущности, группировки/анализ, ключевые слова и поддержанные операции запросов. Методы изменения авторского профиля не добавляйте для обычного исследования.

Местный `openalex-api` со своим ключом: сущности и пакетное получение, смысловой поиск, аннотации, связи/метрики, запросы/классификация, загрузка содержимого, `content_structure`, `read_content`, `read_pdf_pages`, `render_pdf_page`, экспорт и сохранение запросов. Содержание PDF и GROBID TEI различаются. Иллюстрацию/таблицу сверяйте по изображению исходной страницы; индексная связь цитирования не означает поддержку вывода. [Свой API-доступ](https://openalex.org/settings/api).

#### Semantic Scholar

Местный `semanticscholar`: поиск/массовый поиск, совпадение названия, карточки и пакетное получение работ/авторов, ссылки и цитирования, рекомендации, фрагменты, сведения о выпусках наборов и различиях. Сначала `service_status`, затем один небольшой `paper_bulk_search` или поиск точного DOI/названия.

Без ключа допустима только фактически доступная публичная выдача. При `429` остановите этот путь и соблюдайте паузу; не запускайте десятки одинаковых попыток. Заявку на ключ не подавайте повторно автоматически. Запись о наборе данных не означает, что набор скачан и прочитан. [Официальный API](https://www.semanticscholar.org/product/api).

#### PubMed и PMC

Местный `pubmed`: поиск, сведения о базе/истории запроса, краткие и полные библиографические записи, связи, исправление поискового термина, сопоставление цитаты и экспорт. PMC: метаданные/лицензия/версия, структура разделов, адресное чтение, таблицы и статус PDF.

Проверьте PMID/PMCID/DOI одной статьи, прочитайте аннотацию, затем одну доступную таблицу PMC с подписью/примечаниями. Библиографический год и дата электронной публикации могут отличаться; сохраните оба. Лицензия и доступность текста проверяются отдельно. Ключ необязателен для исходной установки; технический контакт — собственный. [NCBI](https://www.ncbi.nlm.nih.gov/).

#### Pendar и Scholar Sidekick

`pendar` после OAuth предоставляет шесть инструментов: `verify_paper`, `survey_literature`, `graph_hopper`, `audit_bibliography`, `profile_researcher`, `find_venues`. Это проверка/структурирование области; `abstract_snippet` не является полной аннотацией. Проверьте один DOI до запуска большого обзора. [Сервис](https://pendar.ai/).

`scholarsidekick`: `verifyCitation`, `auditBibliography`, `checkRetraction`, `checkOpenAccess`, `resolveIdentifier`, `formatCitation`, `exportCitation`. В проверке метаданных явно используйте `screenWithLlm=false`, если модельный разбор не настроен и не нужен. Форматированную ссылку сверяйте с метаданными: форматировщик может пропустить номер статьи. DOI-совпадение не подтверждает изложенные в статье выводы. Адрес MCP: `https://scholar-sidekick.com/api/mcp`.

#### Русскоязычные площадки и Web of Science

`russianresearch` объединяет план запросов, обнаружение кандидатов, DOI-разрешение и чтение законно предоставленных документов. Для eLIBRARY/DisserCat/КиберЛенинки прямой доступ по умолчанию не заявляется. В отчёте указывайте настоящий поисковый сервис, например Tavily с ограничением домена. Отдельно подтверждайте открытие оригинальной страницы, автора, год и полноту файла.

`webofscience` в исходной конфигурации предоставляет `service_status`, `capability_catalog`, `query_plan`, `access_request`. Это подготовка подключения, а не действующий поиск по базе. Получите собственный продукт/ключ и необходимое разрешение Clarivate для работы с LLM; чужие согласия не применяются. До разрешения оставьте рабочий поиск закрытым и используйте доступные источники с точным указанием ограничения. [Clarivate Developer](https://developer.clarivate.com/).

### Подключение к ролям, профилям и каналам

Правьте четыре области осознанно: основной BN; `bn-gsd-only`; `bn-udr-only`; самостоятельный UDR, если он используется. Не копируйте весь YAML основного профиля поверх независимого: это вернёт отключённый модуль. Переносите только рассмотренные подключения и ссылки на свои секреты. `tools.include` не является изоляцией файловой системы процесса.

Для местных серверов Windows не исполняет bash-оболочки `bin/*`: нужен явный `python.exe` и проверенная точка входа `.py`. На Linux также замените Mac-пути Python/Java/Node. Аргументы, каталог запуска и среда должны соответствовать **реальной** программе r8; переименование оболочки в `.exe` не является переносом. До готовности такой сервер остаётся выключенным.

В управляемом UDR поиск выполняет основной BN; `mcp__udr__udr_research` ведёт состояние исследования, но не заменяет реестр поставщиков. Исполнители наследуют ограничения, общий учёт и адресные входы. Полный набор сервисов у родителя не означает все права у каждого потомка.

Разрешённая поверхность сборщика находится в `operator/bn-bridge/worker_policy.py`: Exa search/fetch, Tavily search/extract/map, Keenable search/fetch, Parallel Search, выбранные Firecrawl/Consensus/Scite/Undermind/AlphaXiv/OpenAlex/PubMed/Crossref. Nimble, SELECT, Parallel Task, Pendar и прочие методы не разрешаются сборщику автоматически. Их выполняет родитель либо проводится адресная адаптация политики. Доменные ограничения должны передаваться поддержанным структурным параметром и проверяться на возвращённых URL.

`bn_parallel_search` — ограниченные независимые поисковые запросы, не произвольные MCP. `bn_udr_team` — сохранённые дочерние задачи с Beads и зависимостями. Не запускайте вложенный самостоятельный исследовательский цикл каждого поставщика в каждом потомке.

Новые установки согласуют рассмотренные подключения до локальной окончательного согласования. В действующей GSD установке `install-support/admit-mcp-transport.py --home ПРОФИЛЬ --server ИМЯ` сначала показывает план; применение требует `--apply`, `--expected-config-sha256`, `--expected-settings-sha256` из этого плана. Он меняет только допуск известного транспорта, сохраняет квитанцию и не разрешает новые инструменты. На Windows/Linux его файловые гарантии и зависимости сначала проверяются на новой копии; успех macOS не переносится автоматически.

При `MCP source transport/config changed` сверяйте подключение и допуск; не отключайте контроллер. При `too many names: 16 > max 10` запрашивайте описания партиями максимум по 10. Имена инструментов берутся из фактической схемы, а не из предполагаемого склеивания `mcpcontext...`.

### От результатов поиска к проверяемому корпусу

Создайте отдельный проект: постановка, план, журнал запросов, реестр источников, оригиналы, извлечённые фрагменты, наблюдения/гипотезы, проверки и итоговый Markdown. Для каждого объекта сохраняйте настоящий сервис/метод, параметры, время, ID внешнего задания, URL, версию/лицензию, SHA-256 оригинала, адрес фрагмента и фактический объём чтения. Отдельно отмечайте ошибки, неполные остатки, расход и ограничения выборки.

Путь документа: исходный файл → разрешённый разбор → регистрация точного фрагмента и его происхождения → чтение конкретным исполнителем → предметная проверка → отчёт. В UDR используйте реальные схемы `source`/`fetch`/`note`/`read` и `intake`; нельзя придумывать дополнительные поля или считать `raw_acquired_requires_host_intake` обработанным источником.

SQLite/первичный журнал хранят происхождение; Dolt — версии таблиц/отчётов; Beads — задачи и зависимости; AgentMemory, Zvec, Graphiti/Neo4j и Cognee — связанные проекции для извлечения. Они не создают независимых подтверждений исходной публикации. Zotero сохраняет библиографию и вложения; ASReview задаёт порядок просмотра и фиксирует решения. R/Wolfram проверяют расчёты, но не исправляют нерепрезентативную выборку отзывов.

### Приёмка каждого внешнего подключения

| Проверка | Подтверждаемый результат |
|---|---|
| Доступ и схема | Свой аккаунт; нужные методы реально объявлены |
| Поиск | Один узкий запрос; известны параметры, поставщик и ограничения |
| Чтение | Открыт конкретный найденный источник; выдача отделена от оригинала |
| Длительное задание | Сохранены ID, состояние, результат; продолжение не создаёт дубль |
| Сохранение | Точный фрагмент и происхождение записаны и повторно прочитаны |
| Профили | Обычный BN, требуемые GSD/UDR-профили и Telegram работают с правильной областью |
| Потомок | Разрешённый запрос выполнен; запрещённый отклонён до действия |
| Ошибка | Неверный ключ/429/тайм-аут дают настоящую причину; повторы ограничены |

Проверьте четыре маршрута: общий поиск → оригинал → отчёт; научная запись → DOI/полный текст → библиография; длительное задание → пауза → чтение того же результата; местный документ → разбор → память → точное чтение оригинала. Не покупайте все службы ради отметок: отсутствующую возможность фиксируйте, отключённое подключение не называйте проверенным.

## Zotero, R/ASReview и Telegram

Zotero 10.0.6 устанавливается нативно из [официального источника](https://www.zotero.org/download/). Создайте **отдельный** профиль и каталог данных своей установки. Запускайте приложение с явно заданным `-profile ПУТЬ`, проверьте настройку каталога данных, местный API и свой порт 23119 или свободный выбранный. Пустой стандартный профиль и библиотека BN — разные источники. После своего входа отдельно проверьте синхронизацию; локальный API её не подтверждает.

Адаптер r8 закрепляет Server-ID: при HTTP412 сначала проверьте профиль/библиотеку, не снимайте защиту. Для Windows/Linux нужны нативный путь приложения и проверенный запуск местного `.py` вместо Mac-оболочки. Контроль: карточка → синтетическая заметка → повторное чтение → восстанавливаемая корзина. PDF-пути, безопасный разбор и чтение полного текста испытываются отдельно.

Для R нужны разные нативные среды BN4.6.1 и UDR4.5.3 с собственными библиотеками. Mac R.framework/conda-библиотеки не копируются. Установите исходные/платформенные пакеты из перечня r8, проверьте `stats`, `ggplot2`, `languageserver`0.3.20, генерацию графика и путь R для Serena. Тест: mean(1:5)=3, var(1:5)=2.5, график x=y=1:5 сохранён и читается. Наличие графика не доказывает все операции Serena.

ASReview включается отдельным местным сервером: своё хранилище, синтетический импорт → две разметки → обучение → следующие записи → новая разметка → повторное обучение → экспорт и чтение. Полнота поиска и научная релевантность требуют предметной проверки, а не только ранжирования.

Создайте своего бота через [BotFather](https://t.me/BotFather), токен сохраните местным защищённым вводом в **нужном профиле**. Настройте разрешённые числовые ID; чужие ID/боты не наследуются. Затем `gateway setup`, пробный `gateway run`, /whoami, сообщение и точный небольшой файл. Один токен обслуживается одним согласованным получателем; второй polling-шлюз с тем же ботом конфликтует. Для совместного шлюза профильная область поиска и исполнения команд должна сохраняться; r8 содержит gateway-r5.

## Автозапуск на Windows

Автозапуск сохраняет команду и условия запуска после входа пользователя. Задача планировщика не равна системной службе, работающей до входа. Остановка родительского процесса не всегда останавливает дочерние; проверяются нужные процессы и порты.

Сначала iii → обработчик AgentMemory; Neo4j → Graphiti; затем SQL/Cognee/наблюдаемость; шлюз — после готовности обязательных зависимостей. Штатные JSON `name/argv/cwd/env_file` содержат абсолютные Windows-пути и ссылки на приватные файлы, без значений секретов. Программы stdio запускает Hermes, дополнительные фоновые копии не нужны.

```powershell
& $env:HERMES_PYTHON "$env:UDR_SETUP_DIR\scripts\render_services.py" "$env:UDR_STATE\services\agentmemory.json" "$env:UDR_STATE\services\generated" --platform windows
if ($LASTEXITCODE -ne 0) { throw 'Служба не подготовлена' }
```

Просмотрите созданный `agentmemory-register.ps1`, имя и владельца задания, затем выполните его и проверьте `Get-ScheduledTaskInfo`. Планировщик запускает задачу при входе пользователя; это не подтверждение работы до входа. Для Neo4j используйте собственную проверенную Windows Service; не устанавливайте дублирующую службу. Остановка задания не гарантирует остановку всех дочерних процессов: подтвердите штатный stop и закрытие нужных портов.

R.exe/Rscript.exe и Zotero.exe указываются полными нативными путями; `npm.cmd`/прочие cmd-оболочки не заменяются Unix shebang. Проверяйте каталоги с пробелами, кириллицей и CRLF, отсутствие наследования чужих секретов и восстановление после повторного входа.

## Общая память, GSD и UDR: подключение и безопасный разбор

Основной интерфейс общей памяти в r8 — сервер `context` из `Memory/releases/1.4.0/bn_memory/server.py` со своим `settings.json`. Он обслуживает BN, GSD и UDR через разрешённые корни проектов, журнал SQLite, очереди проекций и адресный контекст. Для каждого проекта задайте владельца, область, путь к оригиналам, версии и состояние свидетельств.

До первого исследования подтвердите: запись синтетического источника → обработка предусмотренных индексов → гибридный поиск → указание, какие системы фактически вернули запись → чтение оригинала → сохранение после перезапуска. Повторите в обычном BN без запуска UDR/GSD. Проверьте отказ в чужой области. При выключенной одной проекции результат должен сообщать неполноту, а не объявлять все индексы успешными. Новому владельцу не переносятся старые ключи общей памяти, уроки Cognee, полномочия или отметки принятия.

GSD Engine 3.0.3 устанавливается из канонической поставки в `GSD/vendor/1.1.0`; история не становится действующими инструкциями. Хуки работают на жизненном цикле, роли G/S/D получают типизированные входы и ограничения; навыки предоставляют каталог операций. Явно проверяются все семь сочетаний ролей и шесть профилей по контрактам, а не по произвольному тексту запроса. Для межмодульного режима необходим местный узел UDR 0.3.1, корректный Beads и подтверждённые Foundation/Research; одна установка плагинов этого не обеспечивает.

Новые ключи и допуски выдаёт владелец/локальная доверенная программа. Нельзя копировать прежние подписи состояния или поручать модели расширить собственные права. Свежая политика расхода r8 — `budget_mode=observe`; контроль разрешений, квитанций, неопределённых исходов, остановки и отмены остаётся. Истёкшее поколение `/gsd resume` не возобновляет: нужно новое поколение `/gsd new` с сохранением старой истории. Длительное исследование UDR продолжается по сохранённому ID и новому допустимому исполнению, даже через большой промежуток времени.

Безопасный разбор r8 — **местный адаптер macOS arm64**, использующий `sandbox-exec`. Он не переносится сменой строки `platform`. На Windows/Linux требуется явная реализация того же контракта: процесс без сети, унаследованных ключей и произвольного запуска программ; чтение разрешённого оригинала; запись только выделенного результата; лимит памяти/времени шага; контроль SHA; продолжение; полный реестр страниц/таблиц/вложений; отказ зависимого пути при сбое защиты. Подписи поставщиков не переписываются. До проверки адаптера разбор недоверенных документов и зависимый путь UDR остаются закрытыми.

Требуемые испытания адаптера: PDF на 1001 страницу с поздним маркером, скан с OCR, кириллица, продолжение после остановки, повтор без нового процесса, повреждённый/зашифрованный файл, смена оригинала, переходы по ссылкам, отсутствие сети и чтения чужих файлов. Дополнительно DOCX/ODT/RTF/TXT/HTML, таблицы XLSX/старый XLS/CSV, JSON/SQL и вложения проверяются по реально реализованным форматам. SQL, макросы, формулы и инструкции оригинала не исполняются. Старый XLS требует закреплённого JDK 21 и проверенного пассивного адаптера; Java ≥24 не заменяет его механизм защиты.

Нет подтверждённого универсального обещания «любой формат и любой объём». Объём разбивается на конечные шаги, ошибки и остатки учитываются. Извлечение текста, чтение моделью и смысловое принятие — разные состояния. Сетевой fetch подписанного SDK имеет отдельный предел 50 000 000 байт; больший местный файл не следует загружать повторно через сетевой обход.

## Итоговая приёмка, обновление и восстановление

Ведите `приёмка.md`: компонент/версия, команда или инструмент, вход, ожидаемый результат, фактический результат, путь квитанции, ограничение. Прежние числа тестов в CURRENT-VERSIONS — история производителя, не новые результаты вашего экземпляра.

1. Запустите основной CLI и все действительно нужные профили. Подтвердите доступ модели, инструменты, работу обязательных контроллеров и отказ защищённого действия при их недоступности.
2. Создайте задачу Beads с дочерними задачами/зависимостью; проверьте blocked → закрытие предшественника → ready. Для UDR должен быть сохранён действительный ID задачи и владельца.
3. В новой ветви Dolt сохраните синтетические before=20/after=30, commit и сумму источника. Прочитайте строку и HEAD повторно; рабочее дерево чистое.
4. Примите оригинал безопасным разбором и реально прочитайте все требуемые единицы. UDR source/read сохраняет точный возвращённый фрагмент и SHA оригинала; большие результаты читаются по `next_offset` до `complete` без подмены предпросмотром.
5. Выполните настоящий G → S → D: три версии изменения x, смещения b или обоих в y=x+b; отдельная синтетическая проверка эталона; передача продуктов; ограниченный вывод. Проверяйте результаты исполнителей, не только статусы SUCCEEDED.
6. Сохраните отчёт в Markdown и повторно прочитайте. Для 20→30 допустимы +10 и +50%; причинность и значимость не следуют из двух чисел. Новый завершённый отчёт должен пройти `finish` по фактической схеме и создать файл; ошибка не закрывает задачу.
7. Штатно остановите исполнение, перезапустите и продолжите тот же UDR ID. Не повторяйте неизвестные действия до проверки эффектов. Сохраняйте план, ссылки, незакрытые вопросы и фактический объём чтения.
8. Проверьте GSD-only при недоступном UDR и UDR-only при недоступном GSD по их собственным контролям. Недоступный модуль не выдаётся за выполненный; обязательная защита работающего модуля не снимается.
9. В Telegram проверьте /whoami, разрешённого владельца, отказ постороннему, содержательный статус, получение и открытие точного файла. Не полагайтесь лишь на ответ API отправки. Большой отчёт передавайте файлом.
10. Выполните резервирование и настоящее восстановление в отдельную папку. Прочитайте известные задачу, commit, источник, заметку, отчёт и запись памяти. До этого состояние — «установлено/проверяется», а не «полностью принято».

Для резервирования: штатно остановите собственных писателей; SQLite копируйте Backup API; Dolt и Beads сохраняйте с историей, правами и конфигурацией; Neo4j Community — остановленный `database dump/load`; Zvec — закрытые коллекции; AgentMemory — завершённые операции, iii и собственные данные; Cognee — оригиналы, SQLite, LanceDB/Ladybug и параметры; Zotero — свою библиотеку, профиль и вложения; Hermes — профиль, сессии, ключи, полный корпус UDR и состояния GSD. Индекс без оригинала не является полным резервом.

Личный резерв шифруется, ключ хранится отдельно. Обезличенная поставка создаётся отдельно с новым подтверждением отсутствия секретов и чужих данных. Публичный Git не хранит личные базы и ключи. Восстанавливайте в новый каталог, не поверх действующего; бинарные базы разных ОС не объявляйте переносимыми без штатного экспорта/импорта и проверки. Neo4j dump и SQLite/Dolt проверяются своей версией.

Для обновления зафиксируйте новую согласованную пару, изменения ядра/адаптеров, зависимости и миграции; испытайте на копии; создайте контрольную точку; переключите только после приёмки. Не выполняйте безусловный `hermes update` или `pip install -U` для всей r8. Откат возвращает согласованные программы и состояние, сохраняя появившиеся после точки данные. Команда отката не должна стирать неизвестные расходы или результаты.

## Диагностика без обхода защиты

| Сообщение | Действие |
|---|---|
| `bn-gsd unavailable` / required controller timed out | Проверить профиль, процесс, манифест и доступ модели; закрыть зависимое действие, сохранить фактические эффекты |
| `Previous provider outcome/usage has not been settled` | Найти незакрытую квитанцию и фактический исход; не переписывать учёт и не повторять вслепую |
| `Unknown command` для существующей команды | Проверить наличие gateway-r5, маршрутизированный профиль и настоящий отказ обработчика |
| context exceeds / compression controller unavailable | Восстановить обязательный контроллер и штатное сжатие; разбить адресные входы, не отрезать обязательное |
| готовый файл отклонён | Проверить разрешённый корень, точный путь, SHA, регистрацию и разрешение выдачи; повторная сборка отчёта не нужна |
| инструмент не найден | Сверить фактическое имя, сервер, фильтры роли/канала, обновление схемы; запрос описаний ≤10 имён |
| Zotero HTTP 412 | Проверить свою библиотеку, явный профиль и Server-ID; не выключать закрепление |
| Beads schema mismatch | Проверить абсолютный исполнитель 1.3.1 и его сумму; не открывать новой базой старый 1.1.0 |
| нет wheel / отказ OS isolation | Зафиксировать несовместимость; сборка/адаптер и отдельная проверка, без скрытого снижения защиты |


## Ограничения и честная фиксация готовности

Различайте: получено → целостность проверена → установлено → настроено → подключено → испытано → восстановление подтверждено. Наличие файла, схемы MCP или успешный вход не подтверждают последующие состояния.

В r8 сохранены незакрытые вопросы: прежняя отметка производственной приёмки UDR `verification_pending_0.2.8`; неполное подтверждение обработки старых корпусов по всем этапам; отдельные пути PDF Cognee/Zotero; отсутствие исчерпывающей проверки согласованности всех хранилищ и восстановления смысловых контрольных точек. Это не доказательство отсутствия функций, но и не основание заявлять полную приёмку.

Проверки поставщика отдельных библиотек на Windows/Linux не являются проверками всей связки Hermes BN + GSD + UDR + общая память на этих системах. Удалённые дополнительные удалённые сервисы и предметные пакеты были заявлены владельцем, но их фактическая конфигурация отсутствовала на машине снимка: не считайте их уже установленными из r8. Для них нужны собственные исходники, подключения и проверка контрактов. Чужие предметные инструкции и личность автоматически не активируются.

## Источники и приоритет документов

1. [Неизменный выпуск r8](https://github.com/olegeklepikov-collab/hermes-bn-gsd-udr-public/releases/tag/public-2026-11-11-gsd-udr-full-r8), `CURRENT-VERSIONS.json`, `CURRENT-SETUP.md`, `MANIFEST.jsonl`, исходники и шаблоны распакованного r8. Они определяют фактическую поставку.
2. Предоставленная прежняя инструкция macOS: редакция 20 октября, parser-r4. Использована как материал сравнения; её двухслойная установка заменена r8.
3. Включённые в r8 `runtime/Hermes UDR/source/docs/setup/README.md`, три исходных документа и `ru/01`–`ru/11`. [Репозиторий UDR](https://github.com/olegeklepikov-collab/hermes-udr) — справка; его подвижная ветка не заменяет закреплённую пару.
4. [Официальная документация Hermes](https://hermes-agent.nousresearch.com/docs/), [нативный Windows](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native). Текущая документация может относиться к другой редакции: команды проверяются по локальному `--help` r8; параметры новых установщиков в старый выпуск не переносятся.
5. [Матрица Zvec](https://zvec.org/en/blog/2026-09-17-zvec-multi-platform/), [uv](https://docs.astral.sh/uv/), [Neo4j](https://neo4j.com/docs/operations-manual/current/installation/), [Zotero](https://www.zotero.org/support/), [R](https://cran.r-project.org/). Поддержка отдельной программы не является поддержкой всей платформы BN.

Состояние ссылок/документов исследовано 11 ноября 2026 года. Точные тарифы, остатки, права аккаунтов и доступность моделей проверяются владельцем на момент подключения. При несовпадении подписанного исходника и местного адаптера сохраняйте оба происхождения, не переписывайте исходную подпись.
