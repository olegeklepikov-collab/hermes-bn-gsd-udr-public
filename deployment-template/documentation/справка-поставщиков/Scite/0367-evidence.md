> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: evidence

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evidence tools

> Search patents, clinical trials, grants, FDA device and drug records, adverse events, and safety alerts through MCP.

Seventeen MCP tools cover Scite's evidence datasets — the same records as the Evidence API (локальный ресурс исходного примера не включён), reachable from a conversation.

Requires Pro, or the dataset's `evidence:<dataset>:mcp` scope. Accounts on an organization license need the explicit entitlement even at Pro; [email sales](mailto:sales@scite.ai) to add one.

## The shared pattern

Every dataset follows the same two-tool shape: a `search_*` tool that returns slim results, and a `get_*` tool that returns the full record for one id.

Search results are deliberately trimmed to save model context. Call the `get_*` tool only when you need a field the search result doesn't already carry — the per-dataset sections below say what each one adds.

All search tools share the same parameters:

| Parameter | Type | Description |
| - | - | - |
| `q` | string | Free-text query. Supports `AND`, `OR`, `NOT`, and `"exact phrase"` |
| `f` | string | Space-delimited field filters in `field:"value"` format |
| `p` | integer | Page number. Default `1` |
| `s` | string | Sort field. Default `_relevance` |
| `sortDir` | string | `asc` or `desc`. Default `desc`; ignored when `s` is `_relevance` |

<Note>
  This is the Evidence query syntax, not the Search syntax. `search_literature` uses named parameters and `limit`/`offset`; Evidence tools use `q`/`f` and page numbers. See Evidence overview (локальный ресурс исходного примера не включён).
</Note>

Four tools — `search_510k_summaries`, `search_mhra`, `search_faers`, and `search_drugs` — sort by relevance only and accept no `s` or `sortDir`.

### Date range filters

Datasets with date fields accept two equivalent notations. Note there is no space before the `gte`/`lt` suffix.

```text theme={null}
date_receivedgte:"2024-01-01" date_receivedlt:"2024-07-01"
date_received:"2024-01-01,2024-07-01"
```

Accepted formats are `YYYY-MM-DD`, ISO datetimes, and epoch milliseconds.

## Patents

`search_patents` returns patent families with titles, abstracts, inventors, assignees, classifications, filing status, and citation counts.

Sort fields: `_relevance`, `forwardCitationCount`, `familySize`, `patents.publications.pubRef.date`, `patents.appRef.filingDate`.

```json theme={null}
{
  "name": "search_patents",
  "arguments": {
    "q": "CRISPR gene editing",
    "f": "assignee:Pfizer filing_status:granted",
    "s": "forwardCitationCount"
  }
}
```

There's no `get_patent` tool — search returns the full family record.

## Clinical trials

`search_clinical_trials` covers ClinicalTrials.gov. Results carry `nctId`, `title`, `briefDescription`, `phase`, `sponsors`, `facilities`, `conditions`, `interventions`, `tags`, `startDate`, `completedDate`, and `publicationCount`. Matched fields come back wrapped in `<strong>` tags.

Sort fields: `_relevance`, `dates.startDate`, `dates.completedDate`, `dates.lastUpdatedDate`.

```json theme={null}
{
  "name": "search_clinical_trials",
  "arguments": {
    "q": "pancreatic cancer",
    "f": "conditions:\"Cancer\" trialState.phase:\"Phase III\""
  }
}
```

`get_clinical_trial` takes an NCT id such as `NCT02986230` and adds the full `description`, study `design`, `enrollment`, primary and secondary `outcomes`, complete `eligibility` criteria, `reportedEvents` (posted adverse events), principal investigator, `contacts`, `citations`, and `resultsUrl`. Use it for deeper analysis or patient-trial matching.

## Grants

`search_grants` spans NIH RePORTER, NSF, SBIR/STTR, Wellcome, EU funders, and more. Results carry `id`, `title`, an abstract preview, `agency`, `organization`, `piName`, `country`, award dates, `awardAmount`, `tags`, `groupSlug`, and `grantsInGroup`.

Sort fields: `_relevance`, `awardStartDate`, `awardCloseDate`, `awardNoticeDate`, `awardAmount`, `employeeCount`.

<Warning>
  Related grants are grouped — NIH subprojects of one center grant, or renewals of the same award. Search returns **one representative grant per group**. `grantsInGroup` gives the group size and `siblingGrantIds` lists the others. To pull a sibling, call `get_grant` with its id rather than searching again.
</Warning>

`get_grant` takes an id such as `5201339`, `nsf.0646294`, or `wellcome.214402.Z.18.Z`. Call it for two things only:

* The full `abstract`. Search returns a \~300-character highlighted preview; the full text usually runs 1–3 KB.
* Source-specific identifiers absent from search: `awardYear`, `agencyTrackingNumber`, `contract`, `nihProgramCode`, `nihrApplicationId`.

Everything else is already in the search result.

## Device clearances

The 510(k) dataset splits across two pairs of tools, and the distinction matters.

| Question | Tool |
| - | - |
| Which devices were cleared, by whom, in what class? | `search_device510k` |
| What did the submission actually say? | `search_510k_summaries` |

`search_device510k` returns structured clearance metadata: `kNumber`, `title`, `summaryText`, device info (name, class, product code, clearance type, regulation number), decision info (code, description, date, committee), applicant details, and tags.

Sort fields: `_relevance`, `device.device_class`, `device.date_received`, `decision.decision_date`.

`get_device510k` takes a K number such as `K210674` and adds the complete `summaryText`, full applicant details (address, contact, country), `registration` info (FEI and registration numbers), and the full `decision` object.

`search_510k_summaries` searches OCR'd full text from 510(k) summary PDFs and returns page-level snippets. Reach for it when the question is about submission *content*: test results, performance data, biocompatibility, substantial equivalence reasoning, indications for use, predicate comparisons, sterilization methods, software descriptions, or bench testing.

`get_510k_summary` takes a document id — also a K number, e.g. `K192757` — and returns the full extracted text organized by page.

## Adverse events

Two separate FDA systems: MAUDE for devices, FAERS for drugs.

### MAUDE (devices)

`search_maude` returns device adverse-event reports with `id`, `title`, `reportNumber`, `eventType`, `adverseEventFlag`, `productProblems`, device info, `patientProblems`, dates, and narrative snippets.

Facet fields for `f`: `event_type`, `device.device_class`, `device.manufacturer_d_name`, `device.device_report_product_code`, `device.regulation_number`, `report_source_code`, `product_problems`, `patient.problems`. Date fields: `date_received`, `date_report`.

Sort fields: `_relevance`, `date_received`, `date_report`.

```json theme={null}
{
  "name": "search_maude",
  "arguments": {
    "q": "infusion pump",
    "f": "event_type:\"Death\" device.manufacturer_d_name:\"Medtronic\" date_receivedgte:\"2024-01-01\"",
    "s": "date_received"
  }
}
```

`get_maude_report` takes a report id such as `17343805` and returns the full MDR narrative entries with their text type codes, reporter occupation, health professional flag, device medical specialty and availability, and patient treatment. Search truncates these narratives; the detail tool doesn't.

### FAERS (drugs)

`search_faers` returns drug adverse-event and medication-error reports. Each links suspect and concomitant drugs to observed patient reactions as MedDRA preferred terms. Results carry `safetyReportId`, `title`, `reportType`, `serious`, `seriousnessType`, `receiveDate`, `occurCountry`, `reactions`, and `drugs`.

Facet fields for `f`: `drug.medicinalproduct`, `drug.brand_name`, `drug.generic_name`, `drug.substance_name`, `drug.manufacturer_name`, `drug.drugindication`, `drug.pharm_class_epc`, `drug.pharm_class_moa`, `reaction.reactionmeddrapt`, `reaction.reactionoutcome`, `event.reporttype`, `event.seriousness_type`, `event.occurcountry`, `event.patientsex`, `primarysource.qualification`, `primarysource.reportercountry`. Date fields: `event.receivedate`, `event.receiptdate`, `drug.drugstartdate`, `drug.drugenddate`.

FAERS sorts by relevance only.

`get_faers_report` takes a safety report id such as `26185565` and adds patient demographics (sex, age group, onset age, weight, death date), report dates, the expedited flag, `primarySource` (reporter qualification and country), `reportDuplicates`, and enriched drug records with dosage text, start and end dates, NDC, application number, and pharmacologic class.

## Drugs

`search_drugs` covers FDA Structured Product Labels, the Orange Book, and Drugs\@FDA. Each result bundles an FDA application — approved products, applicant, approval dates, marketing status — with its Structured Product Label.

Facet fields for `f` include `labels.brand_name`, `labels.generic_name`, `labels.substance_name`, `labels.manufacturer_name`, `labels.product_type`, `labels.route`, `labels.pharm_class_epc`, `labels.pharm_class_moa`, `labels.pharm_class_cs`, `labels.rxcui`, `labels.unii`, `labels.product_ndc`, `labels.package_ndc`, `application.application_number`, `application.sponsor_name`, `application.products.marketing_status`, `application.products.dosage_form`, `application.products.route`, `application.products.te_code`, `tags`, and `categories`. Date fields: `labels.effective_time`, `application.products.approval_date`.

Sorted by relevance only.

`get_drug` takes the record UUID from search results, e.g. `${OBJECT_ID}`. It adds every approved product (product number, applicant, approval date, dosage form, route, active ingredients, TE code) and the main label sections: indications and usage, dosage and administration, contraindications, boxed warning, warnings and cautions, adverse reactions, drug interactions, use in specific populations, pharmacology, clinical studies, how supplied, overdosage, and description.

## Safety alerts

`search_mhra` covers UK MHRA drug safety alerts, medical device alerts, field safety notices, and regulatory publications, searching headlines, descriptions, and page-level document content. Results carry `id`, `headline`, `description`, `tags`, `categories`, `date`, and matching content snippets.

Facet fields for `f`: `ontology.tags`, `ontology.categories`, `domain`. Date fields: `attachments.file.createdAt`, `attachments.file.modifiedAt`. Sorted by relevance only.

```json theme={null}
{
  "name": "search_mhra",
  "arguments": {
    "q": "immunosuppressant",
    "f": "attachments.file.createdAtgte:\"2025-10-01\" attachments.file.createdAtlt:\"2026-01-01\""
  }
}
```

`get_mhra_alert` takes a document id from search results and returns the complete alert: headline, description, the full article body (`contentHtml`), tags, and per-page content.

## Related

* Evidence API guides (локальный ресурс исходного примера не включён): the same datasets over HTTP, with per-dataset filter references
* Tool reference (локальный ресурс исходного примера не включён): the full catalog and access requirements
* Errors and rate limits (локальный ресурс исходного примера не включён): retry guidance


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
