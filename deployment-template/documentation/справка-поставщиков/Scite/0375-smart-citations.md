> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: smart-citations

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Citations

> Get tallies, browse the citation graph, and look up journal-level Smart Citation data.

A citation count says a paper was cited 400 times. A Smart Citation tally says how many of those citations support the finding, contradict it, or mention it. These endpoints return that breakdown for any DOI, the citing papers behind it, and the section where each statement appears. See Citations & Tallies (локальный ресурс исходного примера не включён) for the difference between a tally count and a citing-publications count.

**Need an API key?** On Pro, create one in the API Console](https://scite.ai/users/me/api). Creating a key doesn't grant every optional scope; see [Authentication (локальный ресурс исходного примера не включён) for feature access. For higher limits or managed credentials, [contact sales](https://scite.ai/contact).

## Get a tally for one DOI

```bash theme={null}
curl 'https://api.scite.ai/tallies/10.1038/nature12373' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

## Get tallies for many DOIs

```bash theme={null}
curl -X POST 'https://api.scite.ai/tallies' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"dois": ["10.1038/nature12373", "10.1126/science.1157784"]}'
```

Up to 500 DOIs per request. A GET variant of this endpoint also exists for compatibility, but POST is recommended for larger DOI lists.

<Tip>
  **Want a ready-made display?** The [Scite Badge](https://scite.ai/badge) embeds Citation Type or paper-section tallies for a DOI. It is free for personal use or for works you authored. Organizations should [contact Scite](mailto:customersupport@researchsolutions.com) before using it. Use the Tallies API when you need a custom interface or high-volume integration.
</Tip>

## Tallies by section

Citations occurring in the Introduction carry different weight than citations in the Discussion. `GET /tallies/cited-by-sections/{doi}` (and the bulk `POST /tallies/cited-by-sections`) breaks the tally down by the section of the citing paper where the statement appears.

## Browsing the citation graph

Rather than a tally, you can retrieve the actual citing/cited publications:

| Endpoint | Returns |
| - | - |
| `GET /api_partner/citations/citing/{doi}` | Sources that cite this DOI as a target |
| `GET /api_partner/citations/cited_by/{doi}` | Targets cited by this DOI as a source |
| `GET /api_partner/references/references_to/{doi}` | Distinct references *to* this publication |
| `GET /api_partner/references/references_from/{doi}` | Distinct references *from* this publication |

Citation Graph responses contain `metadata` and a `citations` array:

```json theme={null}
{
  "metadata": {},
  "citations": [
    {
      "source": "10.1000/source-doi",
      "target": "10.1000/target-doi",
      "type": "supporting",
      "section": "discussion"
    }
  ]
}
```

<Warning>
  A highly cited DOI can return thousands of citation records. Use `limit` with `offset` to page through graphs that exceed 3,000 records, and avoid fetching the full graph when a tally is sufficient.
</Warning>

## Journal-level data

* `GET /journal/{issn}/tallies`: Smart Citation tallies aggregated for an entire journal
* `GET /journal/{issn}/yearly-si`: the Scite Journal Index (SJI) broken down by year
* `GET /issn-sji` / `POST /issn-sji-bulk`: look up the Scite Journal Index for one or many ISSNs

<Note>
  Journal-level tallies use different field names than DOI-level tallies: `totalCites`, `totalSupportingCites`, `totalContrastingCites`, `totalMentioningCites`, and `totalUnclassifiedCites`, rather than `total`, `supporting`, `contradicting`, `mentioning`, and `unclassified`. Don't assume the two shapes match.
</Note>

## Related

* Search guide (локальный ресурс исходного примера не включён): filter by tally signals like `has_tally` or `supporting_from`
* Citations & Tallies (локальный ресурс исходного примера не включён): the underlying data model
* Errors and rate limits (локальный ресурс исходного примера не включён): authentication, scope, and retry guidance


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
