> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: collections

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Collections

> Create collections of papers and monitor how their citations develop over time.

A **collection** is a set of papers you monitor over time. Collections alert you to new supporting or contradicting citations, flag retractions, and give you a living view of how a research area is developing. Use them to track your own publications, monitor another group's output, or stay on top of a field. A **dashboard** is a report on a collection.

Create collections from a list of DOIs or a search query through this API, via MCP (локальный ресурс исходного примера не включён), or in the Scite UI, which also imports from Zotero, Mendeley, or a CSV of DOIs. A collection created anywhere is available everywhere: use it as context in the UI, the API, or MCP.

## Working with collections

```bash theme={null}
curl -X POST 'https://api.scite.ai/api_partner/collections/create' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "My Review", "dois": ["10.1038/nature12373", "10.1126/science.1157784"]}'
```

If both `dois` and `query` are provided, `query` takes precedence.

| Endpoint | Purpose |
| - | - |
| `POST /api_partner/collections/create` | Create a collection from DOIs or a query |
| `GET /api_partner/collections/{collection_slug}` | Fetch a collection by slug |
| `PUT /api_partner/collections/{collection_slug}` | Update a collection |
| `DELETE /api_partner/collections/{collection_slug}` | Delete a collection |

Collection write operations (create/update/delete) require an API key with **write** scope; see Authentication (локальный ресурс исходного примера не включён).

<Note>
  If you get a `403 User not authorized` on a Collections call even with a valid key, your account may not have Collections access enabled. [Email sales](mailto:sales@scite.ai) to check.
</Note>

## Related

* Search guide (локальный ресурс исходного примера не включён): the `query` you can pass into a collection is the same search syntax
* Papers & Authors guide (локальный ресурс исходного примера не включён): look up the publications inside a collection by DOI
* Errors and rate limits (локальный ресурс исходного примера не включён): troubleshoot `401`, `403`, and retryable failures


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
