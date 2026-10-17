> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: glossary

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> Quick reference for Scite-specific terminology used across the API.

| Term | Meaning |
| - | - |
| **Target** | The publication being cited. See Citations & Tallies (локальный ресурс исходного примера не включён). |
| **Source** | The publication making the citation. |
| **Tally** | Counts of citation statements toward a target: `total`, `supporting`, `contradicting`, `mentioning`, `unclassified`. |
| **Smart Citation** | A citation statement classified by how it uses the target (supporting / contradicting / mentioning). |
| **Contradicting / Contrasted** | The same concept: the API uses `contradicting`, the Scite UI displays "contrasted." |
| **Citing publications** | The count of distinct publications citing a target: not the same as the tally `total` (see Citations & Tallies (локальный ресурс исходного примера не включён)). |
| **Papers** | Publication metadata: DOI, title, publication date, and related fields. |
| **Collection** | A set of papers monitored over time. Created from DOIs or a search query via the API or MCP, or in the Scite UI (which also imports from Zotero, Mendeley, or CSV). |
| **Dashboard** | A report on a collection. |
| **Reference Check** | Scite's capability for evaluating and linking the references of a submitted document. |
| **Scite Journal Index (SJI)** | A journal-level index derived from Scite's citation data, looked up by ISSN. |
| **Assistant** | Scite's Q\&A endpoint that returns answers backed by citation evidence. |
| **Evidence** | Non-citation regulatory and research records searchable alongside citation data: patents, grants, clinical trials, and FDA/MHRA regulatory records. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
