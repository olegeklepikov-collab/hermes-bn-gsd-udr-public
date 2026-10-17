> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: adverse-events

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Adverse Events

> Search FDA MAUDE device and FAERS drug adverse-event reports.

Two datasets cover FDA post-market adverse-event reporting:

* **`maude`**: MAUDE reports for **medical devices** — event type, product problems, device details, patient treatment, and the narrative MDR text.
* **`faers`**: FAERS reports for **drugs** — the reported reactions (MedDRA terms), seriousness, patient demographics, and the drugs involved with dosage and indication.

<Info>
  Each dataset requires its own Evidence scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search MAUDE (devices)

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/maude' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q="insulin pump" AND occlusion' \
  --data-urlencode 's=date_received'
```

Each item in `results` includes `mdrReportKey`, `reportNumber`, `eventType`, `adverseEventFlag`, `productProblemFlag`, `productProblems`, a `device` object (`brandName`, `genericName`, `deviceName`, `manufacturerDName`, `modelNumber`, `deviceClass`, `regulationNumber`), a `patient` object, and `mdrText` — the narrative event descriptions. `s` accepts `_relevance` (default), `date_received`, and `date_report`.

## Search FAERS (drugs)

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/faers' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q=rhabdomyolysis AND statin'
```

Each item in `results` includes `safetyreportid`, an `event` object (`serious`, `seriousnessType`, `receiptdate`, patient age/sex/weight fields), a `reaction` array with MedDRA preferred terms (`reactionmeddrapt`) and outcomes, a `drug` array (`medicinalproduct`, `activesubstancename`, `drugindication`, dosage fields, `brandName`, `genericName`), and `primarysource` (reporter qualification and country).

## Single report

`GET /api_partner/evidence/maude/{report_id}` and `GET /api_partner/evidence/faers/{report_id}` return one full report each.

## Common uses

* **Signal monitoring**: facet by reaction term or product problem over time via the `facets` endpoint to spot emerging safety signals.
* **Due diligence**: pull the adverse-event history for a specific device model or drug substance before a deal, launch, or formulary decision.
* **Literature triangulation**: FAERS `literaturereference` fields and Scite Search (локальный ресурс исходного примера не включён) let you connect spontaneous reports to published case reports.

<Note>
  Adverse-event reports are spontaneous and unverified; report counts reflect reporting behavior as much as true incidence. Treat them as signals to investigate, not incidence rates.
</Note>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
