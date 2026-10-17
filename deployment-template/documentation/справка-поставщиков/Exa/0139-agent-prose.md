> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Exa: agent-prose

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Exa Agent
URL: https://exa.ai/docs/agent/quickstart.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Exa Agent
> Run deep research, list-building, and enrichment workflows that return structured outputs.
Exa Agent is an async, usage-based endpoint for high-compute tasks like list building, enrichment, and deep research. It handles complex reasoning and can return many structured output fields.
Think of it as a context agent: you describe the data you want and the shape it should come back in, and Exa Agent orchestrates the tool calls needed to get there. A single run can fan out many searches across different angles, read and condense the pages behind them, split list building into subtasks that run in parallel, verify each candidate against your criteria, enrich contacts, and query any Exa Connect data partners you attach. You get the assembled context back as one grounded, structured result instead of orchestrating each `/search` and `/contents` call yourself.
Each run can return a natural-language answer, schema-validated JSON, field-level grounding, metadata, and a cost breakdown. You can retrieve completed runs later, list past runs, replay events, or continue from a previous run.
Prefer MCP? Exa Agent and Exa Connect are available in Exa MCP. Connect with OAuth or your API key and the `agent_run` tool is enabled by default, so you can run multi-step research, list-building, enrichment, and structured output from Claude, Cursor, and other MCP clients.
## When to use Exa Agent
Use Exa Agent when a workflow needs more than a single search or extraction call, or when you would otherwise write your own loop of searches, page reads, and verification steps to assemble the data:
- Build lists from open-ended criteria, then enrich each result
- Research entities across many fields with citations
- Run multi-hop tasks like "find companies, then find their decision makers"
- Produce structured JSON from a long-running web research task
- Combine web research with premium data partners in one grounded answer
- Continue from a previous run with a follow-up request like "find 10 more results"
Exa Agent is higher-latency and async by design. For a single low-latency search where you orchestrate the calls yourself, start with the Search API.
## Quickstart
This example starts a run that builds a structured list of people matching your criteria. It returns JSON in `output.structured`.
### 1. Install the Exa SDK
### 2. Set your API key
## macOS/Linux
## Windows
### 3. Create a run
Add `Accept: text/event-stream` when creating a run to receive server-sent events as the run is queued, started, and completed. See Stream events for more details.
### 4. Poll for completion
If you do not stream events, save the returned `id` and poll the run until it reaches a terminal status.
Completed runs include:
- `output.text`: a natural-language answer
- `output.structured`: validated JSON when you provide `outputSchema`
- `output.grounding`: citations for text or structured fields, when emitted
- `costDollars`: the run's cost breakdown
Exa Agent is also available through the OpenAI-compatible Responses API. Point
the OpenAI SDK at `https://api.exa.ai`, use `model: "exa-agent"`, and choose
synchronous, streaming, or background execution. See OpenAI SDK
compatibility.
## Verify and enrich a specific entity
Beyond list building, use Exa Agent to inspect a single known entity, verify a claim against authoritative sources, and return structured enrichment. This example checks whether a company's official website has a publicly accessible pricing page, and enriches the result with pricing details when they are available. The schema requires only `domain` and `verdict`; everything else is optional enrichment.
Schemas for verification workflows should account for uncertainty. Make
fields that may not be verifiable nullable and leave them out of `required`,
so the agent can return `null` instead of fabricating a value. The `verdict`
enum distinguishes a failed inspection (`cannot_verify`) from actual negative
evidence (`absent`): a site that could not be reached is not evidence that
the page does not exist.
## Stream events
Streaming keeps the create request open and sends Server-Sent Events (SSE) until the run completes. See Event format for the event types and payloads.
Set `stream=True` in Python, `stream: true` in JavaScript, or send `Accept: text/event-stream` over HTTP:
### Event format
Each SSE frame contains an event ID, event name, and JSON payload:
The stream may also contain comment lines such as `: keep-alive`. SSE clients ignore comments automatically; custom parsers should do the same.
### Event types
| Event | `data` payload | How to use it |
| --- | --- | --- |
| `agent_run.created` | `{ id, status: "queued", createdAt }` | Save the run ID as soon as the request is accepted. |
| `agent_run.started` | `{ id, status: "running" }` | Mark the run as actively processing. |
| `agent_run.completed` | The completed Agent run object | Read the final answer from `data.output.text` or `data.output.structured`, and citations from `data.output.grounding`. |
| `agent_run.failed` | `{ id, status: "failed", error }` | Surface `error.code` and `error.message`; no completed output is available. |
| `agent_run.cancelled` | `{ id, status: "cancelled", ... }` | Stop consuming the stream and handle the run as cancelled. |
Events associated with the same research step include a `callId`. It corresponds to `item.call_id` in tool progress events. Use it to group search traces, sources, and tool progress. Some search-trace descriptions are generated asynchronously and can arrive after the source or tool event they describe, so do not correlate them by arrival order alone.
Treat `agent_run.source.added` as a live preview rather than a complete citation list. The terminal run's `output.grounding` is the authoritative grounding output.
### Replay stored events
For non-ZDR runs, `GET /agent/runs/{id}/events` returns stored events as paginated JSON. Send `Accept: text/event-stream` to replay the stored events as SSE, and `Last-Event-ID` to skip events your client has already processed:
The replay endpoint sends the events stored at request time and then closes; it does not continue following a running run. ZDR runs do not retain events and cannot be replayed.
For forward compatibility, ignore event names your application does not recognize and continue until a terminal event arrives.
## Return structured JSON
Use `outputSchema` to return schema-validated JSON in `output.structured`.
`outputSchema` supports the JSON Schema specification.
Runs with a schema that no output can satisfy fail fast with a `400` `INVALID_OUTPUT_SCHEMA` error. For example, a root object with `additionalProperties: false` whose `required` list names a property missing from its `properties`.
To request contact information, describe the desired contact fields in `outputSchema`. Use standard JSON Schema shapes such as `{ "type": "string", "format": "email" }` for email addresses, `{ "type": "string", "format": "phone" }` for phone numbers, and `{ "type": "string", "format": "uri" }` for URLs. Bound list sizes with `maxItems` when possible so the maximum contact-enrichment cost is predictable.
## Process input rows
Use `input.data` when you have an existing set of data that you want to enrich. You can add more fields to each data entity, surface more entities based on the data you bring in, or both.
For complete row-enrichment examples, see Agent examples.
## Process exclusions
Use `input.exclusion` to exclude certain entries from being surfaced in the run. In the example below, we want to look for the top 10 cutest animals, but we exclude goats and pandas from the run because we already know how cute they are.
## Connect data sources
The index is already available on every run. Use `dataSources` only to attach Exa Connect partners. Each entry selects a `provider`. When a property in your `outputSchema` references a specific source (e.g., "from Similarweb"), Exa Agent calls the matching provider tool instead of guessing from a web page.
See Exa Connect for the full list of data partners, with examples for each.
## Continue from a previous run
Use `previousRunId` to ask follow-ups to a previous response. Each follow-up starts a new run with its own ID. `previousRunId` carries context into the new run; it is not reused as the new run's ID.
## Find a run ID
List recent runs and inspect their statuses:
## Pricing
Costs are usage-based and priced by component:
| Component | Price |
| --- | --- |
| Agent Compute Units | `1 ACU = $0.10` |
| Search tool calls | `$0.005 / search` |
Contact enrichment is separate from the core pricing components above: email contact enrichment is `$0.02 / email`, and phone number contact enrichment is `$0.07 / phone number`.
`usage.agentComputeUnits` measures model computation across the full run. Complex queries, especially ones with a large `input.data` field, need more reasoning steps and tool calls and consume more ACUs.
See Agent limits for concurrency and rate limits.
### Effort
Use `effort` to choose a cost and reasoning level for each run. The supported values are `minimal`, `low`, `medium`, `high`, `xhigh`, `auto`, and `ultra`; the default is `auto`. Fixed efforts have a predictable per-request price, while `auto` and `ultra` are metered by usage:
| Effort | Price |
| --- | --- |
| `minimal` | `$0.012 / request` |
| `low` | `$0.025 / request` |
| `medium` | `$0.10 / request` |
| `high` | `$0.50 / request` |
| `xhigh` | `$1.00 / request` |
| `auto` | Metered; up to the default `$5` cap |
| `ultra` | Metered; up to the default `$20` cap |
`budget.maxCostDollars` is an optional per-run ceiling for `auto` and `ultra`. It accepts `$1`–`$100`; the shipped maximum is `$100`, though the server may configure a lower maximum. The default cap is `$5` for `auto` and `$20` for `ultra`. This is a ceiling rather than a fixed price: runs that finish early cost less. Budget is not accepted for fixed efforts.
### Choosing an effort mode
Fixed effort modes work well when you want predictable per-request pricing for standard research. Use `auto` for variable-scope work like list building, where the number of entities can vary from request to request.
| Effort | Best for | Suggested schema complexity | Runtime expectation |
| --- | --- | --- | --- |
| `minimal` | Lowest-cost lookups, very narrow factual tasks, short answers | One or two fields, shallow schema | Cheapest, least exhaustive |
| `low` | Simple lookups, narrow factual tasks, short answers | A few fields, shallow schema | Fast, light research |
| `medium` | Default starting point for most standard research tasks | Moderate field count, simple nested objects | Balanced quality/runtime |
| `high` | Harder research, more citations, stricter completeness | Larger schemas or more nuanced fields | Slower, more thorough |
| `xhigh` | High-value tasks where completeness matters more than cost/latency | Complex schemas, many fields, difficult verification | Slowest fixed effort |
| `auto` | Variable-scope work, list building, unknown task difficulty | Flexible; useful when entity count or work required is unknown | Variable |
| `ultra` | Large list building, exhaustive research, hard-to-verify criteria | Complex schemas, many fields, difficult verification | Longest-running |
Start with `medium` for standard single-entity research. Drop to `low` or `minimal` when cost and latency matter more than completeness. Move up to `high` or `xhigh` when the output schema is larger, fields need verification, or the task needs deeper reasoning. Use `auto` when you don't know the scope ahead of time, such as list building or workflows that may return many entities. Use `ultra` when completeness matters more than latency or cost.
Runtime varies by query difficulty, schema complexity, and external source availability. Treat effort modes as quality/cost/runtime tradeoffs rather than strict latency guarantees.
## Agent Ultra
Run Exa Agent at its highest effort for large list building and exhaustive research.
## Zero Data Retention
Exa Agent supports Zero Data Retention (ZDR). ZDR is enabled per team. Contact us (sales@exa.ai) to enable it for your account.
When ZDR is enabled for your team:
- Create runs with streaming (`Accept: text/event-stream`) to consume output live, or poll asynchronous runs within the retention window.
- Run data is available while the run executes and for up to 10 minutes after it reaches a terminal state. After that window, the run cannot be retrieved.
- `previousRunId` is not available.
- Exa Connect `dataSources` are not available; requests that include them return a `400` error.
## Next steps
## What's in the index
Explore news, code, company, and people sources across the public web.
## Exa Connect
Attach premium partner databases to a run.
## Agent best practices
Best practices for using Exa Agent.
## Agent examples
Examples of using Exa Agent.
# Agent Best Practices
URL: https://exa.ai/docs/agent/best-practices.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Agent Best Practices
> Tune query quality, structured output, effort, and cost for production Exa Agent integrations.
Use this guide after the Exa Agent quickstart to improve query quality, structure outputs, and control runtime and cost. For complete requests, start with Agent examples.
## Core principles
Treat `query` as a task specification. Name what Agent should find, the scope of the work, the evidence required, and what a complete result looks like.
Without an `outputSchema`, Agent returns prose in `output.text` and citations in `output.grounding`. Add another field only when it has a clear job:
| Field | Use it when |
| --- | --- |
| `outputSchema` | Downstream code needs structured fields |
| `input.data` | You already have rows to enrich |
| `input.exclusion` | Known records should not be returned |
| `dataSources` | A field should come from an Exa Connect partner |
| `previousRunId` | The request continues a completed run |
| `effort` | Cost or research depth needs an explicit setting |
| `budget.maxCostDollars` | An `auto` or `ultra` run needs a hard cost ceiling |
Keep rows, exclusions, and response shape in their dedicated fields rather than embedding them in `query`.
## Writing list-building and enrichment queries
For list building, define the entity, target count, qualification criteria, exclusions, and evidence bar. For enrichment, put the existing records in `input.data` and describe only the research Agent should add.
Ask for a rationale when qualification requires judgment. Give examples only when a criterion has multiple plausible interpretations.
See Find all GTM members for a discovery request and Enrich input rows for the corresponding row-enrichment pattern.
## Handle asynchronous runs
Agent runs can take seconds to minutes while they search, read, and reason. Build around the lifecycle instead of holding an application request open.
## Create and persist
Create the run and save its returned `id` with your request metadata. The create response is not the final result.
## Wait for a terminal state
Use an SDK polling helper, poll `GET /agent/runs/{id}`, or consume the SSE stream. Continue while the run is `queued` or `running`.
## Store the result
Stop waiting at `completed`, `failed`, or `cancelled`, then persist the terminal response and grounding.
Persisting the run ID lets your application recover after a restart, reconnect to a stream, and inspect failures. Keep latency down by narrowing the scope, limiting result count, keeping the schema focused, and choosing `minimal` or `low` when speed matters more than completeness.
For batches, benchmark representative tasks before estimating concurrency or putting Agent on a synchronous UI path. Runtime varies with item count, schema complexity, source availability, and effort.
For Zero Data Retention teams, consume the live stream or poll within the retention window. `previousRunId` and Connect `dataSources` are not available. See Zero Data Retention.
## Write custom JSON schemas for structured output
Use `outputSchema` when downstream code needs machine-readable fields, normalized values, table rows, or enrichment records. If a prose answer is enough, omit it and read `output.text`; structured output adds formatting work and can increase latency.
Keep research instructions in `query` and response shape in `outputSchema`. Use clear property names and descriptions, choose the narrowest useful types, and bound arrays with `maxItems`.
Schema adherence validates shape, not facts. Agent may return `null` when evidence does not support a field, even if the submitted schema marks it as required or non-nullable. `stopReason: schema_satisfied` means Agent considers the expected shape complete with those nulls allowed; it does not guarantee strict validation against the submitted schema.
Do not duplicate Exa's built-in citations or confidence in your schema. Add a rationale field only when each item should explain why it qualifies, and persist `output.grounding` with the structured result. Verify important claims against their sources and test schema changes on representative inputs before shipping.
Browse the structured Agent examples to compare schemas for list building, KYB, job postings, exclusions, and continued runs.
## Agent vs Search
| Need | Start with |
| --- | --- |
| Web results for your LLM | Search |
| Fast research and synthesis | Deep Search |
| Async list building, multi-hop research, or enrichment | Agent |
Use Agent when the work requires several retrieval steps, per-entity verification, or enrichment over known records. Use Search when you need pages quickly and your application will perform the remaining reasoning.
## Tips for common use cases
| If you need | Use | Avoid |
| --- | --- | --- |
| A researched list of unknown size | `auto` and a bounded `outputSchema` | A fixed cheap effort and an unbounded array |
| Enrichment of records you already have | `input.data` plus fields to add | Pasting the table into `query` |
| A follow-up over the last result set | `previousRunId` | Re-sending the full previous output |
| Records that should not appear again | `input.exclusion` plus downstream deduplication | Treating exclusions as a strict identity guarantee |
| Premium provider data | Exa Connect with `dataSources` | Asking Agent to infer provider-only fields from the open web |
| Predictable per-request cost | A fixed `effort` | `auto` or `ultra` without a budget |
| Completeness over latency & cost | `xhigh` or `ultra` | Raising effort before tightening the query |
## Next steps
## Agent quickstart
Create a run, stream events, set effort, and read structured output.
## Agent examples
Copy complete list-building, enrichment, KYB, exclusion, and follow-up requests.
## Exa Connect
Add premium company, people, traffic, compliance, finance, and other provider data.
## Search best practices
Retrieval quality, latency, and synthesis when Search is enough.
# Agent Ultra
URL: https://exa.ai/docs/agent/agent-ultra.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Agent Ultra
> Run Exa Agent at its highest effort for large list building and exhaustive research.
Agent Ultra is Exa Agent's highest-effort mode. It runs longer and spends more compute than any other effort to return the most complete results.
Use it for large list building, deep multi-source research, and criteria that are hard to verify, where completeness matters more than latency or cost. For a predictable price per request, use a fixed effort instead.
Agent Ultra is metered at the standard Agent usage rates, up to a
default $20 per run. Runs that finish early cost less.
## Run Agent Ultra
Set `effort: "ultra"` on an Agent run. The rest of the request works like any other run, including `outputSchema`, `input.data`, and streaming.
Ultra runs typically complete complex tasks in about 30 minutes, but can take up to three hours for very challenging ones.
By default, the SDK polling helpers time out after one hour, so use a longer timeout as shown above or stream events for extended runs.
## Set a budget
Add `budget` to cap how much a run spends and how long it takes. Both fields are optional.
| Field | Accepts | Default |
| --- | --- | --- |
| `maxCostDollars` | $1 to $100 | $20 |
| `maxDurationSeconds` | 300 to 10,800 (5 minutes to 3 hours) | None |
As a run approaches either limit, the agent stops starting new work and returns what it has found.
## Stop a run early
Stop Agent Ultra run to end it now and keep what it has found. The run completes with `stopReason: "stopped"`, and you are billed for usage up to the stop.
## Stop reasons
`stopReason` on a finished run says why it ended. Every reason except `error` and `cancelled` means the run completed and returned what it found.
| `stopReason` | Meaning |
| --- | --- |
| `schema_satisfied` | The agent finished the task. |
| `budget_reached` | The run reached `budget.maxCostDollars`. |
| `time_limit_reached` | The run reached `budget.maxDurationSeconds`. |
| `stopped` | You stopped the run. |
| `error` | The run failed. |
| `cancelled` | The run was cancelled. |
## Limits and compatibility
## Ultra-only controls
`budget.maxDurationSeconds` and stopping a run early work only with `effort: "ultra"`.
`budget.maxCostDollars` also works with `auto`.
## OpenAI Responses API
On `/responses`, set
`reasoning.effort: "ultra"` with `stream: true` or `background: true`.
## Next steps
## Agent quickstart
Create runs, stream events, and read structured output.
## Agent examples
Copy complete list-building, enrichment, and follow-up requests.
# Exa Connect
URL: https://exa.ai/docs/agent/connect/overview.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Exa Connect
> Give your Exa Agent live access to premium data partners, alongside Exa web search, in a single run.
Exa Connect integrates premium data partners into the Exa Agent loop. Attach a
provider to a run, and the Exa Agent queries that partner's database alongside web
search before combining the results into one grounded, structured answer.
New to agent runs? Start with the Exa Agent guide,
then come back to attach data partners.
Exa Agent already searches the full data index, the same
news, code, company, and people sources as the Search API. Exa Connect adds
premium partner databases on top of it.
Prefer MCP? Exa Agent and Exa Connect are available in Exa MCP. Connect with OAuth or your API key and the `agent_run` tool is enabled by default, so you can run multi-step research, list-building, enrichment, and structured output from Claude, Cursor, and other MCP clients.
## Why Exa Connect
- Premium data without separate integrations. Access partner data without
signing contracts or wiring up an SDK. You call one Exa API.
- Exa handles the plumbing. We manage provider authentication, tool selection,
retries, and result ranking.
- The Exa Agent chooses the source. When your `outputSchema` asks for
"monthly visits from Similarweb" or "verified officers," the Exa Agent calls the
matching partner tool instead of guessing from a web page.
- Index and partner data in one run. Connect sits on top of the Exa index.
The Exa Agent uses each source where it is strongest and cites the results.
## How it works
1. Attach one or more providers via the `dataSources` array on
`POST /agent/runs`.
2. The Exa Agent selects the right tool for each step based on your query and
`outputSchema`: partner data or Exa web search.
3. Partner results are fused with web research into your structured output,
with sources attached.
## Pricing
Exa Connect pricing is additive with standard Agent run pricing.
You pay the usual Agent compute and search costs, plus the provider call charge for each Exa Connect tool call.
| Provider | Price |
| --- | --- |
| Fiber.ai | `$0.02 / credit` |
| Similarweb | `$0.30 / credit` |
| Baselayer | `$0.10 – $4.00 / order (varies by operation)` |
| Polymarket | `Free` |
| Macrobond | `Free` |
| Affiliate.com | `$0.015 / call` |
| Particle | `$0.015 / call` |
| Financial Datasets | `$0.01 / call` |
| Jinko | `$0.005 / call` |
Fiber.ai bills in credits rather than per call, because its own charge varies by
call: a search costs 2 credits plus 1 per result returned, a company or person
lookup is billed per candidate returned (so raising a company lookup's
`numResults` to disambiguate an ambiguous name costs more), and a contact
reveal 2–5 credits depending on whether you ask for work email, personal email,
or phone. You are charged the credits Fiber reports for each call; calls that
return no match are free. See Fiber.ai pricing.
Similarweb bills in data credits (roughly one per metric × row × month), so a
call's price follows its `numResults`/`months` — 1 to 15 credits per call. You
are charged the credits Similarweb reports for each call; calls that return no
data are free. See Similarweb pricing.
Baselayer bills per order, and the rate depends on the operation: a KYB
business search is $1.00, a UCC lien search is $2.00 per state searched, a
litigation/bankruptcy docket search is $1.00 per category, watchlist screening
is $0.10–$0.25 per list requested, industry classification and website
analysis are $0.35 each, web presence is the sum of the selected analyses
($0.15–$0.35 each), and an international business search is $4.00. Follow-up
reads of a prior business search (business lookup, officers, registrations,
officer reverse lookup) are free. See Baselayer pricing.
## Data partners
## Fiber.ai
GTM & recruiting. B2B database of companies and people for lead discovery
and contact research.
## Similarweb
Web analytics. Traffic estimates, global rankings, and competitor
discovery for any domain.
## Baselayer
Compliance & KYB. Verify US businesses: officers, registrations, and risk
signals.
## Polymarket
Prediction markets. Prediction market odds, price history, and trader
positions from Polymarket.
## Macrobond
Macroeconomic data. Global economic and financial time series, entity
metadata, and release calendars.
## Affiliate.com
Commerce. Product catalog search with pricing, brands, and merchant links.
## Particle
Media intelligence. Search podcast transcripts with speaker attribution
and timestamps.
## Financial Datasets
Finance. Prices, fundamentals, earnings, SEC filings, ownership, and
stock screening for 27,000+ U.S. tickers.
## Jinko
Travel. Flight and Hotel search with real-time pricing.
Need a source that isn't listed above? See our Additional providers, which are available upon request by contacting our team.
## Usage
### Combining providers
Attach as many partners as your task needs. The Exa Agent calls each one where it is
strongest and blends the results with web search into a single structured answer:
For a full walkthrough, including how to shape your query and `outputSchema` so every
partner fires, see Combining providers.
