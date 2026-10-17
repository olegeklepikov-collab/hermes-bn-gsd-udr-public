> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: search

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

> Query Scite's publication metadata and citation data with Boolean terms and 25+ filters.

Search covers publication metadata (topic, title, author, journal, date) and the content of citation statements, including where in the citing paper each statement occurs. Filters include retraction status, citation type counts, and 25+ other signals, so it works for screening papers as well as finding them.

## Access and licensing

Commercial or research use of Search requires a separate license agreement, it isn't covered by individual plans. [Email sales](mailto:sales@scite.ai) before relying on Search for anything beyond evaluation.

## Basic search

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/search' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'term="machine learning" AND healthcare' \
  --data-urlencode 'limit=5' \
  --data-urlencode 'sort=date' \
  --data-urlencode 'sort_order=desc'
```

`term` supports Boolean operators (`AND`, `OR`, `NOT`) and phrase search (`"exact phrase"`).

## Filtering results

Beyond `term`, the search endpoint accepts filters across three categories:

<Tabs>
  <Tab title="Publication metadata">
    `title`, `abstract`, `author` / `authors`, `journal` / `journals`, `publisher`, `paper_type` / `paper_types`, `affiliation` / `affiliations`, `topic` / `topics`, `date_from`, `date_to`, `doi` / `dois`
  </Tab>

  <Tab title="Citation signals">
    `has_tally`, `has_retraction`, `has_concern`, `has_correction`, `has_erratum`, `has_withdrawn`, `citation_types`, `supporting_from` / `supporting_to`, `mentioning_from` / `mentioning_to`, `contrasting_from` / `contrasting_to`, `citing_publications_from` / `citing_publications_to`
  </Tab>

  <Tab title="Domain-specific">
    `substances` (PubChem canonical name), `mesh_type` (PubMed MeSH descriptor/qualifier), `section` / `sections` (where in the paper the citation occurs)
  </Tab>
</Tabs>

Scope a search to specific publications with `doi` (single) or `dois` (multiple). Combine with `term` to search within those publications only.

## Sorting

Use `sort` to control result order:

| Value | Behavior |
| - | - |
| `relevance` | Default when a `term` is provided |
| `date` | Most recent first (with `sort_order`) |
| `citations` | By citation count |

Combine with `sort_order` (`asc`/`desc`).

## Pagination

Use `limit` (up to 10,000 per request) and `offset` together to page through results.

## Aggregations

Set `compute_aggregations=true` and pass `aggregations` to get facet counts (e.g. by journal or year) alongside your results, useful for building filter UIs without a second round-trip.

<Note>
  Search snippets are always redacted on self-service (Pro plan) API keys. Full snippet access requires an Enterprise agreement. [Contact sales](https://scite.ai/contact).
</Note>

## Response shape

Results come back as `{ count, countIsApproximate, aggregations, hits, suggestedTerm, restrictedCites }`. Each item in `hits` is a full paper object, including a `tally` field with the same shape as the tallies endpoints (локальный ресурс исходного примера не включён) when one has already been computed for that paper (`null` otherwise), so you often don't need a separate tally call for search results you're already displaying.

<Warning>
  Don't use the top-level `restrictedCites` value to decide whether an individual citation snippet is visible. Check `hits[].citations[].snippetHidden`. When `snippetHidden` is `true`, `snippet` is an empty string. Self-service keys don't include citation snippet text.
</Warning>

## Get recommended papers

If you already have a DOI, retrieve related papers without constructing a search query:

```bash theme={null}
curl 'https://api.scite.ai/api_partner/recommend-papers/10.1038/nature12373' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

The response is an array of recommended papers. Each item includes publication metadata, a citation `tally` when available, and a recommendation `score`.

## Related

* Full parameter reference: see **Search** in the API Reference tab for every filter with types and examples
* Recommendation endpoint reference: see **Paper recommendations** in the API Reference tab
* Citations & Tallies (локальный ресурс исходного примера не включён): what `has_tally`, `supporting_from`, etc. actually measure
* Errors and rate limits (локальный ресурс исходного примера не включён): distinguish invalid credentials from missing scopes


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
