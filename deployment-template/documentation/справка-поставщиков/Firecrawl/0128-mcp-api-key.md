> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: mcp-api-key

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/mcp-server/keyless

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/mcp-server/keyless#content-area)

## [​](https://docs.firecrawl.dev/mcp-server/keyless\#try-keyless)  Try keyless

### Set up Firecrawl MCP

No API key required. Add an API key to unlock more usage.

![](https://docs.firecrawl.dev/images/agent-clients/codex.svg)**ChatGPT & Codex** Run in terminal![](https://docs.firecrawl.dev/images/agent-clients/claude-code.svg)**Claude & Claude Code** Run in terminal![](https://docs.firecrawl.dev/images/agent-clients/cursor.svg)**Cursor** One click![](https://docs.firecrawl.dev/images/agent-clients/opencode.svg)**OpenCode** Copy config

Run this in your terminal to add Firecrawl as a remote MCP server in Codex CLI.

$`codex mcp add firecrawl --url https://mcp.firecrawl.dev/v2/mcp`

Copy

Then run `codex mcp list` and confirm **firecrawl** is enabled.

Run this in your terminal to add Firecrawl as a remote MCP server in Claude Code.

$`claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp`

Copy

Then run `/mcp` and confirm **firecrawl** is connected.

Install the hosted MCP server in one click, or copy the configuration below.

[![](https://docs.firecrawl.dev/images/agent-clients/cursor.svg)Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJ1cmwiOiJodHRwczovL21jcC5maXJlY3Jhd2wuZGV2L3YyL21jcCJ9)

mcp.jsonCopy

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp"
    }
  }
}
```

Open **Cursor Settings**, select **MCP**, and confirm **firecrawl** is connected.

Add this remote server configuration to your global or project config.

opencode.jsonCopy

```
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "firecrawl": {
      "type": "remote",
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "enabled": true
    }
  }
}
```

Then run `opencode mcp list` and confirm **firecrawl** is connected.

Using another MCP client? Point it at:

`https://mcp.firecrawl.dev/v2/mcp`

Copy

Keyless MCP is rate limited and exposes Search, Scrape, and Parse. Add an API key to unlock the full tool surface or higher limits.

## [​](https://docs.firecrawl.dev/mcp-server/keyless\#add-an-api-key)  Add an API key

[Create a Firecrawl API key](https://www.firecrawl.dev/app/api-keys), then add it as a bearer token on the same endpoint in your client config:

```
{
  "mcpServers": {
    "firecrawl": {
      "type": "http",
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer <FIRECRAWL_API_KEY>"
      }
    }
  }
}
```

## [​](https://docs.firecrawl.dev/mcp-server/keyless\#verify-your-connection)  Verify your connection

Open your client’s MCP status or tool list and confirm that `firecrawl` is connected. A keyless connection shows `firecrawl_search`, `firecrawl_scrape`, and `firecrawl_parse`; an API-key connection can expose the [full tool surface](https://docs.firecrawl.dev/mcp-server/tools), subject to plan, deployment, and team policy.

## [​](https://docs.firecrawl.dev/mcp-server/keyless\#try)  Try

```
Search the web for the latest Firecrawl release notes and summarize the sources.
```

If no Firecrawl tools appear, restart or reload the client after saving its MCP configuration.

## [​](https://docs.firecrawl.dev/mcp-server/keyless\#more)  More

[**Choose a tool** \\
\\
Find the right Firecrawl MCP tool and review connection-specific availability.](https://docs.firecrawl.dev/mcp-server/tools)

[**Run locally** \\
\\
Start the open-source server over stdio or Streamable HTTP.](https://docs.firecrawl.dev/mcp-server/local)

For the current keyless allowance and plan limits, see [Rate limits](https://docs.firecrawl.dev/rate-limits#keyless-no-api-key).

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/mcp-server/keyless.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/mcp-server/keyless)

✕
