> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-native

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

**Native** entities are the ones where OpenAlex mints its own IDs — `W123` for a [work](https://help.openalex.org/data/works/), `A456` for an [author](https://help.openalex.org/data/authors/), `S789` for a [source](https://help.openalex.org/data/sources/) — and each ID encodes a judgment call about a genuine real-world boundary dispute:

- Are these two records the *same work*, or two different ones?
- Is this cluster of papers all by *one author*, or several people who share a name?
- Is "Springer Nature" the same [publisher](https://help.openalex.org/data/publishers/) as "Springer Verlag"?
- Does this affiliation string mean the University of Washington or Washington University?

There's no external authority we can just look up for these; the answer is OpenAlex's best inference, and it can be wrong. That's why native entities are the ones you can [correct through curation](https://help.openalex.org/data/curations/), and why every native entity page has an **About** section explaining where the records come from, what we do to disambiguate them, and the known failure modes.

## The native entities

- [**Works**](https://help.openalex.org/data/works/) — every scholarly document. The core entity; everything else connects to works.
- [**Authors**](https://help.openalex.org/data/authors/) — the people who create works, [disambiguated](https://help.openalex.org/data/authors/disambiguation/) from raw authorship strings.
- [**Sources**](https://help.openalex.org/data/sources/) — journals, conferences, repositories, and other venues where works appear.
- [**Publishers**](https://help.openalex.org/data/publishers/) — the organizations behind sources, arranged in a hierarchy.
- [**Funders**](https://help.openalex.org/data/funders/) — the organizations that fund research.
- [**Awards**](https://help.openalex.org/data/awards/) — specific grants, linking funders to the works they funded.
- [**Institutions**](https://help.openalex.org/data/institutions/) — universities, companies, hospitals, and other organizations authors are affiliated with.

Compare these with [vocabulary entities](https://help.openalex.org/data/vocabulary/), where there's no boundary to adjudicate — just a consistent handle on something that already exists crisply.
