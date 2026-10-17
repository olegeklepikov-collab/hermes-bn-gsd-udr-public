> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: select

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Title: SELECT - Keenable
URL: https://docs.keenable.ai/select

This server answers a question with **one SQL query over live web search results** — and you do not write that query. You ask your agent a question in plain language; the agent composes a read-only `SELECT` (DuckDB dialect) following the guide the tool ships with itself, and the server runs the searches, fetches the pages, extracts the fields the query asks for with an LLM, deduplicates, and returns a table. The point is the shape of the answer. One tool call covers many pages at once and comes back as structured rows, instead of the agent reading results one at a time and assembling them by hand. It is a **separate MCP server** from the [Keenable MCP server](https://docs.keenable.ai/mcp-server), at its own URL. Adding it does not change the `search_web_pages` / `fetch_page_content` server — you can run both side by side.

```
https://select.keenable.ai/mcp
```

The server also answers on `https://webql.keenable.ai/mcp`, the address it had first. Neither address redirects to the other, because a redirect ends an MCP session — a client set up on the old one keeps working, and a new one should use `select.keenable.ai`.

Any Keenable account can connect. Sign up at [app.keenable.ai/signup](https://app.keenable.ai/signup) if you do not have one — the same account you use for the console and API keys. The `/select` playground in the console is still invitation-only; the MCP server is not.

##
​

Connect

Two credentials work: a browser sign-in, or an API key in a header. Which of them you can use depends on the client, so go to the one you use.

## Claude Code

Browser sign-in, or your own key in a header

## Claude

Desktop, claude.ai and mobile, from the connector directory

## ChatGPT

From the Plugins Directory, or by URL in developer mode

## Codex, Cursor

Any client that takes a URL and a header

###
​

One click

Cursor and VS Code take the server from a link. They add it without a key, so it signs you in on first use.
Add to Cursor (пример адреса или протокола; задаётся в целевой среде)Add to VS Code (пример адреса или протокола; задаётся в целевой среде)Add to VS Code Insiders (пример адреса или протокола; задаётся в целевой среде)

###
​

Claude Code

Sign in through the browser, with no key to paste:

```
claude mcp add keenable-select \
  --transport http https://select.keenable.ai/mcp \
  --scope user
```

Then run `/mcp` in a session, pick **keenable-select**, and choose **Authenticate**. Your browser opens a Keenable sign-in; approve it and the tools appear. To use an API key instead — created in the [console](https://app.keenable.ai/console) — add the header and skip the sign-in:

```
claude mcp add keenable-select \
  --transport http https://select.keenable.ai/mcp \
  --scope user \
  --header "X-API-Key: keen_<your_key>"
```

`--scope user` makes the server available in every project. Without it the entry is written for the current directory only.

###
​

Claude Desktop, claude.ai and mobile

**Keenable SELECT** is a listed connector in Claude’s directory, next to the standard Keenable connector. It signs you in instead of taking a key: the connector UI has no field for a request header, so use Claude Code or another client that sends headers if you need a specific API key applied.

1

Add the connector

**Settings → Connectors**, find **Keenable SELECT**, and add it. There is nothing to paste.Not listed yet in your account? Add it by URL instead — **Settings → Connectors → Add custom connector** — leaving OAuth Client ID / Secret **empty**; the server advertises its own authorization server and Claude registers itself:

```
https://select.keenable.ai/mcp
```

2

Connect

A newly added connector is not active until you connect it. Open **Manage connectors**, find it, and click **Connect**. Your browser opens a Keenable sign-in; approve it and the tools appear.

3

Enable it in a chat

In the composer, click **+ → Connectors** and toggle it on for the conversation.

If you add it by URL, give it a name that distinguishes it from the standard Keenable connector — e.g. **Keenable SELECT** — since they are separate servers with different tools.

###
​

ChatGPT

**Keenable SELECT** is a published plugin in OpenAI’s Plugins Directory, the catalog ChatGPT shares with Codex. It is a second listing next to the [Keenable search plugin](https://docs.keenable.ai/integrations/chatgpt), because the two are different servers with different tools.

1

Install the plugin

Find **Keenable SELECT** in the directory and install it. There is no config file, no developer mode, and no URL to paste.

2

Sign in

The plugin authenticates with your Keenable account through OAuth — click through the sign-in prompt on first use. Usage is attributed to the account you connect and metered against that account’s organization.

3

Use it in a chat

Pick the plugin from the composer’s tools menu before asking. A query runs for as long as it needs; see What to expect.

The route that worked before the listing still does, and it is the one to use if the directory has not reached your account yet.

1. **Settings → Connectors → Advanced settings → Developer mode**. Without it, ChatGPT offers no way to add a server by URL.
2. **Settings → Connectors → Create**, paste `https://select.keenable.ai/mcp`, and choose **OAuth** as the authentication. Sign in when the browser opens; there is no client ID or secret to fill in.

Deep research in ChatGPT accepts only connectors that expose `search` and `fetch` tools. This server exposes `select` instead, so use it as an ordinary plugin, and the [Keenable search plugin](https://docs.keenable.ai/integrations/chatgpt) for deep research.

###
​

Codex, Cursor and other clients

Codex also installs **Keenable SELECT** from the Plugins Directory it shares with ChatGPT, with an OAuth sign-in and nothing to paste. The `config.toml` route below is the one that takes your own API key. Any client that takes a remote MCP URL and a header works. Create a key in the [console](https://app.keenable.ai/console) first. Codex — add to `~/.codex/config.toml`:

```
[mcp_servers.keenable-select]
url = "https://select.keenable.ai/mcp"
http_headers = { "X-API-Key" = "keen_<your_key>" }
```

Cursor, Windsurf, and similar:

```
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

##
​

The tools

The main tool is `select`. Its parameters are filled in by the agent, not by you; they are listed here so you can read a transcript and see what was actually run.
​

string

required

A single read-only `SELECT` in DuckDB dialect. Web pages enter the query through the `WEB_SEARCH(...)` and `WEB_FETCH(...)` table functions; the `SEM_*` functions extract, filter, rank and normalise values with an LLM.

​

boolean

Return a small sample of rows instead of the full table. Defaults to `false`.

Nobody has to teach the agent this dialect, and you do not have to learn it yourself. The `select` tool carries its own full usage guide as its description — syntax, semantic functions and worked examples — so the model has everything it needs the moment the connector is enabled. Two more tools publish what a query found as a web page: `generate_html_report` builds a document from a brief plus the result sets you name and returns its link, and `revoke_html_report` takes that link back down. So a session reads like an ordinary conversation. You ask *“which electric cars sold in Europe come up most often, and what are their range and starting price?”*; the agent turns that into a query like this:

```
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
| model | sources | range_km | price_eur |
|---|---|---|---|
| Tesla Model Y | 119 | 455 | 39990 |
| Tesla Model 3 | 118 | 580 | 44990 |
| Renault 5 E-Tech | 113 | 400 | 25000 |
| Dacia Spring | 91 | 225 | 16900 |
| Citroen e-C3 | 81 | 320 | 23300 |
| BMW iX3 | 78 | 805 | 70900 |
| Leapmotor T03 | 77 | 265 | 18900 |
| Volkswagen ID.3 | 65 | 420 | 35000 |

That is a real run, and the figures are whatever the pages said — the server reports its sources, it does not audit them. See What to expect.

The seven searches are the point of the shape: the guide tells the agent to cast wide with genuinely different phrasings rather than variations of one, and the pages they return are merged and deduplicated by URL before the rest of the query runs. On the wire the rows arrive in a compact tabular encoding rather than JSON, which is why a table this size costs so little context.

##
​

Result sets

Every call stores its output and returns a **result set id** — `ra84968f0532` for the query above. A later query reads it by putting that id in `FROM`, so a follow-up costs no new searching. That is what makes the second question cheap. Ask *“now just the ones under €30,000, longest range first”* and the agent queries the stored table instead of going back to the web:

```
SELECT model, range_km, price_eur
FROM ra84968f0532
WHERE TRY_CAST(price_eur AS INTEGER) < 30000
ORDER BY TRY_CAST(range_km AS INTEGER) DESC
```

| model | range_km | price_eur |
|---|---|---|
| Renault 5 E-Tech | 400 | 25000 |
| Citroen e-C3 | 320 | 23300 |
| Leapmotor T03 | 265 | 18900 |
| Dacia Spring | 225 | 16900 |
| BYD Dolphin Surf | 220 | 18990 |

That one returned in seconds, because no page was searched or fetched. The searched pages are also kept as their own result set, so a different question can be asked of the same 1,125 pages without paying for the crawl twice. Result sets are kept for **30 days**.

##
​

What to expect

- **Queries are slow by ordinary tool standards** — seconds to minutes, because each one runs real searches, fetches pages and calls an LLM per row. That is normal, not a hang.
- **Large tables come back as a preview.** Above roughly 50,000 characters the response degrades to a few sample rows with long strings clipped; the full table stays available through the result set id.
- **A report takes minutes to build**, and a client that gives up on a slow tool call cancels it. Ask for a report from aggregated result sets rather than a raw table of hundreds of rows, so it finishes before the client stops waiting.
- **Extraction does not fact-check its sources.** A single page can be outdated or the wrong edition, so cross-check precise numbers across independent pages.

##
​

When something is refused

- **401** — no credential reached the server, or it is invalid. Check the header name and the key.
- **429** — too many queries at once, cluster-wide. Retry shortly.
- **403** — this deployment runs an allowlist and the account is not on it. Production does not, so you should not see this; if you do, email [support@keenable.ai](mailto:support@keenable.ai) with the address you signed in with. Signing in again will not clear it.
