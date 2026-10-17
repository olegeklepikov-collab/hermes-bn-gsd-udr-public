> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-component

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

**Component** entities are structured *parts of a work* that OpenAlex models in detail but doesn't give their own OpenAlex IDs. They aren't full citizens of the [entity galaxy](https://help.openalex.org/data/): a component has no minted ID, and you'll normally meet one *inside* a [work](https://help.openalex.org/data/works/) object, by selecting the field that holds it.

But "no ID" no longer means "no endpoint." Two of the three components now have their own top-level list endpoints you can page and filter directly — [`/locations`](https://api.openalex.org/locations) and [`/raw-affiliation-strings`](https://api.openalex.org/raw-affiliation-strings) — and an authorships endpoint is on the way. These are views over the same work-embedded data, not a promotion to native status: the rows carry namespaced handles (`doi:…`, `pmh:…`) or none at all rather than minted OpenAlex IDs, and are still defined only in relation to their work.

Components sit between [native entities](https://help.openalex.org/data/native/) (which get minted IDs and are curatable) and [vocabulary](https://help.openalex.org/data/vocabulary/) (fixed controlled lists). A component is real and richly structured, but it's meaningful only in the context of its work.

## The component entities

- [**Authorships**](https://help.openalex.org/data/authorships/) — the join between a work and its authors: for each author, their raw name as printed, their position, whether they're corresponding, and the institutions they listed. Lives in `work.authorships`; a standalone authorships endpoint is on the way.
- [**Locations**](https://help.openalex.org/data/locations/) — each place a version of the work is available (the publisher's site, a repository, a preprint server), with its version, license, and open-access status. Lives in `work.locations` / `primary_location` / `best_oa_location`, and also has a standalone [`/locations`](https://api.openalex.org/locations) endpoint you can filter, search, and group, with each copy fetchable at `/locations/{id}`.
- [**Raw affiliation strings**](https://help.openalex.org/data/raw-affiliation-strings/) — the exact affiliation text an author printed on a work, before OpenAlex matches it to an [institution](https://help.openalex.org/data/institutions/). The raw input to institution disambiguation; also queryable directly at [`/raw-affiliation-strings`](https://api.openalex.org/raw-affiliation-strings).

Because components carry much of a work's richest metadata, their fields are documented on their own pages here rather than crammed into the [works attribute dictionary](https://help.openalex.org/data/works/attributes/).
