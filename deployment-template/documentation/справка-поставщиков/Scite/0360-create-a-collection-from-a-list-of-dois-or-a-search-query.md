> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: create-a-collection-from-a-list-of-dois-or-a-search-query

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a collection from a list of DOIs or a search query

> Either 'dois' or 'query' is required to create a dashboard. If both are provided, 'query' will be used.



## OpenAPI

````yaml /openapi.json post /api_partner/collections/create
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
  /api_partner/collections/create:
    post:
      tags:
        - Collections
      summary: Create a collection from a list of DOIs or a search query
      description: >-
        Either 'dois' or 'query' is required to create a dashboard. If both are
        provided, 'query' will be used.
      operationId: createCollection
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
              $ref: '#/components/schemas/PartnerCreateDashboardRQ'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomDashboardSchema'
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
    PartnerCreateDashboardRQ:
      properties:
        name:
          type: string
          title: Name
        email:
          type: string
          format: email
          title: Email
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          default: ''
        isPublic:
          type: boolean
          title: Ispublic
          default: false
        isHidden:
          type: boolean
          title: Ishidden
          default: false
        isSharedWithOrg:
          type: boolean
          title: Issharedwithorg
          default: false
        dois:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Dois
        query:
          anyOf:
            - $ref: '#/components/schemas/QuerySchemaV2'
            - type: 'null'
        enableDashboardCitationAlerts:
          type: boolean
          title: Enabledashboardcitationalerts
          default: false
      type: object
      required:
        - name
        - email
      title: PartnerCreateDashboardRQ
    CustomDashboardSchema:
      properties:
        id:
          type: integer
          title: Id
        name:
          type: string
          title: Name
        description:
          type: string
          title: Description
          default: ''
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
        dashboardType:
          anyOf:
            - type: string
            - type: 'null'
          title: Dashboardtype
        isPublic:
          type: boolean
          title: Ispublic
          default: false
        organizationSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Organizationslug
        componentLayout:
          items:
            $ref: '#/components/schemas/DashboardComponentLayoutSchema'
          type: array
          title: Componentlayout
        doiQuery:
          $ref: '#/components/schemas/DashboardDoiQuerySchema'
        lastUpdated:
          anyOf:
            - type: string
              format: date
            - type: 'null'
          title: Lastupdated
        doisUpdatedTS:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Doisupdatedts
        doisRefreshedTS:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Doisrefreshedts
        refreshStatus:
          type: string
          title: Refreshstatus
          default: '-'
        accessType:
          anyOf:
            - type: string
            - type: 'null'
          title: Accesstype
          default: VIEWER
        totalDoiCount:
          type: integer
          title: Totaldoicount
          default: 0
        matchedDoiCount:
          type: integer
          title: Matcheddoicount
          default: 0
        unmatchedDoiCount:
          type: integer
          title: Unmatcheddoicount
          default: 0
        unmatchedDois:
          items: {}
          type: array
          uniqueItems: true
          title: Unmatcheddois
        warning:
          anyOf:
            - type: string
            - type: 'null'
          title: Warning
      type: object
      required:
        - id
        - name
        - componentLayout
        - doiQuery
      title: CustomDashboardSchema
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    QuerySchemaV2:
      properties:
        term:
          anyOf:
            - type: string
            - type: 'null'
          title: Term
          description: Cross-field search term. Can be left blank.
          default: ''
          examples:
            - mitosis
        mode:
          type: string
          enum:
            - all
            - citations
            - papers
            - question-answering
          title: Mode
          description: Select search mode, see above.
          default: all
          examples:
            - citations
        limit:
          type: integer
          title: Limit
          description: How many results to fetch. Up to 10,000 can be fetched at once.
          default: 10
          examples:
            - 100
        offset:
          type: integer
          title: Offset
          description: Can be used for pagination in combination with `limit`.
          default: 0
          examples:
            - 10
        sort:
          anyOf:
            - type: string
              enum:
                - date
                - total_cited
                - total_supported
                - total_contrasted
                - total_mentioned
                - total_citing_publications
            - type: 'null'
          title: Sort
          description: >-
            How the results should be sorted. Leave blank for generic query
            'relevance'.
          examples:
            - total_supported
        sortOrder:
          anyOf:
            - type: string
              enum:
                - asc
                - desc
            - type: 'null'
          title: Sortorder
          description: Result sort order for selected sort.
        title:
          anyOf:
            - type: string
            - type: 'null'
          title: Title
          description: Match text in publication title.
          examples:
            - Cellular
        abstract:
          anyOf:
            - type: string
            - type: 'null'
          title: Abstract
          description: Match text in publication abstract.
          examples:
            - Amygdala
        doi:
          anyOf:
            - type: string
            - type: 'null'
          title: Doi
          description: >-
            Scope the search to a single DOI (exact match). Convenience alias
            for a one-element `dois`. Combine with `term` to search within a
            known publication.
          examples:
            - 10.1002/cepa.3344
        dois:
          items:
            type: string
          type: array
          title: Dois
          description: >-
            Scope the search to one or more specific DOIs (exact match). Combine
            with `term` to search within a known publication.
          default: []
          examples:
            - - 10.1002/cepa.3344
        dateFrom:
          anyOf:
            - type: string
            - type: 'null'
          title: Datefrom
          description: >-
            Match publications published from this date onwards (YYYY-MM-DD or
            just YYYY).
        dateTo:
          anyOf:
            - type: string
            - type: 'null'
          title: Dateto
          description: >-
            Match publications published up to this date (YYYY-MM-DD or just
            YYYY).
          examples:
            - '2001-05-04'
        indexedFrom:
          anyOf:
            - type: string
            - type: 'null'
          title: Indexedfrom
          description: Match only records indexed from this time
        citationTypes:
          items:
            type: string
            enum:
              - supporting
              - contrasting
              - mentioning
          type: array
          title: Citationtypes
          description: Match smart citations of certain types.
          default: []
        hasRetraction:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Hasretraction
          description: Publication has retraction or not.
          examples:
            - true
        hasConcern:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Hasconcern
          description: Publication has editorial concern or not.
          examples:
            - true
        hasCorrection:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Hascorrection
          description: Publication has correction or not.
          examples:
            - true
        hasErratum:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Haserratum
          description: Publication has erratum or not.
          examples:
            - true
        hasWithdrawn:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Haswithdrawn
          description: Publication has been withdrawn or not.
          examples:
            - true
        hasTally:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Hastally
          description: >-
            Publication has smart citations made towards it or not (i.e. a Scite
            tally of > 0).
          examples:
            - true
        supportingFrom:
          anyOf:
            - type: integer
            - type: 'null'
          title: Supportingfrom
          description: >-
            Number of supporting citations made from publication. Leave blank
            for any count.
        supportingTo:
          anyOf:
            - type: integer
            - type: 'null'
          title: Supportingto
          description: >-
            Number of supporting citations made toward publication. Leave blank
            for any count.
          examples:
            - 1
        mentioningFrom:
          anyOf:
            - type: integer
            - type: 'null'
          title: Mentioningfrom
          description: >-
            Number of mentioning citations made from publication. Leave blank
            for any count.
          examples:
            - 100
        mentioningTo:
          anyOf:
            - type: integer
            - type: 'null'
          title: Mentioningto
          description: >-
            Number of mentioning citations made toward publication. Leave blank
            for any count.
          examples:
            - 500
        contrastingFrom:
          anyOf:
            - type: integer
            - type: 'null'
          title: Contrastingfrom
          description: >-
            Number of contrasting citations made from publication. Leave blank
            for any count.
          examples:
            - 5
        contrastingTo:
          anyOf:
            - type: integer
            - type: 'null'
          title: Contrastingto
          description: >-
            Number of contrasting citations made toward publication. Leave blank
            for any count.
        citingPublicationsFrom:
          anyOf:
            - type: integer
            - type: 'null'
          title: Citingpublicationsfrom
          description: >-
            Number of traditional citations made from publication AKA the number
            of references. Leave blank for any count.
          examples:
            - 5
        citingPublicationsTo:
          anyOf:
            - type: integer
            - type: 'null'
          title: Citingpublicationsto
          description: >-
            Number of traditional citations made toward publication. Leave blank
            for any count.
        author:
          anyOf:
            - type: string
            - type: 'null'
          title: Author
          description: Publication author name.
          examples:
            - Albert Einstein
        authors:
          items:
            type: string
          type: array
          title: Authors
          default: []
        journal:
          anyOf:
            - type: string
            - type: 'null'
          title: Journal
          description: Journal in which publication appears.
          examples:
            - Nature
        journals:
          items:
            type: string
          type: array
          title: Journals
          default: []
        publisher:
          anyOf:
            - type: string
            - type: 'null'
          title: Publisher
          description: Publisher of the publication.
          examples:
            - Elsevier
        section:
          anyOf:
            - type: string
            - type: 'null'
          title: Section
          description: Publication section in which citation statement appears.
        sections:
          items:
            type: string
          type: array
          title: Sections
          default: []
        paperType:
          anyOf:
            - type: string
            - type: 'null'
          title: Papertype
          description: Publication type.
        paperTypes:
          items:
            type: string
          type: array
          title: Papertypes
          default: []
        affiliation:
          anyOf:
            - type: string
            - type: 'null'
          title: Affiliation
          description: Author affiliation.
          examples:
            - Stanford University
        affiliations:
          items:
            type: string
          type: array
          title: Affiliations
          default: []
        topic:
          anyOf:
            - type: string
            - type: 'null'
          title: Topic
          description: Publication topic.
          examples:
            - Diplomacy
        topics:
          items:
            type: string
          type: array
          title: Topics
          default: []
        substances:
          items:
            type: string
          type: array
          title: Substances
          description: Pubchem substance canonical name.
          default: []
          examples:
            - - Bromantane
        meshType:
          items:
            type: string
          type: array
          title: Meshtype
          description: Pubmed mesh descriptor and/or qualifier for publication.
          default: []
        dashboardSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Dashboardslug
        dashboardDoiSource:
          anyOf:
            - type: string
              enum:
                - manual
                - search
            - type: 'null'
          title: Dashboarddoisource
          description: >-
            For a dashboard search, restrict results to manually-added papers
            ('manual') or search-result papers ('search'). Defaults to all
            papers in the collection.
        computeAggregations:
          type: boolean
          title: Computeaggregations
          description: >-
            For a given search query, this flag will control whether counts are
            computed and returned for the possible aggregations.
          default: false
        aggregations:
          items:
            type: string
            enum:
              - authors
              - affiliations
              - paper_types
              - journals
              - topics
              - substances
              - mesh_descriptors
              - editorial_notices
              - date_histogram_tally
              - max_date
              - min_date
          type: array
          title: Aggregations
          description: >-
            List of aggregation types to compute counts for. Only used if
            `compute_aggregations` is true.
          default:
            - authors
            - affiliations
            - paper_types
            - journals
            - editorial_notices
            - date_histogram_tally
            - topics
            - mesh_descriptors
            - substances
            - max_date
            - min_date
          examples:
            - - authors
              - journals
        aggregationsOptions:
          type: string
          title: Aggregationsoptions
          default: ''
      type: object
      title: QuerySchemaV2
    DashboardComponentLayoutSchema:
      properties:
        _id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        components:
          items:
            $ref: '#/components/schemas/DashboardComponent'
          type: array
          title: Components
      type: object
      required:
        - components
      title: DashboardComponentLayoutSchema
    DashboardDoiQuerySchema:
      properties:
        queryType:
          anyOf:
            - type: string
              enum:
                - list
                - saved_search
            - type: 'null'
          title: Querytype
        query:
          anyOf:
            - $ref: '#/components/schemas/DashboardManualListQuerySchema'
            - $ref: '#/components/schemas/DashboardSavedSearchQuerySchema'
          title: Query
      type: object
      required:
        - query
      title: DashboardDoiQuerySchema
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
    DashboardComponent:
      properties:
        _id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        name:
          type: string
          title: Name
        width:
          anyOf:
            - type: integer
            - type: 'null'
          title: Width
      type: object
      required:
        - name
      title: DashboardComponent
    DashboardManualListQuerySchema:
      properties:
        dois:
          items:
            type: string
          type: array
          title: Dois
      type: object
      required:
        - dois
      title: DashboardManualListQuerySchema
    DashboardSavedSearchQuerySchema:
      properties:
        saved_search_id:
          type: integer
          title: Saved Search Id
        doi_exclude_list:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Doi Exclude List
        dois:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Dois
      type: object
      required:
        - saved_search_id
      title: DashboardSavedSearchQuerySchema
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
