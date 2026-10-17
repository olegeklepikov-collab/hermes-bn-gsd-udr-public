> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ScholarSidekick: mcp-markdown

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Scholar Sidekick MCP Server
description: Use Scholar Sidekick as an MCP server in Claude, Cursor, and other AI assistants.
doc_version: "1.0"
last_updated: "2026-07-14"
---

# Scholar Sidekick MCP Server

> Use Scholar Sidekick as an MCP server in Claude, Cursor, and other AI assistants.
> Last updated: 2026-07-14
> HTML version: https://scholar-sidekick.com/mcp

Scholar Sidekick is available as a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) server. This lets AI assistants such as Claude, Cursor, and other MCP-compatible clients resolve scholarly identifiers, format citations, and export bibliography files - directly within a conversation.

---

## Set up with a prompt

Rather than editing a config file by hand, paste one of these prompts into an assistant that can read a URL and run commands (Claude, ChatGPT, Cursor, Cline, Gemini CLI) and it will install and verify the right surface itself. Each prompt points at [/AGENTS.md](https://scholar-sidekick.com/AGENTS.md) rather than embedding a config, so it stays correct as setup instructions change. All three run anonymously — there is no key to paste.

### MCP server

```
Set yourself up to use Scholar Sidekick, a citation resolver and verifier, over MCP.

Read https://scholar-sidekick.com/AGENTS.md and follow its MCP installation instructions for whichever host you are running in. Prefer the hosted Streamable HTTP endpoint if this host supports remote MCP servers; otherwise use the local stdio server. It runs anonymously - do not ask me for an API key, and do not set RAPIDAPI_KEY.

Then verify the install by formatting DOI 10.1038/nphys1170 in APA style, and show me the result.
```

### Command-line CLI

```
Set yourself up to use Scholar Sidekick, a citation resolver and verifier, from the command line.

Read https://scholar-sidekick.com/AGENTS.md and follow its CLI installation instructions. It runs anonymously - do not ask me for an API key.

Then verify the install by running the format command on DOI 10.1038/nphys1170 in APA style, and show me the result.
```

### REST API (nothing to install)

```
Use Scholar Sidekick, a citation resolver and verifier, via its REST API. There is nothing to install.

Read https://scholar-sidekick.com/docs.md for the endpoint reference. The API is free and needs no key or signup.

Then confirm you can reach it by formatting DOI 10.1038/nphys1170 in APA style via POST /api/format, and show me the result.
```

Agentic installers that look for the `llms-install.md` convention (Cline and others) can read https://scholar-sidekick.com/llms-install.md directly.

---

## Available Tools

The MCP server exposes seven tools:

### verifyCitation

Check whether a *claimed* citation matches the record at its identifier - the dominant LLM citation-fabrication pattern is a real DOI paired with an invented title (Topaz et al., *The Lancet* 2026), which a plain lookup never catches. Takes a claimed title plus one identifier (DOI, PMID, PMCID, arXiv ID, ISBN, ISSN, ADS bibcode, or WHO IRIS URL); returns a verdict (`matched | mismatch | not_found | ambiguous`), a confidence tier, and a per-field similarity diff. Wraps [`POST /api/verify`](https://scholar-sidekick.com/api/verify).

### auditBibliography

Run the `verifyCitation` check across a WHOLE bibliography in one call. Takes either raw `bibliography` text (BibTeX / RIS / CSL-JSON, format auto-detected) or a `claims` array of pre-parsed references, and returns a per-entry verdict table plus a corpus `summary` (`{ total, matched, mismatch, ambiguous, not_found, errored, retracted }`). Each resolved entry also gets a retraction lookup (default; pass `checks: []` to skip). Capped at 25 entries per call, with the excess counted in `truncated`; per-entry leniency means one unresolvable entry becomes `status: "error"` without failing the batch. Reading the result: each entry's `index` is **1-based**, `sourceKey` echoes the entry's own key in the source file (BibTeX cite key, RIS `ID`, CSL-JSON `id`) so a verdict maps back to the user's bibliography, and `parseErrors[]` shares that index space — report those entries as unchecked, not clean. `summary.total` counts verifiable entries only, and `summary.retracted` is a separate axis from the verdict counts. Wraps [`POST /api/audit`](https://scholar-sidekick.com/api/audit).

### checkRetraction

Check whether a single work has been retracted, corrected, or had an expression of concern raised. Sourced from Crossref `updated-by` (Retraction Watch). Accepts a DOI, PMID, PMCID, arXiv ID, or ADS bibcode (non-DOI inputs are resolved to a DOI before lookup). Wraps [`POST /api/retraction-check`](https://scholar-sidekick.com/api/retraction-check).

### checkOpenAccess

Check whether a single work is openly accessible and where to find the best legal version. Sourced from Unpaywall. Returns OA status (gold/green/hybrid/bronze/closed), the best landing or PDF URL, license, and version when available. Wraps [`POST /api/oa-check`](https://scholar-sidekick.com/api/oa-check).

### resolveIdentifier

Resolve DOIs, PMIDs, PMCIDs, ISBNs, arXiv IDs, ISSNs, ADS bibcodes, and WHO IRIS URLs to structured bibliographic metadata (title, authors, journal, year, identifiers).

### formatCitation

Format one or more identifiers into a specific citation style. Supports Vancouver, AMA, APA, IEEE, CSE, and 10,000+ CSL styles. Output as text, HTML, or JSON.

### exportCitation

Export one or more identifiers to bibliography file formats: BibTeX, RIS, CSL JSON, EndNote (XML and Refer), RefWorks, MEDLINE/NBIB, Zotero RDF, CSV, or plain text.

`auditBibliography` batches a whole bibliography through the verifier; `resolveIdentifier`, `formatCitation`, and `exportCitation` accept multiple identifiers in a single request (separated by newlines), so batch operations work out of the box. `verifyCitation`, `checkRetraction`, and `checkOpenAccess` take a single identifier per call. For per-item enrichment across a batch, use the `?checks=retraction,oa` query flag on `POST /api/format`, `POST /api/format/stream`, or `POST /api/format-items` (which adds a per-item `_checks` sibling field to the response).

---

## Supported Identifiers

- DOIs (e.g. `10.1056/NEJMoa2033700`)
- PubMed IDs (e.g. `PMID:30049270`)
- PubMed Central IDs (e.g. `PMC7793608`)
- ISBNs (e.g. `ISBN:9780192854087`)
- arXiv IDs (e.g. `2301.08745`)
- ISSNs and eISSNs
- NASA ADS bibcodes
- WHO IRIS URLs

Identifiers are auto-detected and normalised. You can mix types freely in a single batch request.

---

## Compatible Clients

- Claude.ai and Claude Desktop (listed in the Claude connectors directory)
- Claude Code
- Cursor
- VS Code (with MCP extension)
- Windsurf
- Any MCP-compatible client

---

## Authentication

**No key required.** Everything runs anonymously by default on a rate-limited free tier: the hosted Streamable-HTTP endpoint (`POST https://scholar-sidekick.com/api/mcp`), the ChatGPT-app endpoint (`/api/apps/mcp`), and the stdio server (`scholar-sidekick-mcp`) all work with no credential.

To raise your limits, set one of (both optional):
- a **first-party API key** - create a free one (prefixed `ssk_`) at https://scholar-sidekick.com/account and set `SCHOLAR_API_KEY`; it authenticates against `scholar-sidekick.com` as `Authorization: Bearer ssk_…` and also enables the verifier's LLM screen, or
- a **RapidAPI key** (`RAPIDAPI_KEY`) - for paid/managed tiers via the RapidAPI gateway. If you already have a Scholar Sidekick subscription on RapidAPI, the same key works.

With both set, RapidAPI takes precedence. Get a RapidAPI key: https://rapidapi.com/scholar-sidekick-scholar-sidekick-api/api/scholar-sidekick

---

## Setup

Two ways to connect - both expose the same seven tools, talk to `https://scholar-sidekick.com`, and run anonymously by default. Add a free `ssk_` key (`SCHOLAR_API_KEY`) to raise your limits.

### Hosted endpoint (no install)

Point any client that speaks Streamable HTTP directly at the hosted endpoint - no npm install, no local process:

```
POST https://scholar-sidekick.com/api/mcp
```

It works anonymously; to authenticate, send `Authorization: Bearer ssk_…`.

Claude Code (HTTP transport):

Anonymous:

```bash
claude mcp add --transport http scholar-sidekick https://scholar-sidekick.com/api/mcp
```

Or with a free `ssk_` key:

```bash
claude mcp add --transport http scholar-sidekick https://scholar-sidekick.com/api/mcp \
  --header "Authorization: Bearer [СЕКРЕТ УДАЛЁН]"
```

Cursor / Windsurf (remote-server config in `.cursor/mcp.json`; omit `headers` to run anonymously):

```json
{
  "mcpServers": {
    "scholar-sidekick": {
      "url": "https://scholar-sidekick.com/api/mcp",
      "headers": {
        "Authorization": "Bearer [СЕКРЕТ УДАЛЁН]"
      }
    }
  }
}
```

VS Code uses a top-level `servers` key with `"type": "http"` and the same `url` / `headers` fields - or install it in one click from VS Code's built-in MCP gallery: open the Extensions view and search `@mcp` for Scholar Sidekick (listed via the [GitHub MCP Registry](https://github.com/mcp/mlava/scholar-sidekick-mcp)). The ChatGPT app has its own no-auth endpoint at `https://scholar-sidekick.com/api/apps/mcp` (a read-only, widget-backed surface built for the ChatGPT app).

### Self-managed (stdio via npx)

Prefer to run the server locally? The configs below launch it over stdio with `npx`. The `env` block is **optional** - omit it to run anonymously, or set `SCHOLAR_API_KEY` to a free `ssk_` key for higher limits.

### Claude.ai and Claude Desktop (connectors directory)

Scholar Sidekick is listed in the Claude connectors directory as a Community connector (see https://claude.com/docs/connectors/verification). In claude.ai or Claude Desktop, open **Customize → Connectors**, search for **Scholar Sidekick**, and click **Connect**. Nothing to install and no key: the listing points at the hosted endpoint on the free anonymous tier, and Claude can suggest the connector in-chat when a task involves citations. To raise your limits, use one of the keyed routes below instead.

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS). This runs on the free anonymous tier - no key, nothing to replace:

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

To raise your limits, add an `env` block alongside `args` - but only if you are *not* using a RapidAPI key (see [Choosing an auth route](#choosing-an-auth-route)). Replace the placeholder with your real key; left as-is it is ignored, with a warning:

```json
      "env": {
        "SCHOLAR_API_KEY": "${API_KEY}"
      }
```

### Claude Code

**Plugin (recommended)** - installs the MCP server *and* the companion agent skill in one step, so Claude knows *when* to reach for the tools, not just how. Runs anonymously; no key:

```bash
/plugin marketplace add mlava/scholar-sidekick-mcp
/plugin install scholar-sidekick@scholar-sidekick
```

Or add just the server manually - use this if you want to set a free `ssk_` key for higher limits:

Anonymous (no key):

```bash
claude mcp add scholar-sidekick -- npx -y scholar-sidekick-mcp@latest
```

Or with a free `ssk_` key for higher limits:

```bash
claude mcp add scholar-sidekick \
  -e SCHOLAR_API_KEY=${API_KEY} \
  -- npx -y scholar-sidekick-mcp@latest
```

### Cursor / VS Code / Windsurf

Add to `.cursor/mcp.json` or `.vscode/mcp.json` in your project. Anonymous by default; add an `env` block as shown under Claude Desktop above to use a key:

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

### Agent skill (optional)

Install a companion [Agent Skill](https://www.skills.sh/mlava/scholar-sidekick-skills) that teaches Claude Code, Cline, and other agents when and how to use these tools - it complements the server config above:

```bash
npx skills add mlava/scholar-sidekick-mcp
```

Already installed the Claude Code plugin (above)? You have this skill already - it ships inside the plugin. Skip this step.

---

## Choosing an auth route

Three routes, and they are **alternatives, not layers**. Pick one:

- **Anonymous** - set nothing. Works out of the box on the rate-limited free tier.
- **First-party key** - set only `SCHOLAR_API_KEY` to a free `ssk_` key from https://scholar-sidekick.com/account. Raises limits and enables the verifier's LLM screen.
- **RapidAPI** - set only `RAPIDAPI_KEY` for a paid RapidAPI subscription. This also switches the base URL to the RapidAPI gateway.

If you set **both** keys, `RAPIDAPI_KEY` wins and `SCHOLAR_API_KEY` is ignored - the server says so on stderr at startup (v0.8.7+). Setting `SCHOLAR_SIDEKICK_URL` alongside a RapidAPI key sends that key somewhere that will not honour it, which is also warned about. A `SCHOLAR_API_KEY` left at the example placeholder is ignored rather than sent, so a pasted snippet degrades to anonymous instead of 401ing every call.

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `SCHOLAR_API_KEY` | No | Free first-party `ssk_` key from https://scholar-sidekick.com/account; raises rate limits and enables the verifier's LLM screen. Sent as `Authorization: Bearer`. **Mutually exclusive with `RAPIDAPI_KEY`** |
| `RAPIDAPI_KEY` | No | RapidAPI subscription key for paid/managed tiers; when set, calls route through the RapidAPI gateway. **Takes precedence over `SCHOLAR_API_KEY`** |
| `RAPIDAPI_HOST` | No | RapidAPI host (default: `scholar-sidekick.p.rapidapi.com`) |
| `SCHOLAR_SIDEKICK_URL` | No | Override the API base URL (default: `https://scholar-sidekick.com`, or the RapidAPI gateway when `RAPIDAPI_KEY` is set) |
| `SCHOLAR_SIDEKICK_TIMEOUT_MS` | No | Request timeout in ms (default: 30000) |

No key at all → anonymous, rate-limited free tier. With both `SCHOLAR_API_KEY` and `RAPIDAPI_KEY` set, RapidAPI takes precedence.

---

## Available in MCP Registries

- GitHub: https://github.com/mlava/scholar-sidekick-mcp
- MCP Registry: https://registry.modelcontextprotocol.io/v0.1/servers?search=scholar-sidekick
- GitHub MCP Registry: https://github.com/mcp/mlava/scholar-sidekick-mcp
- mcpservers.org: https://mcpservers.org/servers/mlava/scholar-sidekick-mcp
- mcp.so: https://mcp.so/server/scholar-sidekick-mcp/mlava
- PulseMCP: https://www.pulsemcp.com/servers/mlava-scholar-sidekick-mcp
- ClawHub: https://clawhub.ai/mlava/scholar-sidekick-mcp
- Glama: https://glama.ai/mcp/servers/mlava/scholar-sidekick-mcp
- Goose: https://goose-docs.ai/extensions/detail?id=scholar-sidekick
- Smithery (hosted / remote HTTP): https://smithery.ai/servers/scholar-sidekick/remote
- Smithery (local / npm / stdio): https://smithery.ai/servers/scholar-sidekick/scholar-sidekick-mcp

---

## Example Usage

Once connected, you can ask your AI assistant:

- "Format 10.1056/NEJMoa2033700 in Vancouver style"
- "Resolve PMID:30049270 and export as BibTeX"
- "Format these three identifiers as AMA and save as a RIS file: 10.1056/NEJMoa2033700, PMID:30049270, ISBN:9780192854087"

The assistant will call the appropriate Scholar Sidekick tools and return the results directly in the conversation.

---

## Useful Workflows

- Format a DOI while drafting a document
- Batch-resolve a list of PMIDs during a literature review
- Export citations to RIS or BibTeX for import into a reference manager
- Generate formatted reference lists in a specific style on demand
- Verify bibliographic metadata for identifiers mid-conversation

---

## Relationship to the REST API

The MCP server wraps the same Scholar Sidekick API that powers the web tool and RapidAPI integration. The underlying resolution, formatting, and export logic is identical. MCP provides a standardised interface for AI assistants to call those same endpoints.

REST API docs: https://scholar-sidekick.com/docs
REST API docs (markdown): https://scholar-sidekick.com/docs.md

For terminal and shell-script use, the same endpoints are wrapped by the [`scholar-sidekick-cli`](https://github.com/mlava/scholar-sidekick-cli) npm package (command: `scholar`). The MCP server is for AI agents inside MCP-compatible hosts; the CLI is for command-line and CI/CD workflows. Both call the same REST API, so output is identical.

---

## Related

- API Docs: https://scholar-sidekick.com/docs
- API Docs (markdown): https://scholar-sidekick.com/docs.md
- Command-line CLI: https://github.com/mlava/scholar-sidekick-cli (npm: https://www.npmjs.com/package/scholar-sidekick-cli)
- Python client: https://github.com/mlava/scholar-sidekick-python (PyPI: https://pypi.org/project/scholar-sidekick/)
- RapidAPI listing: https://rapidapi.com/scholar-sidekick-scholar-sidekick-api/api/scholar-sidekick
- API Terms: https://scholar-sidekick.com/legal/api-terms

## Sitemap

See the full sitemap (локальный ресурс исходного примера не включён) for all pages.
