> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: resources--memory

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Parallel Memory to Build on Past Research

> Let your agents search and reuse past Task, Monitor, and FindAll results so new research builds on work you have already done.

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

Memory lets your agents build on research you've already done with Parallel.

When you use Parallel personally — through the CLI (локальный ресурс исходного примера не включён), or
third-party agents like Claude Code (локальный ресурс исходного примера не включён) — your agents can search past
Task, Monitor, and FindAll results and reference them in new work.

This personal memory never changes the results of Task, FindAll, Monitor, or other API requests.

<Note>
  We're gradually rolling out memory over the coming weeks. As part of this rollout, memory will be
  enabled by default for some newly created organizations.
</Note>

## How memory works

Once memory is enabled, the inputs and outputs of supported Parallel runs are saved to your
personal memory.

When your agent starts new research, it can choose to search your memory for relevant past work.
Memory is never used automatically — your agent must explicitly retrieve it.

Only you and your personal agents can access your personal memory, and it follows you across the
agents that you use.

### Memory example

| # | Task request | Without memory | With memory |
| :- | :- | :- | :- |
| 1 | "Research the latest trends in data center buildouts in the midwest" | Parallel conducts a research task against the web to find data centers in the midwest. | Same as without memory — this is the first run, so there is nothing to build on. |
| 2 | "Which data centers came online in Ohio recently?" | Parallel conducts a research task against the web to find data centers in Ohio. | Agent decides the previous query contains enough information to answer without further research. |

## Manage personal memory

Personal memory is on by default once memory is enabled for your organization. Members can turn it
off under **Settings → Account**.

Your account settings show the account keys that contribute to your personal memory.

When memory is turned off, new memories will not be created. Existing memories are retained and
become available again if memory is turned back on.

You can also permanently delete your personal memory. This cannot be undone.

## Organization controls

Organization admins manage memory under **Settings → Organization**.

The organization setting controls whether members can use personal memory.

Turning memory off stops new personal memories from being created. Existing personal and application
memories are retained until they are permanently deleted.

Admins can permanently delete all personal and application memory. This cannot be undone.

## Taking advantage of memory

Use the [memory API](#api-reference) to take advantage of memory. Access the API using the
Parallel CLI (локальный ресурс исходного примера не включён) or the Parallel skill (локальный ресурс исходного примера не включён).
Update to the latest version of the Parallel CLI:

```bash theme={"system"}
parallel-cli update
```

Update to the latest version of the skill:

```bash theme={"system"}
parallel-cli skills install
```

Ask your agents to "check what I've already researched with Parallel before starting."

## Building applications with memory

If you're a developer building on Parallel, you can also create application-scoped memory.

Application memory is opt-in per request. Runs are saved only when your application provides a
`memory_scope_key`. Each `memory_scope_key` maps to its own isolated memory bank.

You can set `memory_scope_key` when creating a Task run (локальный ресурс исходного примера не включён), a
FindAll run (локальный ресурс исходного примера не включён), or a
Monitor (локальный ресурс исходного примера не включён).

## API reference

| Endpoint | Description |
| :- | :- |
| Retrieve Memory (локальный ресурс исходного примера не включён) | Search memories created by past Task, Monitor, and FindAll runs. |
| Evict from Memory (локальный ресурс исходного примера не включён) | Remove a specific source from a memory bank. |
| Clear Memory (локальный ресурс исходного примера не включён) | Permanently delete the contents of a memory bank. |
