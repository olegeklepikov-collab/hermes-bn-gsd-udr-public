> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: findall-api--features--findall-cancel

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel

> Stop FindAll runs early to control costs

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

Stop a running FindAll search when you have enough matches or need to control costs. Results found before cancellation are preserved.

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X POST \
    https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/cancel \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H "Content-Type: application/json"
  ```

  ```python Python theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="YOUR_API_KEY")

  client.beta.findall.cancel(
      findall_id="findall_40e0ab8c10754be0b7a16477abb38a2f"
  )
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from 'parallel-web';

  const client = new Parallel({
    apiKey: ${API_KEY},
  });

  await client.beta.findall.cancel("findall_40e0ab8c10754be0b7a16477abb38a2f");
  ```
</CodeGroup>

## How Cancellation Works

The cancel endpoint marks the run `cancelled` and returns `204 No Content`. The orchestrator then detects that terminal state and stops scheduling more work:

* Work already in flight may finish before orchestration shuts down
* Candidates already persisted remain accessible through `/result`
* Cancellation does not reverse charges for work that already completed
* Current FindAll runs move directly to `cancelled`; they do not emit an intermediate `cancelling` status (see **Run Lifecycle (локальный ресурс исходного примера не включён)**)

<Warning>
  Cancelled runs **cannot be extended**. Results found before cancellation remain available. Adding an enrichment to a terminal run requeues it, so create a new run instead if you want an independent search.
</Warning>

## Common Use Cases

* Control costs when a run takes longer than expected
* Stop after finding enough matches (monitor via webhooks (локальный ресурс исходного примера не включён) or SSE (локальный ресурс исходного примера не включён))
* Iterate quickly with refined queries instead of waiting for completion

## Related Topics

* **Generators and Pricing (локальный ресурс исходного примера не включён)**: Understand generator options and pricing
* **Preview (локальный ресурс исходного примера не включён)**: Test queries with 5–10 evaluated candidates before running full searches
* **Enrichments (локальный ресурс исходного примера не включён)**: Extract additional structured data for matched candidates
* **Extend Runs (локальный ресурс исходного примера не включён)**: Increase match limits without paying new fixed costs
* **Streaming Events (локальный ресурс исходного примера не включён)**: Receive real-time updates via Server-Sent Events
* **Webhooks (локальный ресурс исходного примера не включён)**: Configure HTTP callbacks for run completion and matches
* **API Reference (локальный ресурс исходного примера не включён)**: Complete endpoint documentation
