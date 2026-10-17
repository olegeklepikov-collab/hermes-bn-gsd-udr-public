> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-continents

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Continents

A **continent** is one of the major geographic regions of the world — Africa, Asia, Europe, and so on. Continents are a [vocabulary](https://help.openalex.org/data/vocabulary/): a fixed, crisply-existing list that OpenAlex simply attaches a handle to. Each [country](https://help.openalex.org/data/countries/) belongs to exactly one continent, so a continent is really a convenient roll-up of countries — handy for filtering works by geographic region or comparing research output across parts of the world. Continents are used on the same entities as countries: [institutions](https://help.openalex.org/data/institutions/), [authors](https://help.openalex.org/data/authors/), and [works](https://help.openalex.org/data/works/). A continent's OpenAlex ID looks like `https://openalex.org/continents/Q15`; fetch one at [`api.openalex.org/continents/Q15`](https://api.openalex.org/continents/Q15).

## About

Continents are the standard seven-continent model, with each [country](https://help.openalex.org/data/countries/) assigned to one via its [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166) code. OpenAlex keys each continent by its [Wikidata](https://www.wikidata.org/) QID (e.g. `Q15` for Africa) and adds live scholarly counts on top.

## Values

There are seven continents — the complete list:

| ID | Continent | Countries |
|----|-----------|:---------:|
| `Q15` | Africa | 57 |
| `Q18` | South America | 15 |
| `Q46` | Europe | 52 |
| `Q48` | Asia | 54 |
| `Q49` | North America | 41 |
| `Q51` | Antarctica | 3 |
| `Q55643` | Oceania | 25 |

## Attributes

The top-level fields on a **continent** object. Attributes shared with other entities ([`id`](https://help.openalex.org/data/common-attributes/#id), [`ids`](https://help.openalex.org/data/common-attributes/#ids), [`display_name`](https://help.openalex.org/data/common-attributes/#display_name), [`created_date`](https://help.openalex.org/data/common-attributes/#created_date), [`updated_date`](https://help.openalex.org/data/common-attributes/#updated_date)) are documented once on [Common attributes](https://help.openalex.org/data/common-attributes/).

### `id`
*String.* The [OpenAlex ID](https://help.openalex.org/data/#the-openalex-id-scheme) for this continent, e.g. `https://openalex.org/continents/Q15`. The final path segment is the [Wikidata](https://www.wikidata.org/) QID. See [Common attributes](https://help.openalex.org/data/common-attributes/#id).

### `ids`
*Object.* External identifiers for the continent: `openalex` and `wikidata`.

### `display_name`
*String.* The continent's English name, e.g. `Africa`. See [Common attributes](https://help.openalex.org/data/common-attributes/#display_name).

### `description`
*String.* A short one-line description (typically just "continent").

### `display_name_alternatives`
*List.* Other names for the continent, when any exist.

### `countries`
*List.* The [countries](https://help.openalex.org/data/countries/) on this continent, each a dehydrated `{ id, display_name }`.

### `created_date`
*String.* When the continent record was added to OpenAlex (`YYYY-MM-DD`). See [Common attributes](https://help.openalex.org/data/common-attributes/#created_date).

### `updated_date`
*String.* When the continent record last changed. See [Common attributes](https://help.openalex.org/data/common-attributes/#updated_date).

## In the API

The Continents endpoint is at [`api.openalex.org/continents`](https://api.openalex.org/continents). Fetch one by ID — [`/continents/Q15`](https://api.openalex.org/continents/Q15) — or list all seven.

To use continents as a filter on other entities, filter [works](https://help.openalex.org/data/works/) by author continent with `filter=authorships.institutions.continent:africa` (the lowercased continent name is accepted), and group any list by continent with `group_by=authorships.institutions.continent`. See [Filtering](https://help.openalex.org/api/filtering/) for the full syntax and the [endpoints index](https://help.openalex.org/api/endpoints/) for every endpoint. Related: [countries](https://help.openalex.org/data/countries/).
