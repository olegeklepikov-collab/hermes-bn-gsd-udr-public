> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: extract--advanced-extract-settings

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Extract Settings

> Advanced configuration for fetch policy, excerpt settings, and full content extraction

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

The `advanced_settings` object on the Extract API lets you tune fetch behavior (cached vs live), excerpt sizing, and full content extraction. Most callers don't need it — the defaults return focused excerpts from the cached index, which works well for the majority of tool-calling and research use cases.

<Note>
  On `/v1/extract`, `fetch_policy`, `excerpt_settings` and `full_content` must be inside `advanced_settings`. Sending the v1beta top-level `excerpts`, `full_content` or `fetch_policy` fields to `/v1/extract` returns a 422. See the migration guide (локальный ресурс исходного примера не включён).
</Note>

## Fields

| Field | Type | Notes | Example |
| - | - | - | - |
| fetch\_policy | object | Controls when to return indexed content (faster) vs fetching live content (fresher). Default is to use cached content from the index. Enabling live fetch significantly increases latency. For more info including field details, see [Fetch Policy](#fetch-policy) below. | `{"max_age_seconds": 3600}` |
| excerpt\_settings | object | Controls excerpt sizes. Provide `max_chars_per_result` for fine-grained control, or omit to use defaults. | `{"max_chars_per_result": 10000}` |
| full\_content | bool or object | Controls full content extraction. Defaults to `false` (disabled). Set to `true` to enable with defaults, or provide a settings object. | `false` or `{"max_chars_per_result": 50000}` |

## Fetch Policy

The `fetch_policy` parameter controls when to return indexed content (faster) or fetch
fresh content from the source (fresher). Fetching fresh content may take up to a minute
and is subject to rate limits to manage the load on source websites.

| Field | Type | Default | Notes |
| - | - | - | - |
| max\_age\_seconds | int | dynamic | Maximum age of indexed content in seconds. If older, fetches live. Minimum 600 (10 minutes). If unspecified, uses dynamic policy based on URL and objective. |
| timeout\_seconds | number | dynamic | Timeout for fetching live content. If unspecified, uses a dynamic timeout based on URL and content type (typically 15s-60s). |
| disable\_cache\_fallback | bool | false | If `true`, returns an error when live fetch fails. If `false`, falls back to older indexed content. |

## Excerpt and Full Content Settings

Both `excerpt_settings` and `full_content` are configured inside the `advanced_settings` object.

**Enable full content with custom excerpt sizes:**

```json wrap theme={"system"}
{
  "urls": ["https://example.com"],
  "advanced_settings": {
    "excerpt_settings": {
      "max_chars_per_result": 5000
    },
    "full_content": {
      "max_chars_per_result": 50000
    }
  }
}
```

**Enable full content with default excerpts:**

```json wrap theme={"system"}
{
  "urls": ["https://example.com"],
  "advanced_settings": {
    "full_content": true
  }
}
```

**Notes:**

* When `full_content` is enabled, you'll receive both excerpts and full content in the response
* Excerpts are always focused on relevance; full content always starts from the beginning
* Without `objective` or `search_queries`, excerpts will be redundant with full content. The request still succeeds, but may return less relevant content and may include a warning.
* `max_chars_total` (top-level) controls total excerpt size but does not affect full content
