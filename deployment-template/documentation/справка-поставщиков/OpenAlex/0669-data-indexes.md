> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-indexes

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Indexes

An **index** is an external bibliographic index or registry that a work can be listed in — Crossref, PubMed, DataCite, DOAJ, arXiv. Indexes are a [vocabulary](https://help.openalex.org/data/vocabulary/): they're not native, judgment-call IDs, just consistent handles on crisply-existing external lists. A single work can appear in several indexes at once, so each work carries an [`indexed_in`](https://help.openalex.org/data/works/attributes/#indexed_in) list, and a [source](https://help.openalex.org/data/sources/) records which of these indexes cover it. An index's OpenAlex ID looks like `https://openalex.org/indexes/doaj`; fetch one at [`api.openalex.org/indexes/doaj`](https://api.openalex.org/indexes/doaj).

## About

The list is the set of external indexes and registries OpenAlex tracks as sources of works: DOI-registration agencies (Crossref, DataCite), curated indexes (DOAJ, PubMed), and a preprint repository (arXiv). We record which of them lists each work; a work can be in more than one. There are 5 indexes.

Indexes are about works. For lists of *journals* (CWTS Core, DOAJ membership, national lists of health journals and so on), see [Source lists](https://help.openalex.org/data/source-lists/).

## Values

The complete list of all 5 indexes:

| ID | Display name | What it indexes |
|----|--------------|-----------------|
| `crossref` | Crossref | The largest DOI-registration agency: journal articles, books, conference proceedings |
| `pubmed` | PubMed | The National Library of Medicine's biomedical and life-sciences literature |
| `datacite` | DataCite | A DOI-registration agency focused on research data and other non-traditional outputs |
| `doaj` | DOAJ | The Directory of Open Access Journals, a curated index of peer-reviewed OA journals |
| `arxiv` | arXiv | The open-access preprint repository for physics, math, CS, and related fields |

The live list is at [`api.openalex.org/indexes`](https://api.openalex.org/indexes).

## Attributes

The top-level fields on an **index** object. Attributes shared with other entities ([`id`](https://help.openalex.org/data/common-attributes/#id), [`display_name`](https://help.openalex.org/data/common-attributes/#display_name), [`works_count`](https://help.openalex.org/data/common-attributes/#works_count), [`cited_by_count`](https://help.openalex.org/data/common-attributes/#cited_by_count), [`created_date`](https://help.openalex.org/data/common-attributes/#created_date), [`updated_date`](https://help.openalex.org/data/common-attributes/#updated_date)) are documented once on [Common attributes](https://help.openalex.org/data/common-attributes/).

### `id`
*String.* The [OpenAlex ID](https://help.openalex.org/data/#the-openalex-id-scheme) for this index, e.g. `https://openalex.org/indexes/doaj`. See [Common attributes](https://help.openalex.org/data/common-attributes/#id).

### `display_name`
*String.* The index's name, e.g. `DOAJ`. See [Common attributes](https://help.openalex.org/data/common-attributes/#display_name).

### `description`
*String.* A short one-line description of the index and what it covers.

### `works_count`
*Integer.* How many works are listed in this index. See [Common attributes](https://help.openalex.org/data/common-attributes/#works_count).

### `cited_by_count`
*Integer.* Total citations across those works. See [Common attributes](https://help.openalex.org/data/common-attributes/#cited_by_count).

### `works_api_url`
*String.* A ready-made [Works](https://help.openalex.org/data/works/) API URL for every work in this index (`filter=indexed_in:<ID>`).

### `created_date`
*String.* When the index record was added to OpenAlex (`YYYY-MM-DD`). See [Common attributes](https://help.openalex.org/data/common-attributes/#created_date).

### `updated_date`
*String.* When the index record last changed. See [Common attributes](https://help.openalex.org/data/common-attributes/#updated_date).

## In the API

The Indexes endpoint is at [`api.openalex.org/indexes`](https://api.openalex.org/indexes). Fetch one by ID — [`/indexes/doaj`](https://api.openalex.org/indexes/doaj) — or list all five.

Indexes are most useful as a filter on [works](https://help.openalex.org/data/works/): `filter=indexed_in:doaj` returns works listed in DOAJ, `filter=indexed_in:crossref` those with a Crossref record, and `group_by=indexed_in` breaks a result set down by index. On [sources](https://help.openalex.org/data/sources/), the same information appears as which indexes cover the source. See [Filtering](https://help.openalex.org/api/filtering/) for the full syntax and the [endpoints index](https://help.openalex.org/api/endpoints/) for every endpoint.
