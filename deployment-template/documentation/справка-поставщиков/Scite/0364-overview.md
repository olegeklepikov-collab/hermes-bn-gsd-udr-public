> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: overview

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scite MCP

> Use Scite inside ChatGPT, Claude, Microsoft 365 Copilot, and other AI tools to search the literature and retrieve citation data.

Scite MCP is a hosted [Model Context Protocol](https://modelcontextprotocol.io/) server that lets AI tools search scientific literature and retrieve citation data in conversation. It powers Scite's first-party ChatGPT plugin and Claude connector, and it works with any other MCP-compatible client.

The plugin, connector, and MCP API are not separate data products. They are three ways to reach the same Scite tools.

Research Solutions also offers [Article Galaxy for Copilot](https://marketplace.microsoft.com/en-us/product/WA200011900), a connector for Microsoft 365 Copilot that can retrieve available full text and Scite Smart Citation content.

## Install a ready-made integration

<CardGroup cols={3}>
  <Card title="Scite plugin for ChatGPT" icon="messages" href="https://chatgpt.com/plugins/plugin_asdk_app_6952b3a3f1e881918951582d59483c78?q=scite">
    Open the Scite listing in ChatGPT, select **Install plugin**, and sign in with your Scite account. Use `@Scite` in a prompt to activate it.
  </Card>

  <Card title="Scite connector for Claude" icon="sparkles" href="https://claude.ai/directory/connectors/scite">
    Open the Scite listing in Claude's Connectors Directory, select **Connect**, and sign in with your Scite account when prompted.
  </Card>

  <Card title="Article Galaxy for Copilot" icon="robot" href="https://marketplace.microsoft.com/en-us/product/WA200011900">
    Add the connector from Microsoft Marketplace to find scientific articles and retrieve available full text and Smart Citation content in Microsoft 365 Copilot. A Research Solutions account is required.
  </Card>
</CardGroup>

The ChatGPT and Claude listings configure Scite MCP and use OAuth, so you do not need to copy an MCP URL or create an API key. The Microsoft 365 Copilot connector uses your Research Solutions account and is read-only. Availability may depend on your AI client plan and workspace settings.

## Choose your setup

| You want to… | Use | Setup |
| - | - | - |
| Use Scite in ChatGPT or Claude | The first-party plugin or connector above | Install, then sign in with Scite |
| Retrieve literature and Smart Citation content in Microsoft 365 Copilot | [Article Galaxy for Copilot](https://marketplace.microsoft.com/en-us/product/WA200011900) | Add the connector, then sign in with Research Solutions |
| Use Scite in another MCP-compatible AI tool | Scite's hosted MCP server | Connect the client to `https://api.scite.ai/mcp` and authenticate with OAuth |
| Build your own script, server, or MCP client | The MCP API | Call `https://api.scite.ai/mcp` with an `mcp`-scoped API key |

See [scite.ai/mcp](https://scite.ai/mcp) for setup instructions for Claude Desktop, Claude Code, Gemini CLI, Copilot Studio, and other clients.

## Authentication

### ChatGPT and Claude (OAuth)

Install Scite from the [ChatGPT Plugin Directory](https://chatgpt.com/plugins/plugin_asdk_app_6952b3a3f1e881918951582d59483c78?q=scite) or [Claude Connectors Directory](https://claude.ai/directory/connectors/scite). The listing configures the connection; sign in with your Scite account when prompted. A Scite premium subscription is required.

### Microsoft 365 Copilot

Install [Article Galaxy for Copilot](https://marketplace.microsoft.com/en-us/product/WA200011900) from Microsoft Marketplace and sign in with your Research Solutions account. The connector is read-only: it can retrieve content and check existing orders, but it does not place orders, complete purchases, or charge users.

### Other MCP clients (OAuth)

Other interactive MCP clients use the standard OAuth 2.1 authorization-code flow with PKCE. Most discover Scite's authorization and registration endpoints automatically after you provide `https://api.scite.ai/mcp`.

<Accordion title="OAuth client requirements and troubleshooting">
  Every request to `/mcp/oauth/authorize` must include `client_id`, `code_challenge`, and `code_challenge_method=S256`. A `client_id` is obtained via Dynamic Client Registration (DCR); clients discover the registration endpoint from `/.well-known/oauth-authorization-server`.

  Some platforms, including Microsoft Copilot Studio, default to PKCE and DCR turned **off**. With those disabled, the authorize request omits required parameters and the server returns `invalid_request`. Enable **PKCE** and **DCR-with-discovery**, or supply a registered `client_id`.
</Accordion>

### MCP API (programmatic API key)

**Need an API key?** On Pro, create one in the API Console](https://scite.ai/users/me/api). Creating a key doesn't grant every optional scope; see [Authentication (локальный ресурс исходного примера не включён) for feature access. For higher limits or managed credentials, [contact sales](https://scite.ai/contact).

For scripts, servers, or your own MCP client: create an API key on Pro from the [API Console](https://scite.ai/users/me/api), grant it the `mcp` scope, and send it as a bearer token to `/mcp`. No token exchange is needed. It shares your account's MCP quota and billing.

Enterprise customers can alternatively use issued `client_id`/`client_secret` credentials; see Authentication (локальный ресурс исходного примера не включён).

If you access Scite through your organization's SAML SSO, sign in to Scite through SSO before authorizing an interactive MCP client. See Use SSO accounts with MCP (локальный ресурс исходного примера не включён).

## What's available

<CardGroup cols={2}>
  <Card title="Tool reference" icon="wrench" href="/mcp/tools/overview">
    25 tools across literature, evidence datasets, and collections.
  </Card>

  <Card title="Prompts" icon="list-check" href="/mcp/prompts">
    Four prebuilt research workflows, from literature review to fact-checking.
  </Card>
</CardGroup>

## Endpoints

| Method | Path | Description |
| - | - | - |
| GET | `/mcp/info` | Server info and capabilities |
| POST | `/mcp` | JSON-RPC 2.0 endpoint for tool calls |
| GET | `/mcp/health` | Health check |

`GET /mcp` returns `405`. The server doesn't support server-initiated SSE streams, so all traffic goes over `POST`.

## Methods

| Method | Description |
| - | - |
| `initialize` | Negotiates the protocol version and returns server capabilities |
| `tools/list` | Lists available tools and their input schemas |
| `tools/call` | Executes a tool (e.g. `search_literature`) |
| `prompts/list` | Lists the prebuilt prompts (локальный ресурс исходного примера не включён) and their arguments |
| `prompts/get` | Renders one prompt with your arguments substituted |
| `resources/list` | Returns an empty list — the server exposes no resources |
| `logging/setLevel` | Sets the log level for the session |
| `ping` | Heartbeat check |
| `notifications/*` | Acknowledged and discarded |

A `POST` body may be a single JSON-RPC message or an array of them for batching.

## Protocol version

The server supports `2024-11-05`, `2025-03-26`, `2025-06-18`, and `2025-11-25`. It echoes back whichever version you request in `initialize` if it's supported, and otherwise negotiates down to `2025-06-18`.

## Sessions

Every response carries an `Mcp-Session-Id` header. The server generates one if your `initialize` request doesn't supply it. Send it back on subsequent requests so tool-call analytics and client capability detection stay tied to your session.

Sessions are optional — the endpoint is stateless and works without the header — but passing it through gives better behavior in clients that support elicitation.

## Example: search literature

```bash theme={null}
curl -X POST 'https://api.scite.ai/mcp' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "tools/call",
    "params": {
      "name": "search_literature",
      "arguments": {
        "term": "\"machine learning\" AND healthcare",
        "limit": 5,
        "sort": "date",
        "sort_order": "desc"
      }
    }
  }'
```

`search_literature` supports Boolean operators, phrase search, and the same 25+ filters as the Search API (локальный ресурс исходного примера не включён). See Literature tools (локальный ресурс исходного примера не включён) for the full parameter reference, or call `tools/list` for the live input schema.

## Errors

Transport-level failures use HTTP status codes; everything inside a successful JSON-RPC exchange uses an `error` object.

| Code | Meaning | What to do |
| - | - | - |
| `-32700` | Parse error — the body isn't valid JSON | Fix the request body |
| `-32600` | Invalid request — malformed or empty batch | Send a JSON object, or a non-empty array of them |
| `-32601` | Method not found | Use one of the methods listed above |
| `-32602` | Invalid params — including a missing required prompt argument | Check the tool's input schema or the prompt's arguments |
| `-32001` | Usage limit reached | Sign in, or wait for the monthly reset |
| `-32003` | Plan, scope, or entitlement required | See access requirements (локальный ресурс исходного примера не включён) |
| `-32042` | Upgrade required, returned as a URL elicitation | Open the URL in the payload to upgrade |

## Usage limits

MCP tool calls draw on a monthly allowance tied to your plan. Organization licenses can be configured per seat, as a shared pool, or without a cap. A self-serve API key shares its owner's allowance rather than getting its own.

Exceeding the allowance returns `-32001`. The counter resets at the start of each calendar month.

## Troubleshooting

* `401 Unauthorized`: the API key is missing, invalid, or revoked.
* `403 User not authorized`: the key or account doesn't have the `mcp` scope.
* `invalid_request` during browser authorization: confirm that the client enables PKCE and Dynamic Client Registration.
* A tool is missing from `tools/list`: your credential lacks the `mcp` scope. Access to individual tools is enforced on `tools/call`, not by hiding them from the list.
* A tool call returns `-32003` right after you upgraded: entitlements can take up to 15 minutes to propagate. Disconnect and reconnect the server to apply them immediately.

See Errors and rate limits (локальный ресурс исходного примера не включён) for retry guidance.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
