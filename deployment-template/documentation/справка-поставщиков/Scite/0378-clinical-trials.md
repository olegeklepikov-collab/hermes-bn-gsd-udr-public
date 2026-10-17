> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: clinical-trials

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Clinical Trials

> Search registered clinical trials with phase, status, sponsor, and intervention filters.

The clinical trials dataset covers registered trials with their design, status, sponsors, conditions, interventions, eligibility criteria, enrollment, key dates, and reported adverse events. Trials also carry `citations` and `publicationsMetadata`, linking them back to the published literature — so you can move from a trial to its results papers and their Smart Citations (локальный ресурс исходного примера не включён).

<Info>
  Requires the `evidence:clinical-trials:api` scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search trials

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/clinical-trials' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q=semaglutide' \
  --data-urlencode 'f=trialState.phase:"Phase III" trialState.overallStatus:"Recruiting"'
```

Each item in `results` includes `title`, `briefDescription`, `description`, `sponsors`, `pi`, `conditions`, `interventions`, `trialState` (phase and overall status), `eligibility`, `enrollment`, `dates`, `registry`, `hasResults`, `reportedEvents`, `citations`, `publicationsMetadata`, and an `externalLink` to the registry entry.

## Useful filters

| Filter | Values |
| - | - |
| `trialState.phase` | `"Phase I"` through `"Phase IV"`, `"N/A"` |
| `trialState.overallStatus` | `"Recruiting"`, `"Completed"`, and other registry statuses |
| `conditions` | Condition name, e.g. `"Type 2 Diabetes"` |
| `interventions.name` | Drug, device, or procedure name |
| `sponsors.name` | Sponsor organization |
| `registry` | Source registry |
| `design.studyType` | Study type, e.g. interventional vs. observational |

Filter by date with range suffixes on `dates.startDate`, `dates.completedDate`, or `dates.lastUpdatedDate`: `f=dates.startDategte:"2024-01-01" dates.startDatelt:"2025-01-01"`.

## Sorting

`s` accepts `_relevance` (default), `dates.startDate`, `dates.completedDate`, and `dates.lastUpdatedDate`. Combine with `sortDir=asc|desc`.

## Single trial

`GET /api_partner/evidence/clinical-trials/{trial_id}` returns the full record, including detailed `reportedEvents` (adverse events reported for the trial).

## Common uses

* **Pipeline monitoring**: filter a condition or intervention by phase and status, sort by `dates.lastUpdatedDate` to catch changes.
* **Site and sponsor analysis**: facet on `sponsors.name` via the `facets` endpoint to see who is active in an indication.
* **Evidence synthesis**: use `hasResults` and the linked `publicationsMetadata` to connect trials to their published outcomes, then check how those papers are cited with tallies (локальный ресурс исходного примера не включён).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
