> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: receive-citations-with-the-doi-as-a-target-paper

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive citations with the DOI as a target paper

> Get citations made toward a given DOI.

Can also return relevant paper metadata and tallies for citation sources.

Results can be filtered both by a list of source_dois and a list of
to limit output.

This endpoint requires an API token with special access. For
more information, please contact us at sales@scite.ai



## OpenAPI

````yaml /openapi.json get /api_partner/citations/citing/{doi}
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
  /api_partner/citations/citing/{doi}:
    get:
      tags:
        - Smart Citation Graph
      summary: Receive citations with the DOI as a target paper
      description: >-
        Get citations made toward a given DOI.


        Can also return relevant paper metadata and tallies for citation
        sources.


        Results can be filtered both by a list of source_dois and a list of

        to limit output.


        This endpoint requires an API token with special access. For

        more information, please contact us at sales@scite.ai
      operationId: getCitingPublications
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
        - name: limit
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Can be used in conjunction with offset to page through references
              if the total count exceeds 3,000.
            title: Limit
          description: >-
            Can be used in conjunction with offset to page through references if
            the total count exceeds 3,000.
        - name: offset
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: >-
              Can be used in conjunction with limit to page through references
              if the total count exceeds 3,000.
            title: Offset
          description: >-
            Can be used in conjunction with limit to page through references if
            the total count exceeds 3,000.
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
                $ref: '#/components/schemas/CitationsExternalSchema'
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
    CitationsExternalSchema:
      properties:
        tallies:
          anyOf:
            - additionalProperties:
                $ref: '#/components/schemas/TallyDB'
              type: object
            - type: 'null'
          title: Tallies
        papers:
          anyOf:
            - additionalProperties:
                $ref: '#/components/schemas/PaperResponse'
              type: object
            - type: 'null'
          title: Papers
        metadata:
          $ref: '#/components/schemas/CitationsMetadataSchema'
        citations:
          items:
            $ref: '#/components/schemas/CitationExternal'
          type: array
          title: Citations
      type: object
      required:
        - metadata
        - citations
      title: CitationsExternalSchema
      example:
        citations:
          - id: 2155776090
            memberId: 78
            negative: 0.9638307094573975
            neutral: 0.18200477659702302
            positive: 0.03134886920452118
            section: discussion
            selfCites:
              - family: Ren
                given: Ping
                type: SHAREDAUTHOR
              - family: Lin
                given: Feng
                type: SHAREDAUTHOR
            source: 10.1016/j.nicl.2018.07.021
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: contradicting
            typeConfidence: 0.9638307094573975
          - id: 2155776097
            memberId: 78
            negative: 0.8688214302062988
            neutral: 0.15333953052759172
            positive: 0.13658252358436584
            section: discussion
            selfCites:
              - family: Ren
                given: Ping
                type: SHAREDAUTHOR
              - family: Lin
                given: Feng
                type: SHAREDAUTHOR
            source: 10.1016/j.nicl.2018.07.021
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: contradicting
            typeConfidence: 0.8688214302062988
          - id: 2824334878
            memberId: 276
            negative: 0.1359453946352005
            neutral: 0.7094927668571472
            positive: 0.24171872437000275
            section: discussion
            selfCites: []
            source: 10.1097/wad.0000000000000494
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 0.7094927668571472
          - id: 2155776098
            memberId: 78
            negative: 0.26392486095428463
            neutral: 0.817299246788025
            positive: 0.03706328198313713
            section: discussion
            selfCites:
              - family: Ren
                given: Ping
                type: SHAREDAUTHOR
              - family: Lin
                given: Feng
                type: SHAREDAUTHOR
            source: 10.1016/j.nicl.2018.07.021
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 0.817299246788025
          - id: 2829831604
            memberId: 276
            negative: 0.07277722209692002
            neutral: 0.9422045171260834
            positive: 0.08280273526906967
            section: discussion
            selfCites: []
            source: 10.1097/wad.0000000000000494
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 0.9422045171260834
          - id: 2155776066
            memberId: 78
            negative: 0.0021165350452065465
            neutral: 1
            positive: 0.0016119263600558043
            section: methods
            selfCites:
              - family: Ren
                given: Ping
                type: SHAREDAUTHOR
              - family: Lin
                given: Feng
                type: SHAREDAUTHOR
            source: 10.1016/j.nicl.2018.07.021
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 1
          - id: 2626090521
            memberId: 276
            negative: 0.024492473155260087
            neutral: 1
            positive: 0.007971957325935364
            section: introduction
            selfCites: []
            source: 10.1097/wad.0000000000000352
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 1
          - id: 2155775980
            memberId: 78
            negative: 0.02985255494713783
            neutral: 1
            positive: 0.007283219136297703
            section: introduction
            selfCites:
              - family: Ren
                given: Ping
                type: SHAREDAUTHOR
              - family: Lin
                given: Feng
                type: SHAREDAUTHOR
            source: 10.1016/j.nicl.2018.07.021
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 1
          - id: 2155776046
            memberId: 78
            negative: 0.012767541781067848
            neutral: 1
            positive: 0.011556158773601055
            section: introduction
            selfCites:
              - family: Ren
                given: Ping
                type: SHAREDAUTHOR
              - family: Lin
                given: Feng
                type: SHAREDAUTHOR
            source: 10.1016/j.nicl.2018.07.021
            target: 10.1016/j.neuropsychologia.2017.03.016
            type: mentioning
            typeConfidence: 1
        metadata:
          citingCounts:
            authors:
              Beeri Michal: 1
              Benussi Luisa: 3
              Chapman Benjamin: 1
              Eng Chloe: 1
              Fascendini Sara: 3
              Fede Giuseppe: 3
              Frisoni Giovanni: 3
              Galluzzi Samantha: 1
              Gilsanz Paola: 1
              Lacy Mary: 1
              Lin Feng: 1
              Maria Emilio: 3
              Mega Anna: 3
              Muscio Cristina: 3
              Ren Ping: 1
              Schifitto Giovanni: 1
              Tagliavini Fabrizio: 3
              Whitmer Rachel: 1
              Zhang Zhengwu: 1
            dateHistogram:
              '2018':
                contradicting: 2
                mentioning: 4
                supporting: 0
                total: 6
              '2019':
                contradicting: 0
                mentioning: 1
                supporting: 0
                total: 1
              '2022':
                contradicting: 0
                mentioning: 2
                supporting: 0
                total: 2
            journals:
              Alzheimer Disease & Associated Disorders: 2
              Neuroimage Clinical: 1
            pubTypes:
              article: 3
              research support, n.i.h., extramural: 1
            relationships:
              independent: 2
              selfCite: 1
            sections:
              discussion: 5
              introduction: 3
              methods: 1
              other: 0
              results: 0
            total: 9
          restrictedCitationCount: 10
          totalCitationCount: 9
        papers:
          10.1016/j.nicl.2018.07.021:
            abstract: >-
              Locus of control (LOC) is an important personality trait. LOC over
              cognitive competency reflects an individual's perceived control of
              desired cognitive outcomes, which is critical for maintaining
              successful cognitive aging. It is important to understand the
              neural substrates of LOC over cognitive competency in older
              adults, especially for individuals at high risk of dementia. Here,
              we characterized a cohesive functional and structural connectivity
              profile underlying LOC among 55 older adults with amnestic mild
              cognitive impairment (aMCI), combining resting-state functional
              magnetic resonance imaging and diffusion tensor imaging. The
              results showed that both functional and structural connectivity
              between the medial prefrontal cortex and amygdala were
              significantly correlated with external LOC. The functional
              connectivity mediated the correlation between structural
              connectivity and external LOC. In addition, aging-associated
              neurodegeneration moderated the relationship between structural
              connectivity and external LOC, showing that the structural
              connectivity was positively correlated with external LOC in low,
              but not high neurodegeneration. Our results suggest a critical
              role of the functional amygdala-frontal network, which may serve
              as a bridge between its white matter tract and LOC over cognitive
              competency in groups at high risk for dementia.
            authors:
              - affiliation: University of Rochester Medical Center
                affiliationID: '4419'
                affiliationSlug: university-of-rochester-medical-center-DxVe
                authorID: '25900534'
                authorName: Ping Ren
                authorSequenceNumber: 1
                authorSlug: ping-ren-OAyjd8
                family: Ren
                given: Ping
              - affiliation: University of Rochester Medical Center
                affiliationID: '4419'
                affiliationSlug: university-of-rochester-medical-center-DxVe
                authorID: '16766756'
                authorName: Benjamin P. Chapman
                authorSequenceNumber: 2
                authorSlug: benjamin-p-chapman-09bZky
                family: Chapman
                given: Benjamin P.
              - affiliation: University of Rochester Medical Center
                affiliationID: '4419'
                affiliationSlug: university-of-rochester-medical-center-DxVe
                authorID: '18713408'
                authorName: Zhengwu Zhang
                authorSequenceNumber: 3
                authorSlug: zhengwu-zhang-Ml54Yp
                family: Zhang
                given: Zhengwu
              - affiliation: University of Rochester Medical Center
                affiliationID: '4419'
                affiliationSlug: university-of-rochester-medical-center-DxVe
                authorID: '6075787'
                authorName: Giovanni Schifitto
                authorSequenceNumber: 4
                authorSlug: giovanni-schifitto-mOrNNe
                family: Schifitto
                given: Giovanni
              - affiliation: University of Rochester Medical Center
                affiliationID: '4419'
                affiliationSlug: university-of-rochester-medical-center-DxVe
                authorID: '24982522'
                authorName: Feng Lin
                authorSequenceNumber: 5
                authorSlug: feng-lin-xWj2pg
                family: Lin
                given: Feng
            doi: 10.1016/j.nicl.2018.07.021
            editorialNotices: []
            id: 240231688
            issns:
              - 2213-1582
            journal: 'NeuroImage: Clinical'
            journalSlug: MVpp0
            keywords:
              - Regular Article
            memberId: 78
            normalizedTypes:
              - article
            page: 297-304
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: 'NeuroImage: Clinical'
            slug: functional-and-structural-connectivity-of-3ndKmxK
            title: >-
              Functional and structural connectivity of the amygdala underpins
              locus of control in mild cognitive impairment
            type: journal-article
            volume: '20'
            year: 2018
          10.1097/wad.0000000000000352:
            abstract: >-
              Objective: Life expectancy for individuals with type 1 diabetes
              mellitus (T1DM) has increased recently; however, it is unknown how
              diabetes care attitudes affect late-life brain health.

              Research design and methods:The Study of Longevity in Diabetes
              (SOLID) consists of 734 older adults with T1DM, reporting diabetes
              locus of control (dLOC), age of diabetes diagnosis and other
              demographics, history of hypoglycemic episodes, and depressive
              symptoms. Global and domain-specific (language, executive
              function, episodic memory, simple attention) cognitive functioning
              was assessed at in-person interviews. Cross-sectional associations
              between dLOC and cognition were estimated using covariate-adjusted
              linear regression models in pooled and sexstratified models.

              Results:In pooled analyses, a one-point increase in dLOC (more
              internal) was positively associated with global cognition (β=0.05,
              95% CI: 0.02, 0.07), language (β=0.04, 95% CI: 0.01, 0.07), and
              executive function (β=0.04, 95% CI: 0.01, 0.07), but not episodic
              memory or simple attention. However, in sex-stratified analyses,
              this effect was seen only in males and not females.

              Conclusions:In elderly individuals with T1DM, we found
              associations between dLOC and cognition overall and in men but not
              women. Underlying sex differences should be considered in future
              research or interventions on psychosocial characteristics for
              cognition.
            authors:
              - affiliation: Kaiser Permanente
                affiliationID: '8677'
                affiliationSlug: kaiser-permanente-nznX
                authorID: '192151687'
                authorName: Chloe W. Eng
                authorSequenceNumber: 1
                authorSlug: chloe-w-eng-mOjXzyY
                family: Eng
                given: Chloe W.
              - affiliation: Kaiser Permanente
                affiliationID: '8677'
                affiliationSlug: kaiser-permanente-nznX
                authorID: '197922564'
                authorName: Paola Gilsanz
                authorSequenceNumber: 2
                authorSlug: paola-gilsanz-y8pDM6J
                family: Gilsanz
                given: Paola
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '11820206'
                authorName: Mary E. Lacy
                authorSequenceNumber: 3
                authorSlug: mary-e-lacy-zLxMNb
                family: Lacy
                given: Mary E.
              - affiliation: Icahn School of Medicine at Mount Sinai
                affiliationID: '4856'
                affiliationSlug: icahn-school-of-medicine-at-0ake
                authorID: '181150'
                authorName: Michal Schnaider Beeri
                authorSequenceNumber: 4
                authorSlug: michal-schnaider-beeri-zb1Gb
                family: Beeri
                given: Michal Schnaider
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '6791748'
                authorName: Rachel A. Whitmer
                authorSequenceNumber: 5
                authorSlug: rachel-a-whitmer-W8yMEw
                family: Whitmer
                given: Rachel A.
            doi: 10.1097/wad.0000000000000352
            editorialNotices: []
            id: 627276268
            issns:
              - 0893-0341
            issue: '1'
            journal: Alzheimer Disease &Amp; Associated Disorders
            journalSlug: V0dxM
            keywords:
              - type 1 diabetes
              - locus of control
              - cognition
              - cognitive function
              - sex differences
            memberId: 276
            normalizedTypes:
              - article
            page: 25-30
            preprintLinks: []
            publicationLinks: []
            publisher: Ovid Technologies (Wolters Kluwer Health)
            retracted: false
            slug: locus-of-control-and-cognition-kvAGrna
            title: >-
              Locus of Control and Cognition in Older Adults With Type 1
              Diabetes
            type: journal-article
            volume: '34'
            year: 2019
          10.1097/wad.0000000000000494:
            abstract: >-
              Aim: Our aim was to evaluate the psychological impact of
              predictive genetic testing in individuals at-risk for inherited
              dementia who underwent a structured counseling and testing
              protocol.

              Methods:Participants were healthy at-risk relatives from families
              with at least one affected patient, in whom a disease-associated
              genetic variant had been ascertained. A comprehensive
              psychological assessment (personality, anxiety and depression,
              quality of life, coping strategies, resilience and health-related
              beliefs) was administered at baseline, at 6 months and 12 months
              follow-up.Results: Twenty-four participants from 13 families were
              included. Sixteen participants underwent blood sampling and
              genetic analysis; 6 resulted to be carriers of pathogenic variants
              (1 in PSEN1, 1 in PSEN2, 4 in GRN). Carriers showed higher score
              on the Resilience Scale for Adults (RSA)social competence, and on
              Multidimensional Health Locus of Controlinternal, than noncarriers
              (P = 0.03 for both). Ten atrisk relatives who completed the
              follow-up showed improvement in RSAplanned future (P = 0.01) with
              respect to baseline. Discussion: Our case series showed that
              at-risk individuals undergoing predictive testing showed benefit
              on personal life and no detrimental impact on a broad range of
              psychological outcomes. Higher social skills and lower internal
              health locus of control in carriers may be an early psychological
              correlate of preclinical dementia.
            authors:
              - authorID: '943113514'
                authorName: Samantha Galluzzi
                authorSequenceNumber: 1
                authorSlug: samantha-galluzzi-g23rlQ1
                family: Galluzzi
                given: Samantha
              - authorID: '948459311'
                authorName: Anna Mega
                authorSequenceNumber: 2
                authorSlug: anna-mega-enyPGdz
                family: Mega
                given: Anna
              - authorID: '944285365'
                authorName: Anna Mega
                authorSequenceNumber: 2
                authorSlug: anna-mega-8mb3WbG
                family: Mega
                given: Anna
              - authorID: '959745484'
                authorName: Anna Mega
                authorSequenceNumber: 2
                authorSlug: anna-mega-LzmDr6a
                family: Mega
                given: Anna
              - authorID: '959925004'
                authorName: Giuseppe Di Fede
                authorSequenceNumber: 3
                authorSlug: giuseppe-di-fede-WEOnP8J
                family: Fede
                given: Giuseppe Di
              - authorID: '942996132'
                authorName: Giuseppe Di Fede
                authorSequenceNumber: 3
                authorSlug: giuseppe-di-fede-2bvwDzJ
                family: Fede
                given: Giuseppe Di
              - authorID: '946020582'
                authorName: Giuseppe Di Fede
                authorSequenceNumber: 3
                authorSlug: giuseppe-di-fede-V8Ykz3M
                family: Fede
                given: Giuseppe Di
              - authorID: '946105767'
                authorName: Cristina Muscio
                authorSequenceNumber: 4
                authorSlug: cristina-muscio-JlNArDY
                family: Muscio
                given: Cristina
              - authorID: '942996149'
                authorName: Cristina Muscio
                authorSequenceNumber: 4
                authorSlug: cristina-muscio-AOkrx8e
                family: Muscio
                given: Cristina
              - authorID: '959962348'
                authorName: Cristina Muscio
                authorSequenceNumber: 4
                authorSlug: cristina-muscio-WEOEdln
                family: Muscio
                given: Cristina
              - authorID: '941648071'
                authorName: Sara Fascendini
                authorSequenceNumber: 5
                authorSlug: sara-fascendini-N8z21AQ
                family: Fascendini
                given: Sara
              - authorID: '946105807'
                authorName: Sara Fascendini
                authorSequenceNumber: 5
                authorSlug: sara-fascendini-Y869ryE
                family: Fascendini
                given: Sara
              - authorID: '959614586'
                authorName: Sara Fascendini
                authorSequenceNumber: 5
                authorSlug: sara-fascendini-4xKLvVP
                family: Fascendini
                given: Sara
              - authorID: '959718660'
                authorName: Luisa Benussi
                authorSequenceNumber: 6
                authorSlug: luisa-benussi-Qkwy0A9
                family: Benussi
                given: Luisa
              - authorID: '948824097'
                authorName: Luisa Benussi
                authorSequenceNumber: 6
                authorSlug: luisa-benussi-vZW9kdJ
                family: Benussi
                given: Luisa
              - authorID: '942074916'
                authorName: Luisa Benussi
                authorSequenceNumber: 6
                authorSlug: luisa-benussi-Qkvjz58
                family: Benussi
                given: Luisa
              - authorID: '959718663'
                authorName: Fabrizio Tagliavini
                authorSequenceNumber: 7
                authorSlug: fabrizio-tagliavini-DRbxEeP
                family: Tagliavini
                given: Fabrizio
              - authorID: '948177452'
                authorName: Fabrizio Tagliavini
                authorSequenceNumber: 7
                authorSlug: fabrizio-tagliavini-Mzpx8aE
                family: Tagliavini
                given: Fabrizio
              - authorID: '945273779'
                authorName: Fabrizio Tagliavini
                authorSequenceNumber: 7
                authorSlug: fabrizio-tagliavini-KgwVRO8
                family: Tagliavini
                given: Fabrizio
              - authorID: '941475868'
                authorName: Giovanni B. Frisoni
                authorSequenceNumber: 8
                authorSlug: giovanni-b-frisoni-kYW3DKa
                family: Frisoni
                given: Giovanni B.
              - authorID: '942074921'
                authorName: Giovanni B Frisoni
                authorSequenceNumber: 8
                authorSlug: giovanni-b-frisoni-8mbLD39
                family: Frisoni
                given: Giovanni B
              - authorID: '959581751'
                authorName: Giovanni B Frisoni
                authorSequenceNumber: 8
                authorSlug: giovanni-b-frisoni-Y8ayx6K
                family: Frisoni
                given: Giovanni B
              - authorID: '945793812'
                authorName: Emilio Di Maria
                authorSequenceNumber: 9
                authorSlug: emilio-di-maria-0EPxnlr
                family: Maria
                given: Emilio Di
              - authorID: '946965432'
                authorName: Emilio Di Maria
                authorSequenceNumber: 9
                authorSlug: emilio-di-maria-2b1xvNx
                family: Maria
                given: Emilio Di
              - authorID: '960041932'
                authorName: Emilio Di Maria
                authorSequenceNumber: 9
                authorSlug: emilio-di-maria-2bnRryn
                family: Maria
                given: Emilio Di
            doi: 10.1097/wad.0000000000000494
            editorialNotices: []
            id: 11342526846
            issns:
              - 0893-0341
            issue: '2'
            journal: Alzheimer Disease &Amp; Associated Disorders
            journalSlug: V0dxM
            keywords:
              - Alzheimer disease
              - frontotemporal dementia
              - genetic counseling
              - genetic testing
              - psychological outcomes
            memberId: 276
            normalizedTypes:
              - article
            page: 118-124
            preprintLinks: []
            publicationLinks: []
            publisher: Ovid Technologies (Wolters Kluwer Health)
            slug: psychological-impact-of-predictive-genetic-9O8G0p0b
            title: >-
              Psychological Impact of Predictive Genetic Testing for Inherited
              Alzheimer Disease and Frontotemporal Dementia
            type: journal-article
            volume: '36'
            year: 2022
        tallies:
          10.1016/j.nicl.2018.07.021:
            citingPublications: 2
            contradicting: 0
            doi: 10.1016/j.nicl.2018.07.021
            mentioning: 4
            supporting: 0
            total: 4
            unclassified: 0
          10.1097/wad.0000000000000352:
            citingPublications: 2
            contradicting: 0
            doi: 10.1097/wad.0000000000000352
            mentioning: 2
            supporting: 0
            total: 2
            unclassified: 0
          10.1097/wad.0000000000000494:
            citingPublications: 0
            contradicting: 0
            doi: 10.1097/wad.0000000000000494
            mentioning: 0
            supporting: 0
            total: 0
            unclassified: 0
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
    CitationsMetadataSchema:
      properties:
        totalCitationCount:
          type: integer
          title: Totalcitationcount
        restrictedCitationCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Restrictedcitationcount
        distinctSourceCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Distinctsourcecount
        citingCounts:
          anyOf:
            - $ref: '#/components/schemas/CitationsCitingCounts'
            - type: 'null'
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
      type: object
      required:
        - totalCitationCount
      title: CitationsMetadataSchema
    CitationExternal:
      properties:
        id:
          type: integer
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
      type: object
      required:
        - id
        - source
        - target
      title: CitationExternal
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
    CitationsCitingCounts:
      properties:
        total:
          type: integer
          title: Total
        sections:
          $ref: '#/components/schemas/SectionCounts'
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
            additionalProperties:
              type: integer
            type: object
          type: object
          title: Datehistogram
        authors:
          additionalProperties:
            type: integer
          type: object
          title: Authors
      type: object
      required:
        - total
        - sections
        - pubTypes
        - journals
        - relationships
        - dateHistogram
        - authors
      title: CitationsCitingCounts
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
