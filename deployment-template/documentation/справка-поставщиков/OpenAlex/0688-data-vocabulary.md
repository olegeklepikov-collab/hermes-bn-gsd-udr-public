> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-vocabulary

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

**Vocabulary** entities are a convenient, consistent vocabulary around things that already have very clear real-world existence, with no fuzziness for OpenAlex to adjudicate. We don't decide what a [country](https://help.openalex.org/data/countries/) *is*, or invent the concept of a CC-BY [license](https://help.openalex.org/data/licenses/) — we just attach a consistent handle to each one so you can filter and group by it reliably.

This is the key contrast with [native entities](https://help.openalex.org/data/native/): a native ID like an [author](https://help.openalex.org/data/authors/) ID represents a judgment call that could be wrong and can be [corrected](https://help.openalex.org/data/curations/). A vocabulary value like `article` or `US` represents no judgment call — the boundary is already crisp; we've only standardized the label. So vocabulary pages have a **Values** section (the full controlled list) rather than a curation story.

Vocabulary entities generally use short, human-readable IDs (`en` for English, `US` for the United States, `article` for a journal article) rather than the minted `W`/`A`/`S` scheme.

## The vocabulary entities

- [**Work types**](https://help.openalex.org/data/work-types/) — article, preprint, dataset, book, and the rest of a work's `type`.
- [**Source types**](https://help.openalex.org/data/source-types/) — journal, conference, repository, ebook platform, and other venue kinds.
- [**Institution types**](https://help.openalex.org/data/institution-types/) — education, healthcare, company, government, and so on.
- [**Countries**](https://help.openalex.org/data/countries/) and [**continents**](https://help.openalex.org/data/continents/) — geography, as ISO codes.
- [**Languages**](https://help.openalex.org/data/languages/) — the language of a work's metadata, as ISO 639-1 codes.
- [**Licenses**](https://help.openalex.org/data/licenses/) — the Creative Commons and other licenses a location can carry.
- [**Indexes**](https://help.openalex.org/data/indexes/) — the external registries (Crossref, PubMed, DOAJ, …) a work's record can come from. These are vocabulary, not native: we're not minting judgment-call IDs, just consistent handles on crisply-existing lists.
- [**Source lists**](https://help.openalex.org/data/source-lists/) — the external journal lists (DOAJ, CWTS Core, national lists) a source can appear on. Membership only; OpenAlex endorses none of them.

Some classification systems that *look* like vocabularies — [topics, fields, subfields, domains](https://help.openalex.org/data/aboutness/) — are grouped under [Aboutness](https://help.openalex.org/data/aboutness/) instead, because assigning them to a work involves real inference. [Study designs](https://help.openalex.org/data/study-designs/) sit there too for the same reason: the seven values come from PubMed's vocabulary, but every work gets them from automated tagging.
