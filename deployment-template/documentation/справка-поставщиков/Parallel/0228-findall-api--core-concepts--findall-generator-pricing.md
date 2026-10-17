> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: findall-api--core-concepts--findall-generator-pricing

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generators

> Choose the right FindAll generator (preview, base, core, pro) based on query complexity and expected match volume

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

FindAll offers different generators that determine the quality and thoroughness of FindAll run results. See Pricing (локальный ресурс исходного примера не включён) for generator costs and all API rates.

## Generators

| Generator | Best For | Candidate Pool | Expected Match Rate |
| - | - | - | - |
| `preview` | Testing queries before committing to a full run | 5–10 candidates evaluated | Varies — use to validate schema |
| `base` | Broad, common queries where you expect many matches | Moderate pool | Higher (broad criteria match more candidates) |
| `core` | Specific queries with moderate expected matches | Large pool | Moderate (balanced breadth and depth) |
| `pro` | Highly specific queries with rare or hard-to-find matches | Largest pool | Lower per candidate (thorough search for rare matches) |

<Note>
  **Candidate pool size matters**: Each generator evaluates a different number of candidates. `preview` evaluates the requested 5–10 candidates, while `pro` searches the most thoroughly. If you're getting 0 matches, try upgrading to a stronger generator before modifying your query — the issue may be pool size, not query quality.
</Note>

## How to Choose

### 1. Start with Preview

Always test your query with `preview` first to validate your approach and get a sense of how many matches to expect. See Preview (локальный ресурс исходного примера не включён).

### 2. Choosing the Right Generator

Based on your preview results and query characteristics:

**Choose `base` when:**

* You expect many matches (e.g., "companies in healthcare")
* Your query has broad criteria that are common
* You're searching for fewer than 20 matches where the low fixed cost matters most

**Choose `core` when:**

* You expect a moderate number of matches (e.g., "healthcare companies using AI for diagnostics")
* Your query is fairly specific but not extremely rare
* You need between 20-50 matches

**Choose `pro` when:**

* You expect few matches or very specific criteria (e.g., "Series A healthcare AI companies with FDA-approved products")
* Your query requires the most thorough and comprehensive search
* The higher per-match cost is acceptable for your use case

**Note:** For match counts above 50, the per-match cost becomes more significant than the fixed cost in your total bill. When using enrichments, consider that enrichment costs also scale with the number of matches.

## Enrichments

When adding enrichments (локальный ресурс исходного примера не включён) to extract additional data from your matches, each enrichment adds its own per-match cost based on the Task API processor (локальный ресурс исходного примера не включён) you choose. Since enrichments run on every match and you can add multiple enrichments, they can significantly impact your total costs for high-match queries. Choose enrichment processors based on the complexity of data extraction needed.

## Additional Notes

* **Extend Runs (локальный ресурс исходного примера не включён)**: Fixed cost is not charged again, only per-match costs for new matches. If enrichments are present, they also run on new matches at the same enrichment processor cost.
* **Enrichments (локальный ресурс исходного примера не включён)**: Enrichments are charged based on Task API processor pricing × number of matches. You can add multiple enrichments using different processors, and each enrichment's cost is calculated separately.
* **Run Lifecycle (локальный ресурс исходного примера не включён)**: You're charged for work completed before cancellation, including any enrichments that finished.

**Tip:** If a run terminates early, consider using a more advanced generator (like `pro` instead of `base`) or refining your query criteria to be more achievable.

## Related Topics

* **Pricing (локальный ресурс исходного примера не включён)**: Consolidated pricing for all Parallel APIs
* **Preview (локальный ресурс исходного примера не включён)**: Test queries with 5–10 evaluated candidates before running full searches
* **Enrichments (локальный ресурс исходного примера не включён)**: Extract additional structured data for matched candidates
* **Task API Processors (локальный ресурс исходного примера не включён)**: Understand processor options for enrichments
* **Extend Runs (локальный ресурс исходного примера не включён)**: Increase match limits without paying new fixed costs
* **Streaming Events (локальный ресурс исходного примера не включён)**: Receive real-time updates via Server-Sent Events
* **Webhooks (локальный ресурс исходного примера не включён)**: Configure HTTP callbacks for run completion and matches
* **Run Lifecycle (локальный ресурс исходного примера не включён)**: Understand run statuses and how to cancel runs
* **API Reference (локальный ресурс исходного примера не включён)**: Complete endpoint documentation
