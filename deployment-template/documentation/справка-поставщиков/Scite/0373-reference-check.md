> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: reference-check

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference Check

> Submit a document and have its references evaluated and linked using Scite's data.

Reference Check takes a document (PDF or DOCX), extracts its references, and evaluates each one against Scite's citation data. It surfaces retractions, contradicting citations, and other flags associated with the cited sources. This is an asynchronous, poll-based flow.

<Warning>
  Reference Check requires a paid license and isn't included in a standard self-service Pro key. [Email sales](mailto:sales@scite.ai) to get access, then generate a new key from the [API Console](https://scite.ai/users/me/api) once it's enabled on your account.
</Warning>

## 1. Submit the document

You can either upload the file directly or point to a URL:

```bash theme={null}
# Upload directly
curl -X POST 'https://api.scite.ai/reference_check' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -F 'file=@paper.pdf'
```

```bash theme={null}
# Or reference a URL
curl -X POST 'https://api.scite.ai/reference_check' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com/paper.pdf"}'
```

The response contains a task ID:

```json theme={null}
{ "id": "task_123" }
```

## 2. Poll for the result

```bash theme={null}
curl 'https://api.scite.ai/reference_check/tasks/task_123' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

Poll until the task status is no longer pending. The response includes the current state and, once complete, the evaluated references.

Back off between polling requests and enforce an overall timeout. See Errors and rate limits (локальный ресурс исходного примера не включён).

<Note>
  An unrecognized or mistyped `task_id` doesn't return a 404, it returns `200 {"status": "PENDING"}` just like a real in-progress task. Hold onto the exact ID from the submit response rather than reconstructing it, or you can end up polling a task that will never complete.
</Note>

## Other task operations

| Endpoint | Purpose |
| - | - |
| `GET /reference_check/tasks/{task_id}/cancel` | Cancel a running task |
| `GET /reference_check/tasks/{task_id}/result_url` | Get a direct URL to the result, instead of the inline payload |

## Related

* Assistant guide (локальный ресурс исходного примера не включён): a similar poll-based flow for Q\&A instead of reference evaluation
* Errors and rate limits (локальный ресурс исходного примера не включён): retry and polling guidance


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
