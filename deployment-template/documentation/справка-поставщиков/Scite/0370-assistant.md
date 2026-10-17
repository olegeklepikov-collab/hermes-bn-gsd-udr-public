> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: assistant

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Assistant

> Ask research questions and get answers backed by citation evidence.

The Assistant API answers research questions using Scite's citation evidence to ground its responses. Like Reference Check, it's a poll-based flow: submit a query, then poll for the result.

<Warning>
  Both endpoints require a key with the `assistant` scope, it isn't included by default on a self-service Pro key. If you get a `403`, [email sales](mailto:sales@scite.ai) to get the scope added, then generate a new key from the [API Console](https://scite.ai/users/me/api).
</Warning>

## 1. Start a query

```bash theme={null}
curl 'https://api.scite.ai/api_partner/assistant/poll' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  --data-raw '{
    "turns": [{"role": "user", "content": "How does the structure of a protein affect its function?"}],
    "user_input": "How does the structure of a protein affect its function?",
    "numReferences": 25,
    "answerLength": "medium",
    "citationStyle": "ieee"
  }'
```

For a single-turn question, `turns` needs only one object. Multi-turn conversations add more objects to the `turns` array.

The response is `{ "id": task_id }`.

## 2. Poll for the result

```bash theme={null}
curl 'https://api.scite.ai/api_partner/assistant/tasks/{task_id}' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

Poll until `status` is `SUCCESS`. While pending, the response's `info` field includes the currently generated content, search strategies, and search results so far, useful for streaming a "thinking" state to users.

Back off between polling requests and enforce an overall timeout. See Errors and rate limits (локальный ресурс исходного примера не включён).

## Useful parameters

| Parameter | Purpose |
| - | - |
| `alwaysUseReferences` / `neverUseReferences` | Force or suppress citation-backed answers |
| `abstractsOnly` / `fullTextsOnly` | Restrict the evidence pool |
| `yearFrom` / `yearTo` | Limit evidence by publication year |
| `topics`, `journals`, `publicationTypes` | Scope the evidence pool |
| `useStructuredResponse` | Enable **tables mode**: returns structured tabular output instead of prose |
| `rankBy` | Controls result ranking: see below |

### `rankBy` values

* `all`: a combination of the factors below (default)
* `relevance`: relevance to the query
* `date`: most recent first
* `citations`: by citation count
* `supporting-citations` / `contrasting-citations`: by supporting or contradicting citation count
* `journal-rank`: by journal rank/impact

## Related

* Reference Check guide (локальный ресурс исходного примера не включён): the same poll pattern, for evaluating a document's references instead of answering a question
* Errors and rate limits (локальный ресурс исходного примера не включён): retry and polling guidance


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
