> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: errors-and-rate-limits

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Errors and rate limits

> Handle authentication failures, missing scopes, invalid requests, and rate limits.

Scite returns JSON error responses with a `detail` field. Use the HTTP status code to decide whether to change the request, update access, or retry.

## Common errors

| Status | Meaning | What to do |
| - | - | - |
| `401 Unauthorized` | The endpoint requires authentication, but the request has no valid credential. | Add or replace the `Authorization: Bearer <YOUR_API_KEY>` header. |
| `403 User not authorized` | The credential is valid, but the key or account lacks the required scope. | Check the key's scopes in the API Console. If the scope isn't available, contact sales. |
| `404` | The requested DOI, task, collection, or other resource wasn't found. | Check the identifier. Don't retry the same value unchanged. |
| `422` | A parameter or request body failed validation. | Use the response details to correct the field name, type, or format. |
| `429` | The request exceeded a rate limit. | Wait for the indicated reset, then retry with backoff. |

For example, Search without a key returns:

```json theme={null}
{
  "detail": "Unauthorized"
}
```

A valid key without the required feature scope returns:

```json theme={null}
{
  "detail": "User not authorized"
}
```

## Rate limit headers

Authenticated responses expose the current short-window limit through `RateLimit-*` headers and the minute limit through `X-RateLimit-*-Minute` headers:

```text theme={null}
RateLimit-Limit: <short-window-limit>
RateLimit-Remaining: <short-window-remaining>
RateLimit-Reset: <seconds-until-reset>
X-RateLimit-Limit-Minute: <minute-limit>
X-RateLimit-Remaining-Minute: <minute-remaining>
```

Limits vary by endpoint and account. Read the headers instead of hard-coding a request rate.

## Retry safely

* Don't retry `401`, `403`, `404`, or `422` responses without changing the credential or request.
* For `429` and transient `5xx` responses, use exponential backoff with jitter.
* Honor `Retry-After` when the response includes it. Otherwise wait until the indicated rate-limit reset.
* Set a maximum retry count and an overall timeout.
* Avoid retrying write requests unless your application can prevent duplicate changes.

## Polling asynchronous tasks

Assistant and Reference Check return a task ID that you poll for results. Don't poll in a tight loop. Back off between requests, enforce an overall timeout, and preserve the exact task ID returned by the submit request.

See the Assistant guide (локальный ресурс исходного примера не включён) and Reference Check guide (локальный ресурс исходного примера не включён) for their task flows.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
