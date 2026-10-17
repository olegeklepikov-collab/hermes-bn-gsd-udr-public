> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: search--advanced-search-settings

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Search Settings

> Advanced configuration for source policy, fetch policy, excerpt settings, location, and result count

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

The `advanced_settings` object on the Search API lets you tune source selection, freshness, excerpt sizing, geo-targeting, and result count. Most callers don't need it — the defaults are chosen to produce the best results for typical requests, and setting these knobs unnecessarily can hurt quality or latency.

## Fields

| Field | Type | Notes | Example |
| - | - | - | - |
| source\_policy | SourcePolicy (локальный ресурс исходного примера не включён) | Controls your sources: include/exclude domains or domain/path prefixes and optionally set a start date for freshness control via `after_date`. Path prefixes are not supported in `turbo` mode. Can significantly reduce result quality by excluding relevant pages — use only when absolutely necessary. See Using include\_domains](#using-include_domains) below. | [Source policy example (локальный ресурс исходного примера не включён) |
| fetch\_policy | object | Controls when to return indexed content (faster) vs fetching live content (fresher). Default is to use cached content from the index. Enabling live fetch significantly increases latency. For more info including field details, see Fetch Policy (локальный ресурс исходного примера не включён). | `{"max_age_seconds": 3600}` |
| excerpt\_settings | object | Controls excerpt sizes. Provide `max_chars_per_result` for fine-grained control, or omit to use defaults. | `{"max_chars_per_result": 10000}` |
| location | string | ISO 3166-1 alpha-2 country code for geo-targeted search results. See [Supported locations](#supported-locations) for the complete list. | `"us"`, `"gb"`, `"de"`, `"jp"` |
| max\_results | int | Upper bound on the number of results to return. Must be greater than 0 and defaults to 10. Public Search modes currently cap results at 20; higher requested values are reduced to 20 with an input validation warning. The API may return fewer results. | 10 |

## Supported locations

Set `advanced_settings.location` to one of the following ISO 3166-1 alpha-2 country codes. Codes are case-insensitive and normalized to lowercase.

| Country | Code |
| - | - |
| Argentina | `ar` |
| Australia | `au` |
| Austria | `at` |
| Belgium | `be` |
| Brazil | `br` |
| Canada | `ca` |
| Chile | `cl` |
| China | `cn` |
| Denmark | `dk` |
| Finland | `fi` |
| France | `fr` |
| Germany | `de` |
| Greece | `gr` |
| Hong Kong | `hk` |
| India | `in` |
| Indonesia | `id` |
| Italy | `it` |
| Japan | `jp` |
| Malaysia | `my` |
| Mexico | `mx` |
| Netherlands | `nl` |
| New Zealand | `nz` |
| Norway | `no` |
| Philippines | `ph` |
| Poland | `pl` |
| Portugal | `pt` |
| Russia | `ru` |
| Saudi Arabia | `sa` |
| South Africa | `za` |
| South Korea | `kr` |
| Spain | `es` |
| Sweden | `se` |
| Switzerland | `ch` |
| Taiwan | `tw` |
| Turkey | `tr` |
| United Kingdom | `gb` |
| United States | `us` |

For example:

```json theme={"system"}
{
  "search_queries": ["latest electric vehicle incentives"],
  "advanced_settings": {
    "location": "gb"
  }
}
```

<Note>
  Use `"gb"` for the United Kingdom, not `"uk"`. Invalid or unsupported values are ignored, and the response includes an input validation warning.
</Note>

## Using include\_domains

<Warning>
  Source policies can significantly reduce result quality by excluding relevant pages from retrieval. Use `include_domains` and `exclude_domains` only when absolutely necessary — for compliance-bound corpora, tasks that require a single known publisher or section of a site, or when specific sources must be blocked.
</Warning>

`include_domains` (локальный ресурс исходного примера не включён) restricts retrieval so that **only** matching domains or domain/path prefixes can appear in results—the rest of the web is not searched. Treat it as a hard allow list, not a soft preference.

**Best practice:** Set `include_domains` only when answers must come **exclusively** from those domains or paths (for example, internal or compliance-bound corpora, or when the task truly requires a single known publisher). If the model or user might still need the open web, avoid `include_domains` and instead steer sources in the **`objective`** (e.g. "prefer official documentation") or use **`exclude_domains`** when you only need to block specific sites or paths. Full parameter details: Source policy (локальный ресурс исходного примера не включён).
