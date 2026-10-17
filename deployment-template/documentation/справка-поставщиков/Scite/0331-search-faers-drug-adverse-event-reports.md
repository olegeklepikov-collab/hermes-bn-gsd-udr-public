> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: search-faers-drug-adverse-event-reports

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search FAERS drug adverse event reports

> Search FDA FAERS drug adverse-event reports with a free-text query, resource-specific field filters, sorting, and pagination. Call the corresponding schema endpoint to discover filterable and sortable fields. Requires the dataset's Evidence scope.



## OpenAPI

````yaml /openapi.json get /api_partner/evidence/faers
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
  /api_partner/evidence/faers:
    get:
      tags:
        - Evidence
      summary: Search FAERS drug adverse event reports
      description: >-
        Search FDA FAERS drug adverse-event reports with a free-text query,
        resource-specific field filters, sorting, and pagination. Call the
        corresponding schema endpoint to discover filterable and sortable
        fields. Requires the dataset's Evidence scope.
      operationId: searchFaersReports
      parameters:
        - name: q
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: >-
              Free-text query. Supports boolean operators (AND, OR, NOT) and
              phrase matching.
            title: Q
          description: >-
            Free-text query. Supports boolean operators (AND, OR, NOT) and
            phrase matching.
        - name: f
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: >-
              Space-delimited filters in `field:"value"` format. Facet fields:
              drug.medicinalproduct, drug.brand_name, drug.generic_name,
              drug.substance_name, drug.manufacturer_name, drug.route,
              drug.pharm_class_epc, drug.pharm_class_moa, drug.drugindication,
              reaction.reactionmeddrapt, reaction.reactionoutcome,
              event.reporttype, event.seriousness_type, event.occurcountry,
              event.patientsex, primarysource.qualification,
              primarysource.reportercountry. Date range fields:
              event.receivedate, event.receiptdate, event.transmissiondate,
              drug.drugstartdate, drug.drugenddate. Use gte/lt suffixes for
              ranges, e.g. event.receivedategte:"2024-01-01"
              event.receivedatelt:"2025-01-01".
            title: F
          description: >-
            Space-delimited filters in `field:"value"` format. Facet fields:
            drug.medicinalproduct, drug.brand_name, drug.generic_name,
            drug.substance_name, drug.manufacturer_name, drug.route,
            drug.pharm_class_epc, drug.pharm_class_moa, drug.drugindication,
            reaction.reactionmeddrapt, reaction.reactionoutcome,
            event.reporttype, event.seriousness_type, event.occurcountry,
            event.patientsex, primarysource.qualification,
            primarysource.reportercountry. Date range fields: event.receivedate,
            event.receiptdate, event.transmissiondate, drug.drugstartdate,
            drug.drugenddate. Use gte/lt suffixes for ranges, e.g.
            event.receivedategte:"2024-01-01" event.receivedatelt:"2025-01-01".
        - name: p
          in: query
          required: false
          schema:
            type: integer
            description: Page number (1-indexed)
            default: 1
            title: P
          description: Page number (1-indexed)
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
                $ref: '#/components/schemas/FaersSearchResponse'
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
    FaersSearchResponse:
      properties:
        totalResults:
          anyOf:
            - type: integer
            - type: 'null'
          title: Totalresults
        delay:
          anyOf:
            - type: number
            - type: 'null'
          title: Delay
        resultsPerPage:
          anyOf:
            - type: integer
            - type: 'null'
          title: Resultsperpage
        from:
          anyOf:
            - type: integer
            - type: 'null'
          title: From
        results:
          items:
            $ref: '#/components/schemas/FaersResult'
          type: array
          title: Results
      additionalProperties: true
      type: object
      title: FaersSearchResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    FaersResult:
      properties:
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
        dataset:
          anyOf:
            - type: string
            - type: 'null'
          title: Dataset
        uid:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        safetyreportid:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Safetyreportid
        title:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Title
        event:
          anyOf:
            - $ref: '#/components/schemas/FaersEvent'
            - type: 'null'
        drug:
          items:
            $ref: '#/components/schemas/FaersDrug'
          type: array
          title: Drug
        reportduplicate:
          items:
            $ref: '#/components/schemas/FaersReportDuplicate'
          type: array
          title: Reportduplicate
        primarysource:
          anyOf:
            - $ref: '#/components/schemas/FaersPrimarySource'
            - type: 'null'
        reaction:
          items:
            $ref: '#/components/schemas/FaersReaction'
          type: array
          title: Reaction
      additionalProperties: true
      type: object
      title: FaersResult
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
    FaersEvent:
      properties:
        authoritynumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        companynumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Companynumb
        duplicate:
          anyOf:
            - type: string
            - type: 'null'
          title: Duplicate
        fulfillexpeditecriteria:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        narrativeincludeclinical:
          anyOf:
            - type: string
            - type: 'null'
          title: Narrativeincludeclinical
        transmissiondate:
          anyOf:
            - type: string
            - type: 'null'
          title: Transmissiondate
        receiptdate:
          anyOf:
            - type: string
            - type: 'null'
          title: Receiptdate
        receivedate:
          anyOf:
            - type: string
            - type: 'null'
          title: Receivedate
        reporttype:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Reporttype
        safetyreportversion:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        serious:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Serious
        seriousnessType:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Seriousnesstype
        occurcountry:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        patientagegroup:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Patientagegroup
        patientonsetage:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Patientonsetage
        patientsex:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Patientsex
        patientweight:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Patientweight
        patientdeathdate:
          anyOf:
            - type: string
            - type: 'null'
          title: Patientdeathdate
      additionalProperties: true
      type: object
      title: FaersEvent
    FaersDrug:
      properties:
        drugauthorizationnumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        drugbatchnumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        applicationNumber:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Applicationnumber
        nui:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Nui
        productNdc:
          items:
            type: string
          type: array
          title: Productndc
        packageNdc:
          items:
            type: string
          type: array
          title: Packagendc
        rxcui:
          items:
            type: string
          type: array
          title: Rxcui
        splId:
          items:
            type: string
          type: array
          title: Splid
        splSetId:
          items:
            type: string
          type: array
          title: Splsetid
        unii:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Unii
        actiondrug:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Actiondrug
        activesubstancename:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        drugadministrationroute:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        drugcharacterization:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Drugcharacterization
        drugdosagetext:
          anyOf:
            - type: string
            - type: 'null'
          title: Drugdosagetext
        drugstartdate:
          anyOf:
            - type: string
            - type: 'null'
          title: Drugstartdate
        drugenddate:
          anyOf:
            - type: string
            - type: 'null'
          title: Drugenddate
        drugindication:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        drugseparatedosagenumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        drugstructuredosagenumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        drugtreatmentduration:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        medicinalproduct:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        brandName:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Brandname
        genericName:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Genericname
        manufacturerName:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Manufacturername
        route:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Route
        substanceName:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Substancename
        pharmClassCs:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Pharmclasscs
        pharmClassEpc:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Pharmclassepc
        pharmClassPe:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Pharmclasspe
        pharmClassMoa:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Pharmclassmoa
        productType:
          items:
            $ref: '#/components/schemas/FacetValue'
          type: array
          title: Producttype
      additionalProperties: true
      type: object
      title: FaersDrug
    FaersReportDuplicate:
      properties:
        duplicatenumb:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        duplicatesource:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
      additionalProperties: true
      type: object
      title: FaersReportDuplicate
    FaersPrimarySource:
      properties:
        literaturereference:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Literaturereference
        qualification:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        reportercountry:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
      additionalProperties: true
      type: object
      title: FaersPrimarySource
    FaersReaction:
      properties:
        reactionmeddrapt:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
        reactionmeddraversionpt:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: string
            - type: 'null'
          title: Reactionmeddraversionpt
        reactionoutcome:
          anyOf:
            - $ref: '#/components/schemas/FacetValue'
            - type: 'null'
      additionalProperties: true
      type: object
      title: FaersReaction
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
