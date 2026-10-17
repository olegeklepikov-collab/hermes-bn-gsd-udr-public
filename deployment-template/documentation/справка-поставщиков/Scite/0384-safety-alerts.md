> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: safety-alerts

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Safety Alerts

> Search UK MHRA safety alerts, including full alert document content.

The `mhra` dataset covers safety alerts from the UK Medicines and Healthcare products Regulatory Agency: device safety notices, drug alerts, and recalls. Records include the alert headline and description plus the full attached documents with per-page extracted text, so you can search what an alert actually says.

<Info>
  Requires the MHRA dataset's Evidence scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search alerts

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/mhra' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q=recall AND "hip implant"'
```

Each item in `results` includes `filename`, `domain`, `url`, and `attachments`. Attachments carry `extras` (`headLine`, `description`, `contentHtml`), file metadata, ontology `tags`/`categories`, and `pages` with extracted text (`content`) for full-document search.

Call `GET /api_partner/evidence/mhra/schema` for filterable fields, and use the `facets` endpoint to aggregate by category or date.

## Single alert

`GET /api_partner/evidence/mhra/{item_id}` returns one full alert with its attachments.

## Common uses

* **Recall monitoring**: watch for new alerts mentioning a product category or manufacturer.
* **Cross-jurisdiction safety view**: pair MHRA alerts with FDA MAUDE and FAERS reports (локальный ресурс исходного примера не включён) to compare UK and US signals for the same product.
* **Compliance research**: full-text search of alert documents supports precise queries (model numbers, lot references) that headline-only feeds miss.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
