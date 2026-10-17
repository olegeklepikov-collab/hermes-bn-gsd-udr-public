> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: authentication

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.keenable.ai/authentication

Authentication - Keenable
Documentation Index
Fetch the complete documentation index at:
/llms.txt
Use this file to discover all available pages before exploring further.
Skip to main content
Keenable
home page
Search...
⌘
## K
GitHub
Console
Console
Search...
Navigation
Get started
Authentication
Documentation
Integrations
Get started
Quickstart
Authentication
Rate limits
Credits
Auto top-up
Pay per request (x402)
Tools
## MCP
## CLI
API reference
API reference
## POST
Search
## GET
Fetch
Reference
Changelog
On this page
## CLI
## MCP
API key header
Evaluating without a key
Paying per request without a key
Error responses
Get started
Authentication
Copy page
Copy page
Get an API key, pass it to the API, CLI and MCP server, and read the error responses.
Copy page
Copy page
Keenable authenticates with an API key.
Log in
to obtain one.
Authenticated requests remove the hourly request limit, are rate limited per organization rather than per IP, and report per-call usage back to you. See
rate limits
for the numbers.
​
## CLI
Run
keenable login
and follow the browser flow to authenticate. The CLI uses device authorization, so an agent can provide the link for a human to complete.
keenable
login
​
## MCP
The easiest way is via the CLI:
# if not authenticated yet
keenable
login
keenable
configure-mcp
--all
This detects supported clients and configures them with your credentials. Alternatively, create an API key in the
console
and add it manually — see
API key header
below.
​
API key header
For manual MCP setup, pass your API key as the
X-API-Key
header.
Claude Code
Codex
## JSON
Claude Desktop
claude
mcp
add
keenable
\
--transport
http
https://api.keenable.ai/mcp
\
--scope
user
\
--header
"X-API-Key: keen_<your_key>"
[
mcp_servers
.
keenable
]
url
=
"https://api.keenable.ai/mcp"
http_headers
= {
"
X-API-Key
"
=
"keen_<your_key>"
}
{
"mcpServers"
: {
"keenable"
: {
"url"
:
"https://api.keenable.ai/mcp"
,
"headers"
: {
"X-API-Key"
:
"keen_<your_key>"
}
}
}
}
{
"mcpServers"
: {
"keenable"
: {
"command"
:
"npx"
,
"args"
: [
"-y"
,
"@keenable/mcp-server"
],
"env"
: {
## "KEENABLE_API_KEY"
:
"keen_<your_key>"
}
}
}
}
Claude Desktop needs that last shape: its config file accepts only local
command
servers, so a remote
"url"
entry is ignored without an error. If you don’t need your key applied, skip the file and add Keenable as a
connector
instead.
Keys are scoped to your workspace, never expire on their own, and can be rotated at any time.
Alternatively, you can pass your API key in the
Authorization
header using the
Bearer
scheme. This can be useful when integrating with MCP clients or frameworks that only support bearer tokens.
Authorization
:
Bearer keen_<your_key>
If both headers are present,
X-API-Key
takes precedence.
​
Evaluating without a key
The MCP server, the CLI and the HTTP API all run unauthenticated, so you can try them before creating an account. For the HTTP API this means the
/public
endpoints described in the
API reference
, which take no key but require an
X-Keenable-Title
header naming your application. Unauthenticated requests draw on a shared public pool capped at 1,000 requests per hour and 10 requests per second per IP, and they carry no usage metadata — the
_meta["keenable/usage"]
block described in the
MCP reference
is only returned for authenticated calls.
Use an API key for anything beyond a first look: the per-IP pool is shared with everyone else on your network or egress address, so its available headroom is outside your control.
​
Paying per request without a key
A third option sits between the two: an agent with a wallet can
pay per request
over the x402 protocol — $0.01 per search or fetch in USDC on Base, on the
/v1/x402/*
paths, with no account and no key. It has its own limits and error responses, described on that page. For regular use an API key stays cheaper.
​
Error responses
Status
Meaning
400
Malformed API key (invalid format)
401
Missing or invalid API key
402
No credits available — the monthly allowance is spent and no purchased credits remain (see
credits
)
403
API key disabled or revoked
429
Rate limit exceeded
Quickstart
Rate limits
x
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform
