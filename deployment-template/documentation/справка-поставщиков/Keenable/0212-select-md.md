> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: select-md

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.keenable.ai/llms.txt
> Use this file to discover all available pages before exploring further.

## # SELECT

> Query the web with SQL — a separate MCP server whose main tool is one read-only SELECT

This server answers a question with **one SQL query over live web search results** — and you do not write that query. You ask your agent a question in plain language; the agent composes a read-only `SELECT` (DuckDB dialect) following the guide the tool ships with itself, and the server runs the searches, fetches the pages, extracts the fields the query asks for with an LLM, deduplicates, and returns a table.

The point is the shape of the answer. One tool call covers many pages at once and comes back as structured rows, instead of the agent reading results one at a time and assembling them by hand.

It is a **separate MCP server** from the [Keenable MCP server](https://select.keenable.ai/mcp-server), at its own URL. Adding it does not change the `search_web_pages` / `fetch_page_content` server — you can run both side by side.

```
https://select.keenable.ai/mcp
```

The server also answers on `https://webql.keenable.ai/mcp`, the address it had first.
Neither address redirects to the other, because a redirect ends an MCP session — a client
set up on the old one keeps working, and a new one should use `select.keenable.ai`.

<Note>
  Any Keenable account can connect. Sign up at [app.keenable.ai/signup](https://app.keenable.ai/signup) if you do not have one — the same account you use for the console and API keys. The `/select` playground in the console is still invitation-only; the MCP server is not.
</Note>

## Connect

Two credentials work: a browser sign-in, or an API key in a header. Which of them you can
use depends on the client, so go to the one you use.

<Columns cols={4}>
  <Column>
    <Card title="Claude Code" icon="terminal" href="#claude-code">
      Browser sign-in, or your own key in a header
    </Card>
  </Column>

  <Column>
    <Card title="Claude" icon="comments" href="#claude-desktop-claude-ai-and-mobile">
      Desktop, claude.ai and mobile, from the connector directory
    </Card>
  </Column>

  <Column>
    <Card title="ChatGPT" icon="robot" href="#chatgpt">
      From the Plugins Directory, or by URL in developer mode
    </Card>
  </Column>

  <Column>
    <Card title="Codex, Cursor" icon="code" href="#codex-cursor-and-other-clients">
      Any client that takes a URL and a header
    </Card>
  </Column>
</Columns>

### One click

Cursor and VS Code take the server from a link. They add it without a key, so it signs you
in on first use.

<div className="install-buttons">
  <a className="install-button" href="cursor://anysphere.cursor-deeplink/mcp/install?name=keenable-select&config=eyJ1cmwiOiJodHRwczovL3NlbGVjdC5rZWVuYWJsZS5haS9tY3AifQ==">
    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23" />
    </svg>

    Add to Cursor
  </a>

  <a className="install-button" href="vscode:mcp/install?%7B%22name%22%3A%22keenable-select%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fselect.keenable.ai%2Fmcp%22%7D">
    <svg viewBox="0 0 100 100" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path fillRule="evenodd" clipRule="evenodd" d="M70.9119 99.3171C72.4869 99.9307 74.2828 99.8914 75.8725 99.1264L96.4608 89.2197C98.6242 88.1787 100 85.9892 100 83.5872V16.4133C100 14.0113 98.6243 11.8218 96.4609 10.7808L75.8725 0.873756C73.7862 -0.130129 71.3446 0.11576 69.5135 1.44695C69.252 1.63711 69.0028 1.84943 68.769 2.08341L29.3551 38.0415L12.1872 25.0096C10.589 23.7965 8.35363 23.8959 6.86933 25.2461L1.36303 30.2549C-0.452552 31.9064 -0.454633 34.7627 1.35853 36.417L16.2471 50.0001L1.35853 63.5832C-0.454633 65.2374 -0.452552 68.0938 1.36303 69.7453L6.86933 74.7541C8.35363 76.1043 10.589 76.2037 12.1872 74.9905L29.3551 61.9587L68.769 97.9167C69.3925 98.5406 70.1246 99.0104 70.9119 99.3171ZM75.0152 27.2989L45.1091 50.0001L75.0152 72.7012V27.2989Z" />
    </svg>

    Add to VS Code
  </a>

  <a className="install-button" href="vscode-insiders:mcp/install?%7B%22name%22%3A%22keenable-select%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fselect.keenable.ai%2Fmcp%22%7D">
    <svg viewBox="0 0 100 100" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path fillRule="evenodd" clipRule="evenodd" d="M70.9119 99.3171C72.4869 99.9307 74.2828 99.8914 75.8725 99.1264L96.4608 89.2197C98.6242 88.1787 100 85.9892 100 83.5872V16.4133C100 14.0113 98.6243 11.8218 96.4609 10.7808L75.8725 0.873756C73.7862 -0.130129 71.3446 0.11576 69.5135 1.44695C69.252 1.63711 69.0028 1.84943 68.769 2.08341L29.3551 38.0415L12.1872 25.0096C10.589 23.7965 8.35363 23.8959 6.86933 25.2461L1.36303 30.2549C-0.452552 31.9064 -0.454633 34.7627 1.35853 36.417L16.2471 50.0001L1.35853 63.5832C-0.454633 65.2374 -0.452552 68.0938 1.36303 69.7453L6.86933 74.7541C8.35363 76.1043 10.589 76.2037 12.1872 74.9905L29.3551 61.9587L68.769 97.9167C69.3925 98.5406 70.1246 99.0104 70.9119 99.3171ZM75.0152 27.2989L45.1091 50.0001L75.0152 72.7012V27.2989Z" />
    </svg>

    Add to VS Code Insiders
  </a>
</div>

### Claude Code

Sign in through the browser, with no key to paste:

```bash theme={"system"}
claude mcp add keenable-select \
  --transport http https://select.keenable.ai/mcp \
  --scope user
```

Then run `/mcp` in a session, pick **keenable-select**, and choose **Authenticate**. Your browser opens a Keenable sign-in; approve it and the tools appear.

To use an API key instead — created in the [console](https://app.keenable.ai/console) — add the header and skip the sign-in:

```bash theme={"system"}
claude mcp add keenable-select \
  --transport http https://select.keenable.ai/mcp \
  --scope user \
  --header "X-API-Key: keen_<your_key>"
```

`--scope user` makes the server available in every project. Without it the entry is written for the current directory only.

### Claude Desktop, claude.ai and mobile

**Keenable SELECT** is a listed connector in Claude's directory, next to the standard
Keenable connector. It signs you in instead of taking a key: the connector UI has no field
for a request header, so use Claude Code or another client that sends headers if you need a
specific API key applied.

<Steps>
  <Step title="Add the connector">
    **Settings → Connectors**, find **Keenable SELECT**, and add it. There is nothing to paste.

    Not listed yet in your account? Add it by URL instead — **Settings → Connectors → Add custom connector** — leaving OAuth Client ID / Secret **empty**; the server advertises its own authorization server and Claude registers itself:

    ```
    https://select.keenable.ai/mcp
    ```
  </Step>

  <Step title="Connect">
    A newly added connector is not active until you connect it. Open **Manage connectors**, find it, and click **Connect**. Your browser opens a Keenable sign-in; approve it and the tools appear.
  </Step>

  <Step title="Enable it in a chat">
    In the composer, click **+ → Connectors** and toggle it on for the conversation.
  </Step>
</Steps>

<Tip>
  If you add it by URL, give it a name that distinguishes it from the standard Keenable connector — e.g. **Keenable SELECT** — since they are separate servers with different tools.
</Tip>

### ChatGPT

**Keenable SELECT** is a published plugin in OpenAI's Plugins Directory, the catalog ChatGPT
shares with Codex. It is a second listing next to the [Keenable search plugin](https://select.keenable.ai/integrations/chatgpt),
because the two are different servers with different tools.

<Steps>
  <Step title="Install the plugin">
    Find **Keenable SELECT** in the directory and install it. There is no config file, no developer mode, and no URL to paste.
  </Step>

  <Step title="Sign in">
    The plugin authenticates with your Keenable account through OAuth — click through the sign-in prompt on first use. Usage is attributed to the account you connect and metered against that account's organization.
  </Step>

  <Step title="Use it in a chat">
    Pick the plugin from the composer's tools menu before asking. A query runs for as long as it needs; see [What to expect](#what-to-expect).
  </Step>
</Steps>

<Accordion title="By URL, in developer mode">
  The route that worked before the listing still does, and it is the one to use if the directory has not reached your account yet.

  1. **Settings → Connectors → Advanced settings → Developer mode**. Without it, ChatGPT offers no way to add a server by URL.
  2. **Settings → Connectors → Create**, paste `https://select.keenable.ai/mcp`, and choose **OAuth** as the authentication. Sign in when the browser opens; there is no client ID or secret to fill in.
</Accordion>

<Note>
  Deep research in ChatGPT accepts only connectors that expose `search` and `fetch` tools. This server exposes `select` instead, so use it as an ordinary plugin, and the [Keenable search plugin](https://select.keenable.ai/integrations/chatgpt) for deep research.
</Note>

### Codex, Cursor and other clients

Codex also installs **Keenable SELECT** from the Plugins Directory it shares with ChatGPT, with an OAuth sign-in and nothing to paste. The `config.toml` route below is the one that takes your own API key.

Any client that takes a remote MCP URL and a header works. Create a key in the [console](https://app.keenable.ai/console) first.

Codex — add to `~/.codex/config.toml`:

```bash theme={"system"}
[mcp_servers.keenable-select]
url = "https://select.keenable.ai/mcp"
http_headers = { "X-API-Key" = "keen_<your_key>" }
```

Cursor, Windsurf, and similar:

```json theme={"system"}
{
  "mcpServers": {
    "keenable-select": {
      "url": "https://select.keenable.ai/mcp",
      "headers": {
        "X-API-Key": "keen_<your_key>"
      }
    }
  }
}
```

An `Authorization: Bearer keen_<your_key>` header works too, if your client only offers that field.

## The tools

The main tool is `select`. Its parameters are filled in by the agent, not by you; they are listed here so you can read a transcript and see what was actually run.

<ParamField body="query" type="string" required>
  A single read-only `SELECT` in DuckDB dialect. Web pages enter the query through the `WEB_SEARCH(...)` and `WEB_FETCH(...)` table functions; the `SEM_*` functions extract, filter, rank and normalise values with an LLM.
</ParamField>

<ParamField body="show_preview" type="boolean">
  Return a small sample of rows instead of the full table. Defaults to `false`.
</ParamField>

Nobody has to teach the agent this dialect, and you do not have to learn it yourself. The `select` tool carries its own full usage guide as its description — syntax, semantic functions and worked examples — so the model has everything it needs the moment the connector is enabled.

Two more tools publish what a query found as a web page: `generate_html_report` builds a document from a brief plus the result sets you name and returns its link, and `revoke_html_report` takes that link back down.

So a session reads like an ordinary conversation. You ask *"which electric cars sold in Europe come up most often, and what are their range and starting price?"*; the agent turns that into a query like this:

```sql theme={"system"}
SELECT SEM_NORM(model, 'merge trim levels and battery variants into one model') AS model,
       COUNT(DISTINCT url) AS sources,
       MODE(range_km) AS range_km,
       MODE(price_eur) AS price_eur
## FROM (
  SELECT url, UNNEST(
##     SEM_EXTRACT_ALL(
      content,
      'an electric car model sold in Europe',
      model := 'brand and model name, e.g. "Renault 5 E-Tech"',
      range_km := 'WLTP range in km, number only',
      price_eur := 'starting price in EUR, number only'
    ),
    recursive := true
  )
##   FROM WEB_SEARCH(
    'best electric cars Europe 2026 WLTP range price',
    'affordable EV Europe comparison starting price',
    'new electric car launches Europe 2026',
    'EV buyers guide range price Germany',
    'site:reddit.com which EV should I buy Europe',
    'electric car WLTP range comparison table',
    'cheapest electric cars Europe list'
  )
)
GROUP BY SEM_NORM(model, 'merge trim levels and battery variants into one model')
ORDER BY sources DESC
## LIMIT 15
```

That is one tool call. It ran seven searches, merged 1,400 results into 1,125 unique pages, extracted three fields from each and grouped them, and came back with this (first 8 of 15 rows):

| model | sources | range\_km | price\_eur |
| - | - | - | - |
| Tesla Model Y | 119 | 455 | 39990 |
| Tesla Model 3 | 118 | 580 | 44990 |
| Renault 5 E-Tech | 113 | 400 | 25000 |
| Dacia Spring | 91 | 225 | 16900 |
| Citroen e-C3 | 81 | 320 | 23300 |
| BMW iX3 | 78 | 805 | 70900 |
| Leapmotor T03 | 77 | 265 | 18900 |
| Volkswagen ID.3 | 65 | 420 | 35000 |

<Note>
  That is a real run, and the figures are whatever the pages said — the server reports its sources, it does not audit them. See [What to expect](#what-to-expect).
</Note>

The seven searches are the point of the shape: the guide tells the agent to cast wide with genuinely different phrasings rather than variations of one, and the pages they return are merged and deduplicated by URL before the rest of the query runs. On the wire the rows arrive in a compact tabular encoding rather than JSON, which is why a table this size costs so little context.

## Result sets

Every call stores its output and returns a **result set id** — `ra84968f0532` for the query above. A later query reads it by putting that id in `FROM`, so a follow-up costs no new searching.

That is what makes the second question cheap. Ask *"now just the ones under €30,000, longest range first"* and the agent queries the stored table instead of going back to the web:

```sql theme={"system"}
SELECT model, range_km, price_eur
FROM ra84968f0532
WHERE TRY_CAST(price_eur AS INTEGER) < 30000
ORDER BY TRY_CAST(range_km AS INTEGER) DESC
```

| model | range\_km | price\_eur |
| - | - | - |
| Renault 5 E-Tech | 400 | 25000 |
| Citroen e-C3 | 320 | 23300 |
| Leapmotor T03 | 265 | 18900 |
| Dacia Spring | 225 | 16900 |
| BYD Dolphin Surf | 220 | 18990 |

That one returned in seconds, because no page was searched or fetched. The searched pages are also kept as their own result set, so a different question can be asked of the same 1,125 pages without paying for the crawl twice.

Result sets are kept for **30 days**.

## What to expect

* **Queries are slow by ordinary tool standards** — seconds to minutes, because each one runs real searches, fetches pages and calls an LLM per row. That is normal, not a hang.
* **Large tables come back as a preview.** Above roughly 50,000 characters the response degrades to a few sample rows with long strings clipped; the full table stays available through the result set id.
* **A report takes minutes to build**, and a client that gives up on a slow tool call cancels it. Ask for a report from aggregated result sets rather than a raw table of hundreds of rows, so it finishes before the client stops waiting.
* **Extraction does not fact-check its sources.** A single page can be outdated or the wrong edition, so cross-check precise numbers across independent pages.

## When something is refused

* **401** — no credential reached the server, or it is invalid. Check the header name and the key.
* **429** — too many queries at once, cluster-wide. Retry shortly.
* **403** — this deployment runs an allowlist and the account is not on it. Production does not, so you should not see this; if you do, email [support@keenable.ai](mailto:support@keenable.ai) with the address you signed in with. Signing in again will not clear it.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
