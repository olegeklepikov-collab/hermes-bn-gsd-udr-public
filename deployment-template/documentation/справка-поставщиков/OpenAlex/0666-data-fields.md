> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-fields

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Fields

A **field** is the second level of OpenAlex's four-level classification hierarchy: 4 [domains](https://help.openalex.org/data/domains/) → 26 fields → 252 [subfields](https://help.openalex.org/data/subfields/) → 4,516 [topics](https://help.openalex.org/data/topics/). The 26 fields are broad disciplines — "Medicine," "Computer Science," "Arts and Humanities," "Physics and Astronomy," and so on — each sitting under one of the four domains and gathering a set of subfields beneath it. A field's OpenAlex ID is a bare number, e.g. `27` for Medicine; fetch one at [`api.openalex.org/fields/27`](https://api.openalex.org/fields/27). Fields are one of several [aboutness](https://help.openalex.org/data/aboutness/) signals — high familiarity, coarse granularity — see that page to choose the right level for your question.

## About

Fields aren't classified on their own — they're a level of the same hierarchy [topics](https://help.openalex.org/data/topics/) are built from. Each of the ~4,500 topics maps up through a [subfield](https://help.openalex.org/data/subfields/) to one of the 26 fields, following Scopus's [ASJC categories](https://service.elsevier.com/app/answers/detail/a_id/12007/supporthub/scopus/), and a work "belongs to" a field through the topics assigned to it. The 26 field **labels** are standardized, but a work lands in one only because a machine-learning model inferred its topic from the work's text — which is why fields, like the rest of the hierarchy, live under [Aboutness](https://help.openalex.org/data/aboutness/) rather than [Vocabulary](https://help.openalex.org/data/vocabulary/). See [Topics → About](https://help.openalex.org/data/topics/#about) for the full pipeline.

A work's primary field is the field of its [`primary_topic`](https://help.openalex.org/data/works/attributes/#primary_topic). To find works in a field, filter [Works](https://help.openalex.org/data/works/) by `topics.field.id` (any assigned topic's field) or `primary_topic.field.id` (the primary only). One level up is a [domain](https://help.openalex.org/data/domains/); one level down is a set of [subfields](https://help.openalex.org/data/subfields/).

## Attributes

This is the canonical dictionary of every attribute on a **field** object. (Confusingly, "field" is both the entity and the generic word for an object's properties; the properties are dictionaried below.) Attributes shared with other entities ([`id`](https://help.openalex.org/data/common-attributes/#id), [`ids`](https://help.openalex.org/data/common-attributes/#ids), [`display_name`](https://help.openalex.org/data/common-attributes/#display_name), [`works_count`](https://help.openalex.org/data/common-attributes/#works_count), [`cited_by_count`](https://help.openalex.org/data/common-attributes/#cited_by_count), [`created_date`](https://help.openalex.org/data/common-attributes/#created_date), [`updated_date`](https://help.openalex.org/data/common-attributes/#updated_date)) are documented once on [Common attributes](https://help.openalex.org/data/common-attributes/); field-specific notes are below.

### `id`
*String.* The [OpenAlex ID](https://help.openalex.org/data/#the-openalex-id-scheme) for this field, e.g. `https://openalex.org/fields/27`. Fields use a bare numeric ID (two digits, 11–36), not the letter-prefixed scheme. See [Common attributes](https://help.openalex.org/data/common-attributes/#id).

### `ids`
*Object.* External identifiers for this field, as URIs: `openalex`, plus `wikidata` and `wikipedia` where a matching article exists.

### `display_name`
*String.* The field's name, e.g. "Medicine." See [Common attributes](https://help.openalex.org/data/common-attributes/#display_name).

### `display_name_alternatives`
*List.* Other names the field is known by (e.g. "healthcare sciences" for Medicine), for matching and search.

### `description`
*String.* A short description of what the field covers.

### `domain`
*Object.* The [domain](https://help.openalex.org/data/domains/) this field belongs to (`id`, `display_name`) — the level directly above it in the hierarchy.

### `subfields`
*List.* The [subfields](https://help.openalex.org/data/subfields/) that belong to this field (`id`, `display_name`) — the level directly below it.

### `siblings`
*List.* The other 25 fields (`id`, `display_name`), for navigating laterally across the classification.

### `works_count`
*Integer.* How many works fall in this field through their primary topic. See [Common attributes](https://help.openalex.org/data/common-attributes/#works_count).

### `cited_by_count`
*Integer.* Total citations across all works in this field. See [Common attributes](https://help.openalex.org/data/common-attributes/#cited_by_count).

### `works_api_url`
*String.* A ready-made [Works](https://help.openalex.org/data/works/) API URL for every work in this field, e.g. `https://api.openalex.org/works?filter=topics.field.id:27`. A convenience link; work IDs aren't stored on the field object.

### `created_date`
*String.* The date this field was added to OpenAlex (`YYYY-MM-DD`). See [Common attributes](https://help.openalex.org/data/common-attributes/#created_date).

### `updated_date`
*String.* The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) UTC timestamp of the last change to the field object. See [Common attributes](https://help.openalex.org/data/common-attributes/#updated_date).

## In the API

The Fields endpoint is at [`api.openalex.org/fields`](https://api.openalex.org/fields). Fetch a single field by ID — [`/fields/27`](https://api.openalex.org/fields/27) — or a list, and [filter](https://help.openalex.org/api/filtering/), [search](https://help.openalex.org/api/searching/), [sort](https://help.openalex.org/api/sorting/), [group](https://help.openalex.org/api/grouping/), and [page](https://help.openalex.org/api/paging/) over it. With only 26 fields, one unfiltered request returns them all.

You can filter and group fields by `domain.id` and `subfields.id`, and by `works_count`, `cited_by_count`, `id`, and `display_name`, all of which also sort. Full-text matching uses the [`search` parameter](https://help.openalex.org/api/searching/) (the older `display_name.search` filter is deprecated). To find works in a field, use the [Works](https://help.openalex.org/data/works/) endpoint: `filter=primary_topic.field.id:27` (primary only) or `filter=topics.field.id:27` (any assigned topic). For the full list of endpoints see the [endpoints index](https://help.openalex.org/api/endpoints/).
