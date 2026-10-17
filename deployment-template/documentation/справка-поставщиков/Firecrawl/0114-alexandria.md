> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: alexandria

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/features/alexandria

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/features/alexandria#content-area)

PodcastsFinanceRetail

Pause

〉Find podcast conversati

Alexandria gives agents access to structured data through Firecrawl. Discover a tool, inspect its inputs, then run it. Discovery is free; execution uses the credits listed on the tool.[Browse providers](https://www.firecrawl.dev/app/alexandria) · [Manage provider terms](https://www.firecrawl.dev/app/settings?tab=data-sources)

## [​](https://docs.firecrawl.dev/features/alexandria\#built-for-agents)  Built for agents

Install the [CLI](https://docs.firecrawl.dev/sdks/cli) or connect the [MCP server](https://docs.firecrawl.dev/mcp-server).

- Firecrawl CLI

## - MCP


```
# Find tools alongside web results.
firecrawl search "podcast conversations about AI agents" --sources web,alexandria --domain-tools --limit 2

# Inspect inputs and pricing.
firecrawl find-tools --providers particle --level tools --expand options,response

# Run the tool.
firecrawl scrape particle/podcasts/episodes/search --options '{"keyword_search":"AI agents","limit":2}'
```

Install with `npm install -g firecrawl-cli` and sign in with `firecrawl login`.

Ask your agent: “Find Particle’s podcast tools, inspect episode-search inputs and pricing, then find conversations about AI agents.”The agent uses `firecrawl_search` to discover tools, `firecrawl_find_tools` to inspect them, and `firecrawl_scrape` to execute them.

## [​](https://docs.firecrawl.dev/features/alexandria\#use-it-from-the-sdks-and-api)  Use it from the SDKs and API

1

Find the right tool

Describe what you need. Alexandria returns relevant tools alongside your web results.

JavaScript

Python

cURL

```
const result = await firecrawl.search(
  "podcast conversations about AI agents",
  {
    sources: ["web", "alexandria"],
    limit: 2,
  },
);
```

```
result = firecrawl.search(
    "podcast conversations about AI agents",
    sources=["web", "alexandria"],
    limit=2,
)
```

```
curl https://api.firecrawl.dev/v2/search \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "query": "podcast conversations about AI agents",
  "sources": [\
    "web",\
    "alexandria"\
  ],
  "limit": 2
}'
```

Results contain `web` pages and ranked `tools`. Each tool includes its provider, capability, inputs, response contract, and price.

2

Check what it needs

Read the selected tool’s `options`, `response`, and execution price before calling it. Use [Find Tools](https://docs.firecrawl.dev/features/alexandria#find-tools) for more detail.

3

Get the data

Use `scrape` to call the tool with the inputs from its contract. Supply the provider and capability under `alexandria`; no page URL is needed.

JavaScript

Python

cURL

```
const episodes = await firecrawl.scrape({
  alexandria: {
    provider: "particle",
    capability: "podcasts/episodes/search",
    options: {
      semantic_search: "AI agents",
      limit: 2,
    },
  },
});

console.log(episodes.alexandria[0].data);
```

```
episodes = firecrawl.scrape(
    alexandria={
        "provider": "particle",
        "capability": "podcasts/episodes/search",
        "options": {
            "semantic_search": "AI agents",
            "limit": 2,
        },
    },
)

print(episodes.alexandria[0].data)
```

```
REQUEST_ID="$(uuidgen)"

curl https://api.firecrawl.dev/v2/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -H "x-request-id: $REQUEST_ID" \
  -d '{
  "alexandria": {
    "provider": "particle",
    "capability": "podcasts/episodes/search",
    "options": {
      "semantic_search": "AI agents",
      "limit": 2
    }
  }
}'
```

Read the result from `episodes.alexandria[0].data`. Check each tool result for errors before using its data. Raw HTTP responses wrap the SDK result in `data`.

## [​](https://docs.firecrawl.dev/features/alexandria\#find-tools)  Find Tools

Use `findTools` / `find_tools` to browse providers and inspect their tools for free. Follow an item’s `next` request for more detail; the top-level `next` paginates the catalogue.

JavaScript

Python

```
const catalogue = await firecrawl.findTools({
  providers: ["particle"],
  limit: 2,
});

// Each next request reveals another part of the catalogue.
const next = catalogue.items[0]?.next;
if (next) {
  const details = await firecrawl.scrape({ alexandria: next });
  console.log(details.alexandria[0].data);
}
```

```
catalogue = firecrawl.find_tools(providers=["particle"], limit=2)

if catalogue.items and catalogue.items[0].get("next"):
    details = firecrawl.scrape(alexandria=catalogue.items[0]["next"])
    print(details.alexandria[0].data)
```

## [​](https://docs.firecrawl.dev/features/alexandria\#pricing-and-access)  Pricing and access

- **Tool discovery:** free. Use `sources: ["alexandria"]` for tools only, or `["web", "alexandria"]` to include paid web results.
- **Execution:** charged at the tool’s listed price.
- **Provider terms:** a `THIRD_PARTY_DATA_TERMS_REQUIRED` error includes `requiresAction.url`. An org admin must review and accept the terms there. Agents need explicit user authorization before accepting terms. [Agent](https://docs.firecrawl.dev/features/agent#data-providers-that-need-terms) runs skip providers whose terms your team hasn’t accepted and report them in `exchange.skippedProviders`.

Find tools for a website

Add `domainTools: true` to a search or ordinary URL scrape to include tools matched to the website. Matching is free; the web search or page scrape is billed normally. Results include `matchedBy` and `matchedUrls`.Search enables domain matching by default when `sources` includes `alexandria`; set `domainTools: false` to disable it. For URL scrapes, domain matching is off by default.

## [​](https://docs.firecrawl.dev/features/alexandria\#feedback)  Feedback

Report issues or request capabilities with `firecrawl alexandria feedback`. Run `firecrawl alexandria feedback --help` for options.

Bounty: 5,000 credit reward for solid feedback on Alexandria

To qualify, complete a high-signal interview (thoughtful, concrete use cases, etc) with our Firecrawl Feedback Assistant. Only takes a few minutes, can be stopped at any time, and is both human/agent-friendly (just paste the link into your agentic harness!). Haven’t used Alexandria yet? Your take still counts.

[Start the interview](https://www.firecrawl.dev/survey/uilpn?src=docs-alexandria)

Include your email to be eligible. Interviews are reviewed for quality at the end of each week.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/features/alexandria.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/features/alexandria)

✕
