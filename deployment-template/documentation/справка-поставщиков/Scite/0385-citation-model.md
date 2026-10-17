> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: citation-model

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Citations & Tallies

> How Scite models citations: targets, sources, Smart Citations, and tallies.

Scite's data model differs from a plain citation count in a few ways that matter once you start building against the API.

## Target and source

* **Target**: the publication being cited.
* **Source**: the publication making the citation.

Endpoints are named from this perspective: `citing/{doi}` returns sources that cite the target `{doi}`; `cited_by/{doi}` returns targets cited by the source `{doi}`.

## Smart Citations

A **Smart Citation** is a citation statement classified by how it uses the target publication:

| Classification | Meaning |
| - | - |
| `supporting` | The citing statement supports the target's findings |
| `contradicting` | The citing statement contradicts the target's findings (referred to as "contrasted" in the Scite UI) |
| `mentioning` | The citing statement mentions the target without a clear supporting/contradicting stance |
| `unclassified` | Not yet classified |

## Tallies vs. citing publications

This is the distinction that trips people up most:

* **Tally counts** (`total`, `supporting`, `contradicting`, `mentioning`, `unclassified`) count individual **citation statements** that Scite has extracted and classified as Smart Citations.
* **`citingPublications`** counts distinct **publications** that cite the target, drawn from the broader citation graph rather than only publications with a classified Smart Citation.

These come from different underlying counts, so neither bounds the other. `citingPublications` can exceed `total` (not every citing publication has a classified statement) or fall below it (one publication can make several classified statements toward the same target). Treat them as two different measurements, not a count and a subset.

## References vs. citations

In everyday language "citation" and "reference" are interchangeable. In the Scite API, **references** specifically means the distinct source/target DOI pairs. See the References endpoints (**References** in the API Reference tab) if you need the raw pairs rather than tally counts.

## Related

* Smart Citations guide (локальный ресурс исходного примера не включён): the endpoints that implement this model
* Glossary (локальный ресурс исходного примера не включён): quick lookup for other terms (dashboards, DOI resolution, etc.)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
