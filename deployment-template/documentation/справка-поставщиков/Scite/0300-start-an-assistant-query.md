> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: start-an-assistant-query

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Start an Assistant query

> Submit a question to the Scite Assistant. Returns a task ID that you poll via `GET /api_partner/assistant/tasks/{task_id}`.

## Required Fields

### `turns` — Conversation History

The conversation history as a list of turn objects. Each turn has a `role` (`"user"` or `"assistant"`) and `content`. For a new conversation, provide a single user turn:

```json
{
  "turns": [{"role": "user", "content": "How does protein structure affect function?"}]
}
```

For multi-turn conversations, include the full history. Assistant turns should include `references`, `searchStrategy`, `model`, `settings`, and `publicationsConsulted` from previous responses.

### `userInput` — Current Question

The current user question (should match the last user turn's content). Used independently for search strategy generation and tool selection.

---

## Reference Behavior Control

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `alwaysUseReferences` | bool | false | Force reference retrieval even for non-scientific questions |
| `neverUseReferences` | bool | false | Skip reference retrieval entirely (takes precedence over `alwaysUseReferences`) |
| `numReferences` | int | 25 | Maximum reference passages to include in LLM context |
| `referenceChecks` | list[str] | [] | Celery task IDs from uploaded documents (reference check feature) |
| `searches` | list[str] | [] | Pre-defined search queries (skips auto-generation) |

---

## Search Filtering

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `yearFrom` / `yearTo` | str or null | null | Filter by date range (4-digit year or ISO date) |
| `topics` | list[str] | [] | Filter by research topics |
| `citationSections` | list[str] | [] | Filter citations by paper section: `results`, `discussion`, `conclusion`, `methods`, `introduction` |
| `publicationTypes` | list[str] | [] | Filter by type: `review`, `systematic review`, `meta-analysis`, `practice guideline`, `journal-article`, etc. |
| `journals` | list[str] | [] | Filter to specific journal names |
| `openAccessOnly` | bool | false | Only return open access publications |
| `abstractsOnly` | bool | false | Only use paper abstracts (excludes citation statements) |
| `fullTextsOnly` | bool | false | Only use citation statements (excludes abstracts) |

---

## Paper Selection

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `dois` | list[str] | [] | Specific DOIs to scope the search to. DOIs in `userInput` are auto-extracted and merged. |
| `dashboards` | list[int] | [] | Collection (dashboard) IDs to pull DOIs from. Requires authenticated user with access. |

---

## Result Ranking — `rankBy`

Controls how retrieved results are ranked before being passed to the LLM. Default: `"all"`.

| Value | Ranking Strategy |
|-------|-----------------|
| `all` | Balanced: relevance + total citations + Scite index + date + supporting + contrasting |
| `relevance` | Semantic relevance only |
| `date` | Recency + relevance |
| `citations` | Total citation count + relevance |
| `supporting-citations` | Supporting citation count + relevance |
| `contrasting-citations` | Contrasting citation count + relevance |
| `journal-rank` | Scite journal index + relevance |

---

## Response Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `answerLength` | str | `"short"` | `"short"` (~100-200 words), `"medium"` (comprehensive), or `"long"` (exhaustive) |
| `model` | str or null | `gpt-5-nano-2025-08-07` | LLM model for response generation (see below) |
| `reasoningEffort` | str or null | null | `"minimal"`, `"low"`, `"medium"`, or `"high"` — only for reasoning models |

### Available Models

| Model ID | Provider | Notes |
|----------|----------|-------|
| `claude-sonnet-4-6` | Anthropic | 200K context, 64K max output |
| `claude-opus-4-6` | Anthropic | 200K context, 128K max output |
| `claude-sonnet-4-5-20250929` | Anthropic | 200K context, 64K max output |
| `claude-opus-4-5-20251101` | Anthropic | 200K context, 64K max output |
| `claude-haiku-4-5-20251001` | Anthropic | 200K context, 64K max output |
| `gpt-5-nano-2025-08-07` | OpenAI | **Default.** 400K context. Reasoning model |
| `gpt-5-mini-2025-08-07` | OpenAI | 400K context. Reasoning model |
| `gpt-5.2-2025-12-11` | OpenAI | 400K context. Reasoning model. Supports `reasoningEffort` |

If one provider fails, the system automatically falls back to the other. Unsupported or retired model strings automatically fall back to the default (`gpt-5-nano-2025-08-07`).

---

## Structured Response Mode

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `useStructuredResponse` | bool | false | Return per-reference structured data instead of prose |
| `jsonResponseType` | str or null | null | `null` (full detail), `"concise"`, or `"boolean"` (yes/no screening) |
| `reprocessTurnIdx` | int or null | null | Index of an existing turn to reprocess |
| `columnSlug` | str or null | null | Slug of a specific column to reprocess |

---

## Patent Modes

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `usePatentMode` | bool | false | Search patents only (no academic papers) |
| `useMixedPatentMode` | bool | false | Search both patents and academic papers |

---

## Session Management

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `sessionId` | int or null | null | Existing session ID to continue a conversation |

---

## Response

Returns `{"id": "<task_id>"}`. If the user is rate-limited, also includes `"usage": {"used": N, "max": M}`.

---

## Examples

**Basic single question:**
```json
{
  "turns": [{"role": "user", "content": "What is the effect of exercise on depression?"}],
  "userInput": "What is the effect of exercise on depression?"
}
```

**DOI-scoped question:**
```json
{
  "turns": [{"role": "user", "content": "Summarize the key findings"}],
  "userInput": "Summarize the key findings",
  "dois": ["10.1002/cepa.3344", "10.1002/hsr2.70931"]
}
```

**Filtered search:**
```json
{
  "turns": [{"role": "user", "content": "What do systematic reviews say about mindfulness for anxiety?"}],
  "userInput": "What do systematic reviews say about mindfulness for anxiety?",
  "publicationTypes": ["systematic review", "meta-analysis"],
  "yearFrom": "2020",
  "rankBy": "supporting-citations",
  "answerLength": "long"
}
```

**Structured response (table mode):**
```json
{
  "turns": [{"role": "user", "content": "Does each paper support the hypothesis that X causes Y?"}],
  "userInput": "Does each paper support the hypothesis that X causes Y?",
  "useStructuredResponse": true,
  "jsonResponseType": "boolean",
  "dois": ["10.1234/a", "10.1234/b", "10.1234/c"]
}
```



## OpenAPI

````yaml /openapi.json post /api_partner/assistant/poll
openapi: 3.1.0
info:
  title: Scite API
  description: >-
    The Scite API provides publication metadata, Smart Citation tallies,
    citation graphs, literature search, paper recommendations, collections,
    Reference Check, Assistant, Evidence datasets, and MCP access.


    Use the **Documentation** tab for task-oriented guides and the **API
    Reference** tab for endpoint schemas and parameters.


    ## Authentication


    Papers and Tallies endpoints are public. Most other endpoints require a
    bearer credential:


    ```

    Authorization: Bearer <YOUR_API_KEY>

    ```


    Pro users can create and manage keys in the [API
    Console](https://scite.ai/users/me/api). Available scopes depend on the
    account. Enterprise credentials, higher limits, and additional scopes are
    available through [sales](https://scite.ai/contact).


    See **Authentication** in the Documentation tab for the access matrix, and
    **Errors and rate limits** for recovery guidance.


    Use of the API is subject to the [Scite Terms of
    Use](https://scite.ai/terms).
  version: latest
  x-logo:
    url: https://cdn.scite.ai/assets/images/logo-blue.svg
  license:
    name: Scite Terms of Use
    url: https://scite.ai/terms
servers:
  - url: https://api.scite.ai
    description: Production
security:
  - BearerAuth: []
tags:
  - name: Search
    description: >-
      Search metadata and citation statements in Scite. Using the Search API for
      commercial or research use requires a separate license agreement not
      covered by individual plans. Please email sales@scite.ai for more
      information.
  - name: Paper recommendations
    description: >-
      Return papers related to a supplied DOI. Recommendations are available for
      evaluation with eligible Pro access; commercial or research use requires a
      separate license agreement. Contact sales@scite.ai for licensing.
  - name: Papers
    description: >-
      Retrieve publication metadata by DOI or PMID, including title, abstract,
      authors, journal, identifiers, retraction status, and editorial notices.
      Papers endpoints are public.
  - name: Tallies
    description: >-
      Retrieve Smart Citation tallies by DOI. Tally counts represent citation
      statements; `citingPublications` represents distinct citing publications.
      Tallies endpoints are public.
  - name: Smart Citation Graph
    description: >-
      Retrieve citations at the in-text level between and from papers by DOI.


      For example, given a DOI, get a list of citing DOIs including the section
      and classification of each citation statement.


      Snippets are not included in the response.


      Note that these endpoints are restricted without an API token.
  - name: References
    description: |-
      Retrieve references to and from publications by DOI.

      Note that these endpoints require an API token for usage.
  - name: Journal
    description: |-

      Retrieve aggregate information about journals by ISSN.

      ### ISSN Format ###

      A valid ISSN is in the format `dddd-dddC`, where:

      ```
      - d = any decimal digit (0-9)
      - C = checksum (0-9 or X)
      ```
  - name: Authors
    description: Retrieve author metadata and papers by author slug.
  - name: Collections
    description: >-
      Create, retrieve, update, and remove collections: sets of papers monitored
      over time. A dashboard is a report on a collection.
  - name: Reference Check
    description: >-
      Schedule and retrieve reference check jobs. Note that a paid license is
      required for this feature (please email sales@scite.ai for more
      information).


      For an example output report: [see
      here](https://scite.ai/reference-check/${OBJECT_ID}).
  - name: Assistant
    description: >-
      Ask research questions and receive answers grounded in Scite citation
      evidence.


      The Assistant API is asynchronous:


      1. Submit a request with `POST /api_partner/assistant/poll` to receive a
      task ID.

      2. Poll `GET /api_partner/assistant/tasks/{task_id}` until the task
      completes.


      Both endpoints require a bearer credential with the `assistant` scope.
  - name: Evidence
    description: >-
      Search patents, clinical trials, and grants via the Resolute evidence
      datasets.


      Requires an API token with a per-dataset scope

      (`evidence:patents:api`, `evidence:grants:api`,
      `evidence:clinical-trials:api`).

      Please email sales@scite.ai for access.


      ## Query parameters


      ### `q` — free-text query


      Supports boolean operators (`AND`, `OR`, `NOT`) and phrase matching with
      double quotes.


      Examples: `q=CRISPR`, `q="gene therapy" AND cancer`, `q=diabetes NOT
      type+1`


      ### `f` — field filters


      Space-delimited filters in `field:"value"` format. **Values must be
      quoted** with double quotes.

      Call `GET /schema` for the full list of filterable fields per dataset.


      **Patent filters**: `patents.filingStatus` (`"application"`, `"grant"`),
      `patents.assignees.name`, `patents.inventors.name`, `patents.languages`
      (ISO 639-1, e.g. `"en"`)


      **Clinical trial filters**: `trialState.phase` (`"Phase I"` .. `"Phase
      IV"`, `"N/A"`), `trialState.overallStatus` (`"Recruiting"`, `"Completed"`,
      …), `conditions`, `interventions.name`, `sponsors.name`, `registry`
      (`"ClinicalTrials.gov"`, `"UMIN-CTR"`, …), `design.studyType`
      (`"Interventional"`, `"Observational"`)


      **Grant filters**: `agency`, `organization`, `piName`, `country` (ISO
      3166-1 alpha-3, e.g. `"USA"`, `"GBR"`), `dataSource` (`"NIH RePORTER"`,
      `"NSF"`, …)


      Example: `f=trialState.phase:"Phase III"
      trialState.overallStatus:"Recruiting"`


      **Date range filters** use `gte` (>=) and `lt` (<) suffixes with ISO dates
      or epoch milliseconds:

      `f=dates.startDategte:"2024-01-01" dates.startDatelt:"2025-01-01"`.

      Epoch ms: `f=dates.startDategte:"1704067200000"
      dates.startDatelt:"1735689600000"`.

      Dates without a timezone are interpreted as UTC. Timezone offsets are
      supported:

      `"2024-01-01T00:00:00+05:00"`. No space between the field name and the
      suffix.


      ### `s` — sort mode


      Default is `_relevance`. Call `GET /schema` to discover sortable fields
      per dataset.


      ## Response format note


      Some fields in search and detail responses may be either a plain string or
      an object

      `{"id": "...", "name": "..."}` (and optionally `"highlighted": "..."`),
      depending on the

      query. Consumers should handle both shapes, e.g. `value.id ?? value.name
      ?? value`.
  - name: PubMed Source Tallies
    description: >-
      Retrieve tallies indicating how many times a given paper was cited by
      documents of various types from PubMed (e.g. how many times was a given
      DOI cited by practice guidelines).
paths:
  /api_partner/assistant/poll:
    post:
      tags:
        - Assistant
      summary: Start an Assistant query
      description: >-
        Submit a question to the Scite Assistant. Returns a task ID that you
        poll via `GET /api_partner/assistant/tasks/{task_id}`.


        ## Required Fields


        ### `turns` — Conversation History


        The conversation history as a list of turn objects. Each turn has a
        `role` (`"user"` or `"assistant"`) and `content`. For a new
        conversation, provide a single user turn:


        ```json

        {
          "turns": [{"role": "user", "content": "How does protein structure affect function?"}]
        }

        ```


        For multi-turn conversations, include the full history. Assistant turns
        should include `references`, `searchStrategy`, `model`, `settings`, and
        `publicationsConsulted` from previous responses.


        ### `userInput` — Current Question


        The current user question (should match the last user turn's content).
        Used independently for search strategy generation and tool selection.


        ---


        ## Reference Behavior Control


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `alwaysUseReferences` | bool | false | Force reference retrieval even
        for non-scientific questions |

        | `neverUseReferences` | bool | false | Skip reference retrieval
        entirely (takes precedence over `alwaysUseReferences`) |

        | `numReferences` | int | 25 | Maximum reference passages to include in
        LLM context |

        | `referenceChecks` | list[str] | [] | Celery task IDs from uploaded
        documents (reference check feature) |

        | `searches` | list[str] | [] | Pre-defined search queries (skips
        auto-generation) |


        ---


        ## Search Filtering


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `yearFrom` / `yearTo` | str or null | null | Filter by date range
        (4-digit year or ISO date) |

        | `topics` | list[str] | [] | Filter by research topics |

        | `citationSections` | list[str] | [] | Filter citations by paper
        section: `results`, `discussion`, `conclusion`, `methods`,
        `introduction` |

        | `publicationTypes` | list[str] | [] | Filter by type: `review`,
        `systematic review`, `meta-analysis`, `practice guideline`,
        `journal-article`, etc. |

        | `journals` | list[str] | [] | Filter to specific journal names |

        | `openAccessOnly` | bool | false | Only return open access publications
        |

        | `abstractsOnly` | bool | false | Only use paper abstracts (excludes
        citation statements) |

        | `fullTextsOnly` | bool | false | Only use citation statements
        (excludes abstracts) |


        ---


        ## Paper Selection


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `dois` | list[str] | [] | Specific DOIs to scope the search to. DOIs
        in `userInput` are auto-extracted and merged. |

        | `dashboards` | list[int] | [] | Collection (dashboard) IDs to pull
        DOIs from. Requires authenticated user with access. |


        ---


        ## Result Ranking — `rankBy`


        Controls how retrieved results are ranked before being passed to the
        LLM. Default: `"all"`.


        | Value | Ranking Strategy |

        |-------|-----------------|

        | `all` | Balanced: relevance + total citations + Scite index + date +
        supporting + contrasting |

        | `relevance` | Semantic relevance only |

        | `date` | Recency + relevance |

        | `citations` | Total citation count + relevance |

        | `supporting-citations` | Supporting citation count + relevance |

        | `contrasting-citations` | Contrasting citation count + relevance |

        | `journal-rank` | Scite journal index + relevance |


        ---


        ## Response Configuration


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `answerLength` | str | `"short"` | `"short"` (~100-200 words),
        `"medium"` (comprehensive), or `"long"` (exhaustive) |

        | `model` | str or null | `gpt-5-nano-2025-08-07` | LLM model for
        response generation (see below) |

        | `reasoningEffort` | str or null | null | `"minimal"`, `"low"`,
        `"medium"`, or `"high"` — only for reasoning models |


        ### Available Models


        | Model ID | Provider | Notes |

        |----------|----------|-------|

        | `claude-sonnet-4-6` | Anthropic | 200K context, 64K max output |

        | `claude-opus-4-6` | Anthropic | 200K context, 128K max output |

        | `claude-sonnet-4-5-20250929` | Anthropic | 200K context, 64K max
        output |

        | `claude-opus-4-5-20251101` | Anthropic | 200K context, 64K max output
        |

        | `claude-haiku-4-5-20251001` | Anthropic | 200K context, 64K max output
        |

        | `gpt-5-nano-2025-08-07` | OpenAI | **Default.** 400K context.
        Reasoning model |

        | `gpt-5-mini-2025-08-07` | OpenAI | 400K context. Reasoning model |

        | `gpt-5.2-2025-12-11` | OpenAI | 400K context. Reasoning model.
        Supports `reasoningEffort` |


        If one provider fails, the system automatically falls back to the other.
        Unsupported or retired model strings automatically fall back to the
        default (`gpt-5-nano-2025-08-07`).


        ---


        ## Structured Response Mode


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `useStructuredResponse` | bool | false | Return per-reference
        structured data instead of prose |

        | `jsonResponseType` | str or null | null | `null` (full detail),
        `"concise"`, or `"boolean"` (yes/no screening) |

        | `reprocessTurnIdx` | int or null | null | Index of an existing turn to
        reprocess |

        | `columnSlug` | str or null | null | Slug of a specific column to
        reprocess |


        ---


        ## Patent Modes


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `usePatentMode` | bool | false | Search patents only (no academic
        papers) |

        | `useMixedPatentMode` | bool | false | Search both patents and academic
        papers |


        ---


        ## Session Management


        | Field | Type | Default | Description |

        |-------|------|---------|-------------|

        | `sessionId` | int or null | null | Existing session ID to continue a
        conversation |


        ---


        ## Response


        Returns `{"id": "<task_id>"}`. If the user is rate-limited, also
        includes `"usage": {"used": N, "max": M}`.


        ---


        ## Examples


        **Basic single question:**

        ```json

        {
          "turns": [{"role": "user", "content": "What is the effect of exercise on depression?"}],
          "userInput": "What is the effect of exercise on depression?"
        }

        ```


        **DOI-scoped question:**

        ```json

        {
          "turns": [{"role": "user", "content": "Summarize the key findings"}],
          "userInput": "Summarize the key findings",
          "dois": ["10.1002/cepa.3344", "10.1002/hsr2.70931"]
        }

        ```


        **Filtered search:**

        ```json

        {
          "turns": [{"role": "user", "content": "What do systematic reviews say about mindfulness for anxiety?"}],
          "userInput": "What do systematic reviews say about mindfulness for anxiety?",
          "publicationTypes": ["systematic review", "meta-analysis"],
          "yearFrom": "2020",
          "rankBy": "supporting-citations",
          "answerLength": "long"
        }

        ```


        **Structured response (table mode):**

        ```json

        {
          "turns": [{"role": "user", "content": "Does each paper support the hypothesis that X causes Y?"}],
          "userInput": "Does each paper support the hypothesis that X causes Y?",
          "useStructuredResponse": true,
          "jsonResponseType": "boolean",
          "dois": ["10.1234/a", "10.1234/b", "10.1234/c"]
        }

        ```
      operationId: startAssistantQuery
      parameters:
        - name: authorization
          in: header
          required: false
          schema:
            type: string
            description: Set to `Bearer <token>` to pass token for authorization.
            title: Authorization
          description: Set to `Bearer <token>` to pass token for authorization.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AssistantRequestSchema'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssistantPollingResponseSchema'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
        '429':
          $ref: '#/components/responses/TooManyRequests'
        '500':
          $ref: '#/components/responses/InternalServerError'
components:
  schemas:
    AssistantRequestSchema:
      properties:
        alwaysUseReferences:
          type: boolean
          title: Alwaysusereferences
          default: false
        neverUseReferences:
          type: boolean
          title: Neverusereferences
          default: false
        abstractsOnly:
          type: boolean
          title: Abstractsonly
          default: false
        fullTextsOnly:
          type: boolean
          title: Fulltextsonly
          default: false
        numReferences:
          type: integer
          maximum: 1000
          minimum: 0
          title: Numreferences
          default: 25
        rankBy:
          $ref: '#/components/schemas/RankByOptions'
          default: all
        answerLength:
          $ref: '#/components/schemas/AnswerLengthOptions'
          default: medium
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
        reasoningEffort:
          anyOf:
            - $ref: '#/components/schemas/ReasoningEffortOptions'
            - type: 'null'
        citationStyle:
          $ref: '#/components/schemas/StyleOptions'
          default: apa
        yearFrom:
          anyOf:
            - type: string
            - type: 'null'
          title: Yearfrom
        yearTo:
          anyOf:
            - type: string
            - type: 'null'
          title: Yearto
        topics:
          items:
            type: string
          type: array
          title: Topics
        journals:
          items:
            type: string
          type: array
          title: Journals
        citationSections:
          items:
            type: string
          type: array
          title: Citationsections
        publicationTypes:
          items:
            type: string
          type: array
          title: Publicationtypes
        dashboards:
          items:
            type: integer
          type: array
          title: Dashboards
        referenceChecks:
          items:
            type: string
          type: array
          title: Referencechecks
        dois:
          items:
            type: string
          type: array
          title: Dois
        useStructuredResponse:
          type: boolean
          title: Usestructuredresponse
          default: false
        usePatentMode:
          type: boolean
          title: Usepatentmode
          default: false
        useMixedPatentMode:
          type: boolean
          title: Usemixedpatentmode
          default: false
        sessionId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Sessionid
        turns:
          items:
            $ref: '#/components/schemas/TurnSchema-Input'
          type: array
          title: Turns
        userInput:
          type: string
          title: Userinput
        searches:
          items:
            type: string
          type: array
          title: Searches
        openAccessOnly:
          type: boolean
          title: Openaccessonly
          default: false
        jsonResponseType:
          anyOf:
            - type: string
              enum:
                - concise
                - boolean
            - type: 'null'
          title: Jsonresponsetype
        reprocessTurnIdx:
          anyOf:
            - type: integer
            - type: 'null'
          title: Reprocessturnidx
        columnSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Columnslug
        anonId:
          anyOf:
            - type: string
            - type: 'null'
          title: Anonid
        recaptchaToken:
          anyOf:
            - type: string
            - type: 'null'
          title: Recaptchatoken
        country:
          anyOf:
            - type: string
            - type: 'null'
          title: Country
        saveSession:
          type: boolean
          title: Savesession
          default: true
      type: object
      required:
        - turns
        - userInput
      title: AssistantRequestSchema
    AssistantPollingResponseSchema:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        info:
          anyOf:
            - $ref: '#/components/schemas/AssitantPollingInfo'
            - type: 'null'
        status:
          anyOf:
            - type: string
            - type: 'null'
          title: Status
        result:
          anyOf:
            - $ref: '#/components/schemas/AssistantResponseSchema'
            - type: 'null'
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
        usage:
          anyOf:
            - $ref: '#/components/schemas/AssistantUsageSchema'
            - type: 'null'
      type: object
      title: AssistantPollingResponseSchema
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    RankByOptions:
      type: string
      enum:
        - all
        - relevance
        - date
        - citations
        - supporting-citations
        - contrasting-citations
        - journal-rank
      title: RankByOptions
    AnswerLengthOptions:
      type: string
      enum:
        - short
        - medium
        - long
      title: AnswerLengthOptions
    ReasoningEffortOptions:
      type: string
      enum:
        - minimal
        - low
        - medium
        - high
      title: ReasoningEffortOptions
    StyleOptions:
      type: string
      enum:
        - apa
        - ieee
        - mla
        - ama
        - chicago
        - harvard
        - vancouver
        - bibtex
      title: StyleOptions
    TurnSchema-Input:
      properties:
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role
        content:
          anyOf:
            - type: string
            - type: 'null'
          title: Content
        sections:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Sections
        structuredResponse:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Structuredresponse
        references:
          items:
            $ref: '#/components/schemas/sciteapi__models__assistant__ReferenceSchema'
          type: array
          title: References
        feedback:
          anyOf:
            - $ref: '#/components/schemas/FeedbackSchema'
            - type: 'null'
        searchStrategy:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Searchstrategy
        warning:
          anyOf:
            - type: string
            - type: 'null'
          title: Warning
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
        settings:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Settings
        publicationsConsulted:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Publicationsconsulted
        columns:
          anyOf:
            - items:
                $ref: '#/components/schemas/StructuredColumn'
              type: array
            - type: 'null'
          title: Columns
      type: object
      title: TurnSchema
    AssitantPollingInfo:
      properties:
        step:
          anyOf:
            - type: string
            - type: 'null'
          title: Step
        stepNumber:
          anyOf:
            - type: integer
            - type: 'null'
          title: Stepnumber
        response:
          anyOf:
            - type: string
            - type: 'null'
          title: Response
        structuredResponse:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Structuredresponse
        searches:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Searches
        publicationsUsed:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Publicationsused
        publicationsConsulting:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Publicationsconsulting
        currentSearch:
          anyOf:
            - type: string
            - type: 'null'
          title: Currentsearch
        dois:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Dois
        factChecks:
          anyOf:
            - $ref: '#/components/schemas/FactCheck'
            - type: 'null'
      type: object
      title: AssitantPollingInfo
    AssistantResponseSchema:
      properties:
        title:
          anyOf:
            - type: string
            - type: 'null'
          title: Title
        sessionId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Sessionid
        turns:
          items:
            $ref: '#/components/schemas/TurnSchema-Output'
          type: array
          title: Turns
        turnsTotal:
          anyOf:
            - type: integer
            - type: 'null'
          title: Turnstotal
        turnsOffset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Turnsoffset
        lastUpdated:
          anyOf:
            - type: string
              format: date
            - type: 'null'
          title: Lastupdated
        shareToken:
          anyOf:
            - type: string
            - type: 'null'
          title: Sharetoken
        createdAt:
          anyOf:
            - type: string
              format: date
            - type: 'null'
          title: Createdat
        hasUploadedReferences:
          type: boolean
          title: Hasuploadedreferences
          default: false
        slug:
          type: string
          title: Slug
          readOnly: true
      type: object
      required:
        - slug
      title: AssistantResponseSchema
    AssistantUsageSchema:
      properties:
        used:
          type: integer
          title: Used
        max:
          type: integer
          title: Max
      type: object
      required:
        - used
        - max
      title: AssistantUsageSchema
    ErrorResponse:
      type: object
      properties:
        detail:
          type: string
          description: Human-readable error detail.
      required:
        - detail
      title: ErrorResponse
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    sciteapi__models__assistant__ReferenceSchema:
      properties:
        answer:
          type: string
          title: Answer
        texts:
          items:
            type: string
          type: array
          title: Texts
        textSources:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Textsources
        context:
          type: string
          title: Context
        title:
          type: string
          title: Title
        doi:
          type: string
          title: Doi
        link:
          type: string
          title: Link
        type:
          type: string
          title: Type
          default: academic_paper
        paper:
          $ref: '#/components/schemas/SearchResultSchemaWithDateStr-Input'
        patent:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Patent
        refCheckId:
          anyOf:
            - type: string
            - type: 'null'
          title: Refcheckid
        included:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Included
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
      type: object
      required:
        - answer
        - texts
        - context
        - title
        - doi
        - link
        - paper
      title: ReferenceSchema
    FeedbackSchema:
      properties:
        feedbackType:
          anyOf:
            - $ref: '#/components/schemas/FeedbackType'
            - type: 'null'
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
      type: object
      title: FeedbackSchema
    StructuredColumn:
      properties:
        name:
          type: string
          title: Name
        slug:
          type: string
          title: Slug
        instructions:
          anyOf:
            - type: string
            - type: 'null'
          title: Instructions
        type:
          $ref: '#/components/schemas/ColumnType'
          default: response
        order:
          type: integer
          title: Order
          default: 0
        json_response_type:
          anyOf:
            - type: string
              enum:
                - concise
                - boolean
            - type: 'null'
          title: Json Response Type
      type: object
      required:
        - name
        - slug
      title: StructuredColumn
    FactCheck:
      properties:
        used:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Used
        rejected:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Rejected
      type: object
      title: FactCheck
    TurnSchema-Output:
      properties:
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role
        content:
          anyOf:
            - type: string
            - type: 'null'
          title: Content
        sections:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Sections
        structuredResponse:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Structuredresponse
        references:
          items:
            $ref: >-
              #/components/schemas/sciteapi__models__assistant__ReferenceSchema-Output
          type: array
          title: References
        feedback:
          anyOf:
            - $ref: '#/components/schemas/FeedbackSchema'
            - type: 'null'
        searchStrategy:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Searchstrategy
        warning:
          anyOf:
            - type: string
            - type: 'null'
          title: Warning
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
        settings:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Settings
        publicationsConsulted:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Publicationsconsulted
        columns:
          anyOf:
            - items:
                $ref: '#/components/schemas/StructuredColumn'
              type: array
            - type: 'null'
          title: Columns
      type: object
      title: TurnSchema
    SearchResultSchemaWithDateStr-Input:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        doi:
          anyOf:
            - type: string
            - type: 'null'
          title: Doi
        title:
          anyOf:
            - type: string
            - type: 'null'
          title: Title
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
        authors:
          anyOf:
            - items:
                $ref: '#/components/schemas/AuthorResults'
              type: array
            - type: 'null'
          title: Authors
        journal:
          anyOf:
            - type: string
            - type: 'null'
          title: Journal
        shortJournal:
          anyOf:
            - type: string
            - type: 'null'
          title: Shortjournal
        publisher:
          anyOf:
            - type: string
            - type: 'null'
          title: Publisher
        memberId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Memberid
        abstract:
          anyOf:
            - type: string
            - type: 'null'
          title: Abstract
        year:
          anyOf:
            - type: integer
            - type: 'null'
          title: Year
        date:
          anyOf:
            - type: string
            - type: 'null'
          title: Date
        lastUpdate:
          anyOf:
            - type: integer
            - type: 'null'
          title: Lastupdate
        volume:
          anyOf:
            - type: string
            - type: 'null'
          title: Volume
        issue:
          anyOf:
            - type: string
            - type: 'null'
          title: Issue
        page:
          anyOf:
            - type: string
            - type: 'null'
          title: Page
        tally:
          anyOf:
            - $ref: '#/components/schemas/TallyResponse'
            - type: 'null'
        issns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Issns
        editorialNotices:
          items:
            $ref: '#/components/schemas/EditorialNoticeSchema'
          type: array
          title: Editorialnotices
        normalizedTypes:
          items:
            type: string
          type: array
          title: Normalizedtypes
        isOa:
          type: boolean
          title: Isoa
          default: false
        oaStatus:
          type: string
          title: Oastatus
          default: closed
        meshTypes:
          items:
            $ref: '#/components/schemas/PubmedMeshTypeResponse'
          type: array
          title: Meshtypes
        relevancyScore:
          anyOf:
            - type: number
            - type: 'null'
          title: Relevancyscore
        citations:
          items:
            $ref: '#/components/schemas/CitationSearch'
          type: array
          title: Citations
        fulltextExcerpts:
          items:
            type: string
          type: array
          title: Fulltextexcerpts
        highlightedFields:
          items:
            type: string
          type: array
          title: Highlightedfields
      type: object
      title: SearchResultSchemaWithDateStr
    FeedbackType:
      type: string
      enum:
        - positive
        - negative
      title: FeedbackType
    ColumnType:
      type: string
      enum:
        - response
        - dynamic
      title: ColumnType
    sciteapi__models__assistant__ReferenceSchema-Output:
      properties:
        answer:
          type: string
          title: Answer
        texts:
          items:
            type: string
          type: array
          title: Texts
        textSources:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Textsources
        context:
          type: string
          title: Context
        title:
          type: string
          title: Title
        doi:
          type: string
          title: Doi
        link:
          type: string
          title: Link
        type:
          type: string
          title: Type
          default: academic_paper
        paper:
          $ref: '#/components/schemas/SearchResultSchemaWithDateStr-Output'
        patent:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Patent
        refCheckId:
          anyOf:
            - type: string
            - type: 'null'
          title: Refcheckid
        included:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Included
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
      type: object
      required:
        - answer
        - texts
        - context
        - title
        - doi
        - link
        - paper
      title: ReferenceSchema
    AuthorResults:
      properties:
        authorName:
          anyOf:
            - type: string
            - type: 'null'
          title: Authorname
        authorSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Authorslug
        authorSequenceNumber:
          anyOf:
            - type: string
            - type: integer
            - type: 'null'
          title: Authorsequencenumber
        affiliation:
          anyOf:
            - type: string
            - type: 'null'
          title: Affiliation
        affiliationSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Affiliationslug
      type: object
      title: AuthorResults
    TallyResponse:
      properties:
        total:
          type: integer
          title: Total
        supporting:
          type: integer
          title: Supporting
        contradicting:
          type: integer
          title: Contradicting
        mentioning:
          type: integer
          title: Mentioning
        unclassified:
          type: integer
          title: Unclassified
        doi:
          anyOf:
            - type: string
            - type: 'null'
          title: Doi
        citingPublications:
          anyOf:
            - type: integer
            - type: 'null'
          title: Citingpublications
      type: object
      required:
        - total
        - supporting
        - contradicting
        - mentioning
        - unclassified
      title: TallyResponse
      example:
        citingPublications: 436
        contradicting: 6
        doi: 10.1016/j.biopsych.2005.08.012
        mentioning: 308
        supporting: 27
        total: 347
        unclassified: 6
    EditorialNoticeSchema:
      properties:
        status:
          anyOf:
            - type: string
            - type: 'null'
          title: Status
        date:
          anyOf:
            - type: string
            - type: 'null'
          title: Date
        noticeDoi:
          anyOf:
            - type: string
            - type: 'null'
          title: Noticedoi
        doi:
          type: string
          title: Doi
        urls:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Urls
      type: object
      required:
        - doi
      title: EditorialNoticeSchema
    PubmedMeshTypeResponse:
      properties:
        descriptorId:
          type: string
          title: Descriptorid
        descriptorName:
          type: string
          title: Descriptorname
        qualifierId:
          anyOf:
            - type: string
            - type: 'null'
          title: Qualifierid
        qualifierName:
          anyOf:
            - type: string
            - type: 'null'
          title: Qualifiername
      type: object
      required:
        - descriptorId
        - descriptorName
      title: PubmedMeshTypeResponse
    CitationSearch:
      properties:
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        source:
          type: string
          title: Source
        target:
          type: string
          title: Target
        negative:
          anyOf:
            - type: number
            - type: 'null'
          title: Negative
        positive:
          anyOf:
            - type: number
            - type: 'null'
          title: Positive
        neutral:
          anyOf:
            - type: number
            - type: 'null'
          title: Neutral
        section:
          anyOf:
            - type: string
            - type: 'null'
          title: Section
        expertClassification:
          anyOf:
            - type: string
            - type: 'null'
          title: Expertclassification
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
        typeConfidence:
          anyOf:
            - type: number
            - type: 'null'
          title: Typeconfidence
        snippet:
          type: string
          title: Snippet
        lang:
          anyOf:
            - type: string
            - type: 'null'
          title: Lang
        langConfidence:
          anyOf:
            - type: number
            - type: 'null'
          title: Langconfidence
        refLocation:
          anyOf:
            - type: string
            - type: 'null'
          title: Reflocation
        memberId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Memberid
        selfCites:
          items:
            $ref: '#/components/schemas/SelfCiteSchema'
          type: array
          title: Selfcites
        snippetHidden:
          type: boolean
          title: Snippethidden
          default: false
      type: object
      required:
        - source
        - target
        - snippet
      title: CitationSearch
    SearchResultSchemaWithDateStr-Output:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        doi:
          anyOf:
            - type: string
            - type: 'null'
          title: Doi
        title:
          anyOf:
            - type: string
            - type: 'null'
          title: Title
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
        authors:
          anyOf:
            - items:
                $ref: '#/components/schemas/AuthorResults'
              type: array
            - type: 'null'
          title: Authors
        journal:
          anyOf:
            - type: string
            - type: 'null'
          title: Journal
        shortJournal:
          anyOf:
            - type: string
            - type: 'null'
          title: Shortjournal
        publisher:
          anyOf:
            - type: string
            - type: 'null'
          title: Publisher
        memberId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Memberid
        abstract:
          anyOf:
            - type: string
            - type: 'null'
          title: Abstract
        year:
          anyOf:
            - type: integer
            - type: 'null'
          title: Year
        date:
          anyOf:
            - type: string
            - type: 'null'
          title: Date
        lastUpdate:
          anyOf:
            - type: integer
            - type: 'null'
          title: Lastupdate
        volume:
          anyOf:
            - type: string
            - type: 'null'
          title: Volume
        issue:
          anyOf:
            - type: string
            - type: 'null'
          title: Issue
        page:
          anyOf:
            - type: string
            - type: 'null'
          title: Page
        tally:
          anyOf:
            - $ref: '#/components/schemas/TallyResponse'
            - type: 'null'
        issns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Issns
        editorialNotices:
          items:
            $ref: '#/components/schemas/EditorialNoticeSchema'
          type: array
          title: Editorialnotices
        normalizedTypes:
          items:
            type: string
          type: array
          title: Normalizedtypes
        isOa:
          type: boolean
          title: Isoa
          default: false
        oaStatus:
          type: string
          title: Oastatus
          default: closed
        meshTypes:
          items:
            $ref: '#/components/schemas/PubmedMeshTypeResponse'
          type: array
          title: Meshtypes
        relevancyScore:
          anyOf:
            - type: number
            - type: 'null'
          title: Relevancyscore
        citations:
          items:
            $ref: '#/components/schemas/CitationSearch'
          type: array
          title: Citations
        fulltextExcerpts:
          items:
            type: string
          type: array
          title: Fulltextexcerpts
        highlightedFields:
          items:
            type: string
          type: array
          title: Highlightedfields
      type: object
      title: SearchResultSchemaWithDateStr
    SelfCiteSchema:
      properties:
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
        family:
          anyOf:
            - type: string
            - type: 'null'
          title: Family
        given:
          anyOf:
            - type: string
            - type: 'null'
          title: Given
      type: object
      required:
        - type
        - family
        - given
      title: SelfCiteSchema
  responses:
    Unauthorized:
      description: The request is missing a valid bearer credential.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: >-
        The credential is valid, but the key or account lacks the required
        scope.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    TooManyRequests:
      description: >-
        The request exceeded a rate limit. Inspect the rate-limit headers before
        retrying.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalServerError:
      description: The server encountered an unexpected error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
