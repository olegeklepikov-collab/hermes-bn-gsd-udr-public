# Программный доступ

Оболочка: `__HERMES_BN_ROOT__/bin/keenable-bn`.

```bash
keenable-bn search --input search.json --output search-result.json
keenable-bn fetch --input fetch.json --output page.json
keenable-bn identity --output identity.json
keenable-bn batch-local --input batch.json --output results.json
keenable-bn mcp --server web --tool search_web_pages --input mcp-search.json --output result.json
keenable-bn mcp --server select --tool select --input select.json --output table.json
keenable-bn mcp --server select --output select-schema.json
keenable-bn official-cli -- search "official documentation for Keenable web search" --max-results 3
keenable-bn official-cli -- fetch https://docs.keenable.ai/credits --live
```

Файлы параметров — JSON; --input - читает стандартный ввод. --output сохраняет полный ответ с правами 600. Ключ автоматически загружается из собственного профиля; передавать его в аргументах не требуется. official-cli передаёт ключ через среду и использует отдельный KEENABLE_HOME на AgentRuntime2. Оболочка допускает только search/fetch и справку: настройка чужих клиентов и управление ключами остаются отдельной административной задачей.

REST search принимает query, mode, site, acquired_after/before, published_after/before, query_time, snippet_max_length, max_results, экспериментальное enableWizards. REST fetch принимает url, max_chars, live, prompt. Действующая схема сохранена в `Keenable/источники/api-schema.json`; неизвестные параметры отклоняются локально. identity возвращает личные сведения аккаунта: проверяй их в закрытом файле, не включай в отчёт без необходимости.

batch-local — последовательный местный пакет 1–50 search/fetch с уникальными customId. Это не отдельный пакетный API Keenable. При 429 пакет останавливается; has_errors и complete позволяют обнаружить неполный результат. Проверь статус каждого запроса.

MCP имеет дополнительные output_format и неперсональный session_id. Оболочка читает актуальную схему сервера до вызова. Метаданные задаются через --meta файл.json, например:

```json
{"keenable/overrides":{"mode":"realtime","skip_cache":true}}
```

Основное MCP-подключение удалённое HTTP. Альтернатива для клиентов без него — официальный пакет Node @keenable/mcp-server 0.2.1; в Hermes BN дополнительный мост не требуется. Нативный поставщик Hermes Keenable поддерживает простой поиск и чтение, но полные настройки открываются через MCP или REST.

Официальная программа Keenable 0.2.3 установлена из релиза GitHub с проверкой SHA256. Общий `configure-mcp --all` не применялся: он меняет другие клиенты, тогда как здесь настраивается отдельный Hermes BN.

Варианты авторизации: собственный API key для поиска/чтения/SELECT; бесплатные публичные Search/Fetch без ключа; браузерный OAuth для совместимых MCP-клиентов и программы. Платежи x402 в USDC/Base — отдельная платная возможность, не выбранная для этого экземпляра. LangChain, LlamaIndex, Haystack, Mastra, Vercel AI SDK, NVIDIA NeMo, Convex, n8n, Dify и другие опубликованные обёртки нужны при разработке соответствующего приложения; для текущего Hermes они не добавляют собственных исследовательских функций.
