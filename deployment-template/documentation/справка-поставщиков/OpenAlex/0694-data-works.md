> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-works

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

A **work** is any scholarly document: a journal article, conference paper, book or book chapter, dataset, dissertation, preprint, and more. There are over 320 million works in OpenAlex, with tens of thousands added every day. A work's OpenAlex ID looks like `W2741809807`; fetch one at [`api.openalex.org/works/W2741809807`](https://api.openalex.org/works/W2741809807).

Works are the central entity in OpenAlex — everything connects to them. [Authors](https://help.openalex.org/data/authors/) write works, [sources](https://help.openalex.org/data/sources/) publish them, [institutions](https://help.openalex.org/data/institutions/) get credit for them, [topics](https://help.openalex.org/data/topics/) describe them, and [funders](https://help.openalex.org/data/funders/) pay for them. Works also carry by far the most information of any entity: all twenty-ish entity types are first-class citizens, but works are the firstest class.

## About

### Where works come from

OpenAlex aggregates and builds on many open data sources. The catalog was seeded by the [Microsoft Academic Graph (MAG)](https://en.wikipedia.org/wiki/Microsoft_Academic) — Microsoft Research's effort to catalog the scholarly literature — whose final open dataset OpenAlex adopted when the project was discontinued in 2021. The other primary source is [Crossref](https://www.crossref.org/), the open DOI-registration agency. Alongside those, works are drawn from DataCite, PubMed, HAL, institutional and subject repositories, and more; see [How it's built](https://help.openalex.org/data/how-its-built/) for the full ingest picture.

### How locations become works

OpenAlex starts from [locations](https://help.openalex.org/data/locations/): copies of a work hosted at particular places. A preprint on arXiv is one location; the same paper published in *Physical Review B* is a second; the accepted manuscript in a university repository is a third. The job is to recognize that all three are one work. Two mechanisms do that, used together:

- **Persistent identifiers.** If a location carries a DOI, PubMed ID, or arXiv ID that OpenAlex already knows, it belongs to that work. This is the certain path: a shared PID is treated as proof.
- **Fuzzy metadata matching.** Locations with no shared PID — most repository copies, many preprints — go through a fuzzy matching algorithm built on title normalization plus author names, tuned over the years for precision and recall.

Whichever path matches, the location joins the existing work and *enriches* it rather than minting a new one. If nothing matches, the location seeds a new work of its own; the only locations that don't are ones with neither a PID nor a usable title, which are dropped.

Once a work exists, OpenAlex tracks its own metadata — title, abstract (and often full text), publication date, type — and the connections that make it useful at scale: authors, institutional affiliations, the source it appeared in, topics, funders, and citations.

How works cite each other — references, citation counts, and FWCI — has its own page: [Citations](https://help.openalex.org/data/works/citations/). How OpenAlex decides whether a work is free to read: [Open access](https://help.openalex.org/data/works/open-access/).

## In the API

The Works endpoint is at [`api.openalex.org/works`](https://api.openalex.org/works). Fetch a single work by ID — [`/works/W2741809807`](https://api.openalex.org/works/W2741809807) — or a list, and [filter](https://help.openalex.org/api/filtering/), [search](https://help.openalex.org/api/searching/), [sort](https://help.openalex.org/api/sorting/), [group](https://help.openalex.org/api/grouping/), and [page](https://help.openalex.org/api/paging/) over the attributes documented on the [Attributes](https://help.openalex.org/data/works/attributes/) page. For the full list of endpoints see the [endpoints index](https://help.openalex.org/api/endpoints/).
