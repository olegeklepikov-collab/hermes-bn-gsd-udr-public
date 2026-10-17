> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-aboutness

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

**Aboutness** is what the things in OpenAlex are about. Most works are "about" something, and that aboutness aggregates up to characterize authors, institutions, sources, and other entities. OpenAlex offers several distinct aboutness signals, each usable as a filter; which one fits depends on your question.

Two properties help you choose. **Granularity** (the number of groups) sets how fine-grained an analysis can be. **Familiarity** is how recognizable the scheme is to others — how easily you can compare or share results.

| Signal | # groups | Familiarity | Fit to custom areas |
|---|---|---|---|
| [SDGs](https://help.openalex.org/data/sdgs/) | 17 | High | Low |
| [Domains](https://help.openalex.org/data/domains/) | 4 | High | Low |
| [Fields](https://help.openalex.org/data/fields/) | 26 | High | Low |
| [Subfields](https://help.openalex.org/data/subfields/) | 252 | High | Medium |
| [Topics](https://help.openalex.org/data/topics/) | 4,516 | Low | Medium-high |
| [Keywords](https://help.openalex.org/data/keywords/) | ~1.9 million | Medium | High |
| [Concepts](https://help.openalex.org/data/concepts/) (deprecated) | ~65,000 | High | Variable |
| [Text search](https://help.openalex.org/api/searching/) | ∞ | Low | High |
| [Semantic search](https://help.openalex.org/api/semantic-search/) | ∞ | Low | High |

A rough guide: the **topics hierarchy** ([domains](https://help.openalex.org/data/domains/) → [fields](https://help.openalex.org/data/fields/) → [subfields](https://help.openalex.org/data/subfields/) → [topics](https://help.openalex.org/data/topics/)) is the supported general-purpose system — pick the level whose granularity matches your question. **Keywords** fit narrower, more specific slices, and find works whatever words their authors used. **SDGs** map research onto the UN Sustainable Development Goals and little else. **Concepts** are deprecated — kept for continuity with Microsoft Academic Graph, no longer maintained; see [Concepts](https://help.openalex.org/data/concepts/). **Text search** fits custom areas no scheme covers, at the cost of comparability.

Not a subject signal, but close by: [**study designs**](https://help.openalex.org/data/study-designs/) say how the research inside a work was done (randomized controlled trial, observational study, systematic review and four more), not what it is about. They combine well with any of the signals above, e.g. every randomized controlled trial in the topic Cancer Immunotherapy and Biomarkers: `filter=topics.id:T10158,study_designs.id:randomized-controlled-trial`.

## Embeddings and semantic search

Aboutness doesn't have to go through a labeling scheme at all. OpenAlex embeds the title and abstract of every work as a vector using an open-source embedding model, so works that are about similar things sit near each other in vector space — no categories required. [Semantic search](https://help.openalex.org/api/semantic-search/) queries these embeddings directly: describe what you're looking for in plain language (a sentence, or even a whole abstract or grant description) and get back the works closest in meaning, even when the wording differs. It's the best fit when your research area doesn't line up with any predefined scheme and keyword matching is too brittle. Embeddings also help build the [keyword](https://help.openalex.org/data/keywords/) vocabulary: they surface candidate synonyms, which a judge then confirms or rejects before they are merged.

## Aboutness for your own text

For the topics hierarchy and keywords, you can supply your own custom text — the title and abstract of an unpublished article, say, or a grant proposal — and get back topics (with their subfield, field, and domain) and keywords in exactly the form OpenAlex assigns them to works. See the [text aboutness endpoint](https://help.openalex.org/api/tag-aboutness/).

## Related pages

- [Topics](https://help.openalex.org/data/topics/) — the four-level hierarchy and how it's assigned
- [Keywords](https://help.openalex.org/data/keywords/) — how keyword tagging works
- [SDGs](https://help.openalex.org/data/sdgs/) — the Sustainable Development Goals tagger
- [Study designs](https://help.openalex.org/data/study-designs/): how the research inside a work was done
- [FWCI](https://help.openalex.org/data/works/citations/#field-weighted-citation-impact) — the field-normalized citation metric built on subfields
