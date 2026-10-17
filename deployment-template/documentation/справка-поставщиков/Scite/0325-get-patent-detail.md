> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: get-patent-detail

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get patent detail

> Retrieve one patents record by its identifier. Requires the dataset's Evidence scope.



## OpenAPI

````yaml /openapi.json get /api_partner/evidence/patents/{patent_id}
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
  /api_partner/evidence/patents/{patent_id}:
    get:
      tags:
        - Evidence
      summary: Get patent detail
      description: >-
        Retrieve one patents record by its identifier. Requires the dataset's
        Evidence scope.
      operationId: getPatent
      parameters:
        - name: patent_id
          in: path
          required: true
          schema:
            type: string
            title: Patent Id
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
                $ref: '#/components/schemas/PatentDetailResponse'
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
    PatentDetailResponse:
      properties:
        familySize:
          anyOf:
            - type: integer
            - type: 'null'
          title: Familysize
        forwardCitationCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Forwardcitationcount
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        patent:
          anyOf:
            - $ref: '#/components/schemas/Patent'
            - type: 'null'
      additionalProperties: true
      type: object
      title: PatentDetailResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    Patent:
      properties:
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
        familyId:
          anyOf:
            - type: string
            - type: 'null'
          title: Familyid
        title:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Title
        abstract:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Abstract
        tags:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Tags
        filingStatus:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        classifications:
          items:
            $ref: '#/components/schemas/Classification'
          type: array
          title: Classifications
        inventors:
          items:
            $ref: '#/components/schemas/Inventor'
          type: array
          title: Inventors
        assignees:
          items:
            $ref: '#/components/schemas/Assignee'
          type: array
          title: Assignees
        applicants:
          items:
            $ref: '#/components/schemas/Assignee'
          type: array
          title: Applicants
        appRef:
          anyOf:
            - $ref: '#/components/schemas/AppRef'
            - type: 'null'
        publications:
          items:
            $ref: '#/components/schemas/Publication'
          type: array
          title: Publications
        languages:
          items:
            $ref: '#/components/schemas/Language'
          type: array
          title: Languages
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        legalEvents:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Legalevents
      additionalProperties: true
      type: object
      title: Patent
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
    FacetValue:
      properties:
        id:
          anyOf:
            - type: string
            - type: integer
            - type: number
            - type: 'null'
          title: Id
        name:
          anyOf:
            - type: string
            - type: integer
            - type: 'null'
          title: Name
        highlighted:
          anyOf:
            - type: string
            - type: 'null'
          title: Highlighted
      additionalProperties: true
      type: object
      title: FacetValue
      description: >-
        A faceted field value as returned by Resolute's formatter.


        Resolute returns faceted fields as {id, name} dicts, optionally with a
        "highlighted" key containing

        HTML-marked-up text when the field matched the search query. The id is
        the ES-stored value (filterable),

        and name is the display value (may differ due to es_to_name transforms,
        e.g. country codes).
    Classification:
      properties:
        cpcSymbol:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        position:
          anyOf:
            - type: string
            - type: 'null'
          title: Position
      additionalProperties: true
      type: object
      title: Classification
    Inventor:
      properties:
        name:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        normalizedName:
          anyOf:
            - type: string
            - type: 'null'
          title: Normalizedname
      additionalProperties: true
      type: object
      title: Inventor
    Assignee:
      properties:
        name:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        normalizedName:
          anyOf:
            - type: string
            - type: 'null'
          title: Normalizedname
        country:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        orgType:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Orgtype
      additionalProperties: true
      type: object
      title: Assignee
    AppRef:
      properties:
        docId:
          anyOf:
            - type: string
            - type: 'null'
          title: Docid
        patentOffice:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Patentoffice
        docNumber:
          anyOf:
            - type: string
            - type: 'null'
          title: Docnumber
        kind:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Kind
        filingDate:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Filingdate
        epodoc:
          anyOf:
            - $ref: '#/components/schemas/EpodocRef'
            - type: 'null'
        original:
          anyOf:
            - $ref: '#/components/schemas/OriginalRef'
            - type: 'null'
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      additionalProperties: true
      type: object
      title: AppRef
    Publication:
      properties:
        ids:
          items:
            type: string
          type: array
          title: Ids
        docId:
          anyOf:
            - type: string
            - type: 'null'
          title: Docid
        familyId:
          anyOf:
            - type: string
            - type: 'null'
          title: Familyid
        filingStatus:
          anyOf:
            - type: string
            - type: 'null'
          title: Filingstatus
        pubRef:
          anyOf:
            - $ref: '#/components/schemas/PubRef'
            - type: 'null'
        appRef:
          anyOf:
            - $ref: '#/components/schemas/AppRef'
            - type: 'null'
        inventors:
          items:
            $ref: '#/components/schemas/Inventor'
          type: array
          title: Inventors
        assignees:
          items:
            $ref: '#/components/schemas/Assignee'
          type: array
          title: Assignees
        applicants:
          items:
            $ref: '#/components/schemas/Assignee'
          type: array
          title: Applicants
        classifications:
          items:
            $ref: '#/components/schemas/Classification'
          type: array
          title: Classifications
        priorityClaims:
          items:
            $ref: '#/components/schemas/PriorityClaim'
          type: array
          title: Priorityclaims
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        usptoPath:
          anyOf:
            - type: string
            - type: 'null'
          title: Usptopath
        externalLink:
          anyOf:
            - type: string
            - type: 'null'
          title: Externallink
        backwardCitationCount:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: integer
            - type: 'null'
          title: Backwardcitationcount
        compounds:
          items:
            $ref: '#/components/schemas/Compound'
          type: array
          title: Compounds
      additionalProperties: true
      type: object
      title: Publication
    Language:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        highlighted:
          anyOf:
            - type: string
            - type: 'null'
          title: Highlighted
      additionalProperties: true
      type: object
      title: Language
    EpodocRef:
      properties:
        docNumber:
          anyOf:
            - type: string
            - type: 'null'
          title: Docnumber
        kind:
          anyOf:
            - type: string
            - type: 'null'
          title: Kind
      additionalProperties: true
      type: object
      title: EpodocRef
    OriginalRef:
      properties:
        docNumber:
          anyOf:
            - type: string
            - type: 'null'
          title: Docnumber
        kind:
          anyOf:
            - type: string
            - type: 'null'
          title: Kind
      additionalProperties: true
      type: object
      title: OriginalRef
    PubRef:
      properties:
        country:
          anyOf:
            - type: string
            - type: 'null'
          title: Country
        docNumber:
          anyOf:
            - type: string
            - type: 'null'
          title: Docnumber
        kind:
          anyOf:
            - type: string
            - type: 'null'
          title: Kind
        year:
          anyOf:
            - type: integer
            - type: 'null'
          title: Year
        date:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Date
        epodoc:
          anyOf:
            - $ref: '#/components/schemas/EpodocRef'
            - type: 'null'
        original:
          anyOf:
            - $ref: '#/components/schemas/OriginalRef'
            - type: 'null'
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      additionalProperties: true
      type: object
      title: PubRef
    PriorityClaim:
      properties:
        country:
          anyOf:
            - type: string
            - type: 'null'
          title: Country
        docNumber:
          anyOf:
            - type: string
            - type: 'null'
          title: Docnumber
        year:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: integer
            - type: 'null'
          title: Year
      additionalProperties: true
      type: object
      title: PriorityClaim
    Compound:
      properties:
        compoundComplexity:
          anyOf:
            - type: string
            - type: 'null'
          title: Compoundcomplexity
        exactMatch:
          anyOf:
            - type: string
            - type: 'null'
          title: Exactmatch
        logPXlogp3Aa:
          anyOf:
            - type: string
            - type: 'null'
          title: Logpxlogp3Aa
        massExact:
          anyOf:
            - type: string
            - type: 'null'
          title: Massexact
        molecularWeight:
          anyOf:
            - type: string
            - type: 'null'
          title: Molecularweight
      additionalProperties: true
      type: object
      title: Compound
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
