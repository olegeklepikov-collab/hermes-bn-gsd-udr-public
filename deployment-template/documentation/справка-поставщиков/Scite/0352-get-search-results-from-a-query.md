> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: get-search-results-from-a-query

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get search results from a query

> Search publication metadata and citation statements with Boolean terms, filters, sorting, pagination, and optional aggregations. Citation snippet text is hidden on self-service keys.



## OpenAPI

````yaml /openapi.json get /api_partner/search
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
  /api_partner/search:
    get:
      tags:
        - Search
      summary: Get search results from a query
      description: >-
        Search publication metadata and citation statements with Boolean terms,
        filters, sorting, pagination, and optional aggregations. Citation
        snippet text is hidden on self-service keys.
      operationId: searchPublications
      parameters:
        - name: format
          in: query
          required: false
          schema:
            enum:
              - json
              - csv
              - ris
            type: string
            description: Result format.
            examples:
              - csv
            default: json
            title: Format
          description: Result format.
        - name: term
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Cross-field search term. Can be left blank.
            default: ''
            title: Term
          description: Cross-field search term. Can be left blank.
        - name: mode
          in: query
          required: false
          schema:
            enum:
              - all
              - citations
              - papers
              - question-answering
            type: string
            description: Select search mode, see above.
            default: all
            title: Mode
          description: Select search mode, see above.
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            description: How many results to fetch. Up to 10,000 can be fetched at once.
            default: 10
            title: Limit
          description: How many results to fetch. Up to 10,000 can be fetched at once.
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            description: Can be used for pagination in combination with `limit`.
            default: 0
            title: Offset
          description: Can be used for pagination in combination with `limit`.
        - name: sort
          in: query
          required: false
          schema:
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
            description: >-
              How the results should be sorted. Leave blank for generic query
              'relevance'.
            title: Sort
          description: >-
            How the results should be sorted. Leave blank for generic query
            'relevance'.
        - name: sort_order
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                enum:
                  - asc
                  - desc
              - type: 'null'
            description: Result sort order for selected sort.
            title: Sort Order
          description: Result sort order for selected sort.
        - name: title
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Match text in publication title.
            title: Title
          description: Match text in publication title.
        - name: abstract
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Match text in publication abstract.
            title: Abstract
          description: Match text in publication abstract.
        - name: doi
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: >-
              Scope the search to a single DOI (exact match). Convenience alias
              for a one-element `dois`. Combine with `term` to search within a
              known publication.
            title: Doi
          description: >-
            Scope the search to a single DOI (exact match). Convenience alias
            for a one-element `dois`. Combine with `term` to search within a
            known publication.
        - name: dois
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
            description: >-
              Scope the search to one or more specific DOIs (exact match).
              Combine with `term` to search within a known publication.
            default: []
            title: Dois
          description: >-
            Scope the search to one or more specific DOIs (exact match). Combine
            with `term` to search within a known publication.
        - name: date_from
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: >-
              Match publications published from this date onwards (YYYY-MM-DD or
              just YYYY).
            title: Date From
          description: >-
            Match publications published from this date onwards (YYYY-MM-DD or
            just YYYY).
        - name: date_to
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: >-
              Match publications published up to this date (YYYY-MM-DD or just
              YYYY).
            title: Date To
          description: >-
            Match publications published up to this date (YYYY-MM-DD or just
            YYYY).
        - name: citation_types
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
              enum:
                - supporting
                - contrasting
                - mentioning
            description: Match smart citations of certain types.
            default: []
            title: Citation Types
          description: Match smart citations of certain types.
        - name: has_retraction
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: Publication has retraction or not.
            title: Has Retraction
          description: Publication has retraction or not.
        - name: has_concern
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: Publication has editorial concern or not.
            title: Has Concern
          description: Publication has editorial concern or not.
        - name: has_correction
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: Publication has correction or not.
            title: Has Correction
          description: Publication has correction or not.
        - name: has_erratum
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: Publication has erratum or not.
            title: Has Erratum
          description: Publication has erratum or not.
        - name: has_withdrawn
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: Publication has been withdrawn or not.
            title: Has Withdrawn
          description: Publication has been withdrawn or not.
        - name: has_tally
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: >-
              Publication has smart citations made towards it or not (i.e. a
              Scite tally of > 0).
            title: Has Tally
          description: >-
            Publication has smart citations made towards it or not (i.e. a Scite
            tally of > 0).
        - name: supporting_from
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of supporting citations made from publication. Leave blank
              for any count.
            title: Supporting From
          description: >-
            Number of supporting citations made from publication. Leave blank
            for any count.
        - name: supporting_to
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of supporting citations made toward publication. Leave
              blank for any count.
            title: Supporting To
          description: >-
            Number of supporting citations made toward publication. Leave blank
            for any count.
        - name: mentioning_from
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of mentioning citations made from publication. Leave blank
              for any count.
            title: Mentioning From
          description: >-
            Number of mentioning citations made from publication. Leave blank
            for any count.
        - name: mentioning_to
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of mentioning citations made toward publication. Leave
              blank for any count.
            title: Mentioning To
          description: >-
            Number of mentioning citations made toward publication. Leave blank
            for any count.
        - name: contrasting_from
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of contrasting citations made from publication. Leave blank
              for any count.
            title: Contrasting From
          description: >-
            Number of contrasting citations made from publication. Leave blank
            for any count.
        - name: contrasting_to
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of contrasting citations made toward publication. Leave
              blank for any count.
            title: Contrasting To
          description: >-
            Number of contrasting citations made toward publication. Leave blank
            for any count.
        - name: citing_publications_from
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of traditional citations made from publication AKA the
              number of references. Leave blank for any count.
            title: Citing Publications From
          description: >-
            Number of traditional citations made from publication AKA the number
            of references. Leave blank for any count.
        - name: citing_publications_to
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Number of traditional citations made toward publication. Leave
              blank for any count.
            title: Citing Publications To
          description: >-
            Number of traditional citations made toward publication. Leave blank
            for any count.
        - name: author
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Publication author name.
            title: Author
          description: Publication author name.
        - name: authors
          in: query
          required: false
          schema:
            items:
              type: string
            type: array
            title: Authors
            default: []
        - name: journal
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Journal in which publication appears.
            title: Journal
          description: Journal in which publication appears.
        - name: journals
          in: query
          required: false
          schema:
            items:
              type: string
            type: array
            title: Journals
            default: []
        - name: publisher
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Publisher of the publication.
            title: Publisher
          description: Publisher of the publication.
        - name: section
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Section
            description: Publication section in which citation statement appears.
          description: Publication section in which citation statement appears.
        - name: sections
          in: query
          required: false
          schema:
            items:
              type: string
            type: array
            title: Sections
            default: []
        - name: paper_type
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Publication type.
            title: Paper Type
          description: Publication type.
        - name: paper_types
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
            default: []
            title: Paper Types
        - name: affiliation
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Author affiliation.
            title: Affiliation
          description: Author affiliation.
        - name: affiliations
          in: query
          required: false
          schema:
            items:
              type: string
            type: array
            title: Affiliations
            default: []
        - name: topic
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Publication topic.
            title: Topic
          description: Publication topic.
        - name: topics
          in: query
          required: false
          schema:
            items:
              type: string
            type: array
            title: Topics
            default: []
        - name: substances
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
            description: Pubchem substance canonical name.
            default: []
            title: Substances
          description: Pubchem substance canonical name.
        - name: mesh_type
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
            description: Pubmed mesh descriptor and/or qualifier for publication.
            default: []
            title: Mesh Type
          description: Pubmed mesh descriptor and/or qualifier for publication.
        - name: compute_aggregations
          in: query
          required: false
          schema:
            type: boolean
            description: >-
              For a given search query, this flag will control whether counts
              are computed and returned for the possible aggregations.
            default: false
            title: Compute Aggregations
          description: >-
            For a given search query, this flag will control whether counts are
            computed and returned for the possible aggregations.
        - name: aggregations
          in: query
          required: false
          schema:
            type: array
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
            title: Aggregations
          description: >-
            List of aggregation types to compute counts for. Only used if
            `compute_aggregations` is true.
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
                $ref: '#/components/schemas/SearchResultsResponse'
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
    SearchResultsResponse:
      properties:
        count:
          type: integer
          title: Count
        countIsApproximate:
          type: boolean
          title: Countisapproximate
          default: false
        aggregations:
          $ref: '#/components/schemas/AggregationSchema'
        hits:
          items:
            $ref: '#/components/schemas/SearchResultSchema'
          type: array
          title: Hits
        suggestedTerm:
          anyOf:
            - type: string
            - type: 'null'
          title: Suggestedterm
        restrictedCites:
          type: boolean
          title: Restrictedcites
          default: false
      type: object
      required:
        - count
        - aggregations
        - hits
      title: SearchResultsResponse
      example:
        aggregations:
          affiliations: []
          authors: []
          dateHistogram: []
          editorialNotices: []
          journals: []
          meshDescriptors: []
          paperTypes: []
          substances: []
          topics: []
        count: 111787
        hits:
          - abstract: >-
              The ability to alter genomes specifically by <strong
              class="highlight">CRISPR</strong>-Cas gene editing has
              revolutionized biological research, biotechnology, and medicine.
              Broad therapeutic application of this technology, however, will
              require thorough preclinical assessment of off-target editing by
              homology-based prediction coupled with reliable methods for
              detecting off-target editing. Several off-target site nomination
              assays exist, but careful comparison is needed to ascertain their
              relative strengths and weaknesses. In this study, HEK293T cells
              were treated with
                   
                    Streptococcus pyogenes
                   
                   Cas9 and eight guide RNAs with varying levels of predicted promiscuity in order to compare the performance of three homology-independent off-target nomination methods: the cell-based assay, GUIDE-seq, and the biochemical assays CIRCLE-seq and SITE-seq. The three methods were benchmarked by sequencing 75,000 homology-nominated sites using hybrid capture followed by high-throughput sequencing, providing the most comprehensive assessment of such methods to date. The three methods performed similarly in nominating sequence-confirmed off-target sites, but with large differences in the total number of sites nominated. When combined with homology-dependent nomination methods and confirmation by sequencing, all three off-target nomination methods provide a comprehensive assessment of off-target activity. GUIDE-seq's low false-positive rate and the high correlation of its signal with observed editing highlight its suitability for nominating off-target sites for
                   
                    ex vivo
                   
                   <strong class="highlight">CRISPR</strong>-Cas therapies.
            authors:
              - authorName: Nicole Flanagan
                authorSequenceNumber: '5'
                authorSlug: nicole-flanagan-RVyDAMN
              - authorName: Maria C Lei Zhang
                authorSequenceNumber: '6'
                authorSlug: maria-c-lei-zhang-K6bjW3p
              - authorName: John D Kulman
                authorSequenceNumber: '13'
                authorSlug: john-d-kulman-9O8j4OG
              - authorName: Andrew Kernytsky
                authorSequenceNumber: '15'
                authorSlug: andrew-kernytsky-VKLdVO
              - authorName: Elaine Huang
                authorSequenceNumber: '7'
                authorSlug: elaine-huang-dvv0pd9
              - authorName: Aditya S Khedkar
                authorSequenceNumber: '8'
                authorSlug: aditya-s-khedkar-XxaxLDE
              - authorName: J Mike Toomey
                authorSequenceNumber: '9'
                authorSlug: j-mike-toomey-mOPAr62
              - authorName: Courtney A Shearer
                authorSequenceNumber: '10'
                authorSlug: courtney-a-shearer-D1MV3Lw
              - authorName: Alexander W Needham
                authorSequenceNumber: '11'
                authorSlug: alexander-w-needham-EWmRZnP
              - authorName: Tony W. Ho
                authorSequenceNumber: '12'
                authorSlug: tony-w-ho-mG9vLj
              - affiliation: CRISPR Therapeutics
                affiliationSlug: crispr-therapeutics-XegjD
                authorName: Hemangi G. Chaudhari
                authorSequenceNumber: '1'
                authorSlug: hemangi-g-chaudhari-ePLGRZ
              - authorName: Thomas J. Cradick
                authorSequenceNumber: '14'
                authorSlug: thomas-j-cradick-4YpK8P
              - affiliation: TScan Therapeutics
                affiliationSlug: tscan-therapeutics-j6D0l
                authorName: Holly J Whitton
                authorSequenceNumber: '3'
                authorSlug: holly-j-whitton-68br3jp
              - affiliation: CRISPR Therapeutics
                affiliationSlug: crispr-therapeutics-XegjD
                authorName: Jon Penterman
                authorSequenceNumber: '2'
                authorSlug: jon-penterman-ke5XYw3
              - affiliation: CRISPR Therapeutics
                affiliationSlug: crispr-therapeutics-XegjD
                authorName: Sarah J Spencer
                authorSequenceNumber: '4'
                authorSlug: sarah-j-spencer-MVEyDLY
            citations:
              - id: 2369710504
                lang: en
                langConfidence: 0.8899999856948853
                negative: 0.015631215646862984
                neutral: 1
                positive: 0.018351007252931595
                refLocation: b2/1
                section: introduction
                selfCites: []
                snippet: >-
                  The development of engineered nucleases that target specific
                  sites in the genome has driven advances in basic and applied
                  research at a rapid pace. <cite
                  data-doi="10.1126/science.1225829"> 1 </cite> , <cite
                  data-doi="10.1038/mtna.2011.5"> 2 </cite> The more recent
                  advent of facile <strong class="highlight">CRISPR</strong>-Cas
                  methods for programmable RNA-guided genome editing has further
                  quickened the pace of both discovery and clinical application.
                  <cite
                  data-doi="https://doi.org/10.1146/annurev-pharmtox-010814-124454">
                  3 </cite> , <cite data-doi="10.1016/j.omtm.2019.02.008"> 4
                  </cite> The Cas9 nuclease, in combination with a chimeric
                  guide RNA (gRNA), cleaves genomic sites in a sequence-specific
                  manner.
                snippetHidden: false
                source: 10.1089/crispr.2020.0053
                target: 10.1038/mtna.2011.5
                type: mentioning
                typeConfidence: 1
            date: '2020-12-01'
            doi: 10.1089/crispr.2020.0053
            editorialNotices:
              - date: 2020-12-1
                doi: 10.1089/crispr.2020.0053
                noticeDoi: 10.1089/crispr.2020.29116.smi
                status: Comment
              - date: 2021-2-1
                doi: 10.1089/crispr.2020.0053
                noticeDoi: 10.1089/crispr.2020.0053.correx
                status: Has erratum
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2020.0053
            issns:
              - 2573-1599
              - 2573-1602
            issue: '6'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1621320453
            meshTypes:
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000379
                qualifierName: methods
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000639
                qualifierName: trends
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000941
                qualifierName: ethics
              - descriptorId: D064113
                descriptorName: CRISPR-Cas Systems
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D015894
                descriptorName: Genome, Human
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D042822
                descriptorName: Genomic Instability
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D059014
                descriptorName: High-Throughput Nucleotide Sequencing
                qualifierId: Q000379
                qualifierName: methods
              - descriptorId: D017394
                descriptorName: RNA, Guide
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D013297
                descriptorName: Streptococcus pyogenes
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D013297
                descriptorName: Streptococcus pyogenes
                qualifierId: Q000472
                qualifierName: pathogenicity
            normalizedTypes:
              - research support, non-u.s. gov't
              - article
            page: 440-453
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: evaluation-of-homology-independent-crispr-cas9-off-target-8G5M9DL9
            tally:
              citingPublications: 13
              contradicting: 0
              mentioning: 9
              supporting: 0
              total: 9
              unclassified: 0
            title: >-
              Evaluation of Homology-Independent <strong
              class="highlight">CRISPR</strong>-Cas9 Off-Target Assessment
              Methods
            volume: '3'
            year: 2020
          - abstract: >-
              The constant selective pressure exerted by phages, the viruses
              that infect bacteria, has led to the evolution of a wide range of
              anti-phage defenses. One of these defense mechanisms, <strong
              class="highlight">CRISPR</strong>-Cas, provides an adaptive immune
              system to battle phage infection and inhibit horizontal gene
              transfer by plasmids, transposons, and other mobile genetic
              elements. Although <strong class="highlight">CRISPR</strong>-Cas
              systems are widespread in bacteria and archaea, they appear to
              have minimal long-term evolutionary effects with respect to
              limiting horizontal gene transfer. One factor that may contribute
              to this may be the presence of potent inhibitors of <strong
              class="highlight">CRISPR</strong>-Cas systems, known as
              anti-<strong class="highlight">CRISPR</strong> proteins. Forty
              unique families of anti-<strong class="highlight">CRISPR</strong>
              proteins have been described to date. These inhibitors, which are
              active against both Class 1 and 2 <strong
              class="highlight">CRISPR</strong>-Cas systems, have a wide range
              of mechanisms of activity. Studies of these proteins have provided
              important insight into the evolutionary arms race between bacteria
              and phages, and have contributed to the development of
              biotechnological tools that can be harnessed for control of
              <strong class="highlight">CRISPR</strong>-Cas genome editing.
            authors:
              - affiliation: University of Toronto
                affiliationSlug: university-of-toronto-xWjA
                authorName: Sungwon Hwang
                authorSequenceNumber: '1'
                authorSlug: sungwon-hwang-G35YWgb
              - affiliation: University of Toronto
                affiliationSlug: university-of-toronto-xWjA
                authorName: Karen L. Maxwell
                authorSequenceNumber: '2'
                authorSlug: karen-l-maxwell-RZvJNG
            citations:
              - id: 2187679880
                lang: en
                langConfidence: 0.8899999856948853
                negative: 0.03010692000389099
                neutral: 1
                positive: 0.02649279497563839
                refLocation: b27/4
                section: protein inhibitors of crispr-cas systems 27
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0052
                target: 10.1016/j.cell.2017.07.037
                type: mentioning
                typeConfidence: 1
              - id: 2187679811
                lang: en
                langConfidence: 0.9300000071525574
                negative: 0.009289187192916869
                neutral: 1
                positive: 0.012535284273326397
                refLocation: b7/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0052
                target: 10.1038/nature11723
                type: mentioning
                typeConfidence: 1
              - id: 2187679834
                lang: en
                langConfidence: 0.8999999761581421
                negative: 0.0020255858078598974
                neutral: 1
                positive: 0.0019376501441001892
                refLocation: b23/1
                section: probing for additional anti-crisprs
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0052
                target: 10.1089/crispr.2018.0043
                type: mentioning
                typeConfidence: 1
            date: '2019-02-01'
            doi: 10.1089/crispr.2018.0052
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2018.0052
            issns:
              - 2573-1599
              - 2573-1602
            issue: '1'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1614211293
            meshTypes:
              - descriptorId: D001105
                descriptorName: Archaea
                qualifierId: Q000821
                qualifierName: virology
              - descriptorId: D001419
                descriptorName: Bacteria
                qualifierId: Q000821
                qualifierName: virology
              - descriptorId: D001435
                descriptorName: Bacteriophages
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D017105
                descriptorName: Pseudomonas Phages
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D014764
                descriptorName: Viral Proteins
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D001105
                descriptorName: Archaea
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D001105
                descriptorName: Archaea
                qualifierId: Q000276
                qualifierName: immunology
              - descriptorId: D001419
                descriptorName: Bacteria
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D001419
                descriptorName: Bacteria
                qualifierId: Q000276
                qualifierName: immunology
              - descriptorId: D001435
                descriptorName: Bacteriophages
                qualifierId: Q000378
                qualifierName: metabolism
              - descriptorId: D000076987
                descriptorName: CRISPR-Associated Protein 9
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D000076987
                descriptorName: CRISPR-Associated Protein 9
                qualifierId: Q000276
                qualifierName: immunology
              - descriptorId: D064112
                descriptorName: Clustered Regularly Interspaced Short Palindromic Repeats
                qualifierId: Q000276
                qualifierName: immunology
              - descriptorId: D019295
                descriptorName: Computational Biology
                qualifierId: Q000379
                qualifierName: methods
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000379
                qualifierName: methods
              - descriptorId: D010957
                descriptorName: Plasmids
                qualifierId: Q000378
                qualifierName: metabolism
              - descriptorId: D039002
                descriptorName: Prophages
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D039002
                descriptorName: Prophages
                qualifierId: Q000378
                qualifierName: metabolism
              - descriptorId: D017105
                descriptorName: Pseudomonas Phages
                qualifierId: Q000378
                qualifierName: metabolism
              - descriptorId: D014764
                descriptorName: Viral Proteins
                qualifierId: Q000378
                qualifierName: metabolism
            normalizedTypes:
              - article
              - review
            page: 23-30
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: meet-the-anti-crisprs-widespread-protein-A32PLdE
            tally:
              citingPublications: 57
              contradicting: 0
              mentioning: 52
              supporting: 0
              total: 52
              unclassified: 0
            title: >-
              Meet the Anti-<strong class="highlight">CRISPRs</strong>:
              Widespread Protein Inhibitors of <strong
              class="highlight">CRISPR</strong>-Cas Systems
            volume: '2'
            year: 2019
          - abstract: >-
              <strong class="highlight">CRISPR</strong>-Cas has proven to be the
              most versatile genetic tinkering system of our time, predominantly
              as a precision genome editing tool. Here, we demonstrate two
              additions to the repertoire of <strong
              class="highlight">CRISPR's</strong> application for constructing
              donor DNA templates: <strong
              class="highlight">CRISPR</strong>-CLONInG and <strong
              class="highlight">CRISPR</strong>-CLIP. <strong
              class="highlight">CRISPR</strong>-CLONInG (<strong
              class="highlight">CRISPR</strong>-Cutting and Ligation Of Nucleic
              acid In vitro via Gibson) was devised to enable efficient
              cut-and-paste of multiple complex DNA fragments by using <strong
              class="highlight">CRISPR</strong>-Cas9 as a digestion alternative
              with precision and exclusivity features, followed by joining the
              digested products via Gibson Assembly, to construct
              double-stranded DNA and adeno-associated virus (AAV) donor vectors
              rapidly without cloning scars. <strong
              class="highlight">CRISPR</strong>-CLIP (<strong
              class="highlight">CRISPR</strong>-Clipped Long ssDNA via Incising
              Plasmid) was devised as a DNA clipping tool to retrieve long
              single-stranded DNA (lssDNA) efficiently from plasmid, up to 3.5
              kbase, which can be supplied as the donor template for creating
              genetically engineered mice via Easi-<strong
              class="highlight">CRISPR</strong>. We utilized two different Cas
              types (Cpf1 and Cas9n) to induce two distinct incisions at the
              respective ends of the lssDNA cassette junctions on the plasmid,
              yielding three independent single-stranded DNA units of unique
              sizes eligible for strand separation, followed by target strand
              clip-out through gel extraction. The retrieval of the lssDNA donor
              circumvents involvements of restriction enzymes and DNA
              polymerase-based steps. Hence, it not only retains sequence
              fidelity but also carries virtually no restriction on sequence
              composition, further mitigating limitations on the current
              Easi-<strong class="highlight">CRISPR</strong> method. With the
              add-on feature of universal DNA-tag sequences of Cpf1-Cas9 duo
              protospacer adjacent motif, <strong
              class="highlight">CRISPR</strong>-CLIP can be facile and
              applicable to generate lssDNA templates for any genomic target of
              choice. Additionally, we demonstrate robust gene editing
              efficiencies in the neuroblastoma cell line, as well as in mice
              attained with the AAV and lssDNA donors constructed herein.
            authors:
              - affiliation: Rockefeller University
                affiliationSlug: rockefeller-university-n6RX
                authorName: Dorjee T.N. Shola
                authorSequenceNumber: '1'
                authorSlug: dorjee-t-n-shola-K6PxwWe
              - affiliation: Rockefeller University
                affiliationSlug: rockefeller-university-n6RX
                authorName: Chingwen Yang
                authorSequenceNumber: '2'
                authorSlug: chingwen-yang-XjPX2D
              - affiliation: Rockefeller University
                affiliationSlug: rockefeller-university-n6RX
                authorName: Vhy-Shelta Kewaldar
                authorSequenceNumber: '3'
                authorSlug: vhy-shelta-kewaldar-3nvp5wd
              - affiliation: Rockefeller University
                affiliationSlug: rockefeller-university-n6RX
                authorName: Pradip Kar
                authorSequenceNumber: '4'
                authorSlug: pradip-kar-V0W1a0W
              - affiliation: Rockefeller University
                affiliationSlug: rockefeller-university-n6RX
                authorName: Victor Bustos
                authorSequenceNumber: '5'
                authorSlug: victor-bustos-9RmVeb
            citations:
              - id: 2062798832
                lang: en
                langConfidence: 0.9300000071525574
                negative: 0.010288532450795173
                neutral: 1
                positive: 0.008860928937792778
                refLocation: b9/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2019.0062
                target: 10.1038/ncomms10431
                type: mentioning
                typeConfidence: 1
              - id: 2062798824
                lang: en
                langConfidence: 0.8700000047683716
                negative: 0.0035790209658443928
                neutral: 1
                positive: 0.0031804069876670837
                refLocation: b0/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2019.0062
                target: 10.1126/science.1225829
                type: mentioning
                typeConfidence: 1
              - id: 2062798828
                lang: en
                langConfidence: 0.9100000262260437
                negative: 0.009582705795764923
                neutral: 1
                positive: 0.007374918088316917
                refLocation: b5/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2019.0062
                target: 10.1126/science.1232033
                type: mentioning
                typeConfidence: 1
            date: '2020-04-01'
            doi: 10.1089/crispr.2019.0062
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2019.0062
            issns:
              - 2573-1599
              - 2573-1602
            issue: '2'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1653308316
            meshTypes:
              - descriptorId: D064113
                descriptorName: CRISPR-Cas Systems
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D003001
                descriptorName: Cloning, Molecular
                qualifierId: Q000379
                qualifierName: methods
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000379
                qualifierName: methods
              - descriptorId: D064112
                descriptorName: Clustered Regularly Interspaced Short Palindromic Repeats
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D004247
                descriptorName: DNA
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D004277
                descriptorName: DNA, Single-Stranded
                qualifierId: Q000235
                qualifierName: genetics
              - descriptorId: D010957
                descriptorName: Plasmids
                qualifierId: Q000235
                qualifierName: genetics
            normalizedTypes:
              - article
              - research support, non-u.s. gov't
            page: 109-122
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: new-additions-to-the-crispr-pn2mgzgQ
            tally:
              citingPublications: 4
              contradicting: 0
              mentioning: 2
              supporting: 0
              total: 2
              unclassified: 0
            title: >-
              New Additions to the <strong class="highlight">CRISPR</strong>
              Toolbox: <strong class="highlight">CRISPR</strong>-CLONInG and
              <strong class="highlight">CRISPR</strong>-CLIP for Donor
              Construction in Genome Editing
            volume: '3'
            year: 2020
          - abstract: >-
              The discovery of <strong class="highlight">CRISPR</strong> has
              revolutionized the field of genome engineering, but the potential
              of this technology is far from reaching its limits. In this
              review, we explore the broad range of applications of <strong
              class="highlight">CRISPR</strong> technology to highlight the
              rapid expansion of the field beyond gene editing alone. It has
              been demonstrated that <strong class="highlight">CRISPR</strong>
              technology can control gene expression, spatiotemporally image the
              genome in vivo, and detect specific nucleic acid sequences for
              diagnostics. In addition, new technologies are under development
              to improve <strong class="highlight">CRISPR</strong> quality
              controls for gene editing, thereby improving the reliability of
              these technologies for therapeutics and beyond. These are just
              some of the many <strong class="highlight">CRISPR</strong> tools
              that have been developed in recent years, and the toolbox
              continues to diversify.
            authors:
              - affiliation: University of Copenhagen
                affiliationSlug: university-of-copenhagen-d3k1
                authorName: Sarah Balderston
                authorSequenceNumber: '1'
                authorSlug: sarah-balderston-PQDRO4R
              - affiliation: University of Copenhagen
                affiliationSlug: university-of-copenhagen-d3k1
                authorName: Gabrielle Clouse
                authorSequenceNumber: '2'
                authorSlug: gabrielle-clouse-0agNzrP
              - affiliation: University of Copenhagen
                affiliationSlug: university-of-copenhagen-d3k1
                authorName: Juan-José Ripoll
                authorSequenceNumber: '3'
                authorSlug: juan-jose-ripoll-ZxJz18y
              - affiliation: University of Copenhagen
                affiliationSlug: university-of-copenhagen-d3k1
                authorName: Grace K Pratt
                authorSequenceNumber: '4'
                authorSlug: grace-k-pratt-JW0z31D
              - affiliation: Novo Nordisk
                affiliationSlug: novo-nordisk-KOwJ
                authorName: Giedrius Gasiunas
                authorSequenceNumber: '5'
                authorSlug: giedrius-gasiunas-PQek6V
              - affiliation: University of Copenhagen
                affiliationSlug: university-of-copenhagen-d3k1
                authorName: Jens-Ole Bock
                authorSequenceNumber: '6'
                authorSlug: jens-ole-bock-kZ62J6w
              - affiliation: Novo Nordisk
                affiliationSlug: novo-nordisk-KOwJ
                authorName: Eric P. Bennett
                authorSequenceNumber: '7'
                authorSlug: eric-p-bennett-6wwEM1
              - affiliation: University of Copenhagen
                affiliationSlug: university-of-copenhagen-d3k1
                authorName: Kiana Aran
                authorSequenceNumber: '8'
                authorSlug: kiana-aran-68aQNp
            citations:
              - id: 2493201676
                lang: en
                langConfidence: 0.8299999833106995
                negative: 0.009431590139865874
                neutral: 1
                positive: 0.009461314417421818
                refLocation: b121/1
                section: ''
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2020.0137
                target: 10.1016/j.cell.2016.02.054
                type: mentioning
                typeConfidence: 1
              - id: 2493201659
                lang: en
                langConfidence: 0.8199999928474426
                negative: 0.0028272774070501328
                neutral: 1
                positive: 0.004844860639423132
                refLocation: b113/1
                section: ''
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2020.0137
                target: 10.1038/s41467-018-07498-y
                type: mentioning
                typeConfidence: 1
              - id: 2493201661
                lang: en
                langConfidence: 0.8299999833106995
                negative: 0.012460177391767501
                neutral: 1
                positive: 0.012772923335433006
                refLocation: b115/1
                section: ''
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2020.0137
                target: 10.1126/science.aac6572
                type: mentioning
                typeConfidence: 1
            date: '2021-06-01'
            doi: 10.1089/crispr.2020.0137
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2020.0137
            issns:
              - 2573-1599
              - 2573-1602
            issue: '3'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1624946906
            meshTypes: []
            normalizedTypes:
              - research support, n.i.h., extramural
              - article
              - research support, u.s. gov't, non-p.h.s.
            page: 400-415
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: diversification-of-the-crispr-toolbox-LedVvaP5
            title: >-
              Diversification of the <strong class="highlight">CRISPR</strong>
              Toolbox: Applications of <strong
              class="highlight">CRISPR</strong>-Cas Systems Beyond Genome
              Editing
            volume: '4'
            year: 2021
          - abstract: >-
              Over the past two decades, developments in nextgeneration
              sequencing technologies have led a flourishing era of ''genome
              reading''. Recent <strong class="highlight">CRISPR</strong>-based
              editing technologies are the beginning of a ''genome editing''
              renaissance. <strong class="highlight">CRISPR</strong> sequences
              were first discovered by microbiologists, but since 2012-2013,
              scientists across numerous fields worldwide have been attracted by
              the potential of <strong class="highlight">CRISPR</strong>-Cas
              editing technologies as a versatile and accessible genome editing
              tool. A growing genome editing toolbox based on <strong
              class="highlight">CRISPR</strong> systems involving Cas9, Cas12,
              Cas13, base editors (BEs), and prime editors (PEs) is advancing
              research in agriculture, biology, biotechnology, and medicine.
              [1][2][3] China has established itself as one of leading nations
              in the <strong class="highlight">CRISPR</strong> revolution due to
              the immense scientific curiosity of the research community and
              generous support from the Chinese government, including heavy
              investment from central, provincial, and city governments in
              China. Both the National Natural Science Foundation of the central
              government and the Ministry of Science and Technology have
              approved multiple projects in various disciplines. In September
              2017, China launched the Committee of Genome Editing, Genetics
              Society of China, which became a platform for accessible
              communication and cooperation between scientists to accelerate the
              development of <strong class="highlight">CRISPR</strong> research
              and applications in China. At this annual workshop, scientists
              working in agriculture, basic research, biotechnology, and
              medicine shared their group's progress.
            authors:
              - affiliation: Chinese Academy of Sciences
                affiliationSlug: chinese-academy-of-sciences-k1lJ
                authorName: Caixia Gao
                authorSequenceNumber: '1'
                authorSlug: caixia-gao-rnWgAO
              - affiliation: Chinese Academy of Sciences
                affiliationSlug: chinese-academy-of-sciences-k1lJ
                authorName: Jia Chen
                authorSequenceNumber: '2'
                authorSlug: jia-chen-6Nnlr1
            citations:
              - id: 2493201788
                lang: en
                langConfidence: 0.9100000262260437
                negative: 0.01616244502365589
                neutral: 1
                positive: 0.018683597445487976
                refLocation: b4/1
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2021.29129.gao
                target: 10.1016/j.cell.2016.12.031
                type: mentioning
                typeConfidence: 1
              - id: 2493201807
                lang: en
                langConfidence: 0.8899999856948853
                negative: 0.015953593701124192
                neutral: 1
                positive: 0.01561760250478983
                refLocation: b25/1
                section: plant progress
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2021.29129.gao
                target: 10.1038/nbt.4202
                type: mentioning
                typeConfidence: 1
              - id: 2493201817
                lang: en
                langConfidence: 0.8999999761581421
                negative: 0.022968332469463348
                neutral: 1
                positive: 0.060677677392959595
                refLocation: b34/1
                section: animal models and clinical trials
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2021.29129.gao
                target: 10.1056/nejmoa1817426
                type: mentioning
                typeConfidence: 1
            date: '2021-06-01'
            doi: 10.1089/crispr.2021.29129.gao
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2021.29129.gao
            issns:
              - 2573-1599
              - 2573-1602
            issue: '3'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1624946906
            meshTypes: []
            normalizedTypes:
              - article
              - editorial
            page: 304-306
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: crispr-adventures-in-china-2NkOdG6D
            title: <strong class="highlight">CRISPR</strong> Adventures in China
            volume: '4'
            year: 2021
          - abstract: >-
              Over the past 8 years, the widespread adoption of <strong
              class="highlight">CRISPR</strong>-based technologies has fueled
              the global genome editing revolution. This platform is based on
              Cas molecular machines such as Cas9, Cas12, Cas13, as well as
              other <strong class="highlight">CRISPR</strong> effector proteins
              that are able to alter the genome, transcriptome, and epigenome of
              virtually any species. Technological improvements have rendered
              these tools more efficient and precise, and enabled functional
              diversification and specialization, as recently illustrated by the
              rise of base editing and the quickly growing demand for prime
              editing constructs. Here, we discuss the continued adoption of
              <strong class="highlight">CRISPR</strong> tools and constructs
              distributed by the nonprofit organization Addgene, highlight the
              trends in the global demand for the <strong
              class="highlight">CRISPR</strong> toolbox, and consider the
              widespread attitude changes around open sharing that are having a
              transformative effect on speeding up science.
            authors:
              - affiliation: North Carolina State University
                affiliationSlug: north-carolina-state-university-dv2b
                authorName: Rodolphe Barrangou
                authorSequenceNumber: '3'
                authorSlug: rodolphe-barrangou-1gjmnM
              - authorName: Caroline M LaManna
                authorSequenceNumber: '1'
                authorSlug: caroline-m-lamanna-n6l1meV
              - authorName: Brook Pyhtila
                authorSequenceNumber: '2'
                authorSlug: brook-pyhtila-G3lv041
            citations:
              - id: 2181110106
                lang: en
                langConfidence: 0.9599999785423279
                negative: 0.008461072482168675
                neutral: 1
                positive: 0.014807685278356075
                refLocation: b2/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2020.0075
                target: 10.1038/nbt.2177
                type: mentioning
                typeConfidence: 1
              - id: 2181110102
                lang: en
                langConfidence: 0.9300000071525574
                negative: 0.010484088957309722
                neutral: 1
                positive: 0.009676134213805199
                refLocation: b0/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2020.0075
                target: 10.1038/s41587-020-0561-9
                type: mentioning
                typeConfidence: 1
              - id: 2181110111
                lang: en
                langConfidence: 0.949999988079071
                negative: 0.01637991853058338
                neutral: 1
                positive: 0.017453733831644058
                refLocation: b0/5
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2020.0075
                target: 10.1038/s41587-020-0561-9
                type: mentioning
                typeConfidence: 1
            date: '2020-08-01'
            doi: 10.1089/crispr.2020.0075
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2020.0075
            issns:
              - 2573-1599
              - 2573-1602
            issue: '4'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1614211293
            meshTypes:
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000706
                qualifierName: statistics & numerical data
              - descriptorId: D000072669
                descriptorName: Gene Editing
                qualifierId: Q000639
                qualifierName: trends
            normalizedTypes:
              - article
            page: 248-252
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: sharing-the-crispr-toolbox-with-b2nDdzdk
            tally:
              citingPublications: 3
              contradicting: 0
              mentioning: 1
              supporting: 0
              total: 1
              unclassified: 0
            title: >-
              Sharing the <strong class="highlight">CRISPR</strong> Toolbox with
              an Expanding Community
            volume: '3'
            year: 2020
          - abstract: >-
              Despite the strong presence of Chinese scientists in
              genome-editing research, little attention has been paid to the
              legal, economic, and scientific development of patented <strong
              class="highlight">CRISPR</strong> technologies in China. In this
              study, we focus on <strong class="highlight">CRISPR</strong>
              patent documents from academic and industrial Chinese players to
              assess their positioning on this breakthrough technology. We
              review the fields of application and the <strong
              class="highlight">CRISPR</strong> components claimed in the
              relevant patent documents. Our results show different profiles
              observed for academic or industrial assignees. Most of the patent
              families in our data set cover applications in genome editing and
              nucleic-acid detection for human therapeutic and diagnostic
              purposes. Trends in the patent data since 2014 confirm that China'
              R&amp;D has rapidly developed a significant <strong
              class="highlight">CRISPR</strong> patent landscape of its own,
              covering a diverse range of systems and applications. These recent
              developments deserve closer scrutiny from the international
              <strong class="highlight">CRISPR</strong> community.
            authors:
              - authorName: Fabien Palazzoli
                authorSequenceNumber: '3'
                authorSlug: fabien-palazzoli-QEbNrQ
              - authorName: Solenne Bire
                authorSequenceNumber: '1'
                authorSlug: solenne-bire-8A25pQ
              - authorName: Corinne Le Buhan
                authorSequenceNumber: '2'
                authorSlug: corinne-le-buhan-pxY89AQ
            citations:
              - id: 2493201751
                lang: en
                langConfidence: 0.8999999761581421
                negative: 0.037576666474342345
                neutral: 1
                positive: 0.007451415061950684
                refLocation: b23/1
                section: distribution of international patent application extensions
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2021.0020
                target: 10.1007/s15010-020-01554-w
                type: mentioning
                typeConfidence: 1
              - id: 2493201750
                lang: en
                langConfidence: 0.9300000071525574
                negative: 0.0068170661106705666
                neutral: 1
                positive: 0.0075931367464363575
                refLocation: b17/1
                section: methods
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2021.0020
                target: 10.1038/s41587-019-0138-7
                type: mentioning
                typeConfidence: 1
              - id: 2493201748
                lang: en
                langConfidence: 0.9399999976158142
                negative: 0.030483537912368772
                neutral: 1
                positive: 0.031298160552978516
                refLocation: b1/2
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2021.0020
                target: 10.1126/science.1225829
                type: mentioning
                typeConfidence: 1
            date: '2021-06-01'
            doi: 10.1089/crispr.2021.0020
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2021.0020
            issns:
              - 2573-1599
              - 2573-1602
            issue: '3'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1624946906
            meshTypes: []
            normalizedTypes:
              - article
              - research support, non-u.s. gov't
            page: 339-349
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: the-crispr-patent-landscape-focus-n6KlMyxk
            tally:
              citingPublications: 1
              contradicting: 0
              mentioning: 3
              supporting: 0
              total: 3
              unclassified: 0
            title: >-
              The <strong class="highlight">CRISPR</strong> Patent Landscape:
              Focus on Chinese Researchers
            volume: '4'
            year: 2021
          - abstract: >-
              <strong class="highlight">CRISPR</strong> technology has
              dramatically changed scientists' ability to conduct research in
              medicine, biotechnology, and agriculture through faster, more
              efficient genome editing. A key driver of the technology's
              adoption is the easy, fast, and inexpensive access to vectors and
              the resulting next-generation tools by the nonprofit plasmid
              repository Addgene. Since 2013, Addgene has shipped over 100,000
              <strong class="highlight">CRISPR</strong> plasmids to more than 75
              countries worldwide. This pipeline of new technologies is enabling
              cutting-edge research to address the grand challenges of mankind.
            authors:
              - affiliation: North Carolina State University
                affiliationSlug: north-carolina-state-university-dv2b
                authorName: Caroline M LaManna
                authorSequenceNumber: '1'
                authorSlug: caroline-m-lamanna-n6l1meV
              - affiliation: North Carolina State University
                affiliationSlug: north-carolina-state-university-dv2b
                authorName: Rodolphe Barrangou
                authorSequenceNumber: '2'
                authorSlug: rodolphe-barrangou-1gjmnM
            citations:
              - id: 2311317903
                lang: en
                langConfidence: 0.9399999976158142
                negative: 0.013812662288546562
                neutral: 1
                positive: 0.019115913659334183
                refLocation: b4/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0022
                target: 10.1016/j.cell.2014.05.010
                type: mentioning
                typeConfidence: 1
              - id: 2311317900
                lang: en
                langConfidence: 0.9200000166893005
                negative: 0.00758434385061264
                neutral: 1
                positive: 0.007091222796589136
                refLocation: b1/1
                section: introduction
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0022
                target: 10.1038/nmicrobiol.2017.92
                type: mentioning
                typeConfidence: 1
              - id: 2311317905
                lang: en
                langConfidence: 0.949999988079071
                negative: 0.03981065154075623
                neutral: 1
                positive: 0.03066163882613182
                refLocation: b6/1
                section: democratizing crispr
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0022
                target: 10.1126/science.307.5717.1877a
                type: mentioning
                typeConfidence: 1
            date: '2018-06-01'
            doi: 10.1089/crispr.2018.0022
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2018.0022
            issns:
              - 2573-1599
              - 2573-1602
            issue: '3'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1614211293
            meshTypes: []
            normalizedTypes:
              - article
            page: 205-208
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: enabling-the-rise-of-a-OVdPEen
            tally:
              citingPublications: 17
              contradicting: 0
              mentioning: 8
              supporting: 0
              total: 8
              unclassified: 0
            title: >-
              Enabling the Rise of a <strong class="highlight">CRISPR</strong>
              World
            volume: '1'
            year: 2018
          - abstract: >-
              The <strong class="highlight">CRISPR</strong>-<strong
              class="highlight">CRISPR</strong>-associated (Cas) nuclease system
              offers the ability to perform unprecedented functional genetic
              experiments and the promise of therapy for a variety of genetic
              disorders. The understanding of factors contributing to <strong
              class="highlight">CRISPR</strong> targeting efficacy and
              specificity continues to evolve. As <strong
              class="highlight">CRISPR</strong> systems rely on Watson-Crick
              base pairing to ultimately mediate genomic cleavage, it logically
              follows that genetic variation would affect <strong
              class="highlight">CRISPR</strong> targeting by increasing or
              decreasing sequence homology at on-target and off-target sites or
              by altering protospacer adjacent motifs. Numerous efforts have
              been made to document the extent of human genetic variation, which
              can serve as resources to understand and mitigate the effect of
              genetic variation on <strong class="highlight">CRISPR</strong>
              targeting. Here, we review efforts to elucidate the effect of
              human genetic variation on <strong
              class="highlight">CRISPR</strong> targeting at on-target and
              off-target sites with considerations for laboratory experiments
              and clinical translation of <strong
              class="highlight">CRISPR</strong>-based therapies.
            authors:
              - affiliation: Harvard University
                affiliationSlug: harvard-university-NmzP
                authorName: Matthew C. Canver
                authorSequenceNumber: '1'
                authorSlug: matthew-c-canver-9OzG29
              - affiliation: Harvard University
                affiliationSlug: harvard-university-NmzP
                authorName: J. Keith Joung
                authorSequenceNumber: '2'
                authorSlug: j-keith-joung-1Z9dGV
              - affiliation: Harvard University
                affiliationSlug: harvard-university-NmzP
                authorName: Luca Pinello
                authorSequenceNumber: '3'
                authorSlug: luca-pinello-b2KgY6
            citations:
              - id: 2446950013
                lang: en
                langConfidence: 0.8799999952316284
                negative: 0.01042686626315117
                neutral: 1
                positive: 0.011256013065576553
                refLocation: b103/1
                section: alteration of the off-target landscape by genetic variation
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2017.0016
                target: 10.1001/jama.2015.287
                type: mentioning
                typeConfidence: 1
              - id: 2446949881
                lang: en
                langConfidence: 0.9100000262260437
                negative: 0.003670770954340696
                neutral: 1
                positive: 0.003853459842503071
                refLocation: b25/1
                section: human genetic variation
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2017.0016
                target: 10.1016/j.cell.2017.04.005
                type: mentioning
                typeConfidence: 1
              - id: 2446949997
                lang: en
                langConfidence: 0.800000011920929
                negative: 0.01579469069838524
                neutral: 1
                positive: 0.01340237632393837
                refLocation: b89/1
                section: alteration of the off-target landscape by genetic variation
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2017.0016
                target: 10.1016/j.molp.2015.06.001
                type: mentioning
                typeConfidence: 1
            date: '2018-04-01'
            doi: 10.1089/crispr.2017.0016
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2017.0016
            issns:
              - 2573-1599
              - 2573-1602
            issue: '2'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1620137337
            meshTypes: []
            normalizedTypes:
              - article
              - review
            page: 159-170
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: impact-of-genetic-variation-on-J12p0ED
            tally:
              citingPublications: 13
              contradicting: 0
              mentioning: 8
              supporting: 0
              total: 8
              unclassified: 0
            title: >-
              Impact of Genetic Variation on <strong
              class="highlight">CRISPR</strong>-Cas Targeting
            volume: '1'
            year: 2018
          - abstract: >-
              Abstract Student-centered practices, including student-focused
              research opportunities, enhance biology education and
              comprehension. One way to support student interest is through
              research opportunities in faculty laboratories. However,
              alternatives to traditional research apprenticeships are important
              for the inclusion of more undergraduate students in <strong
              class="highlight">CRISPR</strong>-Cas-based research. Student
              interest in <strong class="highlight">CRISPR</strong>-Cas
              technologies serves as a timely focal point for deepening
              undergraduate student engagement in biology courses. In this
              article, we describe some of the ongoing efforts to bring <strong
              class="highlight">CRISPR</strong>-Cas technology out of the
              classroom and into the teaching laboratory.

              IntroductionThe most effective biology teaching actively engages
              students in their classrooms and coursework through group-work,
              activities, and discussion, which all access higher-order thinking
              and problem-solving skills.
            authors:
              - affiliation: Western Washington University
                affiliationSlug: western-washington-university-vZeN
                authorName: Lina Dahlberg
                authorSequenceNumber: '1'
                authorSlug: lina-dahlberg-9OpEQYb
              - affiliation: Western Washington University
                affiliationSlug: western-washington-university-vZeN
                authorName: Anna M Groat Carmona
                authorSequenceNumber: '2'
                authorSlug: anna-m-groat-carmona-vJXwMjW
            citations:
              - id: 1026238417
                lang: en
                langConfidence: 0.9100000262260437
                negative: 0.0003956407424993813
                neutral: 1.0982242345809938
                positive: 0.0008117514313198626
                refLocation: b21/5
                section: measuring success
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0007
                target: 10.1038/nprot.2016.186
                type: mentioning
                typeConfidence: 1.0982242345809938
              - id: 1026238405
                lang: en
                langConfidence: 0.9200000166893005
                negative: 0.007233731634914874
                neutral: 1
                positive: 0.00824350118637085
                refLocation: b24/2
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0007
                target: 10.1002/bmb.21025
                type: mentioning
                typeConfidence: 1
              - id: 1026238385
                lang: en
                langConfidence: 0.8700000047683716
                negative: 0.01746259890496731
                neutral: 1
                positive: 0.017191654071211815
                refLocation: b5/1
                section: faculty research opportunities
                selfCites: []
                snippet: ''
                snippetHidden: true
                source: 10.1089/crispr.2018.0007
                target: 10.1002/sce.20173
                type: mentioning
                typeConfidence: 1
            date: '2018-04-01'
            doi: 10.1089/crispr.2018.0007
            editorialNotices: []
            highlightedFields:
              - journal
              - shortJournal
              - abstract
              - citations.snippet
              - title
            id: 10.1089/crispr.2018.0007
            issns:
              - 2573-1599
              - 2573-1602
            issue: '2'
            journal: The <strong Class="highlight">crispr</Strong> Journal
            lastUpdate: 1614211293
            meshTypes: []
            normalizedTypes:
              - article
            page: 107-114
            publisher: Mary Ann Liebert Inc
            shortJournal: The <strong class="highlight">CRISPR</strong> Journal
            slug: crispr-cas-technology-in-and-out-RVdWyv5
            tally:
              citingPublications: 12
              contradicting: 0
              mentioning: 10
              supporting: 0
              total: 10
              unclassified: 0
            title: >-
              <strong class="highlight">CRISPR</strong>-Cas Technology In and
              Out of the Classroom
            volume: '1'
            year: 2018
        restrictedCites: true
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AggregationSchema:
      properties:
        paperTypes:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Papertypes
        journals:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Journals
        topics:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Topics
        substances:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Substances
        meshDescriptors:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Meshdescriptors
        editorialNotices:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Editorialnotices
        authors:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Authors
        affiliations:
          items:
            $ref: '#/components/schemas/_AggregationBucketSchema'
          type: array
          title: Affiliations
        dateHistogram:
          items:
            $ref: '#/components/schemas/_DateBucket'
          type: array
          title: Datehistogram
        maxDate:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Maxdate
          description: Maximum Date
        minDate:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Mindate
          description: Minimum Date
      type: object
      title: AggregationSchema
    SearchResultSchema:
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
              format: date
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
      title: SearchResultSchema
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
    _AggregationBucketSchema:
      properties:
        key:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
          title: Key
        docCount:
          type: integer
          title: Doccount
        metadata:
          additionalProperties: true
          type: object
          title: Metadata
          default: {}
      type: object
      required:
        - key
        - docCount
      title: _AggregationBucketSchema
    _DateBucket:
      properties:
        docCount:
          type: integer
          title: Doccount
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
        date:
          type: string
          format: date
          title: Date
      type: object
      required:
        - docCount
        - total
        - supporting
        - contradicting
        - mentioning
        - unclassified
        - date
      title: _DateBucket
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
