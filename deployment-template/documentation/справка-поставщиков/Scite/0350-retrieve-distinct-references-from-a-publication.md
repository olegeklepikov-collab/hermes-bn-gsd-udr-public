> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: retrieve-distinct-references-from-a-publication

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve distinct references from a publication

> Gets distinct references from a given DOI.

Can also return relevant paper metadata and tallies for references.

Note that this endpoint requires an API token for usage.



## OpenAPI

````yaml /openapi.json get /api_partner/references/references_from/{doi}
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
  /api_partner/references/references_from/{doi}:
    get:
      tags:
        - References
      summary: Retrieve distinct references from a publication
      description: |-
        Gets distinct references from a given DOI.

        Can also return relevant paper metadata and tallies for references.

        Note that this endpoint requires an API token for usage.
      operationId: getReferencesFrom
      parameters:
        - name: doi
          in: path
          required: true
          schema:
            type: string
            title: Doi
        - name: papers
          in: query
          required: false
          schema:
            type: boolean
            description: Also fetch source paper metadata.
            default: false
            title: Papers
          description: Also fetch source paper metadata.
        - name: tallies
          in: query
          required: false
          schema:
            type: boolean
            description: Also fetch source tally metadata.
            default: false
            title: Tallies
          description: Also fetch source tally metadata.
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
                $ref: '#/components/schemas/ReferencesResponse'
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
    ReferencesResponse:
      properties:
        metadata:
          $ref: '#/components/schemas/ReferencesMetadataSchema'
        references:
          items:
            $ref: '#/components/schemas/sciteapi__models__reference__ReferenceSchema'
          type: array
          title: References
        tallies:
          anyOf:
            - additionalProperties:
                anyOf:
                  - $ref: '#/components/schemas/TallyDB'
                  - type: 'null'
              type: object
            - type: 'null'
          title: Tallies
        papers:
          anyOf:
            - additionalProperties:
                anyOf:
                  - $ref: '#/components/schemas/PaperResponse'
                  - type: 'null'
              type: object
            - type: 'null'
          title: Papers
      type: object
      required:
        - metadata
        - references
      title: ReferencesResponse
      example:
        metadata:
          totalReferenceCount: 45
        references:
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0959-4388(02)00301-x
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1111/j.1749-6632.2003.tb07091.x
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/j.cpr.2004.07.006
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0005-7967(03)00039-1
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/j.biopsych.2005.01.044
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1097/00001756-199804200-00048
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1038/nn1173
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0896-6273(00)80219-6
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s1364-6613(00)01483-2
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1176/appi.ajp.161.1.1
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0006-3223(01)01296-3
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1006/cbmr.1996.0014
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1097/00001756-200001170-00024
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0887-6185(00)00036-0
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1002/mrm.1910330508
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1017/s0033291701004056
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/j.neulet.2004.02.070
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1001/archpsyc.59.5.425
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0165-0270(02)00006-7
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1038/35094500
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1017/s0033291798007879
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/j.tips.2004.05.009
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1002/hipo.1113
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1007/s11920-003-0055-8
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1097/00001756-200108080-00050
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0304-3940(02)00965-5
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1176/appi.ajp.158.10.1558
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1006/nimg.2002.1087
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0006-3223(03)00171-9
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1002/1097-0193(200104)12:4<193::aid-hbm1015>3.0.co;2-a
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1002/(sici)1522-2594(199907)42:1<87::aid-mrm13>3.0.co;2-o
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0006-3223(98)00269-8
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1136/bmj.327.7414.515
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0006-3223(01)01263-x
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1001/archpsyc.62.3.273
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/j.biopsych.2004.01.007
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1001/archpsyc.59.11.1027
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1176/appi.ajp.157.10.1606
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1001/archpsyc.57.11.1046
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/j.biopsych.2004.09.024
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1176/appi.ajp.158.8.1220
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0006-3223(02)01396-3
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1038/nn816
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1097/00001756-200102120-00039
          - dataSource: CR
            selfCites: []
            source: 10.1016/j.biopsych.2005.08.012
            target: 10.1016/s0165-0173(02)00248-5
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ReferencesMetadataSchema:
      properties:
        totalReferenceCount:
          type: integer
          title: Totalreferencecount
        distinctSourceCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Distinctsourcecount
        restrictedReferenceCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Restrictedreferencecount
        isApproximate:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Isapproximate
        maxPaginationOffset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maxpaginationoffset
        dateHistogram:
          anyOf:
            - additionalProperties:
                additionalProperties:
                  type: integer
                type: object
              type: object
            - type: 'null'
          title: Datehistogram
        referencesCounts:
          anyOf:
            - $ref: '#/components/schemas/ReferencesFromCounts'
            - type: 'null'
        filteredCitationStatementsCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Filteredcitationstatementscount
      type: object
      required:
        - totalReferenceCount
      title: ReferencesMetadataSchema
    sciteapi__models__reference__ReferenceSchema:
      properties:
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        target:
          type: string
          title: Target
        createdAt:
          anyOf:
            - type: string
              format: date
            - type: 'null'
          title: Createdat
        lastUpdated:
          anyOf:
            - type: string
              format: date
            - type: 'null'
          title: Lastupdated
        selfCites:
          items:
            $ref: '#/components/schemas/SelfCiteSchema'
          type: array
          title: Selfcites
        dataSource:
          anyOf:
            - type: string
            - type: 'null'
          title: Datasource
        citationStatementCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Citationstatementcount
          description: Number of citation statements from source to this reference
      type: object
      required:
        - source
        - target
      title: ReferenceSchema
    TallyDB:
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
          type: string
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
        - doi
      title: TallyDB
      example:
        citingPublications: 436
        contradicting: 6
        doi: 10.1016/j.biopsych.2005.08.012
        mentioning: 308
        supporting: 27
        total: 347
        unclassified: 6
    PaperResponse:
      properties:
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        doi:
          type: string
          title: Doi
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
        title:
          anyOf:
            - type: string
            - type: 'null'
          title: Title
          default: Untitled
        abstract:
          anyOf:
            - type: string
            - type: 'null'
          title: Abstract
        authors:
          anyOf:
            - items:
                $ref: '#/components/schemas/AuthorSchema'
              type: array
            - type: 'null'
          title: Authors
        keywords:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Keywords
        year:
          anyOf:
            - type: integer
            - type: 'null'
          title: Year
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
        issue:
          anyOf:
            - type: string
            - type: 'null'
          title: Issue
        volume:
          anyOf:
            - type: string
            - type: 'null'
          title: Volume
        page:
          anyOf:
            - type: string
            - type: 'null'
          title: Page
        pmPublicationType:
          anyOf:
            - type: string
            - type: 'null'
          title: Pmpublicationtype
        retracted:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Retracted
        memberId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Memberid
        issns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Issns
        tally:
          anyOf:
            - $ref: '#/components/schemas/TallyDB'
            - type: 'null'
        citingTally:
          anyOf:
            - $ref: '#/components/schemas/CitingTallySourceDB'
            - type: 'null'
        editorialNotices:
          items:
            $ref: '#/components/schemas/EditorialNoticeSchema'
          type: array
          title: Editorialnotices
        journalSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Journalslug
        journal:
          anyOf:
            - type: string
            - type: 'null'
          title: Journal
        preprintLinks:
          items:
            $ref: '#/components/schemas/PreprintLinkSchema'
          type: array
          title: Preprintlinks
        publicationLinks:
          items:
            $ref: '#/components/schemas/PublicationLinkSchema'
          type: array
          title: Publicationlinks
        normalizedTypes:
          items:
            type: string
          type: array
          title: Normalizedtypes
      type: object
      required:
        - doi
      title: PaperResponse
      example:
        authors:
          - affiliation: University of Chicago
            affiliationID: '17898'
            affiliationSlug: university-of-chicago-6096
            authorID: '20073081'
            authorName: K. Luan Phan
            authorSequenceNumber: 1
            authorSlug: k-luan-phan-jz0xRV
            family: Phan
            given: K. Luan
          - affiliation: Wayne State University
            affiliationID: '11741'
            affiliationSlug: wayne-state-university-Xje9
            authorID: '14943755'
            authorName: Daniel A. Fitzgerald
            authorSequenceNumber: 2
            authorSlug: daniel-a-fitzgerald-e6pg3O
            family: Fitzgerald
            given: Daniel A.
          - affiliation: Monash University
            affiliationID: '6663'
            affiliationSlug: monash-university-DZee
            authorID: '15102805'
            authorName: Pradeep J. Nathan
            authorSequenceNumber: 3
            authorSlug: pradeep-j-nathan-Ax3j3L
            family: Nathan
            given: Pradeep J.
          - affiliation: Wayne State University
            affiliationID: '11741'
            affiliationSlug: wayne-state-university-Xje9
            authorID: '3534491'
            authorName: Manuel Tancer
            authorSequenceNumber: 4
            authorSlug: manuel-tancer-1O4Lj
            family: Tancer
            given: Manuel
        doi: 10.1016/j.biopsych.2005.08.012
        editorialNotices: []
        id: 66831114
        issns:
          - 0006-3223
        issue: '5'
        journal: Biological Psychiatry
        journalSlug: 5GzJD
        memberId: 78
        normalizedTypes:
          - article
        page: 424-429
        preprintLinks: []
        publicationLinks: []
        publisher: Elsevier BV
        retracted: false
        shortJournal: Biological Psychiatry
        slug: association-between-amygdala-hyperactivity-to-gVamGz
        title: >-
          Association between Amygdala Hyperactivity to Harsh Faces and Severity
          of Social Anxiety in Generalized Social Phobia
        type: journal-article
        volume: '59'
        year: 2006
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
    ReferencesFromCounts:
      properties:
        total:
          type: integer
          title: Total
        pubTypes:
          additionalProperties:
            type: integer
          type: object
          title: Pubtypes
        journals:
          additionalProperties:
            type: integer
          type: object
          title: Journals
        relationships:
          $ref: '#/components/schemas/RelationshipCounts'
        dateHistogram:
          additionalProperties:
            type: integer
          type: object
          title: Datehistogram
        authors:
          additionalProperties:
            type: integer
          type: object
          title: Authors
        sections:
          $ref: '#/components/schemas/SectionCounts'
        types:
          $ref: '#/components/schemas/TypeCounts'
      type: object
      required:
        - total
        - pubTypes
        - journals
        - relationships
        - dateHistogram
        - authors
        - sections
        - types
      title: ReferencesFromCounts
      description: Counts for filter sidebar when viewing references FROM a paper.
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
    AuthorSchema:
      properties:
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
        orcid:
          anyOf:
            - type: string
            - type: 'null'
          title: Orcid
        affiliation:
          anyOf:
            - type: string
            - type: 'null'
          title: Affiliation
        authorSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Authorslug
        authorName:
          anyOf:
            - type: string
            - type: 'null'
          title: Authorname
        authorID:
          anyOf:
            - type: string
            - type: 'null'
          title: Authorid
        authorLastKnownAffiliationId:
          anyOf:
            - type: integer
            - type: 'null'
          title: Authorlastknownaffiliationid
        authorSequenceNumber:
          anyOf:
            - type: integer
            - type: 'null'
          title: Authorsequencenumber
        affiliationSlug:
          anyOf:
            - type: string
            - type: 'null'
          title: Affiliationslug
        affiliationID:
          anyOf:
            - type: string
            - type: 'null'
          title: Affiliationid
      type: object
      title: AuthorSchema
    CitingTallySourceDB:
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
        sourceDoi:
          type: string
          title: Sourcedoi
        numCitedPublications:
          anyOf:
            - type: integer
            - type: 'null'
          title: Numcitedpublications
      type: object
      required:
        - total
        - supporting
        - contradicting
        - mentioning
        - unclassified
        - sourceDoi
      title: CitingTallySourceDB
      example:
        total: 317
        supporting: 24
        contradicting: 3
        mentioning: 290
        unclassified: 0
        sourceDoi: 10.1016/j.biopsych.2005.08.012
        numCitedPublications: 377
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
    PreprintLinkSchema:
      properties:
        preprintDoi:
          type: string
          title: Preprintdoi
      type: object
      required:
        - preprintDoi
      title: PreprintLinkSchema
    PublicationLinkSchema:
      properties:
        publishedDoi:
          type: string
          title: Publisheddoi
      type: object
      required:
        - publishedDoi
      title: PublicationLinkSchema
    RelationshipCounts:
      properties:
        selfCite:
          type: integer
          title: Selfcite
        independent:
          type: integer
          title: Independent
      type: object
      required:
        - selfCite
        - independent
      title: RelationshipCounts
    SectionCounts:
      properties:
        introduction:
          type: integer
          title: Introduction
        methods:
          type: integer
          title: Methods
        results:
          type: integer
          title: Results
        discussion:
          type: integer
          title: Discussion
        other:
          type: integer
          title: Other
      type: object
      required:
        - introduction
        - methods
        - results
        - discussion
        - other
      title: SectionCounts
    TypeCounts:
      properties:
        supporting:
          type: integer
          title: Supporting
        mentioning:
          type: integer
          title: Mentioning
        contradicting:
          type: integer
          title: Contradicting
        unclassified:
          type: integer
          title: Unclassified
      type: object
      required:
        - supporting
        - mentioning
        - contradicting
        - unclassified
      title: TypeCounts
      description: >-
        Counts of citation types (supporting, mentioning, contradicting,
        unclassified).
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
