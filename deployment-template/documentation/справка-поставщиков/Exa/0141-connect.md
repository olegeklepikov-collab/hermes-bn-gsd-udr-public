> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Exa: connect

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Macrobond
URL: https://exa.ai/docs/agent/connect/macrobond.md

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

# Macrobond

> Search and fetch macroeconomic and financial time series, entity metadata, and release calendars.

Macrobond aggregates macroeconomic and financial
time series from central banks, statistical offices, and other primary sources
worldwide. Exa Connect provides read-only access to
Macrobond's time-series catalog and data.

Attach `macrobond` to an Exa Agent run, and the agent
queries Macrobond alongside Exa web search.

## Use it for

- Finding the right series for an indicator (GDP, CPI, unemployment, policy rates) for a given country or region.
- Pulling recent observations for one or more series, with a cap on how many observations to return.
- Comparing series with different native frequencies or currencies on a shared calendar.
- Looking up a series' source, units, frequency, region, and date range without fetching data.
- Checking when an indicator is next scheduled to be published or revised.

## Provider ID

Use this value in `dataSources`:

```text
macrobond

```

## Pricing

Macrobond tool calls currently carry no per-call provider charge: you pay only
the standard Agent run pricing.

## Data available

| Data | Description |
| --- | --- |
| Series search | Free-text search over Macrobond's time-series catalog, optionally filtered by entity type or metadata attributes such as `Region` and `Frequency`. Returns metadata only. |
| Series observations | Dates and values plus metadata for up to 10 named series per call, keeping the most recent observations (100 by default, up to 2,000). |
| Unified series | Multiple series converted server-side to a shared frequency and optional currency, with aligned dates, for comparing series that differ natively. |
| Entity metadata | Full metadata for series, releases, regions, and sources: description, region, frequency, source, units, date range, and related entities. |
| Upcoming releases | Scheduled publication events for a release: expected and source release times, reference periods, and whether each event brings new or revised values. |

Macrobond entities have no public web URL. The agent identifies each series by its
Macrobond entity name (for example `usgdp` or `uscpi`), discovered through search,
and uses that name in every other Macrobond tool.

## Example

Compare US and euro-area headline inflation over the past two years and find the next US CPI release.

```python
from exa_py import Exa

exa = Exa()
run = exa.agent.runs.create(
    query=(
        "Compare year-over-year headline CPI inflation in the US and the euro "
        "area over the past two years, and tell me when the next US CPI "
        "release is scheduled."
    ),
    data_sources=[{"provider": "macrobond"}],
    output_schema={
        "type": "object",
        "required": ["usLatest", "euroAreaLatest", "comparison", "nextUsCpiRelease"],
        "properties": {
            "usLatest": {"type": "number", "description": "latest US YoY CPI inflation, percent"},
            "euroAreaLatest": {"type": "number", "description": "latest euro-area YoY CPI inflation, percent"},
            "comparison": {"type": "string", "description": "how the two paths diverged over the past two years"},
            "nextUsCpiRelease": {"type": "string", "description": "ISO 8601 timestamp of the next scheduled US CPI release"},
        },
    },
)
run = exa.agent.runs.poll_until_finished(run.id)

```

```typescript
import Exa from "exa-js";

const exa = new Exa();
const run = await exa.agent.runs.create({
  query:
    "Compare year-over-year headline CPI inflation in the US and the euro area over the past two years, and tell me when the next US CPI release is scheduled.",
  dataSources: [{ provider: "macrobond" }],
  outputSchema: {
    type: "object",
    required: ["usLatest", "euroAreaLatest", "comparison", "nextUsCpiRelease"],
    properties: {
      usLatest: { type: "number", description: "latest US YoY CPI inflation, percent" },
      euroAreaLatest: { type: "number", description: "latest euro-area YoY CPI inflation, percent" },
      comparison: { type: "string", description: "how the two paths diverged over the past two years" },
      nextUsCpiRelease: { type: "string", description: "ISO 8601 timestamp of the next scheduled US CPI release" },
    },
  },
});

```

```bash
curl -s -X POST "https://api.exa.ai/agent/runs" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "query": "Compare year-over-year headline CPI inflation in the US and the euro area over the past two years, and tell me when the next US CPI release is scheduled.",
    "dataSources": [{ "provider": "macrobond" }],
    "outputSchema": {
      "type": "object",
      "required": ["usLatest", "euroAreaLatest", "comparison", "nextUsCpiRelease"],
      "properties": {
        "usLatest": { "type": "number", "description": "latest US YoY CPI inflation, percent" },
        "euroAreaLatest": { "type": "number", "description": "latest euro-area YoY CPI inflation, percent" },
        "comparison": { "type": "string", "description": "how the two paths diverged over the past two years" },
        "nextUsCpiRelease": { "type": "string", "description": "ISO 8601 timestamp of the next scheduled US CPI release" }
      }
    }
  }'

```

## Pairs well with

- Exa web search: add central-bank commentary and news context to the numbers.
- Financial Datasets: connect macro series to company prices, fundamentals, and filings.
- Polymarket: compare official data and release dates with market-implied expectations.

## Next steps

## Attach it to a run

The Exa Connect quickstart covers `dataSources`, pricing, and the full partner catalog.

## Combine providers

Attach up to five partners to one run and shape the query so each one fires.

## Learn Exa Agent

Create runs, stream progress, design output schemas, and control effort and cost.

## Get an API key

Create a key in the dashboard and run this page's example as-is. New accounts start with free credits.

# Financial Datasets
URL: https://exa.ai/docs/agent/connect/financialdatasets.md

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

# Financial Datasets

> Structured financial and market data for 27,000+ U.S. tickers: prices, fundamentals, earnings, SEC filings, ownership, and stock screening.

Financial Datasets provides machine-ready
company and market data for AI agents. Through
Exa Connect, agents can retrieve
real-time and historical prices, company facts, financial statements and
valuation metrics, earnings, insider and institutional ownership, SEC filings
and filing sections, company news, and screen the U.S. market by fundamental
criteria.

Attach `financial_datasets` to an Exa Agent run,
and the agent queries Financial Datasets alongside Exa web search.

## Use it for

- Building structured company research snapshots.
- Analyzing financial performance, valuation, and historical trends.
- Reading SEC filings and extracting sections such as risk factors and MD&A.
- Examining insider transactions and institutional ownership.
- Screening the U.S. market by fundamental criteria.
- Monitoring company news and relevant developments.

## Data available

Each of the following datasets is available under the `financial_datasets`
provider; the agent selects whichever fits the task:

| Dataset | What it returns |
| --- | --- |
| Beneficial ownership | 5%+ beneficial owners from Schedules 13D/13G, including activist and passive stakes. |
| Company facts | Name, sector, industry, exchange, location, SEC CIK, SIC classification. |
| Company news | Recent news articles for a ticker. |
| Earnings | Quarterly revenue and EPS with YoY change and beat/miss surprises. |
| Financial metrics | Market cap, EV, P/E, P/B, P/S, EV/EBITDA, PEG, margins, ROE/ROA/ROIC, growth, EPS. |
| Financial statements | Income statement, balance sheet, and cash flow from SEC filings. |
| Historical stock prices | OHLCV bars over a date range at day/week/month/year granularity. |
| Index-fund holdings | ETF/index-fund constituents by weight, or the funds that hold a given security. |
| Insider ownership | Insider holdings from SEC Forms 3 and 5 (shares owned by officers, directors, 10% owners). |
| Insider trades | SEC Form 4 insider transactions (name, role, type, shares, value). |
| Institutional ownership | 13F institutional holders, shares, and reported value. |
| Interest rates | Current and historical central-bank policy rates (Fed, ECB, BOJ, and more). |
| SEC filing items | Extracted text of specific 10-K/10-Q/8-K items (e.g. risk factors, MD&A). |
| SEC filings | Filing metadata and direct EDGAR links, optionally filtered by form type. |
| Segmented financials | Revenue, operating income, and other line items broken down by product, business segment, and geography. |
| Stock price snapshot | Current real-time price, day change, and quote time. |
| Stock screener | Companies matching fundamental filter criteria. |

## Provider ID

Use this value in `dataSources`:

```text
financial_datasets

```

## Example

Build a structured company-research snapshot for NVIDIA.

```python
from exa_py import Exa

exa = Exa()
run = exa.agent.runs.create(
    query=(
        "Analyze NVIDIA using its latest price, valuation metrics, most recent "
        "quarterly financial statements and earnings, institutional and insider "
        "activity, and material SEC filing sections. Return a structured "
        "company-research snapshot with reporting dates."
    ),
    data_sources=[{"provider": "financial_datasets"}],
    output_schema={
        "type": "object",
        "required": ["ticker", "price", "valuation", "financials", "earnings", "ownership", "filings"],
        "properties": {
            "ticker": {"type": "string"},
            "price": {
                "type": "object",
                "required": ["latest", "asOf"],
                "properties": {
                    "latest": {"type": "number"},
                    "asOf": {"type": "string"},
                },
            },
            "valuation": {
                "type": "object",
                "properties": {
                    "marketCap": {"type": "number"},
                    "peRatio": {"type": "number"},
                    "evToEbitda": {"type": "number"},
                },
            },
            "financials": {
                "type": "object",
                "required": ["reportPeriod", "summary"],
                "properties": {
                    "reportPeriod": {"type": "string"},
                    "summary": {"type": "string"},
                },
            },
            "earnings": {
                "type": "object",
                "required": ["reportPeriod", "summary"],
                "properties": {
                    "reportPeriod": {"type": "string"},
                    "summary": {"type": "string"},
                },
            },
            "ownership": {
                "type": "object",
                "properties": {
                    "institutionalHighlights": {"type": "string"},
                    "insiderActivity": {"type": "string"},
                },
            },
            "filings": {
                "type": "array",
                "maxItems": 5,
                "items": {
                    "type": "object",
                    "required": ["formType", "filedAt", "keySection"],
                    "properties": {
                        "formType": {"type": "string"},
                        "filedAt": {"type": "string"},
                        "keySection": {"type": "string"},
                    },
                },
            },
        },
    },
)
run = exa.agent.runs.poll_until_finished(run.id)

```

```javascript
import Exa from "exa-js";

const exa = new Exa();
const run = await exa.agent.runs.create({
  query:
    "Analyze NVIDIA using its latest price, valuation metrics, most recent quarterly financial statements and earnings, institutional and insider activity, and material SEC filing sections. Return a structured company-research snapshot with reporting dates.",
  dataSources: [{ provider: "financial_datasets" }],
  outputSchema: {
    type: "object",
    required: ["ticker", "price", "valuation", "financials", "earnings", "ownership", "filings"],
    properties: {
      ticker: { type: "string" },
      price: {
        type: "object",
        required: ["latest", "asOf"],
        properties: {
          latest: { type: "number" },
          asOf: { type: "string" },
        },
      },
      valuation: {
        type: "object",
        properties: {
          marketCap: { type: "number" },
          peRatio: { type: "number" },
          evToEbitda: { type: "number" },
        },
      },
      financials: {
        type: "object",
        required: ["reportPeriod", "summary"],
        properties: {
          reportPeriod: { type: "string" },
          summary: { type: "string" },
        },
      },
      earnings: {
        type: "object",
        required: ["reportPeriod", "summary"],
        properties: {
          reportPeriod: { type: "string" },
          summary: { type: "string" },
        },
      },
      ownership: {
        type: "object",
        properties: {
          institutionalHighlights: { type: "string" },
          insiderActivity: { type: "string" },
        },
      },
      filings: {
        type: "array",
        maxItems: 5,
        items: {
          type: "object",
          required: ["formType", "filedAt", "keySection"],
          properties: {
            formType: { type: "string" },
            filedAt: { type: "string" },
            keySection: { type: "string" },
          },
        },
      },
    },
  },
});

```

```bash
curl -s -X POST "https://api.exa.ai/agent/runs" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "query": "Analyze NVIDIA using its latest price, valuation metrics, most recent quarterly financial statements and earnings, institutional and insider activity, and material SEC filing sections. Return a structured company-research snapshot with reporting dates.",
    "dataSources": [{ "provider": "financial_datasets" }],
    "outputSchema": {
      "type": "object",
      "required": ["ticker", "price", "valuation", "financials", "earnings", "ownership", "filings"],
      "properties": {
        "ticker": { "type": "string" },
        "price": {
          "type": "object",
          "required": ["latest", "asOf"],
          "properties": {
            "latest": { "type": "number" },
            "asOf": { "type": "string" }
          }
        },
        "valuation": {
          "type": "object",
          "properties": {
            "marketCap": { "type": "number" },
            "peRatio": { "type": "number" },
            "evToEbitda": { "type": "number" }
          }
        },
        "financials": {
          "type": "object",
          "required": ["reportPeriod", "summary"],
          "properties": {
            "reportPeriod": { "type": "string" },
            "summary": { "type": "string" }
          }
        },
        "earnings": {
          "type": "object",
          "required": ["reportPeriod", "summary"],
          "properties": {
            "reportPeriod": { "type": "string" },
            "summary": { "type": "string" }
          }
        },
        "ownership": {
          "type": "object",
          "properties": {
            "institutionalHighlights": { "type": "string" },
            "insiderActivity": { "type": "string" }
          }
        },
        "filings": {
          "type": "array",
          "maxItems": 5,
          "items": {
            "type": "object",
            "required": ["formType", "filedAt", "keySection"],
            "properties": {
              "formType": { "type": "string" },
              "filedAt": { "type": "string" },
              "keySection": { "type": "string" }
            }
          }
        }
      }
    }
  }'

```

## Pairs well with

- Particle: compare published coverage with podcast commentary.
- Baselayer: verify the underlying entity behind a ticker.
- Fiber.ai: enrich a public company with private-market peers and leadership contacts.

## Next steps

## Attach it to a run

The Exa Connect quickstart covers `dataSources`, pricing, and the full partner catalog.

## Combine providers

Attach up to five partners to one run and shape the query so each one fires.

## Learn Exa Agent

Create runs, stream progress, design output schemas, and control effort and cost.

## Get an API key

Create a key in the dashboard and run this page's example as-is. New accounts start with free credits.

# Particle
URL: https://exa.ai/docs/agent/connect/particle.md

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

# Particle

> Search podcast transcripts with speaker attribution and timestamps.

Particle' Podcast Intelligence indexes 100,000+ shows,
fully transcribed, diarized, speaker-identified, labeled, and enriched with metadata
within minutes of airing, making spoken conversations searchable. Each result is a
speaker-attributed transcript window with timestamps.

Attach `particle` to an Exa Agent run through
Exa Connect, and the agent queries
Particle alongside Exa web search.

## Use it for

- Finding expert commentary and quotable soundbites.
- Media and brand monitoring.
- Narrative and sentiment research.
- Discovering and staying up to date with podcasts.

## Provider ID

Use this value in `dataSources`:

```text
particle

```

## Example

Find what podcast hosts are saying about AI regulation.

```python
from exa_py import Exa

exa = Exa()
run = exa.agent.runs.create(
    query="What are prominent podcast hosts and guests saying about AI regulation in 2025?",
    data_sources=[{"provider": "particle"}],
    output_schema={
        "type": "object",
        "required": ["mentions"],
        "properties": {
            "mentions": {
                "type": "array",
                "maxItems": 10,
                "items": {
                    "type": "object",
                    "required": ["podcast", "episode", "speaker", "quote", "stance"],
                    "properties": {
                        "podcast": {"type": "string"},
                        "episode": {"type": "string"},
                        "speaker": {"type": "string"},
                        "quote": {"type": "string"},
                        "stance": {"type": "string", "description": "pro-regulation, anti-regulation, or nuanced"},
                    },
                },
            }
        },
    },
)
run = exa.agent.runs.poll_until_finished(run.id)

```

```javascript
import Exa from "exa-js";

const exa = new Exa();
const run = await exa.agent.runs.create({
  query: "What are prominent podcast hosts and guests saying about AI regulation in 2025?",
  dataSources: [{ provider: "particle" }],
  outputSchema: {
    type: "object",
    required: ["mentions"],
    properties: {
      mentions: {
        type: "array",
        maxItems: 10,
        items: {
          type: "object",
          required: ["podcast", "episode", "speaker", "quote", "stance"],
          properties: {
            podcast: { type: "string" },
            episode: { type: "string" },
            speaker: { type: "string" },
            quote: { type: "string" },
            stance: { type: "string", description: "pro-regulation, anti-regulation, or nuanced" },
          },
        },
      },
    },
  },
});

```

```bash
curl -s -X POST "https://api.exa.ai/agent/runs" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "query": "What are prominent podcast hosts and guests saying about AI regulation in 2025?",
    "dataSources": [{ "provider": "particle" }],
    "outputSchema": {
      "type": "object",
      "required": ["mentions"],
      "properties": {
        "mentions": {
          "type": "array",
          "maxItems": 10,
          "items": {
            "type": "object",
            "required": ["podcast", "episode", "speaker", "quote", "stance"],
            "properties": {
              "podcast": { "type": "string" },
              "episode": { "type": "string" },
              "speaker": { "type": "string" },
              "quote": { "type": "string" },
              "stance": { "type": "string", "description": "pro-regulation, anti-regulation, or nuanced" }
            }
          }
        }
      }
    }
  }'

```

## Pairs well with

- Financial Datasets: cross-check podcast chatter against published news.
- Fiber.ai: attach company and contact context to the people being discussed.

## Next steps

## Attach it to a run

The Exa Connect quickstart covers `dataSources`, pricing, and the full partner catalog.

## Combine providers

Attach up to five partners to one run and shape the query so each one fires.

## Learn Exa Agent

Create runs, stream progress, design output schemas, and control effort and cost.

## Get an API key

Create a key in the dashboard and run this page's example as-is. New accounts start with free credits.

# Combining providers
URL: https://exa.ai/docs/agent/connect/combining-providers.md

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

# Combining providers

> Use several data partners together in a single Exa Agent run.

Attaching a partner to `dataSources` makes it available to the Exa Agent as a tool — it does not force the agent to call it. Whether a partner fires depends on your `query` and `outputSchema`: name the kind of result you want from each partner, and the Exa Agent reaches for the matching tool instead of guessing from a web page. You can attach up to five partners per run; the Exa Agent picks which to call for each step, with Exa web search available alongside them. Need more than five for a single run? Contact us (sales@exa.ai) to raise the limit.

## Two partners in one run

List several partners together and the Exa Agent draws on each where it's strongest. Two is just an example here — attach up to five partners to `dataSources`, and the same principle applies: ask for each one's data explicitly. This investor-briefing run combines Financial Datasets for ticker news with Particle for podcast commentary. The query asks for each partner's distinctive data and the schema splits the output into `financialNews` and `podcastChatter`, so the Exa Agent calls both partners in the same run.

```python
from exa_py import Exa

exa = Exa()
run = exa.agent.runs.create(
    query=(
        "Give me an investor briefing on NVIDIA (NVDA): (1) the latest financial and "
        "earnings news, and (2) what podcast hosts and guests have recently been saying "
        "about NVIDIA, with speaker-attributed quotes and their stance."
    ),
    data_sources=[
        {"provider": "financial_datasets"},
        {"provider": "particle"},
    ],
    output_schema={
        "type": "object",
        "required": ["ticker", "financialNews", "podcastChatter"],
        "properties": {
            "ticker": {"type": "string"},
            "financialNews": {
                "type": "array",
                "maxItems": 6,
                "items": {
                    "type": "object",
                    "required": ["title", "source", "date", "theme"],
                    "properties": {
                        "title": {"type": "string"},
                        "source": {"type": "string"},
                        "date": {"type": "string"},
                        "theme": {"type": "string", "description": "earnings, guidance, analyst rating, product, or market"},
                    },
                },
            },
            "podcastChatter": {
                "type": "array",
                "maxItems": 6,
                "items": {
                    "type": "object",
                    "required": ["podcast", "speaker", "quote", "stance"],
                    "properties": {
                        "podcast": {"type": "string"},
                        "speaker": {"type": "string"},
                        "quote": {"type": "string"},
                        "stance": {"type": "string", "description": "bullish, bearish, or neutral"},
                    },
                },
            },
        },
    },
)
run = exa.agent.runs.poll_until_finished(run.id)

```

```javascript
import Exa from "exa-js";

const exa = new Exa();
const run = await exa.agent.runs.create({
  query:
    "Give me an investor briefing on NVIDIA (NVDA): (1) the latest financial and " +
    "earnings news, and (2) what podcast hosts and guests have recently been saying " +
    "about NVIDIA, with speaker-attributed quotes and their stance.",
  dataSources: [
    { provider: "financial_datasets" },
    { provider: "particle" },
  ],
  outputSchema: {
    type: "object",
    required: ["ticker", "financialNews", "podcastChatter"],
    properties: {
      ticker: { type: "string" },
      financialNews: {
        type: "array",
        maxItems: 6,
        items: {
          type: "object",
          required: ["title", "source", "date", "theme"],
          properties: {
            title: { type: "string" },
            source: { type: "string" },
            date: { type: "string" },
            theme: { type: "string", description: "earnings, guidance, analyst rating, product, or market" },
          },
        },
      },
      podcastChatter: {
        type: "array",
        maxItems: 6,
        items: {
          type: "object",
          required: ["podcast", "speaker", "quote", "stance"],
          properties: {
            podcast: { type: "string" },
            speaker: { type: "string" },
            quote: { type: "string" },
            stance: { type: "string", description: "bullish, bearish, or neutral" },
          },
        },
      },
    },
  },
});

```

```bash
curl -s -X POST "https://api.exa.ai/agent/runs" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "query": "Give me an investor briefing on NVIDIA (NVDA): (1) the latest financial and earnings news, and (2) what podcast hosts and guests have recently been saying about NVIDIA, with speaker-attributed quotes and their stance.",
    "dataSources": [
      { "provider": "financial_datasets" },
      { "provider": "particle" }
    ],
    "outputSchema": {
      "type": "object",
      "required": ["ticker", "financialNews", "podcastChatter"],
      "properties": {
        "ticker": { "type": "string" },
        "financialNews": {
          "type": "array",
          "maxItems": 6,
          "items": {
            "type": "object",
            "required": ["title", "source", "date", "theme"],
            "properties": {
              "title": { "type": "string" },
              "source": { "type": "string" },
              "date": { "type": "string" },
              "theme": { "type": "string", "description": "earnings, guidance, analyst rating, product, or market" }
            }
          }
        },
        "podcastChatter": {
          "type": "array",
          "maxItems": 6,
          "items": {
            "type": "object",
            "required": ["podcast", "speaker", "quote", "stance"],
            "properties": {
              "podcast": { "type": "string" },
              "speaker": { "type": "string" },
              "quote": { "type": "string" },
              "stance": { "type": "string", "description": "bullish, bearish, or neutral" }
            }
          }
        }
      }
    }
  }'

```

Make each partner's data explicit in your query — name the kind of result you want from each one (here: ticker financial news vs. speaker-attributed podcast quotes). If the request is generic ("latest news"), the Exa Agent tends to fall back to web search instead of a partner. Mirroring those distinct asks in your `outputSchema` fields reinforces it.

# Additional providers
URL: https://exa.ai/docs/agent/connect/additional-partners.md

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

# Additional providers

> Exa Connect partners beyond the self-serve provider set.

Beyond the self-serve providers, Exa Connect supports additional data partners.
These are available upon request, connect with our team to enable them for
your account (sales@exa.ai).

- Crunchbase
- Definitive Healthcare
- Faraday AI
- Harmonic
- Intellizence
- Kernel
- ZoomInfo

## Talk to our team

Tell us which partner your Exa Agent needs and we'll get you connected.

## Become a provider

Have data to offer? Apply to join Exa Connect as a partner.
