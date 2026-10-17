> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: overview

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Search patents, grants, clinical trials, and regulatory records alongside citation data.

The Evidence API searches non-citation research and regulatory records: patents, grants, clinical trials, FDA device/drug records, and adverse-event and safety-alert databases, sourced from Resolute's evidence datasets. Every dataset follows the **same four-endpoint pattern**, so once you've used one, you've used them all.

<Warning>
  Evidence isn't included in a standard self-service Pro key. Each dataset requires its own scope (`evidence:patents:api`, `evidence:grants:api`, `evidence:clinical-trials:api`, and equivalents for the other datasets). [Email sales](mailto:sales@scite.ai) to get a dataset scope added to your account, then generate a new key from the [API Console](https://scite.ai/users/me/api) so it picks up the scope.
</Warning>

## The pattern

For a resource `{resource}` (e.g. `patents`):

| Endpoint | Purpose |
| - | - |
| `GET /api_partner/evidence/{resource}` | Search |
| `GET /api_partner/evidence/{resource}/schema` | Get the filterable fields and their types for this resource |
| `POST /api_partner/evidence/{resource}/facets` | Get facet counts (e.g. how many results per year) without fetching full results |
| `GET /api_partner/evidence/{resource}/{id}` | Get a single record by its ID |

Search takes two parameters, and they work differently than the Search API (локальный ресурс исходного примера не включён):

* **`q`**: free-text query. Supports `AND`, `OR`, `NOT`, and phrase matching with double quotes: `q=CRISPR`, `q="gene therapy" AND cancer`.
* **`f`**: field filters, space-delimited, in `field:"value"` format (values must be double-quoted). Call the resource's `schema` endpoint to see which fields are filterable.

```bash theme={null}
curl 'https://api.scite.ai/api_partner/evidence/patents/schema' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/patents' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q=CRISPR' \
  --data-urlencode 'f=patents.assignees.name:"Acme Corp" patents.filingStatus:"grant"'
```

Date range filters use `gte`/`lt` suffixes with no space before the suffix: `f=dates.startDategte:"2024-01-01" dates.startDatelt:"2025-01-01"`. ISO dates, epoch milliseconds, and timezone offsets are all accepted; dates without a timezone are treated as UTC.

Sorting uses `s` (default `_relevance`; each dataset page lists its sortable fields) and `sortDir`, not the `sort`/`sort_order` names from Search. Pagination uses `p` (page number), not `limit`/`offset`.

Every search response has the same envelope: `{ totalResults, delay, resultsPerPage, from, results }`. Only the shape of each item in `results` differs per dataset.

<Warning>
  Some fields in search and detail responses are either a plain string or an object shaped like `{"id": "...", "name": "...", "highlighted": "..."}`, depending on the query. Handle both, e.g. `value.id ?? value.name ?? value`.
</Warning>

## Datasets

<CardGroup cols={2}>
  <Card title="Patents" icon="file-certificate" href="/guides/evidence/patents">
    Patent filings with family, citation, assignee, and legal-event data.
  </Card>

  <Card title="Clinical Trials" icon="stethoscope" href="/guides/evidence/clinical-trials">
    Registered trials with phase, status, sponsors, interventions, and linked publications.
  </Card>

  <Card title="Grants" icon="hand-holding-dollar" href="/guides/evidence/grants">
    Research grant awards from NIH RePORTER, NSF, and other funders.
  </Card>

  <Card title="Drugs" icon="pills" href="/guides/evidence/drugs">
    FDA drug labels, Orange Book listings, and Drugs\@FDA application records.
  </Card>

  <Card title="Device Clearances" icon="microchip" href="/guides/evidence/devices">
    FDA 510(k) clearance decisions and their summary PDFs.
  </Card>

  <Card title="Adverse Events" icon="triangle-exclamation" href="/guides/evidence/adverse-events">
    FDA MAUDE (device) and FAERS (drug) adverse-event reports.
  </Card>

  <Card title="Safety Alerts" icon="bell-exclamation" href="/guides/evidence/safety-alerts">
    UK MHRA safety alerts, including full alert document content.
  </Card>
</CardGroup>

## Related

* Search guide (локальный ресурс исходного примера не включён): the equivalent search over publications, with a different query syntax than Evidence
* Full parameter reference: see **Evidence** in the API Reference tab; per-resource filters are best discovered via each resource's `/schema` endpoint
* Errors and rate limits (локальный ресурс исходного примера не включён): troubleshoot missing dataset scopes and retryable failures


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
