> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: get-assistant-task

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Assistant Task

> Poll the status and results of an assistant task. Call this endpoint repeatedly until the status is `SUCCESS`.

## Task States

| Status | Description |
|--------|-------------|
| `PENDING` | Task is queued, not yet started |
| `STARTED` | Task is actively processing — `info` contains progress details |
| `SUCCESS` | Task completed — `result` contains the full response |
| `FAILURE` | Task failed — `error` contains the error message |
| `CANCELLED` | Task was cancelled via the cancel endpoint |
| `REVOKED` | Task was revoked |

## Progress Info (during `STARTED`)

While the task is running, the `info` field provides real-time progress:

```json
{
  "id": "abc123",
  "status": "STARTED",
  "info": {
    "step": "EXECUTING_SEARCHES",
    "stepNumber": 3,
    "response": "partial response text...",
    "searches": ["query 1", "query 2"],
    "publicationsUsed": ["10.1234/example"],
    "publicationsConsulting": ["Author et al., Title, Journal, 2024"],
    "currentSearch": "current query being executed"
  }
}
```

**Processing steps in order:**
1. `SCHEDULING_ASSISTANT` — task queued
2. `GENERATING_SEARCH_STRATEGY` — AI generating search queries
3. `EXECUTING_SEARCHES` — running queries against Elasticsearch
4. `RETRIEVING_UPLOADED_DOCUMENTS` — loading reference check documents (if applicable)
5. `RETRIEVING_PRIMARY_SOURCES` — enriching with primary source data
6. `COMPOSING_RESPONSE` — preparing context for LLM
7. `GENERATING_RESPONSE` — LLM generating the answer

## Success Result

```json
{
  "id": "abc123",
  "status": "SUCCESS",
  "result": {
    "title": "How does protein structure affect function?",
    "sessionId": 42,
    "slug": "how-does-protein-structure-affect-function-xK9mP",
    "turns": [...],
    "lastUpdated": "2025-01-15",
    "createdAt": "2025-01-15",
    "tooManySessions": false
  }
}
```

## Turn Structure

Each assistant turn in the `turns` array contains:

| Field | Type | Description |
|-------|------|-------------|
| `role` | str | `"user"` or `"assistant"` |
| `content` | str | Response text with numbered citation markers like `[1]`, `[2]` |
| `structuredResponse` | list or null | Structured response data (when `useStructuredResponse` was true) |
| `references` | list | Cited references (see below) |
| `searchStrategy` | list[str] or null | Search queries that were used |
| `warning` | str or null | Warning message if applicable |
| `model` | str or null | The model that generated this response |
| `settings` | dict or null | Settings applied (e.g., AI-suggested `rankBy`, `yearFrom`, `yearTo`) |
| `publicationsConsulted` | list[dict] or null | All publications considered (including unused ones) |

## Reference Structure

Each reference in the `references` array:

| Field | Type | Description |
|-------|------|-------------|
| `answer` | str | The relevant text passage (citation statement or abstract excerpt) |
| `texts` | list[str] | Text passages used |
| `context` | str | Surrounding context of the passage |
| `title` | str | Paper title |
| `doi` | str | Paper DOI |
| `link` | str | Link to the Scite report page |
| `type` | str | `"abstract"` or `"citation_statement"` |
| `paper` | object | Full paper metadata (title, authors, journal, year, date, abstract, tally, DOI, etc.) |
| `patent` | object or null | Patent data if from patent search |
| `refCheckId` | str or null | Reference check task ID if from uploaded document |



## OpenAPI

````yaml /openapi.json get /api_partner/assistant/tasks/{task_id}
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
  /api_partner/assistant/tasks/{task_id}:
    get:
      tags:
        - Assistant
      summary: Get Assistant Task
      description: >-
        Poll the status and results of an assistant task. Call this endpoint
        repeatedly until the status is `SUCCESS`.


        ## Task States


        | Status | Description |

        |--------|-------------|

        | `PENDING` | Task is queued, not yet started |

        | `STARTED` | Task is actively processing — `info` contains progress
        details |

        | `SUCCESS` | Task completed — `result` contains the full response |

        | `FAILURE` | Task failed — `error` contains the error message |

        | `CANCELLED` | Task was cancelled via the cancel endpoint |

        | `REVOKED` | Task was revoked |


        ## Progress Info (during `STARTED`)


        While the task is running, the `info` field provides real-time progress:


        ```json

        {
          "id": "abc123",
          "status": "STARTED",
          "info": {
            "step": "EXECUTING_SEARCHES",
            "stepNumber": 3,
            "response": "partial response text...",
            "searches": ["query 1", "query 2"],
            "publicationsUsed": ["10.1234/example"],
            "publicationsConsulting": ["Author et al., Title, Journal, 2024"],
            "currentSearch": "current query being executed"
          }
        }

        ```


        **Processing steps in order:**

        1. `SCHEDULING_ASSISTANT` — task queued

        2. `GENERATING_SEARCH_STRATEGY` — AI generating search queries

        3. `EXECUTING_SEARCHES` — running queries against Elasticsearch

        4. `RETRIEVING_UPLOADED_DOCUMENTS` — loading reference check documents
        (if applicable)

        5. `RETRIEVING_PRIMARY_SOURCES` — enriching with primary source data

        6. `COMPOSING_RESPONSE` — preparing context for LLM

        7. `GENERATING_RESPONSE` — LLM generating the answer


        ## Success Result


        ```json

        {
          "id": "abc123",
          "status": "SUCCESS",
          "result": {
            "title": "How does protein structure affect function?",
            "sessionId": 42,
            "slug": "how-does-protein-structure-affect-function-xK9mP",
            "turns": [...],
            "lastUpdated": "2025-01-15",
            "createdAt": "2025-01-15",
            "tooManySessions": false
          }
        }

        ```


        ## Turn Structure


        Each assistant turn in the `turns` array contains:


        | Field | Type | Description |

        |-------|------|-------------|

        | `role` | str | `"user"` or `"assistant"` |

        | `content` | str | Response text with numbered citation markers like
        `[1]`, `[2]` |

        | `structuredResponse` | list or null | Structured response data (when
        `useStructuredResponse` was true) |

        | `references` | list | Cited references (see below) |

        | `searchStrategy` | list[str] or null | Search queries that were used |

        | `warning` | str or null | Warning message if applicable |

        | `model` | str or null | The model that generated this response |

        | `settings` | dict or null | Settings applied (e.g., AI-suggested
        `rankBy`, `yearFrom`, `yearTo`) |

        | `publicationsConsulted` | list[dict] or null | All publications
        considered (including unused ones) |


        ## Reference Structure


        Each reference in the `references` array:


        | Field | Type | Description |

        |-------|------|-------------|

        | `answer` | str | The relevant text passage (citation statement or
        abstract excerpt) |

        | `texts` | list[str] | Text passages used |

        | `context` | str | Surrounding context of the passage |

        | `title` | str | Paper title |

        | `doi` | str | Paper DOI |

        | `link` | str | Link to the Scite report page |

        | `type` | str | `"abstract"` or `"citation_statement"` |

        | `paper` | object | Full paper metadata (title, authors, journal, year,
        date, abstract, tally, DOI, etc.) |

        | `patent` | object or null | Patent data if from patent search |

        | `refCheckId` | str or null | Reference check task ID if from uploaded
        document |
      operationId: getAssistantTask
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            title: Task Id
        - name: authorization
          in: header
          required: false
          schema:
            type: string
            description: Set to `Bearer <token>` to pass token for authorization.
            title: Authorization
          description: Set to `Bearer <token>` to pass token for authorization.
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
        '404':
          $ref: '#/components/responses/NotFound'
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
    NotFound:
      description: The requested resource was not found.
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
