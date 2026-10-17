> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: mcp-local

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/mcp-server/local

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/mcp-server/local#content-area)

Run Firecrawl MCP locally when a client needs to launch a local process, when you need a local HTTP transport, or when the MCP server must connect to a self-hosted Firecrawl API. For the managed service, start with [Get Started](https://docs.firecrawl.dev/mcp-server).

## [​](https://docs.firecrawl.dev/mcp-server/local\#prerequisites)  Prerequisites

- Node.js 22 or newer
- npm and `npx`, included with Node.js
- A Firecrawl API key for the cloud API, or a self-hosted Firecrawl API URL

Confirm the installed Node.js version:

```
node --version
```

## [​](https://docs.firecrawl.dev/mcp-server/local\#start-the-server)  Start the server

- stdio

- Streamable HTTP


Use stdio when the MCP client launches Firecrawl as a local process:

```
env FIRECRAWL_API_KEY=fc-YOUR-API-KEY \
  npx -y firecrawl-mcp@3.23.7
```

Configure the client to run `npx -y firecrawl-mcp@3.23.7` and provide `FIRECRAWL_API_KEY` through the client’s protected environment or secret mechanism.

Use HTTP when a client such as n8n connects to an already-running server:

```
env HTTP_STREAMABLE_SERVER=true \
  FIRECRAWL_API_KEY=fc-YOUR-API-KEY \
  npx -y firecrawl-mcp@3.23.7
```

Connect the client to:

```
http://localhost:3000/mcp
```

Confirm the server is ready:

```
curl http://localhost:3000/health
```

The health check returns `ok`. The local route is `/mcp`; `/v2/mcp` belongs to the hosted Firecrawl service.

## [​](https://docs.firecrawl.dev/mcp-server/local\#configure-the-firecrawl-api)  Configure the Firecrawl API

| Environment variable | Purpose |
| --- | --- |
| `FIRECRAWL_API_KEY` | Authenticates to the Firecrawl cloud API. It is optional only when a self-hosted API does not require authentication. |
| `FIRECRAWL_API_URL` | Sends requests to a self-hosted Firecrawl API instead of the cloud API. |
| `HTTP_STREAMABLE_SERVER` | Set to `true` to start the local Streamable HTTP transport instead of stdio. |

Cloud API

Self-hosted API

```
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
npx -y firecrawl-mcp@3.23.7
```

```
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com
export FIRECRAWL_API_KEY=your-api-key # Omit if the instance does not require authentication
npx -y firecrawl-mcp@3.23.7
```

Direct local-file parsing with `firecrawl_parse` requires `FIRECRAWL_API_URL` pointing to a self-hosted Firecrawl API. A local MCP server connected only to the cloud API cannot upload a local file through that tool; the [hosted server uses a signed upload handoff](https://docs.firecrawl.dev/mcp-server/tools#important-behavior) instead.

## [​](https://docs.firecrawl.dev/mcp-server/local\#install-globally)  Install globally

Use `npx` for the shortest setup. To install the same reviewed release globally instead:

```
npm install -g firecrawl-mcp@3.23.7
```

Then run:

```
env FIRECRAWL_API_KEY=fc-YOUR-API-KEY firecrawl-mcp
```

## [​](https://docs.firecrawl.dev/mcp-server/local\#troubleshooting)  Troubleshooting

The client reports spawn npx ENOENT

Install Node.js 22 or newer, confirm that `npx` is on the client’s `PATH`, and fully restart the client. On Windows, run `where npx` in Command Prompt and configure the client to use the returned `npx.cmd` path.

The HTTP client cannot connect

Confirm that `HTTP_STREAMABLE_SERVER=true`, then call `http://localhost:3000/health`. Use `http://localhost:3000/mcp` as the client endpoint, not the hosted `/v2/mcp` path.

A tool is unavailable

Tool availability depends on the Firecrawl services enabled in the target deployment. Compare the connection in [Tools](https://docs.firecrawl.dev/mcp-server/tools) and check the local process output for registration or authentication errors.

The server is rate-limited

Rate limits are enforced by the connected Firecrawl API. Review the current [rate limits](https://docs.firecrawl.dev/rate-limits) and the limits configured for a self-hosted deployment.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/mcp-server/local.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/mcp-server/local)

✕
