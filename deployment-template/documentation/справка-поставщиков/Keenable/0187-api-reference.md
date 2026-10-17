> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: api-reference

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.keenable.ai/api-reference

API reference - Keenable
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
API reference
API reference
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
Base URL
Authentication
Endpoints
Limits and billing
API reference
API reference
Copy page
Copy page
The HTTP API behind the Keenable CLI, MCP server, and integrations.
Copy page
Copy page
Two endpoints sit under everything else Keenable ships — the
## CLI
, the
MCP server
, and every
integration
call one or both of them. Reach for the HTTP API directly when you are building something none of those cover.
​
Base URL
https://api.keenable.ai
​
Authentication
There are three ways in, and the one you pick decides the path you call.
With an API key
, in the
X-API-Key
header:
curl
## -X
## POST
"https://api.keenable.ai/v1/search"
\
## -H
"X-API-Key: keen_<your_key>"
\
## -H
"Content-Type: application/json"
\
-d
'{ "query": "typescript best practices" }'
Authorization: Bearer keen_<your_key>
works too, and
X-API-Key
wins if both are present. See
Authentication
for obtaining and rotating a key, and for the error responses both endpoints share.
Without one
, on the
/public
twin of each endpoint:
curl
## -X
## POST
"https://api.keenable.ai/v1/search/public"
\
## -H
"X-Keenable-Title: My App"
\
## -H
"Content-Type: application/json"
\
-d
'{ "query": "typescript best practices" }'
X-Keenable-Title
names the application making the call. It is
required
on the public endpoints — a request without it is rejected with
400 Missing app identifier
— and it is how keyless traffic is attributed. Values longer than 256 characters are truncated, and
?keenable_title=
carries the same value when a header is not an option.
Paying per request
, on the
/v1/x402/*
paths, with no key and no account: each call pays $0.01 in USDC on Base over the x402 protocol. See
Pay per request
for the payment flow and a client example.
Parameters and response shapes are identical across all three, so moving between them means changing the path and swapping one header. The keyless tier is what the
## CLI
, the
MCP server
, and every
integration
fall back to when no key is configured.
​
Endpoints
Endpoint
Method
Path
Keyless path
Pay-per-request path
Returns
Search
## POST
/v1/search
/v1/search/public
/v1/x402/search
Ranked results with URLs, titles, descriptions, and snippets
Fetch
## GET
/v1/fetch
/v1/fetch/public
/v1/x402/fetch
Page content as markdown, with title, description, and author
Each endpoint page carries the full request and response shape, examples in curl, Python, and TypeScript, and a playground you can call with your own key.
​
Limits and billing
Authenticated requests are rate limited per organization rather than per IP — see
Rate limits
for the numbers — and draw on your
credit
balance.
Keyless requests are limited per IP instead, on a public pool capped at 1,000 requests per hour and 10 per second, and they consume no credits. Responses carry
X-RateLimit-Limit
,
X-RateLimit-Remaining
and
X-RateLimit-Reset
, and a
429
adds
Retry-After
. That pool is shared with everyone else on your egress address, so its headroom is outside your control: use a key for anything past a first look.
Pay-per-request calls consume no credits either: each one is paid for on its own, and has its own
limits
.
## CLI
Search
x
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform
