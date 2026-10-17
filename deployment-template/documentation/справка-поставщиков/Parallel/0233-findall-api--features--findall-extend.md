> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: findall-api--features--findall-extend

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Extend

> Increase the match limit of existing FindAll runs to get more results without changing query criteria

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

## Overview

Extend allows you to increase the `match_limit` of an existing FindAll run to get more results using the same evaluation criteria—without paying the fixed cost again. Start with a small limit (10-20) to validate your criteria, then extend to get more matches.

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X POST "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/extend" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{ "additional_match_limit": 40 }'
  ```

  ```python Python theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="YOUR_API_KEY")

  client.beta.findall.extend(
      findall_id="findall_40e0ab8c10754be0b7a16477abb38a2f",
      additional_match_limit=40
  )
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from 'parallel-web';

  const client = new Parallel({
    apiKey: ${API_KEY}
  });

  await client.beta.findall.extend(
    "findall_40e0ab8c10754be0b7a16477abb38a2f",
    {
      additional_match_limit: 40
    }
  );
  ```
</CodeGroup>

### How Extend Works

* **Increases match limit:** The `additional_match_limit` you set is the **incremental** number of matches to add (not the total). For example, to go from 10 to 50 matches, set `additional_match_limit: 40`, not `50`.
* **Continues the same evaluation:** The **objective**, **entity type**, **generator**, and **match conditions** stay the same. Existing enrichments continue to run on new matches.
* **Handles run status automatically:**
  * If the run is *active*, it continues seamlessly up to the new match limit.
  * If the run is *completed*, it automatically "respawns" and resumes until reaching the new limit.
* **Pricing:** Extending has **no fixed cost—you only pay for the additional matches beyond the original run**. For example, extending from 10 to 100 matches means paying for 90 additional matches (plus evaluation costs).

### Limitations

* **Preview runs:** Cannot be extended. Use a full generator (`base`, `core`, or `pro`) if you plan to extend.
* **Total limit:** The current `match_limit` plus `additional_match_limit` cannot exceed 1,000.
* **Termination reason:** A completed run can be extended only when `termination_reason` is `match_limit_met`. Runs stopped for low match rate, exhausted candidates, insufficient funds, cancellation, timeout, or error must be replaced with a new run.
* **Fixed parameters:** Extend changes only `match_limit`. Use `/enrich` to add an enrichment; start a new run to change the objective, entity type, generator, match conditions, or an existing enrichment definition.

## Related Topics

* **Preview (локальный ресурс исходного примера не включён)**: Test queries with 5–10 evaluated candidates before running full searches
* **Generators and Pricing (локальный ресурс исходного примера не включён)**: Understand generator options and pricing
* **Enrichments (локальный ресурс исходного примера не включён)**: Extract additional structured data for matched candidates
* **Streaming Events (локальный ресурс исходного примера не включён)**: Receive real-time updates via Server-Sent Events
* **Webhooks (локальный ресурс исходного примера не включён)**: Configure HTTP callbacks for run completion and matches
* **Run Lifecycle (локальный ресурс исходного примера не включён)**: Understand run statuses and how to cancel runs
* **API Reference (локальный ресурс исходного примера не включён)**: Complete endpoint documentation
