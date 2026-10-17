> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: access-querying

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

There are several ways to ask OpenAlex a question, each suited to a different kind of user: point-and-click on the website, a raw REST URL, the OpenAlex Query Language, the command line, or an AI agent. Pick whichever fits how you like to work.

Here's the key idea that ties them together: **every one of these surfaces transpiles to the same canonical query object internally — the OpenAlex Query Object, or OQO.** A click in the web interface, a `filter=` string in a URL, and a line of OQL all compile down to the same OQO and run against the same engine. That means they're **equivalent in power**, up to the limits of each surface — the differences below are about ergonomics and reach, not about which one can "really" ask the question.

## The ways to query, compared

| Way | Best for | Tradeoffs |
|---|---|---|
| [**Web (basic)**](https://help.openalex.org/access/website-basic/): point-and-click search and filters on the OpenAlex website | Non-technical users; quick one-off questions; browsing and exporting | Easiest to learn; a friendly subset — not every query shape is expressible |
| [**Web (advanced)**](https://help.openalex.org/access/website-advanced/): the visual query builder | Complex filters without writing code; systematic reviews | More expressive than basic; covers the common shapes, not every valid query |
| [**URL**](https://help.openalex.org/access/url/): traditional REST API parameters | Programmatic access; scripts; sharing a query as a link | Fast and well-documented; classic URL syntax can't express deep nesting or cross-field OR |
| [**OQL**](https://help.openalex.org/access/oql/): the OpenAlex Query Language | Modeling complex queries — and sharing them in a form people can actually read | Most expressive by hand; a new syntax to learn |
| [**CLI**](https://help.openalex.org/access/cli/): query from your terminal | Terminal workflows; automation; feeding your own tools | Scriptable and composable; requires the command line |
| [**AI agent connector**](https://help.openalex.org/how-to/ai-assistants/): add OpenAlex to Claude and ask in plain language | Most everyday questions, if you use Claude; free to add, ChatGPT version coming soon | No syntax to learn; Claude shows the OQL it ran, so you can check or rerun it |
| [**Agents**](https://help.openalex.org/access/agents/): tell your AI agent to use OpenAlex | Letting an agent do the whole job for you | No syntax to learn; best to verify consequential results yourself |

## Where to go next

- **[Website](https://help.openalex.org/access/website-basic/)** — the no-code way. Start with [basic](https://help.openalex.org/access/website-basic/) search and filters, and move to [advanced](https://help.openalex.org/access/website-advanced/) when you need more.
- **[REST URLs](https://help.openalex.org/access/url/)** — query by URL against `api.openalex.org`. The [API](https://help.openalex.org/api/) tab documents the wire mechanics in full.
- **[OQL](https://help.openalex.org/access/oql/)** — the OpenAlex Query Language, a readable way to express queries the classic URL syntax can't.
- **[CLI](https://help.openalex.org/access/cli/)** — query from your terminal.
- **[AI agent connector](https://help.openalex.org/how-to/ai-assistants/)**: in Claude, the easiest way. Add it free and ask in plain language.
- **[Agents](https://help.openalex.org/access/agents/)** — hand the whole job to an AI agent.

For the underlying HTTP mechanics — endpoints, parameters, paging, and rate limits — see the [API](https://help.openalex.org/api/) tab.
