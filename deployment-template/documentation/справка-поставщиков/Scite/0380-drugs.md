> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: drugs

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Drugs

> Search FDA drug labels, Orange Book listings, and Drugs@FDA application records.

The drugs dataset (`drugs`) combines FDA drug labels, Orange Book listings, and Drugs\@FDA application records into one searchable resource. Each result ties together the regulatory application (sponsor, products, approval dates, marketing status, therapeutic equivalence codes) and the label metadata (brand/generic names, active ingredients, pharmacologic classes, routes, NDC codes).

<Info>
  Requires the drugs dataset's Evidence scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search drugs

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/drugs' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q=semaglutide'
```

Each item in `results` carries `title`, `tags`, `categories`, an `application` object (`applicationNumber`, `sponsorName`, `products` — each with `approvalDate`, `marketingStatus`, `dosageForm`, `route`, `teCode`, and `activeIngredients` with strengths), and a `labels` object (`brandName`, `genericName`, `manufacturerName`, `substanceName`, pharmacologic class fields like `pharmClassEpc` and `pharmClassMoa`, plus `rxcui`, `unii`, and NDC identifiers).

Call `GET /api_partner/evidence/drugs/schema` for the filterable fields, and use the `facets` endpoint to aggregate, for example, by pharmacologic class or sponsor.

## Single drug

`GET /api_partner/evidence/drugs/{drug_id}` returns the full record for one drug.

## Common uses

* **Regulatory lookup**: resolve a brand or generic name to its application number, sponsor, approval dates, and marketing status in one call.
* **Formulary and equivalence work**: `teCode` and `referenceDrug` on products support therapeutic-equivalence checks against the Orange Book.
* **Cross-dataset safety picture**: pair a drug's identifiers with FAERS adverse-event reports (локальный ресурс исходного примера не включён) and the published literature via Search (локальный ресурс исходного примера не включён).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
