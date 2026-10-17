> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Exa: integration-prose

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Hermes Agent
URL: https://exa.ai/docs/integrations/hermes-agent.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Hermes Agent
> Give Hermes Agent live web search and page contents with Exa.
Hermes Agent includes Exa as a native backend for its model-callable `web_search` and `web_extract` tools. Use Exa for both capabilities, or pair it with another Hermes web provider.
## Connect your Exa account
## Get an Exa API key
## Get your Exa API key
Create a key in the dashboard. New accounts start with free credits.
## Select Exa in Hermes
Run the tool setup wizard:
Open Web Search & Extract, choose Exa, and select the API-key-backed option. When prompted, enter your Exa API key. Hermes stores secrets in `~/.hermes/.env` and provider selection in `~/.hermes/config.yaml`.
## Test web access
Start Hermes and ask it to search, then read one of the results:
Hermes should call `web_search`, followed by `web_extract` when it needs the page itself.
## Configure manually
Add your key to the Hermes environment file:
Then select Exa for both web capabilities:
You can use the shared fallback instead:
The per-capability settings take precedence over `web.backend`. This lets you use Exa only for search or only for extraction when combining providers.
## Tools Hermes gets
| Tool | Exa behavior |
| --- | --- |
| `web_search` | Searches with Exa and returns ranked pages with titles, URLs, and text snippets. |
| `web_extract` | Retrieves readable content from one or more URLs through Exa Contents. |
Hermes truncates long extracted pages to its configured character budget and stores the complete text on disk. Change the default with `web.extract_char_limit`, or let the agent request a larger `char_limit` for an individual call.
Hermes can use Exa through its keyless free-provider pool without an API key. That pool is rate-limited and may rotate among providers. Configure `EXA_API_KEY` and select the API-key-backed Exa option when you need requests to use your Exa account consistently.
## Troubleshooting
## Hermes does not select Exa
Run `hermes tools` and explicitly select Exa. If you configure files manually, check that `web.search_backend`, `web.extract_backend`, or `web.backend` is set to `exa`.
## Hermes reports that EXA_API_KEY is missing
Add the key to `~/.hermes/.env`, then restart Hermes so it reloads the environment.
## Search works but extraction uses another provider
Hermes can configure search and extraction independently. Set both `web.search_backend` and `web.extract_backend` to `exa`.
## Resources
## Hermes web tools
Review Hermes provider selection, caching, and extraction behavior.
## Exa Search
Learn how Exa searches, filters, and returns page contents.
## Exa Contents
Understand the extraction API behind `web_extract`.
# Exa MCP
URL: https://exa.ai/docs/get-started/exa-mcp.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Exa MCP
> Connect ChatGPT, Codex, Claude, Grok, Cursor, and any other MCP client to Exa's web search, page fetching, Exa Agent, and Exa Connect tools.
Use Exa MCP to improve the built-in web search in ChatGPT, Claude, and MCP-compatible tools with Exa's search capabilities, including web search, code search, Exa Agent, and Exa Connect.
Exa offers a hosted server that works in any MCP client:
No API key is required to get started. Exa MCP is open source and available on GitHub.
## Install
## ChatGPT & Codex
Exa is an official plugin in OpenAI's plugin directory, which includes the hosted MCP server plus Exa's `search` and `exa-agent` skills.
## Open the plugin
Go to chatgpt.com/plugins/exa. It opens Exa in OpenAI's plugin directory, which is the same directory for ChatGPT and for Codex.
## Install it
Select the plus button to install. Sign in to Exa when prompted, either during install or the first time Codex or ChatGPT uses it.
## Start a new session
Skills load in chats and CLI sessions started after the install, so open a fresh one and ask for something that needs the web.
That's it. The plugin includes both Exa's MCP integration and skills, so there's no separate MCP or skill setup required.
See Exa in Codex and ChatGPT for the full setup and workflow guide.
## Claude
### Claude Code CLI
## Install the plugin
Install Exa from the terminal:
You can also type `/plugin` in Claude Code, search for Exa, and install it.
## Use Exa
Start a new Claude Code session and ask for something that needs the web.
### Desktop, Web & Cowork
Claude Desktop, Web, and Cowork all use Exa's official connector.
## Open the connector directory
Select the plus button in a new chat, choose Add connector, and search for Exa.
## Connect Exa
Open Exa, select Connect to Claude, and authorize access when prompted.
## Use Exa
Start a new chat and ask for something that needs current information from the web.
See Exa in Claude Code, Web, and Desktop for the full setup and workflow guide.
Claude Team and Enterprise admins can provision the connector for everyone through their identity provider instead: see Enterprise Managed Auth.
## Grok Build
Exa is available on the Grok Build marketplace.
## Open the marketplace
In Grok Build, run `/marketplace`.
## Install Exa
Find exa in the list and press `i`.
## Sign in
Run `/mcp`, select exa, and press `i` to sign in to your Exa account in the browser.
New accounts get free credits at signup.
## Cursor
Install Exa MCP from the Cursor marketplace, or add it to `~/.cursor/mcp.json`:
## VS Code
Use the one-click install, or add it to `.vscode/mcp.json` in your project:
## Other clients
Most clients use the standard `mcpServers` shape:
Where the config lives and what the URL key is called varies by client:
| Client | Where to add it | URL key |
| --- | --- | --- |
| fx by Vercel | `/mcp add --transport http exa https://mcp.exa.ai/mcp` in the fx shell (saved to `~/.fx/mcp.json`) | `url` |
| OpenCode | `opencode.json` (under `mcp`, with `"type": "remote"`) | `url` |
| Kiro | `~/.kiro/settings/mcp.json` (under `mcpServers`) | `url` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` (under `mcpServers`) | `serverUrl` |
| Google Antigravity | Agent panel → `…` → MCP Servers, search for Exa in the MCP Store and click Install (no config needed) | — |
| Zed | Zed `settings.json` (under `context_servers`) | `url` |
| Gemini CLI | `~/.gemini/settings.json` (under `mcpServers`) | `httpUrl` |
| Warp | Settings → MCP Servers → Add MCP Server (top-level `exa`) | `url` |
| v0 by Vercel | Prompt Tools → Add MCP | paste the URL directly |
If your client doesn't support remote MCP servers, use the `mcp-remote` bridge:
Or run the local npm package with your Exa API key:
## Authentication
Exa MCP supports three authentication modes:
| Mode | Use it for | Setup |
| --- | --- | --- |
| Keyless | Free rate-limited usage without sign-in or API key | Connect to `https://mcp.exa.ai/mcp` |
| OAuth | Interactive clients, marketplace installs, production usage | Connect to `https://mcp.exa.ai/mcp?login` to sign in to Exa in the browser. Usage belongs to your Exa team. |
| API key | Clients without MCP OAuth | Connect to `https://mcp.exa.ai/mcp` with the `x-api-key` header set to your API key |
### Sign in with OAuth
ChatGPT, Claude, and other marketplace installs prompt you to sign in when needed. In any client that supports MCP OAuth, you can request the same flow by connecting to:
Your client discovers Exa's authorization server, opens the browser sign-in, and manages access.
### Use an API key
## Get your Exa API key
Create a key in the dashboard. New accounts start with free credits.
Add the `x-api-key` header to the MCP server configuration:
## Available Tools
| Tool | Availability | Use it for |
| --- | --- | --- |
| `web_search_exa` | Enabled by default | Search the web and return relevant, ready-to-use content |
| `web_fetch_exa` | Enabled by default | Read clean content from one or more known URLs |
| `web_search_advanced_exa` | Availiable when opted in | Configure web search with advanced filters and controls |
| `agent_run` | Enabled by default with OAuth or API key | Run multi-step research, list-building, enrichment, and structured output |
Use the `tools` URL parameter to choose what your client sees. For example, to enable all tools:
An explicit `tools` list replaces the defaults, so include every tool you want enabled including web search and fetch.
## Exa Agent
Use Exa Agent for research that takes more than one search—for example, building a list, checking each item against criteria, or returning structured results.
Agent runs are usage-based, so `agent_run` requires OAuth or an API key. Once authenticated, it is enabled by default alongside the search tools, with no `tools` parameter needed. This URL starts OAuth:
If you use an API key, omit `login` and add the key as described in Authentication. If you set an explicit `tools` list, include `agent_run` in it.
## Describe what you need
Ask for the research in plain language. Your assistant passes the request to `agent_run` with a `query`, and Exa Agent works out what to search, reads the sources, and checks what it finds against the request.
Ask your Agent to provide an `outputSchema` only when your application needs the findings in a consistent JSON format. You can share one with your assistant in the system prompt, or have it generate one for you.
## Get the result
When the research completes, the tool call hands your assistant the full research package:
- The written findings
- The sources behind them
- Validated JSON if you provided `outputSchema`
- Usage and cost
Your assistant writes its reply from this package, so tell it what you want done with the output. You can ask it to summarize the findings, compare them, save them to a file, or anything else.
## Continue if it needs more time
Research that outlasts a single MCP call doesn't fail: the tool reports `status: "running"` with an `id` while the run continues on Exa. Your assistant calls `agent_run` again with that `id` as `runId` to pick the same run back up.
## Optional controls
| Field | Use it to |
| --- | --- |
| `systemPrompt` | Give Agent extra guidance for researching or judging results |
| `outputSchema` | Return the answer in a specific JSON format |
| `input.data` | Enrich rows or entities you already have |
| `input.exclusion` | Skip results you already know about |
| `dataSources` | Add up to five Exa Connect providers |
| `previousRunId` | Build a new request on completed research |
| `effort` | Choose how much research Agent should do |
Use `runId` to keep waiting on current work. Use `previousRunId` to ask a new follow-up based on finished work.
See the Exa Agent guide for output schema patterns, effort modes, data sources, and pricing.
## Advanced search
Use `web_search_advanced_exa` when the request needs explicit category or domain filters, date ranges, text constraints, geo-targeting, query expansion, summaries, highlights, freshness control, or subpage crawling. For ordinary searches, keep `web_search_exa`; it gives the model a smaller tool surface and requires less configuration.
Advanced Search does not require authentication, although authenticated connections use your own plan and rate limits. Enable it alongside the default tools with:
The MCP tool presents common Search API controls as tool-friendly fields such as `includeDomains`, `startPublishedDate`, `enableHighlights`, and `maxAgeHours`. Read the tool schema in your client for the exact field names.
## Troubleshooting
## Rate limit error (429)
The connection is using Exa's free rate limits. Sign in with OAuth or add your own API key, then reconnect so requests use your team's plan and limits.
## Get your Exa API key
Create a key in the dashboard. New accounts start with free credits.
## Agent is missing or asks for authentication
`agent_run` cannot use the free rate limits, so it only appears once you connect with `?login` or configure an API key. If you set an explicit `tools` list, make sure it includes `agent_run`. See Exa Agent.
## OAuth sign-in does not open
Confirm that your client supports MCP OAuth and connect to `https://mcp.exa.ai/mcp?login`. Restart the client after changing the URL. If the client cannot complete MCP OAuth, use an API key instead.
## Tools not appearing
An explicit `tools` parameter replaces the default tool list. Check that every tool you want is present in the URL, then restart your MCP client so it fetches the tool list again.
## Claude desktop not connecting
Use the built-in connector: select + (or Add connectors) → Connectors tab → search for Exa → select +.
## Config file not found
Common config locations:
- Cursor: `~/.cursor/mcp.json`
- fx: `~/.fx/mcp.json`
- VS Code: `.vscode/mcp.json` (in project root)
- Claude desktop (macOS): `~/Library/Application Support/Claude/claude_desktop_config.json`
- Claude desktop (Windows): `%APPDATA%\Claude\claude_desktop_config.json`
## Resources
## GitHub
Exa MCP source code.
## npm
Run Exa MCP locally with the npm package.
## Agent skills
Portable skills that pair with Exa MCP.
## Exa in Codex and ChatGPT
Full setup and workflow guide for the Exa plugin.
# Agent Skills
URL: https://exa.ai/docs/get-started/agent-skills/overview.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Agent Skills
> Install Exa skills in Claude Code, Codex, and other coding agents.
Exa skills teach coding agents how to search, retrieve content, and build with Exa’s APIs. Find them in the open-source exa-labs/agent-skills repository.
Each skill contains markdown files that follow the open Agent Skills standard, so the same files install into any compatible agent.
## Install
Install every Exa skill at once:
## Get your Exa API key
Create a key in the dashboard. New accounts start with free credits.
Set your key as `EXA_API_KEY` in your agent environment.
Or open a skill page below and copy its setup prompt into your agent. The prompt installs that skill and verifies your API key without printing it.
## Skills
Each skill page includes a one-line description, a copyable setup prompt, and a link to the raw `SKILL.md` source.
## Build with Exa
Build applications and agents with Exa's full API platform.
## Exa Search
Call Exa Search directly with cURL or raw HTTP.
## Exa Contents
Call Exa Contents directly with cURL or raw HTTP.
## Related
## Skills repository
Source for every skill, including raw `SKILL.md` files.
## Exa MCP
Connect Claude, Cursor, VS Code, and other clients to Exa over MCP.
# SDK Quickstart
URL: https://exa.ai/docs/sdks/quickstart.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# SDK Quickstart
> Install and use the Exa Python and JavaScript SDKs
The official Exa SDKs. Search the web, get page contents, and get answers with citations.
## Get your Exa API key
Create a key in the dashboard. New accounts start with free credits.
## Install
The Python SDK requires Python 3.9+.
## Authentication
Set your API key as an environment variable:
## macOS/Linux
## Windows
## Getting started
Initialize the client and run your first search:
Both clients read your key from the `EXA_API_KEY` environment variable. To set it explicitly
instead, pass it inline: `Exa(api_key="your-api-key")` or `new Exa("your-api-key")`.
## Recommended defaults
| Decision | Recommended default |
| --- | --- |
| Starting point | Use `search` |
| Search type | Keep `auto` unless latency or synthesis needs require another type |
| Page content | Start with `highlights: true` |
| Known URLs | Use `get_contents` / `getContents` |
| Freshness | Set `max_age_hours` / `maxAgeHours` only when stale content would be unusable |
The two request types take the same content options in different places:
| Method | Content option placement |
| --- | --- |
| `search` | Inside `contents`, as in `exa.search(query, contents={"highlights": True})` |
| `get_contents` / `getContents` | Directly on the request, as in `exa.get_contents(urls, highlights=True)` |
## Search
Search finds relevant pages and returns their contents in one call.
Use `highlights: true` for AI answers, RAG, and search previews. Exa sizes each result's
excerpts to its relevance; set `max_characters` / `maxCharacters` only when your application
requires a fixed limit.
Filters, date ranges, and result counts:
When an agent chooses the query, pass the goal that search serves as `objective` alongside it:
See Pass the objective from agents for when to use it and how to describe it to a model.
### Output schema
`output_schema` / `outputSchema` works with every search type and returns the synthesized value
in `output.content`. Use `system_prompt` / `systemPrompt` for source preferences or emphasis.
Grounding is returned automatically in `output.grounding`, so do not duplicate citations or
confidence in your schema.
Deep modes are recommended when the output requires research across several searches. Use `deep-lite` for lightweight research or `deep` for multi-step search and stronger synthesis. See the Search guide for the full request options.
## Contents
Extract highlights, full text, or summaries from URLs you already know. Start with highlights and
add a query to focus them on the information you need.
Use full text when you need broader context or document structure. See the Contents guide for output shapes, freshness controls, and subpage crawling.
## Answer
Get answers to questions with citations.
## Async and types
Python exposes `AsyncExa` for async operations, and the JavaScript SDK ships TypeScript types for
every method.
## Resources
Python: exa-py source and PyPI package. JavaScript: exa-js source and npm package.
## Continue
## Search guide
Return to the main Search guide for request patterns, filters, and deeper modes.
## Search reference
Jump to the full `/search` request and response schema.
## Contents guide
Use Contents when you already know the URLs and want direct extraction.
