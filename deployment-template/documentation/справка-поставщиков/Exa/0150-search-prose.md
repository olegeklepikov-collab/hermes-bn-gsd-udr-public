> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Exa: search-prose

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Exa Search API
URL: https://exa.ai/docs/search/quickstart.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Exa Search API
> Search the web in natural language and get clean, relevant page content in one request.
Exa Search takes a natural language query and returns ranked web results with clean page content.
## Make your first request
Start with a `query` in natural language and `contents: { highlights: true }`, which returns excerpts sized to each result's relevance. Other fields control how Exa searches and what each result includes; the rest of this page covers the ones you will actually use.
Search returns up to 10 results by default. Set `numResults` to request up to 100 results; fewer may be returned when fewer relevant pages are available. Search does not support pagination.
## Example response
Highlights and the list below are shortened.
Results are ranked by relevance. Each one carries metadata such as title, URL, and publication date, plus whatever you requested under `contents`.
## Writing queries
The `query` field is the only required field when using the Search API.
Write queries in natural language. Include the subject and, when useful, the kind of source and time period you want.
Queries can be broad and exploratory. `"Latest news on EU battery policy"` gives Exa enough intent to discover relevant pages; `"news"` does not. When the source type matters, name it in the query:
See What's in Exa's Index for what Exa's index includes and how to search those content types.
Choose a search type
`type` selects a search mode, each tuned for a different balance of speed, search depth, and synthesis. `auto` is the default and works for most searches.
| Type | Use it when | Typical latency |
| --- | --- | --- |
| `auto` | You want the best default balance of quality and speed | ~1 second |
| `fast` | The request is latency-sensitive | ~450 ms |
| `instant` | The request is on a real-time path such as autocomplete or voice | ~250 ms |
| `deep-lite` | The task needs lightweight research and synthesis | ~4 seconds |
| `deep` | The task requires multi-step search and stronger synthesis | 4–15 seconds |
| `deep-reasoning` | Completeness and reasoning depth matter more than latency | 12–40 seconds |
`instant` costs $4 per 1,000 requests with up to 10 results.
Latency figures are approximate and cover the search itself with cached content. `outputSchema` adds a synthesis step and a low `contents.maxAgeHours` adds a fresh page fetch; see Budget latency and context.
Deep modes run a research process rather than a single retrieval pass. See Deep Search for how that process works and how to use its additional controls.
Instead of `deep-reasoning`, use Exa Agent for long-running research, list
building, and multi-hop enrichment. Agent has more compute per run and returns grounded,
structured results.
## Output shapes
Every result includes metadata such as its title, URL, and publication date. Use `contents` to add highlights, full text, or a summary from the page.
## Highlights
Highlights return the excerpts most relevant to your query. They give models and agents the
evidence they need without filling the context window with unrelated parts of each page.
This is the recommended output shape for most tasks.
Start with bare `highlights: true`. Exa uses the query to select an appropriate amount of
content from each result.
See Highlights for Dynamic Highlights and guidance on when to enable it.
## Full text
Full text returns the clean page body. Use it when the task depends on broader context, document
structure, or details that may fall outside query-focused excerpts.
Full pages can be large. Limit both the number of results and the text returned per page.
Pick one content view per request. Requesting both highlights and text returns and bills two views of the same page. `summary` is a third option, but it adds a language model call for every result.
`/search` and `/contents` accept the same content options in different places:
- `/search` nests `highlights`, `text`, and `summary` inside the `contents` object:
`"contents": { "highlights": true }`
- `/contents` has no `contents` wrapper. Its body is the content options themselves, so the
same fields sit at the top level next to `urls`: `"urls": [...], "highlights": true`
## Output schema
Add `outputSchema` when you want Exa to synthesize the search results. It works with every search type and adds an `output` object to the response.
The ranked pages remain in `results`. The generated value is returned in `output.content`, with field-level sources and confidence in `output.grounding`.
## Freeform Text
Use `type: "text"` for generated prose. Add a `description` to specify its format or length.
## Structured JSON
Use `type: "object"` for JSON that follows the properties and requirements you define.
Use `systemPrompt` for instructions such as source preferences or emphasis; use `outputSchema` for the response shape. Python uses `system_prompt` and `output_schema`.
Object schemas are capped at 10 properties in total (nested and array `items` properties count) and
2 levels of nesting. See Output schema limits. Do not add
citation or confidence fields to the schema; Exa returns them automatically in `output.grounding`.
## Filter results
Filters are hard constraints: add one when a result outside it would be unusable to you, and keep softer source preferences in the query text instead. The API reference has the full set.
### Include domains or paths
`includeDomains` restricts results to sources you trust. It accepts full domains, path prefixes such as `anthropic.com/news`, and subdomain wildcards such as `*.substack.com`.
Put the path in the filter rather than repeating it as a `site:` operator in the query.
### Exclude domains or paths
`excludeDomains` removes results from specific domains or paths. It supports the same path prefixes and subdomain wildcards as `includeDomains`. Use it when those sources would make a result unusable, not to express a preference.
## Content freshness
`contents.maxAgeHours` controls how fresh the content extracted from each result must be. It does not filter results by publication date.
| Value | Behavior |
| --- | --- |
| Omit | Use cached content when available and fetch the page when needed |
| Positive integer | Use cached content if it is newer than this many hours; otherwise fetch the page |
| `0` | Always fetch fresh content |
| `-1` | Only use cached content |
Most searches should omit this field. Set it when stale page content would be unusable, such as for prices, availability, or a page that changes frequently.
## Next steps
## Best practices
Token budgets, content freshness, structured output, and system prompts.
## API reference
Every request parameter and response field, with a live playground.
## Contents
You already have the URLs and want clean text, highlights, or summaries.
## Exa Agent
You need long-running research, list building, or enrichment.
# Deep Search
URL: https://exa.ai/docs/search/deep-search.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Deep Search
> Use iterative search, reasoning, and grounded synthesis for complex research tasks.
Deep Search is the research mode of the Search API. It uses the same `/search` endpoint, but the retrieval process can issue multiple searches, inspect the evidence, refine its approach, and synthesize a grounded result.
Use standard Search when you need ranked pages for a well-formed query. Use Deep when finding the answer requires research.
## How Deep Search works
Deep Search adds a research loop before the final response:
## Plan the search
Exa starts with your `query` and may expand it into searches that cover different parts of the
request. You can supply starting variations with `additionalQueries`.
## Search and inspect
Deep searches for evidence, compares the findings with the request, and determines what is
supported or still missing.
## Refine
When the evidence is incomplete or contradictory, Deep can issue a more targeted search instead
of returning the first plausible pages.
## Select and synthesize
Deep selects the useful results and then uses the same synthesis path as other search types.
When you provide `outputSchema`, the response includes structured `output.content` and
field-level citations in `output.grounding`.
This process is especially useful for lists and structured outputs. Each requested item may require a different search, and Deep can gather and check those results before producing the final structure.
## Choose a Deep mode
| Type | Use it when |
| --- | --- |
| `deep-lite` | You need lightweight query expansion and synthesis |
| `deep` | The task needs iterative search, evidence gathering, or multiple structured items |
| `deep-reasoning` | The task requires more deliberate reasoning across difficult or conflicting evidence |
Start with `deep` for research workflows. Move to `deep-lite` when the task is simpler and latency matters.
Instead of `deep-reasoning`, use Exa Agent for long-running research, list
building, and multi-hop enrichment. Agent has more compute per run and returns grounded,
structured results.
See Pricing for current cost and latency guidance.
## Make a Deep request
Set `type` on a normal Search API request:
Deep returns the selected search results under `results`. Add `outputSchema` when you also want a synthesized answer or structured dataset.
## Provide starting queries
Deep normally decides which searches to run. Use `additionalQueries` when you already know distinct terminology, perspectives, or subproblems that the research should cover:
The main `query` is always included. You can provide up to 10 additional queries, and the list is available only to Deep search types.
Do not provide minor rephrasings just to increase search volume. Add queries when each one contributes a meaningfully different search direction.
## Guide behavior and output separately
`systemPrompt` and `outputSchema` affect different parts of the request:
- `systemPrompt` guides source preferences, novelty, deduplication, and Deep's research behavior.
- `outputSchema` defines the final shape and triggers synthesis.
The query should describe what to research. The system prompt should describe how to conduct and present that research.
Prefer Deep when you need more than two structured items or each item must satisfy several requirements. Standard search types use the same synthesis path, but they do not perform the same iterative research before synthesis.
## Output schema limits
`outputSchema` is validated before the search runs. A request that breaks any of these rules is rejected with a `400` error.
| Limit | Rule |
| --- | --- |
| Properties | At most 10 properties in total, counted across every level of the schema. Properties inside nested objects and inside array `items` all count toward the 10. |
| Nesting | At most 2 levels of nested objects below the root. `companies` → `items` → `name` is fine; an object inside that item object is not. |
| Arrays | Every `type: "array"` field must define `items`. |
The funding example above uses 4 of the 10 properties: `companies`, plus `name`, `round`, and `amount` inside its items. A schema with 3 top-level fields and a nested object holding 8 more uses 11 and fails with `output_schema exceeds maximum of 10 properties`.
If you need more than 10 fields, split the work into several Deep requests with focused schemas, or use Exa Agent for wide enrichment tables.
## Read the grounded response
Structured responses separate generated values from their evidence:
Use `output.content` as the generated result and `output.grounding` to show or verify the sources supporting each field. Do not add citation or confidence fields to your own schema; Exa returns them automatically.
`numResults` controls how many selected pages are returned in `results`. It does not set the number of searches Deep may perform.
## Stream the synthesis
Set `stream: true` with `outputSchema` to receive the synthesized output over server-sent events:
Consume the typed events until `done`. The final event contains the completed output and search time, with cost information when available.
## When to stay with standard Search
Deep is unnecessary when one retrieval pass can satisfy the request:
- You need relevant pages, not a researched conclusion.
- The query already identifies a specific source or narrow topic.
- Your application performs its own reasoning and only needs retrieval.
- The request is on an interactive, autocomplete, or voice path.
Use `auto` for the default quality and speed balance, or `fast` and `instant` for measured latency requirements.
## Search API guide
Build requests, choose result content, and apply filters.
## Search best practices
Improve quality, context, latency, and agent integrations.
## Search API reference
See every request parameter and response field.
## Pricing
Review current Deep Search costs and latency.
# Search Best Practices
URL: https://exa.ai/docs/search/best-practices.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Search Best Practices
> Tune retrieval quality, latency, context, and synthesis for production Search API integrations.
This guide assumes you already have a working Search API request. It covers how to improve that request following Exa's recommended best practices.
## Start with the smallest useful request
The best baseline is a natural-language query with `highlights: true`. Exa sizes each result's excerpts to its relevance, so there is no character budget to tune:
This gives you ranked pages and token-efficient context per page, relevant to the query.
Add additional parameters only as needed:
| Parameter | Add it when |
| --- | --- |
| `type` | Adjusting to meet a latency budget or depth requirement |
| `numResults` | Fewer pages for a smaller context window, or more for broader recall |
| `objective` | An agent is searching as one step of a larger task; pass the goal that step serves |
| `outputSchema` | Synthesizing results or structuring them into JSON |
| `maxAgeHours` | Cached page content may be too old |
| `highlights.maxCharacters` | Your application requires a fixed excerpt limit per page |
| Domain or date filters | Results outside the constraint would be unusable |
## Search vs. Deep Search
Standard search retrieves and ranks pages for a query. Deep Search runs a research process that can
search iteratively, inspect what it found, refine the search, and synthesize a grounded result.
| Need | Start with |
| --- | --- |
| Ranked pages for a well-formed query | `auto` or `fast` |
| Difficult searches, synthesis across many results, or structured outputs that cannot be filled with a single search (3+ fields) | `deep` |
| Long-running research, list building, or multi-hop enrichment | Exa Agent |
Deep modes are recommended by default when using `outputSchema`. Read the Deep Search guide for full instructions and examples.
## Improve retrieval quality
When results need improvement, change one part of the request at a time.
## Clarify the query
Describe the pages you want, not a bag of keywords. Include the subject and any source type,
time period, or other detail that changes what a relevant result looks like.
## Read the response in layers
Look at the titles, URLs, publication dates, and highlights before changing the request.
The title and URL show the kind of source Exa retrieved, `publishedDate` shows
its recency, and the highlight shows the evidence that matched the query. Refine the query to
retrieve different pages, add date filters to narrow the time period, or fetch full text when
you need more context from a useful result.
## Add only hard constraints
Use `includeDomains`, `excludeDomains`, and publication-date filters only when a result that
violates the constraint cannot be used. Put retrieval preferences in the query and, when
synthesizing, put response instructions in `systemPrompt`.
## Change the search mode last
Use a faster mode for a latency requirement or a deep mode when the retrieval process itself
needs iteration and reasoning. A different mode cannot repair an underspecified query.
### Pass the objective from agents
`objective` is the broader goal behind a search: the task the search is one step of. The query says what to retrieve; the objective says what that task needs from the results, such as which documents should rank first, which to exclude, and which facts or figures to pull. It is most useful when a model picks the `query` as part of a larger task.
When you expose Search to a model as a tool, add `objective` as a required string parameter with a description that tells the model what the search turn is trying to achieve. We recommend the wording below verbatim, which is what the Exa MCP server uses:
The exa-py and exa-js `web_search` tool-calling helpers do this automatically.
If you define the tool manually, use the schema above.
Keep a small set of representative queries while tuning. Compare result relevance and downstream task success across the set instead of optimizing for one example. Record `requestId`, `searchTime`, and `costDollars` so regressions are reproducible.
## Budget latency and context
Each control spends a different resource:
| Control | What it adds |
| --- | --- |
| More results | More pages, response data, and downstream context |
| Full text | Broader page context and a larger payload |
| `summary` | One additional language model call per result |
| `outputSchema` | Synthesis across the retrieved results |
| `contents.maxAgeHours: 0` | A fresh page fetch instead of cached content |
| Deep search types | Iterative search, synthesis, and reasoning |
For a real-time path where cached content is acceptable, combine the lowest-latency mode with highlights and cache-only content:
Do not use this recipe when page freshness is part of correctness. Start from `auto` and default freshness unless the product has a measured latency target.
To let Exa allocate one context budget across the whole result set — more from strong sources, less from redundant ones — see the Dynamic Highlights research preview.
## Tips for common use cases
| If you need | Use | Avoid |
| --- | --- | --- |
| Newer publications | Put the time window in the query or use publication-date filters | `maxAgeHours` |
| Fresh content from pages that change | `contents.maxAgeHours` | Publication-date filters |
| A preferred kind of source | Query phrasing; `systemPrompt` when synthesizing | A hard domain allowlist |
| The task an agent's search serves | `objective` | Pasting the whole task description into `query` |
| Results only from approved sources | `includeDomains` | Repeating `site:` in the query |
| A small structured output | `outputSchema` with standard Search | Choosing Deep only because the output is JSON |
| A multi-item researched output | `deep` with `outputSchema`, or Exa Agent | Expecting one retrieval pass to gather every item |
| More context from a few pages | Search with highlights, then call Contents | Full text for every result |
| Lower latency | Measure `fast` or `instant` with compact content | Adding freshness or synthesis controls by default |
## Common mistakes
Requests copied from older examples often include parameters that are removed, deprecated, or belong somewhere else in the request. The API reference is the source of truth for the current schema.
| Instead of | Use |
| --- | --- |
| `useAutoprompt` | Nothing. Exa interprets the query directly; remove the field. |
| `includeUrls`, `excludeUrls` | `includeDomains`, `excludeDomains`. Each entry can be a hostname, a hostname with a path prefix, or a wildcard subdomain. |
| Top-level `text`, `highlights`, or `summary` | The same fields nested under `contents` (for example, `contents: { highlights: true }`). |
| `numSentences`, `highlightsPerUrl` | `contents.highlights: true`. Exa sizes highlights to each result; set `highlights.maxCharacters` only for a fixed excerpt limit. |
| `tokensNum` | `contents.text.maxCharacters`. |
| `livecrawl: "always"` | `contents.maxAgeHours: 0`. Do not send `livecrawl` and `maxAgeHours` together. |
| `contents.crawledBeforeDate` | `contents.snapshotAsOf`. |
| `contents.context` | `contents.highlights` or `contents.text`; build the context string from `results[]`. |
| `includeText`, `excludeText` | The terms in the query itself. Both filters are deprecated. |
| `startCrawlDate`, `endCrawlDate` | `startPublishedDate`, `endPublishedDate`. The crawl-date fields are ignored. |
A few behaviors that are easy to miss:
- The Python SDK uses snake_case for every key, including nested ones: `contents={"highlights": True, "max_age_hours": 24}`.
- `stream: true` returns server-sent events only when `outputSchema` is set. Without a schema, the response is the normal JSON body.
- `highlights`, `text`, and `summary` can be combined in one request, but each view is billed separately. Request one view unless the task needs both.
## When to use another endpoint
Use a different Exa endpoint when the task changes shape:
| Task | Use |
| --- | --- |
| Long-running research, list building, or enrichment | Exa Agent |
| The URLs are already known | Contents |
| Run a search on a schedule | Monitors |
## Next steps
## Search API reference
Every request parameter and response field.
## Search quickstart
Core request shapes, filters, output, and freshness.
## Contents API
Extract highlights or full text from pages you already know.
## Exa Agent
Long-running research, list building, and enrichment.
# Exa Snapshot
URL: https://exa.ai/docs/search/snapshot.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Exa Snapshot
> Pin Search and Contents to a stored version of a page at a datetime you choose.
Exa Snapshot keeps stored versions of pages Exa has crawled. Send `snapshotAsOf` to pin the request to a datetime.
Use this to backtest agents, run reproducible evals, and compare earlier versions of docs, pricing pages, policies, and filings.
Exa Snapshot is available on pay as you go at 10 QPS, with a rolling 5-month index window.
After 100 requests, talk to sales to continue.
## Search at a datetime
On `/search`, put `snapshotAsOf` inside `contents`.
Exa discovers candidate URLs, then keeps only pages with a stored version at or before `snapshotAsOf`.
## Example response
## Pin contents to a datetime
Add `snapshotAsOf` at the top level of a `/contents` request.
Exa returns the newest stored version at or before that datetime.
## Example response
IDs with no eligible version are omitted from `results` and reported in `statuses` with
`"status": "error"` and `"tag": "CONTENT_NOT_CACHED"`.
## How snapshots work
| Field | Where | Meaning |
| --- | --- | --- |
| `snapshotAsOf` | Request | Cutoff instant as an ISO 8601 date-time (`2026-06-01T00:00:00Z`) or date (`2026-06-01`, midnight UTC). Exa returns the newest stored version at or before this instant. |
For both endpoints:
- Returned page content comes from that stored version.
- Title, author, publication date, text, highlights, and summaries are generated only from that version.
- Pages without an eligible version in the 5-month window are omitted.
On Search, the cutoff bounds content, not ranking. Exa still uses current retrieval signals to
discover candidate URLs. Use the results as evidence bounded by `snapshotAsOf`, not as an exact
reconstruction of what a search would have ranked at that time.
## Limits and compatibility
## Access, rate limit, and lookback
Pay as you go includes 10 QPS and a rolling 5 months of index access. A `snapshotAsOf` older
than that window is rejected. After 100 requests, talk to sales
to continue.
## Historical requests use stored content
Do not combine `snapshotAsOf` with options that can reach the live web or expand to other pages.
Omit `livecrawl`, `livecrawlTimeout`, `maxAgeHours`, and `subpages` entirely; requests that set
any of them alongside `snapshotAsOf` are rejected with `INVALID_REQUEST`.
## Supported Search requests
Exa Snapshot on Search supports `auto`, `fast`, and `instant`. It does not support
`deep-lite`, `deep`, or `deep-reasoning`.
Exa Snapshot does not support the `category` parameter on Search.
## Common uses
Use Exa Snapshot when the task depends on what Exa had stored by a specific datetime:
- Backtest an agent without exposing it to later page updates.
- Run an evaluation against a repeatable content boundary.
- Compare earlier versions of documentation, pricing, policies, or filings.
# Contents API
URL: https://exa.ai/docs/contents/quickstart.md
> ## Documentation Index
> 
> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.
# Contents API
> Extract text, highlights, and summaries from any URL.
Exa Contents returns clean page content from URLs, handling JavaScript-rendered pages, PDFs, and complex layouts automatically.
All contents features are also available in Exa Search for returned URLs, at no extra charge up to 10 results per search ($1/1000 pages afterwards). We recommend using Search in this way instead of Contents for web search tool use cases.
For search results feeding AI context, request `contents: { highlights: true }` on `/search` —
Exa sizes each result's excerpts to its relevance. See Highlights.
## Make your first request
Pass one or more URLs or document IDs and request highlights for the parts relevant to your task. In HTTP requests, provide them in `ids`:
## Example response
Each item in `results` includes page metadata and the content view you requested. Check `statuses` for the success or failure of every URL.
Output shapes
## Highlights
Highlights return relevant passages copied from the page. Start here for agents, RAG, and
factual lookups because highlights keep context smaller than full text.
Set `highlights: true` to enable highlights. An additional `query` parameter is recommended when using Contents to focus content extraction from the page:
See Highlights for Dynamic Highlights and guidance on allocating context
across several pages.
## Full text
Full text returns the clean page body as markdown. Use it when the task depends on broad context,
document structure, or details that highlights may leave out.
Full pages can be large, so use `maxCharacters` when you need a limit:
## Summary
Summary makes a language model call for each page. Use it when you need a generated overview or
fields extracted into a JSON schema.
To extract fields instead of prose, pass a JSON schema in `summary.schema`. The summary comes
back as a JSON string matching the schema; parse it to read the fields:
Pick one content view per request. Requesting highlights, text, and summary together returns and bills each view separately.
## Content freshness
`maxAgeHours` controls how fresh the extracted page content must be.
| Value | Behavior |
| --- | --- |
| Omit | Use cached content when available and fetch the page when needed |
| Positive integer | Use cached content if it is newer than this many hours, otherwise fetch the page |
| `0` | Always fetch fresh content |
| `-1` | Only use cached content |
Most requests should omit this field. Set it when stale page content would be unusable, such as for prices, availability, or frequently updated pages. Pair a low `maxAgeHours` with `livecrawlTimeout` (milliseconds) to cap how long a fresh fetch may take.
## Migrate from the deprecated livecrawl parameter
The `livecrawl` string parameter (`"always"`, `"preferred"`, `"fallback"`, `"never"`) is
deprecated in favor of `maxAgeHours`:
| Old `livecrawl` value | Equivalent |
| --- | --- |
| `"always"` | `maxAgeHours: 0` |
| `"never"` | `maxAgeHours: -1` |
| `"fallback"` | Omit `maxAgeHours` |
| `"preferred"` | No direct equivalent; use a low value such as `maxAgeHours: 1` |
## Crawl subpages
Set `subpages` to follow links from each starting URL. Add `subpageTarget` when you want Exa to prioritize particular site sections:
## Images and favicons
Set `extras.imageLinks` to the number of image URLs you want from each page. Results also include
the site's `favicon` and a representative `image` URL when available. On `/search`, this option
sits at `contents.extras.imageLinks`.
## Common mistakes
`/contents` shares most of its options with `/search` but places them differently, and requests copied from older examples often carry parameters this endpoint never had. The API reference is the source of truth for the current schema.
| Instead of | Use |
| --- | --- |
| `contents: { text: ... }` | Top-level `text`, `highlights`, and `summary`. Unlike `/search`, `/contents` has no `contents` wrapper. |
| `useAutoprompt` | Nothing. There is no query to rewrite on `/contents`; remove the field. |
| `stream: true` | A normal request. `/contents` does not support streaming. |
| `numSentences`, `highlightsPerUrl` | `highlights: true`. Exa sizes highlights to each page; set `highlights.maxCharacters` only for a fixed excerpt limit. |
| `tokensNum` | `text.maxCharacters`. |
| `livecrawl: "always"` | `maxAgeHours: 0`. Do not send `livecrawl` and `maxAgeHours` together. |
| `crawledBeforeDate` | `snapshotAsOf`. |
| `context: true` | `highlights` or `text`; build the context string from `results[]`. |
A few behaviors that are easy to miss:
- `urls` and `ids` are interchangeable. Pass either the page URLs or the `id` values from a search response.
- A fresh fetch (`maxAgeHours: 0` or a low value) waits up to `livecrawlTimeout` milliseconds (default 10000). Raise it to 12000–15000 for slow sites, or lower it when latency matters more than freshness.
- The Python SDK uses snake_case for every key: `exa.get_contents(urls, highlights=True, max_age_hours=24)`.
## Next steps
## API reference
See every request parameter and response field.
## Highlights
Compare regular and Dynamic Highlights for agent and RAG context.
## Search API
Find relevant pages before extracting their content.
## SDKs
Use Exa from Python or JavaScript.
