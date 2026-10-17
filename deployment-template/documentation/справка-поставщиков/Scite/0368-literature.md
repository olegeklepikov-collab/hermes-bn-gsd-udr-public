> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: literature

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Literature tools

> Search the scientific literature, read full-text excerpts, and retrieve Smart Citations through MCP.

`search_literature` is the core Scite MCP tool. One tool covers three jobs: finding papers, reading inside them, and pulling the Smart Citation statements that cite them.

Requires a Scite premium subscription.

## What it returns

Every hit carries the paper's identity plus the evidence attached to it.

| Field | Contents |
| - | - |
| `doi`, `title`, `authors`, `abstract`, `journal`, `year`, `volume`, `issue`, `page` | Paper metadata; `authors` returns the first three |
| `fulltextExcerpts` | Up to 5 passages (\~500 characters each) from the paper matching your query, open access only |
| `citations` | Smart Citation statements, each with `snippet`, `type`, `section`, `sourceDoi`, `targetDoi` |
| `tally` | Citation metrics: `total`, `supporting`, `contrasting`, `mentioning`, `citingPublications` |
| `editorialNotices` | Retractions, corrections, concerns, and errata, each with `status`, `noticeDoi`, `date` |
| `access` | Resolved access link with `url`, `accessType` (open, institutional, purchase), `contentType`, and pricing |
| `isOa`, `oaStatus`, `license` | Open access status |

A `type` of `unclassified` means the citation statement exists but the classifier hasn't assigned it a category. It isn't a fourth citation category — see Citation model (локальный ресурс исходного примера не включён).

## Three ways to call it

### Search for papers

Pass `term` with domain-specific vocabulary. The index spans every academic field, so broad phrases return noise.

```json theme={null}
{
  "name": "search_literature",
  "arguments": {
    "term": "\"PAC learning\" AND \"generalization bounds\"",
    "limit": 10,
    "supporting_from": 5
  }
}
```

### Fetch metadata for known papers

Pass `dois` (preferred) or `titles` **without** a `term`. No search runs; you get the records back.

```json theme={null}
{
  "name": "search_literature",
  "arguments": {
    "dois": ["10.1038/s41586-020-2649-2"]
  }
}
```

### Read inside a specific paper

Pass `dois` **with** a `term`. Each call returns up to 5 matching excerpts, so vary the term across calls to walk through a paper section by section.

```json theme={null}
{
  "name": "search_literature",
  "arguments": {
    "dois": ["10.1038/s41586-020-2649-2"],
    "term": "limitations OR confounding"
  }
}
```

If `fulltextExcerpts` comes back empty, the full text either isn't indexed or your terms didn't match. Use the `access` field to reach the PDF instead.

## Query syntax

`term` searches across title, abstract, and full text, and supports:

* Boolean operators: `AND`, `OR`, `NOT`
* Phrase search: `"exact phrase"`
* Proximity: `"term1 term2"~5`

## Parameters

Calling `search_literature` with no arguments browses the whole corpus, relevance-sorted. That's allowed but rarely useful — pass at least a `term`, `dois`, or `titles`.

### Query and pagination

| Parameter | Type | Description |
| - | - | - |
| `term` | string | Cross-field query. Optional when `dois` or `titles` is given |
| `dois` | string\[] | Restrict to specific DOIs. Exact match, so prefer this over `titles` |
| `titles` | string\[] | Restrict to papers matching these titles. Use when DOIs aren't available |
| `limit` | integer | Results per call. Default `10`, maximum `1000` |
| `offset` | integer | Pagination offset. Default `0` |

<Warning>
  Keep `limit` small. Every hit can carry excerpts and citation statements, so large limits produce payloads that consume a lot of model context. Use `10`–`50` with `offset` to page.
</Warning>

### Metadata filters

| Parameter | Type | Description |
| - | - | - |
| `title` | string | Text in the publication title |
| `abstract` | string | Text in the abstract |
| `author` | string | Author name; partial names work |
| `affiliation` | string | Author institutional affiliation |
| `journal` | string | Journal name |
| `publisher` | string | Publisher name |
| `topic` | string | Research topic or subject area |
| `paper_type` | string | Publication type, e.g. `Article`, `Review`, `Meta-Analysis` |
| `year` | integer | Exact publication year. Can't be combined with `date_from`/`date_to` |
| `date_from` | string | Published on or after. `YYYY` or `YYYY-MM-DD` |
| `date_to` | string | Published on or before. `YYYY` or `YYYY-MM-DD` |
| `collection_slug` | string | Restrict the search to one of your Collections (локальный ресурс исходного примера не включён) |

### Citation filters

Each filter is a range bound. `tally` counts citation *statements*; `citingPublications` counts distinct *publications*.

| Parameter | Type | Description |
| - | - | - |
| `supporting_from` / `supporting_to` | integer | Bounds on supporting Smart Citations |
| `contrasting_from` / `contrasting_to` | integer | Bounds on contradicting Smart Citations |
| `mentioning_from` / `mentioning_to` | integer | Bounds on mentioning Smart Citations |
| `citing_publications_from` / `citing_publications_to` | integer | Bounds on total citing publications |
| `has_tally` | boolean | Only papers with at least one Smart Citation |

<Note>
  The API field is `contrasting`, matching the parameter names above. Scite's interface labels the same category "contrasted." Both refer to contradicting citation statements.
</Note>

### Editorial filters

| Parameter | Type | Description |
| - | - | - |
| `has_retraction` | boolean | Only retracted papers |
| `has_concern` | boolean | Only papers with editorial concerns |
| `has_correction` | boolean | Only papers with published corrections |
| `has_erratum` | boolean | Only papers with published errata |

Check `editorialNotices` on every paper before citing it, even when you haven't filtered on these. A paper can be accurate and still be withdrawn.

## Reading a paper efficiently

The token-efficient pattern is search once, then read incrementally.

<Steps>
  <Step title="Find the paper">
    Search with a narrow `term` and a small `limit` to get candidate DOIs.
  </Step>

  <Step title="Confirm it">
    Call again with `dois` and no `term` to pull metadata, `tally`, and `editorialNotices`.
  </Step>

  <Step title="Read sections">
    Call repeatedly with the same `dois` and different `term` values — methods, results, limitations — collecting 5 excerpts per call.
  </Step>

  <Step title="Follow the citations">
    Read the `citations` array for what other papers say about it, quoting `snippet` text as evidence.
  </Step>
</Steps>

## Related

* Search guide (локальный ресурс исходного примера не включён): the same corpus and filters over HTTP
* Smart Citations guide (локальный ресурс исходного примера не включён): how citation statements are classified
* Prompts (локальный ресурс исходного примера не включён): prebuilt literature review, fact-check, and screening workflows


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
