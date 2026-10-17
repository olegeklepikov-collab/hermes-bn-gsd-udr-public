> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ScholarSidekick: docs-markdown

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


---
title: Scholar Sidekick API Docs - Free Citation API for DOIs, PMIDs & ISBNs
description: Free citation API for DOIs, PubMed IDs, ISBNs, arXiv IDs, and ADS bibcodes. Endpoints, parameters, examples, headers, caching, and rate limits.
doc_version: "1.1"
last_updated: "2026-05-30"
---

# Scholar Sidekick API Docs - Free Citation API for DOIs, PMIDs & ISBNs

> Quick reference for endpoints, parameters, examples, and headers.
> Last updated: 2026-05-30
> HTML version: https://scholar-sidekick.com/docs

## Base URL

```
https://scholar-sidekick.com
```

OpenAPI specs:
- Public: https://scholar-sidekick.com/openapi/openapi.yml
- RapidAPI: https://scholar-sidekick.com/openapi/rapidapi/openapi.yml
- JSON (via API): https://scholar-sidekick.com/api/openapi

## Endpoints

```
GET  /api/health
POST /api/format
POST /api/format/stream     (NDJSON)
POST /api/format-items
POST /api/export
POST /api/verify            (citation verifier)
POST /api/audit             (bibliography audit)
POST /api/retraction-check
POST /api/oa-check
```

---

## POST /api/format

Formats a list of identifiers (DOI, PMID, PMCID, ISBN, ISSN, arXiv, ADS bibcode, WHO IRIS). Detects and normalises automatically.

### Request

```http
POST /api/format
Content-Type: application/json

{
  "text": "10.1038/nphys1170\nPMID: 34812345\n9780306406157",
  "style": "vancouver",
  "locale": "en-US",
  "output": "text",
  "footnote": false
}
```

**Fields:**
- `text` (string) - One identifier per line, or free text containing identifiers. Mixed types OK.
- `style` (string, optional) - Citation style. Builtins: `vancouver`, `ama`, `apa`, `ieee`, `cse`. Also accepts any CSL style ID (e.g. `chicago-author-date`, `nature`, `lancet`). Defaults to `vancouver`.
- `locale` (string, optional) - CSL locale, e.g. `en-US`, `en-GB`. Used for CSL styles only.
- `output` (string, optional) - `"text"` or `"html"`. Defaults to `"text"`.
- `footnotes` (boolean, optional) - When `output=html`, render as footnotes. Default: `false`.

### Response

```http
## 200 OK
X-Scholar-Cache: ENABLED|BYPASS
X-Scholar-Formatter: builtin|csl
X-Scholar-Style: vancouver
X-RateLimit-Limit: 30
X-RateLimit-Remaining: 28
X-RateLimit-Reset: 1736569200

{
  "ok": true,
  "formatter": "builtin",
  "styleRequested": "vancouver",
  "styleUsed": "vancouver",
  "lang": "en-US",
  "footnote": false,
  "outputMode": "text",
  "orderApplied": "input",
  "itemsIn": 1,
  "itemsOut": 1,
  "items": [
    {
      "id": "doi:10.1038/nphys1170",
      "type": "journal-article",
      "title": "Measured measurement",
      "idx": 0,
      "sourceIdxs": [0]
    }
  ],
  "html": "Aspelmeyer M. Measured measurement. <em>Nature Phys</em>. 2009;5(1):11-12. doi:10.1038/nphys1170.",
  "text": "Aspelmeyer M. Measured measurement. Nature Phys. 2009;5(1):11-12. doi:10.1038/nphys1170.",
  "warnings": [],
  "meta": { "linesIn": 1, "resolved": 1, "notFound": 0, "errored": 0 }
}
```

### cURL example

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/format" \
  -H "Content-Type: application/json" \
  -d '{"text":"10.1038/nphys1170","style":"vancouver","output":"text"}'
```

---

## POST /api/format/stream

Streaming NDJSON variant of `/api/format`. Emits one JSON object per line: `start` → `item` (one per identifier) → `done`.

Content-Type: `application/x-ndjson`

### cURL example

```bash
curl -N -sS -X POST "https://scholar-sidekick.com/api/format/stream" \
  -H "Content-Type: application/json" \
  -d '{"text":"10.1038/nphys1170\nPMID:34812345","style":"apa","output":"html"}'
```

---

## POST /api/format-items

Like `/api/format` but accepts already-resolved CSL JSON items - skips the resolution step.

### Request

```json
{
  "items": [ /* CSL-JSON bibliographic items */ ],
  "style": "apa",
  "output": "text"
}
```

---

## POST /api/export

Exports citations to a bibliography file format.

### Request

```http
POST /api/export
Content-Type: application/json

{
  "text": "10.1038/nphys1170\n9780306406157",
  "format": "ris",
  "style": "vancouver"
}
```

**Fields:**
- `text` (string) OR `items` (CSL-JSON[]) - Input identifiers or pre-resolved items.
- `format` (string, required) - Export format (see below).
- `style` (string, optional) - Citation style (used for `txt` format).

**Supported formats:**

| format | Description |
|---|---|
| `ris` | Research Information Systems (EndNote, Zotero, Mendeley) |
| `bibtex` | BibTeX (LaTeX, Overleaf, JabRef) |
| `csl-json` | Raw CSL-JSON structured metadata |
| `endnote-xml` | EndNote XML |
| `refworks` | RefWorks tagged format |
| `nbib` | MEDLINE/NBIB |
| `rdf` | Zotero RDF |
| `csv` | Comma-separated values |
| `txt` | Formatted plain-text citations |

### Response

Unlike the other endpoints, the body is the export file itself as a plain string -
not JSON. `Content-Type` varies by `format`, and `Content-Disposition` names the
file, so a browser or `curl -O` saves it directly.

```http
## 200 OK
Content-Type: application/x-research-info-systems; charset=utf-8
Content-Disposition: attachment; filename="citations.ris"; filename*=UTF-8''citations.ris

## TY  - JOUR
AU  - Aspelmeyer, Markus
TI  - Measured measurement
JO  - Nature Physics
## PY  - 2009
## VL  - 5
## IS  - 1
## SP  - 11
## EP  - 12
DO  - 10.1038/nphys1170
UR  - https://doi.org/10.1038/nphys1170
## ER  -
```

### cURL example

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/export" \
  -H "Content-Type: application/json" \
  -d '{"text":"10.1038/nphys1170\n9780306406157","format":"ris","style":"vancouver"}' \
  -o citations.ris
```

---

## POST /api/verify

Checks whether a *claimed* citation matches the record its identifier resolves to - catching the dominant AI-era fabrication pattern (a real, resolving DOI paired with a fabricated title). The verdict *is* the answer: `200 OK` on every produced verdict; `4xx`/`5xx` only for protocol errors (malformed JSON, missing `claimed.title` → `400 MISSING_TITLE`, resolver upstream failure → `502`).

### Request

```http
POST /api/verify
Content-Type: application/json

{
  "claimed": {
    "title": "A Novel Deep Learning Framework for Real-Time Citation Verification",
    "authors": [{ "family": "Chen", "given": "F" }],
    "year": 2023,
    "container": "Neuroscience",
    "doi": "10.1016/S0140-6736(26)00603-3"
  }
}
```

**Fields:**
- `claimed.title` (string, **required**) - The claimed title to verify.
- `claimed.authors`, `claimed.year`, `claimed.container` (optional) - Additional claimed metadata.
- `claimed.doi` / `pmid` / `pmcid` / `isbn` / `arxiv` / `issn` / `ads` (optional) - A claimed identifier. When supplied it is resolved and compared; when omitted the verifier falls back to a title search.

### Response

```http
## 200 OK
X-Scholar-Verify-Verdict: mismatch
X-Scholar-Verify-Confidence: high
X-Scholar-Verify-Version: 2026-05-26

{
  "ok": true,
  "verdict": "mismatch",
  "confidence": "high",
  "matched": {
    "title": "Fabricated citations: an audit across 2.5 million biomedical papers",
##     "DOI": "10.1016/S0140-6736(26)00603-3",
    "type": "article-journal"
  },
  "mismatches": [
    { "field": "title", "claimed": "A Novel Deep Learning Framework...", "resolved": "Fabricated citations...", "similarity": 0.12 }
  ],
  "_provenance": { "stages_run": ["compare"], "resolved_via": "crossref" }
}
```

Verdict is one of `matched | mismatch | ambiguous | not_found`, each with a `confidence` tier (`high | medium | low`). Known limitations: https://scholar-sidekick.com/citation-integrity/known-failures.md

### cURL example

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/verify" \
  -H "Content-Type: application/json" \
  -d '{"claimed":{"title":"A Novel Deep Learning Framework for Real-Time Citation Verification","doi":"10.1016/S0140-6736(26)00603-3"}}'
```

---

## POST /api/audit

Audit a WHOLE bibliography in one call — the batch counterpart to `/api/verify`. Each entry runs the same fabrication check plus a retraction lookup; the response carries a per-entry verdict table and a corpus summary.

### Request

Provide exactly one of `bibliography` (raw text), `claims` (array), or `references` (array):

```json
{ "bibliography": "@article{a, title={A real title}, doi={10.1038/nphys1170}}", "format": "bibtex", "options": { "checks": ["retraction"] } }
```

- `bibliography` (string) - raw BibTeX / RIS / CSL-JSON; format auto-detected (override with `format`).
- `claims` (array) - pre-parsed `{ "title": "...", + one identifier }` objects.
- `references` (array) - raw prose reference strings (the `.docx` upload path). Verified via the containment method: the resolved title is checked for word-containment in the reference text. Entries carry `_provenance.method: "containment"`; the version is pinned by `x-scholar-containment-version`.
- `options.checks` (array, default `["retraction"]`; pass `[]` to skip); `options.screen_with_llm` (boolean, default false).

Capped at 25 entries per call; excess is dropped and reported via `truncated`.

### Response

```json
{
  "ok": true,
  "format": "bibtex",
  "entries": [
    { "index": 1, "status": "ok", "verdict": "matched", "confidence": "high", "matched": { "...": "..." }, "retraction": { "checked": true, "doi": "10.1038/nphys1170", "isRetracted": false, "notices": [] } }
  ],
  "parseErrors": [],
  "truncated": 0,
  "summary": { "total": 1, "matched": 1, "mismatch": 0, "ambiguous": 0, "not_found": 0, "errored": 0, "retracted": 0 }
}
```

Returns 200 on every produced audit. Per-entry leniency: one unresolvable entry becomes `status: "error"` without failing the batch; a total verification outage returns 502.

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/audit" \
  -H "Content-Type: application/json" \
  -d '{"bibliography":"@article{a, title={A real title}, doi={10.1038/nphys1170}}\n@article{b, title={An invented title}, doi={10.1016/j.neuroscience.2023.02.008}}"}'
```

---

## POST /api/retraction-check

Resolves a single identifier (DOI, PMID, PMCID, arXiv, ADS bibcode) to a DOI and returns its retraction / correction / expression-of-concern status, sourced from Crossref `updated-by` (Retraction Watch).

### Request

```json
{ "id": "10.1056/nejmoa2033700" }
```

### Response

```json
{
  "ok": true,
  "doi": "10.1056/nejmoa2033700",
  "result": {
    "isRetracted": false,
    "hasCorrections": false,
    "hasConcern": false,
    "notices": [],
    "title": "Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine"
  }
}
```

`result` is `null` when no DOI could be resolved (the `reason` field then distinguishes `no_doi` / `timeout` / `upstream`).

### cURL example

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/retraction-check" \
  -H "Content-Type: application/json" \
  -d '{"id":"10.1056/nejmoa2033700"}'
```

---

## POST /api/oa-check

Resolves a single identifier to a DOI and returns its open-access status, sourced from Unpaywall - OA status (`gold`/`green`/`hybrid`/`bronze`/`closed`), the best legal landing / PDF URL, license, and version when available.

### Request

```json
{ "id": "10.1038/s41586-020-2649-2" }
```

### Response

```json
{
  "ok": true,
  "doi": "10.1038/s41586-020-2649-2",
  "result": {
    "isOa": true,
    "oaStatus": "hybrid",
    "title": "Array programming with NumPy",
    "bestLocation": {
      "url": "https://www.nature.com/articles/s41586-020-2649-2.pdf",
      "hostType": "publisher",
      "license": "cc-by",
      "version": "publishedVersion"
    },
    "locations": []
  }
}
```

### cURL example

```bash
curl -sS -X POST "https://scholar-sidekick.com/api/oa-check" \
  -H "Content-Type: application/json" \
  -d '{"id":"10.1038/s41586-020-2649-2"}'
```

---

## GET /api/health

Liveness check. Returns `{ "status": "ok", "time": "<ISO timestamp>" }`.

---

## Headers & Rate Limits

- `X-Scholar-Cache`: `BYPASS` or `ENABLED`
- `X-Scholar-Formatter`: `builtin` or `csl`
- `X-Scholar-Style`: style actually applied
- `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` - sliding-window rate limit
- `Retry-After` - present on HTTP 429

Plan tiers: anonymous, free, pro, ultra, mega. Anonymous-tier numbers per route family are in
[Pricing](#pricing) below.

### Authentication

Anonymous access works with no key at the lowest rate-limit tier.

For higher limits, create a free first-party API key (prefixed `ssk_`) at
[/account](https://scholar-sidekick.com/account) and send it as:
- `Authorization: Bearer ssk_…`

Paid/managed tiers are available via the RapidAPI gateway:
- `X-RapidAPI-Key: <key>` - via RapidAPI

Scholar Sidekick does not use OAuth/OIDC.

---

## Pricing

Every web tool is free with no account. The REST API and MCP server are free for light, anonymous use; for a monthly quota and higher rate limits, paid tiers are billed through RapidAPI. **Every tier has the full feature set** — only the monthly request quota and per-IP burst allowance scale with price.

| Plan | Price | Requests / month | Per-IP burst | Best for |
|------|-------|------------------|--------------|----------|
| BASIC | Free ($0 / mo) | 500 | 1× (base) | Trying the API, hobby scripts, low-volume agents |
| PRO | $9 / mo | 10,000 | 2× | Indie apps, research tooling, steady production use |
| ULTRA | $49 / mo | 100,000 | 4× | High-traffic apps and batch citation pipelines |
| MEGA | $199 / mo | 500,000 | 8× | Platforms and bulk bibliography processing at scale |

All prices are USD per month. Past the monthly quota, requests are billed per-request (BASIC/PRO $0.001, ULTRA $0.0008, MEGA $0.0005 each) and are never hard-cut mid-month. One call to any endpoint counts as one request, single or batch. Manage or cancel plans any time on [RapidAPI](https://rapidapi.com/scholar-sidekick-scholar-sidekick-api/api/scholar-sidekick); machine-readable pricing at [/pricing.md](https://scholar-sidekick.com/pricing.md).

**Anonymous-tier per-IP burst limits** (measured against production, 2026-08-05 — treat the live `RateLimit-Limit` / `X-RateLimit-Limit` response header as authoritative, not this table):

| Route family | Limit |
|---|---|
| `/api/format`, `/api/format/stream`, `/api/export`, `/api/format-items` | 10 requests / 60s |
| `/api/retraction-check`, `/api/oa-check`, `/api/verify` | 60 requests / 60s |
| `/api/audit` | 4 requests / 30s |

A free `ssk_` key raises this ~5×; PRO/ULTRA/MEGA scale further per the tier table above.

---

## Error Format

```json
{ "ok": false, "code": "BAD_REQUEST", "error": "human-readable message" }
```

Every 4xx/5xx response mirrors `code` in the `X-Error-Code` header. Full set, by status:

| Status | Codes |
|---|---|
| 400 | `BAD_REQUEST`, `VALIDATION_ERROR`, `UNKNOWN_STYLE`, `INVALID_CONTENT_TYPE`, `EMPTY_BODY`, `MALFORMED_JSON`, `MISSING_TITLE`, `LLM_SCREEN_FORBIDDEN` |
## | 401 | `AUTH_MISSING`, `AUTH_INVALID` |
## | 403 | `AUTH_DISABLED`, `STREAMING_DISABLED` |
## | 404 | `NOT_FOUND` |
| 405 | `READ_ONLY` (mutating call while `READ_ONLY_MODE=1`) |
## | 413 | `PAYLOAD_TOO_LARGE` |
## | 422 | `IDEMPOTENCY_KEY_REUSED` |
| 429 | `RL_BLOCKED` (not `RATE_LIMITED`) |
## | 500 | `ROUTE_ERROR` |
| 502 | `UPSTREAM_ERROR`, `UPSTREAM_RATE_LIMITED`, `UPSTREAM_UNAVAILABLE`, `UPSTREAM_NETWORK_ERROR`, `RESOLVE_ERROR` |
## | 503 | `MAINTENANCE` (`MAINTENANCE_MODE=1`) |
## | 504 | `UPSTREAM_TIMEOUT` |

Full machine-readable definition: the `ErrorResponse` schema in the [OpenAPI spec](https://scholar-sidekick.com/openapi/openapi.yml).

---

## ## FAQ

**Is there a free citation API?**
Yes. The Scholar Sidekick citation API is free for light, anonymous use with no key. A free first-party key raises the rate limit, and paid tiers add a higher monthly quota; every tier has the full feature set.

**How do I resolve a DOI to a citation with an API?**
POST the DOI to `/api/format` with a style, and the API returns a formatted citation. The same endpoint resolves PMID, PMCID, ISBN, ISSN, arXiv ID, and ADS bibcode — it detects and normalises the identifier type automatically.

**Is there a citation API for AI agents and coding agents?**
Yes. Scholar Sidekick is a REST API and an open-source MCP (Model Context Protocol) server, so Claude, ChatGPT, Cursor, and custom agents can call it directly. Output is deterministic and version-pinned, so identical input returns identical bytes.

**What is the rate limit, and does it need an API key?**
Anonymous access works with no key at the lowest sliding-window tier. For higher limits, create a free key (prefixed `ssk_`) at https://scholar-sidekick.com/account and send it as an `Authorization: Bearer` header. Paid/managed tiers are available via RapidAPI. Scholar Sidekick does not use OAuth.

**What can the API export to?**
POST to `/api/export` to get BibTeX, RIS, EndNote XML, RefWorks, MEDLINE/NBIB, Zotero RDF, CSL-JSON, or CSV. You can pass raw identifiers or already-resolved CSL-JSON items.

See the full overview at https://scholar-sidekick.com/citation-api

---

## Related

- Citation API overview: https://scholar-sidekick.com/citation-api
- MCP Server: https://scholar-sidekick.com/mcp
- MCP Server docs (markdown): https://scholar-sidekick.com/mcp.md
- Help & Limits: https://scholar-sidekick.com/help
- RapidAPI: https://rapidapi.com/scholar-sidekick-scholar-sidekick-api/api/scholar-sidekick
- API Terms: https://scholar-sidekick.com/legal/api-terms

## Sitemap

See the full [sitemap](https://scholar-sidekick.com/sitemap.md) for all pages.
