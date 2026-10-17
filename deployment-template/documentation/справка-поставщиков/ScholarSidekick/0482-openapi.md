> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ScholarSidekick: openapi

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


openapi: 3.0.3
info:
  title: Scholar Sidekick API
  version: 1.2.1
  description: |
    Resolve scholarly identifiers (DOI, PMID, PMCID, ISBN, ISSN/eISSN, arXiv, ADS bibcode, scholarly URLs)
    into normalized metadata and formatted citations. Supports export to RIS and BibTeX.

    ## Versioning & deprecation

    The API uses **header-based versioning**. Clients may pin a version with the
    optional `Api-Version` request header (see the `ApiVersion` parameter). The
    API currently serves a single version, and the active version tag is
    returned on **every** response in the `X-Scholar-Transform-Version` header
    (the verifier pipeline additionally returns `X-Scholar-Verify-Version`).

    **Deprecation policy:** when a future breaking version ships, the prior
    version is announced on its responses via the standard `Deprecation` header
    and a `Sunset` header (RFC 8594) giving the retirement date, with a minimum
    180-day overlap before removal. Deprecations are also recorded publicly at
    https://scholar-sidekick.com/changelog. This policy is also published in
    machine-readable form in the `x-api-lifecycle` extension on this document.

    ## Errors

    Errors return the typed `ErrorResponse` envelope (`{ ok: false, error, code }`)
    as `application/json` by default. The stable `code` is also mirrored in the
    `X-Error-Code` response header. Clients that send
    `Accept: application/problem+json` instead receive the same error as an
    RFC 9457 `ProblemDetails` document (`type`/`title`/`status`/`detail`/`code`).

    ## Idempotency

    The mutating POST routes (`/api/format`, `/api/format-items`, `/api/export`,
    `/api/verify`) accept an optional `Idempotency-Key` request header (see the
    `IdempotencyKey` parameter). When the server has idempotency enabled, a
    repeated request with the same key and body replays the original response
    verbatim with `Idempotent-Replayed: true`; the same key with a different body
    returns `422`. These operations are deterministic and side-effect-free, so the
    key exists purely for retry safety.

    ## Long-running work

    There is no async-job/polling pattern: the synchronous endpoints complete in a
    single request. For incremental/large batches use `POST /api/format/stream`,
    which streams newline-delimited JSON (NDJSON) events as records resolve.

    ## Pagination

    `GET /api/csl/styles` is offset-paginated (`limit`/`offset`). Each page returns
    an explicit `nextOffset` (or `null` on the last page) and, when more results
    exist, an RFC 8288 `Link: <…>; rel="next"` response header.
  termsOfService: https://scholar-sidekick.com/legal/api-terms
  contact:
    name: Scholar Sidekick
    email: support@scholar-sidekick.com
    url: https://scholar-sidekick.com
  x-logo:
    url: https://scholar-sidekick.com/icon-512.png
    altText: Scholar Sidekick
  license:
    name: Apache-2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  x-api-lifecycle:
    versioning: header
    versionHeader: Api-Version
    activeVersionHeader: X-Scholar-Transform-Version
    activeVersion: 2026-10-01
    deprecation:
      signalHeaders:
        - Deprecation
        - Sunset
      sunsetStandard: RFC 8594
      minOverlapDays: 180
    changelog: https://scholar-sidekick.com/changelog
servers:
  - url: https://scholar-sidekick.com
    description: Production
tags:
  - name: Health
    description: Service status and diagnostic endpoints.
  - name: Resolve
    description: |
      Pre-format primitives. Detect scholarly identifiers in free text, and
      resolve one identifier to normalized metadata — without running the
      formatter pipeline.
  - name: Format
    description: Resolve identifiers and format citations.
  - name: Export
    description: Export citations to manager-friendly formats.
  - name: Checks
    description: Retraction and open-access lookups for a single identifier.
  - name: Verify
    description: |
      Verify a claimed citation against its resolved record (Phase 12i).
      Detects the dominant biomedical fabrication pattern documented in
      Topaz et al. (Lancet 2026, doi:10.1016/S0140-6736(26)00603-3).
  - name: Styles
    description: Discover and browse available CSL citation styles.
security:
  - {}
  - BearerAuth: []
  - RapidApiKey: []
paths:
  /api/health:
    get:
      tags:
        - Health
      summary: Health check
      operationId: healthCheck
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
      responses:
        "200":
          description: OK
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Auth-Source:
              $ref: "#/components/headers/X-Auth-Source"
            X-Auth-Plan:
              $ref: "#/components/headers/X-Auth-Plan"
            Content-Security-Policy:
              $ref: "#/components/headers/Content-Security-Policy"
            X-Content-Type-Options:
              $ref: "#/components/headers/X-Content-Type-Options"
            X-Frame-Options:
              $ref: "#/components/headers/X-Frame-Options"
            Referrer-Policy:
              $ref: "#/components/headers/Referrer-Policy"
            Permissions-Policy:
              $ref: "#/components/headers/Permissions-Policy"
            Cross-Origin-Opener-Policy:
              $ref: "#/components/headers/Cross-Origin-Opener-Policy"
            Cross-Origin-Resource-Policy:
              $ref: "#/components/headers/Cross-Origin-Resource-Policy"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HealthResponse"
              example:
                ok: true
                time: 2026-06-04T00:00:00.000Z
                uptime_ms: 12345
                region: iad1
                version: c7f9977
        "400":
          description: Bad request
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
              examples:
                badInput:
                  value:
                    ok: false
                    code: BAD_REQUEST
                    error: Invalid input
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/detect:
    post:
      tags:
        - Resolve
      summary: Detect scholarly identifiers in free-form text
      description: |
        Pure text processing. Returns every scholarly identifier found in the
        supplied text. **No outbound network calls, no resolution, and no
        formatter pipeline** — so this route never emits `x-scholar-formatter`,
        `x-scholar-style`, or any `x-csl-*` header.

        Results are de-duplicated by `(type, value)` in detection order, and
        `value` is the canonical form of the token. **Zero identifiers is not an
        error**: `count: 0` with an empty array is a valid 200.

        `HEAD /api/detect` returns 204 with the same rails headers and an empty
        body.
      operationId: detectCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/DetectRequest"
            examples:
              mixed:
                summary: Free text carrying two identifiers
                value:
                  text: "See 10.1038/nature12373 and PMID: 23831765 for details."
      responses:
        "200":
          description: Identifiers found in the supplied text.
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Auth-Source:
              $ref: "#/components/headers/X-Auth-Source"
            X-Auth-Plan:
              $ref: "#/components/headers/X-Auth-Plan"
            X-RateLimit-Limit:
              $ref: "#/components/headers/X-RateLimit-Limit"
            X-RateLimit-Remaining:
              $ref: "#/components/headers/X-RateLimit-Remaining"
            X-RateLimit-Reset:
              $ref: "#/components/headers/X-RateLimit-Reset"
            X-RateLimit-Reset-After:
              $ref: "#/components/headers/X-RateLimit-Reset-After"
            X-RateLimit-Policy:
              $ref: "#/components/headers/X-RateLimit-Policy"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/DetectSuccessBody"
              examples:
                found:
                  summary: Two identifiers detected
                  value:
                    ok: true
                    count: 2
                    identifiers:
                      - type: doi
                        value: 10.1038/nature12373
                      - type: pmid
                        value: "23831765"
                none:
                  summary: No identifiers — still a 200
                  value:
                    ok: true
                    count: 0
                    identifiers: []
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/lookup:
    post:
      tags:
        - Resolve
      summary: Resolve a single identifier to normalized metadata
      description: |
        Resolves one identifier (DOI, PMID, PMCID, ISBN, ISSN/eISSN, arXiv, ADS
        bibcode, or a scholarly URL) and returns the normalized bibliographic
        record. **No citation is rendered** — use `/api/format` for that.

        The input is normalized before detection, so wrapped forms (a `doi.org`
        URL, a `PMID:` prefix) are accepted. Only the **first** identifier found
        is resolved; the detected type and canonical value are echoed back in
        `input`.

        A record that resolves nowhere is **not an error**: the response is 200
        with `result: null` and `reason: "not_found"`. A 400 is returned only
        when the input carries no recognizable identifier at all.

        `HEAD /api/lookup` returns 204 with the same rails headers and an empty
        body.
      operationId: lookupCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/LookupRequest"
            examples:
              doi:
                summary: Bare DOI
                value:
                  id: 10.1056/nejmoa2033700
              wrapped:
                summary: DOI as a doi.org URL
                value:
                  id: https://doi.org/10.1038/s41586-020-2649-2
              pmid:
                summary: Prefixed PMID
                value:
                  id: "PMID: 30049270"
      responses:
        "200":
          description: |
            Resolution outcome. `result` is the normalized record, or `null`
            with `reason: "not_found"` when no record was found.
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Auth-Source:
              $ref: "#/components/headers/X-Auth-Source"
            X-Auth-Plan:
              $ref: "#/components/headers/X-Auth-Plan"
            X-RateLimit-Limit:
              $ref: "#/components/headers/X-RateLimit-Limit"
            X-RateLimit-Remaining:
              $ref: "#/components/headers/X-RateLimit-Remaining"
            X-RateLimit-Reset:
              $ref: "#/components/headers/X-RateLimit-Reset"
            X-RateLimit-Reset-After:
              $ref: "#/components/headers/X-RateLimit-Reset-After"
            X-RateLimit-Policy:
              $ref: "#/components/headers/X-RateLimit-Policy"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/LookupSuccessBody"
              examples:
                resolved:
                  summary: Resolved record
                  value:
                    ok: true
                    input:
                      type: doi
                      value: 10.1056/nejmoa2033700
                    result:
                      id: doi:10.1056/nejmoa2033700
                      type: article-journal
                      title: Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine
                      authors:
                        - family: Baden
                          given: Lindsey R.
                        - family: El Sahly
                          given: Hana M.
                      container:
                        title: The New England Journal of Medicine
                        volume: "384"
                        issue: "5"
                        issn: 0028-4793
                      identifiers:
                        - type: doi
                          value: 10.1056/nejmoa2033700
                      issued:
                        year: 2021
                      pages:
                        first: "403"
                        last: "416"
                      _source:
                        service: crossref
                notFound:
                  summary: Identifier recognized, but no record resolved
                  value:
                    ok: true
                    input:
                      type: doi
                      value: 10.9999/does-not-exist
                    result: null
                    reason: not_found
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/format:
    post:
      tags:
        - Format
      summary: Resolve & format identifiers (batch, non-streaming)
      description: |
        Accepts a list of identifiers or a single free-text string. Resolves to metadata, deduplicates,
        and formats citations in the requested style. Returns JSON with text or HTML output.

        Optional enrichment via query flags:
        - `?provenance=1` — adds `_provenance` to each item (where the metadata came from)
        - `?checks=retraction,oa` (or `?checks=1`) — adds `_checks` to each item (retraction + open-access status)
      operationId: formatCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - $ref: "#/components/parameters/IdempotencyKey"
        - $ref: "#/components/parameters/ChecksFlag"
        - $ref: "#/components/parameters/ProvenanceFlag"
        - $ref: "#/components/parameters/ResolverModeFlag"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/FormatRequest"
            examples:
              linesExample:
                summary: Batch lines
                value:
                  lines:
                    - 10.1056/nejmoa2033700
##                     - "PMID: 30049270"
##                     - "ISBN: 9780192854087"
                  style: vancouver
                  output: text
              textExample:
                summary: Single text
                value:
                  text: 10.1056/nejmoa2033700
                  style: vancouver
                  output: text
      responses:
        "200":
          $ref: "#/components/responses/OkJsonWithRL"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "403":
          $ref: "#/components/responses/Forbidden"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/format-items:
    post:
      tags:
        - Format
      summary: Format pre-parsed items (batch, CSL-JSON input)
      description: |
        Accepts pre-parsed items in CSL-JSON form (e.g., results from a prior resolve step)
        and formats citations without re-resolving identifiers.

        Optional enrichment via query flags:
        - `?provenance=1` — adds `_provenance` to each item
        - `?checks=retraction,oa` (or `?checks=1`) — adds `_checks` to each item

        When either flag is set, the response also includes an `items[]` array with the slim items
        (alongside the formatted `output` string).
      operationId: formatItemsCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - $ref: "#/components/parameters/IdempotencyKey"
        - $ref: "#/components/parameters/ChecksFlag"
        - $ref: "#/components/parameters/ProvenanceFlag"
        - $ref: "#/components/parameters/ResolverModeFlag"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/FormatItemsRequest"
      responses:
        "200":
          $ref: "#/components/responses/OkJsonWithRL"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "403":
          $ref: "#/components/responses/Forbidden"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/format/stream:
    post:
      tags:
        - Format
      summary: Resolve & format identifiers (batch, NDJSON stream)
      description: |
        Streams incremental formatting output as **newline-delimited JSON**
        (`application/x-ndjson`) — one JSON event object per line. This is the
        long-running / incremental counterpart to `POST /api/format`.
        If streaming is disabled by policy, returns 403.

        Optional enrichment via query flags (echoed in headers and on the
        terminating `done` event's `itemsRaw[]`):
        - `?provenance=1` — adds `_provenance` to each item
        - `?checks=retraction,oa` (or `?checks=1`) — adds `_checks` to each item
      operationId: formatStreamCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - $ref: "#/components/parameters/ChecksFlag"
        - $ref: "#/components/parameters/ProvenanceFlag"
        - $ref: "#/components/parameters/ResolverModeFlag"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - lines
              properties:
                lines:
                  type: array
                  description: "Batch input: identifiers to resolve and format, one per element."
                  minItems: 1
                  maxItems: 500
                  items:
                    type: string
                style:
                  type: string
                  example: vancouver
      responses:
        "200":
          description: OK (SSE stream)
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Auth-Source:
              $ref: "#/components/headers/X-Auth-Source"
            X-Auth-Plan:
              $ref: "#/components/headers/X-Auth-Plan"
            X-Auth-Subject:
              $ref: "#/components/headers/X-Auth-Subject"
            X-RateLimit-Limit:
              $ref: "#/components/headers/X-RateLimit-Limit"
            X-RateLimit-Remaining:
              $ref: "#/components/headers/X-RateLimit-Remaining"
            X-RateLimit-Reset:
              $ref: "#/components/headers/X-RateLimit-Reset"
            X-RateLimit-Reset-After:
              $ref: "#/components/headers/X-RateLimit-Reset-After"
            X-RateLimit-Policy:
              $ref: "#/components/headers/X-RateLimit-Policy"
            Cache-Control:
              $ref: "#/components/headers/Cache-Control-NoStore"
            Content-Security-Policy:
              $ref: "#/components/headers/Content-Security-Policy"
            X-Content-Type-Options:
              $ref: "#/components/headers/X-Content-Type-Options"
            X-Frame-Options:
              $ref: "#/components/headers/X-Frame-Options"
            Referrer-Policy:
              $ref: "#/components/headers/Referrer-Policy"
            Permissions-Policy:
              $ref: "#/components/headers/Permissions-Policy"
            Cross-Origin-Opener-Policy:
              $ref: "#/components/headers/Cross-Origin-Opener-Policy"
            Cross-Origin-Resource-Policy:
              $ref: "#/components/headers/Cross-Origin-Resource-Policy"
          content:
            application/x-ndjson:
              schema:
                type: array
                description: |
                  Newline-delimited JSON stream: each line is one `StreamEvent`
                  object (serialized newline-delimited, NOT as a JSON array). The
                  stream begins with a `start` event and ends with a `done` event.
                items:
                  $ref: "#/components/schemas/StreamEvent"
              examples:
                ndjson:
                  summary: One JSON event object per line
                  value: |-
                    {"type":"start","idx":-1,"linesIn":1,"warnings":[]}
                    {"type":"item","idx":0,"render":"Baden LR, El Sahly HM, et al. N Engl J Med. 2021;384(5):403-416."}
                    {"type":"done","idx":-1,"output":"…","afterDedupe":1,"formatter":"builtin","styleUsed":"vancouver","lang":"en-US","footnote":false,"outputMode":"text","errors":[],"meta":{"linesIn":1,"resolved":1,"afterDedupe":1,"duplicates":0,"notFound":0,"errored":0,"skipped":0,"warned":0,"duplicateGroups":[]}}
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "403":
          description: Forbidden (read-only mode or streaming disabled)
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Scholar-Mode:
              $ref: "#/components/headers/X-Scholar-Mode"
            X-Error-Code:
              $ref: "#/components/headers/X-Error-Code"
            Content-Security-Policy:
              $ref: "#/components/headers/Content-Security-Policy"
            X-Content-Type-Options:
              $ref: "#/components/headers/X-Content-Type-Options"
            X-Frame-Options:
              $ref: "#/components/headers/X-Frame-Options"
            Referrer-Policy:
              $ref: "#/components/headers/Referrer-Policy"
            Permissions-Policy:
              $ref: "#/components/headers/Permissions-Policy"
            Cross-Origin-Opener-Policy:
              $ref: "#/components/headers/Cross-Origin-Opener-Policy"
            Cross-Origin-Resource-Policy:
              $ref: "#/components/headers/Cross-Origin-Resource-Policy"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
              examples:
                readOnly:
                  value:
                    ok: false
                    code: READ_ONLY
                    error: Read-only mode
                streamingDisabled:
                  value:
                    ok: false
                    code: STREAMING_DISABLED
                    error: Streaming disabled
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/retraction-check:
    post:
      tags:
        - Checks
      summary: Check retraction status of a single identifier
      description: |
        Resolves the supplied identifier (DOI incl. shortDOI, PMID, PMCID, arXiv ID, ADS bibcode) to a DOI
        and returns its retraction / correction / expression-of-concern status, sourced from
        Crossref `updated-by` (Retraction Watch).

        Response includes the resolved DOI, the source identifier (when different), and the
        `result` object (or `null` when no DOI could be resolved).
      operationId: retractionCheckCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CheckRequest"
            examples:
              doi:
                summary: DOI to check
                value:
                  id: 10.1056/nejmoa2033700
      responses:
        "200":
          description: Retraction status
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/RetractionCheckResponse"
              example:
                ok: true
                doi: 10.1056/nejmoa2033700
                result:
                  isRetracted: false
                  hasCorrections: false
                  hasConcern: false
                  notices: []
                  title: Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "502":
          description: |
            Upstream data source failure (Crossref 429 rate-limit, 5xx, or network error —
            transient, safe to retry). Body `code` is one of `UPSTREAM_RATE_LIMITED`,
##             `UPSTREAM_UNAVAILABLE`, `UPSTREAM_NETWORK_ERROR`, `UPSTREAM_ERROR`.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "503":
          $ref: "#/components/responses/Maintenance"
        "504":
          description: Upstream data source timed out (code `UPSTREAM_TIMEOUT` — transient, safe to retry).
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
  /api/oa-check:
    post:
      tags:
        - Checks
      summary: Check open-access status of a single identifier
      description: |
        Resolves the supplied identifier to a DOI and returns its open-access status,
        sourced from Unpaywall. Includes the best legal landing/PDF URL, OA status
        (gold/green/hybrid/bronze/closed), license, and version when available.
      operationId: oaCheckCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CheckRequest"
            examples:
              doi:
                summary: Open-access DOI
                value:
                  id: 10.1038/s41586-020-2649-2
      responses:
        "200":
          description: Open-access status
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/OaCheckResponse"
              example:
                ok: true
                doi: 10.1038/s41586-020-2649-2
                result:
                  isOa: true
                  oaStatus: hybrid
                  title: Array programming with NumPy
                  bestLocation:
                    url: https://www.nature.com/articles/s41586-020-2649-2.pdf
                    hostType: publisher
                    license: cc-by
                    version: publishedVersion
                  locations: []
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "502":
          description: |
            Upstream data source failure (Unpaywall 429 rate-limit, 5xx, or network error —
            transient, safe to retry). Body `code` is one of `UPSTREAM_RATE_LIMITED`,
##             `UPSTREAM_UNAVAILABLE`, `UPSTREAM_NETWORK_ERROR`, `UPSTREAM_ERROR`.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "503":
          $ref: "#/components/responses/Maintenance"
        "504":
          description: Upstream data source timed out (code `UPSTREAM_TIMEOUT` — transient, safe to retry).
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
  /api/export:
    post:
      tags:
        - Export
      summary: Export citations in a target format (batch)
      description: |
        Exports resolved citations as **RIS** or **BibTeX** for easy import into reference managers.
        Input may be raw identifiers (`text`) or pre-parsed items.
      operationId: exportCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - $ref: "#/components/parameters/IdempotencyKey"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ExportRequest"
            examples:
              textExample:
                summary: Single identifier
                value:
                  text: 10.1056/nejmoa2033700
                  style: vancouver
                  format: ris
              itemsExample:
                summary: Pre-parsed CSL-JSON items
                value:
                  items:
                    - title: Example title
                      type: article-journal
                  style: ama
                  format: bibtex
      responses:
        "200":
          description: |
            Exported bibliography file. The concrete `Content-Type` varies by
            `format` (e.g. `text/x-bibtex`, `application/x-research-info-systems`,
            `application/vnd.citationstyles.csl+json`, `text/csv`, `application/xml`);
            the body is the file content, delivered as an attachment.
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Scholar-Transform-Version:
              $ref: "#/components/headers/X-Scholar-Transform-Version"
            Idempotent-Replayed:
              $ref: "#/components/headers/Idempotent-Replayed"
            Content-Disposition:
              description: Attachment filename for the exported file.
              schema:
                type: string
                example: attachment; filename="citations.ris"
            X-Scholar-Batch-Lines-In:
              $ref: "#/components/headers/X-Scholar-Batch-Lines-In"
            X-Scholar-Batch-Resolved:
              $ref: "#/components/headers/X-Scholar-Batch-Resolved"
            X-Scholar-Batch-After-Dedupe:
              $ref: "#/components/headers/X-Scholar-Batch-After-Dedupe"
            X-Scholar-Batch-Duplicates:
              $ref: "#/components/headers/X-Scholar-Batch-Duplicates"
            X-Scholar-Batch-Not-Found:
              $ref: "#/components/headers/X-Scholar-Batch-Not-Found"
            X-Scholar-Batch-Errored:
              $ref: "#/components/headers/X-Scholar-Batch-Errored"
            X-Scholar-Batch-Skipped:
              $ref: "#/components/headers/X-Scholar-Batch-Skipped"
            X-Scholar-Batch-Warned:
              $ref: "#/components/headers/X-Scholar-Batch-Warned"
          content:
            text/plain:
              schema:
                type: string
                description: Exported file content (format-specific; see the response Content-Type).
              example: |-
##                 TY  - JOUR
                TI  - Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine
                AU  - Baden, Lindsey R.
                JO  - New England Journal of Medicine
##                 VL  - 384
##                 IS  - 5
##                 SP  - 403
##                 EP  - 416
##                 PY  - 2021
                DO  - 10.1056/nejmoa2033700
##                 ER  -
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
        default:
          $ref: "#/components/responses/Error"
  /api/verify:
    post:
      tags:
        - Verify
      summary: Verify a claimed citation against its resolved record
      description: |
        Takes a single *claimed* citation and returns whether the record it
        resolves to matches what the caller claimed — detecting the dominant
        AI-era fabrication pattern (a real, resolving identifier paired with a
        fabricated title).

        Verdict is one of `matched | mismatch | ambiguous | not_found`, each
        with a `confidence` tier (`high | medium | low`).
        200 OK on every produced verdict — the verdict IS the answer, not a
        failure mode. 4xx/5xx only for protocol errors: malformed JSON, a
        missing `claimed.title` (`400 MISSING_TITLE`), or resolver upstream
        failure (`502`).

        `claimed.title` is required; an identifier is optional. When an
        identifier is supplied it is resolved and compared; on a title mismatch
        (or an identifier that does not resolve) the route falls back to a
        title-search (Crossref + PubMed + OpenAlex) to tell a wrong-identifier
        citation (`ambiguous`) apart from one that resolves nowhere
        (`not_found`). With no identifier and a title too sparse to search
        safely, the verdict is `not_found` with
        `_provenance.skipped_reason: "insufficient_claim"`. Optional Stage-3 LLM
        screening of low-confidence mismatches is gated to paid / authenticated
        callers.

        Known limitations — what the verifier is weak on, and what it does NOT
        tell you (retraction and open-access status are separate signals) — are
        published at
        https://scholar-sidekick.com/citation-integrity/known-failures.md.

        Motivation: Topaz et al., *The Lancet* 2026;407(10541):1779-1781
        (doi:10.1016/S0140-6736(26)00603-3) document that the dominant
        biomedical citation-fabrication pattern is a valid identifier paired
        with a fabricated title — every resolvable case in their Supplementary
        Appendix 2 is caught by this endpoint.
      operationId: verifyCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - $ref: "#/components/parameters/IdempotencyKey"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/VerifyRequest"
            examples:
              matchedExample:
                summary: Matched citation (DOI + claimed metadata align)
                value:
                  claimed:
                    title: "Fabricated citations: an audit across 2·5 million biomedical papers"
                    authors:
                      - family: Topaz
                        given: M
                    year: 2026
                    container: The Lancet
                    doi: 10.1016/S0140-6736(26)00603-3
              mismatchExample:
                summary: Mismatch — real DOI, fabricated title
                value:
                  claimed:
                    title: Microglial Modulation via Cannabinoid Receptor 2 Alleviates Fibromyalgia-Related Central Sensitization and Pain Hypersensitivity
                    authors:
                      - family: Chen
                        given: F
                    year: 2023
                    container: Neuroscience
                    doi: 10.1016/j.neuroscience.2023.02.008
      responses:
        "200":
          description: Verification verdict produced
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            Idempotent-Replayed:
              $ref: "#/components/headers/Idempotent-Replayed"
            X-Scholar-Transform-Version:
              schema:
                type: string
                example: 2026-10-01
              description: Public, monotonically-versioned tag for normalisation + formatting logic.
            X-Scholar-Verify-Version:
              schema:
                type: string
                example: 2026-08-26
              description: |
                Public, monotonically-versioned tag for the verifier pipeline.
                Bumped when verdict semantics change.
            X-Scholar-Verify-Verdict:
              schema:
                type: string
                enum:
                  - matched
                  - mismatch
                  - not_found
                  - ambiguous
              description: Verdict surfaced for log-scraping without parsing the JSON body.
            X-Scholar-Verify-Confidence:
              schema:
                type: string
                enum:
                  - high
                  - medium
                  - low
              description: Confidence tier of the verdict.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/VerifySuccessBody"
              examples:
                matched:
                  summary: Claimed metadata matches the resolved record
                  value:
                    ok: true
                    verdict: matched
                    confidence: high
                    matched:
                      title: "Fabricated citations: an audit across 2·5 million biomedical papers"
##                       DOI: 10.1016/S0140-6736(26)00603-3
                      type: article-journal
                    mismatches: []
                    _provenance:
                      stages_run:
                        - compare
                      resolved_via: crossref
                mismatch:
                  summary: Real DOI paired with a fabricated title (the Topaz et al. pattern)
                  value:
                    ok: true
                    verdict: mismatch
                    confidence: high
                    matched:
                      title: "Fabricated citations: an audit across 2·5 million biomedical papers"
##                       DOI: 10.1016/S0140-6736(26)00603-3
                      type: article-journal
                    mismatches:
                      - field: title
                        claimed: A Novel Deep Learning Framework for Real-Time Citation Verification
                        resolved: "Fabricated citations: an audit across 2·5 million biomedical papers"
                        similarity: 0.12
                    _provenance:
                      stages_run:
                        - compare
                      resolved_via: crossref
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "413":
          description: Request body exceeds the maximum allowed size.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "502":
          description: Resolver upstream failure (transient — safe to retry).
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/audit:
    post:
      tags:
        - Verify
      summary: Audit a whole bibliography for fabrication + retraction
      description: |
        The batch counterpart to `/api/verify`. Takes a whole bibliography —
        either raw `bibliography` text (BibTeX / RIS / CSL-JSON, format
        auto-detected) or a `claims[]` array of pre-parsed references — and
        runs the same fabrication check on every entry (a real, resolving
        identifier paired with a title that does not match the resolved paper;
        Topaz et al., *The Lancet* 2026). Each resolved entry also gets a
        retraction lookup (default; pass `checks: []` to skip).

        Provide **exactly one** of `bibliography` or `claims`. Capped at 25
        entries per call — excess is dropped and reported via `truncated`.

        200 OK on every produced audit: a per-citation mismatch / not_found /
        retracted is a body field, not an HTTP error. Per-entry leniency means
        one entry that fails to resolve becomes `status: "error"` without
        failing the batch. 4xx only for protocol errors (bad content-type,
        malformed JSON, oversize body → `413`, schema violation). A total
        verification outage (every entry errored upstream) returns `502`.

        This audits citation IDENTITY at corpus scale; it does NOT check whether
        a source supports the claim it is cited for.
      operationId: auditCreate
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - $ref: "#/components/parameters/IdempotencyKey"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/AuditRequest"
            examples:
              bibliographyExample:
                summary: Raw BibTeX bibliography (mixed real + fabricated)
                value:
                  bibliography: |-
                    @article{a, title={Fabricated citations: an audit across 2.5 million biomedical papers}, doi={10.1016/S0140-6736(26)00603-3}}
                    @article{b, title={An invented title}, doi={10.1016/j.neuroscience.2023.02.008}}
              claimsExample:
                summary: Pre-parsed claims array
                value:
                  claims:
                    - title: "Fabricated citations: an audit across 2.5 million biomedical papers"
                      doi: 10.1016/S0140-6736(26)00603-3
                  options:
                    checks:
                      - retraction
      responses:
        "200":
          description: Audit produced (per-entry verdicts + corpus summary)
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            Idempotent-Replayed:
              $ref: "#/components/headers/Idempotent-Replayed"
            X-Scholar-Transform-Version:
              schema:
                type: string
                example: 2026-10-01
              description: Public, monotonically-versioned tag for normalisation + formatting logic.
            X-Scholar-Verify-Version:
              schema:
                type: string
                example: 2026-08-26
              description: Public, monotonically-versioned tag for the verifier pipeline.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AuditSuccessBody"
              examples:
                mixed:
                  summary: One matched, one fabricated (mismatch)
                  value:
                    ok: true
                    format: bibtex
                    entries:
                      - index: 1
                        status: ok
                        verdict: matched
                        confidence: high
                        matched:
                          title: "Fabricated citations: an audit across 2.5 million biomedical papers"
##                           DOI: 10.1016/S0140-6736(26)00603-3
                        mismatches: []
                        retraction:
                          checked: true
                          doi: 10.1016/S0140-6736(26)00603-3
                          isRetracted: false
                          hasCorrections: false
                          hasConcern: false
                          notices: []
                        _provenance:
                          stages_run:
                            - compare
                          resolved_via: crossref
                      - index: 2
                        status: ok
                        verdict: mismatch
                        confidence: high
                        matched:
                          title: "ChatGPT in Research: Balancing Ethics, Transparency and Advancement"
                          DOI: 10.1016/j.neuroscience.2023.02.008
                        mismatches:
                          - field: title
                            claimed: An invented title
                            resolved: "ChatGPT in Research: Balancing Ethics, Transparency and Advancement"
                            similarity: 0.08
                        retraction:
                          checked: true
                          doi: 10.1016/j.neuroscience.2023.02.008
                          isRetracted: false
                          hasCorrections: false
                          hasConcern: false
                          notices: []
                        _provenance:
                          stages_run:
                            - compare
                            - search
                          resolved_via: crossref
                    parseErrors: []
                    truncated: 0
                    summary:
                      total: 2
                      matched: 1
                      mismatch: 1
                      ambiguous: 0
                      not_found: 0
                      errored: 0
                      retracted: 0
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "413":
          description: Request body exceeds the maximum allowed size.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "502":
          description: Total verification outage (every entry errored upstream — safe to retry).
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
            application/problem+json:
              schema:
                $ref: "#/components/schemas/ProblemDetails"
        "503":
          $ref: "#/components/responses/Maintenance"
  /api/csl/styles:
    get:
      tags:
        - Styles
      summary: Discover CSL citation styles (searchable, paginated)
      description: |
        Search and browse available CSL styles — hand-tuned builtins, common
        aliases, and (when `ENABLE_CSL_IMPORTS` is on) the remote CSL registry.
        Results are **offset-paginated** via `limit` and `offset`; the response
        carries `total` (the full match count) alongside the applied
        `limit`/`offset` window.
      operationId: cslStylesList
      parameters:
        - $ref: "#/components/parameters/ApiVersion"
        - in: query
          name: q
          required: false
          description: Case-insensitive substring match against style id, title, and short title.
          schema:
            type: string
          example: chicago
        - in: query
          name: category
          required: false
          description: Filter to styles whose categories include this token.
          schema:
            type: string
          example: medicine
        - in: query
          name: bundled
          required: false
          description: When `true`, return only hand-tuned builtin styles (no aliases or remote).
          schema:
            type: boolean
        - in: query
          name: limit
          required: false
          description: Page size. Defaults to 50; clamped to 20000. Use `0` to return all matches.
          schema:
            type: integer
            minimum: 0
            maximum: 20000
            default: 50
        - in: query
          name: offset
          required: false
          description: Zero-based start offset into the matched set.
          schema:
            type: integer
            minimum: 0
            default: 0
        - in: query
          name: remote
          required: false
          description: Set to `0` to exclude remote-registry styles even when imports are enabled.
          schema:
            type: string
            enum:
              - "0"
              - "1"
        - in: query
          name: categories
          required: false
          description: Set to `1` to include available category facets in the response.
          schema:
            type: string
            enum:
              - "1"
      responses:
        "200":
          description: Paginated list of matching CSL styles.
          headers:
            X-Request-Id:
              $ref: "#/components/headers/X-Request-Id"
            X-Scholar-Transform-Version:
              $ref: "#/components/headers/X-Scholar-Transform-Version"
            Cache-Control:
              description: Public cache hint for style discovery.
              schema:
                type: string
                example: public, max-age=3600
            Link:
              description: |
                RFC 8288 link header. Present only when more results exist; carries
                the next-page URL with `rel="next"`.
              schema:
                type: string
                example: </api/csl/styles?q=chicago&offset=50&limit=50>; rel="next"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/CslStylesResponse"
              example:
                ok: true
                total: 2
                limit: 50
                offset: 0
                nextOffset: null
                importsEnabled: false
                styles:
                  - id: vancouver
                    title: Vancouver
                    categories:
                      - medicine
                      - science
                      - numeric
                    bundled: true
                    engineSupported: true
                  - id: harvard
                    title: Harvard style (uses APA formatting)
                    categories: []
                    bundled: false
                    engineSupported: true
                    aliasFor: apa
                meta:
                  bundledCount: 10
                  aliasCount: 3
                  note: Only bundled styles are available. Set ENABLE_CSL_IMPORTS=1 to enable remote styles.
        "429":
          $ref: "#/components/responses/TooManyRequests"
        "503":
          $ref: "#/components/responses/Maintenance"
        default:
          $ref: "#/components/responses/Error"
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: ssk_
      description: "First-party Scholar Sidekick API key (prefixed `ssk_`). Create one at https://scholar-sidekick.com/account and send it as `Authorization: Bearer ssk_…`. Signed-in keys get a higher rate-limit tier than anonymous access."
    RapidApiKey:
      type: apiKey
      in: header
      name: X-RapidAPI-Key
      description: RapidAPI marketplace key forwarded by RapidAPI gateway (paid/managed tiers).
  parameters:
    ChecksFlag:
      in: query
      name: checks
      required: false
      description: |
        Opt-in retraction/open-access enrichment. Comma-separated tokens or `1` for all known checks.
        Unknown tokens are silently stripped. Resolved set is echoed via the `x-scholar-checks` header.

        Tokens: `retraction`, `oa`. `1`/`true` expands to the always-available set (`retraction,oa`).
        `doaj` (DOAJ journal-indexing, ISSN-keyed) is additionally available but must be named
        explicitly — it is gated by the server flag `ENABLE_DOAJ_CHECK` and is not part of `?checks=1`.
      schema:
        type: string
        example: retraction,oa
    ProvenanceFlag:
      in: query
      name: provenance
      required: false
      description: |
        Opt-in per-item provenance manifest (`_provenance`). Set to `1`, `true`, `yes`, or `on`
        to enable the standard block; set to `full` to additionally include the large
        `full_metadata` linked-data block (funders, ORCID iDs, ROR iDs, license, trial IDs);
        set to `conflicts` to add cross-source verification (`_provenance.conflicts`), which
        also requires the `ENABLE_PROVENANCE_CONFLICTS` server flag. Modes combine, e.g.
        `full,conflicts`. Acknowledged via the `x-scholar-provenance` response header
        (`1`, `full`, `conflicts`, or a comma-joined combination).
      schema:
        type: string
        example: "1"
    ResolverModeFlag:
      in: query
      name: mode
      required: false
      description: |
        Resolver mode (Phase 12h). Only `strict` is supported — the fixed-order resolver chain
        (deterministic ordering within the currently-deployed `transform_version`; it is NOT a
        version pin or a historical snapshot — see /engineering-principles "What it does not
        promise"). `best-effort` is reserved and not yet implemented; any value other than
        `strict` resolves to `strict`, and the `x-scholar-resolver-mode` response header then
        reports `strict` (the mode that actually ran).
      schema:
        type: string
        enum:
          - strict
    ApiVersion:
      in: header
      name: Api-Version
      required: false
      description: |
        Optional API version selector (header-based versioning). The API
        currently serves a single version; the active version is returned on
        every response in `X-Scholar-Transform-Version`. Reserved for forward
        compatibility — when a future breaking version ships, clients pin to a
        version with this header and retired versions follow the deprecation
        policy described in the API overview.
      schema:
        type: string
        example: 2026-10-01
    IdempotencyKey:
      in: header
      name: Idempotency-Key
      required: false
      description: |
        Optional client-chosen key for retry-safe requests on the mutating POST
        routes. When the server has idempotency enabled, a repeated request with
        the same key and body replays the original response verbatim (with
        `Idempotent-Replayed: true`); the same key with a different body returns
        `422`. Keys are scoped per authenticated principal (or client IP when
        anonymous), so they never collide across callers. 1–255 characters of
        `[A-Za-z0-9_.:-]`.
      schema:
        type: string
        pattern: ^[A-Za-z0-9_.:-]{1,255}$
        example: ${OBJECT_ID}
  headers:
    X-Request-Id:
      description: Unique request correlation ID.
      schema:
        type: string
    X-Scholar-Checks:
      description: Echo of the resolved enrichment checks (e.g. "retraction,oa") when ?checks= is honored.
      schema:
        type: string
    X-Scholar-Provenance:
      description: Set to "1" when ?provenance=1 is honored; "full" when ?provenance=full is honored.
      schema:
        type: string
        enum:
          - "1"
          - full
    X-Scholar-Resolver-Mode:
      description: Resolver mode applied (currently always "strict"); set only when ?mode= is supplied.
      schema:
        type: string
        enum:
          - strict
    X-Auth-Source:
      description: Where the auth came from (first-party, rapidapi, anonymous).
      schema:
        type: string
        enum:
          - first-party
          - rapidapi
          - anonymous
    X-Auth-Plan:
      description: Effective plan for this request (Free/Developer/Pro/Enterprise).
      schema:
        type: string
    X-Auth-Subject:
      description: Subject/account identifier (user id, key hash, etc.).
      schema:
        type: string
    X-Error-Code:
      description: Stable internal error code.
      schema:
        type: string
    Idempotent-Replayed:
      description: |
        Set to "true" when this response was replayed from a prior request with
        the same `Idempotency-Key` (not freshly computed).
      schema:
        type: string
        enum:
          - "true"
    X-Scholar-Mode:
      description: Effective service mode (normal, read-only, maintenance).
      schema:
        type: string
        enum:
          - normal
          - read-only
          - maintenance
    X-Scholar-Transform-Version:
      description: |
        Public, monotonically-versioned tag for normalisation + formatting
        logic — returned on every response. Serves as the active API version
        under the header-based versioning scheme.
      schema:
        type: string
        example: 2026-10-01
    Deprecation:
      description: |
        Present only on responses from a deprecated API version. Signals that
        the version is deprecated (per the deprecation policy in the API
        overview); pair with `Sunset` for the retirement date.
      schema:
        type: string
    Sunset:
      description: |
        Present only on deprecated API versions. RFC 8594 HTTP-date after which
        the version is retired (minimum 180 days after the `Deprecation` notice).
      schema:
        type: string
    X-Scholar-Batch-Lines-In:
      description: Number of input lines received by the export batch.
      schema:
        type: string
    X-Scholar-Batch-Resolved:
      description: Number of input lines that resolved to a record.
      schema:
        type: string
    X-Scholar-Batch-After-Dedupe:
      description: Number of items actually serialized into the exported file (after dedupe).
      schema:
        type: string
    X-Scholar-Batch-Duplicates:
      description: Number of resolved rows dropped by dedupe (resolved - after-dedupe).
      schema:
        type: string
    X-Scholar-Batch-Not-Found:
      description: Number of input lines with no matching record.
      schema:
        type: string
    X-Scholar-Batch-Errored:
      description: Number of input lines that failed for a non-not-found reason.
      schema:
        type: string
    X-Scholar-Batch-Skipped:
      description: Number of input lines skipped before resolution (e.g. ISSN-only lines).
      schema:
        type: string
    X-Scholar-Batch-Warned:
      description: Number of warnings emitted via the response warning headers.
      schema:
        type: string
    X-RateLimit-Limit:
      description: Maximum requests allowed in the current window.
      schema:
        type: integer
        minimum: 0
    X-RateLimit-Remaining:
      description: Requests remaining in the current window.
      schema:
        type: integer
        minimum: 0
    X-RateLimit-Reset:
      description: UTC epoch seconds when the window resets.
      schema:
        type: integer
        minimum: 0
    X-RateLimit-Reset-After:
      description: Seconds until reset.
      schema:
        type: integer
        minimum: 0
    X-RateLimit-Policy:
      description: Policy string (e.g., "60;w=60, 1000;w=3600").
      schema:
        type: string
    Cache-Control-NoStore:
      description: Instructs clients not to cache.
      schema:
        type: string
        enum:
          - no-store
    Content-Security-Policy:
      description: CSP controlling resource loading.
      schema:
        type: string
    X-Content-Type-Options:
      description: MIME type sniffing prevention.
      schema:
        type: string
        enum:
          - nosniff
    X-Frame-Options:
      description: Clickjacking protection.
      schema:
        type: string
        enum:
##           - DENY
##           - SAMEORIGIN
    Referrer-Policy:
      description: Referrer information policy.
      schema:
        type: string
        enum:
          - no-referrer
          - no-referrer-when-downgrade
          - origin
          - origin-when-cross-origin
          - same-origin
          - strict-origin
          - strict-origin-when-cross-origin
          - unsafe-url
    Permissions-Policy:
      description: Feature policy controls.
      schema:
        type: string
    Cross-Origin-Opener-Policy:
      description: Cross-origin opener policy.
      schema:
        type: string
        enum:
          - same-origin
          - same-origin-allow-popups
          - unsafe-none
    Cross-Origin-Resource-Policy:
      description: Cross-origin resource policy.
      schema:
        type: string
        enum:
          - same-origin
          - same-site
          - cross-origin
  schemas:
    ErrorResponse:
      type: object
      additionalProperties: false
      required:
        - ok
        - code
        - error
      description: |
        Typed error envelope returned on 4xx/5xx protocol errors. `error` is a
        human-readable message. `code` is a stable, machine-readable token,
        always present on error responses and mirrored in the `X-Error-Code`
        response header. Known codes: BAD_REQUEST, VALIDATION_ERROR,
##         UNKNOWN_STYLE, INVALID_CONTENT_TYPE, EMPTY_BODY, MALFORMED_JSON,
##         PAYLOAD_TOO_LARGE, MISSING_TITLE, RESOLVE_ERROR, READ_ONLY,
##         STREAMING_DISABLED, AUTH_MISSING, AUTH_INVALID, AUTH_DISABLED,
##         LLM_SCREEN_FORBIDDEN, IDEMPOTENCY_KEY_REUSED, NOT_FOUND, RL_BLOCKED,
##         MAINTENANCE, UPSTREAM_ERROR, UPSTREAM_TIMEOUT, UPSTREAM_RATE_LIMITED,
##         UPSTREAM_UNAVAILABLE, UPSTREAM_NETWORK_ERROR, ROUTE_ERROR. RL_BLOCKED
        (429) is the code actually returned when the per-IP rate limit is
        exceeded — not a generic RATE_LIMITED token.
      properties:
        ok:
          type: boolean
          enum:
            - false
        error:
          type: string
          description: Human-readable error message.
        code:
          type: string
          description: Stable machine-readable error code (mirrors X-Error-Code).
      example:
        ok: false
        code: BAD_REQUEST
        error: Invalid input
    ProblemDetails:
      type: object
      description: |
        RFC 9457 (Problem Details for HTTP APIs) representation of an error.
        Served on any error response when the request sends
        `Accept: application/problem+json`; otherwise the default `ErrorResponse`
        envelope is returned. The stable `code` is preserved as an extension
        member and mirrored in the `X-Error-Code` header.
      required:
        - type
        - title
        - status
        - code
      properties:
        type:
          type: string
          format: uri
          description: A URI identifying the problem type (per stable error code).
          example: https://scholar-sidekick.com/errors/VALIDATION_ERROR
        title:
          type: string
          description: Short, human-readable summary of the problem type.
          example: Validation Error
        status:
          type: integer
          description: HTTP status code (duplicated from the response line).
          example: 400
        detail:
          type: string
          description: Human-readable explanation specific to this occurrence.
          example: Missing 'lines' (array) or 'text' (string) in body.
        instance:
          type: string
          description: Optional request correlation id (mirrors X-Request-Id).
        code:
          type: string
          description: Stable machine-readable error code (extension member; mirrors X-Error-Code).
          example: VALIDATION_ERROR
      example:
        type: https://scholar-sidekick.com/errors/VALIDATION_ERROR
        title: Validation Error
        status: 400
        detail: Missing 'lines' (array) or 'text' (string) in body.
        code: VALIDATION_ERROR
    StreamEvent:
      type: object
      description: |
        A single newline-delimited JSON event from `POST /api/format/stream`.
        `type` discriminates the event; `idx` is the 0-based item index (or `-1`
        for stream-level events). The stream opens with `start` and ends with `done`.
      required:
        - type
        - idx
      properties:
        type:
          type: string
          enum:
            - start
            - item
            - error
            - skip-duplicate
            - warning
            - done
        idx:
          type: integer
          description: Item index, or -1 for stream-level events.
        render:
          type: string
          description: Rendered citation (builtin formatter `item` events).
        message:
          type: string
          description: Human-readable text (`error` / `warning` events).
        code:
          type: string
          description: Stable error code (`error` events).
        output:
          type: string
          description: Full rendered output (terminal `done` event).
        formatter:
          type: string
          enum:
            - builtin
            - csl
        styleUsed:
          type: string
        afterDedupe:
          type: integer
        meta:
          allOf:
            - $ref: "#/components/schemas/BatchSummary"
          description: Batch summary on the terminal `done` event (same shape as /api/format `meta`).
    HealthResponse:
      type: object
      description: Service liveness and diagnostic snapshot.
      required:
        - ok
        - time
        - uptime_ms
        - version
      properties:
        ok:
          type: boolean
          enum:
            - true
        time:
          type: string
          format: date-time
        now:
          type: string
          format: date-time
        uptime_ms:
          type: integer
          minimum: 0
        region:
          type: string
        version:
          type: string
        commit:
          type: string
          nullable: true
        sentry_env:
          type: string
          nullable: true
        kv_namespace:
          type: string
          nullable: true
        ua_ok:
          type: boolean
        cache_conf:
          type: object
          properties:
            version:
              type: string
            ttl_s:
              type: integer
            negative_ttl_s:
              type: integer
            kv_enabled:
              type: boolean
        limits:
          type: object
          description: "Per-route-family rate-limit ceiling for anonymous callers, as actually enforced by the rate-limit middleware (derived from the same policy pipeline, not a static default). Keys are route families: format, format_stream, export, format_items, audit, fallback. Windows differ per family, so each entry carries its own window_s."
          additionalProperties:
            type: object
            required:
              - limit
              - window_s
            properties:
              limit:
                type: integer
                minimum: 1
              window_s:
                type: integer
                minimum: 1
    CslStyle:
      type: object
      description: A single CSL style entry returned by style discovery.
      required:
        - id
        - title
        - bundled
      properties:
        id:
          type: string
          example: vancouver
        title:
          type: string
          example: Vancouver
        titleShort:
          type: string
          example: APA
        categories:
          type: array
          items:
            type: string
          example:
            - medicine
            - numeric
        bundled:
          type: boolean
          description: True for hand-tuned builtin styles shipped with the API.
        engineSupported:
          type: boolean
          description: True when the CSL engine can render the style directly.
        aliasFor:
          type: string
          description: Present on alias entries — the style this alias resolves to.
          example: apa
    CslStylesResponse:
      type: object
      description: |
        Paginated CSL style discovery result. Pagination is offset-based:
        `total` is the full match count; `limit`/`offset` echo the applied
        window (`limit: 0` returns all matches).
      required:
        - ok
        - styles
        - total
        - limit
        - offset
      properties:
        ok:
          type: boolean
          enum:
            - true
        styles:
          type: array
          items:
            $ref: "#/components/schemas/CslStyle"
        total:
          type: integer
          minimum: 0
          description: Total number of styles matching the query, before pagination.
        limit:
          type: integer
          minimum: 0
          description: Applied page size (0 means "all matches", no windowing).
        offset:
          type: integer
          minimum: 0
          description: Applied start offset into the matched set.
        nextOffset:
          description: |
            Explicit continuation token — the `offset` to request for the next
            page, or `null` on the last page (or when `limit: 0` returned all
            matches). When non-null, an RFC 8288 `Link: <…>; rel="next"` response
            header carries the same next-page URL.
          type: integer
          minimum: 0
          nullable: true
        importsEnabled:
          type: boolean
          description: Whether remote CSL imports are enabled for this deployment.
        categories:
          type: object
          description: Present only when `?categories=1`. Available category facets.
          properties:
            all:
              type: array
              items:
                type: string
            bundled:
              type: array
              items:
                type: string
            remote:
              type: array
              items:
                type: string
        meta:
          type: object
          properties:
            bundledCount:
              type: integer
              minimum: 0
            aliasCount:
              type: integer
              minimum: 0
            note:
              type: string
    RenderStyle:
      type: string
      maxLength: 64
      description: Citation style id — a builtin name or a CSL style id.
    RenderLang:
      type: string
      maxLength: 16
      default: en-US
      description: BCP-47 locale for the rendered citation.
    RenderLocale:
      type: string
      maxLength: 16
      description: Accepted alias for `lang`. When both are sent, `lang` wins.
    RenderFootnote:
      type: boolean
      default: false
      description: |
        Render note form instead of a bibliography entry.

        ⚠️ **Honoured only when the request resolves to the CSL engine**
        (`formatter: "csl"` — an alias, dependent or resolved style). The five
        builtin styles (`vancouver`/`ama`/`apa`/`ieee`/`cse`) have no note form,
        so the flag is **silently downgraded** and the response echoes
        `footnote: false`. The downgrade is reported honestly in the body but
        raises no warning header.
    RenderOutput:
      type: string
      enum:
        - text
        - html
        - json
      default: text
      description: |
        Output mode.

        ⚠️ `html` is **CSL path only**, on the same rule as `footnote`: on a
        builtin style the response reports `outputMode: "text"`. Note that both
        `text` and `html` are populated in the response regardless of
        `outputMode`, so builtin callers still get an HTML rendering.
    NoCacheFlag:
      type: boolean
      default: false
      description: Bypass the resolver cache for this request.
    FormatRequest:
      description: |
        Batch-capable. Provide either `text` (free text containing one or more
        identifiers, one per line) or `lines` (an array of identifiers); both
        resolve and format every identifier in a single call. Bounded by a
        128 KB request body and a maximum of 500 identifiers per request.
      oneOf:
        - type: object
          additionalProperties: false
          required:
            - text
          properties:
            text:
              type: string
              description: Free text with one or more identifiers, one per line (batch input).
            style:
              $ref: "#/components/schemas/RenderStyle"
            lang:
              $ref: "#/components/schemas/RenderLang"
            locale:
              $ref: "#/components/schemas/RenderLocale"
            footnote:
              $ref: "#/components/schemas/RenderFootnote"
            output:
              $ref: "#/components/schemas/RenderOutput"
            nocache:
              $ref: "#/components/schemas/NoCacheFlag"
        - type: object
          additionalProperties: false
          required:
            - lines
          properties:
            lines:
              type: array
              description: "Batch input: identifiers to resolve and format, one per element."
              minItems: 1
              maxItems: 500
              items:
                type: string
            style:
              $ref: "#/components/schemas/RenderStyle"
            lang:
              $ref: "#/components/schemas/RenderLang"
            locale:
              $ref: "#/components/schemas/RenderLocale"
            footnote:
              $ref: "#/components/schemas/RenderFootnote"
            output:
              $ref: "#/components/schemas/RenderOutput"
            nocache:
              $ref: "#/components/schemas/NoCacheFlag"
    FormatItemsRequest:
      type: object
      additionalProperties: false
      required:
        - items
      description: |
        Batch-capable: formats up to 500 pre-parsed CSL-JSON items in one call.
      properties:
        items:
          type: array
          description: "Batch input: pre-parsed CSL-JSON items, one per element."
          minItems: 1
          maxItems: 500
          items:
            type: object
            description: CSL-JSON item
        style:
          $ref: "#/components/schemas/RenderStyle"
        lang:
          $ref: "#/components/schemas/RenderLang"
        locale:
          $ref: "#/components/schemas/RenderLocale"
        footnote:
          $ref: "#/components/schemas/RenderFootnote"
        output:
          $ref: "#/components/schemas/RenderOutput"
        nocache:
          $ref: "#/components/schemas/NoCacheFlag"
    ExportRequest:
      description: |
        Batch-capable. Provide `text` (one or more identifiers, one per line) or
        `items` (pre-parsed CSL-JSON); exports all entries into a single file.
        Bounded by a 128 KB request body and a maximum of 500 items per request.
      oneOf:
        - type: object
          additionalProperties: false
          required:
            - text
            - format
          properties:
            text:
              type: string
              description: Free text with one or more identifiers, one per line (batch input).
            style:
              $ref: "#/components/schemas/RenderStyle"
            lang:
              $ref: "#/components/schemas/RenderLang"
            locale:
              $ref: "#/components/schemas/RenderLocale"
            footnote:
              $ref: "#/components/schemas/RenderFootnote"
            output:
              $ref: "#/components/schemas/RenderOutput"
            nocache:
              $ref: "#/components/schemas/NoCacheFlag"
            format:
              type: string
              description: |
                Export format. The route additionally accepts the internal
                spellings `bib`, `csl`, `medline` and `zotero-rdf`; the names
                published here are the ecosystem-standard equivalents.
              enum:
                - txt
                - ris
                - bibtex
                - csl-json
                - endnote-xml
                - endnote-refer
                - refworks
                - nbib
                - rdf
                - csv
        - type: object
          additionalProperties: false
          required:
            - items
            - format
          properties:
            items:
              type: array
              description: "Batch input: pre-parsed CSL-JSON items to export, one per element."
              minItems: 1
              maxItems: 500
              items:
                type: object
                description: CSL-JSON item
            style:
              $ref: "#/components/schemas/RenderStyle"
            lang:
              $ref: "#/components/schemas/RenderLang"
            locale:
              $ref: "#/components/schemas/RenderLocale"
            footnote:
              $ref: "#/components/schemas/RenderFootnote"
            output:
              $ref: "#/components/schemas/RenderOutput"
            nocache:
              $ref: "#/components/schemas/NoCacheFlag"
            format:
              type: string
              enum:
                - txt
                - ris
                - bibtex
                - csl-json
                - endnote-xml
                - endnote-refer
                - refworks
                - nbib
                - rdf
                - csv
    VerifyAuthor:
      type: object
      additionalProperties: false
      required:
        - family
      properties:
        family:
          type: string
          minLength: 1
          maxLength: 200
        given:
          type: string
          maxLength: 200
    VerifyClaim:
      type: object
      additionalProperties: false
      description: |
        Caller-supplied citation under verification. `title` is required (a
        missing title returns `400 MISSING_TITLE`). An identifier is optional;
        with none, the verifier title-searches when the title is specific
        enough, otherwise returns `not_found` with
        `_provenance.skipped_reason: "insufficient_claim"`.
      properties:
        title:
          type: string
          minLength: 1
          maxLength: 2000
        authors:
          type: array
          maxItems: 50
          items:
            $ref: "#/components/schemas/VerifyAuthor"
        year:
          type: integer
          minimum: 0
          maximum: 9999
        container:
          type: string
          maxLength: 500
        doi:
          type: string
          maxLength: 200
        pmid:
          type: string
          maxLength: 50
        pmcid:
          type: string
          maxLength: 50
        isbn:
          type: string
          maxLength: 50
        arxiv:
          type: string
          maxLength: 50
        issn:
          type: string
          maxLength: 50
        ads:
          type: string
          maxLength: 50
        whoIrisUrl:
          type: string
          maxLength: 2000
    VerifyRequest:
      type: object
      additionalProperties: false
      required:
        - claimed
      properties:
        claimed:
          $ref: "#/components/schemas/VerifyClaim"
        options:
          type: object
          additionalProperties: false
          properties:
            bypassCache:
              type: boolean
            screen_with_llm:
              type: boolean
              description: |
                Opt-in Stage 3 LLM screen (Phase 12i.3). Fires only when the
                pre-LLM verdict is `mismatch` with `confidence: low` (the
                informal-abbreviation false-positive bucket). Gated:
                authenticated first-party callers and paid RapidAPI tiers
                only. Anonymous / free callers receive `400
                LLM_SCREEN_FORBIDDEN`. Per-day budget cap is configurable
                via `LLM_VERIFY_DAILY_BUDGET_USD` (default $5/day); when
                exceeded the request still returns its non-LLM verdict
                with `_provenance.llm_screen.reason = daily_budget_exceeded`.
    VerifyMismatch:
      type: object
      additionalProperties: false
      required:
        - field
        - similarity
      properties:
        field:
          type: string
          enum:
            - title
            - first_author
            - year
            - container
            - coauthor
          description: |
            Which field disagreed. `coauthor` rows are emitted only when the
            co-author cross-check is enabled server-side, one row per claimed
            co-author that matched no author on the resolved record; unlike the
            other fields they never drive a `mismatch` — they downgrade
            `matched` to `ambiguous` (review).
        claimed:
          oneOf:
            - type: string
            - type: number
        resolved:
          oneOf:
            - type: string
            - type: number
        similarity:
          type: number
          minimum: 0
          maximum: 1
    VerifyCandidate:
      type: object
      additionalProperties: false
      required:
        - item
        - registries
        - score
      description: |
        A title-search alternative surfaced when the verifier cannot confirm
        the supplied identifier matches the claimed metadata. Present on
        verdicts `matched` (no-identifier path), `ambiguous`, `mismatch`
        (post-12i.2), and `not_found` (post-12i.2).
      properties:
        item:
          type: object
          description: BiblioItem matching the claim's title via search.
        registries:
          type: array
          items:
            type: string
            enum:
              - crossref
              - pubmed
              - openalex
        score:
          type: number
          minimum: 0
          maximum: 1
          description: Title similarity (0-1) against the claim.
    RegistrySearchStatus:
      type: object
      additionalProperties: false
      required:
        - registry
        - ok
        - count
      properties:
        registry:
          type: string
          enum:
            - crossref
            - pubmed
            - openalex
        ok:
          type: boolean
        count:
          type: integer
          minimum: 0
        reason:
          type: string
          description: |
            Failure reason (e.g., `upstream_error`, `invalid_input`) when
            the registry adapter did not return results.
    LlmScreenProvenance:
      type: object
      additionalProperties: false
      required:
        - applied
      description: |
        LLM screen telemetry (Phase 12i.3). Emitted on the response
        envelope whenever the caller passed `options.screen_with_llm:
        true`. `applied: true` means a model call ran and produced a
        structured verdict; `applied: false` carries a `reason` field
        explaining why the screen was skipped.
      properties:
        applied:
          type: boolean
        model:
          type: string
          description: Model slug used for the screen (e.g., `anthropic/claude-haiku-4.5`).
        prompt_version:
          type: string
          description: Prompt revision identifier — bumped with `SCHOLAR_VERIFY_VERSION`.
        verdict:
          type: string
          enum:
            - informal_abbreviation
            - different_paper
            - uncertain
          description: |
            LLM classification. `informal_abbreviation` upgrades the
            verdict to `matched / low`; `different_paper` keeps `mismatch`
            and raises confidence to `high`; `uncertain` leaves the
            pre-LLM verdict unchanged.
        reasoning:
          type: string
          description: Justification (≤2000 chars) emitted alongside the verdict.
        cost_usd:
          type: number
          minimum: 0
          description: |
            Approximate USD cost of the model call, computed from token
            usage and published list prices. Used by the daily-budget
            guard at `LLM_VERIFY_DAILY_BUDGET_USD`.
        reason:
          type: string
          enum:
            - verdict_not_eligible
            - daily_budget_exceeded
            - no_gateway
            - upstream_error
            - malformed_response
          description: |
            Set when `applied: false`. `verdict_not_eligible` means the
            pre-LLM verdict was not `mismatch / low` so no model call was
            attempted.
    VerifyProvenance:
      type: object
      additionalProperties: false
      required:
        - stages_run
        - resolved_via
      properties:
        stages_run:
          type: array
          items:
            type: string
            enum:
              - compare
              - search
              - llm_screen
              - containment
        resolved_via:
          description: Identifier of the resolver-source service (e.g., `crossref`, `pubmed`).
          type: string
          nullable: true
        method:
          type: string
          enum:
            - compare
            - containment
          description: |
            Which verdict method produced this entry. Absent (or `compare`) is the
            default single-citation path: a clean claimed title compared to the
            resolved title via full-string similarity. `containment` is the
            prose-reference path (`/api/audit` `references[]` input, e.g. a `.docx`
            upload): no clean title is available, so the resolved title is checked
            for token-containment within the raw reference text.
        containment:
          type: object
          additionalProperties: false
          required:
            - score
            - matched_tokens
            - total_tokens
          description: Containment scoring detail — present only on containment-method entries.
          properties:
            score:
              type: number
              description: Fraction (0-1) of the resolved title's significant tokens found in the reference text.
            matched_tokens:
              type: integer
            total_tokens:
              type: integer
            corroboration:
              type: string
              enum:
                - corroborated
                - refuted
                - partial
                - unavailable
              description: |
                Author+year second signal, used to disambiguate a LOW title score —
                a translated or reworded genuine citation and a fabricated title
                both score near zero on title tokens alone, but author surnames
                and the year are language-invariant.
                - `corroborated`: the resolved record's author AND year appear in
                  the reference, so the citation points at this work however the
                  title was written. The entry is rescued to `ambiguous` (review)
                  and never flagged as a fabrication; a caveat explains why.
                - `refuted`: the record has a usable surname and a year and
                  NEITHER appears, so two independent signals agree — a wider
                  mismatch cutoff applies.
                - `partial`: exactly one of the two appears. That is not
                  disagreement — a genuine citation that omits the year, or
                  romanises an author differently ("Mueller" vs "Müller"), trips
                  this — so the conservative cutoff applies.
                - `unavailable`: the record carries no usable surname or no year,
                  so there is nothing to corroborate with; the conservative
                  near-zero-overlap cutoff applies.
        v1_limitations:
          type: array
          deprecated: true
          items:
            type: string
          description: |
            Deprecated since 12i.2 and never emitted by the current route.
            Pre-12i.2 the verifier emitted `no_identifier_provided_in_v1` here
            when the claim lacked an identifier; the active title-search path
            replaced that case. Superseded by `caveats`.
        caveats:
          type: array
          items:
            type: string
          description: |
            Point-of-use limitations of this verdict (SPEC §10). Each string is
            emitted only when deterministically TRUE of the comparison — e.g.
            `"resolved via title-search; the supplied identifier did not
            resolve"`, `"container-only identifier (ISSN); verifies the journal,
            not a specific work"`, `"title is non-Latin script; character-level
            similarity is weaker here"`, `"verdict reflects a publication-year
            gap"`, `"group author could not be cross-checked against the
            record"`, `"a claimed co-author could not be found on the resolved
            record"`, `"identifier resolution failed upstream (registry outage
            or refusal), so the missing record may reflect that failure rather
            than a fabricated identifier"`, `"no record found in the scholarly
            registries searched; sources outside them (standards, software
            repositories, model cards, institutional reports) are not indexed
            here"`. Absent (not an empty array) on a clean high-confidence
            `matched`.
        skipped_reason:
          type: string
          enum:
            - insufficient_claim
            - container_only
            - no_identifier
            - sparse_resolved_title
          description: |
            Present when the verifier short-circuited before searching. Verdict is
            `not_found` in these cases; absent on normal verdicts.
            - `insufficient_claim`: the claim carried no identifier and a title too
              sparse to title-search safely (e.g. a single token).
            - `container_only`: the identifier resolved to a journal/container
              (e.g. an ISSN), not a work — there is no paper to verify (Phase 12j).
            - `no_identifier`: (containment path) the reference text carried no
              detectable identifier, so there was nothing to resolve against.
            - `sparse_resolved_title`: (containment path) the identifier resolved,
              but the record's title is too short to score containment safely.
        registries_searched:
          type: array
          description: |
            Per-registry status block surfaced when the title-search
            aggregator ran. Absent on the compare-only fast path.
          items:
            $ref: "#/components/schemas/RegistrySearchStatus"
        llm_screen:
          $ref: "#/components/schemas/LlmScreenProvenance"
    VerifySuccessBody:
      type: object
      additionalProperties: false
      required:
        - ok
        - verdict
        - confidence
        - matched
        - mismatches
        - _provenance
      properties:
        ok:
          type: boolean
          enum:
            - true
        verdict:
          type: string
          enum:
            - matched
            - mismatch
            - not_found
            - ambiguous
        confidence:
          type: string
          enum:
            - high
            - medium
            - low
        matched:
          description: |
            Best record the verifier matched the claim to (resolver record
            on the identifier path, or top search candidate on the no-id
            path). `null` when nothing meaningful matched.
          type: object
          nullable: true
        mismatches:
          type: array
          items:
            $ref: "#/components/schemas/VerifyMismatch"
        candidates:
          type: array
          description: |
            Title-search alternatives, ranked by similarity (best first).
            Present whenever the search stage ran; absent on the compare-only
            fast path.
          items:
            $ref: "#/components/schemas/VerifyCandidate"
        _provenance:
          $ref: "#/components/schemas/VerifyProvenance"
    AuditClaim:
      type: object
      additionalProperties: false
      required:
        - title
      description: A single pre-parsed citation for the `claims[]` path. `title` is required.
      properties:
        title:
          type: string
          minLength: 1
          maxLength: 2000
        authors:
          type: array
          maxItems: 50
          items:
            $ref: "#/components/schemas/VerifyAuthor"
        year:
          type: integer
          minimum: 0
          maximum: 9999
        container:
          type: string
          maxLength: 500
        doi:
          type: string
          maxLength: 200
        pmid:
          type: string
          maxLength: 50
        pmcid:
          type: string
          maxLength: 50
        isbn:
          type: string
          maxLength: 50
        arxiv:
          type: string
          maxLength: 50
        issn:
          type: string
          maxLength: 50
        ads:
          type: string
          maxLength: 50
        whoIrisUrl:
          type: string
          maxLength: 2000
    AuditRequest:
      type: object
      additionalProperties: false
      description: |
        Provide EXACTLY ONE of `bibliography` (raw text), `claims` (array), or
        `references` (array of raw reference strings).
      properties:
        bibliography:
          type: string
          maxLength: 131072
          description: Raw BibTeX / RIS / CSL-JSON text. Format is auto-detected unless `format` is set.
        format:
          type: string
          enum:
            - bibtex
            - ris
            - csl-json
          description: Override format auto-detection for `bibliography`.
        claims:
          type: array
          maxItems: 25
          items:
            $ref: "#/components/schemas/AuditClaim"
        references:
          type: array
          maxItems: 25
          items:
            type: string
            minLength: 1
            maxLength: 5000
          description: |
            Raw prose reference paragraphs (e.g. extracted from a `.docx`
            manuscript). Each is verified via the CONTAINMENT method: its
            identifier is resolved and the resolved title is checked for
            token-containment in the reference text (no clean claimed title is
            parsed). Response entries carry `_provenance.method: "containment"`;
            the `x-scholar-containment-version` header pins the method version.
        options:
          type: object
          additionalProperties: false
          properties:
            bypassCache:
              type: boolean
            screen_with_llm:
              type: boolean
              description: Opt-in Stage 3 LLM screen per entry (same gating as /api/verify). Default false.
            checks:
              type: array
              items:
                type: string
                enum:
                  - retraction
              description: "Per-entry enrichment checks. Default: [retraction]. Pass [] to skip."
    AuditRetraction:
      type: object
      additionalProperties: false
      description: |
        Per-entry retraction status. `checked` is false when retraction was not
        requested, the entry had no resolvable DOI, or an upstream error was
        swallowed. `null` when `checks` did not include `retraction`.
      required:
        - checked
        - doi
        - isRetracted
        - hasCorrections
        - hasConcern
        - notices
      properties:
        checked:
          type: boolean
        doi:
          type: string
          nullable: true
        isRetracted:
          type: boolean
        hasCorrections:
          type: boolean
        hasConcern:
          type: boolean
        notices:
          type: array
          items:
            $ref: "#/components/schemas/RetractionNotice"
    AuditEntry:
      type: object
      description: |
        One result per verifiable entry. `status: "ok"` carries a verdict;
        `status: "error"` marks a per-entry upstream failure (the batch is not
        failed by one bad entry).
      required:
        - index
        - status
      properties:
        index:
          type: integer
          description: 1-based position in the input batch.
        sourceKey:
          type: string
          description: BibTeX key / RIS record index / CSL-JSON id, when present.
        status:
          type: string
          enum:
            - ok
            - error
        error:
          type: string
          description: Present only on status=error.
        verdict:
          type: string
          enum:
            - matched
            - mismatch
            - not_found
            - ambiguous
        confidence:
          type: string
          enum:
            - high
            - medium
            - low
        matched:
          type: object
          description: Resolver-returned BiblioItem.
          nullable: true
        mismatches:
          type: array
          items:
            $ref: "#/components/schemas/VerifyMismatch"
        candidates:
          type: array
          items:
            $ref: "#/components/schemas/VerifyCandidate"
        retraction:
          $ref: "#/components/schemas/AuditRetraction"
        _provenance:
          $ref: "#/components/schemas/VerifyProvenance"
    AuditParseError:
      type: object
      additionalProperties: false
      required:
        - index
        - error
        - message
      properties:
        index:
          type: integer
        error:
          type: string
          description: e.g. "missing_title", "invalid_syntax", "empty_entry", "unsupported_type".
        message:
          type: string
    AuditSummary:
      type: object
      additionalProperties: false
      required:
        - total
        - matched
        - mismatch
        - ambiguous
        - not_found
        - errored
        - retracted
      description: Corpus roll-up (a pure function of `entries`).
      properties:
        total:
          type: integer
        matched:
          type: integer
        mismatch:
          type: integer
        ambiguous:
          type: integer
        not_found:
          type: integer
        errored:
          type: integer
        retracted:
          type: integer
    AuditSuccessBody:
      type: object
      additionalProperties: false
      required:
        - ok
        - format
        - entries
        - parseErrors
        - truncated
        - summary
      properties:
        ok:
          type: boolean
          enum:
            - true
        format:
          type: string
          enum:
            - bibtex
            - ris
            - csl-json
            - null
          description: Detected input format, or null for the claims[] path.
          nullable: true
        entries:
          type: array
          items:
            $ref: "#/components/schemas/AuditEntry"
        parseErrors:
          type: array
          items:
            $ref: "#/components/schemas/AuditParseError"
        truncated:
          type: integer
          description: Entries dropped beyond the 25-entry cap.
        summary:
          $ref: "#/components/schemas/AuditSummary"
    StringOrInteger:
      oneOf:
        - type: string
        - type: integer
    StringOrNumber:
      oneOf:
        - type: string
        - type: number
    DetectRequest:
      type: object
      additionalProperties: false
      required:
        - text
      properties:
        text:
          type: string
          minLength: 1
          maxLength: 10000
          description: |
            Free-form text to scan. Trimmed before processing, and the 10,000
            character cap is applied to the trimmed value.
    DetectedIdentifier:
      type: object
      additionalProperties: false
      required:
        - type
        - value
      description: |
        One detected identifier. `raw` and `source` are present only when the
        detector kept the original token or recorded which pass matched — do
        not depend on either being set.
      properties:
        type:
          type: string
          enum:
            - doi
            - pmid
            - pmcid
            - isbn
            - arxiv
            - issn
            - eissn
            - ads
            - url
          description: |
            `url` is emitted for a recognized scholarly host that is not
            already covered by a more specific identifier.
        value:
          type: string
          description: Canonical form of the identifier.
        raw:
          type: string
          description: Original token, when it differs from `value`.
        source:
          type: string
          description: Detector pass that matched, e.g. `detect:url`.
    DetectSuccessBody:
      type: object
      additionalProperties: false
      required:
        - ok
        - count
        - identifiers
      properties:
        ok:
          type: boolean
          enum:
            - true
        count:
          type: integer
          minimum: 0
          description: Length of `identifiers`.
        identifiers:
          type: array
          description: De-duplicated by `(type, value)`, in detection order.
          items:
            $ref: "#/components/schemas/DetectedIdentifier"
    LookupRequest:
      type: object
      additionalProperties: false
      required:
        - id
      properties:
        id:
          type: string
          minLength: 1
          maxLength: 500
          description: |
            One identifier — DOI, PMID, PMCID, ISBN, ISSN/eISSN, arXiv, ADS
            bibcode, or a scholarly URL. Wrapped forms (a `doi.org` URL, a
            `PMID:` prefix) are normalized before detection. A shortDOI alias
            (`10/aabbe`, from shortdoi.org) is accepted anywhere a DOI is and is
            expanded to the full DOI before resolving, so the response carries
            the real DOI. Only the first identifier found is resolved.
    SlimItem:
      type: object
      additionalProperties: true
      description: |
        Compact, response-safe view of a resolved bibliographic record — the
        same slim shape the format routes build their items from. Every field
        except `id` is optional, because a record carries only what its source
        supplied.
      required:
        - id
      properties:
        id:
          type: string
          description: Stable item key derived from the identifiers.
        type:
          type: string
          description: CSL item type (e.g. `article-journal`, `book`, `chapter`, `dataset`).
        title:
          type: string
        authors:
          type: array
          items:
            type: object
            additionalProperties: true
            description: |
              A person. Structured records carry `family`/`given`; sources that
              supply an unsplittable name use `literal` instead.
            properties:
              family:
                type: string
              given:
                type: string
              suffix:
                type: string
              literal:
                type: string
        container:
          type: object
          additionalProperties: true
          description: Journal or book the work appears in.
          properties:
            title:
              type: string
            abbreviated:
              type: string
            volume:
              $ref: "#/components/schemas/StringOrInteger"
            issue:
              $ref: "#/components/schemas/StringOrInteger"
            issn:
              type: string
              description: Print ISSN of the serial.
            eissn:
              type: string
              description: Electronic ISSN of the serial.
        identifiers:
          type: array
          description: Present only when the record carries at least one identifier.
          items:
            type: object
            additionalProperties: true
            required:
              - type
              - value
            properties:
              type:
                type: string
              value:
                type: string
        issued:
          type: object
          additionalProperties: true
          description: Present only when the record carries a publication year.
          properties:
            year:
              type: integer
        pages:
          type: object
          additionalProperties: true
          description: Present only when the record carries a first or last page.
          properties:
            first:
              $ref: "#/components/schemas/StringOrInteger"
            last:
              $ref: "#/components/schemas/StringOrInteger"
        number:
          allOf:
            - $ref: "#/components/schemas/StringOrInteger"
          description: Report or thesis number, where the record carries one.
        url:
          type: string
        _source:
          description: Which upstream service supplied the record.
          oneOf:
            - type: string
            - type: object
              additionalProperties: true
              properties:
                service:
                  type: string
                requestUrl:
                  type: string
        _checks:
          $ref: "#/components/schemas/ChecksMeta"
        _provenance:
          $ref: "#/components/schemas/ProvenanceMeta"
    LookupSuccessBody:
      type: object
      additionalProperties: false
      required:
        - ok
        - input
        - result
      description: |
        `result` is `null` with `reason: "not_found"` when the identifier was
        recognized but resolved to no record. That is a 200, not an error.
      properties:
        ok:
          type: boolean
          enum:
            - true
        input:
          type: object
          additionalProperties: false
          required:
            - type
            - value
          description: The first identifier detected in the request, canonicalized.
          properties:
            type:
              type: string
              enum:
                - doi
                - pmid
                - pmcid
                - isbn
                - arxiv
                - issn
                - eissn
                - ads
                - url
            value:
              type: string
        result:
          description: The resolved record, or `null` when nothing resolved.
          type: object
          allOf:
            - $ref: "#/components/schemas/SlimItem"
          nullable: true
        reason:
          type: string
          enum:
            - not_found
          description: Present only when `result` is `null`.
    CheckRequest:
      type: object
      additionalProperties: false
      required:
        - id
      properties:
        id:
          type: string
          minLength: 1
          maxLength: 500
          description: |
            Identifier to check. Accepts DOI (including a shortDOI alias such as
            `10/aabbe`, expanded to the full DOI first), PMID, PMCID, arXiv, or
            ADS bibcode.
            Non-DOI identifiers are resolved to a DOI before lookup.
    RetractionNotice:
      type: object
      additionalProperties: false
      properties:
        type:
          type: string
          description: e.g., "retraction", "correction", "expression-of-concern"
        label:
          type: string
        doi:
          type: string
          nullable: true
        date:
          type: string
          nullable: true
        source:
          type: string
          nullable: true
    RetractionResult:
      type: object
      additionalProperties: false
      properties:
        isRetracted:
          type: boolean
        hasCorrections:
          type: boolean
        hasConcern:
          type: boolean
        notices:
          type: array
          items:
            $ref: "#/components/schemas/RetractionNotice"
        title:
          type: string
          nullable: true
    RetractionCheckResponse:
      type: object
      additionalProperties: false
      required:
        - ok
        - doi
        - result
      properties:
        ok:
          type: boolean
          enum:
            - true
        doi:
          type: string
          description: Resolved DOI, or null when no DOI was found
          nullable: true
        resolvedFrom:
          type: object
          description: Original identifier when different from the resolved DOI
          properties:
            type:
              type: string
            value:
              type: string
        reason:
          type: string
          description: Optional reason code (e.g., "no_doi")
        result:
          $ref: "#/components/schemas/RetractionResult"
    OaLocation:
      type: object
      additionalProperties: false
      properties:
        url:
          type: string
        hostType:
          type: string
        license:
          type: string
          nullable: true
        version:
          type: string
          nullable: true
    OaResult:
      type: object
      additionalProperties: false
      properties:
        isOa:
          type: boolean
        oaStatus:
          type: string
          enum:
            - gold
            - green
            - hybrid
            - bronze
            - closed
        title:
          type: string
          nullable: true
        bestLocation:
          $ref: "#/components/schemas/OaLocation"
        locations:
          type: array
          items:
            $ref: "#/components/schemas/OaLocation"
    OaCheckResponse:
      type: object
      additionalProperties: false
      required:
        - ok
        - doi
        - result
      properties:
        ok:
          type: boolean
          enum:
            - true
        doi:
          type: string
          nullable: true
        resolvedFrom:
          type: object
          properties:
            type:
              type: string
            value:
              type: string
        reason:
          type: string
        result:
          $ref: "#/components/schemas/OaResult"
    ChecksMeta:
      type: object
      description: Sibling field on resolved items; populated only when ?checks= is set.
      additionalProperties: false
      properties:
        retraction:
          type: object
          additionalProperties: false
          properties:
            status:
              type: string
              enum:
                - ok
                - retracted
                - concern
                - correction
                - unknown
            notices:
              type: array
              items:
                $ref: "#/components/schemas/RetractionNotice"
            error:
              type: object
              additionalProperties: false
              properties:
                code:
                  type: string
                message:
                  type: string
        open_access:
          type: object
          additionalProperties: false
          properties:
            status:
              type: string
              enum:
                - open
                - closed
                - unknown
            oa_status:
              type: string
              enum:
                - gold
                - green
                - hybrid
                - bronze
                - closed
            best_url:
              type: string
            pdf_url:
              type: string
              description: Direct free-PDF link when Unpaywall supplies `url_for_pdf`.
              nullable: true
            license:
              type: string
              nullable: true
            version:
              type: string
              nullable: true
            error:
              type: object
              additionalProperties: false
              properties:
                code:
                  type: string
                message:
                  type: string
        doaj:
          type: object
          description: |
            DOAJ (Directory of Open Access Journals) indexing status for the work's JOURNAL,
            keyed by the container ISSN. A VENUE-level signal: `indexed` means the journal is in
            DOAJ's vetted open-access index. `not_indexed` is NOT a predatory-journal verdict —
            subscription journals and brand-new OA titles are legitimately absent. Present only
            when `?checks=doaj` is requested AND the server has `ENABLE_DOAJ_CHECK=1`; otherwise
            `status` is `unknown`. (The DOAJ Seal is not surfaced — absent from the public API.)
          additionalProperties: false
          properties:
            status:
              type: string
              enum:
                - indexed
                - not_indexed
                - unknown
            in_doaj:
              type: boolean
            title:
              type: string
              description: DOAJ's journal title (match confirmation).
            license:
              type: string
              description: Primary licence type, e.g. "CC BY".
            issn:
              type: string
              description: ISSN matched on (normalised NNNN-NNNX).
            url:
              type: string
              description: Canonical DOAJ table-of-contents URL for the journal.
            error:
              type: object
              additionalProperties: false
              properties:
                code:
                  type: string
                message:
                  type: string
    ProvenanceMeta:
      type: object
      description: |
        Sibling field on resolved items; populated only when ?provenance=1 (or =full) is set.
        All fields beyond {transform_version, sources, resolved_at} are additive and optional —
        omitted when not applicable (e.g. fallbacks_tried is absent when the primary resolver
        won on the first try). full_metadata appears only under ?provenance=full.
      additionalProperties: false
      required:
        - transform_version
        - sources
        - resolved_at
      properties:
        transform_version:
          type: string
          description: Pinned dep digest mirroring x-scholar-transform-version.
        resolved_at:
          type: string
          format: date-time
        request_id:
          type: string
          description: Request correlation id (mirrors x-request-id); aligns with the verifier _provenance block.
        sources:
          type: array
          description: Sources that contributed the winning record (V2 emits the single winner).
          items:
            type: object
            additionalProperties: false
            required:
              - name
            properties:
              name:
                type: string
                description: Source service name (e.g., "crossref")
              url:
                type: string
              fetched_at:
                type: string
                format: date-time
                description: When this process fetched the record.
              upstream_fetched_at:
                type: string
                format: date-time
                description: Upstream's own record timestamp (e.g. Crossref indexed/deposited), when available.
              cache:
                type: string
                enum:
                  - hit
                  - miss
                  - bypass
              role:
                type: string
                enum:
                  - primary
                  - fallback
                description: Reserved for multi-source mode; unset in V2 (sources holds only the winner).
              ttl_band:
                type: string
                enum:
                  - recent
                  - mid
                  - frozen
                description: "Cache-TTL recency band applied to this record (Phase 12g): recent (short TTL), mid, or frozen (long TTL). Present only when TTL calibration is enabled."
        fallbacks_tried:
          type: array
          description: Resolvers consulted before the winner; omitted when the primary won first try.
          items:
            type: object
            additionalProperties: false
            required:
              - name
              - outcome
            properties:
              name:
                type: string
              outcome:
                type: string
                enum:
                  - won
                  - not_found
                  - error
                  - empty
                  - skipped
              reason:
                type: string
        fields_from_source:
          type: array
          description: CSL-relevant fields the upstream record populated.
          items:
            type: string
        fields_absent:
          type: array
          description: CSL-relevant fields the schema permits but upstream did not supply.
          items:
            type: string
        normalization:
          type: array
          description: Canonicalisation steps applied to the identifier(s) on this request's input.
          items:
            type: object
            additionalProperties: false
            required:
              - rule
              - from
              - to
            properties:
              rule:
                type: string
                description: Stable rule token, e.g. "doi:lowercase", "issn:format".
              from:
                type: string
              to:
                type: string
        field_provenance:
          type: object
          description: |
            Per-field source attribution. Reserved for per-field × per-source freshness;
            sparse/omitted in V2. Object-valued so future freshness keys are additive.
          additionalProperties:
            type: object
            additionalProperties: false
            required:
              - source
            properties:
              source:
                type: string
              upstream_fetched_at:
                type: string
                format: date-time
        full_metadata:
          type: object
          description: Rich linked-data graph; present only under ?provenance=full.
          additionalProperties: false
          properties:
            funders:
              type: array
              items:
                type: object
                additionalProperties: false
                properties:
                  name:
                    type: string
                  doi:
                    type: string
                  award:
                    type: array
                    items:
                      type: string
            orcids:
              type: array
              items:
                type: string
            ror_ids:
              type: array
              items:
                type: string
            license:
              type: string
              nullable: true
            clinical_trial_ids:
              type: array
              items:
                type: string
        trust_signals:
          type: object
          description: |
            Per-signal trust summary; present only when ?checks= ran alongside
            ?provenance=. Records, per requested signal, whether it was evaluated
            (a DOI was available) or skipped (no_doi), plus the resulting status.
          additionalProperties: false
          properties:
            retraction:
              type: object
              additionalProperties: false
              required:
                - requested
                - evaluated
              properties:
                requested:
                  type: boolean
                evaluated:
                  type: boolean
                status:
                  type: string
                  enum:
                    - ok
                    - retracted
                    - concern
                    - correction
                    - unknown
                skipped_reason:
                  type: string
                  enum:
                    - no_doi
            open_access:
              type: object
              additionalProperties: false
              required:
                - requested
                - evaluated
              properties:
                requested:
                  type: boolean
                evaluated:
                  type: boolean
                status:
                  type: string
                  enum:
                    - open
                    - closed
                    - unknown
                oa_status:
                  type: string
                  enum:
                    - gold
                    - green
                    - hybrid
                    - bronze
                    - closed
                pdf_url:
                  type: string
                  nullable: true
                skipped_reason:
                  type: string
                  enum:
                    - no_doi
        mode:
          type: string
          enum:
            - strict
            - best-effort
          description: Resolver mode that produced the item (Phase 12h). `strict` = fixed-order chain (today's only mode); `best-effort` reserved.
        selection_reason:
          type: string
          enum:
            - static_chain_position
          description: Why the winning source was chosen. For `strict`, always static_chain_position.
        container_only:
          type: boolean
          description: |
            True when the resolved record is a journal/container, not a work — e.g.
            the input was an ISSN/eISSN, which identifies a serial, not a paper
            (Phase 12j). Omitted (not `false`) for ordinary work records.
        conflicts:
          type: object
          description: |
            Cross-source verification (Phase 12a.V2b); present only under
            ?provenance=conflicts AND the ENABLE_PROVENANCE_CONFLICTS server flag.
            The winning record is cross-checked against ONE independent source
            (e.g. PubMed for a Crossref DOI; Google Books vs Open Library).
            Observational — exempt from the byte-determinism guarantee.
          additionalProperties: false
          required:
            - status
          properties:
            checked_against:
              type: string
              description: The independent source cross-checked against (omitted when none available).
            status:
              type: string
              enum:
                - agreed
                - conflict
                - unavailable
            skipped_reason:
              type: string
              enum:
                - no_secondary_source
                - upstream_error
                - not_found
            fields:
              type: array
              description: Field-level disagreements; present only when status is `conflict`.
              items:
                type: object
                additionalProperties: false
                required:
                  - field
                  - primary
                  - secondary
                properties:
                  field:
                    type: string
                    enum:
                      - title
                      - first_author
                      - year
                      - container
                  primary:
                    type: object
                    additionalProperties: false
                    required:
                      - source
                      - value
                    properties:
                      source:
                        type: string
                      value:
                        $ref: "#/components/schemas/StringOrNumber"
                  secondary:
                    type: object
                    additionalProperties: false
                    required:
                      - source
                      - value
                    properties:
                      source:
                        type: string
                      value:
                        $ref: "#/components/schemas/StringOrNumber"
                  similarity:
                    type: number
                    description: Similarity score (0–1) for fuzzy fields.
    EnrichedItem:
      type: object
      additionalProperties: true
      description: |
        Slim bibliographic item view. Carries optional `_checks` and `_provenance`
        sibling fragments when the corresponding query flags are set on the request.
      properties:
        id:
          type: string
        type:
          type: string
        title:
          type: string
        idx:
          type: integer
          description: First contributing input index.
        sourceIdxs:
          type: array
          items:
            type: integer
        _checks:
          $ref: "#/components/schemas/ChecksMeta"
        _provenance:
          $ref: "#/components/schemas/ProvenanceMeta"
    FormatSuccessBody:
      type: object
      additionalProperties: true
      description: |
        Successful format response. `items[]` is always populated by /api/format and
        is populated by /api/format-items only when `?checks=` or `?provenance=1` is set.
      properties:
        ok:
          type: boolean
          enum:
            - true
        formatter:
          type: string
          enum:
            - builtin
            - csl
        styleRequested:
          type: string
          nullable: true
        styleUsed:
          type: string
        lang:
          type: string
        footnote:
          type: boolean
        outputMode:
          type: string
          enum:
            - text
            - html
            - json
        itemsIn:
          type: integer
        itemsOut:
          type: integer
        items:
          type: array
          items:
            $ref: "#/components/schemas/EnrichedItem"
        text:
          type: string
          description: Plain-text rendered citation(s).
        html:
          type: string
          description: HTML rendered citation(s).
        warnings:
          type: array
          items:
            type: string
        meta:
          $ref: "#/components/schemas/BatchSummary"
    BatchSummary:
      type: object
      additionalProperties: true
      description: |
        Phase 12b batch summary. Aggregate counts + a duplicate-group list for a
        request. Additive metadata only — it never changes the formatted output.
        `resolved` counts input lines that mapped to a work, so the buckets are
        self-consistent: `linesIn === resolved + notFound + errored + skipped`,
        and `duplicates === resolved - afterDedupe`. The same shape appears on the
        stream `done` frame. Error/skip buckets are best-effort and may differ
        slightly between /api/format (dedups failing lines) and
        /api/format/stream (counts them per occurrence).
      properties:
        linesIn:
          type: integer
          description: Total input lines.
        resolved:
          type: integer
          description: Input lines that resolved to a work.
        afterDedupe:
          type: integer
          description: Distinct works after de-duplication.
        duplicates:
          type: integer
          description: Collapsed duplicate lines (resolved - afterDedupe).
        notFound:
          type: integer
          description: Lines that resolved to no record.
        errored:
          type: integer
          description: Lines that failed on an upstream/other error.
        skipped:
          type: integer
          description: ISSN-container / ADS-without-token lines skipped.
        warned:
          type: integer
          description: Count of batch warning strings.
        duplicateGroups:
          type: array
          description: One entry per item whose input lines collapsed (>1 source line).
          items:
            type: object
            properties:
              idx:
                type: integer
                description: First contributing input-line index.
              sourceIdxs:
                type: array
                items:
                  type: integer
                description: All input-line indices that collapsed into this item.
  responses:
    OkJsonWithRL:
      description: OK
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-Auth-Source:
          $ref: "#/components/headers/X-Auth-Source"
        X-Auth-Plan:
          $ref: "#/components/headers/X-Auth-Plan"
        X-Scholar-Checks:
          $ref: "#/components/headers/X-Scholar-Checks"
        X-Scholar-Provenance:
          $ref: "#/components/headers/X-Scholar-Provenance"
        X-Scholar-Resolver-Mode:
          $ref: "#/components/headers/X-Scholar-Resolver-Mode"
        X-Scholar-Transform-Version:
          $ref: "#/components/headers/X-Scholar-Transform-Version"
        Idempotent-Replayed:
          $ref: "#/components/headers/Idempotent-Replayed"
        Deprecation:
          $ref: "#/components/headers/Deprecation"
        Sunset:
          $ref: "#/components/headers/Sunset"
        X-RateLimit-Limit:
          $ref: "#/components/headers/X-RateLimit-Limit"
        X-RateLimit-Remaining:
          $ref: "#/components/headers/X-RateLimit-Remaining"
        X-RateLimit-Reset:
          $ref: "#/components/headers/X-RateLimit-Reset"
        X-RateLimit-Reset-After:
          $ref: "#/components/headers/X-RateLimit-Reset-After"
        X-RateLimit-Policy:
          $ref: "#/components/headers/X-RateLimit-Policy"
        Cache-Control:
          $ref: "#/components/headers/Cache-Control-NoStore"
        Content-Security-Policy:
          $ref: "#/components/headers/Content-Security-Policy"
        X-Content-Type-Options:
          $ref: "#/components/headers/X-Content-Type-Options"
        X-Frame-Options:
          $ref: "#/components/headers/X-Frame-Options"
        Referrer-Policy:
          $ref: "#/components/headers/Referrer-Policy"
        Permissions-Policy:
          $ref: "#/components/headers/Permissions-Policy"
        Cross-Origin-Opener-Policy:
          $ref: "#/components/headers/Cross-Origin-Opener-Policy"
        Cross-Origin-Resource-Policy:
          $ref: "#/components/headers/Cross-Origin-Resource-Policy"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/FormatSuccessBody"
          example:
            ok: true
            formatter: builtin
            styleRequested: vancouver
            styleUsed: vancouver
            lang: en-US
            footnote: false
            outputMode: text
            itemsIn: 1
            itemsOut: 1
            text: Baden LR, El Sahly HM, Essink B, et al. Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine. N Engl J Med. 2021;384(5):403-416.
            warnings: []
            meta:
              linesIn: 1
              resolved: 1
              afterDedupe: 1
              duplicates: 0
              notFound: 0
              errored: 0
              skipped: 0
              warned: 0
              duplicateGroups: []
    BadRequest:
      description: Bad Request
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-Error-Code:
          $ref: "#/components/headers/X-Error-Code"
        Cache-Control:
          $ref: "#/components/headers/Cache-Control-NoStore"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
        application/problem+json:
          schema:
            $ref: "#/components/schemas/ProblemDetails"
    Unauthorized:
      description: Unauthorized
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-Error-Code:
          $ref: "#/components/headers/X-Error-Code"
        Cache-Control:
          $ref: "#/components/headers/Cache-Control-NoStore"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
        application/problem+json:
          schema:
            $ref: "#/components/schemas/ProblemDetails"
    Forbidden:
      description: Forbidden
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-Scholar-Mode:
          $ref: "#/components/headers/X-Scholar-Mode"
        X-Error-Code:
          $ref: "#/components/headers/X-Error-Code"
        Cache-Control:
          $ref: "#/components/headers/Cache-Control-NoStore"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
        application/problem+json:
          schema:
            $ref: "#/components/schemas/ProblemDetails"
    TooManyRequests:
      description: Too Many Requests
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-RateLimit-Limit:
          $ref: "#/components/headers/X-RateLimit-Limit"
        X-RateLimit-Remaining:
          $ref: "#/components/headers/X-RateLimit-Remaining"
        X-RateLimit-Reset:
          $ref: "#/components/headers/X-RateLimit-Reset"
        X-RateLimit-Reset-After:
          $ref: "#/components/headers/X-RateLimit-Reset-After"
        X-RateLimit-Policy:
          $ref: "#/components/headers/X-RateLimit-Policy"
        Retry-After:
          description: Seconds until next request allowed.
          schema:
            type: integer
            minimum: 0
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
        application/problem+json:
          schema:
            $ref: "#/components/schemas/ProblemDetails"
    Maintenance:
      description: Service temporarily unavailable (maintenance mode).
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-Scholar-Mode:
          $ref: "#/components/headers/X-Scholar-Mode"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
        application/problem+json:
          schema:
            $ref: "#/components/schemas/ProblemDetails"
    Error:
      description: |
        Typed error (catch-all). Body is the shared `ErrorResponse` envelope and
        the stable code is mirrored in the `X-Error-Code` response header.
      headers:
        X-Request-Id:
          $ref: "#/components/headers/X-Request-Id"
        X-Error-Code:
          $ref: "#/components/headers/X-Error-Code"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
        application/problem+json:
          schema:
            $ref: "#/components/schemas/ProblemDetails"
