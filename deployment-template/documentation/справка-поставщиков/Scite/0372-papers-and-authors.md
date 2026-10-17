> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: papers-and-authors

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Papers & Authors

> Look up publication metadata by DOI or PMID, and author-level metadata and citation statistics.

These endpoints resolve a DOI or PMID to full metadata: title, abstract, authors with affiliations, journal, retraction status, and editorial notices. Pair with tallies (локальный ресурс исходного примера не включён) for citation data.

## Get a single paper

```bash theme={null}
curl 'https://api.scite.ai/papers/10.1038/nature12373' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

## Get multiple papers

```bash theme={null}
curl -X POST 'https://api.scite.ai/papers' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"dois": ["10.1038/nature12373", "10.1126/science.1157784"]}'
```

Up to 500 DOIs per request. A GET variant also exists for compatibility; prefer POST for larger lists.

## Resolve a PMID to a DOI

```bash theme={null}
curl 'https://api.scite.ai/papers/resolve-pmid/23851394' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

## Get papers citing a target

```bash theme={null}
curl 'https://api.scite.ai/papers/sources/10.1038/nature12373' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

## Author metadata

Look up an author's publications and aggregated citation statistics by author slug:

```bash theme={null}
curl 'https://api.scite.ai/authors/georg-kucsko-mvlovd/papers' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

| Endpoint | Purpose |
| - | - |
| `GET /authors/{author_slug}/papers` | Author metadata and papers |
| `GET /authors/{author_slug}/stats` | Aggregated citation statistics for the author |

<Note>
  `author_slug` isn't something you construct from a name, it's a Scite-generated identifier (name plus a random suffix, e.g. `georg-kucsko-mvlovd`). Get it from the `authorSlug` field on author objects returned by paper lookups](#get-a-single-paper) or [search (локальный ресурс исходного примера не включён) results. An unrecognized slug returns `404 {"detail": "Slug not found"}`.
</Note>

## Related

* Smart Citations guide (локальный ресурс исходного примера не включён): get tallies once you have a DOI
* Search and recommendations (локальный ресурс исходного примера не включён): discover related papers from a DOI
* Errors and rate limits (локальный ресурс исходного примера не включён): handle missing papers and invalid requests


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
