> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: api-endpoints

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

Every OpenAlex entity has a REST endpoint under `https://api.openalex.org/`. They all work the same way: request the plural path for a **list** (filter, search, sort, group, page), or add an ID for a **single** entity. The query mechanics are the same across every endpoint — see [Filtering](https://help.openalex.org/api/filtering/), [Searching](https://help.openalex.org/api/searching/), [Sorting](https://help.openalex.org/api/sorting/), [Grouping](https://help.openalex.org/api/grouping/), [Paging](https://help.openalex.org/api/paging/), and [Selecting fields](https://help.openalex.org/api/selecting-fields/).

This page is the index. What each entity *is*, and what every field on it *means*, lives on its [Entities](https://help.openalex.org/data/) page — follow the links.

## Entity endpoints

| Endpoint | List / single | What it returns |
|---|---|---|
| `/works` | `/works` · `/works/W…` | [Works](https://help.openalex.org/data/works/) — scholarly documents |
| `/authors` | `/authors` · `/authors/A…` | [Authors](https://help.openalex.org/data/authors/) — the people who create works |
| `/sources` | `/sources` · `/sources/S…` | [Sources](https://help.openalex.org/data/sources/) — journals, conferences, repositories |
| `/institutions` | `/institutions` · `/institutions/I…` | [Institutions](https://help.openalex.org/data/institutions/) — universities, companies, and more |
| `/publishers` | `/publishers` · `/publishers/P…` | [Publishers](https://help.openalex.org/data/publishers/) — the organizations behind sources |
| `/funders` | `/funders` · `/funders/F…` | [Funders](https://help.openalex.org/data/funders/) — research funders |
| `/awards` | `/awards` · `/awards/G…` | [Awards](https://help.openalex.org/data/awards/) — specific grants |

## Component endpoints

[Component](https://help.openalex.org/data/component/) entities are parts of a work. They have no minted OpenAlex ID, but two of them have their own list endpoints; locations are addressed by a namespaced id (`doi:…`, `pmh:…`, `pmid:…`, `mag:…`) rather than a letter-prefixed one.

| Endpoint | List / single | What it returns |
|---|---|---|
| `/locations` | `/locations` · `/locations/doi:…` | [Locations](https://help.openalex.org/data/locations/) — every harvested copy of a work, one row per copy |
| `/raw-affiliation-strings` | `/raw-affiliation-strings` | [Raw affiliation strings](https://help.openalex.org/data/raw-affiliation-strings/) — distinct affiliation strings as printed |

## Aboutness endpoints

| Endpoint | What it returns |
|---|---|
| `/topics` | [Topics](https://help.openalex.org/data/topics/) — ~4,500 fine-grained subjects |
| `/subfields` | [Subfields](https://help.openalex.org/data/subfields/) — 252 mid-level subjects |
| `/fields` | [Fields](https://help.openalex.org/data/fields/) — 26 broad disciplines |
| `/domains` | [Domains](https://help.openalex.org/data/domains/) — the 4 top-level branches |
| `/keywords` | [Keywords](https://help.openalex.org/data/keywords/) — short topic-derived phrases |
| `/sdgs` | [SDGs](https://help.openalex.org/data/sdgs/) — the 17 UN Sustainable Development Goals |
| `/study-designs` | [Study designs](https://help.openalex.org/data/study-designs/): the 7 designs a work's research can have (randomized controlled trial, systematic review, …) |
| `/concepts` | [Concepts](https://help.openalex.org/data/concepts/) *(deprecated — use Topics)* |

## Vocabulary endpoints

| Endpoint | What it returns |
|---|---|
| `/work-types` | [Work types](https://help.openalex.org/data/work-types/) |
| `/source-types` | [Source types](https://help.openalex.org/data/source-types/) |
| `/institution-types` | [Institution types](https://help.openalex.org/data/institution-types/) |
| `/countries` | [Countries](https://help.openalex.org/data/countries/) |
| `/continents` | [Continents](https://help.openalex.org/data/continents/) |
| `/languages` | [Languages](https://help.openalex.org/data/languages/) |
| `/licenses` | [Licenses](https://help.openalex.org/data/licenses/) |
| `/indexes` | [Indexes](https://help.openalex.org/data/indexes/) |
| `/source-lists` | [Source lists](https://help.openalex.org/data/source-lists/) |

## Special-purpose endpoints

| Endpoint | What it does |
|---|---|
| `/autocomplete/{entity}` | Fast type-ahead suggestions — see [Autocomplete](https://help.openalex.org/api/autocomplete/) |
| `/text` | Tag arbitrary text with topics and keywords — see [Tag Aboutness](https://help.openalex.org/api/tag-aboutness/) |
| `/collections` | [Collections](https://help.openalex.org/data/collections/): list the public ones (no key) and your own (filter, search, sort, group), create, read, share and change them and their members (no credits) — see [Collections API](https://help.openalex.org/api/collections/) |
| `/curations` | Submit corrections *(on `user.openalex.org`)* — see [Author curation](https://help.openalex.org/api/author-curation/) and [Curations](https://help.openalex.org/data/curations/) |
| `/saved-searches` | Save searches and set email alerts for new works (no credits) — see [Alerts and saved searches](https://help.openalex.org/api/alerts/) |

## OQL and OQO

Beyond REST, OpenAlex answers the same queries through [OQL](https://help.openalex.org/access/oql/) (a readable query language) and its machine-readable twin [OQO](https://help.openalex.org/access/oqo-schema/). Every query surface — REST, OQL, the web builder — transpiles to the same OQO under the hood; see [Querying](https://help.openalex.org/access/querying/).
