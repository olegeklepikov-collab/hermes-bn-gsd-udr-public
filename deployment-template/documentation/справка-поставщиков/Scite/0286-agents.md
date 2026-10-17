> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: agents

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# For agents

> Give ChatGPT, Claude, Microsoft 365 Copilot, and other AI agents access to Scite documentation and citation data.

Give an AI agent the context and tools it needs to search scientific literature, inspect citation evidence, and build with the Scite API.

This page covers the three ways to make Scite available to an agent: machine-readable documentation, the hosted MCP server, and direct REST API access.

## AI-accessible documentation

Scite publishes its documentation in formats that agents can read directly.

<CardGroup cols={2}>
  <Card title="llms.txt" icon="list" href="https://docs.scite.ai/llms.txt">
    A compact index that helps an agent discover the right guide or API area.
  </Card>

  <Card title="llms-full.txt" icon="file-lines" href="https://docs.scite.ai/llms-full.txt">
    The complete documentation in one file for tasks that need broad context.
  </Card>

  <Card title="OpenAPI specification" icon="file-code" href="https://docs.scite.ai/openapi.json">
    Exact REST endpoints, parameters, request bodies, and response schemas.
  </Card>

  <Card title="Copy a page" icon="copy" href="https://docs.scite.ai">
    Use **Copy page** on any guide when an agent only needs that page.
  </Card>
</CardGroup>

### Add Scite context to your agent

Add a short instruction like this to `AGENTS.md`, `CLAUDE.md`, or another context file your agent reads:

```markdown theme={null}
## Scite

Use Scite for scientific literature search and citation evidence.

- Documentation: https://docs.scite.ai/llms-full.txt
- API schema: https://docs.scite.ai/openapi.json
- Hosted MCP server: https://api.scite.ai/mcp

Use the API schema for exact fields and parameters. Do not infer response fields from examples.
```

Scite does not currently publish a separate installable skills package. The documentation and OpenAPI specification provide the agent context, while MCP or the REST API provides access to Scite data.

## Choose an integration

<CardGroup cols={2}>
  <Card title="Use Scite with MCP" icon="plug" href="/mcp/overview">
    Give an interactive agent ready-made tools for literature search, paper retrieval, Smart Citations, and Collections.
  </Card>

  <Card title="Build with the REST API" icon="code" href="/quickstart">
    Control requests, responses, retries, and persistent workflow logic in your own application.
  </Card>
</CardGroup>

## MCP

Connect an MCP-compatible client to Scite's hosted server:

```text theme={null}
https://api.scite.ai/mcp
```

ChatGPT, Claude, and most interactive MCP clients open Scite in a browser for authentication. Sign in and approve the connection; you do not need to create an API key. Microsoft 365 Copilot users can instead install [Article Galaxy for Copilot](https://marketplace.microsoft.com/en-us/product/WA200011900), a read-only Research Solutions connector that can retrieve available full text and Scite Smart Citation content.

Once connected, ask the agent naturally:

* "Find recent papers on CRISPR delivery and compare the approaches."
* "Check whether later studies support or contradict this DOI."
* "Save these papers to a collection for my review."

<CardGroup cols={3}>
  <Card title="Install Scite in ChatGPT" icon="messages" href="https://chatgpt.com/plugins/plugin_asdk_app_6952b3a3f1e881918951582d59483c78?q=scite">
    Install Scite, sign in, and use `@Scite` in a prompt.
  </Card>

  <Card title="Connect Scite to Claude" icon="sparkles" href="https://claude.ai/directory/connectors/scite">
    Add the Scite connector and sign in when Claude prompts you.
  </Card>

  <Card title="Use Article Galaxy in Copilot" icon="robot" href="https://marketplace.microsoft.com/en-us/product/WA200011900">
    Add the connector from Microsoft Marketplace and sign in with your Research Solutions account.
  </Card>
</CardGroup>

For Cursor, Claude Code, Gemini CLI, and other clients, see the MCP setup guide](https://scite.ai/mcp). For authentication details and programmatic MCP requests, see [Scite MCP (локальный ресурс исходного примера не включён).

## REST API

Choose the REST API when your application owns its requests, response handling, retries, and workflow state. Send requests to:

```text theme={null}
https://api.scite.ai
```

Start with the Quickstart (локальный ресурс исходного примера не включён) to make a public request and then an authenticated request. Use the **API Reference** tab for exact parameters and schemas.

Use an API key when an agent calls the REST API directly or when a programmatic MCP client cannot complete browser sign-in. Create and manage keys in the API Console](https://scite.ai/users/me/api). Grant only the scopes the integration needs, and see [Authentication (локальный ресурс исходного примера не включён) for credential and plan requirements.

Keep API keys out of source code, prompts, context files, command history, and logs. Store keys in a secret manager or environment variable and send them as bearer tokens.

## What agents can do with Scite

| Job | Start here |
| - | - |
| Search publication metadata and citation context | Search (локальный ресурс исходного примера не включён) |
| Find supporting or contradicting evidence | Smart Citations (локальный ресурс исходного примера не включён) |
| Retrieve paper and author metadata | Papers and Authors (локальный ресурс исходного примера не включён) |
| Work with saved sets of papers | Collections (локальный ресурс исходного примера не включён) |
| Screen a manuscript bibliography | Reference Check (локальный ресурс исходного примера не включён) |
| Search patents, trials, grants, and regulatory records | Evidence datasets (локальный ресурс исходного примера не включён) |

## Before you ship

* Treat `401` as a credential problem and `403` as an access or scope problem.
* Retry `429` and transient `5xx` responses with exponential backoff and jitter.
* Read returned rate-limit headers instead of hard-coding a request rate.
* Use the response schema in the **API Reference** tab instead of inferring fields from examples.
* Confirm that your plan and agreement cover the intended use. See Pricing and plans (локальный ресурс исходного примера не включён).

See Errors and rate limits (локальный ресурс исходного примера не включён) for retry behavior, asynchronous polling, and production guidance.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
