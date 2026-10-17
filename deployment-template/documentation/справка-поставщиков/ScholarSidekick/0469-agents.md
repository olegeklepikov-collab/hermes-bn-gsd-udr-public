> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ScholarSidekick: agents

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Scholar Sidekick — Agent Guide

> For AI coding agents (Claude Code, Copilot, Cursor, Windsurf).
> Full API reference: https://scholar-sidekick.com/docs.md
> Full MCP reference: https://scholar-sidekick.com/mcp.md

Scholar Sidekick is the trust layer between scholarly identifiers and your bibliography — resolve, verify, format. It turns DOIs, PMIDs, ISBNs, arXiv IDs, and more into formatted citations and bibliography files, and verifies citations against the registries of record. It is available as a REST API and as an MCP server.

**If you are an agent that was handed this file to set yourself up:** pick the surface that matches your environment — MCP if your host supports it, the CLI if you have a shell, plain REST otherwise — follow the matching section below, then confirm it works by formatting `10.1038/nphys1170` in APA style. No API key is needed for any of them.

---

## Installation

Everything below runs **anonymously — no API key required** — on a rate-limited free tier. Nothing in these snippets needs replacing before it works.

### MCP Server (recommended for AI assistants)

**Hosted endpoint (no install)** — point any client that speaks Streamable HTTP at `https://scholar-sidekick.com/api/mcp`. In Claude Code:

```bash
claude mcp add --transport http scholar-sidekick https://scholar-sidekick.com/api/mcp
```

**Claude.ai / Claude Desktop (connectors directory)** — listed as a Community connector. Open Customize → Connectors, search "Scholar Sidekick", click Connect. No install, no key; runs on the hosted endpoint's free anonymous tier. Details: https://scholar-sidekick.com/mcp#claude-connector

**Claude Desktop** — add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "scholar-sidekick": {
      "command": "npx",
      "args": ["-y", "scholar-sidekick-mcp@latest"]
    }
  }
}
```

**Claude Code** — the plugin installs the server _and_ the companion agent skill, so Claude knows _when_ to reach for the tools, not just how:

```bash
/plugin marketplace add mlava/scholar-sidekick-mcp
/plugin install scholar-sidekick@scholar-sidekick

# Or the server alone:
claude mcp add scholar-sidekick -- npx -y scholar-sidekick-mcp@latest
```

**Cursor / VS Code / Windsurf** — add to `.cursor/mcp.json` or `.vscode/mcp.json` (VS Code uses a top-level `servers` key instead of `mcpServers`):

```json
{
  "mcpServers": {
    "scholar-sidekick": {
      "command": "npx",
      "args": ["-y", "scholar-sidekick-mcp@latest"]
    }
  }
}
```

**Raising your rate limits (optional)** — add an `env` block setting `SCHOLAR_API_KEY` to a free first-party `ssk_` key from https://scholar-sidekick.com/account. See [Configuration](#configuration) for the full precedence rules; do not set `SCHOLAR_API_KEY` and `RAPIDAPI_KEY` together.

```json
      "env": {
        "SCHOLAR_API_KEY": "${API_KEY}"
      }
```

**Gemini CLI / Antigravity** — install the [`scholar-sidekick-gemini`](https://github.com/mlava/scholar-sidekick-gemini) extension (bundles the MCP server above plus `/scholar:*` slash commands; no key required):

```bash
gemini extensions install https://github.com/mlava/scholar-sidekick-gemini
# Antigravity CLI: agy plugin import gemini
```

**Agent skills (skills.sh)** — companion [Agent Skills](https://www.skills.sh/mlava/scholar-sidekick-skills) that teach agents when and how to use these tools. Four are published in the dedicated [`scholar-sidekick-skills`](https://github.com/mlava/scholar-sidekick-skills) repo: `scholar-sidekick-api` (zero-install, plain REST over `curl`, no key), `scholar-sidekick-mcp` (for hosts that have the MCP server above connected), `scholar-sidekick-cli` (for the `scholar` terminal command), and `scholar-sidekick-python` (for agents running Python, via the `scholar-sidekick` PyPI package):

```bash
npx skills add mlava/scholar-sidekick-skills
```

### CLI (terminal / shell scripts)

For command-line and CI/CD use, the [`scholar-sidekick-cli`](https://github.com/mlava/scholar-sidekick-cli) npm package exposes the same REST endpoints as a `scholar` command. No key is required for the free tier.

```bash
npm i -g scholar-sidekick-cli

scholar format 10.1038/nphys1170 --style apa
scholar export PMID:30049270 --format ris > refs.ris
scholar verify --title "Some title" --doi 10.1038/nphys1170
scholar retraction 10.1038/nphys1170
scholar oa 10.1038/nphys1170
```

Add `--json` to any command for machine-readable output. Commands: `format`, `resolve`, `export`, `format-items`, `stream`, `verify`, `retraction`, `oa`, `styles`, `health`.

### Python (scripts, notebooks, Python agents)

The [`scholar-sidekick`](https://pypi.org/project/scholar-sidekick/) PyPI package ([source](https://github.com/mlava/scholar-sidekick-python)) exposes the same REST endpoints as a typed Python client, sync and async. No key is required for the free tier.

```bash
pip install scholar-sidekick
```

```python
from scholar_sidekick import ScholarSidekick

client = ScholarSidekick()
client.verify(title="Some title", doi="10.1038/nphys1170").verdict  # matched | mismatch | ambiguous | not_found

# Whole-bibliography audit of any length — chunks past the per-call cap and paces itself.
report = client.audit_bibliography(references)
report.needs_review            # entries a human should check
```

Prefer this over hand-rolled `requests` calls when working in Python: it handles the audit cap, rate-limit pacing, retries and partial failure. `AsyncScholarSidekick` is the async equivalent.

---

## Configuration

**No variable is required.** With none set, every surface runs anonymously on the rate-limited free tier.

| Variable                      | Required | Description                                                                                                                                                                 |
| ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SCHOLAR_API_KEY`             | No       | Free first-party `ssk_` key from https://scholar-sidekick.com/account; raises rate limits and enables the verifier's LLM screen. **Mutually exclusive with `RAPIDAPI_KEY`** |
| `RAPIDAPI_KEY`                | No       | RapidAPI subscription key for paid/managed tiers; when set, calls route through the RapidAPI gateway. **Takes precedence over `SCHOLAR_API_KEY`**                           |
| `RAPIDAPI_HOST`               | No       | Override host (default: `scholar-sidekick.p.rapidapi.com`)                                                                                                                  |
| `SCHOLAR_SIDEKICK_URL`        | No       | Override the API base URL (default: `https://scholar-sidekick.com`)                                                                                                         |
| `SCHOLAR_SIDEKICK_TIMEOUT_MS` | No       | Request timeout ms (default: `30000`)                                                                                                                                       |

The three auth routes are **alternatives, not layers**: anonymous (set nothing), a first-party `ssk_` key (`SCHOLAR_API_KEY`), or RapidAPI (`RAPIDAPI_KEY`). If both keys are set, `RAPIDAPI_KEY` wins and `SCHOLAR_API_KEY` is ignored — the server warns on stderr at startup (v0.8.7+). A `SCHOLAR_API_KEY` left at the example placeholder is ignored rather than sent, so a pasted snippet degrades to anonymous instead of 401ing every call.

Free first-party key: https://scholar-sidekick.com/account · Paid/managed tiers: https://rapidapi.com/scholar-sidekick-scholar-sidekick-api/api/scholar-sidekick

---

## Usage

### Via MCP (natural language)

Once connected, ask your AI assistant:

```
Format 10.1056/NEJMoa2033700 in Vancouver style
Resolve PMID:30049270 and export as BibTeX
Format these identifiers as AMA: 10.1038/nphys1170, PMID:30049270, ISBN:9780192854087
```

### Via REST API

**Base URL:** `https://scholar-sidekick.com`

**Format a citation:**

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/format" \
  -H "Content-Type: application/json" \
  -d '{"text": "10.1038/nphys1170", "style": "vancouver", "output": "text"}'
```

**Export to BibTeX:**

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/export" \
  -H "Content-Type: application/json" \
  -d '{"text": "10.1038/nphys1170\nPMID:30049270", "format": "bibtex"}' \
  -o refs.bib
```

**Resolve metadata only:**

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/format" \
  -H "Content-Type: application/json" \
  -d '{"text": "10.1038/nphys1170", "style": "vancouver", "output": "text"}'
# Returns: { "ok": true, "formatter": "builtin", "styleUsed": "vancouver", "outputMode": "text",
#            "itemsIn": 1, "itemsOut": 1, "items": [...], "text": "Aspelmeyer M. Measured ...",
#            "warnings": [], "meta": { "linesIn": 1, "resolved": 1, "notFound": 0 } }
# The citation is the whole-batch "text" string — there is no per-item "formatted" field.
```

### Supported identifiers

Pass any mix of these — one per line in the `text` field:

- `10.1038/nphys1170` — DOI
- `PMID:30049270` — PubMed ID
- `PMC7793608` — PubMed Central ID
- `ISBN:9780192854087` — ISBN (10 or 13 digit)
- `arXiv:2301.07041` — arXiv ID
- `2001ApJ...552..459C` — ADS bibcode
- WHO IRIS URLs

### Citation styles

Built-ins: `vancouver`, `ama`, `apa`, `ieee`, `cse`

Any CSL style ID also works: `chicago-author-date`, `nature`, `lancet`, `mla`, `harvard`, etc.

### Export formats

`bibtex`, `ris`, `csl-json`, `endnote-xml`, `refworks`, `nbib`, `rdf`, `csv`, `txt`

### Rate limits

Anonymous-tier limits, measured against production 2026-08-05 (the live `RateLimit-Limit` / `X-RateLimit-Limit` response header is authoritative, not this table — allowances are environment-tunable):

| Route family                                                            | Limit             |
| ----------------------------------------------------------------------- | ----------------- |
| `/api/format`, `/api/format/stream`, `/api/export`, `/api/format-items` | 10 requests / 60s |
| `/api/retraction-check`, `/api/oa-check`, `/api/verify`                 | 60 requests / 60s |
| `/api/audit`                                                            | 4 requests / 30s  |

A free `ssk_` key (see [Configuration](#configuration)) raises this ~5×; RapidAPI paid tiers scale further. Full tier table: https://scholar-sidekick.com/docs#pricing

### Error codes

Every 4xx/5xx response is `{ "ok": false, "code": "<CODE>", "error": "<message>" }`, mirrored in the `X-Error-Code` header. Full set, by status:

| Status | Codes                                                                                                                                               |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400    | `BAD_REQUEST`, `VALIDATION_ERROR`, `UNKNOWN_STYLE`, `INVALID_CONTENT_TYPE`, `EMPTY_BODY`, `MALFORMED_JSON`, `MISSING_TITLE`, `LLM_SCREEN_FORBIDDEN` |
| 401    | `AUTH_MISSING`, `AUTH_INVALID`                                                                                                                      |
| 403    | `AUTH_DISABLED`, `STREAMING_DISABLED`                                                                                                               |
| 404    | `NOT_FOUND`                                                                                                                                         |
| 405    | `READ_ONLY` (mutating call while `READ_ONLY_MODE=1`)                                                                                                |
| 413    | `PAYLOAD_TOO_LARGE`                                                                                                                                 |
| 422    | `IDEMPOTENCY_KEY_REUSED`                                                                                                                            |
| 429    | `RL_BLOCKED` (not `RATE_LIMITED`)                                                                                                                   |
| 500    | `ROUTE_ERROR`                                                                                                                                       |
| 502    | `UPSTREAM_ERROR`, `UPSTREAM_RATE_LIMITED`, `UPSTREAM_UNAVAILABLE`, `UPSTREAM_NETWORK_ERROR`, `RESOLVE_ERROR`                                        |
| 503    | `MAINTENANCE` (`MAINTENANCE_MODE=1`)                                                                                                                |
| 504    | `UPSTREAM_TIMEOUT`                                                                                                                                  |

Full machine-readable definition: the `ErrorResponse` schema in the [OpenAPI spec](https://scholar-sidekick.com/openapi/openapi.yml). Human reference: [/docs#errors](https://scholar-sidekick.com/docs#errors).

---

## MCP Tools

| Tool                | Description                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `verifyCitation`    | Check whether a claimed citation matches the record at its identifier                                               |
| `auditBibliography` | Verify a whole bibliography (BibTeX / RIS / CSL-JSON) in one call — per-entry verdict + retraction + corpus summary |
| `checkRetraction`   | Check a work's retraction / correction / expression-of-concern status                                               |
| `checkOpenAccess`   | Check open-access status and find the best legal full-text URL                                                      |
| `resolveIdentifier` | Resolve identifiers to structured metadata                                                                          |
| `formatCitation`    | Format identifiers in a citation style                                                                              |
| `exportCitation`    | Export identifiers to a bibliography file format                                                                    |

`resolveIdentifier`, `formatCitation`, and `exportCitation` accept multiple identifiers separated by newlines (batch); `auditBibliography` audits a whole bibliography through the verifier in one call. `checkRetraction`, `checkOpenAccess`, and `verifyCitation` take a single identifier per call.

### WebMCP (in-browser, experimental)

These same seven tools are also exposed **in the browser** via [WebMCP](https://developer.chrome.com/docs/ai/webmcp). When [scholar-sidekick.com](https://scholar-sidekick.com) is opened in a browser whose experimental in-browser Model Context API is enabled (Chrome's `navigator.modelContext`, origin-trial / flag stage), the page registers `verifyCitation`, `auditBibliography`, `checkRetraction`, `checkOpenAccess`, `resolveIdentifier`, `formatCitation`, and `exportCitation` directly to the in-browser AI agent — each tool calls the same same-origin REST API as the hosted MCP server. No install and no API key; it self-disables in browsers without WebMCP support, so a page visit is unaffected when the API is absent. This is a preview surface tracking an emerging web standard, not a stable contract.

---

## Discovery / `.well-known/`

For machine-readable provenance and reproducibility metadata at canonical paths:

| Path                                   | Purpose                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/.well-known/openapi.yaml`            | OpenAPI 3.1 spec at the canonical discovery path (mirrors `/openapi/openapi.yml`)                                                                                                                                                                                                                                                                                                                  |
| `/.well-known/sources.json`            | Data source manifest — resolver chain, fallback order per identifier type, allowlisted hosts, network-safety guarantees, `transform_version`                                                                                                                                                                                                                                                       |
| `/.well-known/ai-plugin.json`          | ChatGPT / agent plugin manifest pointing at the OpenAPI spec; `auth.type` = `none`                                                                                                                                                                                                                                                                                                                 |
| `/.well-known/api-catalog`             | RFC 9727 linkset — catalog anchor with `item` links to each API, plus `service-desc`, `service-doc`, `status`, `describedby` context objects                                                                                                                                                                                                                                                       |
| `/.well-known/ai-catalog.json`         | AI Catalog (ai-catalog.io) — owner-published manifest of every agentic artifact (MCP server card, A2A agent card, the 7 agent skills, OpenAPI, llms.txt) for agentic-resource-discovery (ARD) registries                                                                                                                                                                                           |
| `/.well-known/mcp/server-card.json`    | SEP-1649 MCP server card — name, version, transport (`stdio` via `npx`), and capability list                                                                                                                                                                                                                                                                                                       |
| `/.well-known/agent-skills/index.json` | Agent Skills Discovery RFC v0.2.0 index — 7 skills (resolve/format/export/retraction/OA/verify/audit), each with a SHA-256 digest                                                                                                                                                                                                                                                                  |
| `/.well-known/agent-card.json`         | A2A agent card — identity, the 7 skills (each mapped to its REST endpoint + MCP tool), supported identifiers, output formats, auth, and links to every surface above. Preferred transport is the native A2A JSON-RPC endpoint at `/api/a2a` (SendMessage → direct Message reply; select a skill via `message.metadata.skill`, default `format-citation`). Also served at `/.well-known/agent.json` |

The homepage `/` also emits an RFC 8288 `Link:` response header pointing at all of the above plus `/openapi.yaml`, `/docs`, `/api/health`, `/llms.txt`, `/index.md`, and `/sitemap.xml`.

**Authentication:** Anonymous access is available at the lowest rate-limit tier — no key required. For higher limits, create a free first-party API key (prefixed `ssk_`) at [https://scholar-sidekick.com/account](https://scholar-sidekick.com/account) and send it as `Authorization: Bearer ssk_…`. The RapidAPI gateway (`X-RapidAPI-Key`) serves paid/managed tiers. Scholar Sidekick runs **no** OAuth/OIDC authorization or token flow — credentials are opaque `ssk_` API keys, and there is intentionally no `/.well-known/openid-configuration`. For agent discovery it does publish RFC 9728 [`/.well-known/oauth-protected-resource`](https://scholar-sidekick.com/.well-known/oauth-protected-resource) and an RFC 8414 [`/.well-known/oauth-authorization-server`](https://scholar-sidekick.com/.well-known/oauth-authorization-server); the latter exists solely to host the WorkOS auth.md `agent_auth` block (`anonymous` + `api_key`) and advertises no OAuth endpoints. There is also intentionally no `/.well-known/http-message-signatures-directory` (Web Bot Auth / RFC 9421): that directory is a _bot-operator_ artifact advertising the Ed25519 keys a client signs its **outbound** requests with, and Scholar Sidekick is the destination server — it signs no outbound traffic, so publishing such a directory would claim a capability it does not have. Full prose walkthrough: [/auth.md](https://scholar-sidekick.com/auth.md).

Every API response includes the `x-scholar-transform-version` response header. Identical inputs at a fixed `transform_version` produce byte-identical output. Edge-case behaviour, the resolver-chain semantics, and the precise rules for when `transform_version` is bumped are documented at [/engineering-principles](https://scholar-sidekick.com/engineering-principles) ([markdown](https://scholar-sidekick.com/engineering-principles.md)).

A copy-paste verification kit — curl commands and expected outputs that let an external evaluator independently verify the determinism, provenance, and edge-case claims against the live API — lives at [/verification](https://scholar-sidekick.com/verification) ([markdown](https://scholar-sidekick.com/verification.md)).

Every `transform_version` and `verify_version` bump is recorded in the changelog at [/changelog](https://scholar-sidekick.com/changelog) ([markdown](https://scholar-sidekick.com/changelog.md)), tagged output-affecting, verdict-affecting, breaking, or non-breaking, so a client can detect drift and re-baseline pinned output. The current `transform_version` is also mirrored in [/.well-known/sources.json](https://scholar-sidekick.com/.well-known/sources.json) (`changelog_url` field links back here).

Service availability — rolling uptime and incident history for the public API — is published at the status page [https://status.scholar-sidekick.com](https://status.scholar-sidekick.com). The headline status reflects Scholar Sidekick's own API only; upstream metadata-source health (Crossref, PubMed, DataCite, arXiv, ADS, Open Library, Unpaywall, WHO IRIS) is reported in a separate, clearly-labelled informational section that does not trip the overall status. The status page URL is also mirrored in [/.well-known/sources.json](https://scholar-sidekick.com/.well-known/sources.json) (`status_url` field).

---

## Citation integrity (the verifier surface)

A long-form explainer covering the dominant citation-fabrication pattern that Topaz et al. (Lancet 2026) documented across 2.5 million biomedical papers — real DOI + invented title — and how Scholar Sidekick's `/api/verify` endpoint catches it. Includes the three illustrative Lancet cases verbatim, the CITADEL→Scholar Sidekick methodology mapping, an inline verifier demo, and the measured 20/20 precision/recall validation set with downloadable JSON receipts. Lives at [/citation-integrity](https://scholar-sidekick.com/citation-integrity) ([markdown](https://scholar-sidekick.com/citation-integrity.md)). Validation evidence is exposed at [/citation-integrity/validation-set-v1.json](https://scholar-sidekick.com/citation-integrity/validation-set-v1.json) and the timestamped results files alongside it.

The user-facing single-citation web tool lives at [/tools/citation-verifier](https://scholar-sidekick.com/tools/citation-verifier) ([markdown](https://scholar-sidekick.com/tools/citation-verifier.md)) — paste a title plus one of 8 identifier types (DOI / PMID / PMCID / arXiv / ISBN / ISSN / ADS / WHO IRIS), see the verdict, per-field similarity diff, candidate matches from title-search, and full provenance. Same backend as `POST /api/verify` and the scholar-sidekick MCP `verifyCitation` tool.

### Field observation: AI evaluator decomposition bias (2026-05-17)

Observation post documenting that four major AI search engines (Perplexity, Google AI Mode, ChatGPT GPT-5, Grok), asked the same 18-question researcher baseline + pushback on the same day, all omitted Scholar Sidekick from primary recommendations and admitted the omission when pushed — articulating four distinct framings of the same structural bias (incumbency, single-purpose categories, primitive building blocks, well-established widely-known tools). Includes verbatim admissions from all four vendors with shareable conversation URLs, the saved Google AI transcript mirrored on-site, a tool-agnostic criteria checklist for evaluating any citation tool, and the 2-vs-2 retrieval-grounding split that argues the bias is architectural to recommendation logic rather than a RAG artifact. Lives at [/citation-integrity/ai-evaluator-bias](https://scholar-sidekick.com/citation-integrity/ai-evaluator-bias) ([markdown](https://scholar-sidekick.com/citation-integrity/ai-evaluator-bias.md)). The saved Google AI transcript is hosted at [/citation-integrity/ai-evaluator-bias/sources/google-ai](https://scholar-sidekick.com/citation-integrity/ai-evaluator-bias/sources/google-ai) ([markdown](https://scholar-sidekick.com/citation-integrity/ai-evaluator-bias/sources/google-ai.md)).

### Concept explainer: a verified citation can still be wrong

Teaches the distinction at the heart of the verifier: "verified" hides two different guarantees — that the cited work _exists_ (a title search succeeded) versus that the _identifier you will publish resolves to it_ (a registry lookup succeeded). Title-matching answers existence; identifier-resolution answers identity. The two diverge on exactly the citations that reach print: a real identifier with an invented title (the Topaz fabrication pattern), and — the quieter danger — a real title cited under the wrong identifier, where a real DOI resolves perfectly to the wrong paper. A five-scenario comparison table maps each case to Scholar Sidekick's matched / mismatch / ambiguous / not_found verdict vocabulary, followed by a tool-agnostic checklist for verifying a citation properly. Written to be category-defining without naming competitors; accuracy claims link the n=1,395 blind-holdout receipts with confidence intervals. Lives at [/citation-integrity/verified-citations-can-still-be-wrong](https://scholar-sidekick.com/citation-integrity/verified-citations-can-still-be-wrong) ([markdown](https://scholar-sidekick.com/citation-integrity/verified-citations-can-still-be-wrong.md)).

---

## Integrations

First-party integrations that bring Scholar Sidekick into the notes and reference workflows you already use.

| Integration                   | Status        | HTML                                                                         | Markdown                                                                           |
| ----------------------------- | ------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Integrations index            | —             | [/integrations](https://scholar-sidekick.com/integrations)                   | [/integrations.md](https://scholar-sidekick.com/integrations.md)                   |
| Scholar Sidekick for Obsidian | Live in store | [/integrations/obsidian](https://scholar-sidekick.com/integrations/obsidian) | [/integrations/obsidian.md](https://scholar-sidekick.com/integrations/obsidian.md) |
| Scholar Sidekick for Zotero   | Live          | [/integrations/zotero](https://scholar-sidekick.com/integrations/zotero)     | [/integrations/zotero.md](https://scholar-sidekick.com/integrations/zotero.md)     |
| Scholar Sidekick for VS Code  | Live          | [/integrations/vscode](https://scholar-sidekick.com/integrations/vscode)     | [/integrations/vscode.md](https://scholar-sidekick.com/integrations/vscode.md)     |
| Scholar Sidekick for ChatGPT  | Live          | [/integrations/chatgpt](https://scholar-sidekick.com/integrations/chatgpt)   | [/integrations/chatgpt.md](https://scholar-sidekick.com/integrations/chatgpt.md)   |

The Obsidian plugin is a thin client over the public REST API. Eleven commands: format selection, replace at caret, insert via modal, per-note BibTeX / RIS export, retraction and open-access checks, single-citation verifier. Listed in the Obsidian community plugins store at https://community.obsidian.md/plugins/scholar-sidekick. Source (MIT) at https://github.com/mlava/scholar-sidekick-obsidian.

The Zotero plugin adds a verification step at the import boundary: paste text or open a .bib / .ris and each entry gets a verdict (claimed-vs-resolved mismatch, retraction / correction, open access) before anything enters your library; import only the clean items, each with a verification note. Zotero 7-9. Source (MIT) at https://github.com/mlava/scholar-sidekick-zotero.

The VS Code extension lints a `.bib` file in place — VS Code (Marketplace: https://marketplace.visualstudio.com/items?itemName=scholar-sidekick.scholar-sidekick-vscode) plus Cursor, Windsurf, Positron, and VSCodium (Open VSX: https://open-vsx.org/extension/scholar-sidekick/scholar-sidekick-vscode). Each entry is checked for the claimed-vs-resolved fabrication pattern, retractions, and open-access status, surfaced as inline diagnostics and hover cards. It is the verify layer Quarto and Zotero don't have — not a citation inserter. Source (MIT) at https://github.com/mlava/scholar-sidekick-vscode.

The ChatGPT App (OpenAI Apps SDK) lets ChatGPT call Scholar Sidekick directly inside a conversation: verify whether a claimed citation is real (the real-DOI + fabricated-title pattern), format any identifier in 10,000+ styles, and check retraction status — each answer rendered as an interactive citation card. Free, no sign-in or API key. Listing: https://chatgpt.com/apps/scholar-sidekick/asdk_app_6a1cfe08d3a081919ed00f619418c457. Backed by the no-auth Streamable-HTTP endpoint https://scholar-sidekick.com/api/apps/mcp.

---

## Free Tools

Single-purpose web tools, each backed by the same REST API + MCP server, each with a markdown mirror for agent discovery.

| Tool                          | HTML                                                                                                   | Markdown                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Citation Verifier             | [/tools/citation-verifier](https://scholar-sidekick.com/tools/citation-verifier)                       | [/tools/citation-verifier.md](https://scholar-sidekick.com/tools/citation-verifier.md)                       |
| Scholarly Identifier Detector | [/tools/identifier-detector](https://scholar-sidekick.com/tools/identifier-detector)                   | [/tools/identifier-detector.md](https://scholar-sidekick.com/tools/identifier-detector.md)                   |
| Identifier Validator          | [/tools/identifier-validator](https://scholar-sidekick.com/tools/identifier-validator)                 | [/tools/identifier-validator.md](https://scholar-sidekick.com/tools/identifier-validator.md)                 |
| DOI Lookup                    | [/tools/doi-lookup](https://scholar-sidekick.com/tools/doi-lookup)                                     | [/tools/doi-lookup.md](https://scholar-sidekick.com/tools/doi-lookup.md)                                     |
| PMID / PMCID / DOI Converter  | [/tools/pubmed-id-converter](https://scholar-sidekick.com/tools/pubmed-id-converter)                   | [/tools/pubmed-id-converter.md](https://scholar-sidekick.com/tools/pubmed-id-converter.md)                   |
| DOI to BibTeX Converter       | [/tools/doi-to-bibtex](https://scholar-sidekick.com/tools/doi-to-bibtex)                               | [/tools/doi-to-bibtex.md](https://scholar-sidekick.com/tools/doi-to-bibtex.md)                               |
| GB/T 7714 Citation Generator  | [/tools/gb-t-7714-citation-generator](https://scholar-sidekick.com/tools/gb-t-7714-citation-generator) | [/tools/gb-t-7714-citation-generator.md](https://scholar-sidekick.com/tools/gb-t-7714-citation-generator.md) |
| AMA Citation Generator        | [/tools/ama-citation-generator](https://scholar-sidekick.com/tools/ama-citation-generator)             | [/tools/ama-citation-generator.md](https://scholar-sidekick.com/tools/ama-citation-generator.md)             |
| Vancouver Citation Generator  | [/tools/vancouver-citation-generator](https://scholar-sidekick.com/tools/vancouver-citation-generator) | [/tools/vancouver-citation-generator.md](https://scholar-sidekick.com/tools/vancouver-citation-generator.md) |
| IEEE Citation Generator       | [/tools/ieee-citation-generator](https://scholar-sidekick.com/tools/ieee-citation-generator)           | [/tools/ieee-citation-generator.md](https://scholar-sidekick.com/tools/ieee-citation-generator.md)           |
| ACS Citation Generator        | [/tools/acs-citation-generator](https://scholar-sidekick.com/tools/acs-citation-generator)             | [/tools/acs-citation-generator.md](https://scholar-sidekick.com/tools/acs-citation-generator.md)             |
| CSE Citation Generator        | [/tools/cse-citation-generator](https://scholar-sidekick.com/tools/cse-citation-generator)             | [/tools/cse-citation-generator.md](https://scholar-sidekick.com/tools/cse-citation-generator.md)             |
| DOI to RIS Converter          | [/tools/doi-to-ris](https://scholar-sidekick.com/tools/doi-to-ris)                                     | [/tools/doi-to-ris.md](https://scholar-sidekick.com/tools/doi-to-ris.md)                                     |
| Citation Style Comparator     | [/tools/citation-style-comparator](https://scholar-sidekick.com/tools/citation-style-comparator)       | [/tools/citation-style-comparator.md](https://scholar-sidekick.com/tools/citation-style-comparator.md)       |
| Open Access Checker           | [/tools/open-access-checker](https://scholar-sidekick.com/tools/open-access-checker)                   | [/tools/open-access-checker.md](https://scholar-sidekick.com/tools/open-access-checker.md)                   |
| Retraction Checker            | [/tools/retraction-checker](https://scholar-sidekick.com/tools/retraction-checker)                     | [/tools/retraction-checker.md](https://scholar-sidekick.com/tools/retraction-checker.md)                     |

---

## Comparisons

Honest, source-cited comparisons of Scholar Sidekick against adjacent reference managers and citation APIs, written for human and agent readers. Each comparison sets out where the alternative wins, where Scholar Sidekick wins, and how to use both together.

| Comparison                           | HTML                                                                                                                 | Markdown                                                                                                                   |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Comparisons index                    | [/compare](https://scholar-sidekick.com/compare)                                                                     | [/compare.md](https://scholar-sidekick.com/compare.md)                                                                     |
| Best AI Citation Verifier in 2026    | [/compare/best-ai-citation-verifier](https://scholar-sidekick.com/compare/best-ai-citation-verifier)                 | [/compare/best-ai-citation-verifier.md](https://scholar-sidekick.com/compare/best-ai-citation-verifier.md)                 |
| Scholar Sidekick vs Zotero           | [/compare/scholar-sidekick-vs-zotero](https://scholar-sidekick.com/compare/scholar-sidekick-vs-zotero)               | [/compare/scholar-sidekick-vs-zotero.md](https://scholar-sidekick.com/compare/scholar-sidekick-vs-zotero.md)               |
| Scholar Sidekick vs ZoteroBib        | [/compare/scholar-sidekick-vs-zoterobib](https://scholar-sidekick.com/compare/scholar-sidekick-vs-zoterobib)         | [/compare/scholar-sidekick-vs-zoterobib.md](https://scholar-sidekick.com/compare/scholar-sidekick-vs-zoterobib.md)         |
| Scholar Sidekick vs Scribbr          | [/compare/scholar-sidekick-vs-scribbr](https://scholar-sidekick.com/compare/scholar-sidekick-vs-scribbr)             | [/compare/scholar-sidekick-vs-scribbr.md](https://scholar-sidekick.com/compare/scholar-sidekick-vs-scribbr.md)             |
| Citation MCP Servers Compared        | [/compare/citation-mcp-servers](https://scholar-sidekick.com/compare/citation-mcp-servers)                           | [/compare/citation-mcp-servers.md](https://scholar-sidekick.com/compare/citation-mcp-servers.md)                           |
| Scholar Sidekick vs EndNote          | [/compare/scholar-sidekick-vs-endnote](https://scholar-sidekick.com/compare/scholar-sidekick-vs-endnote)             | [/compare/scholar-sidekick-vs-endnote.md](https://scholar-sidekick.com/compare/scholar-sidekick-vs-endnote.md)             |
| Scholar Sidekick vs MyBib            | [/compare/scholar-sidekick-vs-mybib](https://scholar-sidekick.com/compare/scholar-sidekick-vs-mybib)                 | [/compare/scholar-sidekick-vs-mybib.md](https://scholar-sidekick.com/compare/scholar-sidekick-vs-mybib.md)                 |
| Scholar Sidekick vs Cite This For Me | [/compare/scholar-sidekick-vs-citethisforme](https://scholar-sidekick.com/compare/scholar-sidekick-vs-citethisforme) | [/compare/scholar-sidekick-vs-citethisforme.md](https://scholar-sidekick.com/compare/scholar-sidekick-vs-citethisforme.md) |

---

## Sitemap

See the full sitemap (локальный ресурс исходного примера не включён) for all pages.
