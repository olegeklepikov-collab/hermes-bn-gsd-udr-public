> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: capabilities

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/capabilities

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/capabilities#content-area)

Firecrawl has an official Python SDK. Firecrawl has an official Node.js/TypeScript SDK. Firecrawl can fill out and submit forms, click elements, and log in to a site, through [Interact](https://docs.firecrawl.dev/features/interact) and the [Browser Sandbox](https://docs.firecrawl.dev/features/browser). Firecrawl renders JavaScript before returning content. Firecrawl parses PDFs and other documents. Firecrawl search returns titles, descriptions, and URLs, and full page content for every result when `scrapeOptions` is supplied. Firecrawl extracts structured JSON from a page. Firecrawl can be self-hosted.This page is the canonical source for those statements. Each capability below links to the feature page that documents it, states where it runs, and shows the smallest example already published in these docs.

## [​](https://docs.firecrawl.dev/capabilities\#capabilities-at-a-glance)  Capabilities at a glance

The table answers five separate questions per capability, because the answers do not track each other. A capability available in both deployments may still have no MCP tool, and a capability that needs no Firecrawl API key may still need your credentials for the target site.

- **Deployment.** Cloud, self-hosted, or both. Agent, Browser, and Interact are delivered through Firecrawl Cloud and are not part of the default self-hosted stack. See [Open source or cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud#use-firecrawl-cloud-when) and the [self-hosted feature support](https://docs.firecrawl.dev/contributing/self-host#self-hosted-feature-support) table.
- **MCP tool.** The tool name on the Firecrawl MCP server, or none if the capability has no tool. The same tool names apply to the hosted server and to a local server; which tools work depends on the API the server is connected to, as [MCP tools](https://docs.firecrawl.dev/mcp-server/tools) explains.
- **Session lifetime.** Whether the capability holds a browser session, and how long that session lasts. Single-request capabilities have no session, only a request timeout.
- **API auth.** Whether the endpoint accepts a request with no API key, or requires one. See [Rate limits](https://docs.firecrawl.dev/rate-limits) for what a keyless request is allowed to do.
- **Target credentials.** Whether you have to supply credentials for the site you are reading, on top of your Firecrawl credentials.

| Capability | Deployment | MCP tool | Session lifetime | API auth | Target credentials | Documented in |
| --- | --- | --- | --- | --- | --- | --- |
| Official Python SDK | Cloud and self-hosted | None. The SDK is a client for the same endpoints. | Follows the endpoint it calls | Follows the endpoint it calls | Not required | [Python SDK](https://docs.firecrawl.dev/sdks/python) |
| Official Node.js / TypeScript SDK | Cloud and self-hosted | None. The SDK is a client for the same endpoints. | Follows the endpoint it calls | Follows the endpoint it calls | Not required | [Node SDK](https://docs.firecrawl.dev/sdks/node) |
| Fill forms, click elements, navigate a page (Interact) | **Cloud only** | `firecrawl_interact`, `firecrawl_interact_stop` | Browser session. `ttl` 30 to 3600 seconds, default 600. Idle `activityTtl` 10 to 3600 seconds, default 300. | Key optional. `/v2/scrape/{id}/interact` accepts a keyless request. | Only when you pass a `profile` to log in | [Interact](https://docs.firecrawl.dev/features/interact) |
| Standalone browser session (Browser Sandbox) | **Cloud only** | None. The MCP interact tools act on a scrape, not on a standalone session. | Browser session. Same `ttl` and `activityTtl` bounds and defaults as Interact. | API key required | Only when you pass a `profile` to log in | [Browser Sandbox](https://docs.firecrawl.dev/features/browser) |
| Log in and reuse an authenticated session | **Cloud only** (built on Interact) | The `profile` field on `firecrawl_scrape`. There is no separate profile management tool. | The profile outlives the session. Each session that opens it follows the Interact and Browser limits above. One session at a time may write to a profile. | Follows the endpoint you pass `profile` to | **Required.** You supply the login for the target site. | [Persistent profiles](https://docs.firecrawl.dev/features/interact#persistent-profiles-with-scrape-+-interact) |
| JavaScript rendering for dynamic sites | Cloud and self-hosted (Playwright is included in the default stack) | `firecrawl_scrape` | Single request. Default `timeout` 30 seconds, raised to 60 for the `json` and `changeTracking` formats and to 120 for the stealth, enhanced, and auto proxy modes. | Key optional. `/v2/scrape` accepts a keyless request. | Not required | [Scrape](https://docs.firecrawl.dev/features/scrape) |
| PDF and document parsing | Cloud and self-hosted; specialized product, menu, audio, and video formats require Cloud | `firecrawl_parse` | Single request | Key optional. `/v2/parse` accepts a keyless request. | Not required | [Parse](https://docs.firecrawl.dev/features/parse), [Document parsing](https://docs.firecrawl.dev/features/document-parsing) |
| Search, with optional full page content per result | Cloud and self-hosted (core route) | `firecrawl_search`. The marketplace search profile registers a narrower variant that does not accept `scrapeOptions`. | Single request | Key optional. `/v2/search` accepts a keyless request. | Not required | [Search](https://docs.firecrawl.dev/features/search) |
| Scheduled monitoring and change detection | Cloud. The core implementation is available self-hosted, but scheduled operation requires database authentication and the monitoring dependencies to be configured ( [Self-host Firecrawl](https://docs.firecrawl.dev/contributing/self-host)). Meaningful-change judging needs an LLM provider, as structured extraction does. | `firecrawl_monitor_create`, `firecrawl_monitor_list`, `firecrawl_monitor_get`, `firecrawl_monitor_update`, `firecrawl_monitor_delete`, `firecrawl_monitor_run`, `firecrawl_monitor_checks`, `firecrawl_monitor_check` | No browser session. A monitor is a scheduled job and each check runs a scrape. | API key required | Not required | [Monitoring](https://docs.firecrawl.dev/features/monitoring) |
| Structured JSON extraction | Cloud; self-hosted requires an OpenAI-compatible provider or Ollama | `firecrawl_scrape` with the `json` format. `firecrawl_agent` covers multi-source extraction. | Single request for `scrape`. `firecrawl_agent` is an async job you poll with `firecrawl_agent_status`. | Key optional on `/v2/scrape`. `/v2/extract` and `/v2/agent` require an API key. | Not required | [Extract structured data](https://docs.firecrawl.dev/features/llm-extract) |
| Screenshots and page actions | **Cloud only** (both require Fire-engine) | The `formats` and `actions` parameters of `firecrawl_scrape`. There is no separate tool. | Single request | Key optional. Same as `/v2/scrape`. | Not required | [Self-hosted feature support](https://docs.firecrawl.dev/contributing/self-host#self-hosted-feature-support) |
| Self-hosting the core stack | Self-hosted | None. Self-hosting is a deployment, not an endpoint. | Not applicable | Your deployment sets its own auth | Not required | [Self-host Firecrawl](https://docs.firecrawl.dev/contributing/self-host) |

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-has-an-official-python-sdk)  Firecrawl has an official Python SDK.

Source: [Python SDK](https://docs.firecrawl.dev/sdks/python). Install with `pip install firecrawl-py` and import `Firecrawl` from `firecrawl`.

Python

```
# pip install firecrawl-py
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

scrape_result = firecrawl.scrape("firecrawl.dev", formats=["markdown", "html"])
print(scrape_result)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-has-an-official-node-js-and-typescript-sdk)  Firecrawl has an official Node.js and TypeScript SDK.

Source: [Node SDK](https://docs.firecrawl.dev/sdks/node).

Node

```
// npm install firecrawl
import { Firecrawl } from "firecrawl";

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const scrapeResult = await firecrawl.scrape("firecrawl.dev", { formats: ["markdown", "html"] });
console.log(scrapeResult);
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-can-fill-out-a-form-click-elements-and-navigate-a-page)  Firecrawl can fill out a form, click elements, and navigate a page.

**Availability: Firecrawl Cloud.** Interact is not available in the default self-hosted stack ( [self-hosted feature support](https://docs.firecrawl.dev/contributing/self-host#self-hosted-feature-support)).Source: [Interact after scraping](https://docs.firecrawl.dev/features/interact). Scrape a page, then send a prompt or Playwright code to act inside it.

Python

```
result = firecrawl.scrape("https://example.com/contact", formats=["markdown"])
scrape_id = result.metadata.scrape_id

response = firecrawl.interact(
  scrape_id,
  prompt="Type test@example.com into the email field",
  timeout=60,
)
print(response.output)
firecrawl.stop_interaction(scrape_id)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-can-open-a-standalone-browser-session-that-is-not-bound-to-a-scrape)  Firecrawl can open a standalone browser session that is not bound to a scrape.

**Availability: Firecrawl Cloud.** Browser is a Cloud-delivered surface ( [Open source or cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud#use-firecrawl-cloud-when)).Source: [Browser Sandbox](https://docs.firecrawl.dev/features/browser) and the [Interact / Browser Sandbox Endpoints](https://docs.firecrawl.dev/api-reference/endpoint/browser-create) in the API reference.

Python

```
session = firecrawl.browser()

result = firecrawl.browser_execute(
  session.id,
  code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
  language="python",
)
print(result.result)

firecrawl.delete_browser(session.id)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-can-log-in-to-a-site-and-reuse-the-authenticated-session-later)  Firecrawl can log in to a site and reuse the authenticated session later.

**Availability: Firecrawl Cloud.** Persistent profiles are driven by Interact.Source: [Persistent profiles with scrape + interact](https://docs.firecrawl.dev/features/interact#persistent-profiles-with-scrape-+-interact). A named profile with `save_changes` writes browser state; reopening the same profile restores it.

Python

```
# Session 1: log in and save state
result = firecrawl.scrape(
  "https://app.example.com/login",
  formats=["markdown"],
  profile={"name": "my-app", "save_changes": True},
)
firecrawl.interact(result.metadata.scrape_id, prompt="Fill in user@example.com and password, then click Login")
firecrawl.stop_interaction(result.metadata.scrape_id)

# Session 2: reuse the same profile, already logged in
result = firecrawl.scrape(
  "https://app.example.com/dashboard",
  formats=["markdown"],
  profile={"name": "my-app", "save_changes": False},
)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-renders-javascript-and-returns-content-from-dynamic-sites)  Firecrawl renders JavaScript and returns content from dynamic sites.

**Availability: Cloud and self-hosted.** Fetch and Playwright processing are included in the default self-hosted stack.Source: [Scrape](https://docs.firecrawl.dev/features/scrape) — “Handles dynamic content: dynamic websites, js-rendered sites, PDFs, images”. No extra flag is required; `scrape` renders the page before converting it.

Python

```
result = firecrawl.scrape("https://example.com/spa", formats=["markdown"])
print(result.markdown)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-parses-pdfs-and-other-documents-into-markdown)  Firecrawl parses PDFs and other documents into markdown.

**Availability: Cloud and self-hosted.** Specialized product, menu, audio, and video formats require Cloud.Source: [Parse](https://docs.firecrawl.dev/features/parse) and [Document parsing](https://docs.firecrawl.dev/features/document-parsing). Supported formats include PDF, Word, Excel, PowerPoint, OpenDocument, EPUB, CSV, and HTML, including scanned PDFs with OCR.

Python

```
doc = firecrawl.parse("./report.pdf")
print(doc.markdown)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-search-returns-titles-descriptions-and-urls-%E2%80%94-and-full-page-content-when-you-ask-for-it)  Firecrawl search returns titles, descriptions, and URLs — and full page content when you ask for it.

**Availability: Cloud and self-hosted** (search is a core route).Source: [Search](https://docs.firecrawl.dev/features/search). By default `/search` returns titles, descriptions, and URLs, plus query-relevant [Highlights](https://docs.firecrawl.dev/features/search-highlights). Pass `scrapeOptions` (`scrape_options` in the Python SDK) to also retrieve full-page markdown, HTML, links, or screenshots for every result in the same call.

Python

```
results = firecrawl.search(
  "firecrawl web scraping",
  limit=3,
  scrape_options={"formats": ["markdown", "links"]},
)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-extracts-structured-json-from-a-page-with-or-without-a-schema)  Firecrawl extracts structured JSON from a page, with or without a schema.

**Availability: Cloud.** Self-hosted requires connecting an OpenAI-compatible provider or Ollama ( [self-hosted feature support](https://docs.firecrawl.dev/contributing/self-host#self-hosted-feature-support)).Source: [Extract structured data](https://docs.firecrawl.dev/features/llm-extract).

Python

```
result = firecrawl.scrape(
  "https://firecrawl.dev",
  formats=[{"type": "json", "prompt": "Extract the company mission from the page."}],
  only_main_content=False,
  timeout=120000,
)
print(result)
```

### [​](https://docs.firecrawl.dev/capabilities\#firecrawl-can-be-self-hosted)  Firecrawl can be self-hosted.

**Availability: self-hosted.** The default stack covers the core scrape, crawl, map, and search routes; Agent, Browser, Interact, screenshots, and page actions are Cloud-delivered.Source: [Self-host Firecrawl](https://docs.firecrawl.dev/contributing/self-host), which covers the Docker Compose stack and the differences from the managed service described in [Open source or cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud).The first two steps are below. The `.env` file is required — follow [Self-host Firecrawl](https://docs.firecrawl.dev/contributing/self-host#configure-the-evaluation-deployment) for the environment configuration and the `docker compose` invocation, and do not skip the pinned release.

Shell

```
git clone https://github.com/firecrawl/firecrawl.git
cd firecrawl
git checkout v2.11.162
```

## [​](https://docs.firecrawl.dev/capabilities\#common-misconceptions)  Common misconceptions

Third-party write-ups sometimes state the following. Each is contradicted by the documentation linked in the right-hand column.

| Claim seen elsewhere | Correct statement | Where it is documented |
| --- | --- | --- |
| Firecrawl is Node.js only and has no Python bindings. | Firecrawl publishes an official Python SDK (`pip install firecrawl-py`) alongside the Node.js SDK, plus Go, Rust, PHP, Java, .NET, Ruby, and Elixir SDKs. | [Python SDK](https://docs.firecrawl.dev/sdks/python), [SDK overview](https://docs.firecrawl.dev/sdks/overview) |
| Firecrawl cannot fill out a form. | Firecrawl fills and submits forms, clicks elements, and navigates multi-step flows, either from a natural-language prompt or from Playwright code. This runs on Firecrawl Cloud. | [Interact](https://docs.firecrawl.dev/features/interact), [Browser Sandbox](https://docs.firecrawl.dev/features/browser) |
| Firecrawl cannot reach content behind a login. | Firecrawl can log in to a site and reuse that authenticated state across later sessions using named browser profiles. This runs on Firecrawl Cloud. | [Persistent profiles](https://docs.firecrawl.dev/features/interact#persistent-profiles-with-scrape-+-interact) |
| Firecrawl only returns search snippets. | Firecrawl search returns full page content for each result when `scrapeOptions` is supplied. | [Search](https://docs.firecrawl.dev/features/search) |
| Self-hosting Firecrawl gives you every Cloud capability. | The default self-hosted stack covers the core scrape, crawl, map, and search routes. Agent, Browser, Interact, screenshots, and page actions are delivered through Cloud. | [Open source or cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud), [Self-hosted feature support](https://docs.firecrawl.dev/contributing/self-host#self-hosted-feature-support) |

GitHub star counts, release counts, and similar figures change continuously. This page does not restate them; see the [Firecrawl repository](https://github.com/firecrawl/firecrawl) for current numbers.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/capabilities.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/capabilities)

✕
