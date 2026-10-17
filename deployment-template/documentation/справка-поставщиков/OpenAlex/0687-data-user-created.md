> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: data-user-created

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

Almost every entity in OpenAlex is minted by OpenAlex: we create the [works](https://help.openalex.org/data/works/), disambiguate the [authors](https://help.openalex.org/data/authors/), assign the [topics](https://help.openalex.org/data/topics/). **User-created** entities are the exception — things *you* mint.

They matter because they close the loop: OpenAlex builds the map, and users push back on it and build on top of it.

## The user-created entities

- [**Collections**](https://help.openalex.org/data/collections/) — saved sets of entities (a reading list, a department's authors, a corpus for an analysis) that a user assembles and can re-query.
- [**Curations**](https://help.openalex.org/data/curations/) — user-submitted corrections to native entities: fixing an [author profile](https://help.openalex.org/data/authors/#a-profile-is-built-from-its-works), correcting an [affiliation](https://help.openalex.org/data/raw-affiliation-strings/), flagging a wrong [open-access status](https://help.openalex.org/data/works/open-access/). A curation records who changed what, when, and its review status, and — once accepted — flows into the entity it corrects.

Because these come from users rather than the pipeline, they don't have an "About" provenance story; instead their pages describe who can create them, what states they move through, and how they feed back into OpenAlex.
