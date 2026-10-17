> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: devices

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Device Clearances

> Search FDA 510(k) device clearance decisions and their summary PDFs.

Two datasets cover FDA 510(k) premarket notifications:

* **`device510k`**: the structured clearance records — device name and class, product code, applicant, decision code and date, advisory committee, and regulation number.
* **`device510k-summaries`**: the 510(k) summary PDFs behind those clearances, with per-page extracted text, so you can search the actual submission content, not just the metadata.

<Info>
  Each dataset requires its own Evidence scope. See the Evidence overview (локальный ресурс исходного примера не включён) for how scopes work.
</Info>

## Search clearances

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/device510k' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q="continuous glucose monitor"' \
  --data-urlencode 's=decision.decision_date'
```

Each item in `results` includes `title`, `statementOrSummary`, `summaryText`, `kNumbersMentioned`, a `device` object (`kNumber`, `tradeName`, `deviceName`, `deviceClass`, `productCode`, `clearanceType`, `regulationNumber`, `medicalSpecialtyDescription`), a `decision` object (`decisionCode`, `decisionDescription`, `decisionDate`, `advisoryCommittee`, `expeditedReviewFlag`), and `applicantInformation`.

`s` accepts `_relevance` (default), `device.device_class`, `device.date_received`, and `decision.decision_date`.

## Search summary PDFs

```bash theme={null}
curl -G 'https://api.scite.ai/api_partner/evidence/device510k-summaries' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-urlencode 'q="predicate device" AND "insulin pump"'
```

Results are documents with `filename` and `attachments`; each attachment carries `pages` with extracted text (`content`), page counts, file metadata, and ontology `tags`/`categories`. Use this when the question is about what a submission actually says — predicate device claims, testing summaries, intended use — rather than the clearance metadata.

## Single record

`GET /api_partner/evidence/device510k/{device_id}` and `GET /api_partner/evidence/device510k-summaries/{item_id}` return one full record each.

## Common uses

* **Predicate research**: search summaries for a device type to find the predicate chains competitors cite; `kNumbersMentioned` on clearance records links related submissions.
* **Regulatory watch**: sort clearances by `decision.decision_date` and filter by product code or advisory committee to monitor a device category.
* **Full safety picture**: combine with MAUDE adverse-event reports (локальный ресурс исходного примера не включён) for post-market signals on the same devices.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
