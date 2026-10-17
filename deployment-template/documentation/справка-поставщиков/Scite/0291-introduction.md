> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: introduction

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Documentation

> Build tools to find, understand, and use scientific research with Scite.

Search papers and get more than titles and abstracts. See where they were cited, what later researchers said about them, and whether those citations support, challenge, or simply mention the work.

<CardGroup cols={2}>
  <Card title="Make your first request" icon="bolt" href="/quickstart">
    Retrieve a paper and its citation tally without an API key, then run an authenticated search.
  </Card>

  <Card title="Set up an agent" icon="robot" href="/agents">
    Give an AI agent Scite documentation and connect it through MCP or the REST API.
  </Card>
</CardGroup>

## Choose a path

Start with the route that matches what you are building.

<CardGroup cols={3}>
  <Card title="Public endpoints" icon="globe" href="/quickstart">
    Retrieve paper metadata and citation tallies without creating an account or API key.
  </Card>

  <Card title="REST API" icon="code" href="/authentication">
    Build applications, batch workflows, and direct integrations with scoped credentials.
  </Card>

  <Card title="Scite MCP" icon="plug" href="/mcp/overview">
    Give ChatGPT, Claude, or another MCP-compatible agent tools for working with research, or use the Article Galaxy connector for Microsoft 365 Copilot.
  </Card>
</CardGroup>

## Build with evidence

Most scholarly APIs provide metadata and citation counts. Scite adds the text and classification around citations, so you can see how later research has evaluated a publication.

| Capability | What it adds | Guide |
| - | - | - |
| **Literature search** | Search publication metadata and full-text citation statements with Boolean queries and more than 25 filters. | Search (локальный ресурс исходного примера не включён) |
| **Smart Citations** | See supporting, contradicting, mentioning, and unclassified citation statements. | Smart Citations (локальный ресурс исходного примера не включён) |
| **Paper enrichment** | Resolve DOIs and add publication, author, retraction, and citation data to a workflow. | Papers and Authors (локальный ресурс исходного примера не включён) |
| **Evidence datasets** | Search patents, grants, clinical trials, drugs, devices, adverse events, and safety alerts. | Evidence datasets (локальный ресурс исходного примера не включён) |

## Start in minutes

<Steps>
  <Step title="Try a public endpoint" icon="bolt">
    Retrieve a paper or citation tally without an account. Make your first request → (локальный ресурс исходного примера не включён)
  </Step>

  <Step title="Choose how to authenticate" icon="key">
    Use an API key for self-service development or managed credentials for an Enterprise integration. Compare credentials → (локальный ресурс исходного примера не включён)
  </Step>

  <Step title="Add Scite to your workflow" icon="rocket">
    Continue with the REST API, connect an agent through MCP, or [talk to sales](https://scite.ai/contact) about production and organization access.
  </Step>
</Steps>

## Explore the documentation

### Build

* Quickstart (локальный ресурс исходного примера не включён): make public and authenticated requests
* For agents (локальный ресурс исходного примера не включён): give AI agents documentation and Scite tools
* **API Reference**: inspect exact endpoints, parameters, and schemas

### Understand

* Citation model (локальный ресурс исходного примера не включён): understand sources, targets, tallies, and Smart Citation classifications
* Glossary (локальный ресурс исходного примера не включён): learn Scite terminology used across the API
* Pricing and plans (локальный ресурс исходного примера не включён): compare API, MCP, and organization access

### Operate

* Errors and rate limits (локальный ресурс исходного примера не включён): handle authentication, scopes, retries, and polling
* Enterprise access and SSO (локальный ресурс исходного примера не включён): configure institutional sign-in and managed access
* Changelog (локальный ресурс исходного примера не включён): follow documentation and API updates


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
