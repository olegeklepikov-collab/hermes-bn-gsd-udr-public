> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-subfields

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Subfields

A **subfield** is the third level of OpenAlex's four-level classification hierarchy: 4 [domains](https://help.openalex.org/data/domains/) → 26 [fields](https://help.openalex.org/data/fields/) → 252 subfields → 4,516 [topics](https://help.openalex.org/data/topics/). Subfields are groupings like "Health Informatics," "Geophysics," or "Oncology" — broader than a topic, narrower than a field. Each subfield sits under exactly one field and gathers a set of related topics beneath it. A subfield's OpenAlex ID is a bare number, e.g. `2718`; fetch one at [`api.openalex.org/subfields/2718`](https://api.openalex.org/subfields/2718). Subfields are the level OpenAlex uses to normalize citation impact ([FWCI](https://help.openalex.org/data/works/citations/#field-weighted-citation-impact)) and are one of several [aboutness](https://help.openalex.org/data/aboutness/) signals — see that page to pick the right granularity for your question.

## About

Subfields aren't classified on their own — they're a level of the same hierarchy [topics](https://help.openalex.org/data/topics/) are built from. Each of the ~4,500 topics is mapped to a single subfield using Scopus's [ASJC categories](https://service.elsevier.com/app/answers/detail/a_id/12007/supporthub/scopus/), and a work "belongs to" a subfield through the topics assigned to it. The subfield **labels** are standardized (the 252 ASJC-derived groupings), but a work lands in one only because a machine-learning model inferred its topic from the work's text — which is why subfields, like the rest of the hierarchy, live under [Aboutness](https://help.openalex.org/data/aboutness/) rather than [Vocabulary](https://help.openalex.org/data/vocabulary/). See [Topics → About](https://help.openalex.org/data/topics/#about) for the full assignment pipeline, including the deliberate choice to give every work a single **primary subfield** from its own text (not from its journal).

A work's primary subfield is the subfield of its [`primary_topic`](https://help.openalex.org/data/works/attributes/#primary_topic). To find works in a subfield, filter [Works](https://help.openalex.org/data/works/) by `topics.subfield.id` (any assigned topic's subfield) or `primary_topic.subfield.id` (the primary only). One level up is a [field](https://help.openalex.org/data/fields/); one level down is a set of [topics](https://help.openalex.org/data/topics/).

## Attributes

This is the canonical dictionary of every attribute on a **subfield** object. Attributes shared with other entities ([`id`](https://help.openalex.org/data/common-attributes/#id), [`ids`](https://help.openalex.org/data/common-attributes/#ids), [`display_name`](https://help.openalex.org/data/common-attributes/#display_name), [`works_count`](https://help.openalex.org/data/common-attributes/#works_count), [`cited_by_count`](https://help.openalex.org/data/common-attributes/#cited_by_count), [`created_date`](https://help.openalex.org/data/common-attributes/#created_date), [`updated_date`](https://help.openalex.org/data/common-attributes/#updated_date)) are documented once on [Common attributes](https://help.openalex.org/data/common-attributes/); subfield-specific notes are below.

### `id`
*String.* The [OpenAlex ID](https://help.openalex.org/data/#the-openalex-id-scheme) for this subfield, e.g. `https://openalex.org/subfields/2718`. Subfields use a bare numeric ID (four digits), not the letter-prefixed scheme. See [Common attributes](https://help.openalex.org/data/common-attributes/#id).

### `ids`
*Object.* External identifiers for this subfield, as URIs: `openalex`, plus `wikidata` and `wikipedia` where a matching article exists.

### `display_name`
*String.* The subfield's name, e.g. "Health Informatics." See [Common attributes](https://help.openalex.org/data/common-attributes/#display_name).

### `display_name_alternatives`
*List.* Other names the subfield is known by (e.g. "medical informatics," "clinical informatics" for Health Informatics), for matching and search.

### `description`
*String.* A short description of what the subfield covers.

### `field`
*Object.* The [field](https://help.openalex.org/data/fields/) this subfield belongs to (`id`, `display_name`) — the level directly above it in the hierarchy.

### `domain`
*Object.* The [domain](https://help.openalex.org/data/domains/) this subfield rolls up into (`id`, `display_name`) — the top of the hierarchy.

### `topics`
*List.* The [topics](https://help.openalex.org/data/topics/) that belong to this subfield (`id`, `display_name`) — the level directly below it.

### `siblings`
*List.* The other subfields (`id`, `display_name`), for navigating laterally across the classification.

### `works_count`
*Integer.* How many works fall in this subfield through their primary topic. See [Common attributes](https://help.openalex.org/data/common-attributes/#works_count).

### `cited_by_count`
*Integer.* Total citations across all works in this subfield. See [Common attributes](https://help.openalex.org/data/common-attributes/#cited_by_count).

### `works_api_url`
*String.* A ready-made [Works](https://help.openalex.org/data/works/) API URL for every work in this subfield, e.g. `https://api.openalex.org/works?filter=topics.subfield.id:2718`. A convenience link; work IDs aren't stored on the subfield object.

### `created_date`
*String.* The date this subfield was added to OpenAlex (`YYYY-MM-DD`). See [Common attributes](https://help.openalex.org/data/common-attributes/#created_date).

### `updated_date`
*String.* The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) UTC timestamp of the last change to the subfield object. See [Common attributes](https://help.openalex.org/data/common-attributes/#updated_date).

## In the API

The Subfields endpoint is at [`api.openalex.org/subfields`](https://api.openalex.org/subfields). Fetch a single subfield by ID — [`/subfields/2718`](https://api.openalex.org/subfields/2718) — or a list, and [filter](https://help.openalex.org/api/filtering/), [search](https://help.openalex.org/api/searching/), [sort](https://help.openalex.org/api/sorting/), [group](https://help.openalex.org/api/grouping/), and [page](https://help.openalex.org/api/paging/) over it.

You can filter and group subfields by their place in the hierarchy — `domain.id`, `field.id`, and `topics.id` — and by `works_count`, `cited_by_count`, `id`, and `display_name`, all of which also sort. Full-text matching uses the [`search` parameter](https://help.openalex.org/api/searching/) (the older `display_name.search` filter is deprecated). To find works in a subfield, use the [Works](https://help.openalex.org/data/works/) endpoint: `filter=primary_topic.subfield.id:2718` (primary only) or `filter=topics.subfield.id:2718` (any assigned topic). For the full list of endpoints see the [endpoints index](https://help.openalex.org/api/endpoints/).
