> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: grants

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grants

> Search research grant awards from NIH RePORTER, NSF, and other funding sources.

The grants dataset covers research funding awards: title, abstract, awarding agency and branch, recipient organization, principal investigator, award amount, and award dates. Records come from sources such as NIH RePORTER and NSF and are grouped so related awards surface together. Use it to see who funds a research area, track a lab's funding history, or spot emerging topics before they show up in publications.

<Info>
  Requires the `evidence:grants:api` scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search grants

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/grants' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q="single cell" AND atlas' \
  --data-urlencode 'f=agency:"NIH" country:"USA"' \
  --data-urlencode 's=awardAmount'
```

Each item in `results` is a grant group: `{ grants, grantsTotal, ... }`, where each grant carries `title`, `abstract`, `organization`, `country`, `state`, `piName`, `awardAmount`, `awardStartDate`, `awardCloseDate`, `awardNoticeDate`, `agency`, `branch`, `researchKeywords`, `dataSource`, `phase`, `program`, and an `externalLink` to the source record.

## Useful filters

| Filter | Values |
| - | - |
| `agency` | Funding agency, e.g. `"NIH"`, `"NSF"` |
| `organization` | Recipient institution |
| `piName` | Principal investigator name |
| `country` | ISO 3166-1 alpha-3 code, e.g. `"USA"` |
| `dataSource` | `"NIH RePORTER"`, `"NSF"`, and other sources |

Filter by award dates with range suffixes: `f=awardStartDategte:"2023-01-01"`.

## Sorting

`s` accepts `_relevance` (default), `awardStartDate`, `awardCloseDate`, `awardNoticeDate`, `awardAmount`, and `employeeCount`. Combine with `sortDir=asc|desc`.

## Single grant

`GET /api_partner/evidence/grants/{grant_id}` returns the full record for one grant group.

## Common uses

* **Funding landscape**: facet on `agency` or `organization` via the `facets` endpoint to map who funds a topic.
* **Prospect and partner research**: look up a PI or institution's active awards, sorted by `awardAmount` or `awardStartDate`.
* **Early signal detection**: grants precede publications; a topic search sorted by `awardNoticeDate` shows where funding is moving now.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
