> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: prompts

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompts

> Prebuilt research workflows the Scite MCP server ships, ready to invoke from any MCP client.

Alongside its tools, the Scite MCP server exposes four prompts — prebuilt, parameterized workflows that walk a model through a research task using the Scite tools. Clients that support MCP prompts surface them as slash commands, templates, or a picker.

Prompts are workflows, not tools. Retrieving one returns instructions for the model to follow; it doesn't call anything by itself. The steps inside then use `search_literature` (локальный ресурс исходного примера не включён).

## The prompts

| Name | Arguments | What it does |
| - | - | - |
| `literature-review` | `topic` (required), `focus` | Runs a structured, cited literature review on a topic |
| `fact-check-claim` | `claim` (required) | Verifies a scientific claim and flags unsupported statements |
| `systematic-review-screen` | `research_question` (required), `inclusion_criteria` | Screens the literature against inclusion criteria |
| `verify-bibliography` | `reference` (required) | Confirms a reference's metadata against Scite |

Optional arguments may be left blank. Omitting a required argument returns JSON-RPC error `-32602`.

### literature-review

Plans several `search_literature` queries using domain vocabulary and Boolean operators, reads the most relevant papers section by section with targeted `term` queries, checks editorial notices before citing anything, synthesizes themes and contradictions across the set, and closes with an APA reference list.

Pass `focus` to emphasize an angle — `clinical outcomes`, `methods`, and so on.

### fact-check-claim

Breaks a claim into its key assertions, searches for each, reads Smart Citation snippets and full-text excerpts, compares what the papers actually report against the claim, and returns a verdict of supported, partially supported, unsupported, or contradicted, with references.

### systematic-review-screen

Builds a comprehensive query set covering synonyms and Boolean variants, assesses each candidate paper against your criteria, and records an include or exclude decision per paper with a one-line rationale.

Pass `inclusion_criteria` to specify population, study type, date bounds, or anything else that governs the screen.

### verify-bibliography

Parses a reference into its fields, looks it up — preferring `dois`, then `titles`, then a `term` query built from title and first author — and reports matches and discrepancies: wrong year, omitted authors, misattributed journal, incorrect or missing DOI. It also checks for retractions, since a citation can be accurate and still point to a withdrawn paper. If no record matches, it says so rather than guessing.

## Using prompts

**Need an API key?** On Pro, create one in the API Console](https://scite.ai/users/me/api). Creating a key doesn't grant every optional scope; see [Authentication (локальный ресурс исходного примера не включён) for feature access. For higher limits or managed credentials, [contact sales](https://scite.ai/contact).

### Discover them

```bash theme={null}
curl -X POST 'https://api.scite.ai/mcp' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "prompts/list"
  }'
```

Each entry returns `name`, `title`, `description`, and `arguments`.

### Retrieve one

```bash theme={null}
curl -X POST 'https://api.scite.ai/mcp' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": "2",
    "method": "prompts/get",
    "params": {
      "name": "fact-check-claim",
      "arguments": {
        "claim": "Vitamin D supplementation reduces the risk of respiratory infection."
      }
    }
  }'
```

The response is the rendered prompt, with your arguments substituted, ready to send to a model.

## A shared discipline

All four prompts enforce the same rules, which are worth applying to any Scite MCP workflow you write yourself:

* Cite only papers actually retrieved through the tools — never from model memory.
* Quote full-text excerpts and Smart Citation snippets as evidence rather than paraphrasing them away.
* Check `editorialNotices` for retractions and corrections before citing any paper.
* Read papers incrementally with `dois` plus targeted `term` queries instead of pulling large result sets.
* End with an APA reference list.

## Related

* Literature tools (локальный ресурс исходного примера не включён): the tool every prompt is built on
* Scite MCP (локальный ресурс исходного примера не включён): setup, authentication, and protocol
* Smart Citations guide (локальный ресурс исходного примера не включён): how the evidence these prompts quote is classified


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
