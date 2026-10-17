> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-languages

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Languages

A **language** is the language of a [work](https://help.openalex.org/data/works/)'s metadata — its title and abstract — identified by a two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code: `en` for English, `es` for Spanish, `zh` for Chinese. Languages are a [vocabulary](https://help.openalex.org/data/vocabulary/): a fixed, standardized list OpenAlex attaches handles to rather than inventing. Each work carries a single [`language`](https://help.openalex.org/data/works/attributes/#language), auto-detected with [langdetect](https://pypi.org/project/langdetect/) — so a language value reflects the metadata language, not necessarily the full text, and is unset when there aren't enough words to guess reliably. A language's OpenAlex ID looks like `https://openalex.org/languages/en`; fetch one at [`api.openalex.org/languages/en`](https://api.openalex.org/languages/en).

## About

We don't build the list — we adopt [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), the standard two-letter language codes, and add live counts of the works detected in each. Detection is per-work and automatic (see the work [`language`](https://help.openalex.org/data/works/attributes/#language) field). There are 180 languages.

## Values

The full list of 180 languages is at [`api.openalex.org/languages`](https://api.openalex.org/languages) — page through with `per_page=200` to pull every one. A sample of the largest by works count:

| Code | Language |
|------|----------|
| `en` | English |
| `de` | German |
| `es` | Spanish |
| `fr` | French |
| `ja` | Japanese |
| `pt` | Portuguese |
| `zh` | Chinese |
| `ru` | Russian |
| `it` | Italian |
| `id` | Indonesian |
| `ko` | Korean |
| `nl` | Dutch |

## Attributes

The top-level fields on a **language** object. Attributes shared with other entities ([`id`](https://help.openalex.org/data/common-attributes/#id), [`display_name`](https://help.openalex.org/data/common-attributes/#display_name), [`works_count`](https://help.openalex.org/data/common-attributes/#works_count), [`cited_by_count`](https://help.openalex.org/data/common-attributes/#cited_by_count), [`created_date`](https://help.openalex.org/data/common-attributes/#created_date), [`updated_date`](https://help.openalex.org/data/common-attributes/#updated_date)) are documented once on [Common attributes](https://help.openalex.org/data/common-attributes/).

### `id`
*String.* The [OpenAlex ID](https://help.openalex.org/data/#the-openalex-id-scheme) for this language, e.g. `https://openalex.org/languages/en`. The final path segment is the ISO 639-1 code. See [Common attributes](https://help.openalex.org/data/common-attributes/#id).

### `display_name`
*String.* The language's English name, e.g. `English`. See [Common attributes](https://help.openalex.org/data/common-attributes/#display_name).

### `works_count`
*Integer.* How many works OpenAlex has detected in this language. See [Common attributes](https://help.openalex.org/data/common-attributes/#works_count).

### `cited_by_count`
*Integer.* Total citations across those works. See [Common attributes](https://help.openalex.org/data/common-attributes/#cited_by_count).

### `works_api_url`
*String.* A ready-made [Works](https://help.openalex.org/data/works/) API URL for every work in this language (`filter=language:<CODE>`).

### `created_date`
*String.* When the language record was added to OpenAlex (`YYYY-MM-DD`). See [Common attributes](https://help.openalex.org/data/common-attributes/#created_date).

### `updated_date`
*String.* When the language record last changed. See [Common attributes](https://help.openalex.org/data/common-attributes/#updated_date).

## In the API

The Languages endpoint is at [`api.openalex.org/languages`](https://api.openalex.org/languages). Fetch one by code — [`/languages/en`](https://api.openalex.org/languages/en) — or list them all.

Languages are most useful as a filter on [works](https://help.openalex.org/data/works/): `filter=language:fr` returns works whose metadata is in French, and `group_by=language` breaks any result set down by language. See [Filtering](https://help.openalex.org/api/filtering/) for the full syntax and the [endpoints index](https://help.openalex.org/api/endpoints/) for every endpoint. See also the work [`language`](https://help.openalex.org/data/works/attributes/#language) field for how the value is assigned.
