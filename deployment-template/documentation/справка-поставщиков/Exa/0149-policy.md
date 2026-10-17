> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Exa: policy

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Pricing
URL: https://exa.ai/docs/admin/pricing.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Pricing

> Pay-as-you-go rates for Exa Search, Contents, Answer, Monitors, and the Agent API

---

Exa is pay-as-you-go. There is no subscription and no minimum spend: you load credits and are charged per request, at the rates below.

Start for free. The Free Tier gives you $10 in credits (up to 2,500 Instant searches) the day you sign up, and your free balance resets to $10 on the first of every month. No payment method required. Complete onboarding in the dashboard and your first team earns a one-time $10 bonus. Get an API key and start building.

Scaling up? For high volume, custom indexes, higher rate limits, SLAs, or Zero Data Retention, talk to us about an Enterprise plan with volume discounts.

## Get your Exa API key

Create a key in the dashboard. New accounts start with free credits.

## Products

## Search

From $4 / 1k requests

Real-time search with token-efficient page contents.

## Deep Search

$12–15 / 1k requests

Multi-step research with structured outputs and citations.

## Contents

$1 / 1k pages

Full page text, highlights, and summaries for known URLs.

## Answer

$5 / 1k requests

An LLM answer to a question, with citations.

## Monitors

$15 / 1k requests

Scheduled searches that surface new events on the web.

## Agent

$0.012–$1.00 / fixed-effort run, or usage-based

Async deep research, list building, and enrichment.

## Search, Contents, Answer, and Monitors

Each endpoint has a base price per request that includes up to 10 results. Additional results and Exa-generated page summaries are billed on top.

| Endpoint | Base price
(up to 10 results) | Each result above 10 | AI page summaries |
| - | - | - | - |
| `/search` (`instant`) | $4 / 1k requests | $1 / 1k results | $1 / 1k pages |
| `/search` (`fast`, `auto`) | $7 / 1k requests | $1 / 1k results | $1 / 1k pages |
| `/answer` | $5 / 1k requests | — | — |
| `/monitors` | $15 / 1k requests | $1 / 1k results | $1 / 1k pages |
| `/contents` | $1 / 1k pages, per content type | — | $1 / 1k pages |

## Agent

Set a fixed `effort` on Agent for a predictable per-request price. `auto` is the default metered mode; `ultra` is also metered and uses the same usage rates:

| Effort | Price |
| --- | --- |
| `minimal` | $0.012 / request |
| `low` | $0.025 / request |
| `medium` | $0.10 / request |
| `high` | $0.50 / request |
| `xhigh` | $1.00 / request |

Metered runs bill actual usage up to their per-run cap. `auto` defaults to a $5 cap; `ultra` defaults to a $20 cap:

| Usage component | Price |
| --- | --- |
| Agent Compute Units | $0.10 / ACU |
| Search tool calls | $0.005 / search |
| Email contact enrichment | $0.02 / email |
| Phone contact enrichment | $0.07 / phone number |

### Connect providers

Runs that use Exa Connect data sources
additionally bill each provider call — for example
Fiber.ai at $0.02 per credit and
Baselayer at $0.15–$4.00 per
order depending on the operation. See
Connect pricing for all
provider rates.

## Deep Search

Set with `type` on `/search`. Additional results and AI page summaries cost the same as standard search.

| Type | Base price
(up to 10 results) | Latency | Best for |
| - | - | - | - |
| `deep-lite` | $12 / 1k requests | ~4 seconds | Lightweight synthesis |
| `deep` | $12 / 1k requests | 4–15 seconds | Multi-step reasoning with structured outputs |
| `deep-reasoning` | $15 / 1k requests | 12–40 seconds | Harder research tasks |

## Enterprise

For high volume, custom datasets, and stricter security requirements.

## Powerful search

Up to 1,000 results per search, requests above 25 results, custom rate limits (QPS), tailored moderation, and custom indexes.

## Enterprise support

SLAs and MSAs, 1:1 onboarding and support, and Zero Data Retention.

## Custom pricing

Volume discounts and postpaid invoice billing.

## Talk to us

Get a quote for enterprise volume and terms

## Cost glossary

## Request

One API call to an endpoint. Prices are quoted per 1,000 requests, so a $7 / 1k rate is $0.007 per call.

## Result

One search result returned in a response. The base price covers the first 10 results in a request; every result above 10 adds $1 / 1k results. Requesting `numResults: 20` therefore costs the base price plus 10 additional results.

## Page and content type

A page is one URL that Exa returns content for. A content type is one view of that page: `text`, `highlights`, or `summary`. `/contents` bills each content type separately, so one page with `text` and `highlights` counts as two.

## AI page summary

An Exa-generated summary of a page, produced by an extra LLM call on our side. Billed at $1 / 1k pages on any endpoint that returns one.

## Agent Compute Unit (ACU)

The unit of model computation an Agent run consumes, reported as `usage.agentComputeUnits`. Longer runs, larger `input.data`, and more reasoning steps consume more ACUs.

## Effort

The Agent parameter that trades cost and latency against thoroughness. `auto` bills by consumption (ACUs plus tool calls) up to a default $5 cap; `ultra` uses the same usage rates up to a default $20 cap. Fixed efforts bill a flat price per request. See Agent effort modes.

## Contact enrichment

An Agent lookup that returns an email address or phone number for a person or company. Billed per contact found, on top of the run's other costs.

## Credits

Prepaid dollar balance on your account. Usage draws down credits at the rates above.

## Billing

Add credits, set up auto recharge, and find your invoices

# Billing and Rate Limits
URL: https://exa.ai/docs/admin/billing.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Billing and Rate Limits

> Manage Exa credits, invoices, and API rate limits.

Exa offers a Free tier, pay-as-you-go billing, and custom Enterprise plans. API usage draws from your team's credit balance, while rate limits control how quickly the team can make requests.

## Billing dashboard

Add credits, configure auto recharge, and view invoices.

## API keys

Review usage and set a lower limit for an individual key.

## Pricing

Compare current rates across Exa products.

## Plans at a glance

| Plan | Billing | Rate limit | Agent concurrency |
| --- | --- | --- | --- |
| Free | $10 in credits every month, plus a one-time $10 onboarding bonus (see Free tier credits) | 10 QPS | 50 active runs |
| Pay as you go | Prepaid credits with no subscription or minimum spend | 10 QPS, up to 25 QPS | 50 active runs |
| Enterprise | Custom volume pricing and optional postpaid invoicing | Custom | Custom |

## Contact Us

We'll advise on the best set up to handle latency, scale, ZDR, and more.

## Billing basics

Requests are charged against prepaid credits at the rates in Pricing or under your Enterprise contract. Team owners can add credits from the Billing dashboard; payments are processed through Stripe.

If your team exhausts its credits, requests return `402 Payment Required`. An API key that reaches its assigned budget also returns `402`. Add credits or ask a team administrator to adjust the key's budget. See Error codes.

### Free tier credits

Every new team starts on the Free tier with $10 in credits, available in full the day you sign up regardless of the date. Your free balance then resets to $10 on the first day of every calendar month. The grant does not accumulate: unused free credits from one month do not carry into the next, so this grant never holds more than $10 at a time. Only a user's first team receives the monthly grant.

A user's first team also earns a one-time $10 bonus when that user completes onboarding in the dashboard. The bonus does not expire.

Free credits spend on API calls at the standard rates and are never paid out or refunded.

For historical usage by API key, use Get API key usage.

## Rate limits

Rate limits are measured in queries per second (QPS) and apply to your team as a whole, across all of its API keys. You can give an individual key a lower limit from the API Keys page, but its traffic still counts toward the team limit.

| Endpoint | Default limit |
| --- | --- |
| `/search`, `/answer`, `/chat/completions` | 10 QPS |
| `/search` with `type` `deep-lite`, `deep`, or `deep-reasoning` | 5 QPS |
| `/contents` | 100 QPS |
| `/agent/runs`, `/responses` | 5 QPS and 50 active runs |
| `/websets/*` | 20 QPS |

Some endpoints share rate limit capacity. Limits are subject to change and can vary by plan; Websets searches also have plan-based concurrency limits, which you can check with Get Team Info.

When you exceed a limit, requests return `429 Too Many Requests`. Wait for the `Retry-After` header when present, or retry with exponential backoff. See Error codes.

### Agent limits

Agent limits are two separate controls: how many runs can be in progress at once, and how fast you can start new ones.

- Concurrency: 50 Agent runs can be in progress at a time. This limit is separate from your QPS and does not change when your QPS is raised. Starting a run past the limit returns `429` with error code `CONCURRENCY_LIMIT_REACHED`; wait for a run to finish or contact us to raise your concurrency limit.
- Starting runs: `POST /agent/runs` draws from your account QPS, and each run start counts as two requests. You can start runs at half your QPS, so an account with the default 10 QPS can start 5 runs per second, and 25 QPS allows 12 per second.
- Polling: `GET` requests for run status, events, and run lists do not count against your QPS and never block dispatch, so poll running Agents independently of how fast you start new ones.

### 25 QPS on pay as you go

Add $1,000 in credits within any 30-day window and your team's rate limit rises to 25 QPS for 90 days, automatically. The threshold counts credits you purchase, not credits you spend, and requalifying resets the 90 days. Track your progress on the Billing dashboard.

Need more than 25 QPS? Talk to sales.

## Auto recharge

Auto recharge purchases credits when your balance reaches a threshold you choose. Configure it from the Billing dashboard.

| Setting | Description |
| --- | --- |
| Recharge amount | Credits purchased each time auto recharge triggers, from $5 to $10,000. |
| Recharge threshold | The balance at which the recharge triggers. |
| Monthly maximum | Optional cap on auto-recharge purchases during the billing cycle. Set it to $0 or leave it blank for no cap. |

For example, a $100 recharge amount, $10 threshold, and $500 monthly maximum purchases $100 whenever the balance reaches $10, up to $500 in automatic purchases during the cycle.

For an upcoming launch or other high-volume workload, add enough credits in advance and set an auto-recharge amount that avoids many small payment attempts.

## Receipts and invoices

Exa emails receipts for credit purchases and auto recharges from billing@exa.ai. Add the address to your allow list if needed. Your full invoice history is available in the Billing dashboard.

Postpaid invoice billing is available with an Enterprise plan.

## Get help

## Increase your limits

Request more than 25 QPS, custom concurrency, volume pricing, or postpaid billing.

## Billing support

Get help with payments, credits, invoices, or account billing questions.

# Error Codes
URL: https://exa.ai/docs/admin/error-codes.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Error Codes

> Reference for common error codes used by the Exa API

Exa APIs signal failures with standard HTTP status codes and a JSON error body.

## HTTP status codes

| Code | Meaning | What to do |
| --- | --- | --- |
| `400` Bad Request | The body, query parameters, headers, or combination of options is invalid. | Correct the request using the returned message. |
| `401` Unauthorized | The API key is missing or invalid. | Verify the authentication header and API key. |
| `402` Payment Required | Credits are exhausted or a spending budget was exceeded. | Top up credits or contact your team administrator. |
| `403` Forbidden | The API key does not have access to the requested feature, or the request was blocked by policy. | Check the returned message and your plan's feature access. |
| `404` Not Found | The route or requested resource does not exist. | Verify the endpoint and resource ID. |
| `409` Conflict | The request conflicts with existing state — for example, a Webset with the same `externalId` already exists. | Fetch the existing resource or use a different identifier. |
| `422` Unprocessable Entity | A Websets preview query could not be decomposed into a valid entity and criteria. | Rephrase the preview query. |
| `429` Too Many Requests | Your API key, team, or network exceeded a rate or concurrency limit. | Reduce your request rate; wait for `Retry-After` seconds when present, otherwise use exponential backoff. |
| `500` Internal Server Error | An unexpected server error occurred. | Retry after a brief delay. Contact support if it persists. |
| `503` Service Unavailable | Exa is temporarily over capacity (`SERVICE_OVERLOADED`) or unavailable. The request was not processed and is not billed. | Retry with exponential backoff. This is independent of your request rate, so reducing it does not help — retrying does. |
| `504` Gateway Timeout | The request exceeded its processing deadline. | Retry the request or reduce its scope. |

URL-level failures from `/contents` are reported in the `statuses` field of a successful `200` response, not as request-level errors. See Content fetch status tags.

## Error response structure

Error responses return a `requestId`, a human-readable `error` message, and a machine-readable `tag`:

```json
{
  "requestId": "67207943fab9832d162b5317f4cca830",
  "error": "Invalid request body | Validation error: Invalid value for type",
  "tag": "INVALID_REQUEST_BODY"
}

```

Include the `requestId` when contacting support for faster troubleshooting.

The set of tags is open-ended and tag names are self-explanatory. Branch on the HTTP status code first and treat unrecognized tags as additional detail rather than parse failures.

## Common error tags

### Account, billing, and access

| Tag | HTTP code | Description |
| --- | --- | --- |
| `INVALID_API_KEY` | `401` | The API key is missing, empty, or invalid. |
| `NO_MORE_CREDITS` | `402` | The account has no remaining credits — top up at dashboard.exa.ai. |
| `API_KEY_BUDGET_EXCEEDED` | `402` | The API key exceeded its spending budget — contact your team administrator. |
| `TEAM_BUDGET_EXCEEDED` | `402` | The team exceeded its spending budget for the current billing period. |
| `FEATURE_DISABLED` | `403` | The requested endpoint, search type, or option is not enabled for your plan. |
| `PROHIBITED_CONTENT` | `403` | The request was rejected by content safety moderation. |
| `CONTENT_FILTER_ERROR` | `403` | Content was rejected by a safety policy during processing. |
| `RATE_LIMIT_EXCEEDED` | `429` | Your API key, team, or network exceeded its own rate limit — reduce your request rate. |
| `SERVICE_OVERLOADED` | `503` | Exa is temporarily over capacity and shed the request before processing it — retry with exponential backoff. |

### Request validation

| Tag | HTTP code | Description |
| --- | --- | --- |
| `INVALID_REQUEST_BODY` | `400` | The JSON body failed schema validation. |
| `INVALID_REQUEST` | `400` | Options conflict with each other, or a beta feature was used without its `Exa-Beta` header. |
| `INVALID_NUM_RESULTS` | `400` | `numResults` must be ≤ 100 when highlights are requested. |
| `NUM_RESULTS_EXCEEDED` | `400` | The requested result count exceeds your plan's limit. |
| `INVALID_JSON_SCHEMA` | `400` | The provided output schema is invalid. |
| `SUBPAGES_LIMIT_EXCEEDED` | `400` | `/contents` allows at most 100 subpages per request. |

### Payment protocols

Requests paid through x402 or MPP can also return:

| Tag | HTTP code | Description |
| --- | --- | --- |
| `X402_PAYMENT_REQUIRED` | `402` | Payment is required. |
| `X402_INVALID_SIGNATURE` | `400` | The x402 payment signature is invalid. |
| `X402_VERIFICATION_FAILED` | `402` | The x402 payment could not be verified. |
| `MPP_VERIFICATION_FAILED` | `402` | The MPP payment could not be verified. |
| `X402_TOO_MANY_UNPAID` | `429` | Too many x402 requests are awaiting payment. |
| `X402_WALLET_RATE_LIMITED` | `429` | The x402 wallet exceeded its rate limit. |
| `X402_INTERNAL_ERROR` | `500` | Exa could not create x402 payment requirements. |

## Content fetch status tags

When `/contents` receives multiple URLs, one URL can fail while the others succeed. URL-level failures are returned in the `statuses` field and do not fail the request:

```json
{
  "results": [],
  "statuses": [
    {
      "id": "https://example.com",
      "status": "error",
      "error": {
        "tag": "CRAWL_NOT_FOUND",
        "httpStatusCode": 404
      }
    }
  ]
}

```

`httpStatusCode` describes the target page, not the `/contents` response.

| Tag | Description | How to handle |
| --- | --- | --- |
| `CRAWL_NOT_FOUND` | The target page was not found. | Verify the URL is correct and accessible. |
| `CRAWL_HTTP_{status}` | The target returned an HTTP error, such as `CRAWL_HTTP_403`. | Handle the embedded target status. |
| `CRAWL_TIMEOUT` | The crawl timed out while fetching the target page. | Retry the request or try again later. |
| `CRAWL_LIVECRAWL_TIMEOUT` | Live retrieval exceeded your requested `livecrawlTimeout`. | Increase `livecrawlTimeout` or adjust `maxAgeHours`. |
| `SOURCE_NOT_AVAILABLE` | Access to the source is forbidden or the source is unavailable. | Check whether the source requires authentication or is restricted. |
| `UNSUPPORTED_URL` | The URL scheme is not supported for content fetching. | Use a standard HTTP or HTTPS URL. |
| `CRAWL_UNKNOWN_ERROR` | The crawl failed for another reason. | Retry the request; contact support if persistent. |

These status tags are specific to `/contents`; `/search` does not return a `statuses` field.

## Getting help

- Check Exa Status when `500`, `503`, or `504` errors persist.
- Check Rate Limits for current limits.
- Review the endpoint's API reference for request requirements.
- Contact hello@exa.ai with the response status, error body, and `requestId`.

# FAQs
URL: https://exa.ai/docs/admin/faqs.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# FAQs

> Answers to common questions about Exa products, search index, freshness, grounding, security, and pricing.

## What is Exa?

Exa provides web search and research infrastructure for AI applications. It combines an independent search index with content extraction and agentic research APIs, so applications can find sources, retrieve their contents, and produce grounded outputs.

## Which Exa product should I use?

- Use the Search API to find ranked web results and optionally return highlights, full text, or summaries.
- Use the Contents API when you already have URLs and need their extracted contents.
- Use the Agent API for asynchronous, multi-step research, list building, and structured enrichment.
- Use Monitors to run recurring searches and receive newly discovered results.

## What is Exa Connect?

Exa Connect gives Exa Agent access to premium data providers alongside web search in the same run. Add providers through `dataSources`, and Exa Agent chooses when to query each source before combining partner data and web research into one grounded, structured output.

For self-serve providers, Exa handles provider authentication and usage billing, so you do not need to build a separate integration or establish a separate provider account.

## What's different about Exa Search?

Exa Search is built for programmatic retrieval rather than ad-driven browsing. It can search by meaning, accept natural-language queries, and return page contents in the same request. Search modes range from low-latency retrieval to multi-step research with structured output.

See the Search quickstart for available search types and response formats.

## How large is Exa's index?

As of August 2026, Exa's index tracks 1.4 trillion URLs and serves 100 billion pages from across the public web. The index changes continuously as pages are discovered, refreshed, or removed.

## How fresh are Exa's results?

Exa discovers and refreshes pages continuously, with timing that varies by source and how often a page changes. When you need content newer than the indexed copy, use the Contents API's `maxAgeHours` option to control cache age and live retrieval.

## Does Exa operate a crawler?

Yes. Exa operates `ExaSearchBot` to discover and refresh pages on the public web for search and retrieval. It respects the Robots Exclusion Protocol, limits request rates per site, and does not attempt to bypass logins, paywalls, or CAPTCHAs.

`robots.txt` controls crawling. To remove an already indexed page, use a `noindex` robots meta tag or an `X-Robots-Tag: noindex` response header; Exa removes the page after its next re-fetch. See Exa Search Crawler for the user agent, cryptographic verification instructions, and crawler controls.

## How does Exa help ground LLM responses?

Exa returns source URLs and the web content used for retrieval, allowing an application to generate answers with citations and inspect the supporting evidence. Search quality and source grounding can reduce unsupported claims, but the application and its language model remain responsible for how retrieved information is interpreted and presented.

## Can I restrict which sources Exa searches?

Yes. Use `includeDomains` to limit Search to selected domains or `excludeDomains` to remove unwanted sources. Exa also provides data categories for source-specific retrieval such as companies, people, news, and code. See Search best practices and Data.

## What security and data-retention options are available?

Exa offers security and compliance controls for production and enterprise use cases, including Zero Data Retention and HIPAA compliance for eligible Enterprise customers. See Security & Compliance for details.

## How does Exa pricing work?

API usage is billed from account credits according to the endpoint and options used. New accounts receive free credits, and paid usage is pay-as-you-go unless your organization has an enterprise contract. See Pricing and Billing.

# Monitors API
URL: https://exa.ai/docs/monitors/quickstart.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Monitors API

> Run recurring searches and receive newly discovered results by webhook.

Monitors run Exa searches on a recurring schedule and deliver results to a webhook endpoint.

Use Monitors to follow news, competitor announcements, funding rounds, regulatory changes, research
publications, or any other topic that changes over time.

## How Monitors work

On each run, Exa executes the configured search, filters by time, removes results or findings the
monitor has already returned, and sends the new output to your webhook.

Each monitor keeps its own run history, so write the query around the ongoing signal you want to
track rather than adding a moving date range yourself.

## Create your first monitor

Create a monitor with a search query, an interval, and the HTTPS endpoint that will receive
updates:

```python
from exa_py import Exa

exa = Exa()

monitor = exa.monitors.create({
    "name": "Battery recycling expansion",
    "search": {
        "query": "new battery recycling facilities announced in North America"
    },
    "trigger": {
        "type": "interval",
        "period": "1d",
    },
    "webhook": {
        "url": "https://example.com/webhooks/exa",
        "events": ["monitor.run.completed"],
    },
})

print(monitor.id)
print(monitor.webhook_secret)

```

```javascript
import Exa from "exa-js";

const exa = new Exa();

const monitor = await exa.monitors.create({
  name: "Battery recycling expansion",
  search: {
    query: "new battery recycling facilities announced in North America"
  },
  trigger: {
    type: "interval",
    period: "1d"
  },
  webhook: {
    url: "https://example.com/webhooks/exa",
    events: ["monitor.run.completed"]
  }
});

console.log(monitor.id);
console.log(monitor.webhookSecret);

```

```bash
curl -s -X POST "https://api.exa.ai/monitors" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "name": "Battery recycling expansion",
    "search": {
      "query": "new battery recycling facilities announced in North America"
    },
    "trigger": {
      "type": "interval",
      "period": "1d"
    },
    "webhook": {
      "url": "https://example.com/webhooks/exa",
      "events": ["monitor.run.completed"]
    }
  }'

```

## Example response

```json
{
  "id": "01k4d9w6y3h7p2m8n5q1r0s4tv",
  "name": "Battery recycling expansion",
  "status": "active",
  "search": {
    "query": "new battery recycling facilities announced in North America"
  },
  "trigger": {
    "type": "interval",
    "period": "1d"
  },
  "outputSchema": null,
  "metadata": null,
  "webhook": {
    "url": "https://example.com/webhooks/exa",
    "events": ["monitor.run.completed"]
  },
  "nextRunAt": null,
  "createdAt": "2026-09-05T20:00:00.000Z",
  "updatedAt": "2026-09-05T20:00:00.000Z",
  "webhookSecret": "<one-time-webhook-signing-secret>"
}

```

Store `webhookSecret` when you create the monitor. It is returned only once and is required to
verify webhook signatures.

## Configure the output

Every completed run returns newly discovered pages in `output.results`.

Exa also synthesizes findings from each page into `output.content`:

| Output shape | How to use | Returned value |
| --- | --- | --- |
| Text summary | Default | A string in `output.content` |
| Structured JSON | Add an object `outputSchema` | JSON matching the schema in `output.content` |

Sources for synthesized fields are returned automatically in `output.grounding`.

Add `outputSchema` when downstream code needs consistent
fields:

```json
{
  "outputSchema": {
    "type": "object",
    "properties": {
      "announcements": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "company": { "type": "string" },
            "location": { "type": "string" },
            "announcement": { "type": "string" }
          },
          "required": ["company", "location", "announcement"]
        }
      }
    },
    "required": ["announcements"]
  }
}

```

Keep citations and confidence out of the schema. They are returned separately in
`output.grounding`.

## Add page content

`search` accepts the same options as Exa Search: use `contents` to include
highlights, full text, or summaries with each result, and `includeDomains` or `excludeDomains` to
constrain sources.

```python
monitor = exa.monitors.create({
    "name": "LLM Research Tracker",
    "search": {
        "query": "new large language model training techniques and architectures",
        "numResults": 10,
        "contents": {
            "highlights": True
        }
    },
    "trigger": {
        "type": "interval",
        "period": "7d"
    },
    "webhook": {
        "url": "https://example.com/webhooks/exa",
        "events": ["monitor.run.completed"]
    }
})

```

```javascript
const monitor = await exa.monitors.create({
  name: "LLM Research Tracker",
  search: {
    query: "new large language model training techniques and architectures",
    numResults: 10,
    contents: {
      highlights: true
    }
  },
  trigger: {
    type: "interval",
    period: "7d"
  },
  webhook: {
    url: "https://example.com/webhooks/exa",
    events: ["monitor.run.completed"]
  }
});

```

```bash
curl -s -X POST "https://api.exa.ai/monitors" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "name": "LLM Research Tracker",
    "search": {
      "query": "new large language model training techniques and architectures",
      "numResults": 10,
      "contents": {
        "highlights": true
      }
    },
    "trigger": {
      "type": "interval",
      "period": "7d"
    },
    "webhook": {
      "url": "https://example.com/webhooks/exa",
      "events": ["monitor.run.completed"]
    }
  }'

```

## Test your monitor

Trigger a run immediately instead of waiting for the next scheduled time, then list its runs:

```python
exa.monitors.trigger(monitor.id)

runs = exa.monitors.runs.list(monitor.id, limit=1)
latest = runs.data[0]
print(latest.id, latest.status)

```

```javascript
await exa.monitors.trigger(monitor.id);

const runs = await exa.monitors.runs.list(monitor.id, { limit: 1 });
const latest = runs.data[0];
console.log(latest.id, latest.status);

```

```bash
curl -s -X POST "https://api.exa.ai/monitors/$MONITOR_ID/trigger" \
  -H "Authorization: Bearer $EXA_API_KEY"

curl -s "https://api.exa.ai/monitors/$MONITOR_ID/runs?limit=1" \
  -H "Authorization: Bearer $EXA_API_KEY"

```

Run statuses are:

| Status | Meaning |
| --- | --- |
| `pending` | The run is queued |
| `running` | The run is executing |
| `completed` | The run finished; fetch it by ID to read its full output |
| `failed` | The run failed; `failReason` says why |
| `cancelled` | The run was cancelled |

`output` is null until the run completes.

## Schedule runs

The minimum interval is one hour. Use a single duration such as `1h`, `6h`, `1d`, or `7d`. The
schedule is anchored to the monitor's creation time — a daily monitor created at 2:30 PM runs
daily around 2:30 PM — but each run may be delayed by up to 30 minutes, so do not rely on an
exact wall-clock delivery time.

Omit `trigger` to create a manual-only monitor. Pausing a scheduled monitor also stops automatic
runs while preserving manual triggers.

Monitor runs do not overlap. If the next scheduled run starts while the previous one is still
running, Exa cancels the previous run.

## Receive webhook updates

Subscribe to `monitor.run.completed` when you only need finished runs. If you omit `events`, Exa
sends monitor lifecycle events and run-created events as well.

The completed-run payload includes the run status and output. Optional monitor `metadata` is
echoed in webhook deliveries, which lets you route an update back to the correct customer,
workspace, channel, or internal job.

## Completed-run webhook payload

The output and timestamps are shortened below.

```json
{
  "id": "event_...",
  "object": "event",
  "type": "monitor.run.completed",
  "data": {
    "id": "01k...",
    "monitorId": "01k...",
    "status": "completed",
    "output": {
      "results": [
        {
          "title": "New battery recycling facility announced",
          "url": "https://example.com/announcement"
        }
      ],
      "content": "...",
      "grounding": [
        {
          "field": "content",
          "citations": [
            {
              "title": "New battery recycling facility announced",
              "url": "https://example.com/announcement"
            }
          ],
          "confidence": "high"
        }
      ]
    },
    "failReason": null,
    "metadata": {
      "workspace_id": "workspace_123"
    }
  },
  "createdAt": "2026-09-05T20:00:00.000Z"
}

```

Your webhook must use HTTPS and be the final destination because redirects are not followed.
Verify `Exa-Signature` before processing the event.

Every delivery includes an `Exa-Signature` header in the form `t=,v1=`.
Construct `. `, compute its HMAC-SHA256 digest with the one-time
`webhookSecret`, and compare the result with `v1` using a constant-time comparison.

```python
import hashlib
import hmac

def verify_webhook(payload: bytes, signature_header: str, secret: str) -> bool:
    parts = dict(part.split("=", 1) for part in signature_header.split(","))
    signed_payload = parts["t"].encode() + b"." + payload
    expected = hmac.new(secret.encode(), signed_payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, parts["v1"])

```

```javascript
import crypto from "crypto";

function verifyWebhook(payload, signatureHeader, secret) {
  const parts = Object.fromEntries(
    signatureHeader.split(",").map((part) => part.split("=", 2))
  );
  const expected = crypto
    .createHmac("sha256", secret)
    .update(`${parts.t}.`)
    .update(payload)
    .digest("hex");
  const actualBuffer = Buffer.from(parts.v1 ?? "", "hex");
  const expectedBuffer = Buffer.from(expected, "hex");

  return (
    actualBuffer.length === expectedBuffer.length &&
    crypto.timingSafeEqual(actualBuffer, expectedBuffer)
  );
}

```

## Next steps

## Create a monitor

See every search, schedule, output, metadata, and webhook field.

## Monitor runs

Inspect a run's status, output, grounding, and failure reason.

## Search guide

Configure queries, filters, highlights, full text, and freshness.

## Search best practices

Improve retrieval quality while keeping output focused.

# Websets
URL: https://exa.ai/docs/websets/quickstart.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Websets

> Build verified, enriched datasets from the web.

## What Are Websets?

A Webset starts with a natural-language query and a target item count. Add criteria that every result must satisfy and enrichment fields to populate for each accepted item. Results arrive asynchronously through the dashboard, API, or webhooks.

You can also build websets visually in the Dashboard, no code
required.

Starting a new list-building or enrichment workflow? Use Exa Agent.
Use this guide to maintain or extend an existing Websets integration.
The Websets API requires a paid Websets plan; Search API credits and Websets credits are separate.

## How It Works

1. Define a search: Provide a natural-language query, a result count, and optional verification criteria and enrichments.
2. Search and verify: Websets finds candidates and checks each one against your criteria. Only matching results become items.
3. Run enrichments: For each verified item, Websets searches for the additional data you requested, such as a CEO name, funding amount, or contact information.
4. Receive results: Poll for status, use webhooks for updates, or check the dashboard as items arrive.

## Choosing a result count

`count` is a target, not a guarantee. Websets keeps searching until it has found that many items that pass every criterion, or until it runs out of candidates that could match, so the final item count can be lower than requested. Small websets finish in minutes; requests for 1,000+ items scan a much larger candidate pool and take significantly longer. The Free plan caps a webset at 25 verified results.

For large or exhaustive lists, use Agent Ultra. It runs Exa Agent at its
highest effort, accepts a `budget` (`maxCostDollars`, `maxDurationSeconds`) so you control cost
and duration, and returns what it has found when the budget is reached.

## Key Capabilities

| Feature | What It Does |
| --- | --- |
| Criteria verification | Each result is checked against rules you define, so you only get relevant matches |
| Enrichments | Extract specific data points (text, numbers, dates, booleans) for every result |
| Monitors | Schedule recurring searches to keep your webset updated automatically |
| Webhooks | Get real-time HTTP callbacks as items are added or enriched |
| Imports | Bring your own URLs and run enrichments on them |

## Human Quickstart

## Get your Exa API key

Create a key in the dashboard. New accounts start with free credits.

Install the SDK:

```bash
pip install exa-py

```

```bash
npm install exa-js

```

Then make your first request:

```python
from exa_py import Exa
from exa_py.websets.types import CreateWebsetParameters, CreateEnrichmentParameters
import os

exa = Exa(api_key=os.getenv("EXA_API_KEY"))

webset = exa.websets.create(
    params=CreateWebsetParameters(
        search={
            "query": "Top AI research labs focusing on large language models",
            "count": 5
        },
        enrichments=[
            CreateEnrichmentParameters(
                description="LinkedIn profile of VP of Engineering or related role",
                format="text",
            ),
        ],
    )
)

print(f"Webset created with ID: {webset.id}")
print(f"View your Webset at: {webset.dashboard_url}")

# Wait until Webset completes processing
webset = exa.websets.wait_until_idle(webset.id)

# Retrieve Webset Items
items = exa.websets.items.list(webset_id=webset.id)
for item in items.data:
    print(f"Item: {item.model_dump_json(indent=2)}")

```

```javascript
import Exa from "exa-js";

const exa = new Exa(process.env.EXA_API_KEY);

const webset = await exa.websets.create({
  search: {
    query: "Top AI research labs focusing on large language models",
    count: 10
  },
  enrichments: [
    { description: "Estimate the company's founding year", format: "number" }
  ],
});

console.log(`Webset created with ID: ${webset.id}`);
console.log(`View your Webset at: ${webset.dashboardUrl}`);

const idleWebset = await exa.websets.waitUntilIdle(webset.id, {
  timeout: 60000,
  pollInterval: 2000,
  onPoll: (status) => console.log(`Current status: ${status}...`)
});

const items = await exa.websets.items.list(webset.id, { limit: 10 });
for (const item of items.data) {
  console.log(`Item: ${JSON.stringify(item, null, 2)}`);
}

```

```bash
curl -s -X POST "https://api.exa.ai/websets/v0/websets/" \
  -H "accept: application/json" \
  -H "content-type: application/json" \
  -H "Authorization: Bearer ${EXA_API_KEY}" \
  -d '{
    "search": {
      "query": "Top AI research labs focusing on large language models",
      "count": 5
    },
    "enrichments": [
      {"description": "Find the company'\''s founding year", "format": "number"}
    ]
  }'

```

See Zero Data Retention for product availability.

## Plans and credits

Websets is billed in Websets credits, which are separate from Search API credits. Verified results, enrichments, contact data, imports, and API previews each consume credits; current rates, plan comparison, and top-ups are on your Websets billing page. Exa Agent is billed pay-as-you-go from your API account instead — see Agent pricing.

## Not getting enough results?

Websets only returns items that pass every criterion, so a short or empty webset usually means the search is over-constrained rather than broken.

- Loosen the narrowest criterion. Remove or broaden the most restrictive rule and search again. Each criterion should be verifiable from public web pages.
- Ask for a list, not an answer. Websets finds entities that match attributes. Open-ended questions ("how is the European economy doing?") and single-fact lookups belong in Search.
- Split rare intersections. Find the broader set first, then capture the rare attribute as an enrichment instead of a criterion.
- Widen without starting over. Use Find more results in the dashboard, or create another search on the same webset.

If the list needs multi-step research — find entities, then verify hard-to-check criteria for each one — Exa Agent runs that loop for you. See Writing list-building and enrichment queries.

## Next

- Dashboard Guide - Step-by-step guide to using Websets in the dashboard
- How to Use Imports - Import your own URLs, then enrich, score, and expand the list
- Websets API Reference - Full API reference for all endpoints
