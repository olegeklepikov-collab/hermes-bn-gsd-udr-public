> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: patents

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Patents

> Search patent filings with family, forward-citation, assignee, and legal-event data.

The patents dataset covers patent filings grouped into **families** (the same invention filed across jurisdictions). Results include inventors, assignees, classifications, filing status, publication references, and legal events, plus family size and forward citation counts for gauging a patent's footprint. Use it to track competitor filings, map the IP landscape around a technology, or connect published research to the patents that cite it.

<Info>
  Requires the `evidence:patents:api` scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search patents

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/patents' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q="mRNA vaccine" AND delivery' \
  --data-urlencode 'f=patents.filingStatus:"grant"' \
  --data-urlencode 's=forwardCitationCount'
```

Each item in `results` is a patent family: `{ familyId, familySize, forwardCitationCount, patents, patentsTotal }`, where `patents` holds the individual filings with `title`, `abstract`, `filingStatus`, `classifications`, `inventors`, `assignees`, `applicants`, `appRef` (application reference and filing date), `publications`, `languages`, and `legalEvents`.

## Useful filters

| Filter | Values |
| - | - |
| `patents.filingStatus` | `"application"`, `"grant"` |
| `patents.assignees.name` | Assignee (company or institution) name |
| `patents.inventors.name` | Inventor name |
| `patents.languages` | ISO 639-1 code, e.g. `"en"` |

Filter by filing or publication date with range suffixes: `f=patents.appRef.filingDategte:"2022-01-01"`. Call `GET /api_partner/evidence/patents/schema` for the full filterable field list.

## Sorting

`s` accepts `_relevance` (default), `forwardCitationCount`, `familySize`, `patents.publications.pubRef.date`, and `patents.appRef.filingDate`. Combine with `sortDir=asc|desc`.

## Single patent

`GET /api_partner/evidence/patents/{patent_id}` returns the full record for one filing, including `familySize` and `forwardCitationCount` alongside the complete `patent` object.

## Common uses

* **Competitive intelligence**: filter by `patents.assignees.name` and sort by filing date to watch a competitor's pipeline.
* **Technology landscaping**: free-text query for a technique, facet by year or assignee via the `facets` endpoint to see who is filing and when.
* **Research-to-IP linkage**: search a topic in both Search (локальный ресурс исходного примера не включён) and patents to see how a body of literature translates into filings.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
