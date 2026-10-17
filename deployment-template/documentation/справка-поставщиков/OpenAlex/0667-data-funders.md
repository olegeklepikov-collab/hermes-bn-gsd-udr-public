> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-funders

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Funders

A **funder** is an organization that funds research — a government agency, foundation, or charity. OpenAlex tracks about 45,000 funders, and each connects to the [works](https://help.openalex.org/data/works/) it funded and to the specific [awards](https://help.openalex.org/data/awards/) (grants) that funded them. A funder's OpenAlex ID looks like `F4320332161`; fetch one at [`api.openalex.org/funders/F4320332161`](https://api.openalex.org/funders/F4320332161) (the US National Institutes of Health).

> [!claude]
> You can profile a funder in one ask: *"Profile the National Natural Science Foundation of China (F4320321001): top fields, open-access share, and the trend by year."* Set up once: [Using OpenAlex with an AI assistant](https://help.openalex.org/how-to/ai-assistants/).

## About

### Where funders come from

Funders are [native entities](https://help.openalex.org/data/native/): OpenAlex decides which real-world organizations count as distinct funders and mints an ID for each. The funder list is grounded in the [Crossref Open Funder Registry](https://www.crossref.org/services/funder-registry/) — Crossref's canonical list of research funders, each with a stable Funder DOI (e.g. `10.13039/100000002` for the NIH) — and enriched with names, homepages, logos, and country from [Wikidata](https://www.wikidata.org/) and [ROR](https://ror.org/). Those registries are also where the external IDs in [`ids`](#ids) come from: the Crossref funder ID and DOI, plus ROR and Wikidata IDs where they exist.

### How funders connect to works

OpenAlex doesn't observe funding directly; it reads it off the works. When a [work's](https://help.openalex.org/data/works/) metadata (from Crossref, a funder's own grant records, or other sources) names a funder or a grant, OpenAlex matches that mention to a funder in this list and to the specific [award](https://help.openalex.org/data/awards/) if one is identified. Roll-up counts live on the funder: [`works_count`](#works_count) is how many works name this funder, [`awards_count`](#awards_count) is how many distinct grants OpenAlex has recorded for it, and [`cited_by_count`](#cited_by_count) sums citations across those works. See [Awards](https://help.openalex.org/data/awards/) for how individual grants are built.

### Lineage and hierarchy

Unlike [publishers](https://help.openalex.org/data/publishers/) and [institutions](https://help.openalex.org/data/institutions/), funders are **flat** in OpenAlex: a funder object carries no parent, no children, and no `lineage` field, so there's no funder tree to roll a sub-agency up into its parent department the way you can roll an imprint up to its publishing group. (The underlying [Crossref funder registry](https://www.crossref.org/services/funder-registry/) does record some parent/child relationships between funders, but OpenAlex does not currently surface them.) To connect a funder to the *same* organization in another role, use [`roles`](#roles) below.

### Roles

A single real-world organization can act as more than one kind of OpenAlex entity: a national agency is a **funder**, but the same organization is often also an **[institution](https://help.openalex.org/data/institutions/)** (when its own staff do research) and sometimes a **[publisher](https://help.openalex.org/data/publishers/)**. [`roles`](#roles) links those alter egos together, so you can hop from the funder record to the institution or publisher record for the same organization.

### Failure modes

Because funders are inferred and matched, they can be wrong: a funder mentioned only by a noisy free-text string may not match (so a work that *was* funded shows no funder), two records for one funder may not yet be merged, or a small funder may be absent from the source registries and so missing here. These are [curatable](https://help.openalex.org/data/curations/).

## Attributes

This is the canonical dictionary of every attribute on a **funder** object. Attributes shared with other entities ([`id`](https://help.openalex.org/data/common-attributes/#id), [`ids`](https://help.openalex.org/data/common-attributes/#ids), [`display_name`](https://help.openalex.org/data/common-attributes/#display_name), [`works_count`](https://help.openalex.org/data/common-attributes/#works_count), [`cited_by_count`](https://help.openalex.org/data/common-attributes/#cited_by_count), [`summary_stats`](https://help.openalex.org/data/common-attributes/#summary_stats), [`counts_by_year`](https://help.openalex.org/data/common-attributes/#counts_by_year), [`created_date`](https://help.openalex.org/data/common-attributes/#created_date), [`updated_date`](https://help.openalex.org/data/common-attributes/#updated_date)) are documented once on [Common attributes](https://help.openalex.org/data/common-attributes/); funder-specific notes are below.

### `id`
*String.* The [OpenAlex ID](https://help.openalex.org/data/#the-openalex-id-scheme) for this funder, e.g. `https://openalex.org/F4320332161`. See [Common attributes](https://help.openalex.org/data/common-attributes/#id).

### `ids`
*Object.* All known external identifiers for this funder, as URIs or bare values. Funder keys: `openalex`, `ror`, `wikidata`, `crossref` (the [Crossref funder registry](https://www.crossref.org/services/funder-registry/) ID), and `doi` (the Funder DOI). See [Common attributes](https://help.openalex.org/data/common-attributes/#ids).

### `display_name`
*String.* The funder's name, e.g. `National Institutes of Health`. See [Common attributes](https://help.openalex.org/data/common-attributes/#display_name). Filterable and searchable; not available as a `group_by`.

### `alternate_titles`
*List.* Other names the funder is known by, including acronyms (`NIH`) and names in other languages.

### `description`
*String.* A short description of the funder, usually pulled from [Wikidata](https://www.wikidata.org/) (e.g. "US government medical research agency").

### `country_code`
*String.* The [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of the country the funder is based in. Unlike a [publisher's](https://help.openalex.org/data/publishers/#country_codes) list, a funder has a single home country.

### `is_global_south`
*Boolean.* Whether the funder is based in the [Global South](https://en.wikipedia.org/wiki/Global_South). Filterable and groupable — handy for equity analyses.

### `awards_count`
*Integer.* The number of distinct [awards](https://help.openalex.org/data/awards/) (grants) OpenAlex has recorded for this funder.

### `homepage_url`
*String.* The URL of the funder's homepage.

### `image_url`
*String.* A URL to the funder's logo or a representative image (usually from [Wikimedia Commons](https://commons.wikimedia.org/)).

### `image_thumbnail_url`
*String.* Like [`image_url`](#image_url), but scaled down for a thumbnail (a `width` parameter is appended).

### `works_count`
*Integer.* The number of works that name this funder. See [Common attributes](https://help.openalex.org/data/common-attributes/#works_count).

### `cited_by_count`
*Integer.* Total citations received across all works this funder funded. See [Common attributes](https://help.openalex.org/data/common-attributes/#cited_by_count).

### `summary_stats`
*Object.* Precomputed bibliometric indicators (`2yr_mean_citedness`, `h_index`, `i10_index`) over the funder's works. See [Common attributes](https://help.openalex.org/data/common-attributes/#summary_stats).

### `counts_by_year`
*List.* Works and citations per year for roughly the last ten years; funder rollups also carry `oa_works_count` per year. See [Common attributes](https://help.openalex.org/data/common-attributes/#counts_by_year).

### `roles`
*List.* The other OpenAlex entities that are the *same real-world organization* — each a `{ role, id, works_count }` object where `role` is one of `funder`, `institution`, or `publisher`. See [Roles](#roles). Filter on `roles.id`.

### `created_date`
*String.* The date this funder was added to OpenAlex (`YYYY-MM-DD`). See [Common attributes](https://help.openalex.org/data/common-attributes/#created_date).

### `updated_date`
*String.* The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) UTC timestamp of the last change to this funder object. See [Common attributes](https://help.openalex.org/data/common-attributes/#updated_date).

## In the API

The Funders endpoint is at [`api.openalex.org/funders`](https://api.openalex.org/funders). Fetch a single funder by ID — [`/funders/F4320332161`](https://api.openalex.org/funders/F4320332161) — or a list, and [filter](https://help.openalex.org/api/filtering/), [search](https://help.openalex.org/api/searching/), [sort](https://help.openalex.org/api/sorting/), [group](https://help.openalex.org/api/grouping/), and [page](https://help.openalex.org/api/paging/) over the fields above. To find the works a funder funded, filter [works](https://help.openalex.org/data/works/) on `funders.id`; for the individual grants, see [awards](https://help.openalex.org/data/awards/). For the full list of endpoints see the [endpoints index](https://help.openalex.org/api/endpoints/).
