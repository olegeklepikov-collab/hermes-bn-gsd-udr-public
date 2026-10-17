> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: access-overview

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Overview

There are many ways to get OpenAlex data, from point-and-click to whole-database. They all serve the same knowledge graph — the difference is how much you take, how fresh it is, how much technical skill it takes, and what it costs. This page helps you pick.

| Product | Best for | Technical skill | Cost |
|---|---|---|---|
| [Website](https://help.openalex.org/access/website-basic/) | Exploring, one-off questions, exporting result lists | None | Free |
| [AI agent connector](https://help.openalex.org/access/connector/) | Asking Claude in plain language to do most of what the website and API do; it can also fix your author profile. ChatGPT version coming soon | None | Free to add; queries use your own [daily budget](https://help.openalex.org/access/pricing/) |
| [Other agents](https://help.openalex.org/access/agents/) | Setting up any other AI agent (ChatGPT, Cursor, coding agents) to query OpenAlex through the API | None | Free tier, then [usage pricing](https://help.openalex.org/access/pricing/) |
| [API](https://help.openalex.org/api/) | Apps, scripts, and analyses that need live data | Some coding | $1/day free, then [usage pricing](https://help.openalex.org/access/pricing/) |
| [CLI](https://help.openalex.org/access/cli/) | Bulk downloads from your terminal, with retries and resume built in | Command line | Same as the API |
| [Snapshot](https://help.openalex.org/access/snapshot/) | Your own copy of the entire database, updated quarterly ([release dates](https://help.openalex.org/access/sync/#public-release-dates)) | Data engineering | Free |
| [Sync](https://help.openalex.org/access/sync/) | Keeping your copy fresh with daily updates | Data engineering | [Member+ and Partner plans](https://help.openalex.org/access/pricing/) |
| [Fulltext](https://help.openalex.org/access/fulltext/) | Full-text PDFs and TEI XML, per-file or the whole archive | Varies by option | $0.01/file; full archive via the [PDF sync add-on](https://help.openalex.org/access/pricing/#the-pdf-sync-add-on) |
| [Unpaywall](https://help.openalex.org/access/unpaywall/) | Legacy Unpaywall integrations and OA lookups by DOI | Some coding | Free |

## Picking a product

**Just exploring?** Use the [website](https://help.openalex.org/access/website-basic/) — search, filter, and export without writing a line of code. If you use Claude, the free [OpenAlex connector](https://help.openalex.org/how-to/ai-assistants/) lets you skip the clicking: ask in plain language and Claude runs the searches for you. Any other AI assistant can [use OpenAlex](https://help.openalex.org/access/agents/) too.

**Building something?** The [API](https://help.openalex.org/api/) is the workhorse: fast, well-documented, and free for most uses — every account gets $1 of usage per day, which covers most research and personal projects. When you outgrow it, [usage pricing](https://help.openalex.org/access/pricing/) is pay-as-you-go. The [CLI](https://help.openalex.org/access/cli/) wraps the same API for bulk work in your terminal, handling parallelism, checkpointing, and resume for you.

**Want the whole database?** The [snapshot](https://help.openalex.org/access/snapshot/) is the entire dataset, free to download, refreshed quarterly on the second Wednesday of January, April, July and October ([release dates](https://help.openalex.org/access/sync/#public-release-dates)). If quarterly isn't fresh enough, [sync](https://help.openalex.org/access/sync/) gets you a complete daily snapshot plus API filters for everything new or changed since any date — a benefit of the Member+ and Partner [plans](https://help.openalex.org/access/pricing/). (Only mirroring a slice of OpenAlex, like your own institution's works? Those [API filters](https://help.openalex.org/access/sync/#premium-api-filters-paid-plans) can keep a subset fresh with no snapshot infrastructure at all.)

**After the documents themselves?** [Fulltext](https://help.openalex.org/access/fulltext/) covers the content archive — more than 50 million open-access PDFs and their machine-readable TEI XML — from single-file downloads up to syncing the complete archive to your own bucket.

However you get it, the data itself is free and open under [CC0](https://creativecommons.org/public-domain/cc0/) — what costs money at the higher tiers is the *service* of serving and refreshing it. That story, and every plan, lives in [Pricing](https://help.openalex.org/access/pricing/).
