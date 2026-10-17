> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: get-result

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Result

> Retrieve reference check job status.

This allows both fetching the job result and polling for job completion.

Whilst the job is in progress its status will be either
`PENDING` or `STARTED`.

Once the job is complete its status will be `SUCCESS` and
the result can be read under the `result` key of this response.



## OpenAPI

````yaml /openapi.json get /reference_check/tasks/{task_id}
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
  /reference_check/tasks/{task_id}:
    get:
      tags:
        - Reference Check
      summary: Get Result
      description: |-
        Retrieve reference check job status.

        This allows both fetching the job result and polling for job completion.

        Whilst the job is in progress its status will be either
        `PENDING` or `STARTED`.

        Once the job is complete its status will be `SUCCESS` and
        the result can be read under the `result` key of this response.
      operationId: getReferenceCheckResult
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
                $ref: '#/components/schemas/TaskResponse'
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
    TaskResponse:
      properties:
        status:
          type: string
          enum:
            - PENDING
            - STARTED
            - FAILURE
            - REVOKED
            - SUCCESS
            - CANCELLED
          title: Status
        overallTally:
          anyOf:
            - $ref: '#/components/schemas/TallyResponse'
            - type: 'null'
        info:
          anyOf:
            - $ref: '#/components/schemas/TaskInfo'
            - type: 'null'
        result:
          anyOf:
            - $ref: '#/components/schemas/KalaParserReport'
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Result
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
        papers:
          anyOf:
            - additionalProperties:
                $ref: '#/components/schemas/PaperResponse'
              type: object
            - type: 'null'
          title: Papers
        tallies:
          anyOf:
            - additionalProperties:
                $ref: '#/components/schemas/TallyResponse'
              type: object
            - type: 'null'
          title: Tallies
      type: object
      required:
        - status
      title: TaskResponse
      example:
        overallTally:
          contradicting: 98
          mentioning: 49577
          supporting: 1027
          total: 51417
          unclassified: 715
        papers:
          10.1002/hep.26015:
            abstract: >-
              Sphingolipids are important structural components of cell
              membranes and act as critical regulators of cell function by
              modulating intracellular signaling pathways. Specific
              sphingolipids, such as ceramide, glucosylceramide, and ganglioside
              GM3, have been implicated in various aspects of insulin
              resistance, because they have been shown to modify several steps
              in the insulin signaling pathway, such as phosphorylation of
              either protein kinase B (Akt) or of the insulin receptor. We now
              explore the role of the ceramide acyl chain length in insulin
              signaling by using a ceramide synthase 2 (CerS2) null mouse, which
              is unable to synthesize very long acyl chain (C22-C24) ceramides.
              CerS2 null mice exhibited glucose intolerance despite normal
              insulin secretion from the pancreas. Both insulin receptor and Akt
              phosphorylation were abrogated in liver, but not in adipose tissue
              or in skeletal muscle. The lack of insulin receptor
              phosphorylation in liver correlated with its inability to
              translocate into detergent-resistant membranes (DRMs). Moreover,
              DRMs in CerS2 null mice displayed properties significantly
              different from those in wild-type mice, suggesting that the
              altered sphingolipid acyl chain length directly affects insulin
              receptor translocation and subsequent signaling. Conclusion: We
              conclude that the sphingolipid acyl chain composition of liver
              regulates insulin signaling by modifying insulin receptor
              translocation into membrane microdomains. (HEPATOLOGY
              2013;57:525-532)
            authors:
              - affiliation: Weizmann Institute of Science
                affiliationID: '11815'
                affiliationSlug: weizmann-institute-of-science-b3jp
                authorID: '178208965'
                authorName: Joo Won Park
                authorSequenceNumber: 1
                authorSlug: joo-won-park-8GVygVM
                family: Park
                given: Joo Won
              - affiliation: Weizmann Institute of Science
                affiliationID: '11815'
                affiliationSlug: weizmann-institute-of-science-b3jp
                authorID: '13634490'
                authorName: Woo Jae Park
                authorSequenceNumber: 2
                authorSlug: woo-jae-park-9DXbrG
                family: Park
                given: Woo Jae
              - affiliation: Weizmann Institute of Science
                affiliationID: '11815'
                affiliationSlug: weizmann-institute-of-science-b3jp
                authorID: '11463805'
                authorName: Yael Kuperman
                authorSequenceNumber: 3
                authorSlug: yael-kuperman-AGNLa3
                family: Kuperman
                given: Yael
              - affiliation: Weizmann Institute of Science
                affiliationID: '11815'
                affiliationSlug: weizmann-institute-of-science-b3jp
                authorID: '187026'
                authorName: Sigalit Boura-Halfon
                authorSequenceNumber: 4
                authorSlug: sigalit-boura-halfon-R5099
                family: Boura-Halfon
                given: Sigalit
              - affiliation: Weizmann Institute of Science
                affiliationID: '11815'
                affiliationSlug: weizmann-institute-of-science-b3jp
                authorID: '6235045'
                authorName: Yael Pewzner-Jung
                authorSequenceNumber: 5
                authorSlug: yael-pewzner-jung-PQRaLL
                family: Pewzner-Jung
                given: Yael
              - affiliation: Weizmann Institute of Science
                affiliationID: '11815'
                affiliationSlug: weizmann-institute-of-science-b3jp
                authorID: '517393'
                authorName: Anthony H. Futerman
                authorSequenceNumber: 6
                authorSlug: anthony-h-futerman-ARGJv
                family: Futerman
                given: Anthony H.
            doi: 10.1002/hep.26015
            editorialNotices: []
            id: 50524713
            issns:
              - 0270-9139
            issue: '2'
            journal: Hepatology
            journalSlug: 5GEpG
            keywords:
              - Steatohepatitis/Metabolic Liver Disease
            memberId: 311
            normalizedTypes:
              - article
            page: 525-532
            preprintLinks: []
            publicationLinks: []
            publisher: Wiley
            retracted: false
            shortJournal: Hepatology
            slug: ablation-of-very-long-acyl-GA16lb
            title: >-
              Ablation of very long acyl chain sphingolipids causes hepatic
              insulin resistance in mice due to altered detergent-resistant
              membranes
            type: journal-article
            volume: '57'
            year: 2012
          10.1002/ijc.21422:
            abstract: >-
              Monocytes are recruited into tumors from the circulation along
              defined chemotactic gradients and they then differentiate into
              tumor-associated macrophages (TAMs). Recent evidence has shown
              that large numbers of TAMs are attracted to and retained in
              avascular and necrotic areas, where they are exposed to tumor
              hypoxia. At these sites, TAMs appear to undergo marked phenotypic
              changes with activation of hypoxia-inducible transcription
              factors, dramatically upregulating the expression of a large
              number of genes encoding mitogenic, proangiogenic and
              prometastatic cytokines and enzymes. As a consequence, high TAMs
              density has been correlated with increased tumor growth and
              angiogenesis in various tumor types. Since hypoxia is a hallmark
              feature of malignant tumors and hypoxic tumor cells are relatively
              resistant to radio-and chemotherapy, these areas have become a
              target for novel forms of anticancer therapy. These include
              hypoxiatargeted gene therapy in which macrophages are armed with
              therapeutic genes that are activated by hypoxia-responsive
              promoter elements. This restricts transgene expression to hypoxic
              areas, where the gene product is then released and acts on
              neighboring hypoxic tumor cells or proliferating blood vessels. In
              this way, the responses of macrophages to tumor hypoxia can be
              exploited to deliver potent antitumor agents to these poorly
              vascularized, and thus largely inaccessible, areas of tumors. '
              2005 Wiley-Liss, Inc.
            authors:
              - affiliation: University of Sheffield
                affiliationID: '10452'
                affiliationSlug: university-of-sheffield-MzKE
                authorID: '10326446'
                authorName: Craig Murdoch
                authorSequenceNumber: 1
                authorSlug: craig-murdoch-9bv0Y9
                family: Murdoch
                given: Craig
              - affiliation: University of Sheffield
                affiliationID: '10452'
                affiliationSlug: university-of-sheffield-MzKE
                authorID: '18992566'
                authorName: Claire E. Lewis
                authorSequenceNumber: 2
                authorSlug: claire-e-lewis-xPQJVw
                family: Lewis
                given: Claire E.
            doi: 10.1002/ijc.21422
            editorialNotices: []
            id: 50587440
            issns:
              - 0020-7136
              - 1097-0215
            issue: '5'
            journal: International Journal of Cancer
            journalSlug: ej5Qr
            keywords:
              - macrophage
              - tumor-associated macrophages (TAMs)
              - angiogenesis
              - hypoxia
              - tumor
            memberId: 311
            normalizedTypes:
              - article
            page: 701-708
            preprintLinks: []
            publicationLinks: []
            publisher: Wiley
            retracted: false
            shortJournal: Int. J. Cancer
            slug: macrophage-migration-and-gene-expression-L6MNGQ
            title: >-
              Macrophage migration and gene expression in response to tumor
              hypoxia
            type: journal-article
            volume: '117'
            year: 2005
          10.1006/bmmb.1993.1059:
            authors:
              - affiliation: City Of Hope National Medical Center
                affiliationID: '1813'
                affiliationSlug: city-of-hope-national-medical-GbZ
                authorID: '38973486'
                authorName: D E Comings
                authorSequenceNumber: 1
                authorSlug: d-e-comings-434RjY
                family: Comings
                given: D E
              - authorID: '238996266'
                authorName: S.D. Flanagan
                authorSequenceNumber: 2
                authorSlug: s-d-flanagan-xXnzrN3
                family: Flanagan
                given: S.D.
              - authorID: '27998969'
                authorName: George Dietz
                authorSequenceNumber: 3
                authorSlug: george-dietz-56lXdZ
                family: Dietz
                given: George
              - authorID: '16332857'
                authorName: D. Muhleman
                authorSequenceNumber: 4
                authorSlug: d-muhleman-GPYkKA
                family: Muhleman
                given: D.
              - authorID: '12811337'
                authorName: E. Knell
                authorSequenceNumber: 5
                authorSlug: e-knell-jXPVP5
                family: Knell
                given: E.
              - authorID: '9120272'
                authorName: Reinhard Gysin
                authorSequenceNumber: 6
                authorSlug: reinhard-gysin-wbjbdy
                family: Gysin
                given: Reinhard
            doi: 10.1006/bmmb.1993.1059
            editorialNotices: []
            id: 52091767
            issns:
              - 0885-4505
            issue: '2'
            journal: Biochemical Medicine and Metabolic Biology
            journalSlug: A38Ya
            memberId: 78
            normalizedTypes:
              - article
            page: 176-185
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Biochemical Medicine and Metabolic Biology
            slug: the-dopamine-d2-receptor-drd2-JMkQkY
            title: >-
              The Dopamine D2 Receptor (DRD2) as a Major Gene in Obesity and
              Height
            type: journal-article
            volume: '50'
            year: 1993
          10.1007/s00125-005-1735-1:
            authors:
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '8690074'
                authorName: Nobuhiro Shojima
                authorSequenceNumber: 1
                authorSlug: nobuhiro-shojima-pxjMON
                family: Shojima
                given: Nobuhiro
              - affiliation: Tohoku University
                affiliationID: '11040'
                affiliationSlug: tohoku-university-Lz4E
                authorID: '211303337'
                authorName: Takehide Ogihara
                authorSequenceNumber: 2
                authorSlug: takehide-ogihara-jMm2nmO
                family: Ogihara
                given: Takehide
              - affiliation: Saitama Medical University
                affiliationID: '18641'
                affiliationSlug: saitama-medical-university-XDLA
                authorID: '8346999'
                authorName: Kouichi Inukai
                authorSequenceNumber: 3
                authorSlug: kouichi-inukai-ePApMm
                family: Inukai
                given: Kouichi
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '78480766'
                authorName: Midori Fujishiro
                authorSequenceNumber: 4
                authorSlug: midori-fujishiro-xY4leM
                family: Fujishiro
                given: Midori
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '12700981'
                authorName: Hideyuki Sakoda
                authorSequenceNumber: 5
                authorSlug: hideyuki-sakoda-jXVgPJ
                family: Sakoda
                given: Hideyuki
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '6124749'
                authorName: Akifumi Kushiyama
                authorSequenceNumber: 6
                authorSlug: akifumi-kushiyama-A3wbrQ
                family: Kushiyama
                given: Akifumi
              - affiliation: Tohoku University
                affiliationID: '11040'
                affiliationSlug: tohoku-university-Lz4E
                authorID: '80950237'
                authorName: Hideki Katagiri
                authorSequenceNumber: 7
                authorSlug: hideki-katagiri-jl3d9z
                family: Katagiri
                given: Hideki
              - authorID: '6063891'
                authorName: Motonobu Anai
                authorSequenceNumber: 8
                authorSlug: motonobu-anai-1ZyzWM
                family: Anai
                given: Motonobu
              - authorID: '29192866'
                authorName: Hiraku Ono
                authorSequenceNumber: 9
                authorSlug: hiraku-ono-xxMAJw
                family: Ono
                given: Hiraku
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '20980323'
                authorName: Yasushi Fukushima
                authorSequenceNumber: 10
                authorSlug: yasushi-fukushima-JlrVd0
                family: Fukushima
                given: Yasushi
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '6301718'
                authorName: Nanao Horike
                authorSequenceNumber: 11
                authorSlug: nanao-horike-dvEwXj
                family: Horike
                given: Nanao
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '7408258'
                authorName: Amelia Y.I. Viana
                authorSequenceNumber: 12
                authorSlug: amelia-y-i-viana-gZzzwK
                family: Viana
                given: Amelia Y.I.
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '5464422'
                authorName: Yasunobu Uchijima
                authorSequenceNumber: 13
                authorSlug: yasunobu-uchijima-xXYWkb
                family: Uchijima
                given: Yasunobu
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '16077383'
                authorName: Hiroki Kurihara
                authorSequenceNumber: 14
                authorSlug: hiroki-kurihara-a82d9j
                family: Kurihara
                given: Hiroki
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '15656692'
                authorName: Tomoichiro Asano
                authorSequenceNumber: 15
                authorSlug: tomoichiro-asano-WnKyEw
                family: Asano
                given: Tomoichiro
            doi: 10.1007/s00125-005-1735-1
            editorialNotices: []
            id: 59412464
            issns:
              - 0012-186X
              - 1432-0428
            issue: '5'
            journal: Diabetologia
            journalSlug: PQL9g
            memberId: 297
            normalizedTypes:
              - article
            page: 984-992
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Diabetologia
            slug: serum-concentrations-of-resistin-like-molecules-y5KM3l
            title: >-
              Serum concentrations of resistin-like molecules β and γ are
              elevated in high-fat-fed and obese db/db mice, with increased
              production in the intestinal tract and bone marrow
            type: journal-article
            volume: '48'
            year: 2005
          10.1007/s00125-013-2846-8:
            abstract: >-
              Aims/hypothesis Metabolic disorders are commonly investigated
              using knockout and transgenic mouse models. A variety of mouse
              strains have been used for this purpose. However, mouse strains
              can differ in their inherent propensities to develop metabolic
              disease, which may affect the experimental outcomes of metabolic
              studies. We have investigated straindependent differences in the
              susceptibility to diet-induced obesity and insulin resistance in
              five commonly used inbred mouse strains (C57BL/6J, 129X1/SvJ,
              BALB/c, DBA/2 and FVB/N). Methods Mice were fed either a low-fat
              or a high-fat diet (HFD) for 8 weeks. Whole-body energy
              expenditure and body composition were then determined. Tissues
              were used to measure markers of mitochondrial metabolism,
              inflammation, oxidative stress and lipid accumulation. Results
              BL6, 129X1, DBA/2 and FVB/N mice were all susceptible to varying
              degrees to HFD-induced obesity, glucose intolerance and insulin
              resistance, but BALB/c mice exhibited some protection from these
              detrimental effects. This protection could not be explained by
              differences in mitochondrial metabolism or oxidative stress in
              liver or muscle, or inflammation in adipose tissue. Interestingly,
              in contrast with the other strains, BALB/c mice did not accumulate
              excess lipid (triacylglycerols and diacylglycerols) in the liver;
              this is potentially related to lower fatty acid uptake rather than
              differences in lipogenesis or lipid oxidation.
              Conclusions/interpretation Collectively, our findings indicate
              that most mouse strains develop metabolic defects on an HFD.
              However, there are inherent differences between strains, and thus
              the genetic background needs to be considered carefully in
              metabolic studies. 

              Keywords
            authors:
              - affiliation: Garvan Institute of Medical Research
                affiliationID: '18807'
                affiliationSlug: garvan-institute-of-medical-research-Y0EG
                authorID: '18166098'
                authorName: Magdalene K. Montgomery
                authorSequenceNumber: 1
                authorSlug: magdalene-k-montgomery-6JAODr
                family: Montgomery
                given: Magdalene K.
              - affiliation: Garvan Institute of Medical Research
                affiliationID: '18807'
                affiliationSlug: garvan-institute-of-medical-research-Y0EG
                authorID: '97047997'
                authorName: Nicole L Hallahan
                authorSequenceNumber: 2
                authorSlug: nicole-l-hallahan-vvrjdV
                family: Hallahan
                given: Nicole L
              - affiliation: University of Wollongong
                affiliationID: '20782'
                affiliationSlug: university-of-wollongong-VWYO
                authorID: '17560038'
                authorName: Simon H. J. Brown
                authorSequenceNumber: 3
                authorSlug: simon-h-j-brown-VyPjvM
                family: Brown
                given: Simon H. J.
              - affiliation: Garvan Institute of Medical Research
                affiliationID: '18807'
                affiliationSlug: garvan-institute-of-medical-research-Y0EG
                authorID: '52122459'
                authorName: Menghan Liu
                authorSequenceNumber: 4
                authorSlug: menghan-liu-bnvKEW
                family: Liu
                given: Menghan
              - affiliation: University of Wollongong
                affiliationID: '20782'
                affiliationSlug: university-of-wollongong-VWYO
                authorID: '18720972'
                authorName: Todd W. Mitchell
                authorSequenceNumber: 5
                authorSlug: todd-w-mitchell-wVJAyr
                family: Mitchell
                given: Todd W.
              - affiliation: Garvan Institute of Medical Research
                affiliationID: '18807'
                affiliationSlug: garvan-institute-of-medical-research-Y0EG
                authorID: '8713947'
                authorName: Gregory J. Cooney
                authorSequenceNumber: 6
                authorSlug: gregory-j-cooney-1gxvRX
                family: Cooney
                given: Gregory J.
              - affiliation: Garvan Institute of Medical Research
                affiliationID: '18807'
                affiliationSlug: garvan-institute-of-medical-research-Y0EG
                authorID: '66870151'
                authorName: Nigel Turner
                authorSequenceNumber: 7
                authorSlug: nigel-turner-Yk1yJK
                family: Turner
                given: Nigel
            doi: 10.1007/s00125-013-2846-8
            editorialNotices: []
            id: 59415386
            issns:
              - 0012-186X
              - 1432-0428
            issue: '5'
            journal: Diabetologia
            journalSlug: PQL9g
            memberId: 297
            normalizedTypes:
              - article
            page: 1129-1139
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Diabetologia
            slug: mouse-strain-dependent-variation-in-obesity-4X12WV
            title: >-
              Mouse strain-dependent variation in obesity and glucose
              homeostasis in response to high-fat feeding
            type: journal-article
            volume: '56'
            year: 2013
          10.1007/s11892-008-0032-z:
            abstract: >-
              Ectopic fat is defined by the deposition of triglycerides within
              cells of non-adipose tissue that normally contain only small
              amounts of fat. Over the past decade, magnetic resonance
              spectroscopy has been used extensively for noninvasive
              quantification of intramyocellular, intrahepatocellular, and more
              recently myocardial and pancreatic lipids. In liver and muscle,
              triglyceride content usually correlates with whole-body and
              tissue-specific insulin sensitivity. However, fat mass and
              oxidative capacity influence this relationship, indicating that
              ectopic lipid content is not the only factor that explains insulin
              resistance. Ectopic lipids may rather serve as biomarkers of the
              balance between metabolic supply and demand in different states of
              insulin sensitivity. Consequently, ectopic lipid concentrations,
              particularly in the liver, decrease with lifestyle- or
              drug-induced improvement of insulin sensitivity.
            authors:
              - affiliation: Hanusch Hospital
                affiliationID: '197271'
                affiliationSlug: hanusch-hospital-NM0w9
                authorID: '11468441'
                authorName: Angelika Lettner
                authorSequenceNumber: 1
                authorSlug: angelika-lettner-X4eL6k
                family: Lettner
                given: Angelika
              - affiliation: Hanusch Hospital
                affiliationID: '197271'
                affiliationSlug: hanusch-hospital-NM0w9
                authorID: '144668417'
                authorName: Michael Roden
                authorSequenceNumber: 2
                authorSlug: michael-roden-Ezr13L
                family: Roden
                given: Michael
            doi: 10.1007/s11892-008-0032-z
            editorialNotices: []
            id: 61188900
            issns:
              - 1534-4827
              - 1539-0829
            issue: '3'
            journal: Current Diabetes Reports
            journalSlug: jMJGJ
            memberId: 297
            normalizedTypes:
              - article
            page: 185-191
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Curr Diab Rep
            slug: ectopic-fat-and-insulin-resistance-3g5eOO
            title: Ectopic fat and insulin resistance
            type: journal-article
            volume: '8'
            year: 2008
          10.1016/j.cell.2012.02.017:
            abstract: >-
              Insulin resistance is a complex metabolic disorder that defies a
              single etiological pathway. Accumulation of ectopic lipid
              metabolites, activation of the unfolded protein response (UPR)
              pathway and innate immune pathways have all been implicated in the
              pathogenesis of insulin resistance. However, these pathways are
              also closely linked to changes in fatty acid uptake, lipogenesis,
              and energy expenditure that can impact ectopic lipid deposition.
              Ultimately, accumulation of specific lipid metabolites
              (diacylglycerols and/or ceramides) in liver and skeletal muscle,
              may be a common pathway leading to impaired insulin signaling and
              insulin resistance.
            authors:
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '10373696'
                authorName: Varman T. Samuel
                authorSequenceNumber: 1
                authorSlug: varman-t-samuel-M2rnek
                family: Samuel
                given: Varman T.
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '5886223'
                authorName: Gerald I. Shulman
                authorSequenceNumber: 2
                authorSlug: gerald-i-shulman-J1LvKY
                family: Shulman
                given: Gerald I.
            doi: 10.1016/j.cell.2012.02.017
            editorialNotices: []
            id: 67157549
            issns:
              - 0092-8674
            issue: '5'
            journal: Cell
            journalSlug: pnm4z
            keywords:
              - Article
            memberId: 78
            normalizedTypes:
              - article
            page: 852-871
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Cell
            slug: mechanisms-for-insulin-resistance-common-Aazynv
            title: >-
              Mechanisms for Insulin Resistance: Common Threads and Missing
              Links
            type: journal-article
            volume: '148'
            year: 2012
          10.1016/j.cell.2014.03.066:
            abstract: >-
              SUMMARY

              Beige fat, which expresses the thermogenic protein UCP1, provides
              a defense against cold and obesity. Although a cold environment is
              the physiologic stimulus for inducing beige fat in mice and
              humans, the events that lead from the sensing of cold to the
              development of beige fat remain poorly understood. Here, we
              identify the efferent beige fat thermogenic circuit, consisting of
              eosinophils, type 2 cytokines interleukin (IL)-4/13 and
              alternatively activated macrophages. Genetic loss of eosinophils
              or IL-4/13 signaling impairs cold-induced biogenesis of beige fat.
              Mechanistically, macrophages recruited to cold-stressed
              subcutaneous white adipose tissue (scWAT) undergo alternative
              activation to induce tyrosine hydroxylase expression and
              catecholamine production, factors required for browning of scWAT.
              Conversely, administration of IL-4 to thermoneutral mice increases
              beige fat mass and thermogenic capacity to ameliorate
              pre-established obesity. Together, our findings have uncovered the
              efferent circuit controlling biogenesis of beige fat and provide
              support for its targeting to treat obesity.
            authors:
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '32615577'
                authorName: Yifu Qiu
                authorSequenceNumber: 1
                authorSlug: yifu-qiu-n15v8D
                family: Qiu
                given: Yifu
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '19867627'
                authorName: Khoa D. Nguyen
                authorSequenceNumber: 2
                authorSlug: khoa-d-nguyen-N802GN
                family: Nguyen
                given: Khoa D.
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '5895306'
                authorName: Justin I. Odegaard
                authorSequenceNumber: 3
                authorSlug: justin-i-odegaard-zRGZz3
                family: Odegaard
                given: Justin I.
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '81078612'
                authorName: Xiaojin Cui
                authorSequenceNumber: 4
                authorSlug: xiaojin-cui-02DQmP
                family: Cui
                given: Xiaojin
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '15221801'
                authorName: Xiao Yu Tian
                authorSequenceNumber: 5
                authorSlug: xiao-yu-tian-Pvz4rQ
                family: Tian
                given: Xiao Yu
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '6048470'
                authorName: Richard M. Locksley
                authorSequenceNumber: 6
                authorSlug: richard-m-locksley-RVle83
                family: Locksley
                given: Richard M.
              - affiliation: University of Washington
                affiliationID: '11969'
                affiliationSlug: university-of-washington-5JeG
                authorID: '398890'
                authorName: Richard D. Palmiter
                authorSequenceNumber: 7
                authorSlug: richard-d-palmiter-9g4O4
                family: Palmiter
                given: Richard D.
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '32477922'
                authorName: Ajay Chawla
                authorSequenceNumber: 8
                authorSlug: ajay-chawla-xpjLMg
                family: Chawla
                given: Ajay
            doi: 10.1016/j.cell.2014.03.066
            editorialNotices: []
            id: 67158910
            issns:
              - 0092-8674
            issue: '6'
            journal: Cell
            journalSlug: pnm4z
            keywords:
              - Article
            memberId: 78
            normalizedTypes:
              - article
            page: 1292-1308
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Cell
            slug: eosinophils-and-type-2-cytokine-64K4kr
            title: >-
              Eosinophils and Type 2 Cytokine Signaling in Macrophages
              Orchestrate Development of Functional Beige Fat
            type: journal-article
            volume: '157'
            year: 2014
          10.1016/j.celrep.2016.06.007:
            abstract: >-
              Summary

              Clostridium difficile infection (CDI) is the most common cause of
              hospital-acquired infection in the United States. Host
              susceptibility and the severity of infection are influenced by
              disruption of the microbiota and the immune response. However, how
              the microbiota regulates immune responses to mediate CDI outcome
              remains unclear. Here, we investigated the role of the
              microbiota-linked cytokine IL-25 during infection. Intestinal
              IL-25 was suppressed during CDI in humans and mice. Restoration of
              IL-25 reduced CDI-associated mortality and tissue pathology even
              though equivalent levels of C. difficile bacteria and toxin
              remained in the gut. IL-25 protection was mediated by gut
              eosinophils, as demonstrated by an increase in intestinal
              eosinophils and a loss of IL-25 protection upon eosinophil
              depletion. These findings support a mechanism whereby the
              induction of IL-25-mediated eosinophilia can reduce host mortality
              during active CDI. This work may provide targets for future
              development of microbial or immune-based therapies.
            authors:
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '9988090'
                authorName: Erica L. Buonomo
                authorSequenceNumber: 1
                authorSlug: erica-l-buonomo-9b1pNb
                family: Buonomo
                given: Erica L.
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '4017735'
                authorName: Carrie A. Cowardin
                authorSequenceNumber: 2
                authorSlug: carrie-a-cowardin-K6lp3p
                family: Cowardin
                given: Carrie A.
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '24766195'
                authorName: Madeline G. Wilson
                authorSequenceNumber: 3
                authorSlug: madeline-g-wilson-Yjv6QD
                family: Wilson
                given: Madeline G.
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '67903236'
                authorName: Mahmoud M. Saleh
                authorSequenceNumber: 4
                authorSlug: mahmoud-m-saleh-l166PE
                family: Saleh
                given: Mahmoud M.
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '6063859'
                authorName: Patcharin Pramoonjago
                authorSequenceNumber: 5
                authorSlug: patcharin-pramoonjago-b2rY3k
                family: Pramoonjago
                given: Patcharin
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '21744467'
                authorName: William A. Petri
                authorSequenceNumber: 6
                authorSlug: william-a-petri-JlYGXE
                family: Petri
                given: William A.
            doi: 10.1016/j.celrep.2016.06.007
            editorialNotices: []
            id: 67169759
            issns:
              - 2211-1247
            issue: '2'
            journal: Cell Reports
            journalSlug: b2DYr
            keywords:
              - Article
            memberId: 78
            normalizedTypes:
              - article
            page: 432-443
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Cell Reports
            slug: microbiota-regulated-il-25-increases-eosinophil-number-bmapM1
            title: >-
              Microbiota-Regulated IL-25 Increases Eosinophil Number to Provide
              Protection during Clostridium difficile Infection
            type: journal-article
            volume: '16'
            year: 2016
          10.1016/j.molmet.2017.12.004:
            abstract: >-
              ObjectiveObesity is a metabolic disorder that has reached epidemic
              proportions worldwide and leads to increased risk for diabetes,
              cardiovascular disease, asthma, certain cancers, and various other
              diseases. Obesity and its comorbidities are associated with
              impaired adipose tissue (AT) function. In the last decade,
              eosinophils have been identified as regulators of proper AT
              function. Our study aimed to determine whether normalizing the
              number of AT eosinophils in obese mice, to those of lean healthy
              mice, would reduce obesity and/or improve metabolic
              fitness.MethodsC57BL/6J mice fed a high fat diet (HFD) were
              simultaneously given recombinant interleukin-5 (rIL5) for 8 weeks
              to increase AT eosinophils. Metabolic fitness was tested by
              evaluating weight gain, AT inflammation, glucose, lipid, and
              mixed-meal tolerance, AT insulin signaling, energy substrate
              utilization, energy expenditure, and white AT beiging
              capacity.ResultsEosinophils were increased ∼3-fold in AT of obese
              HFD-fed mice treated with rIL5, and thus were restored to levels
              observed in lean healthy mice. However, there were no significant
              differences in rIL5-treated mice among the above listed
              comprehensive set of metabolic assays, despite the increased AT
              eosinophils.ConclusionsWe have shown that restoring obese AT
              eosinophils to lean healthy levels is not sufficient to allow for
              improvement in any of a range of metabolic features otherwise
              impaired in obesity. Thus, the mechanisms that identified
              eosinophils as positive regulators of AT function, and therefore
              systemic health, are more complex than initially understood and
              will require further study to fully elucidate.
            authors:
              - affiliation: Vanderbilt University
                affiliationID: '16364'
                affiliationSlug: vanderbilt-university-ypnx
                authorID: '11125700'
                authorName: W. Reid Bolus
                authorSequenceNumber: 1
                authorSlug: w-reid-bolus-38VwWO
                family: Bolus
                given: W. Reid
              - affiliation: Vanderbilt University
                affiliationID: '16364'
                affiliationSlug: vanderbilt-university-ypnx
                authorID: '56697354'
                authorName: Kristin R. Peterson
                authorSequenceNumber: 2
                authorSlug: kristin-r-peterson-6jwyP9
                family: Peterson
                given: Kristin R.
              - affiliation: Vanderbilt University
                affiliationID: '16364'
                affiliationSlug: vanderbilt-university-ypnx
                authorID: '8524948'
                authorName: Merla J. Hubler
                authorSequenceNumber: 3
                authorSlug: merla-j-hubler-WGdxJO
                family: Hubler
                given: Merla J.
              - affiliation: Vanderbilt University
                affiliationID: '16364'
                affiliationSlug: vanderbilt-university-ypnx
                authorID: '21870360'
                authorName: Arion Kennedy
                authorSequenceNumber: 4
                authorSlug: arion-kennedy-Qkw9NX
                family: Kennedy
                given: Arion
              - affiliation: Vanderbilt University
                affiliationID: '16364'
                affiliationSlug: vanderbilt-university-ypnx
                authorID: '67455575'
                authorName: Marnie L. Gruen
                authorSequenceNumber: 5
                authorSlug: marnie-l-gruen-ZkMNv9
                family: Gruen
                given: Marnie L.
              - affiliation: Vanderbilt University
                affiliationID: '16364'
                affiliationSlug: vanderbilt-university-ypnx
                authorID: '3944334'
                authorName: Alyssa H. Hasty
                authorSequenceNumber: 6
                authorSlug: alyssa-h-hasty-OVjb2k
                family: Hasty
                given: Alyssa H.
            doi: 10.1016/j.molmet.2017.12.004
            editorialNotices: []
            id: 242253400
            issns:
              - 2212-8778
            journal: Molecular Metabolism
            journalSlug: lZrJ3
            keywords:
              - Original Article
            memberId: 78
            normalizedTypes:
              - article
            page: 86-95
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Molecular Metabolism
            slug: elevating-adipose-eosinophils-in-obese-3ndxRPK
            title: >-
              Elevating adipose eosinophils in obese mice to physiologically
              normal levels does not rescue metabolic impairments
            type: journal-article
            volume: '8'
            year: 2018
          10.1038/ijo.2008.229:
            abstract: >-
              Recent studies consistently support a hypoxia response in the
              adipose tissue in obese animals. The observations have led to the
              formation of an exciting concept, adipose tissue hypoxia (ATH), in
              the understanding of major disorders associated with obesity. ATH
              may provide cellular mechanisms for chronic inflammation,
              macrophage infiltration, adiponectin reduction, leptin elevation,
              adipocyte death, endoplasmic reticulum stress and mitochondrial
              dysfunction in white adipose tissue in obesity. The concept
              suggests that inhibition of adipogenesis and triglyceride
              synthesis by hypoxia may be a new mechanism for elevated free
              fatty acids in the circulation in obesity. ATH may represent a
              unified cellular mechanism for a variety of metabolic disorders
              and insulin resistance in patients with metabolic syndrome. It
              suggests a new mechanism of pathogenesis of insulin resistance and
              inflammation in obstructive sleep apnea. In addition, it may help
              us to understand the beneficial effects of caloric restriction,
              physical exercise and angiotensin II inhibitors in the improvement
              of insulin sensitivity. In this review article, literatures are
              reviewed to summarize the evidence and possible cellular
              mechanisms of ATH. The directions and road blocks in the future
              studies are analyzed.
            authors:
              - affiliation: Pennington Biomedical Research Center
                affiliationID: '16649'
                affiliationSlug: pennington-biomedical-research-center-A5ra
                authorID: '14162755'
                authorName: Jianping Ye
                authorSequenceNumber: 1
                authorSlug: jianping-ye-e6J2MO
                family: Ye
                given: Jianping
            doi: 10.1038/ijo.2008.229
            editorialNotices: []
            id: 81259318
            issns:
              - 0307-0565
              - 1476-5497
            issue: '1'
            journal: International Journal of Obesity
            journalSlug: QePv9
            keywords:
              - adipose tissue
              - insulin resistance
              - hypoxia
              - inflammation
              - angiogenesis
            memberId: 297
            normalizedTypes:
              - article
            page: 54-66
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Int J Obes
            slug: emerging-role-of-adipose-tissue-dlEPxb
            title: >-
              Emerging role of adipose tissue hypoxia in obesity and insulin
              resistance
            type: journal-article
            volume: '33'
            year: 2008
          10.1038/mi.2014.123:
            abstract: >-
              Eosinophils are multifunctional leukocytes that reside in the
              gastrointestinal (GI) lamina propria, where their basal function
              remains largely unexplored. In this study, by examining mice with
              a selective deficiency of systemic eosinophils (by lineage
              ablation) or GI eosinophils (eotaxin-1/2 double–deficient or CC
              chemokine receptor 3–deficient), we show that eosinophils support
              immunoglobulin A (IgA) class switching, maintain intestinal mucus
              secretions, affect intestinal microbial composition, and promote
              the development of Peyer’s patches. Eosinophil-deficient mice
              showed reduced expression of mediators of secretory IgA
              production, including intestinal interleukin 1β (IL-1β), inducible
              nitric oxide synthase, lymphotoxin (LT) α, and LT-β, and reduced
              levels of retinoic acid-related orphan receptor gamma t–positive
              (ROR-γt+) innate lymphoid cells (ILCs) while maintaining normal
              levels of APRIL (a proliferation-inducing ligand), BAFF (B
              cell–activating factor of the tumor necrosis factor family), and
              TGF-β (transforming growth factor β). GI eosinophils expressed a
              relatively high level of IL-1β, and IL-1β–deficient mice
              manifested the altered gene expression profiles observed in
              eosinophil-deficient mice and decreased levels of IgA+ cells and
              ROR-γt+ ILCs. On the basis of these collective data, we propose
              that eosinophils are required for homeostatic intestinal immune
              responses including IgA production and that their affect is
              mediated via IL-1β in the small intestine.
            authors:
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '139679076'
                authorName: Yun-Jae Jung
                authorSequenceNumber: 1
                authorSlug: yun-jae-jung-2PO1JE
                family: Jung
                given: Yun-Jae
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '17384861'
                authorName: Ting Wen
                authorSequenceNumber: 2
                authorSlug: ting-wen-EOXp5P
                family: Wen
                given: Ting
              - affiliation: University of Cincinnati
                affiliationID: '19659'
                affiliationSlug: university-of-cincinnati-bQ3Z
                authorID: '411647800'
                authorName: M K Mingler
                authorSequenceNumber: 3
                authorSlug: m-k-mingler-38LOGQO
                family: Mingler
                given: M K
              - affiliation: University of Cincinnati
                affiliationID: '19659'
                affiliationSlug: university-of-cincinnati-bQ3Z
                authorID: '346531809'
                authorName: J M Caldwell
                authorSequenceNumber: 4
                authorSlug: j-m-caldwell-vydAJ14
                family: Caldwell
                given: J M
              - affiliation: University of Cincinnati
                affiliationID: '19659'
                affiliationSlug: university-of-cincinnati-bQ3Z
                authorID: '48788791'
                authorName: Y H Wang
                authorSequenceNumber: 5
                authorSlug: y-h-wang-1vR92W
                family: Wang
                given: Y H
              - affiliation: University of Alabama at Birmingham
                affiliationID: '26599'
                affiliationSlug: university-of-alabama-at-birmingham-eNxm
                authorID: '69032083'
                authorName: David D. Chaplin
                authorSequenceNumber: 6
                authorSlug: david-d-chaplin-a66kyx
                family: Chaplin
                given: David D.
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '176464118'
                authorName: E H Lee
                authorSequenceNumber: 7
                authorSlug: e-h-lee-dvKK5a9
                family: Lee
                given: E H
              - affiliation: Pohang University of Science and Technology
                affiliationID: '12801'
                affiliationSlug: pohang-university-of-science-and-Pl3k
                authorID: '27638113'
                authorName: Myoung Ho Jang
                authorSequenceNumber: 8
                authorSlug: myoung-ho-jang-G2ygMb
                family: Jang
                given: Myoung Ho
              - affiliation: Ewha Womans University
                affiliationID: '20765'
                affiliationSlug: ewha-womans-university-8Wb3
                authorID: '20013547'
                authorName: So Youn Woo
                authorSequenceNumber: 9
                authorSlug: so-youn-woo-15xObj
                family: Woo
                given: So Youn
              - affiliation: Ewha Womans University
                affiliationID: '20765'
                affiliationSlug: ewha-womans-university-8Wb3
                authorID: '7285494'
                authorName: Ju Young Seoh
                authorSequenceNumber: 10
                authorSlug: ju-young-seoh-zR4kwE
                family: Seoh
                given: Ju Young
              - affiliation: Osaka University
                affiliationID: '2722'
                affiliationSlug: osaka-university-xX9D
                authorID: '20136199'
                authorName: Masayuki Miyasaka
                authorSequenceNumber: 11
                authorSlug: masayuki-miyasaka-enkk90
                family: Miyasaka
                given: Masayuki
              - affiliation: University of Cincinnati
                affiliationID: '19659'
                affiliationSlug: university-of-cincinnati-bQ3Z
                authorID: '11358116'
                authorName: Marc E. Rothenberg
                authorSequenceNumber: 12
                authorSlug: marc-e-rothenberg-QmeOgJ
                family: Rothenberg
                given: Marc E.
            doi: 10.1038/mi.2014.123
            editorialNotices: []
            id: 81304296
            issns:
              - 1933-0219
              - 1935-3456
            issue: '4'
            journal: Mucosal Immunology
            journalSlug: OV5EQ
            keywords:
              - Article
            memberId: 297
            normalizedTypes:
              - article
            page: 930-942
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Mucosal Immunol
            slug: il-1-in-eosinophil-mediated-small-intestinal-Mv4WYd
            title: >-
              IL-1β in eosinophil-mediated small intestinal homeostasis and IgA
              production
            type: journal-article
            volume: '8'
            year: 2015
          10.1038/nature05483:
            abstract: >-
              Adipocytes have been studied with increasing intensity as a result
              of the emergence of obesity as a serious public health problem and
              the realization that adipose tissue serves as an integrator of
              various physiological pathways. In particular, their role in
              calorie storage makes adipocytes well suited to the regulation of
              energy balance. Adipose tissue also serves as a crucial integrator
              of glucose homeostasis. Knowledge of adipocyte biology is
              therefore crucial for understanding the pathophysiological basis
              of obesity and metabolic diseases such as type 2 diabetes.
              Furthermore, the rational manipulation of adipose physiology is a
              promising avenue for therapy of these conditions.
            authors:
              - authorID: '23569687'
                authorName: Evan D. Rosen
                authorSequenceNumber: 1
                authorSlug: evan-d-rosen-mALkWz
                family: Rosen
                given: Evan D.
              - affiliation: Harvard University
                affiliationID: '14927'
                affiliationSlug: harvard-university-NmzP
                authorID: '376984'
                authorName: Bruce M. Spiegelman
                authorSequenceNumber: 2
                authorSlug: bruce-m-spiegelman-LAYWm
                family: Spiegelman
                given: Bruce M.
            doi: 10.1038/nature05483
            editorialNotices: []
            id: 81323364
            issns:
              - 0028-0836
              - 1476-4687
            issue: '7121'
            journal: Nature
            journalSlug: wmGvz
            keywords: []
            memberId: 297
            normalizedTypes:
              - article
            page: 847-853
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Nature
            slug: adipocytes-as-regulators-of-energy-ymzOyl
            title: Adipocytes as regulators of energy balance and glucose homeostasis
            type: journal-article
            volume: '444'
            year: 2006
          10.1038/nbt.1621:
            abstract: >-
              High-throughput mRNA sequencing (RNA-Seq) holds the promise of
              simultaneous transcript discovery and abundance estimation1-3. We
              introduce an algorithm for transcript assembly coupled with a
              statistical model for RNA-Seq experiments that produces estimates
              of abundances. Our algorithms are implemented in an open source
              software program called Cufflinks. To test Cufflinks, we sequenced
              and analyzed more than 430 million paired 75bp RNA-Seq reads from
              a mouse myoblast cell line representing a differentiation time
              series. We detected 13,692 known transcripts and 3,724 previously
              unannotated ones, 62% of which are supported by independent
              expression data or by homologous genes in other species. Analysis
              of transcript expression over the time series revealed complete
              switches in the dominant transcription start site (TSS) or
              splice-isoform in 330 genes, along with more subtle shifts in a
              further 1,304 genes. These dynamics suggest substantial regulatory
              flexibility and complexity in this well-studied model of muscle
              development.
            authors:
              - affiliation: University of Maryland, College Park
                affiliationID: '2613'
                affiliationSlug: university-of-maryland-college-park-G3YK
                authorID: '8885272'
                authorName: Cole Trapnell
                authorSequenceNumber: 1
                authorSlug: cole-trapnell-wb9XKL
                family: Trapnell
                given: Cole
              - affiliation: California Institute of Technology
                affiliationID: '9687'
                affiliationSlug: california-institute-of-technology-mb8j
                authorID: '81257310'
                authorName: Brian A. Williams
                authorSequenceNumber: 2
                authorSlug: brian-a-williams-623WzM
                family: Williams
                given: Brian A.
              - affiliation: University of Maryland, College Park
                affiliationID: '2613'
                affiliationSlug: university-of-maryland-college-park-G3YK
                authorID: '11546170'
                authorName: Geo Pertea
                authorSequenceNumber: 3
                authorSlug: geo-pertea-RjjyJN
                family: Pertea
                given: Geo
              - affiliation: California Institute of Technology
                affiliationID: '9687'
                affiliationSlug: california-institute-of-technology-mb8j
                authorID: '22304516'
                authorName: Ali Mortazavi
                authorSequenceNumber: 4
                authorSlug: ali-mortazavi-Qk5wxw
                family: Mortazavi
                given: Ali
              - affiliation: California Institute of Technology
                affiliationID: '9687'
                affiliationSlug: california-institute-of-technology-mb8j
                authorID: '19605467'
                authorName: Gordon Kwan
                authorSequenceNumber: 5
                authorSlug: gordon-kwan-JlZ3pY
                family: Kwan
                given: Gordon
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '33888465'
                authorName: Marijke J. van Baren
                authorSequenceNumber: 6
                authorSlug: marijke-j-van-baren-8OG15a
                family: Baren
                given: Marijke J. van
              - affiliation: University of Maryland, College Park
                affiliationID: '2613'
                affiliationSlug: university-of-maryland-college-park-G3YK
                authorID: '483606902'
                authorName: Steven L. Salzberg
                authorSequenceNumber: 7
                authorSlug: steven-l-salzberg-9bPOnP9
                family: Salzberg
                given: Steven L.
              - affiliation: California Institute of Technology
                affiliationID: '9687'
                affiliationSlug: california-institute-of-technology-mb8j
                authorID: '13876604'
                authorName: Barbara J. Wold
                authorSequenceNumber: 8
                authorSlug: barbara-j-wold-WxmjWJ
                family: Wold
                given: Barbara J.
              - affiliation: University of California, Berkeley
                affiliationID: '19129'
                affiliationSlug: university-of-california-berkeley-rDm3
                authorID: '8878157'
                authorName: Lior Pachter
                authorSequenceNumber: 9
                authorSlug: lior-pachter-G5yZdA
                family: Pachter
                given: Lior
            doi: 10.1038/nbt.1621
            editorialNotices: []
            id: 81334047
            issns:
              - 1087-0156
              - 1546-1696
            issue: '5'
            journal: Nature Biotechnology
            journalSlug: QePXQ
            keywords:
              - Article
            memberId: 297
            normalizedTypes:
              - article
            page: 511-515
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Nat Biotechnol
            slug: transcript-assembly-and-quantification-by-14aEdn
            title: >-
              Transcript assembly and quantification by RNA-Seq reveals
              unannotated transcripts and isoform switching during cell
              differentiation
            type: journal-article
            volume: '28'
            year: 2010
          10.1038/ncb942:
            abstract: >-
              Pluripotent mesenchymal stem cells in bone marrow differentiate
              into adipocytes, osteoblasts and other cells. Balanced
              cytodifferentiation of stem cells is essential for the formation
              and maintenance of bone marrow; however, the mechanisms that
              control this balance remain largely unknown. Whereas cytokines
              such as interleukin-1 (IL-1) and tumour-necrosis factor-alpha
              (TNF-alpha) inhibit adipogenesis, the ligand-induced transcription
              factor peroxisome proliferator-activated receptor-gamma
              (PPAR-gamma), is a key inducer of adipogenesis. Therefore,
              regulatory coupling between cytokine- and PPAR-gamma-mediated
              signals might occur during adipogenesis. Here we show that the
              ligand-induced transactivation function of PPAR-gamma is
              suppressed by IL-1 and TNF-alpha, and that this suppression is
              mediated through NF-kappaB activated by the
              TAK1/TAB1/NF-kappaB-inducing kinase (NIK) cascade, a downstream
              cascade associated with IL-1 and TNF-alpha signalling. Unlike
              suppression of the PPAR-gamma transactivation function by
              mitogen-activated protein kinase-induced growth factor signalling
              through phosphorylation of the A/B domain, NF-kappaB blocks
              PPAR-gamma binding to DNA by forming a complex with PPAR-gamma and
              its AF-1-specific co-activator PGC-2. Our results suggest that
              expression of IL-1 and TNF-alpha in bone marrow may alter the fate
              of pluripotent mesenchymal stem cells, directing cellular
              differentiation towards osteoblasts rather than adipocytes by
              suppressing PPAR-gamma function through NF-kappaB activated by the
              TAK1/TAB1/NIK cascade.
            authors:
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '385146832'
                authorName: Miyuki Suzawa
                authorSequenceNumber: 1
                authorSlug: miyuki-suzawa-2WX942D
                family: Suzawa
                given: Miyuki
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '10649873'
                authorName: Ichiro Takada
                authorSequenceNumber: 2
                authorSlug: ichiro-takada-rxwyEA
                family: Takada
                given: Ichiro
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '140018780'
                authorName: Junn Yanagisawa
                authorSequenceNumber: 3
                authorSlug: junn-yanagisawa-lxgANM
                family: Yanagisawa
                given: Junn
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '7433361'
                authorName: Fumiaki Ohtake
                authorSequenceNumber: 4
                authorSlug: fumiaki-ohtake-EWvNmW
                family: Ohtake
                given: Fumiaki
              - affiliation: National Institute for Basic Biology
                affiliationID: '7342'
                affiliationSlug: national-institute-for-basic-biology-4ZMN
                authorID: '28753366'
                authorName: Satoko Ogawa
                authorSequenceNumber: 5
                authorSlug: satoko-ogawa-xxjk4g
                family: Ogawa
                given: Satoko
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '8070377'
                authorName: Toshimasa Yamauchi
                authorSequenceNumber: 6
                authorSlug: toshimasa-yamauchi-ng0ZPN
                family: Yamauchi
                given: Toshimasa
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '205520820'
                authorName: Toshimasa Yamauchi
                authorSequenceNumber: 6
                authorSlug: toshimasa-yamauchi-y8waOn6
                family: Yamauchi
                given: Toshimasa
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '261239592'
                authorName: Takashi Kadowaki
                authorSequenceNumber: 7
                authorSlug: takashi-kadowaki-W8Lmzyg
                family: Kadowaki
                given: Takashi
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '81359524'
                authorName: Yasuhiro Takeuchi
                authorSequenceNumber: 8
                authorSlug: yasuhiro-takeuchi-klWy5y
                family: Takeuchi
                given: Yasuhiro
              - affiliation: National Institute for Basic Biology
                affiliationID: '7342'
                affiliationSlug: national-institute-for-basic-biology-4ZMN
                authorID: '76280891'
                authorName: Hiroshi Shibuya
                authorSequenceNumber: 9
                authorSlug: hiroshi-shibuya-1Qj4Jy
                family: Shibuya
                given: Hiroshi
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '27430905'
                authorName: Yukiko Gotoh
                authorSequenceNumber: 10
                authorSlug: yukiko-gotoh-ADKWQe
                family: Gotoh
                given: Yukiko
              - affiliation: Nagoya University
                affiliationID: '8173'
                affiliationSlug: nagoya-university-rLD3
                authorID: '19915519'
                authorName: Kunihiro Matsumoto
                authorSequenceNumber: 11
                authorSlug: kunihiro-matsumoto-DR9k0e
                family: Matsumoto
                given: Kunihiro
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '144333332'
                authorName: Shigeaki Kato
                authorSequenceNumber: 12
                authorSlug: shigeaki-kato-25kG4L
                family: Kato
                given: Shigeaki
            doi: 10.1038/ncb942
            editorialNotices:
              - date: '2014-10-31'
                doi: 10.1038/ncb942
                noticeDoi: 10.1038/ncb3068
                status: Has correction
              - date: '2014-10-31'
                doi: 10.1038/ncb942
                noticeDoi: 10.1038/ncb3068
                status: Retracted
            id: 81351309
            issns:
              - 1465-7392
              - 1476-4679
            issue: '3'
            journal: Nature Cell Biology
            journalSlug: r6W4d
            memberId: 297
            normalizedTypes:
              - article
            page: 224-230
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Nat Cell Biol
            slug: cytokines-suppress-adipogenesis-and-ppar-vNbgV3
            title: >-
              Cytokines suppress adipogenesis and PPAR-γ function through the
              TAK1/TAB1/NIK cascade
            type: journal-article
            volume: '5'
            year: 2003
          10.1038/nm.1964:
            authors:
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '18891380'
                authorName: Satoshi Nishimura
                authorSequenceNumber: 1
                authorSlug: satoshi-nishimura-l6ZN43
                family: Nishimura
                given: Satoshi
              - authorID: '6401907'
                authorName: Ichiro Manabe
                authorSequenceNumber: 2
                authorSlug: ichiro-manabe-YZEjM3
                family: Manabe
                given: Ichiro
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '9353705'
                authorName: Mika Nagasaki
                authorSequenceNumber: 3
                authorSlug: mika-nagasaki-AN2nlZ
                family: Nagasaki
                given: Mika
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '9615874'
                authorName: Koji Eto
                authorSequenceNumber: 4
                authorSlug: koji-eto-pxWeez
                family: Eto
                given: Koji
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '23923457'
                authorName: Hiroshi Yamashita
                authorSequenceNumber: 5
                authorSlug: hiroshi-yamashita-Gayxab
                family: Yamashita
                given: Hiroshi
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '14720946'
                authorName: Mitsuru Ohsugi
                authorSequenceNumber: 6
                authorSlug: mitsuru-ohsugi-9DV5G9
                family: Ohsugi
                given: Mitsuru
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '7024481'
                authorName: Makoto Otsu
                authorSequenceNumber: 7
                authorSlug: makoto-otsu-jMAG0d
                family: Otsu
                given: Makoto
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '178577914'
                authorName: Hara Kazuo
                authorSequenceNumber: 8
                authorSlug: hara-kazuo-gZXDjDz
                family: Kazuo
                given: Hara
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '7998801'
                authorName: Kohjiro Ueki
                authorSequenceNumber: 9
                authorSlug: kohjiro-ueki-PzVp3k
                family: Ueki
                given: Kohjiro
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '17300362'
                authorName: Seiryo Sugiura
                authorSequenceNumber: 10
                authorSlug: seiryo-sugiura-dOrO93
                family: Sugiura
                given: Seiryo
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '21167864'
                authorName: Kotaro Yoshimura
                authorSequenceNumber: 11
                authorSlug: kotaro-yoshimura-y9rmDa
                family: Yoshimura
                given: Kotaro
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '19649000'
                authorName: Takashi Kadowaki
                authorSequenceNumber: 12
                authorSlug: takashi-kadowaki-3NvpyZ
                family: Kadowaki
                given: Takashi
              - affiliation: University of Tokyo
                affiliationID: '11716'
                affiliationSlug: university-of-tokyo-QYyz
                authorID: '27486996'
                authorName: Ryozo Nagai
                authorSequenceNumber: 13
                authorSlug: ryozo-nagai-MyRJkW
                family: Nagai
                given: Ryozo
            doi: 10.1038/nm.1964
            editorialNotices: []
            id: 81413230
            issns:
              - 1078-8956
              - 1546-170X
            issue: '8'
            journal: Nature Medicine
            journalSlug: PQ3Xm
            memberId: 297
            normalizedTypes:
              - article
            page: 914-920
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Nat Med
            slug: cd8-effector-t-cells-contribute-ppmP2N
            title: >-
              CD8+ effector T cells contribute to macrophage recruitment and
              adipose tissue inflammation in obesity
            type: journal-article
            volume: '15'
            year: 2009
          10.1038/nm.2353:
            abstract: >-
              Chronic inflammation characterized by T cell and macrophage
              infiltration of visceral adipose tissue (VAT) is a hallmark of
              obesity associated insulin resistance and glucose intolerance.
              Here we demonstrate a fundamental pathogenic role for B cells in
              the development of these metabolic abnormalities. B cells
              accumulate in VAT in diet induced obese (DIO) mice, and DIO mice
              lacking B cells are protected from disease despite weight gain. B
              cell effects on glucose metabolism are mechanistically linked to
              activation of pro-inflammatory macrophages and T cells, and
              production of pathogenic IgG antibodies. Treatment with a B
              cell-depleting CD20 antibody attenuates disease, while transfer of
              DIO-IgG rapidly induces insulin resistance and glucose
              intolerance. Moreover, insulin resistance in obese humans is
              associated with a unique profile of IgG autoantibodies. These
              results establish the importance of B cells and adaptive immunity
              in insulin resistance and suggest new diagnostic and therapeutic
              modalities to manage the disease.
            authors:
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '193185945'
                authorName: Daniel A. Winer
                authorSequenceNumber: 1
                authorSlug: daniel-a-winer-PQxdEVR
                family: Winer
                given: Daniel A.
              - affiliation: University of Toronto
                affiliationID: '12922'
                affiliationSlug: university-of-toronto-xWjA
                authorID: '8957022'
                authorName: Shawn Winer
                authorSequenceNumber: 2
                authorSlug: shawn-winer-xQ9W0A
                family: Winer
                given: Shawn
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '21345297'
                authorName: Lei Shen
                authorSequenceNumber: 3
                authorSlug: lei-shen-vZ1vA3
                family: Shen
                given: Lei
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '41498331'
                authorName: Persis P. Wadia
                authorSequenceNumber: 4
                authorSlug: persis-p-wadia-Z9ynyP
                family: Wadia
                given: Persis P.
              - affiliation: University of Toronto
                affiliationID: '12922'
                affiliationSlug: university-of-toronto-xWjA
                authorID: '95448406'
                authorName: Jason Yantha
                authorSequenceNumber: 5
                authorSlug: jason-yantha-zGvNl5
                family: Yantha
                given: Jason
              - affiliation: University of Toronto
                affiliationID: '12922'
                affiliationSlug: university-of-toronto-xWjA
                authorID: '5914355'
                authorName: Geoffrey Paltser
                authorSequenceNumber: 6
                authorSlug: geoffrey-paltser-ejwg4K
                family: Paltser
                given: Geoffrey
              - affiliation: University of Toronto
                affiliationID: '12922'
                affiliationSlug: university-of-toronto-xWjA
                authorID: '20465397'
                authorName: Hubert Tsui
                authorSequenceNumber: 7
                authorSlug: hubert-tsui-vZAwmO
                family: Tsui
                given: Hubert
              - affiliation: University of Toronto
                affiliationID: '12922'
                affiliationSlug: university-of-toronto-xWjA
                authorID: '34213183'
                authorName: Ping Wu
                authorSequenceNumber: 8
                authorSlug: ping-wu-aPYG81
                family: Wu
                given: Ping
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '80922272'
                authorName: Matthew G. Davidson
                authorSequenceNumber: 9
                authorSlug: matthew-g-davidson-wN6xWe
                family: Davidson
                given: Matthew G.
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '14095121'
                authorName: Michael N. Alonso
                authorSequenceNumber: 10
                authorSlug: michael-n-alonso-8VMlE9
                family: Alonso
                given: Michael N.
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '13809772'
                authorName: Hwei X Leong
                authorSequenceNumber: 11
                authorSlug: hwei-x-leong-wZW31z
                family: Leong
                given: Hwei X
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '29260441'
                authorName: Alec J. Glassford
                authorSequenceNumber: 12
                authorSlug: alec-j-glassford-XG8y5x
                family: Glassford
                given: Alec J.
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '1250253'
                authorName: Maria Caimol
                authorSequenceNumber: 13
                authorSlug: maria-caimol-vROz2
                family: Caimol
                given: Maria
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '9862557'
                authorName: Justin A. Kenkel
                authorSequenceNumber: 14
                authorSlug: justin-a-kenkel-G5wNA3
                family: Kenkel
                given: Justin A.
              - affiliation: Duke University
                affiliationID: '6797'
                affiliationSlug: duke-university-vxKN
                authorID: '52059623'
                authorName: Thomas F. Tedder
                authorSequenceNumber: 15
                authorSlug: thomas-f-tedder-JMk3MG
                family: Tedder
                given: Thomas F.
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '18132862'
                authorName: Tracey McLaughlin
                authorSequenceNumber: 16
                authorSlug: tracey-mclaughlin-dOaj9R
                family: McLaughlin
                given: Tracey
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '7927765'
                authorName: David B. Miklos
                authorSequenceNumber: 17
                authorSlug: david-b-miklos-8gmgj2
                family: Miklos
                given: David B.
              - affiliation: University of Toronto
                affiliationID: '12922'
                affiliationSlug: university-of-toronto-xWjA
                authorID: '45908801'
                authorName: H.-M. Dosch
                authorSequenceNumber: 18
                authorSlug: h-m-dosch-PAjkgm
                family: Dosch
                given: H.-M.
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '6347955'
                authorName: Edgar G. Engleman
                authorSequenceNumber: 19
                authorSlug: edgar-g-engleman-ejQR0r
                family: Engleman
                given: Edgar G.
            doi: 10.1038/nm.2353
            editorialNotices: []
            id: 81413498
            issns:
              - 1078-8956
              - 1546-170X
            issue: '5'
            journal: Nature Medicine
            journalSlug: PQ3Xm
            keywords:
              - Article
            memberId: 297
            normalizedTypes:
              - article
            page: 610-617
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Nat Med
            slug: b-cells-promote-insulin-resistance-62GY16
            title: >-
              B cells promote insulin resistance through modulation of T cells
              and production of pathogenic IgG antibodies
            type: journal-article
            volume: '17'
            year: 2011
          10.1038/nri2921:
            abstract: >-
              The worldwide epidemic of obesity has brought cons iderable
              attention to research aimed at understanding the biology of
              adipocytes (fat cells) and the events occurring in adipose tissue
              (fat) and in the bodies of obese individuals. Accumulating
              evidence indicates that obesity causes chronic low-grade
              inflammation and that this contributes to systemic metabolic
              dysfunction that is associated with obesity-linked disorders.
              Adipose tissue functions as a key endocrine organ by releasing
              multiple bioactive substances, known as adipose-derived secreted
              factors or adipokines, that have pro-inflammatory or
              anti-inflammatory activities. Dysregulated production or secretion
              of these adipokines owing to adipose tissue dysfunction can
              contribute to the pathogenesis of obesity-linked complications. In
              this Review, we focus on the role of adipokines in inflammatory
              responses and discuss their potential as regulators of metabolic
              function.
            authors:
              - affiliation: Nagoya University
                affiliationID: '8173'
                affiliationSlug: nagoya-university-rLD3
                authorID: '25408956'
                authorName: Noriyuki Ouchi
                authorSequenceNumber: 1
                authorSlug: noriyuki-ouchi-04WLbL
                family: Ouchi
                given: Noriyuki
              - affiliation: Boston University
                affiliationID: '7891'
                affiliationSlug: boston-university-11nj
                authorID: '67379244'
                authorName: Jennifer L. Parker
                authorSequenceNumber: 2
                authorSlug: jennifer-l-parker-3aVQ5d
                family: Parker
                given: Jennifer L.
              - affiliation: Boston University
                affiliationID: '7891'
                affiliationSlug: boston-university-11nj
                authorID: '10069091'
                authorName: Jesse J. Lugus
                authorSequenceNumber: 3
                authorSlug: jesse-j-lugus-1gazl0
                family: Lugus
                given: Jesse J.
              - affiliation: Boston University
                affiliationID: '7891'
                affiliationSlug: boston-university-11nj
                authorID: '141932666'
                authorName: Kenneth Walsh
                authorSequenceNumber: 4
                authorSlug: kenneth-walsh-xODp3b
                family: Walsh
                given: Kenneth
            doi: 10.1038/nri2921
            editorialNotices: []
            id: 81483874
            issns:
              - 1474-1733
              - 1474-1741
            issue: '2'
            journal: Nature Reviews Immunology
            journalSlug: lZ5yr
            keywords:
              - Article
            memberId: 297
            normalizedTypes:
              - article
            page: 85-97
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Nat Rev Immunol
            slug: adipokines-in-inflammation-and-metabolic-ppPW3w
            title: Adipokines in inflammation and metabolic disease
            type: journal-article
            volume: '11'
            year: 2011
          10.1038/oby.2009.192:
            abstract: >-
              Inflammation and insulin resistance associated with visceral
              obesity are important risk factors for the development of type 2
              diabetes, atherosclerosis, and the metabolic syndrome. The
              12/15‐lipoxygenase (12/15‐LO) enzyme has been linked to
              inflammatory changes in blood vessels that precede the development
              of atherosclerosis. The expression and role of 12/15‐LO in
              adipocytes have not been evaluated. We found that 12/15‐LO mRNA
              was dramatically upregulated in white epididymal adipocytes of
              high‐fat fed mice. 12/15‐LO was poorly expressed in 3T3‐L1
              fibroblasts and was upregulated during differentiation into
              adipocytes. Interestingly, the saturated fatty acid palmitate, a
              major component of high fat diets, augmented expression of
              12/15‐LO in vitro. When 3T3‐L1 adipocytes were treated with the
              12/15‐LO products, 12‐hydroxyeicosatetranoic acid (12(S)‐HETE) and
              12‐hydroperoxyeicosatetraenoic acid (12(S)‐HPETE), expression of
              proinflammatory cytokine genes, including tumor necrosis factor‐α
              (TNF‐α), monocyte chemoattractant protein 1 (MCP‐1), interleukin 6
              (IL‐6), and IL‐12p40, was upregulated whereas anti‐inflammatory
              adiponectin gene expression was downregulated. 12/15‐LO products
              also augmented c‐Jun N‐terminal kinase 1 (JNK‐1) phosphorylation,
              a known negative regulator of insulin signaling. Consistent with
              impaired insulin signaling, we found that insulin‐stimulated
              3T3‐L1 adipocytes exhibited decreased IRS‐1(Tyr) phosphorylation,
              increased IRS‐1(Ser) phosphorylation, and impaired Akt
              phosphorylation when treated with 12/15‐LO product. Taken
              together, our data suggest that 12/15‐LO products create a
              proinflammatory state and impair insulin signaling in 3T3‐L1
              adipocytes. Because 12/15‐LO expression is upregulated in visceral
              adipocytes by high‐fat feeding in vivo and also by addition of
              palmitic acid in vitro, we propose that 12/15‐LO plays a role in
              promoting inflammation and insulin resistance associated with
              obesity.
            authors:
              - affiliation: Eastern Virginia Medical School
                affiliationID: '382'
                affiliationSlug: eastern-virginia-medical-school-VLP
                authorID: '63079324'
                authorName: Swarup K. Chakrabarti
                authorSequenceNumber: 1
                authorSlug: swarup-k-chakrabarti-kEaKjX
                family: Chakrabarti
                given: Swarup K.
              - affiliation: Eastern Virginia Medical School
                affiliationID: '382'
                affiliationSlug: eastern-virginia-medical-school-VLP
                authorID: '12170150'
                authorName: Banumathi K. Cole
                authorSequenceNumber: 2
                authorSlug: banumathi-k-cole-zL3839
                family: Cole
                given: Banumathi K.
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '54942341'
                authorName: Yeshao Wen
                authorSequenceNumber: 3
                authorSlug: yeshao-wen-XOmWlw
                family: Wen
                given: Yeshao
              - affiliation: University of Virginia
                affiliationID: '26257'
                affiliationSlug: university-of-virginia-GAeJ
                authorID: '19537263'
                authorName: Susanna R. Keller
                authorSequenceNumber: 4
                authorSlug: susanna-r-keller-DROWMN
                family: Keller
                given: Susanna R.
              - affiliation: Eastern Virginia Medical School
                affiliationID: '382'
                affiliationSlug: eastern-virginia-medical-school-VLP
                authorID: '16259863'
                authorName: Jerry L. Nadler
                authorSequenceNumber: 5
                authorSlug: jerry-l-nadler-DmQA4W
                family: Nadler
                given: Jerry L.
            doi: 10.1038/oby.2009.192
            editorialNotices: []
            id: 81510862
            issns:
              - 1930-7381
            issue: '9'
            journal: Obesity
            journalSlug: V01EE
            keywords:
              - Article
            memberId: 311
            normalizedTypes:
              - article
            page: 1657-1663
            preprintLinks: []
            publicationLinks: []
            publisher: Wiley
            retracted: false
            slug: 12-15-lipoxygenase-products-induce-inflammation-and-dl8jmy
            title: >-
              12/15-Lipoxygenase Products Induce Inflammation and Impair Insulin
              Signaling in 3T3-L1 Adipocytes
            type: journal-article
            volume: '17'
            year: 2009
          10.1038/s41598-017-06397-4:
            abstract: >-
              Eosinophils and their associated cytokines IL-4 and IL-5 are
              emerging as central orchestrators of the immune-metabolic axis.
              Herein, we demonstrate that cross-talk between the Ig-superfamily
              receptor CD300f and IL-5 is a key checkpoint that modifies the
              ability of eosinophils to regulate metabolic outcomes. Generation
              of Il5

              Tg

              /Cd300f

              −/− mice revealed marked and distinct increases in eosinophil
              levels and their production of IL-4 in the white and brown adipose
              tissues. Consequently, Il5

              Tg

              /Cd300f

              −/− mice had increased alternatively activated macrophage
              accumulation in the adipose tissue. Cd300f

              −/− mice displayed age-related accumulation of eosinophils and
              macrophages in the adipose tissue and decreased adipose tissue
              weight, which was associated with decreased diet-induced weight
              gain and insulin resistance. Notably, Il5

              Tg

              /CD300f

              −/− were protected from diet-induced weight gain and glucose
              intolerance. These findings highlight the cross-talk between IL-5
              receptor and CD300f as a novel pathway regulating adipose tissue
              eosinophils and offer new entry points for therapeutic
              intervention for obesity and its complications.
            authors:
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '11006029'
                authorName: Perri Rozenberg
                authorSequenceNumber: 1
                authorSlug: perri-rozenberg-rx4Y46
                family: Rozenberg
                given: Perri
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '28124321'
                authorName: Hadar Reichman
                authorSequenceNumber: 2
                authorSlug: hadar-reichman-86K6Gm
                family: Reichman
                given: Hadar
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '131934550'
                authorName: Israel Zab-Bar
                authorSequenceNumber: 3
                authorSlug: israel-zab-bar-zypaVK
                family: Zab-Bar
                given: Israel
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '5216739'
                authorName: Michal Itan
                authorSequenceNumber: 4
                authorSlug: michal-itan-aXkmEv
                family: Itan
                given: Michal
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '14034264'
                authorName: Metsada Pasmanik-Chor
                authorSequenceNumber: 5
                authorSlug: metsada-pasmanik-chor-yg6YJG
                family: Pasmanik-Chor
                given: Metsada
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '297869'
                authorName: Carine Bouffi
                authorSequenceNumber: 6
                authorSlug: carine-bouffi-5M2WA
                family: Bouffi
                given: Carine
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '1662244'
                authorName: Udi Qimron
                authorSequenceNumber: 7
                authorSlug: udi-qimron-3Gkwy
                family: Qimron
                given: Udi
              - authorID: '7517075'
                authorName: Ido Bachelet
                authorSequenceNumber: 8
                authorSlug: ido-bachelet-ZxQm0r
                family: Bachelet
                given: Ido
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '7740496'
                authorName: Patricia C. Fulkerson
                authorSequenceNumber: 9
                authorSlug: patricia-c-fulkerson-M22g0m
                family: Fulkerson
                given: Patricia C.
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '11358116'
                authorName: Marc E. Rothenberg
                authorSequenceNumber: 10
                authorSlug: marc-e-rothenberg-QmeOgJ
                family: Rothenberg
                given: Marc E.
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '121132203'
                authorName: Ariel Munitz
                authorSequenceNumber: 11
                authorSlug: ariel-munitz-19xRJy
                family: Munitz
                given: Ariel
            doi: 10.1038/s41598-017-06397-4
            editorialNotices: []
            id: 233718020
            issns:
              - 2045-2322
            issue: '1'
            journal: Scientific Reports
            journalSlug: n6W5k
            keywords:
              - Article
            memberId: 297
            normalizedTypes:
              - article
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Sci Rep
            slug: cd300f-il-5-cross-talk-inhibits-adipose-tissue-y8Q5z9p
            title: >-
              CD300f:IL-5 cross-talk inhibits adipose tissue eosinophil homing
              and subsequent IL-4 production
            type: journal-article
            volume: '7'
            year: 2017
          10.1038/s41598-018-28371-4:
            abstract: >-
              Accumulating data have indicated a fundamental role of eosinophils
              in regulating adipose tissue homeostasis. Here, we performed
              whole-genome RNA sequencing of the small intestinal tract, which
              suggested the presence of impaired lipid metabolism in
              eosinophil-deficient ΔdblGATA mice. ΔdblGATA mice fed a high-fat
              diet (HFD) showed reduced body fat mass, impaired enlargement of
              adipocytes, decreased expression of adipogenic genes, and
              developed glucose intolerance. HFD induced accumulation of
              eosinophils in the perigonadal white adipose tissue. Concordantly,
              adipocyte-differentiated 3T3-L1 cells promoted the migration of
              eosinophils through the expression of CCL11 (eotaxin-1) and likely
              promoted their survival through the expression of interleukin
              (IL)-3, IL-5, and granulocyte-macrophage colony-stimulating
              factor. HFD-fed ΔdblGATA mice showed increased infiltration of
              macrophages, CD4+ T-cells, and B-cells, increased expression of
              interferon-γ, and decreased expression of IL-4 and IL-13 in white
              adipose tissue. Interferon-γ treatment significantly decreased
              lipid deposition in adipocyte-differentiated 3T3-L1 cells, while
              IL-4 treatment promoted lipid accumulation. Notably, HFD-fed
              ΔdblGATA mice showed increased lipid storage in the liver as
              compared with wild-type mice. We propose that obesity promotes the
              infiltration of eosinophils into adipose tissue that subsequently
              contribute to the metabolic homeostasis by promoting adipocyte
              maturation.
            authors:
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '152962979'
                authorName: Eun-Hui Lee
                authorSequenceNumber: 1
                authorSlug: eun-hui-lee-KQMmMe
                family: Lee
                given: Eun-Hui
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '5216739'
                authorName: Michal Itan
                authorSequenceNumber: 2
                authorSlug: michal-itan-aXkmEv
                family: Itan
                given: Michal
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '152979076'
                authorName: Jinsun Jang
                authorSequenceNumber: 3
                authorSlug: jinsun-jang-2Zd5bY
                family: Jang
                given: Jinsun
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '152933925'
                authorName: Hyeon-Jung Gu
                authorSequenceNumber: 4
                authorSlug: hyeon-jung-gu-5O8x8G
                family: Gu
                given: Hyeon-Jung
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '11006029'
                authorName: Perri Rozenberg
                authorSequenceNumber: 5
                authorSlug: perri-rozenberg-rx4Y46
                family: Rozenberg
                given: Perri
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '4965324'
                authorName: Melissa K. Mingler
                authorSequenceNumber: 6
                authorSlug: melissa-k-mingler-kenLwL
                family: Mingler
                given: Melissa K.
              - affiliation: Cincinnati Children's Hospital Medical Center
                affiliationID: '16374'
                affiliationSlug: cincinnati-children-s-hospital-medical-center-pADQ
                authorID: '17384861'
                authorName: Ting Wen
                authorSequenceNumber: 7
                authorSlug: ting-wen-EOXp5P
                family: Wen
                given: Ting
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '38694820'
                authorName: Jiyoung Yoon
                authorSequenceNumber: 8
                authorSlug: jiyoung-yoon-ywPwN6
                family: Yoon
                given: Jiyoung
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '52112172'
                authorName: Shi-Young Park
                authorSequenceNumber: 9
                authorSlug: shi-young-park-wXpAje
                family: Park
                given: Shi-Young
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '12711292'
                authorName: Joo Young Roh
                authorSequenceNumber: 10
                authorSlug: joo-young-roh-WxV0zQ
                family: Roh
                given: Joo Young
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '8946745'
                authorName: Cheol Soo Choi
                authorSequenceNumber: 11
                authorSlug: cheol-soo-choi-PzKQ1V
                family: Choi
                given: Cheol Soo
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '152936204'
                authorName: Woo-Jae Park
                authorSequenceNumber: 12
                authorSlug: woo-jae-park-Wwy42O
                family: Park
                given: Woo-Jae
              - affiliation: Tel Aviv University
                affiliationID: '12679'
                affiliationSlug: tel-aviv-university-KPbp
                authorID: '121132203'
                authorName: Ariel Munitz
                authorSequenceNumber: 13
                authorSlug: ariel-munitz-19xRJy
                family: Munitz
                given: Ariel
              - affiliation: Gachon University
                affiliationID: '9120'
                affiliationSlug: gachon-university-yJdl
                authorID: '139679076'
                authorName: Yun-Jae Jung
                authorSequenceNumber: 14
                authorSlug: yun-jae-jung-2PO1JE
                family: Jung
                given: Yun-Jae
            doi: 10.1038/s41598-018-28371-4
            editorialNotices: []
            id: 223144610
            issns:
              - 2045-2322
            issue: '1'
            journal: Scientific Reports
            journalSlug: n6W5k
            keywords:
              - Article
            memberId: 297
            normalizedTypes:
              - article
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Sci Rep
            slug: eosinophils-support-adipocyte-maturation-and-68jbdR1
            title: >-
              Eosinophils support adipocyte maturation and promote glucose
              tolerance in obesity
            type: journal-article
            volume: '8'
            year: 2018
          10.1053/j.gastro.2013.04.010:
            abstract: >-
              BACKGROUND & AIMS

              An increased number of macrophages in adipose tissue is associated
              with insulin resistance and metabolic dysfunction in obese people.
              However, little is known about other immune cells in adipose
              tissue from obese people, and whether they contribute to insulin
              resistance. We investigated the characteristics of T cells in
              adipose tissue from metabolically abnormal insulin-resistant obese
              (MAO) subjects, metabolically normal insulin-sensitive obese (MNO)
              subjects, and lean subjects. Insulin sensitivity was determined by
              using the hyperinsulinemic euglycemic clamp procedure.



              METHODS

              We assessed plasma cytokine concentrations and subcutaneous
              adipose tissue CD4+ T-cell populations in 9 lean, 12 MNO, and 13
              MAO subjects. Skeletal muscle and liver samples were collected
              from 19 additional obese patients undergoing bariatric surgery to
              determine the presence of selected cytokine receptors.



              RESULTS

              Adipose tissue from MAO subjects had 3- to 10-fold increases in
              numbers of CD4+ T cells that produce interleukin (IL)-22 and IL-17
              (a T-helper [Th] 17 and Th22 phenotype) compared with MNO and lean
              subjects. MAO subjects also had increased plasma concentrations of
              IL-22 and IL-6. Receptors for IL-17 and IL-22 were expressed in
              human liver and skeletal muscle samples. IL-17 and IL-22 inhibited
              uptake of glucose in skeletal muscle isolated from rats and
              reduced insulin sensitivity in cultured human hepatocytes.



              CONCLUSIONS

              Adipose tissue from MAO individuals contains increased numbers of
              Th17 and Th22 cells, which produce cytokines that cause metabolic
              dysfunction in liver and muscle in vitro. Additional studies are
              needed to determine whether these alterations in adipose tissue T
              cells contribute to the pathogenesis of insulin resistance in
              obese people.
            authors:
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '6328562'
                authorName: Elisa Fabbrini
                authorSequenceNumber: 1
                authorSlug: elisa-fabbrini-dvbLj1
                family: Fabbrini
                given: Elisa
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '19860613'
                authorName: Marina Cella
                authorSequenceNumber: 2
                authorSlug: marina-cella-G6AaLL
                family: Cella
                given: Marina
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '64542774'
                authorName: Steve A. Mccartney
                authorSequenceNumber: 3
                authorSlug: steve-a-mccartney-pVLNLw
                family: Mccartney
                given: Steve A.
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '8082696'
                authorName: Anja Fuchs
                authorSequenceNumber: 4
                authorSlug: anja-fuchs-M21g8X
                family: Fuchs
                given: Anja
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '1846449'
                authorName: Nada A. Abumrad
                authorSequenceNumber: 5
                authorSlug: nada-a-abumrad-A2edE
                family: Abumrad
                given: Nada A.
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '10659883'
                authorName: Terri A. Pietka
                authorSequenceNumber: 6
                authorSlug: terri-a-pietka-ayennj
                family: Pietka
                given: Terri A.
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '13723397'
                authorName: Zhouji Chen
                authorSequenceNumber: 7
                authorSlug: zhouji-chen-vxOdk3
                family: Chen
                given: Zhouji
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '22224481'
                authorName: Brian N. Finck
                authorSequenceNumber: 8
                authorSlug: brian-n-finck-jzYEOy
                family: Finck
                given: Brian N.
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '154715410'
                authorName: Dong Ho Han
                authorSequenceNumber: 9
                authorSlug: dong-ho-han-6aL9xE
                family: Han
                given: Dong Ho
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '865583'
                authorName: Faidon Magkos
                authorSequenceNumber: 10
                authorSlug: faidon-magkos-amb81
                family: Magkos
                given: Faidon
              - affiliation: Sapienza University of Rome
                affiliationID: '7808'
                affiliationSlug: sapienza-university-of-rome-MlVW
                authorID: '147884582'
                authorName: Caterina Conte
                authorSequenceNumber: 11
                authorSlug: caterina-conte-VlGK1W
                family: Conte
                given: Caterina
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '19312583'
                authorName: Steven M. Bradley
                authorSequenceNumber: 12
                authorSlug: steven-m-bradley-aYn5R1
                family: Bradley
                given: Steven M.
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '15028188'
                authorName: David Bradley
                authorSequenceNumber: 12
                authorSlug: david-bradley-3KA3LW
                family: Bradley
                given: David
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '28339390'
                authorName: Gemma Fraterrigo
                authorSequenceNumber: 13
                authorSlug: gemma-fraterrigo-9x84Rb
                family: Fraterrigo
                given: Gemma
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '2597312'
                authorName: J. Christopher Eagon
                authorSequenceNumber: 14
                authorSlug: j-christopher-eagon-0V2gZ
                family: Eagon
                given: J. Christopher
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '17244299'
                authorName: Bruce W. Patterson
                authorSequenceNumber: 15
                authorSlug: bruce-w-patterson-eD8zK0
                family: Patterson
                given: Bruce W.
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '9938079'
                authorName: Marco Colonna
                authorSequenceNumber: 16
                authorSlug: marco-colonna-KWXmvd
                family: Colonna
                given: Marco
              - affiliation: Washington University in St. Louis
                affiliationID: '19037'
                affiliationSlug: washington-university-in-st-louis-jjaJ
                authorID: '13449418'
                authorName: Samuel Klein
                authorSequenceNumber: 17
                authorSlug: samuel-klein-dKZeXy
                family: Klein
                given: Samuel
            doi: 10.1053/j.gastro.2013.04.010
            editorialNotices: []
            id: 83257460
            issns:
              - 0016-5085
            issue: '2'
            journal: Gastroenterology
            journalSlug: pnmJj
            keywords:
              - Article
            memberId: 78
            normalizedTypes:
              - article
            page: 366-374.e3
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Gastroenterology
            slug: association-between-specific-adipose-tissue-QpEVZJ
            title: >-
              Association Between Specific Adipose Tissue CD4+ T-Cell
              Populations and Insulin Resistance in Obese Individuals
            type: journal-article
            volume: '145'
            year: 2013
          10.1074/jbc.275.12.8456:
            abstract: >-
              Insulin resistance is a major factor in the pathogenesis of type 2
              diabetes and may be related to alterations in fat metabolism.
              Fatless mice have been created using dominant-negative protein
              (A-ZIP/F-1) targeted gene expression in the adipocyte and shown to
              develop diabetes. To understand the mechanism responsible for the
              insulin resistance in these mice, we conducted
              hyperinsulinemic-euglycemic clamps in awake fatless and wild type
              littermates before the development of diabetes and examined
              insulin action and signaling in muscle and liver. We found the
              fatless mice to be severely insulinresistant, which could be
              attributed to defects in insulin action in muscle and liver. Both
              of these abnormalities were associated with defects in insulin
              activation of insulin receptor substrate-1 and -2-associated
              phosphatidylinositol 3-kinase activity and a 2-fold increase in
              muscle and liver triglyceride content. We also show that upon
              transplantation of fat tissue into these mice, triglyceride
              content in muscle and liver returned to normal as does insulin
              signaling and action. In conclusion, these results suggest that
              the development of insulin resistance in type 2 diabetes may be
              due to alterations in the partitioning of fat between the
              adipocyte and muscle/liver leading to accumulation of triglyceride
              in the latter tissues with subsequent impairment of insulin
              signaling and action.
            authors:
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '15023009'
                authorName: Jason K. Kim
                authorSequenceNumber: 1
                authorSlug: jason-k-kim-vdg5aJ
                family: Kim
                given: Jason K.
              - affiliation: National Institutes of Health
                affiliationID: '26753'
                affiliationSlug: national-institutes-of-health-vVaJ
                authorID: '17567133'
                authorName: Oksana Gavrilova
                authorSequenceNumber: 2
                authorSlug: oksana-gavrilova-nz5X46
                family: Gavrilova
                given: Oksana
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '92152483'
                authorName: Yan Chen
                authorSequenceNumber: 3
                authorSlug: yan-chen-aZwp6r
                family: Chen
                given: Yan
              - affiliation: National Institutes of Health
                affiliationID: '26753'
                affiliationSlug: national-institutes-of-health-vVaJ
                authorID: '6596888'
                authorName: Marc L. Reitman
                authorSequenceNumber: 4
                authorSlug: marc-l-reitman-3n1GLy
                family: Reitman
                given: Marc L.
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '5886223'
                authorName: Gerald I. Shulman
                authorSequenceNumber: 5
                authorSlug: gerald-i-shulman-J1LvKY
                family: Shulman
                given: Gerald I.
            doi: 10.1074/jbc.275.12.8456
            editorialNotices: []
            id: 85706041
            issns:
              - 0021-9258
            issue: '12'
            journal: Journal of Biological Chemistry
            journalSlug: MVW30
            memberId: 78
            normalizedTypes:
              - article
            page: 8456-8460
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Journal of Biological Chemistry
            slug: mechanism-of-insulin-resistance-in-XR5Emw
            title: Mechanism of Insulin Resistance in A-ZIP/F-1 Fatless Mice
            type: journal-article
            volume: '275'
            year: 2000
          10.1074/jbc.m109.061655:
            abstract: >-
              Recent reports demonstrate T-cell infiltration of adipose tissue
              in early obesity. We hypothesized that interferon (IFN) ␥, a major
              T-cell inflammatory cytokine, would attenuate human adipocyte
              functions and sought to establish signaling mechanisms.
              Differentiated human adipocytes were treated with IFN␥ ؎
              pharmacological inhibitors prior to insulin stimulation.
            authors:
              - affiliation: University of Pennsylvania
                affiliationID: '15362'
                affiliationSlug: university-of-pennsylvania-dN49
                authorID: '8092877'
                authorName: Fiona C. McGillicuddy
                authorSequenceNumber: 1
                authorSlug: fiona-c-mcgillicuddy-ngJQX6
                family: McGillicuddy
                given: Fiona C.
              - affiliation: Cardiovascular Institute of the South
                affiliationID: '5887'
                affiliationSlug: cardiovascular-institute-of-the-south-meOY
                authorID: '104629'
                authorName: Elise H. Chiquoine
                authorSequenceNumber: 2
                authorSlug: elise-h-chiquoine-r6j64
                family: Chiquoine
                given: Elise H.
              - affiliation: Cardiovascular Institute of the South
                affiliationID: '5887'
                affiliationSlug: cardiovascular-institute-of-the-south-meOY
                authorID: '10676726'
                authorName: Christine C. Hinkle
                authorSequenceNumber: 3
                authorSlug: christine-c-hinkle-R5nOrD
                family: Hinkle
                given: Christine C.
              - affiliation: Children's Hospital of Philadelphia
                affiliationID: '25227'
                affiliationSlug: children-s-hospital-of-philadelphia-N0lg
                authorID: '20859841'
                authorName: Roy J. Kim
                authorSequenceNumber: 4
                authorSlug: roy-j-kim-XEa5Ql
                family: Kim
                given: Roy J.
              - affiliation: Children's Hospital of Philadelphia
                affiliationID: '25227'
                affiliationSlug: children-s-hospital-of-philadelphia-N0lg
                authorID: '12514307'
                authorName: Rachana Shah
                authorSequenceNumber: 5
                authorSlug: rachana-shah-YD4pyD
                family: Shah
                given: Rachana
              - affiliation: University College Dublin
                affiliationID: '6020'
                affiliationSlug: university-college-dublin-ygJa
                authorID: '15444403'
                authorName: Helen M. Roche
                authorSequenceNumber: 6
                authorSlug: helen-m-roche-115v4W
                family: Roche
                given: Helen M.
              - affiliation: University of Pennsylvania
                affiliationID: '15362'
                affiliationSlug: university-of-pennsylvania-dN49
                authorID: '8509012'
                authorName: Emer M. Smyth
                authorSequenceNumber: 7
                authorSlug: emer-m-smyth-0aOj4y
                family: Smyth
                given: Emer M.
              - affiliation: Cardiovascular Institute of the South
                affiliationID: '5887'
                affiliationSlug: cardiovascular-institute-of-the-south-meOY
                authorID: '14621088'
                authorName: Muredach P. Reilly
                authorSequenceNumber: 8
                authorSlug: muredach-p-reilly-3MPJrd
                family: Reilly
                given: Muredach P.
            doi: 10.1074/jbc.m109.061655
            editorialNotices: []
            id: 85722044
            issns:
              - 0021-9258
            issue: '46'
            journal: Journal of Biological Chemistry
            journalSlug: MVW30
            memberId: 78
            normalizedTypes:
              - article
            page: 31936-31944
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Journal of Biological Chemistry
            slug: interferon-attenuates-insulin-signaling-3kRe2y
            title: >-
              Interferon γ Attenuates Insulin Signaling, Lipid Storage, and
              Differentiation in Human Adipocytes via Activation of the JAK/STAT
              Pathway
            type: journal-article
            volume: '284'
            year: 2009
          10.1074/jbc.m114.628487:
            authors:
              - authorID: '15368351'
                authorName: R. Grace Walton
                authorSequenceNumber: 1
                authorSlug: r-grace-walton-YXX9NE
                family: Walton
                given: R. Grace
              - authorID: '72555609'
                authorName: Beibei Zhu
                authorSequenceNumber: 2
                authorSlug: beibei-zhu-vn5WxZ
                family: Zhu
                given: Beibei
              - affiliation: Muğla University
                affiliationID: '25281'
                affiliationSlug: mugla-university-jd6O
                authorID: '14893089'
                authorName: Resat Unal
                authorSequenceNumber: 3
                authorSlug: resat-unal-PD5NMb
                family: Unal
                given: Resat
              - authorID: '20249405'
                authorName: Michael L. Spencer
                authorSequenceNumber: 4
                authorSlug: michael-l-spencer-AOakaE
                family: Spencer
                given: Michael L.
              - authorID: '8655003'
                authorName: Manjula Sunkara
                authorSequenceNumber: 5
                authorSlug: manjula-sunkara-1gvwGy
                family: Sunkara
                given: Manjula
              - authorID: '13056434'
                authorName: Andrew J. Morris
                authorSequenceNumber: 6
                authorSlug: andrew-j-morris-OMeWVA
                family: Morris
                given: Andrew J.
              - authorID: '16010415'
                authorName: Richard Charnigo
                authorSequenceNumber: 7
                authorSlug: richard-charnigo-bj6408
                family: Charnigo
                given: Richard
              - authorID: '12419796'
                authorName: Wendy S. Katz
                authorSequenceNumber: 8
                authorSlug: wendy-s-katz-Mae60l
                family: Katz
                given: Wendy S.
              - affiliation: University of Kentucky
                affiliationID: '15265'
                affiliationSlug: university-of-kentucky-86Z3
                authorID: '25982711'
                authorName: Alan Daugherty
                authorSequenceNumber: 9
                authorSlug: alan-daugherty-e14XaK
                family: Daugherty
                given: Alan
              - affiliation: University of Kentucky
                affiliationID: '15265'
                affiliationSlug: university-of-kentucky-86Z3
                authorID: '201658'
                authorName: Deborah A. Howatt
                authorSequenceNumber: 10
                authorSlug: deborah-a-howatt-g1jRA
                family: Howatt
                given: Deborah A.
              - authorID: '50346380'
                authorName: Philip A. Kern
                authorSequenceNumber: 11
                authorSlug: philip-a-kern-ldGZgv
                family: Kern
                given: Philip A.
              - authorID: '24271720'
                authorName: Brian S. Finlin
                authorSequenceNumber: 12
                authorSlug: brian-s-finlin-yAM4ZR
                family: Finlin
                given: Brian S.
            doi: 10.1074/jbc.m114.628487
            editorialNotices: []
            id: 85742367
            issns:
              - 0021-9258
            issue: '18'
            journal: Journal of Biological Chemistry
            journalSlug: MVW30
            memberId: 78
            normalizedTypes:
              - article
            page: 11547-11556
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Journal of Biological Chemistry
            slug: increasing-adipocyte-lipoprotein-lipase-improves-JQegAn
            title: >-
              Increasing Adipocyte Lipoprotein Lipase Improves Glucose
              Metabolism in High Fat Diet-induced Obesity
            type: journal-article
            volume: '290'
            year: 2015
          10.1080/2162402x.2015.1056442:
            abstract: >-
              Hypoxia is a common feature of solid tumors, particularly in
              glioblastoma (GBM), and known to be a poor prognosis factor in GBM
              patients. The growth of GBM is also associated with a marked
              inflammation partially characterized by an accumulation of
              macrophage (MΦ) of the M2 phenotype. However, the transition
              between M1 MΦ (antitumoral) and M2 MΦ (protumoral) phenotypes is a
              dynamic process. We made the assumption that oxygen (O2)
              availability could be a major regulator of this transition and
              that the intratumoral O2 gradient is of importance. We evaluated,
              in vivo, the impact of hypoxia on MΦ tropism and polarization in
              two models of human GBM, well differentiated by their degree of
              hypoxia. MΦ migration in the tumor was more pronounced in the more
              hypoxic tumor of the two GBM models. In the more hypoxic of the
              models, we have shown that MΦ migrated at the tumor site only when
              hypoxia takes place. We also demonstrated that the acquisition of
              the M2 phenotype was clearly an evolving phenomenon with hypoxia
              as the major trigger for this transition. In support of these in
              vivo finding, M0 but also M1 MΦ cultured in moderate or severe
              hypoxia displayed a phenotype close to that of M2 MΦ whose
              phenotype was further reinforced by severe hypoxia. These results
              highlight the role of hypoxia in the aggressiveness of GBM, in
              part, by transforming MΦ such that a protumoral activity is
              expressed.
            authors:
              - authorID: '10811488'
                authorName: M.M. Leblond
                authorSequenceNumber: 1
                authorSlug: m-m-leblond-38R2GJ
                family: Leblond
                given: M.M.
              - authorID: '8445599'
                authorName: Aurélie N. Gérault
                authorSequenceNumber: 2
                authorSlug: aurelie-n-gerault-eP21Vz
                family: Gérault
                given: Aurélie N.
              - authorID: '66161215'
                authorName: Aurélien Corroyer-Dulmont
                authorSequenceNumber: 3
                authorSlug: aurelien-corroyer-dulmont-bmgGNk
                family: Corroyer-Dulmont
                given: Aurélien
              - authorID: '14725421'
                authorName: Eric T. MacKenzie
                authorSequenceNumber: 4
                authorSlug: eric-t-mackenzie-8VjZn9
                family: MacKenzie
                given: Eric T.
              - authorID: '18194196'
                authorName: Edwige Petit
                authorSequenceNumber: 5
                authorSlug: edwige-petit-MlwLkW
                family: Petit
                given: Edwige
              - authorID: '8501403'
                authorName: Myriam Bernaudin
                authorSequenceNumber: 6
                authorSlug: myriam-bernaudin-1gXEKM
                family: Bernaudin
                given: Myriam
              - authorID: '27051663'
                authorName: Samuel Valable
                authorSequenceNumber: 7
                authorSlug: samuel-valable-DjOMGz
                family: Valable
                given: Samuel
            doi: 10.1080/2162402x.2015.1056442
            editorialNotices: []
            id: 88644956
            issns:
              - 2162-402X
            issue: '1'
            journal: OncoImmunology
            journalSlug: zR0j9
            keywords:
              - Original Research
            memberId: 301
            normalizedTypes:
              - article
            page: e1056442
            preprintLinks: []
            publicationLinks: []
            publisher: Informa UK Limited
            retracted: false
            shortJournal: OncoImmunology
            slug: hypoxia-induces-macrophage-polarization-and-0vyDV9
            title: >-
              Hypoxia induces macrophage polarization and re-education toward an
              M2 phenotype in U87 and U251 glioblastoma models
            type: journal-article
            volume: '5'
            year: 2015
          10.1091/mbc.e02-02-0105:
            abstract: >-
              Much of the work conducted on adult stem cells has focused on
              mesenchymal stem cells (MSCs) found within the bone marrow stroma.
              Adipose tissue, like bone marrow, is derived from the embryonic
              mesenchyme and contains a stroma that is easily isolated.
              Preliminary studies have recently identified a putative stem cell
              population within the adipose stromal compartment. This cell
              population, termed processed lipoaspirate (PLA) cells, can be
              isolated from human lipoaspirates and, like MSCs, differentiate
              toward the osteogenic, adipogenic, myogenic, and chondrogenic
              lineages. To confirm whether adipose tissue contains stem cells,
              the PLA population and multiple clonal isolates were analyzed
              using several molecular and biochemical approaches. PLA cells
              expressed multiple CD marker antigens similar to those observed on
              MSCs. Mesodermal lineage induction of PLA cells and clones
              resulted in the expression of multiple lineage-specific genes and
              proteins. Furthermore, biochemical analysis also confirmed
              lineage-specific activity. In addition to mesodermal capacity, PLA
              cells and clones differentiated into putative neurogenic cells,
              exhibiting a neuronal-like morphology and expressing several
              proteins consistent with the neuronal phenotype. Finally, PLA
              cells exhibited unique characteristics distinct from those seen in
              MSCs, including differences in CD marker profile and gene
              expression.
            authors:
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '10904548'
                authorName: Patricia A. Zuk
                authorSequenceNumber: 1
                authorSlug: patricia-a-zuk-WGwQR1
                family: Zuk
                given: Patricia A.
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '214178751'
                authorName: Min Zhu
                authorSequenceNumber: 2
                authorSlug: min-zhu-YZbjbV3
                family: Zhu
                given: Min
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '6176633'
                authorName: Peter Ashjian
                authorSequenceNumber: 3
                authorSlug: peter-ashjian-n6RKm6
                family: Ashjian
                given: Peter
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '32143121'
                authorName: Daniel A. De Ugarte
                authorSequenceNumber: 4
                authorSlug: daniel-a-de-ugarte-88xJY2
                family: Ugarte
                given: Daniel A. De
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '31478953'
                authorName: Jerry I. Huang
                authorSequenceNumber: 5
                authorSlug: jerry-i-huang-vp3kzW
                family: Huang
                given: Jerry I.
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '31856060'
                authorName: Hiroshi Mizuno
                authorSequenceNumber: 6
                authorSlug: hiroshi-mizuno-QQGRLV
                family: Mizuno
                given: Hiroshi
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '8164751'
                authorName: Zeni Alfonso
                authorSequenceNumber: 7
                authorSlug: zeni-alfonso-YgK14L
                family: Alfonso
                given: Zeni
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '31602369'
                authorName: John K. Fraser
                authorSequenceNumber: 8
                authorSlug: john-k-fraser-5e9ygp
                family: Fraser
                given: John K.
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '205945766'
                authorName: Prosper Benhaim
                authorSequenceNumber: 9
                authorSlug: prosper-benhaim-xXw4r4g
                family: Benhaim
                given: Prosper
              - affiliation: University of California, Los Angeles
                affiliationID: '16569'
                affiliationSlug: university-of-california-los-angeles-5eED
                authorID: '8997341'
                authorName: Marc H. Hedrick
                authorSequenceNumber: 10
                authorSlug: marc-h-hedrick-XekLkx
                family: Hedrick
                given: Marc H.
            doi: 10.1091/mbc.e02-02-0105
            editorialNotices: []
            id: 90224106
            issns:
              - 1059-1524
              - 1939-4586
            issue: '12'
            journal: Molecular Biology of the Cell
            journalSlug: 3naW2
            memberId: 1076
            normalizedTypes:
              - article
            page: 4279-4295
            preprintLinks: []
            publicationLinks: []
            publisher: American Society for Cell Biology (ASCB)
            retracted: false
            shortJournal: MBoC
            slug: human-adipose-tissue-is-a-zgLwX8
            title: Human Adipose Tissue Is a Source of Multipotent Stem Cells
            type: journal-article
            volume: '13'
            year: 2002
          10.1093/bioinformatics/btp101:
            abstract: >-
              Summary: We have developed ClueGO, an easy to use Cytoscape
              plug-in that strongly improves biological interpretation of large
              lists of genes. ClueGO integrates Gene Ontology (GO) terms as well
              as KEGG/BioCarta pathways and creates a functionally organized
              GO/pathway term network. It can analyze one or compare two lists
              of genes and comprehensively visualizes functionally grouped
              terms. A one-click update option allows ClueGO to automatically
              download the most recent GO/KEGG release at any time. ClueGO
              provides an intuitive representation of the analysis results and
              can be optionally used in conjunction with the GOlorize
              plug-in.Availability:
              http://www.ici.upmc.fr/cluego/cluegoDownload.shtmlContact:
              jerome.galon@crc.jussieu.frSupplementary information:
              Supplementary data are available at Bioinformatics online.
            authors:
              - affiliation: Inserm
                affiliationID: '6896'
                affiliationSlug: inserm-MaEp
                authorID: '190599640'
                authorName: Gabriela-Luana Bindea
                authorSequenceNumber: 1
                authorSlug: gabriela-luana-bindea-Le9NdZ5
                family: Bindea
                given: Gabriela-Luana
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '5929588'
                authorName: Bernhard Mlecnik
                authorSequenceNumber: 2
                authorSlug: bernhard-mlecnik-3nEwDg
                family: Mlecnik
                given: Bernhard
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '175923479'
                authorName: Bernhard Mlecnik
                authorSequenceNumber: 2
                authorSlug: bernhard-mlecnik-K6WDab5
                family: Mlecnik
                given: Bernhard
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '6807462'
                authorName: Hubert Hackl
                authorSequenceNumber: 3
                authorSlug: hubert-hackl-dvnP03
                family: Hackl
                given: Hubert
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '5188329'
                authorName: Pornpimol Charoentong
                authorSequenceNumber: 4
                authorSlug: pornpimol-charoentong-r6X5bA
                family: Charoentong
                given: Pornpimol
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '67195293'
                authorName: Marie Tosolini
                authorSequenceNumber: 5
                authorSlug: marie-tosolini-Aaz0jE
                family: Tosolini
                given: Marie
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '7006357'
                authorName: Amos Kirilovsky
                authorSequenceNumber: 6
                authorSlug: amos-kirilovsky-G3MnGK
                family: Kirilovsky
                given: Amos
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '7234686'
                authorName: Wolf H. Fridman
                authorSequenceNumber: 7
                authorSlug: wolf-h-fridman-4LnnnV
                family: Fridman
                given: Wolf H.
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '191883796'
                authorName: Franck Pagès
                authorSequenceNumber: 8
                authorSlug: franck-pages-MVy0Lbm
                family: Pagès
                given: Franck
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '51866335'
                authorName: Zlatko Trajanoski
                authorSequenceNumber: 9
                authorSlug: zlatko-trajanoski-Kvx09e
                family: Trajanoski
                given: Zlatko
              - affiliation: Sorbonne University
                affiliationID: '21314'
                affiliationSlug: sorbonne-university-g0bQ
                authorID: '23365565'
                authorName: Jérôme Galon
                authorSequenceNumber: 10
                authorSlug: jerome-galon-8NWDRx
                family: Galon
                given: Jérôme
            doi: 10.1093/bioinformatics/btp101
            editorialNotices: []
            id: 90562888
            issns:
              - 1460-2059
              - 1367-4803
            issue: '8'
            journal: Bioinformatics
            journalSlug: PQ0m2
            keywords:
              - Applications Note
            memberId: 286
            normalizedTypes:
              - article
            page: 1091-1093
            preprintLinks: []
            publicationLinks: []
            publisher: Oxford University Press (OUP)
            retracted: false
            slug: cluego-a-cytoscape-plug-in-to-3bzmjd
            title: >-
              ClueGO: a Cytoscape plug-in to decipher functionally grouped gene
              ontology and pathway annotation networks
            type: journal-article
            volume: '25'
            year: 2009
          10.1093/bioinformatics/btp120:
            abstract: >-
              Motivation: A new protocol for sequencing the messenger RNA in a
              cell, known as RNA-Seq, generates millions of short sequence
              fragments in a single run. These fragments, or ‘reads’, can be
              used to measure levels of gene expression and to identify novel
              splice variants of genes. However, current software for aligning
              RNA-Seq data to a genome relies on known splice junctions and
              cannot identify novel ones. TopHat is an efficient read-mapping
              algorithm designed to align reads from an RNA-Seq experiment to a
              reference genome without relying on known splice sites.Results: We
              mapped the RNA-Seq reads from a recent mammalian RNA-Seq
              experiment and recovered more than 72% of the splice junctions
              reported by the annotation-based software from that study, along
              with nearly 20 000 previously unreported junctions. The TopHat
              pipeline is much faster than previous systems, mapping nearly 2.2
              million reads per CPU hour, which is sufficient to process an
              entire RNA-Seq experiment in less than a day on a standard desktop
              computer. We describe several challenges unique to ab initio
              splice site discovery from RNA-Seq reads that will require further
              algorithm development.Availability: TopHat is free, open-source
              software available from http://tophat.cbcb.umd.eduContact:
              cole@cs.umd.eduSupplementary information: Supplementary data are
              available at Bioinformatics online.
            authors:
              - affiliation: University of Maryland, College Park
                affiliationID: '2613'
                affiliationSlug: university-of-maryland-college-park-G3YK
                authorID: '8885272'
                authorName: Cole Trapnell
                authorSequenceNumber: 1
                authorSlug: cole-trapnell-wb9XKL
                family: Trapnell
                given: Cole
              - affiliation: University of Maryland, College Park
                affiliationID: '2613'
                affiliationSlug: university-of-maryland-college-park-G3YK
                authorID: '8878157'
                authorName: Lior Pachter
                authorSequenceNumber: 2
                authorSlug: lior-pachter-G5yZdA
                family: Pachter
                given: Lior
              - affiliation: University of Maryland, College Park
                affiliationID: '2613'
                affiliationSlug: university-of-maryland-college-park-G3YK
                authorID: '483606902'
                authorName: Steven L. Salzberg
                authorSequenceNumber: 3
                authorSlug: steven-l-salzberg-9bPOnP9
                family: Salzberg
                given: Steven L.
            doi: 10.1093/bioinformatics/btp120
            editorialNotices: []
            id: 90562907
            issns:
              - 1460-2059
              - 1367-4803
            issue: '9'
            journal: Bioinformatics
            journalSlug: PQ0m2
            keywords:
              - Original Papers
            memberId: 286
            normalizedTypes:
              - article
            page: 1105-1111
            preprintLinks: []
            publicationLinks: []
            publisher: Oxford University Press (OUP)
            retracted: false
            slug: tophat-discovering-splice-junctions-with-Y5Kj23
            title: 'TopHat: discovering splice junctions with RNA-Seq'
            type: journal-article
            volume: '25'
            year: 2009
          10.1126/science.1201475:
            abstract: >-
              Eosinophils are associated with helminth immunity and allergy,
              often in conjunction with alternatively activated macrophages
              (AAMs). Adipose tissue AAMs are necessary to maintain glucose
              homeostasis and are induced by the cytokine interleukin-4 (IL-4).
              Here, we show that eosinophils are the major IL-4-expressing cells
              in white adipose tissues of mice, and, in their absence, AAMs are
              greatly attenuated. Eosinophils migrate into adipose by an
              integrin-dependent process and reconstitute AAMs through an
              IL-4/IL-13-dependent process. Mice on high-fat diet develop
              increased body fat, impaired glucose tolerance and insulin
              resistance in the absence of eosinophils, and helminth-induced
              adipose eosinophilia enhances glucose tolerance. Our results
              suggest that eosinophils play an unexpected role in metabolic
              homeostasis through maintenance of adipose AAMs.
            authors:
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '14547459'
                authorName: Davina Wu
                authorSequenceNumber: 1
                authorSlug: davina-wu-b8KyY8
                family: Wu
                given: Davina
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '6805954'
                authorName: Ari B. Molofsky
                authorSequenceNumber: 2
                authorSlug: ari-b-molofsky-68mWl6
                family: Molofsky
                given: Ari B.
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '11178770'
                authorName: Hong-Erh Liang
                authorSequenceNumber: 3
                authorSlug: hong-erh-liang-R5K3MN
                family: Liang
                given: Hong-Erh
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '10317769'
                authorName: Roberto R. Ricardo-Gonzalez
                authorSequenceNumber: 4
                authorSlug: roberto-r-ricardo-gonzalez-5YAR9A
                family: Ricardo-Gonzalez
                given: Roberto R.
              - affiliation: Stanford University
                affiliationID: '23761'
                affiliationSlug: stanford-university-EVVW
                authorID: '9020513'
                authorName: Hani A. Jouihan
                authorSequenceNumber: 5
                authorSlug: hani-a-jouihan-G5K8YE
                family: Jouihan
                given: Hani A.
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '8379223'
                authorName: Jennifer K. Bando
                authorSequenceNumber: 6
                authorSlug: jennifer-k-bando-JWZ2vk
                family: Bando
                given: Jennifer K.
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '32477922'
                authorName: Ajay Chawla
                authorSequenceNumber: 7
                authorSlug: ajay-chawla-xpjLMg
                family: Chawla
                given: Ajay
              - affiliation: University of California, San Francisco
                affiliationID: '12272'
                affiliationSlug: university-of-california-san-francisco-w1Ry
                authorID: '6048470'
                authorName: Richard M. Locksley
                authorSequenceNumber: 8
                authorSlug: richard-m-locksley-RVle83
                family: Locksley
                given: Richard M.
            doi: 10.1126/science.1201475
            editorialNotices: []
            id: 103081497
            issns:
              - 0036-8075
              - 1095-9203
            issue: '6026'
            journal: Science
            journalSlug: y8MnG
            keywords:
              - Article
            memberId: 221
            normalizedTypes:
              - article
            page: 243-247
            preprintLinks: []
            publicationLinks: []
            publisher: American Association for the Advancement of Science (AAAS)
            retracted: false
            shortJournal: Science
            slug: eosinophils-sustain-adipose-alternatively-activated-vMKdvV
            title: >-
              Eosinophils Sustain Adipose Alternatively Activated Macrophages
              Associated with Glucose Homeostasis
            type: journal-article
            volume: '332'
            year: 2011
          10.1146/annurev-immunol-031210-101322:
            abstract: >-
              The modern rise in obesity and its strong association with insulin
              resistance and type 2 diabetes have elicited interest in the
              underlying mechanisms of these pathologies. The discovery that
              obesity itself results in an inflammatory state in metabolic
              tissues ushered in a research field that examines the inflammatory
              mechanisms in obesity. Here, we summarize the unique features of
              this metabolic inflammatory state, termed metaflammation and
              defined as low-grade, chronic inflammation orchestrated by
              metabolic cells in response to excess nutrients and energy. We
              explore the effects of such inflammation in metabolic tissues
              including adipose, liver, muscle, pancreas, and brain and its
              contribution to insulin resistance and metabolic dysfunction.
              Another area in which many unknowns still exist is the origin or
              mechanism of initiation of inflammatory signaling in obesity. We
              discuss signals or triggers to the inflammatory response,
              including the possibility of endoplasmic reticulum stress as an
              important contributor to metaflammation. Finally, we examine
              anti-inflammatory therapies for their potential in the treatment
              of obesity-related insulin resistance and glucose intolerance.
            authors:
              - affiliation: Harvard University
                affiliationID: '14927'
                affiliationSlug: harvard-university-NmzP
                authorID: '16265116'
                authorName: Margaret F. Gregor
                authorSequenceNumber: 1
                authorSlug: margaret-f-gregor-Q6O5K9
                family: Gregor
                given: Margaret F.
              - affiliation: Harvard University
                affiliationID: '14927'
                affiliationSlug: harvard-university-NmzP
                authorID: '24580538'
                authorName: Gökhan S. Hotamisligil
                authorSequenceNumber: 2
                authorSlug: gokhan-s-hotamisligil-Vj555z
                family: Hotamisligil
                given: Gökhan S.
            doi: 10.1146/annurev-immunol-031210-101322
            editorialNotices: []
            id: 105718425
            issns:
              - 0732-0582
              - 1545-3278
            issue: '1'
            journal: Annual Review of Immunology
            journalSlug: ejgZO
            keywords:
              - adiposity
              - metaflammation
              - insulin resistance
              - inflammatory signaling
              - organelle stress
              - nutrient signals vi Contents
            memberId: 22
            normalizedTypes:
              - article
            page: 415-445
            preprintLinks: []
            publicationLinks: []
            publisher: Annual Reviews
            retracted: false
            shortJournal: Annu. Rev. Immunol.
            slug: inflammatory-mechanisms-in-obesity-55ZYk2
            title: Inflammatory Mechanisms in Obesity
            type: journal-article
            volume: '29'
            year: 2011
          10.1146/annurev.med.53.082901.104057:
            abstract: >-
              I review evidence that leptin is a liporegulatory hormone that
              controls lipid homeostasis in nonadipose tissues during periods of
              overnutrition. When adipocytes store excess calories as
              triacylglycerol (TG), leptin secretion rises so as to prevent
              accumulation of lipids in nonadipose tissues, which are not
              adapted for TG storage. Whenever leptin action is lacking, whether
              through leptin deficiency or leptin resistance, overnutrition
              causes disease of nonadipose tissues with generalized steatosis,
              lipotoxicity, and lipoapoptosis. Examples of such disorders of
              liporegulation include generalized lipodystrophies, mutations of
              leptin and leptin receptor genes, and diet-induced obesity.
              Lipotoxicity of pancreatic beta-cells, myocardium, and skeletal
              muscle leads, respectively, to type 2 diabetes, cardiomyopathy,
              and insulin resistance. In humans this constellation of
              abnormalities is referred to as the metabolic syndrome, a major
              health problem in the United States. When lipids overaccumulate in
              nonadipose tissues during overnutrition, fatty acids enter
              deleterious pathways such as ceramide production, which, through
              increased nitric oxide formation, causes apoptosis of lipid-laden
              cells, such as beta-cells and cardiomyocytes. Lipoapoptosis can be
              prevented by caloric restriction, by thiazolidinedione treatment,
              and by administration of nitric oxide blockers. There is now
              substantial evidence that complications of human obesity may
              reflect lipotoxicity similar to that described in rodents.
            authors:
              - affiliation: The University of Texas Southwestern Medical Center
                affiliationID: '3092'
                affiliationSlug: the-university-of-texas-southwestern-W8Yd
                authorID: '982324166'
                authorName: Roger H. Unger
                authorSequenceNumber: 1
                authorSlug: roger-h-unger-xPJRMOw
                family: Unger
                given: Roger H.
            doi: 10.1146/annurev.med.53.082901.104057
            editorialNotices: []
            id: 105740370
            issns:
              - 0066-4219
              - 1545-326X
            issue: '1'
            journal: Annual Review of Medicine
            journalSlug: vJGbV
            memberId: 22
            normalizedTypes:
              - article
            page: 319-336
            preprintLinks: []
            publicationLinks: []
            publisher: Annual Reviews
            retracted: false
            shortJournal: Annu. Rev. Med.
            slug: lipotoxic-diseases-RX8EN3
            title: Lipotoxic Diseases
            type: journal-article
            volume: '53'
            year: 2002
          10.1172/jci15001:
            abstract: >-
              Lipodystrophy is a rare disorder that is characterized by
              selective loss of subcutaneous and visceral fat and is associated
              with hypertriglyceridemia, hepatomegaly, and disordered glucose
              metabolism. It has recently been shown that chronic leptin
              treatment ameliorates these abnormalities. Here we show that
              chronic leptin treatment improves insulin-stimulated hepatic and
              peripheral glucose metabolism in severely insulin-resistant
              lipodystrophic patients. This improvement in insulin action was
              associated with a marked reduction in hepatic and muscle
              triglyceride content. These data suggest that leptin may represent
              an important new therapy to reverse the severe hepatic and muscle
              insulin resistance and associated hepatic steatosis in patients
              with lipodystrophy
            authors:
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '19514059'
                authorName: Kitt Falk Petersen
                authorSequenceNumber: 1
                authorSlug: kitt-falk-petersen-bM98wW
                family: Petersen
                given: Kitt Falk
              - authorID: '101157744'
                authorName: Elif A. Oral
                authorSequenceNumber: 2
                authorSlug: elif-a-oral-3wQkPJ
                family: Oral
                given: Elif A.
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '148536730'
                authorName: Sylvie Dufour
                authorSequenceNumber: 3
                authorSlug: sylvie-dufour-pJ9mK3
                family: Dufour
                given: Sylvie
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '1529050'
                authorName: Douglas E. Befroy
                authorSequenceNumber: 4
                authorSlug: douglas-e-befroy-zW4yx
                family: Befroy
                given: Douglas E.
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '24586504'
                authorName: Charlotte E. Ariyan
                authorSequenceNumber: 5
                authorSlug: charlotte-e-ariyan-Wa5r1N
                family: Ariyan
                given: Charlotte E.
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '18585489'
                authorName: Chunli Yu
                authorSequenceNumber: 6
                authorSlug: chunli-yu-Pv5xk0
                family: Yu
                given: Chunli
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '7080077'
                authorName: Gary W. Cline
                authorSequenceNumber: 7
                authorSlug: gary-w-cline-n68Dgk
                family: Cline
                given: Gary W.
              - affiliation: Amgen
                affiliationID: '18955'
                affiliationSlug: amgen-eAJO
                authorID: '7128516'
                authorName: Alex M. DePaoli
                authorSequenceNumber: 8
                authorSlug: alex-m-depaoli-QeZ4m9
                family: DePaoli
                given: Alex M.
              - affiliation: National Institutes of Health
                affiliationID: '26753'
                affiliationSlug: national-institutes-of-health-vVaJ
                authorID: '19599942'
                authorName: Simeon I. Taylor
                authorSequenceNumber: 9
                authorSlug: simeon-i-taylor-4x3Zj3
                family: Taylor
                given: Simeon I.
              - affiliation: National Institutes of Health
                affiliationID: '26753'
                affiliationSlug: national-institutes-of-health-vVaJ
                authorID: '7701276'
                authorName: Phillip Gorden
                authorSequenceNumber: 10
                authorSlug: phillip-gorden-2WWaKL
                family: Gorden
                given: Phillip
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '5886223'
                authorName: Gerald I. Shulman
                authorSequenceNumber: 11
                authorSlug: gerald-i-shulman-J1LvKY
                family: Shulman
                given: Gerald I.
            doi: 10.1172/jci15001
            editorialNotices: []
            id: 108000450
            issns:
              - 0021-9738
            issue: '10'
            journal: Journal of Clinical Investigation
            journalSlug: G3Dlb
            keywords: []
            memberId: 232
            normalizedTypes:
              - article
            page: 1345-1350
            preprintLinks: []
            publicationLinks: []
            publisher: American Society for Clinical Investigation
            shortJournal: J. Clin. Invest.
            slug: leptin-reverses-insulin-resistance-and-zmylXY
            title: >-
              Leptin reverses insulin resistance and hepatic steatosis in
              patients with severe lipodystrophy
            type: journal-article
            volume: '109'
            year: 2002
          10.1172/jci19246:
            authors:
              - affiliation: Columbia University
                affiliationID: '8275'
                affiliationSlug: columbia-university-Z3Ly
                authorID: '150108093'
                authorName: Stuart P. Weisberg
                authorSequenceNumber: 1
                authorSlug: stuart-p-weisberg-AzNDDL
                family: Weisberg
                given: Stuart P.
              - authorID: '106203356'
                authorName: Daniel McCann
                authorSequenceNumber: 2
                authorSlug: daniel-mccann-0yx39y
                family: McCann
                given: Daniel
              - authorID: '28017296'
                authorName: Manisha Desai
                authorSequenceNumber: 3
                authorSlug: manisha-desai-MyWNpp
                family: Desai
                given: Manisha
              - authorID: '12962727'
                authorName: Michael Rosenbaum
                authorSequenceNumber: 4
                authorSlug: michael-rosenbaum-NYAma9
                family: Rosenbaum
                given: Michael
              - authorID: '1464126'
                authorName: Rudolph L. Leibel
                authorSequenceNumber: 5
                authorSlug: rudolph-l-leibel-Rm0A9
                family: Leibel
                given: Rudolph L.
              - authorID: '15926846'
                authorName: Anthony W. Ferrante
                authorSequenceNumber: 6
                authorSlug: anthony-w-ferrante-9gA91G
                family: Ferrante
                given: Anthony W.
            doi: 10.1172/jci19246
            editorialNotices: []
            id: 108001285
            issns:
              - 0021-9738
            issue: '12'
            journal: Journal of Clinical Investigation
            journalSlug: G3Dlb
            memberId: 232
            normalizedTypes:
              - article
            page: 1796-1808
            preprintLinks: []
            publicationLinks: []
            publisher: American Society for Clinical Investigation
            shortJournal: J. Clin. Invest.
            slug: obesity-is-associated-with-macrophage-Xm896A
            title: >-
              Obesity is associated with macrophage accumulation in adipose
              tissue
            type: journal-article
            volume: '112'
            year: 2003
          10.1172/jci31021:
            abstract: >-
              Excess caloric intake can lead to insulin resistance. The
              underlying reasons are complex but likely related to ectopic lipid
              deposition in nonadipose tissue. We hypothesized that the
              inability to appropriately expand subcutaneous adipose tissue may
              be an underlying reason for insulin resistance and beta cell
              failure. Mice lacking leptin while overexpressing adiponectin
              showed normalized glucose and insulin levels and dramatically
              improved glucose as well as positively affected serum triglyceride
              levels. Therefore, modestly increasing the levels of circulating
              full-length adiponectin completely rescued the diabetic phenotype
              in ob/ob mice. They displayed increased expression of PPARgamma
              target genes and a reduction in macrophage infiltration in adipose
              tissue and systemic inflammation. As a result, the transgenic mice
              were morbidly obese, with significantly higher levels of adipose
              tissue than their ob/ob littermates, leading to an interesting
              dichotomy of increased fat mass associated with improvement in
              insulin sensitivity. Based on these data, we propose that
              adiponectin acts as a peripheral "starvation" signal promoting the
              storage of triglycerides preferentially in adipose tissue. As a
              consequence, reduced triglyceride levels in the liver and muscle
              convey improved systemic insulin sensitivity. These mice therefore
              represent what we believe is a novel model of morbid obesity
              associated with an improved metabolic profile.
            authors:
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '56710517'
                authorName: Ja Young Kim
                authorSequenceNumber: 1
                authorSlug: ja-young-kim-EAkxZK
                family: Kim
                given: Ja Young
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '74763281'
                authorName: Esther Van De Wall
                authorSequenceNumber: 2
                authorSlug: esther-van-de-wall-je4JVl
                family: Wall
                given: Esther Van De
              - affiliation: Université Laval
                affiliationID: '7104'
                affiliationSlug: universite-laval-WxWg
                authorID: '73675717'
                authorName: Mathieu Laplante
                authorSequenceNumber: 3
                authorSlug: mathieu-laplante-E0XDXk
                family: Laplante
                given: Mathieu
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '66287203'
                authorName: Anthony Azzara
                authorSequenceNumber: 4
                authorSlug: anthony-azzara-1daWXj
                family: Azzara
                given: Anthony
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '16587171'
                authorName: Maria E. Trujillo
                authorSequenceNumber: 5
                authorSlug: maria-e-trujillo-Nnvzpm
                family: Trujillo
                given: Maria E.
              - affiliation: University of Cincinnati
                affiliationID: '19659'
                affiliationSlug: university-of-cincinnati-bQ3Z
                authorID: '19153644'
                authorName: Susanna M. Hofmann
                authorSequenceNumber: 6
                authorSlug: susanna-m-hofmann-3NK93K
                family: Hofmann
                given: Susanna M.
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '39422588'
                authorName: Todd Schraw
                authorSequenceNumber: 7
                authorSlug: todd-schraw-3vkYP2
                family: Schraw
                given: Todd
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '12833947'
                authorName: Jorge L. Durand
                authorSequenceNumber: 8
                authorSlug: jorge-l-durand-1nNL1y
                family: Durand
                given: Jorge L.
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '27704089'
                authorName: Hua Li
                authorSequenceNumber: 9
                authorSlug: hua-li-PxKg5K
                family: Li
                given: Hua
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '17474293'
                authorName: Guangyu Li
                authorSequenceNumber: 10
                authorSlug: guangyu-li-AxeOP3
                family: Li
                given: Guangyu
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '379055'
                authorName: Linda A. Jelicks
                authorSequenceNumber: 11
                authorSlug: linda-a-jelicks-eDzJ0
                family: Jelicks
                given: Linda A.
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '17417115'
                authorName: Mark F. Mehler
                authorSequenceNumber: 12
                authorSlug: mark-f-mehler-bjgA1p
                family: Mehler
                given: Mark F.
              - affiliation: University of Cincinnati
                affiliationID: '19659'
                affiliationSlug: university-of-cincinnati-bQ3Z
                authorID: '424319808'
                authorName: David Y. Hui
                authorSequenceNumber: 13
                authorSlug: david-y-hui-M2LQQWY
                family: Hui
                given: David Y.
              - affiliation: Université Laval
                affiliationID: '7104'
                affiliationSlug: universite-laval-WxWg
                authorID: '918119'
                authorName: Yves Deshaies
                authorSequenceNumber: 14
                authorSlug: yves-deshaies-DJkJW
                family: Deshaies
                given: Yves
              - affiliation: Yale University
                affiliationID: '8068'
                affiliationSlug: yale-university-kyQE
                authorID: '5886223'
                authorName: Gerald I. Shulman
                authorSequenceNumber: 15
                authorSlug: gerald-i-shulman-J1LvKY
                family: Shulman
                given: Gerald I.
              - affiliation: Yeshiva University
                affiliationID: '25469'
                affiliationSlug: yeshiva-university-5QJW
                authorID: '21123336'
                authorName: Gary J. Schwartz
                authorSequenceNumber: 16
                authorSlug: gary-j-schwartz-l62eza
                family: Schwartz
                given: Gary J.
              - authorID: '52493527'
                authorName: Philipp E. Scherer
                authorSequenceNumber: 17
                authorSlug: philipp-e-scherer-NOE2vz
                family: Scherer
                given: Philipp E.
            doi: 10.1172/jci31021
            editorialNotices: []
            id: 108005431
            issns:
              - 0021-9738
            issue: '9'
            journal: Journal of Clinical Investigation
            journalSlug: G3Dlb
            keywords: []
            memberId: 232
            normalizedTypes:
              - article
            page: 2621-2637
            preprintLinks: []
            publicationLinks: []
            publisher: American Society for Clinical Investigation
            retracted: false
            shortJournal: J. Clin. Invest.
            slug: obesity-associated-improvements-in-metabolic-profile-ZzJPZP
            title: >-
              Obesity-associated improvements in metabolic profile through
              expansion of adipose tissue
            type: journal-article
            volume: '117'
            year: 2007
          10.1172/jci7901:
            authors:
              - affiliation: National Institutes of Health
                affiliationID: '26753'
                affiliationSlug: national-institutes-of-health-vVaJ
                authorID: '17567133'
                authorName: Oksana Gavrilova
                authorSequenceNumber: 1
                authorSlug: oksana-gavrilova-nz5X46
                family: Gavrilova
                given: Oksana
              - authorID: '7000847'
                authorName: Bernice Marcus-Samuels
                authorSequenceNumber: 2
                authorSlug: bernice-marcus-samuels-1ZkzDW
                family: Marcus-Samuels
                given: Bernice
              - authorID: '170545366'
                authorName: David Graham
                authorSequenceNumber: 3
                authorSlug: david-graham-xXXKR6Q
                family: Graham
                given: David
              - authorID: '15023009'
                authorName: Jason K. Kim
                authorSequenceNumber: 4
                authorSlug: jason-k-kim-vdg5aJ
                family: Kim
                given: Jason K.
              - authorID: '5886223'
                authorName: Gerald I. Shulman
                authorSequenceNumber: 5
                authorSlug: gerald-i-shulman-J1LvKY
                family: Shulman
                given: Gerald I.
              - authorID: '98232358'
                authorName: Arthur L. Castle
                authorSequenceNumber: 6
                authorSlug: arthur-l-castle-gJYREJ
                family: Castle
                given: Arthur L.
              - authorID: '8852758'
                authorName: Charles Vinson
                authorSequenceNumber: 7
                authorSlug: charles-vinson-g1vW31
                family: Vinson
                given: Charles
              - authorID: '78461932'
                authorName: Michael Eckhaus
                authorSequenceNumber: 8
                authorSlug: michael-eckhaus-2EKlP1
                family: Eckhaus
                given: Michael
              - authorID: '6596888'
                authorName: Marc L. Reitman
                authorSequenceNumber: 9
                authorSlug: marc-l-reitman-3n1GLy
                family: Reitman
                given: Marc L.
            doi: 10.1172/jci7901
            editorialNotices: []
            id: 108012655
            issns:
              - 0021-9738
            issue: '3'
            journal: Journal of Clinical Investigation
            journalSlug: G3Dlb
            memberId: 232
            normalizedTypes:
              - article
            page: 271-278
            preprintLinks: []
            publicationLinks: []
            publisher: American Society for Clinical Investigation
            retracted: false
            shortJournal: J. Clin. Invest.
            slug: surgical-implantation-of-adipose-tissue-eEOpd6
            title: >-
              Surgical implantation of adipose tissue reverses diabetes in
              lipoatrophic mice
            type: journal-article
            volume: '105'
            year: 2000
          10.1172/jci85664:
            abstract: >-
              Increases in eosinophil numbers are associated with infection and
              allergic diseases, including asthma, but there is also evidence
              that eosinophils contribute to homeostatic immune processes. In
              mice, the normal lung contains resident eosinophils (rEos), but
              their function has not been characterized. Here, we have reported
              that steady-state pulmonary rEos are IL-5-independent parenchymal
              Siglec-FintCD62L+CD101lo cells with a ring-shaped nucleus. During
              house dust mite-induced airway allergy, rEos features remained
              unchanged, and rEos were accompanied by recruited inflammatory
              eosinophils (iEos), which were defined as IL-5-dependent
              peribronchial Siglec-FhiCD62L-CD101hi cells with a segmented
              nucleus. Gene expression analyses revealed a more regulatory
              profile for rEos than for iEos, and correspondingly, mice lacking
              lung rEos showed an increase in Th2 cell responses to inhaled
              allergens. Such elevation of Th2 responses was linked to the
              ability of rEos, but not iEos, to inhibit the maturation, and
              therefore the pro-Th2 function, of allergen-loaded DCs. Finally,
              we determined that the parenchymal rEos found in nonasthmatic
              human lungs (Siglec-8+CD62L+IL-3Rlo cells) were phenotypically
              distinct from the iEos isolated from the sputa of eosinophilic
              asthmatic patients (Siglec-8+CD62LloIL-3Rhi cells), suggesting
              that our findings in mice are relevant to humans. In conclusion,
              our data define lung rEos as a distinct eosinophil subset with key
              homeostatic functions
            authors:
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '177678837'
                authorName: Claire Mesnil
                authorSequenceNumber: 1
                authorSlug: claire-mesnil-jMXVabV
                family: Mesnil
                given: Claire
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '26329268'
                authorName: Stéfanie Raulier
                authorSequenceNumber: 2
                authorSlug: stefanie-raulier-kQevag
                family: Raulier
                given: Stéfanie
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '10250781'
                authorName: Geneviève Paulissen
                authorSequenceNumber: 3
                authorSlug: genevieve-paulissen-j6NRad
                family: Paulissen
                given: Geneviève
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '81340856'
                authorName: Xue Xiao
                authorSequenceNumber: 4
                authorSlug: xue-xiao-02VJjZ
                family: Xiao
                given: Xue
              - authorID: '214095906'
                authorName: Mark A. Birrell
                authorSequenceNumber: 5
                authorSlug: mark-a-birrell-zRd19eb
                family: Birrell
                given: Mark A.
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '71959784'
                authorName: Dimitri Pirottin
                authorSequenceNumber: 6
                authorSlug: dimitri-pirottin-L3lw6X
                family: Pirottin
                given: Dimitri
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '27354415'
                authorName: Thibaut Janss
                authorSequenceNumber: 7
                authorSlug: thibaut-janss-bNnMW6
                family: Janss
                given: Thibaut
              - authorID: '11397405'
                authorName: Philipp Starkl
                authorSequenceNumber: 8
                authorSlug: philipp-starkl-AG3nGv
                family: Starkl
                given: Philipp
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '3244950'
                authorName: Eve Ramery
                authorSequenceNumber: 9
                authorSlug: eve-ramery-z8zz8
                family: Ramery
                given: Eve
              - authorID: '8764964'
                authorName: Monique Henket
                authorSequenceNumber: 10
                authorSlug: monique-henket-yZP256
                family: Henket
                given: Monique
              - authorID: '33968931'
                authorName: Florence Schleich
                authorSequenceNumber: 11
                authorSlug: florence-schleich-ZDxvOn
                family: Schleich
                given: Florence
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '11327135'
                authorName: Marc Radermecker
                authorSequenceNumber: 12
                authorSlug: marc-radermecker-KljyZ5
                family: Radermecker
                given: Marc
              - authorID: '24111146'
                authorName: Kris Thielemans
                authorSequenceNumber: 13
                authorSlug: kris-thielemans-9N3bgr
                family: Thielemans
                given: Kris
              - authorID: '25816346'
                authorName: Laurent Gillet
                authorSequenceNumber: 14
                authorSlug: laurent-gillet-9NYbYN
                family: Gillet
                given: Laurent
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '16452683'
                authorName: Marc Thiry
                authorSequenceNumber: 15
                authorSlug: marc-thiry-a8kn2r
                family: Thiry
                given: Marc
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '214066975'
                authorName: Maria G. Belvisi
                authorSequenceNumber: 16
                authorSlug: maria-g-belvisi-ZGb3M0p
                family: Belvisi
                given: Maria G.
              - authorID: '16310778'
                authorName: Renaud Louis
                authorSequenceNumber: 17
                authorSlug: renaud-louis-Ov2zr8
                family: Louis
                given: Renaud
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '30627395'
                authorName: Christophe Desmet
                authorSequenceNumber: 18
                authorSlug: christophe-desmet-YNKLnK
                family: Desmet
                given: Christophe
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '5569771'
                authorName: Thomas Marichal
                authorSequenceNumber: 19
                authorSlug: thomas-marichal-Nl6Rxz
                family: Marichal
                given: Thomas
              - affiliation: University of Liège
                affiliationID: '7680'
                affiliationSlug: university-of-liege-lQe3
                authorID: '8267496'
                authorName: Fabrice Bureau
                authorSequenceNumber: 20
                authorSlug: fabrice-bureau-M2Q2KX
                family: Bureau
                given: Fabrice
            doi: 10.1172/jci85664
            editorialNotices: []
            id: 108013849
            issns:
              - 0021-9738
              - 1558-8238
            issue: '9'
            journal: Journal of Clinical Investigation
            journalSlug: G3Dlb
            memberId: 232
            normalizedTypes:
              - article
            page: 3279-3295
            preprintLinks: []
            publicationLinks: []
            publisher: American Society for Clinical Investigation
            retracted: false
            slug: lung-resident-eosinophils-represent-a-distinct-AX0WVZ
            title: >-
              Lung-resident eosinophils represent a distinct regulatory
              eosinophil subset
            type: journal-article
            volume: '126'
            year: 2016
          10.1186/s12944-015-0123-1:
            abstract: >-
              Insulin resistance is a multi-faceted disruption of the
              communication between insulin and the interior of a target cell.
              The underlying cause of insulin resistance appears to be
              inflammation that can either be increased or decreased by the
              fatty acid composition of the diet. However, the molecular basis
              for insulin resistance can be quite different in various organs.
              This review deals with various types of inflammatory inputs
              mediated by fatty acids, which affect the extent of insulin
              resistance in various organs.
            authors:
              - authorID: '12372440'
                authorName: Barry Sears
                authorSequenceNumber: 1
                authorSlug: barry-sears-Lp6ZWm
                family: Sears
                given: Barry
              - authorID: '76675623'
                authorName: Mary Perry
                authorSequenceNumber: 2
                authorSlug: mary-perry-JPPlnY
                family: Perry
                given: Mary
            doi: 10.1186/s12944-015-0123-1
            editorialNotices: []
            id: 110076748
            issns:
              - 1476-511X
            issue: '1'
            journal: Lipids in Health and Disease
            journalSlug: Nlkme
            keywords:
              - Review
            memberId: 297
            normalizedTypes:
              - article
            preprintLinks: []
            publicationLinks: []
            publisher: Springer Science and Business Media LLC
            retracted: false
            shortJournal: Lipids Health Dis
            slug: the-role-of-fatty-acids-WWJ0Od
            title: The role of fatty acids in insulin resistance
            type: journal-article
            volume: '14'
            year: 2015
          10.1194/jlr.m008771:
            abstract: >-
              Storing excess energy for future use during starvation is critical
              for the survival of mammals. Much of this energy is stored in the
              form of triacylglycerol (TAG) within lipid droplets, which are
              present most abundantly in adipocytes and which, in turn,
              accumulate in depots such as subcutaneous and visceral adipose
              tissue in mice and humans. TAG in lipid droplets is mobilized
              during starvation by lipase-catalyzed hydrolysis (lipolysis) to
              release energy in the forms of glycerol and free fatty acids,
              providing fuel to other cell types such as muscle and liver.
              Previous work investigating formation of lipid droplets and
              regulation of lipolysis has elucidated the importance of lipid
              dropletassociated proteins for these processes ( 1, 2 ). Based on
              shared sequence homology, one set of lipid droplet proteins is
              grouped as the perilipin-adipophilin-tail interacting protein 47
              (PAT/TIP47) family of proteins ( 3 ). PAT-related proteins are
              functionally conserved from mammals to lower organisms such as
              Drosophila and Dictyostelium spp ( 4 ). In Drosophila , two PAT
              domain proteins are encoded by the Lsdp1 and Lsd2 genes.
              Drosophila loss-of-function Lsd2 mutants are lean, whereas Lsd2
              overexpression causes obesity ( 5 ). In mammals, PAT proteins can
              be divided into exchangeable TAG-associated PAT proteins (EPATs)
              or constitutively TAG-associated PAT proteins (CPATs). EPATs
              include the TIP47/perilipin-3 (PLIN3), S3-12/PLIN4, and Abstract
              The lipid droplet-associated fat specifi c protein 27 (FSP27)
              suppresses lipolysis and thereby enhances triglyceride
              accumulation in adipocytes. We and others have recently found
              FSP27 to be a remarkably short-lived protein (half-life, 15 min)
              due to its rapid ubiquitination and proteasomal degradation. Thus,
              we tested the hypothesis that lipolytic agents such as tumor
              necrosis factor-␣ (TNF-␣ ) and isoproterenol modulate FSP27 levels
              to regulate FFA release. Consistent with this concept, we showed
              that the lipolytic actions of TNF-␣ , interleukin-1 ␤ (IL-1 ␤ ),
              and IFN-␥ are accompanied by marked decreases in FSP27 expression
              and lipid droplet size in mouse adipocytes. Similar depletion of
              FSP27 using short interfering RNA (siRNA) mimicked the
              lipolysis-enhancing effect of TNF-␣ , while maintaining stable
              FSP27 levels using expression of hemagglutinin epitopetagged FSP27
              blocked TNF-␣ -mediated lipolysis. In contrast, we show the robust
              lipolytic action of isoproterenol is paradoxically associated with
              increases in FSP27 levels and a delayed degradation rate
              corresponding to decreased ubiquitination. This
              catecholamine-mediated increase in FSP27 abundance, probably a
              feedback mechanism for restraining excessive lipolysis by
              catecholamines, is mimicked by forskolin or 8-bromo-cAMP treatment
              and is prevented by the protein kinase A (PKA) inhibitor KT5720 or
              by PKA depletion using siRNA. Taken together, these data identify
              the regulation of FSP27 as an important intermediate in the
              mechanism of lipolysis in adipocytes in response to TNF-␣ and
              isoproterenol. -Ranjit, S
            authors:
              - affiliation: University of Massachusetts Medical School
                affiliationID: '260'
                affiliationSlug: university-of-massachusetts-medical-school-Qkx
                authorID: '14107537'
                authorName: Srijana Ranjit
                authorSequenceNumber: 1
                authorSlug: srijana-ranjit-jX534y
                family: Ranjit
                given: Srijana
              - affiliation: University of Massachusetts Medical School
                affiliationID: '260'
                affiliationSlug: university-of-massachusetts-medical-school-Qkx
                authorID: '9832653'
                authorName: Emilie Boutet
                authorSequenceNumber: 2
                authorSlug: emilie-boutet-vyMG23
                family: Boutet
                given: Emilie
              - affiliation: University of Massachusetts Medical School
                affiliationID: '260'
                affiliationSlug: university-of-massachusetts-medical-school-Qkx
                authorID: '16649396'
                authorName: Pallavi Gandhi
                authorSequenceNumber: 3
                authorSlug: pallavi-gandhi-MlPPNm
                family: Gandhi
                given: Pallavi
              - affiliation: University of Massachusetts Medical School
                affiliationID: '260'
                affiliationSlug: university-of-massachusetts-medical-school-Qkx
                authorID: '102839282'
                authorName: Matthieu Prot
                authorSequenceNumber: 4
                authorSlug: matthieu-prot-Vr6vGE
                family: Prot
                given: Matthieu
              - affiliation: Kobe University
                affiliationID: '18337'
                affiliationSlug: kobe-university-jjG5
                authorID: '9831292'
                authorName: Yoshikazu Tamori
                authorSequenceNumber: 5
                authorSlug: yoshikazu-tamori-WGr3ag
                family: Tamori
                given: Yoshikazu
              - affiliation: University of Massachusetts Medical School
                affiliationID: '260'
                affiliationSlug: university-of-massachusetts-medical-school-Qkx
                authorID: '13735848'
                authorName: Anil Chawla
                authorSequenceNumber: 6
                authorSlug: anil-chawla-WxWA2J
                family: Chawla
                given: Anil
              - affiliation: Tufts University
                affiliationID: '10923'
                affiliationSlug: tufts-university-JlXG
                authorID: '9750173'
                authorName: Andrew S. Greenberg
                authorSequenceNumber: 7
                authorSlug: andrew-s-greenberg-rxMPjw
                family: Greenberg
                given: Andrew S.
              - affiliation: Boston University
                affiliationID: '7891'
                affiliationSlug: boston-university-11nj
                authorID: '73159816'
                authorName: Vishwajeet Puri
                authorSequenceNumber: 8
                authorSlug: vishwajeet-puri-QAp2r6
                family: Puri
                given: Vishwajeet
              - affiliation: University of Massachusetts Medical School
                affiliationID: '260'
                affiliationSlug: university-of-massachusetts-medical-school-Qkx
                authorID: '8333398'
                authorName: Michael P. Czech
                authorSequenceNumber: 9
                authorSlug: michael-p-czech-6M0PQ1
                family: Czech
                given: Michael P.
            doi: 10.1194/jlr.m008771
            editorialNotices: []
            id: 110258347
            issns:
              - 0022-2275
            issue: '2'
            journal: Journal of Lipid Research
            journalSlug: y8j1x
            memberId: 78
            normalizedTypes:
              - article
            page: 221-236
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Journal of Lipid Research
            slug: regulation-of-fat-specific-protein-1LNjy6
            title: >-
              Regulation of fat specific protein 27 by isoproterenol and TNF-α
              to control lipolysis in murine adipocytes
            type: journal-article
            volume: '52'
            year: 2011
          10.1194/jlr.m800132-jlr200:
            abstract: >-
              Chronic inflammation of adipose tissue in obesity is by now an
              established phenomenon, but the initiating event(s) of the
              inflammatory cascade are still unknown. We hypothesized that
              neutrophil infiltration into adipose tissue may precede macrophage
              infiltration as in classical immune responses. Here we demonstrate
              that early (3 and 7 days) after initiating high-fat feeding of
              C57BL/6J mice, neutrophils transiently infiltrate the parenchyma
              of intra-abdominal adipose tissue. Mean periepdidymal fat
              myeloperoxidase expression (representing neutrophils) was
              significantly increased 3.5-fold (P , 0.01) and 2.9-fold (P ,
              0.03), at days 3 and 7 compared with day 0. Immunohystochemistry
              analysis demonstrated a physical binding between neutrophils and
              adipocytes, which was supported by in vitro adherence assay: mouse
              peritoneal neutrophils adhered to a monolayer of 3T3-L1 mouse
              adipocytes, in a manner dependent on their activation state, 41.9
              6 3.7% or 29.5 6 2%, by PMA or the IL-8 analog CXCL1 (KC),
              respectively, compared with 24.8 6 1.5% in unstimulated
              neutrophils, respectively. The degree of surface exposure of CD11b
              (Mac-1) corresponded to the percentage of adhered neutrophils. The
              adherence was prevented by preincubating neutrophils or adipocytes
              with anti-CD11b or anti-ICAM-1 antibodies. Furthermore,
              immunoprecipitation of CD11b from lysates of a mixed
              neutrophil-adipocyte cell population resulted in
              coimmunoprecipitation of ICAM-1, indicating that the interaction
              is mediated by neutrophil CD11b and adipocyte
              ICAM-1.-Elgazar-Carmon, V., A. Rudich, N. Hadad, and R. Levy.
              Neutrophils transiently infiltrate intra-abdominal fat early in
              the course of high-fat feeding.
            authors:
              - affiliation: Ben-Gurion University of the Negev
                affiliationID: '22717'
                affiliationSlug: ben-gurion-university-of-the-negev-ENx1
                authorID: '1070938'
                authorName: Vered Elgazar-Carmon
                authorSequenceNumber: 1
                authorSlug: vered-elgazar-carmon-VewxR
                family: Elgazar-Carmon
                given: Vered
              - affiliation: Ben-Gurion University of the Negev
                affiliationID: '22717'
                affiliationSlug: ben-gurion-university-of-the-negev-ENx1
                authorID: '5757299'
                authorName: Assaf Rudich
                authorSequenceNumber: 2
                authorSlug: assaf-rudich-ejmwOr
                family: Rudich
                given: Assaf
              - affiliation: Ben-Gurion University of the Negev
                affiliationID: '22717'
                affiliationSlug: ben-gurion-university-of-the-negev-ENx1
                authorID: '47105233'
                authorName: Nurit Hadad
                authorSequenceNumber: 3
                authorSlug: nurit-hadad-nL9AXn
                family: Hadad
                given: Nurit
              - affiliation: Ben-Gurion University of the Negev
                affiliationID: '22717'
                affiliationSlug: ben-gurion-university-of-the-negev-ENx1
                authorID: '56245434'
                authorName: Rachel Levy
                authorSequenceNumber: 4
                authorSlug: rachel-levy-O2xWKO
                family: Levy
                given: Rachel
            doi: 10.1194/jlr.m800132-jlr200
            editorialNotices: []
            id: 110260909
            issns:
              - 0022-2275
            issue: '9'
            journal: Journal of Lipid Research
            journalSlug: y8j1x
            keywords:
              - Supplementary key words inflammation
              - obesity
              - adipocytes
            memberId: 78
            normalizedTypes:
              - article
            page: 1894-1903
            preprintLinks: []
            publicationLinks: []
            publisher: Elsevier BV
            retracted: false
            shortJournal: Journal of Lipid Research
            slug: neutrophils-transiently-infiltrate-intra-abdominal-fat-vOGP4W
            title: >-
              Neutrophils transiently infiltrate intra-abdominal fat early in
              the course of high-fat feeding
            type: journal-article
            volume: '49'
            year: 2008
          10.1371/journal.pone.0134089:
            abstract: >-
              Immune reactivity plays an important role in obesity-associated
              metabolic disorders. We investigated immunometabolic phenotype of
              C57Bl/6 and BALB/c mice, prototypical Th1 and Th2-type strains,
              fed chow or high-fat diet (HFD) for 24 weeks. In comparison to
              C57Bl/6 mice, chow-fed BALB/c mice had higher body weight and
              weight gain, lower glycemia, more pronounced liver steatosis, but
              less inflammation and collagen deposition in liver. In response to
              HFD C57Bl/6 mice exhibited higher weight gain, higher glycemia,
              HbA1c and liver glycogen content, increased amount of visceral
              adipose tissue (VAT) and number of VAT associated CD3+CXCR3+ T
              cells, CD11c+ dendritic cells (DCs) and F4/80+ macrophages than
              BALB/c mice. More numerous CD3+ and CD8+ T lymphocytes, myeloid
              DCs, proinflammatory macrophages (F4/80+CD11b+CD11+ and
              F4/80+IL-1β+) and CD11b+Ly6Chigh monocytes and higher levels of
              proinflammatory IL-6, TNF-α and IFN-γ were present in liver in
              HFD-fed C57Bl/6 mice compared with diet-matched BALB/c mice. As
              opposed to C57Bl/6 mice, HFD induced marked liver steatosis and
              upregulated the hepatic LXRα and PPARγ genes in BALB/c mice.
              C57Bl/6 mice fed HFD developed liver fibrosis and increased
              hepatic procollagen and TGF-β mRNA expression, and IL-33, IL-13
              and TGF-β levels in liver homogenates, while BALB/c mice fed HFD
              had scarce collagen deposition in liver. The obtained results
              suggest inherent immunometabolic differences in C57Bl/6 and BALB/c
              mice. Moreover, HFD Th1-type mice on high fat diet regimen are
              more susceptible to adiposity, liver inflammation and fibrosis,
              while Th2-type mice to liver steatosis, which is associated with
              differential immune cell composition in metabolic tissues.
              Strain-dependent differences in immunometabolic phenotype may be
              relevant for studies of obesity-associated metabolic diseases in
              humans.
            authors:
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '11814723'
                authorName: Nemanja Jovicic
                authorSequenceNumber: 1
                authorSlug: nemanja-jovicic-Ja34XE
                family: Jovicic
                given: Nemanja
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '11217656'
                authorName: Ilija Jeftic
                authorSequenceNumber: 2
                authorSlug: ilija-jeftic-0a6VzP
                family: Jeftic
                given: Ilija
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '8132872'
                authorName: Ivan Jovanovic
                authorSequenceNumber: 3
                authorSlug: ivan-jovanovic-wb0zdL
                family: Jovanovic
                given: Ivan
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '81803378'
                authorName: Ivan Jovanović
                authorSequenceNumber: 3
                authorSlug: ivan-jovanovic-OeRb04
                family: Jovanović
                given: Ivan
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '7345090'
                authorName: Gordana Radosavljevic
                authorSequenceNumber: 4
                authorSlug: gordana-radosavljevic-9O90P2
                family: Radosavljevic
                given: Gordana
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '7855593'
                authorName: Nebojsa Arsenijevic
                authorSequenceNumber: 5
                authorSlug: nebojsa-arsenijevic-ANxZXZ
                family: Arsenijevic
                given: Nebojsa
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '6059854'
                authorName: Miodrag L. Lukic
                authorSequenceNumber: 6
                authorSlug: miodrag-l-lukic-685gnX
                family: Lukic
                given: Miodrag L.
              - affiliation: University of Kragujevac
                affiliationID: '22460'
                affiliationSlug: university-of-kragujevac-QWPM
                authorID: '7904963'
                authorName: Nada Pejnovic
                authorSequenceNumber: 7
                authorSlug: nada-pejnovic-DxmP2p
                family: Pejnovic
                given: Nada
            doi: 10.1371/journal.pone.0134089
            editorialNotices: []
            id: 114840636
            issns:
              - 1932-6203
            issue: '7'
            journal: Plos One
            journalSlug: lZbEk
            keywords:
              - Research Article
            memberId: 340
            normalizedTypes:
              - article
            page: e0134089
            preprintLinks: []
            publicationLinks: []
            publisher: Public Library of Science (PLoS)
            retracted: false
            shortJournal: PLoS ONE
            slug: differential-immunometabolic-phenotype-in-th1-lJkWKb
            title: >-
              Differential Immunometabolic Phenotype in Th1 and Th2 Dominant
              Mouse Strains in Response to High-Fat Feeding
            type: journal-article
            volume: '10'
            year: 2015
          10.1530/joe-16-0229:
            abstract: >-
              Group 2 innate lymphoid cells (ILC2s) in white adipose tissue
              (WAT) promotes WAT browning and assists in preventing the
              development of obesity. However, how ILC2 in adipose tissue is
              regulated remains largely unknown. Here, our present study shows
              that ILC2s are present in brown adipose tissue (BAT) as well as
              subcutaneous and epididymal WAT (sWAT and eWAT). The fractions of
              ILC2s, Natural Killer T (NKT) cells and eosinophils in sWAT, eWAT
              and BAT are significantly decreased by high fat diet (HFD) feeding
              and leptin deficiency-induced obesity. Consistent with this, the
              adipose expression and circulating levels of IL-33, a key inducing
              cytokine of ILC2 are significantly downregulated by obesity.
              Furthermore, administration of IL-33 markedly increases the
              fraction of ILC2 and eosinophil as well as expression of UCP1 and
              tyrosine hydroxylase (TH), a rate-limiting enzyme in catecholamine
              biosynthesis, in adipose tissue of HFD-fed mice. On the other
              hand, cold exposure induces the expression levels of IL-33 and
              UCP1 and the population of ILC2 and eosinophil in sWAT, and these
              promoting effects of cold stress are reversed by neutralization of
              IL-33 signaling in vivo. Moreover, the basal and cold-induced
              IL-33 and ILC2/eosinophil pathways are significantly suppressed by
              sympathetic denervation via local injection of 6-hydroxydopamine
              (6-OHDA) in sWAT. Taken together, our data suggests that the
              ILC2/eosinophil axis in adipose tissue is regulated by sympathetic
              nervous system and obesity in IL-33-dependent manner, and
              IL-33-driven ILC2/eosinophil axis are implicated in the
              development of obesity.
            authors:
              - affiliation: Hunan Normal University
                affiliationID: '14267'
                affiliationSlug: hunan-normal-university-Jn2G
                authorID: '20857129'
                authorName: Xiaofeng Ding
                authorSequenceNumber: 1
                authorSlug: xiaofeng-ding-rQzwdO
                family: Ding
                given: Xiaofeng
              - affiliation: Central South University
                affiliationID: '26050'
                affiliationSlug: central-south-university-zdvb
                authorID: '84945490'
                authorName: Yan Luo
                authorSequenceNumber: 2
                authorSlug: yan-luo-9k1n5E
                family: Luo
                given: Yan
              - authorID: '103107960'
                authorName: Xing Zhang
                authorSequenceNumber: 3
                authorSlug: xing-zhang-Qlp0a9
                family: Zhang
                given: Xing
              - authorID: '61202478'
                authorName: Handong Zheng
                authorSequenceNumber: 4
                authorSlug: handong-zheng-OdOzp6
                family: Zheng
                given: Handong
              - authorID: '149529729'
                authorName: Xin Yang
                authorSequenceNumber: 5
                authorSlug: xin-yang-r55Xv4
                family: Yang
                given: Xin
              - authorID: '14741551'
                authorName: Xuexian O. Yang
                authorSequenceNumber: 6
                authorSlug: xuexian-o-yang-YDngGP
                family: Yang
                given: Xuexian O.
              - affiliation: Central South University
                affiliationID: '26050'
                affiliationSlug: central-south-university-zdvb
                authorID: '14791762'
                authorName: Meilian Liu
                authorSequenceNumber: 7
                authorSlug: meilian-liu-dK4QJG
                family: Liu
                given: Meilian
            doi: 10.1530/joe-16-0229
            editorialNotices: []
            id: 117609312
            issns:
              - 0022-0795
              - 1479-6805
            issue: '1'
            journal: Journal of Endocrinology
            journalSlug: r6v4w
            keywords:
              - Article
            memberId: 416
            normalizedTypes:
              - article
            page: 35-48
            preprintLinks: []
            publicationLinks: []
            publisher: Bioscientifica
            retracted: false
            slug: il-33-driven-ilc2-eosinophil-axis-in-fat-0Yeywr
            title: >-
              IL-33-driven ILC2/eosinophil axis in fat is induced by sympathetic
              tone and suppressed by obesity
            type: journal-article
            volume: '231'
            year: 2016
        result:
          citations:
            - refLocation: b13/1
              snippet: >-
                Adipose tissue regulates energy homeostasis through the storage
                of excess calories and the secretion of adipocyte-derived
                secretory proteins such as leptin, adiponectin, and resistin
                10,11 . However, excessive caloric Published: xx xx xxxx OPEN
                www.nature.com/scientificreports/ 2 SCIentIfIC REPORTS | (2018)
                8:9894 | intake induces the overexpansion of adipocytes, which
                results in inflammatory responses within adipose tissue 12
                .Obesity-related metabolic dysfunctions are associated with an
                excessive infiltration of immune cells and chronic inflammation
                in adipose tissue <cite
                data-doi="10.1146/annurev-immunol-031210-101322">13,</cite><cite
                data-doi="10.1038/nature05483">14</cite> .Here, we used
                eosinophil-deficient ∆dblGATA and wild-type (WT) mice to
                investigate the roles of eosinophils in obesity, adipose tissue
                maturation, and associated metabolic responses. We performed
                whole-genome RNA sequencing of the small intestinal tract, which
                suggested the presence of a defective lipid metabolism in the
                absence of eosinophils.
              source: 10.1038/s41598-018-28371-4
              target: 10.1146/annurev-immunol-031210-101322
            - refLocation: b14/1
              snippet: >-
                Adipose tissue regulates energy homeostasis through the storage
                of excess calories and the secretion of adipocyte-derived
                secretory proteins such as leptin, adiponectin, and resistin
                10,11 . However, excessive caloric Published: xx xx xxxx OPEN
                www.nature.com/scientificreports/ 2 SCIentIfIC REPORTS | (2018)
                8:9894 | intake induces the overexpansion of adipocytes, which
                results in inflammatory responses within adipose tissue 12
                .Obesity-related metabolic dysfunctions are associated with an
                excessive infiltration of immune cells and chronic inflammation
                in adipose tissue <cite
                data-doi="10.1146/annurev-immunol-031210-101322">13,</cite><cite
                data-doi="10.1038/nature05483">14</cite> .Here, we used
                eosinophil-deficient ∆dblGATA and wild-type (WT) mice to
                investigate the roles of eosinophils in obesity, adipose tissue
                maturation, and associated metabolic responses. We performed
                whole-genome RNA sequencing of the small intestinal tract, which
                suggested the presence of a defective lipid metabolism in the
                absence of eosinophils.
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/nature05483
            - refLocation: b13/2
              snippet: >-
                Obesity-related metabolic dysfunctions are associated with an
                excessive infiltration of immune cells and chronic inflammation
                in adipose tissue <cite
                data-doi="10.1146/annurev-immunol-031210-101322">13,</cite><cite
                data-doi="10.1038/nature05483">14</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1146/annurev-immunol-031210-101322
            - refLocation: b14/2
              snippet: >-
                Obesity-related metabolic dysfunctions are associated with an
                excessive infiltration of immune cells and chronic inflammation
                in adipose tissue <cite
                data-doi="10.1146/annurev-immunol-031210-101322">13,</cite><cite
                data-doi="10.1038/nature05483">14</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/nature05483
            - refLocation: b15/1
              snippet: >-
                S1). Of note, genes associated with lipid metabolism, such as
                Retnlg, Alox15, and Drd2 <cite
                data-doi="10.1038/oby.2009.192">[15]</cite><cite
                data-doi="10.1006/bmmb.1993.1059">[16]</cite><cite
                data-doi="10.1007/s00125-005-1735-1">[17]</cite> were included
                in the top 10 downregulated genes (Table S1). Additionally, a GO
                analysis of the downregulated genes and visualization of a
                functionally grouped network using the ClueGO plugin <cite
                data-doi="10.1093/bioinformatics/btp101">18</cite> suggested a
                defect in lipase activity (Table S3 and Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/oby.2009.192
            - refLocation: b16/1
              snippet: >-
                S1). Of note, genes associated with lipid metabolism, such as
                Retnlg, Alox15, and Drd2 <cite
                data-doi="10.1038/oby.2009.192">[15]</cite><cite
                data-doi="10.1006/bmmb.1993.1059">[16]</cite><cite
                data-doi="10.1007/s00125-005-1735-1">[17]</cite> were included
                in the top 10 downregulated genes (Table S1). Additionally, a GO
                analysis of the downregulated genes and visualization of a
                functionally grouped network using the ClueGO plugin <cite
                data-doi="10.1093/bioinformatics/btp101">18</cite> suggested a
                defect in lipase activity (Table S3 and Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1006/bmmb.1993.1059
            - refLocation: b17/1
              snippet: >-
                S1). Of note, genes associated with lipid metabolism, such as
                Retnlg, Alox15, and Drd2 <cite
                data-doi="10.1038/oby.2009.192">[15]</cite><cite
                data-doi="10.1006/bmmb.1993.1059">[16]</cite><cite
                data-doi="10.1007/s00125-005-1735-1">[17]</cite> were included
                in the top 10 downregulated genes (Table S1). Additionally, a GO
                analysis of the downregulated genes and visualization of a
                functionally grouped network using the ClueGO plugin <cite
                data-doi="10.1093/bioinformatics/btp101">18</cite> suggested a
                defect in lipase activity (Table S3 and Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1007/s00125-005-1735-1
            - refLocation: b18/1
              snippet: >-
                Of note, genes associated with lipid metabolism, such as Retnlg,
                Alox15, and Drd2 <cite
                data-doi="10.1038/oby.2009.192">[15]</cite><cite
                data-doi="10.1006/bmmb.1993.1059">[16]</cite><cite
                data-doi="10.1007/s00125-005-1735-1">[17]</cite> were included
                in the top 10 downregulated genes (Table S1). Additionally, a GO
                analysis of the downregulated genes and visualization of a
                functionally grouped network using the ClueGO plugin <cite
                data-doi="10.1093/bioinformatics/btp101">18</cite> suggested a
                defect in lipase activity (Table S3 and Fig. S2) and a
                significant decrease in the expression of Lpl was observed (
                Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1093/bioinformatics/btp101
            - refLocation: b10/1
              snippet: >-
                Eosinophil-deficient mice gained less weight and perigonadal fat
                mass and displayed impaired glucose tolerance on a HFD. Excess
                caloric intake induces expansion of fat mass and accelerates
                development of insulin resistance <cite
                data-doi="10.1172/jci31021">10</cite> . To further examine the
                role of eosinophils in adipose tissue expansion and energy
                homeostasis, we fed 8-10-week-old male WT and ΔdblGATA mice with
                a HFD for 12 weeks and monitored their body weights weekly.
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci31021
            - refLocation: b19/1
              snippet: >-
                Eosinophil-deficient mice showed an impaired maturation of
                perigonadal adipocytes on a HFD. The inability of adipose tissue
                to expand to accommodate excess calories causes systemic insulin
                resistance and hyperglycaemia <cite
                data-doi="10.1172/jci7901">19</cite> . As we observed an
                impaired WAT development in HFD-fed ΔdblGATA mice, which showed
                glucose intolerance, we examined whether eosinophils are
                required for adipocyte maturation in diet-induced obesity.
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci7901
            - refLocation: b20/1
              snippet: >-
                Adipocytes support the migration and survival of eosinophils.
                Since eosinophils are resident cells in the adipose tissue <cite
                data-doi="10.1038/s41598-017-06397-4">20</cite> and ΔdblGATA
                mice showed an impairment of adipocyte maturation, we questioned
                whether adipocytes support the migration or survival of
                eosinophils. Eosinophils migrate in a manner dependent on CCL11
                and its receptor, CC chemokine receptor (CCR) 3 2,21 .
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/s41598-017-06397-4
            - refLocation: b22/1
              snippet: >-
                The perigonadal adipose tissue of eosinophil-deficient mice
                showed an increased inflammatory response. Excess calorie intake
                results in chronic inflammation in adipose tissue involving an
                infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci19246
            - refLocation: b23/1
              snippet: >-
                The perigonadal adipose tissue of eosinophil-deficient mice
                showed an increased inflammatory response. Excess calorie intake
                results in chronic inflammation in adipose tissue involving an
                infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1053/j.gastro.2013.04.010
            - refLocation: b24/1
              snippet: >-
                The perigonadal adipose tissue of eosinophil-deficient mice
                showed an increased inflammatory response. Excess calorie intake
                results in chronic inflammation in adipose tissue involving an
                infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/nm.1964
            - refLocation: b25/1
              snippet: >-
                The perigonadal adipose tissue of eosinophil-deficient mice
                showed an increased inflammatory response. Excess calorie intake
                results in chronic inflammation in adipose tissue involving an
                infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/nm.2353
            - refLocation: b26/1
              snippet: >-
                The perigonadal adipose tissue of eosinophil-deficient mice
                showed an increased inflammatory response. Excess calorie intake
                results in chronic inflammation in adipose tissue involving an
                infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1194/jlr.m800132-jlr200
            - refLocation: b27/1
              snippet: >-
                Excess calorie intake results in chronic inflammation in adipose
                tissue involving an infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> . The total numbers of cells
                isolated from the perigonadal WAT of HFD-fed ΔdblGATA and WT
                mice were not significantly different (p = 0.1263, data not
                shown).
              source: 10.1038/s41598-018-28371-4
              target: 10.1074/jbc.m109.061655
            - refLocation: b28/1
              snippet: >-
                Excess calorie intake results in chronic inflammation in adipose
                tissue involving an infiltration of various immune cells <cite
                data-doi="10.1172/jci19246">[22]</cite><cite
                data-doi="10.1053/j.gastro.2013.04.010">[23]</cite><cite
                data-doi="10.1038/nm.1964">[24]</cite><cite
                data-doi="10.1038/nm.2353">[25]</cite><cite
                data-doi="10.1194/jlr.m800132-jlr200">[26]</cite> . In obesity,
                the infiltrated immune cells promote the production of
                pro-inflammatory cytokines that inhibit adipogenesis and insulin
                signalling <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1038/ncb942">28</cite> . The total numbers of cells
                isolated from the perigonadal WAT of HFD-fed ΔdblGATA and WT
                mice were not significantly different (p = 0.1263, data not
                shown).
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/ncb942
            - refLocation: b29/1
              section: The cytokine expression profile in the perigonadal adipose t...
              snippet: >-
                Eosinophil-deficient mice showed lipid accumulation in the
                liver. Excessive lipid accumulation in non-adipose tissues such
                as the liver, muscle, and pancreas is closely associated with
                insulin resistance <cite
                data-doi="10.1007/s11892-008-0032-z">29</cite> . Given that
                lipids tend to be stored ectopically in the absence of
                functional adipocytes <cite
                data-doi="10.1146/annurev.med.53.082901.104057">30</cite> , we
                hypothesized that eosinophil deficiency would influence the
                development of ectopic fat accumulation.
              source: 10.1038/s41598-018-28371-4
              target: 10.1007/s11892-008-0032-z
            - refLocation: b30/1
              section: The cytokine expression profile in the perigonadal adipose t...
              snippet: >-
                Excessive lipid accumulation in non-adipose tissues such as the
                liver, muscle, and pancreas is closely associated with insulin
                resistance <cite data-doi="10.1007/s11892-008-0032-z">29</cite>
                . Given that lipids tend to be stored ectopically in the absence
                of functional adipocytes <cite
                data-doi="10.1146/annurev.med.53.082901.104057">30</cite> , we
                hypothesized that eosinophil deficiency would influence the
                development of ectopic fat accumulation. The livers of HFD-fed
                ΔdblGATA mice exhibited a paler colour and more prominent lipid
                deposits than those of WT mice (Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1146/annurev.med.53.082901.104057
            - refLocation: b31/1
              section: Discussion
              snippet: >-
                Although eosinophils have been characterized as destructive
                effector cells that mediate tissue damage during helminth
                infections and allergic diseases, they are found in various
                tissues under resting conditions without having obvious
                pro-inflammatory activities <cite
                data-doi="10.1172/jci85664">31,</cite><cite
                data-doi="10.1038/mi.2014.123">32</cite> . Accumulating evidence
                has indicated that tissue-resident eosinophils regulate
                biological processes that are not restricted to Th2 immune
                responses.
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci85664
            - refLocation: b32/1
              section: Discussion
              snippet: >-
                Although eosinophils have been characterized as destructive
                effector cells that mediate tissue damage during helminth
                infections and allergic diseases, they are found in various
                tissues under resting conditions without having obvious
                pro-inflammatory activities <cite
                data-doi="10.1172/jci85664">31,</cite><cite
                data-doi="10.1038/mi.2014.123">32</cite> . Accumulating evidence
                has indicated that tissue-resident eosinophils regulate
                biological processes that are not restricted to Th2 immune
                responses.
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/mi.2014.123
            - refLocation: b33/1
              section: Discussion
              snippet: >-
                Accumulating evidence has indicated that tissue-resident
                eosinophils regulate biological processes that are not
                restricted to Th2 immune responses. Eosinophils in adipose
                tissue promote the accumulation of alternatively activated
                macrophages, which protect against insulin resistance induced by
                obesity-associated changes such as the activation of innate
                immune activity, alterations in fatty acid uptake, lipogenesis,
                and energy expenditure that can impact ectopic lipid deposition
                <cite data-doi="10.1016/j.cell.2012.02.017">33</cite> . Obesity
                itself does not necessarily induce insulin resistance and
                primarily results from adipocytes expanding to buffer against
                excess nutrient uptake 9 .
              source: 10.1038/s41598-018-28371-4
              target: 10.1016/j.cell.2012.02.017
            - refLocation: b4/1
              section: Discussion
              snippet: >-
                These cytokines provide signals that promote the permissive
                proliferation and differentiation of eosinophils 2,3 . These
                findings contrast with previous observations that suggested an
                inverse correlation between the abundance of eosinophils in
                adipose tissue and adiposity <cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1016/j.molmet.2017.12.004">34,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> . The reasons for this
                difference are unclear, but mouse strains vary in their
                immunometabolic phenotypes <cite
                data-doi="10.1007/s00125-013-2846-8">36</cite> , as evidenced by
                the difference between BALB/c and C57BL/6 mice in their immune
                cell profiles with a HFD <cite
                data-doi="10.1371/journal.pone.0134089">37</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1126/science.1201475
            - refLocation: b34/1
              section: Discussion
              snippet: >-
                These cytokines provide signals that promote the permissive
                proliferation and differentiation of eosinophils 2,3 . These
                findings contrast with previous observations that suggested an
                inverse correlation between the abundance of eosinophils in
                adipose tissue and adiposity <cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1016/j.molmet.2017.12.004">34,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> . The reasons for this
                difference are unclear, but mouse strains vary in their
                immunometabolic phenotypes <cite
                data-doi="10.1007/s00125-013-2846-8">36</cite> , as evidenced by
                the difference between BALB/c and C57BL/6 mice in their immune
                cell profiles with a HFD <cite
                data-doi="10.1371/journal.pone.0134089">37</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1016/j.molmet.2017.12.004
            - refLocation: b35/1
              section: Discussion
              snippet: >-
                These cytokines provide signals that promote the permissive
                proliferation and differentiation of eosinophils 2,3 . These
                findings contrast with previous observations that suggested an
                inverse correlation between the abundance of eosinophils in
                adipose tissue and adiposity <cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1016/j.molmet.2017.12.004">34,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> . The reasons for this
                difference are unclear, but mouse strains vary in their
                immunometabolic phenotypes <cite
                data-doi="10.1007/s00125-013-2846-8">36</cite> , as evidenced by
                the difference between BALB/c and C57BL/6 mice in their immune
                cell profiles with a HFD <cite
                data-doi="10.1371/journal.pone.0134089">37</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1530/joe-16-0229
            - refLocation: b36/1
              section: Discussion
              snippet: >-
                These findings contrast with previous observations that
                suggested an inverse correlation between the abundance of
                eosinophils in adipose tissue and adiposity <cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1016/j.molmet.2017.12.004">34,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> . The reasons for this
                difference are unclear, but mouse strains vary in their
                immunometabolic phenotypes <cite
                data-doi="10.1007/s00125-013-2846-8">36</cite> , as evidenced by
                the difference between BALB/c and C57BL/6 mice in their immune
                cell profiles with a HFD <cite
                data-doi="10.1371/journal.pone.0134089">37</cite> . In line with
                this, chow diet-fed male C57BL/6 mice showed significantly more
                eosinophils in the perigonadal adipose tissue than BALB/c mice,
                while showing fewer eosinophils in the small intestine ( Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1007/s00125-013-2846-8
            - refLocation: b37/1
              section: Discussion
              snippet: >-
                These findings contrast with previous observations that
                suggested an inverse correlation between the abundance of
                eosinophils in adipose tissue and adiposity <cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1016/j.molmet.2017.12.004">34,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> . The reasons for this
                difference are unclear, but mouse strains vary in their
                immunometabolic phenotypes <cite
                data-doi="10.1007/s00125-013-2846-8">36</cite> , as evidenced by
                the difference between BALB/c and C57BL/6 mice in their immune
                cell profiles with a HFD <cite
                data-doi="10.1371/journal.pone.0134089">37</cite> . In line with
                this, chow diet-fed male C57BL/6 mice showed significantly more
                eosinophils in the perigonadal adipose tissue than BALB/c mice,
                while showing fewer eosinophils in the small intestine ( Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1371/journal.pone.0134089
            - refLocation: b38/1
              section: Discussion
              snippet: >-
                S13). There are likely differences in microbiota, and thus
                endotoxin exposure may explain the weight difference between
                results of previous reports and those of our study, as exposure
                to microbial endotoxins may alter eosinophil maturation and
                activities <cite
                data-doi="10.1016/j.celrep.2016.06.007">38</cite> . Considering
                that our results are consistent with previous reports indicating
                eosinophils role in the regulation of metabolic homeostasis
                <cite data-doi="10.1016/j.cell.2014.03.066">4,</cite><cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> , we propose that
                differences in mice strain and cohort might account for the
                divergence on eosinophil abundance in the adipose tissue between
                this study and previous observations.
              source: 10.1038/s41598-018-28371-4
              target: 10.1016/j.celrep.2016.06.007
            - refLocation: b3/1
              section: Discussion
              snippet: >-
                There are likely differences in microbiota, and thus endotoxin
                exposure may explain the weight difference between results of
                previous reports and those of our study, as exposure to
                microbial endotoxins may alter eosinophil maturation and
                activities <cite
                data-doi="10.1016/j.celrep.2016.06.007">38</cite> . Considering
                that our results are consistent with previous reports indicating
                eosinophils role in the regulation of metabolic homeostasis
                <cite data-doi="10.1016/j.cell.2014.03.066">4,</cite><cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> , we propose that
                differences in mice strain and cohort might account for the
                divergence on eosinophil abundance in the adipose tissue between
                this study and previous observations.
              source: 10.1038/s41598-018-28371-4
              target: 10.1016/j.cell.2014.03.066
            - refLocation: b4/2
              section: Discussion
              snippet: >-
                There are likely differences in microbiota, and thus endotoxin
                exposure may explain the weight difference between results of
                previous reports and those of our study, as exposure to
                microbial endotoxins may alter eosinophil maturation and
                activities <cite
                data-doi="10.1016/j.celrep.2016.06.007">38</cite> . Considering
                that our results are consistent with previous reports indicating
                eosinophils role in the regulation of metabolic homeostasis
                <cite data-doi="10.1016/j.cell.2014.03.066">4,</cite><cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> , we propose that
                differences in mice strain and cohort might account for the
                divergence on eosinophil abundance in the adipose tissue between
                this study and previous observations.
              source: 10.1038/s41598-018-28371-4
              target: 10.1126/science.1201475
            - refLocation: b35/2
              section: Discussion
              snippet: >-
                There are likely differences in microbiota, and thus endotoxin
                exposure may explain the weight difference between results of
                previous reports and those of our study, as exposure to
                microbial endotoxins may alter eosinophil maturation and
                activities <cite
                data-doi="10.1016/j.celrep.2016.06.007">38</cite> . Considering
                that our results are consistent with previous reports indicating
                eosinophils role in the regulation of metabolic homeostasis
                <cite data-doi="10.1016/j.cell.2014.03.066">4,</cite><cite
                data-doi="10.1126/science.1201475">5,</cite><cite
                data-doi="10.1530/joe-16-0229">35</cite> , we propose that
                differences in mice strain and cohort might account for the
                divergence on eosinophil abundance in the adipose tissue between
                this study and previous observations.
              source: 10.1038/s41598-018-28371-4
              target: 10.1530/joe-16-0229
            - refLocation: b8/1
              section: Discussion
              snippet: >-
                The fat cells of adipose tissue are the only cells in the body
                that are designed to safely contain large amounts of fat <cite
                data-doi="10.1186/s12944-015-0123-1">9</cite> . Therefore, the
                impaired development of perigonadal adipose tissue observed in
                HFD-fed ΔdblGATA mice may lead to the accumulation of lipid
                outside adipose tissue.
              source: 10.1038/s41598-018-28371-4
              target: 10.1186/s12944-015-0123-1
            - refLocation: b33/2
              section: Discussion
              snippet: >-
                Therefore, the impaired development of perigonadal adipose
                tissue observed in HFD-fed ΔdblGATA mice may lead to the
                accumulation of lipid outside adipose tissue. The excessive
                accumulation of lipids in non-adipose tissues is closely
                associated with insulin resistance <cite
                data-doi="10.1016/j.cell.2012.02.017">33</cite> , and we propose
                that ectopic fat accumulation in HFD-fed ΔdblGATA mice might
                account for their glucose intolerance. Although increased
                visceral adiposity has been implicated in hepatic insulin
                resistance, patients with severe lipodystrophy, as well as a
                mouse model of lipoatrophy, manifest insulin resistance
                associated with lipid deposition in the liver <cite
                data-doi="10.1172/jci15001">39,</cite><cite
                data-doi="10.1074/jbc.275.12.8456">40</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1016/j.cell.2012.02.017
            - refLocation: b39/1
              section: Discussion
              snippet: >-
                The excessive accumulation of lipids in non-adipose tissues is
                closely associated with insulin resistance <cite
                data-doi="10.1016/j.cell.2012.02.017">33</cite> , and we propose
                that ectopic fat accumulation in HFD-fed ΔdblGATA mice might
                account for their glucose intolerance. Although increased
                visceral adiposity has been implicated in hepatic insulin
                resistance, patients with severe lipodystrophy, as well as a
                mouse model of lipoatrophy, manifest insulin resistance
                associated with lipid deposition in the liver <cite
                data-doi="10.1172/jci15001">39,</cite><cite
                data-doi="10.1074/jbc.275.12.8456">40</cite> . The significant
                decrease in the expression of Pparg, which encodes a
                transcription factor involved in adipocyte differentiation, and
                genes associated with lipid droplet formation (Cav1, Cav2, Cd36,
                and Cidec) in the perigonadal WAT of HFD-fed ΔdblGATA mice (
                Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci15001
            - refLocation: b40/1
              section: Discussion
              snippet: >-
                The excessive accumulation of lipids in non-adipose tissues is
                closely associated with insulin resistance <cite
                data-doi="10.1016/j.cell.2012.02.017">33</cite> , and we propose
                that ectopic fat accumulation in HFD-fed ΔdblGATA mice might
                account for their glucose intolerance. Although increased
                visceral adiposity has been implicated in hepatic insulin
                resistance, patients with severe lipodystrophy, as well as a
                mouse model of lipoatrophy, manifest insulin resistance
                associated with lipid deposition in the liver <cite
                data-doi="10.1172/jci15001">39,</cite><cite
                data-doi="10.1074/jbc.275.12.8456">40</cite> . The significant
                decrease in the expression of Pparg, which encodes a
                transcription factor involved in adipocyte differentiation, and
                genes associated with lipid droplet formation (Cav1, Cav2, Cd36,
                and Cidec) in the perigonadal WAT of HFD-fed ΔdblGATA mice (
                Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1074/jbc.275.12.8456
            - refLocation: b41/1
              section: Discussion
              snippet: >-
                3) suggests insufficient lipid storage in adipose tissue in the
                absence of eosinophils. Concordantly, the expression of Lpl,
                Slc2a4, and Adipoq, which are regulated by Pparg and involved in
                glucose homeostasis <cite
                data-doi="10.1074/jbc.m114.628487">41</cite> , significantly
                decreased in the perigonadal adipose tissue of HFD-fed ΔdblGATA
                mice (Fig. 3).
              source: 10.1038/s41598-018-28371-4
              target: 10.1074/jbc.m114.628487
            - refLocation: b28/2
              section: Discussion
              snippet: >-
                We suggest that an altered immune environment in the perigonadal
                fat of HFD-fed ΔdblGATA accounts for the decreased expression of
                adipogenic genes. The exposure of preadipocytes to
                pro-inflammatory cytokines inhibits adipogenesis by reducing the
                expression of Pparg and inhibiting the adipogenic action of
                insulin <cite data-doi="10.1038/ncb942">28</cite> . Th1
                cytokines, including IFN-γ, can inhibit insulin signalling and
                lipid droplet formation <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1194/jlr.m008771">42</cite> , while Th2 cytokines,
                including IL-4 and IL-13, can suppress inflammatory responses in
                adipose tissue <cite data-doi="10.1038/nri2921">43</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/ncb942
            - refLocation: b27/2
              section: Discussion
              snippet: >-
                The exposure of preadipocytes to pro-inflammatory cytokines
                inhibits adipogenesis by reducing the expression of Pparg and
                inhibiting the adipogenic action of insulin <cite
                data-doi="10.1038/ncb942">28</cite> . Th1 cytokines, including
                IFN-γ, can inhibit insulin signalling and lipid droplet
                formation <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1194/jlr.m008771">42</cite> , while Th2 cytokines,
                including IL-4 and IL-13, can suppress inflammatory responses in
                adipose tissue <cite data-doi="10.1038/nri2921">43</cite> . The
                increased expression of Ifng and decreased expression of Il4 and
                Il13 in the perigonadal fat of HFD-fed ΔdblGATA mice imply that
                the microenvironments of the WAT of these mice are unfavourable
                for adipocyte maturation.
              source: 10.1038/s41598-018-28371-4
              target: 10.1074/jbc.m109.061655
            - refLocation: b42/1
              section: Discussion
              snippet: >-
                The exposure of preadipocytes to pro-inflammatory cytokines
                inhibits adipogenesis by reducing the expression of Pparg and
                inhibiting the adipogenic action of insulin <cite
                data-doi="10.1038/ncb942">28</cite> . Th1 cytokines, including
                IFN-γ, can inhibit insulin signalling and lipid droplet
                formation <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1194/jlr.m008771">42</cite> , while Th2 cytokines,
                including IL-4 and IL-13, can suppress inflammatory responses in
                adipose tissue <cite data-doi="10.1038/nri2921">43</cite> . The
                increased expression of Ifng and decreased expression of Il4 and
                Il13 in the perigonadal fat of HFD-fed ΔdblGATA mice imply that
                the microenvironments of the WAT of these mice are unfavourable
                for adipocyte maturation.
              source: 10.1038/s41598-018-28371-4
              target: 10.1194/jlr.m008771
            - refLocation: b43/1
              section: Discussion
              snippet: >-
                The exposure of preadipocytes to pro-inflammatory cytokines
                inhibits adipogenesis by reducing the expression of Pparg and
                inhibiting the adipogenic action of insulin <cite
                data-doi="10.1038/ncb942">28</cite> . Th1 cytokines, including
                IFN-γ, can inhibit insulin signalling and lipid droplet
                formation <cite
                data-doi="10.1074/jbc.m109.061655">27,</cite><cite
                data-doi="10.1194/jlr.m008771">42</cite> , while Th2 cytokines,
                including IL-4 and IL-13, can suppress inflammatory responses in
                adipose tissue <cite data-doi="10.1038/nri2921">43</cite> . The
                increased expression of Ifng and decreased expression of Il4 and
                Il13 in the perigonadal fat of HFD-fed ΔdblGATA mice imply that
                the microenvironments of the WAT of these mice are unfavourable
                for adipocyte maturation.
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/nri2921
            - refLocation: b22/2
              section: Discussion
              snippet: >-
                Obesity is associated with an increased infiltration of
                macrophages, preferentially the pro-inflammatory M1 phenotype,
                into adipose tissue <cite data-doi="10.1172/jci19246">22</cite>
                , and IL-4 produced by adipose tissue eosinophils supports the
                polarization of anti-inflammatory M2 macrophages <cite
                data-doi="10.1126/science.1201475">5</cite> . In agreement this
                with this idea, conditioned media (CM) collected from
                eosinophilic cell line EoL-1 cells or CM from palmitic-acid
                stimulated EoL-1 cells promoted M2-polarization of monocytic
                THP-1 cells (Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci19246
            - refLocation: b4/3
              section: Discussion
              snippet: >-
                Obesity is associated with an increased infiltration of
                macrophages, preferentially the pro-inflammatory M1 phenotype,
                into adipose tissue <cite data-doi="10.1172/jci19246">22</cite>
                , and IL-4 produced by adipose tissue eosinophils supports the
                polarization of anti-inflammatory M2 macrophages <cite
                data-doi="10.1126/science.1201475">5</cite> . In agreement this
                with this idea, conditioned media (CM) collected from
                eosinophilic cell line EoL-1 cells or CM from palmitic-acid
                stimulated EoL-1 cells promoted M2-polarization of monocytic
                THP-1 cells (Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1126/science.1201475
            - refLocation: b44/1
              section: Discussion
              snippet: >-
                5). Given that hypoxia induces macrophage proliferation and
                polarization towards the M2 phenotype <cite
                data-doi="10.1002/ijc.21422">44,</cite><cite
                data-doi="10.1080/2162402x.2015.1056442">45</cite> , it is
                plausible that hypoxia determined the composition of macrophages
                in the adipose tissue of HFD-fed ΔdblGATA mice. The
                significantly elevated concentration of lactate in the
                perigonadal WAT of HFD-fed ΔdblGATA mice also supports this idea
                (Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1002/ijc.21422
            - refLocation: b45/1
              section: Discussion
              snippet: >-
                5). Given that hypoxia induces macrophage proliferation and
                polarization towards the M2 phenotype <cite
                data-doi="10.1002/ijc.21422">44,</cite><cite
                data-doi="10.1080/2162402x.2015.1056442">45</cite> , it is
                plausible that hypoxia determined the composition of macrophages
                in the adipose tissue of HFD-fed ΔdblGATA mice. The
                significantly elevated concentration of lactate in the
                perigonadal WAT of HFD-fed ΔdblGATA mice also supports this idea
                (Fig.
              source: 10.1038/s41598-018-28371-4
              target: 10.1080/2162402x.2015.1056442
            - refLocation: b46/1
              section: Discussion
              snippet: >-
                Although adipose tissue is rich in stem cells that can
                differentiate into fat cells to contain excess energy <cite
                data-doi="10.1091/mbc.e02-02-0105">46</cite> , the
                pro-inflammatory microenvironment of adipose tissue induced by
                obesity is associated with the inhibition of adipocyte
                maturation and increased adipocyte death <cite
                data-doi="10.1172/jci31021">10,</cite><cite
                data-doi="10.1038/ijo.2008.229">12</cite> . Our data demonstrate
                that adipocytes provide signals to promote eosinophil migration
                and survival, and that eosinophils support adipocyte maturation
                and protect adipose tissue against inflammatory changes.
              source: 10.1038/s41598-018-28371-4
              target: 10.1091/mbc.e02-02-0105
            - refLocation: b10/2
              section: Discussion
              snippet: >-
                Although adipose tissue is rich in stem cells that can
                differentiate into fat cells to contain excess energy <cite
                data-doi="10.1091/mbc.e02-02-0105">46</cite> , the
                pro-inflammatory microenvironment of adipose tissue induced by
                obesity is associated with the inhibition of adipocyte
                maturation and increased adipocyte death <cite
                data-doi="10.1172/jci31021">10,</cite><cite
                data-doi="10.1038/ijo.2008.229">12</cite> . Our data demonstrate
                that adipocytes provide signals to promote eosinophil migration
                and survival, and that eosinophils support adipocyte maturation
                and protect adipose tissue against inflammatory changes.
              source: 10.1038/s41598-018-28371-4
              target: 10.1172/jci31021
            - refLocation: b12/1
              section: Discussion
              snippet: >-
                Although adipose tissue is rich in stem cells that can
                differentiate into fat cells to contain excess energy <cite
                data-doi="10.1091/mbc.e02-02-0105">46</cite> , the
                pro-inflammatory microenvironment of adipose tissue induced by
                obesity is associated with the inhibition of adipocyte
                maturation and increased adipocyte death <cite
                data-doi="10.1172/jci31021">10,</cite><cite
                data-doi="10.1038/ijo.2008.229">12</cite> . Our data demonstrate
                that adipocytes provide signals to promote eosinophil migration
                and survival, and that eosinophils support adipocyte maturation
                and protect adipose tissue against inflammatory changes.
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/ijo.2008.229
            - refLocation: b47/1
              section: Method
              snippet: >-
                RNA isolated from the small intestine of 8-10-week-old WT (n =
                4) and ∆dblGATA mice (n = 4) was subjected to RNA sequencing at
                the Cincinnati Children's Hospital Medical Center sequencing
                core. Sequencing data were demultiplexed and reads were mapped
                to the mm10 mouse genome reference using TopHat <cite
                data-doi="10.1093/bioinformatics/btp120">47</cite> . The total
                number of mapped reads per transcript was determined and the
                data were normalized to detect the number of fragments per
                kilobase of exon per million fragments mapped (FPKM) using
                Cufflinks <cite data-doi="10.1038/nbt.1621">48</cite> .
              source: 10.1038/s41598-018-28371-4
              target: 10.1093/bioinformatics/btp120
            - refLocation: b48/1
              section: Method
              snippet: >-
                Sequencing data were demultiplexed and reads were mapped to the
                mm10 mouse genome reference using TopHat <cite
                data-doi="10.1093/bioinformatics/btp120">47</cite> . The total
                number of mapped reads per transcript was determined and the
                data were normalized to detect the number of fragments per
                kilobase of exon per million fragments mapped (FPKM) using
                Cufflinks <cite data-doi="10.1038/nbt.1621">48</cite> . An FPKM
                &gt;0.1 in at least 1 of the analysed samples was used to filter
                for potentially significant gene expression.
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/nbt.1621
            - refLocation: b50/1
              section: Method
              snippet: >-
                Insulin (0.75 U/kg) or saline was infused into the liver via the
                portal vein. Five minutes after infusion, liver, perigonadal
                fat, and skeletal muscle were quickly excised and snap-frozen in
                liquid nitrogen <cite data-doi="10.1002/hep.26015">50</cite> .
                At sacrifice, all mice were weighed and the livers and
                perigonadal fat were removed and weighed.
              source: 10.1038/s41598-018-28371-4
              target: 10.1002/hep.26015
            - refLocation: b50/2
              section: Method
              snippet: >-
                Total protein extraction and western blot analysis. The tissue
                lysates were prepared in ice-cold tissue lysis buffer (50 mM
                Tris-HCl, pH 7.5; 150 mM NaCl; 1% Nonidet P-40; 0.5% sodium
                deoxycholate; 0.1% SDS) containing 50 mM NaF, 2 mM Na 3 VO 4 ,
                protease inhibitors (Sigma-Aldrich, St. Louis, MO, USA) and
                phosphatase inhibitors (Sigma-Aldrich) and total protein was
                extracted as previously described <cite
                data-doi="10.1002/hep.26015">50</cite> . Samples from tissue
                lysates were resolved by SDS-PAGE and then transferred to a
                nitrocellulose membrane.
              source: 10.1038/s41598-018-28371-4
              target: 10.1002/hep.26015
            - refLocation: b20/2
              section: Isolation of eosinophils.
              snippet: >-
                Eosinophils were isolated from the peritoneal cavity of CD3-IL-5
                transgenic mice as described <cite
                data-doi="10.1038/s41598-017-06397-4">20</cite> and used for
                chemotaxis assay and co-culture with adipocyte-differentiated
                3T3-L1 cells. Total cells were extracted and subjected to
                lymphocyte depletion using a MACS ® system with antibodies
                against CD90.2 and CD45R (Miltenyi Biotec, Auburn, CA, USA).
              source: 10.1038/s41598-018-28371-4
              target: 10.1038/s41598-017-06397-4
          filetype: pdf
          metadata:
            abstract: >-
              Accumulating data have indicated a fundamental role of eosinophils
              in regulating adipose tissue homeostasis. Here, we performed
              whole-genome RNA sequencing of the small intestinal tract, which
              suggested the presence of impaired lipid metabolism in
              eosinophil-deficient ΔdblGATA mice. ΔdblGATA mice fed a high-fat
              diet (HFD) showed reduced body fat mass, impaired enlargement of
              adipocytes, decreased expression of adipogenic genes, and
              developed glucose intolerance. HFD induced accumulation of
              eosinophils in the perigonadal white adipose tissue. Concordantly,
              adipocytedifferentiated 3T3-L1 cells promoted the migration of
              eosinophils through the expression of CCL11 (eotaxin-1) and likely
              promoted their survival through the expression of interleukin
              (IL)-3, IL-5, and granulocyte-macrophage colony-stimulating
              factor. HFD-fed ΔdblGATA mice showed increased infiltration of
              macrophages, CD4 + T-cells, and B-cells, increased expression of
              interferon-γ, and decreased expression of IL-4 and IL-13 in white
              adipose tissue. Interferon-γ treatment significantly decreased
              lipid deposition in adipocyte-differentiated 3T3-L1 cells, while
              IL-4 treatment promoted lipid accumulation. Notably, HFD-fed
              ΔdblGATA mice showed increased lipid storage in the liver as
              compared with wild-type mice. We propose that obesity promotes the
              infiltration of eosinophils into adipose tissue that subsequently
              contribute to the metabolic homeostasis by promoting adipocyte
              maturation.Eosinophils have been considered as destructive cells
              involved in T helper cell type (Th) 2 immune responses in
              parasitic infections or allergic diseases 1 . However,
              accumulating evidence has indicated additional roles for
              eosinophils. For example, eosinophils reside in several organs
              including the gastrointestinal tract 2,3 and adipose tissue and
              contribute to metabolic homeostasis 4,5 . Adipose tissue
              eosinophils secrete interleukin (IL)-4 and induce the polarization
              of white adipose tissue (WAT) macrophages into
              alternatively-activated macrophages, which support glucose
              tolerance by regulating local catecholamine stores in the
              microenvironment through the import of catecholamines produced by
              nerve cells 4,6,7 . Despite recent advances, the roles of
              eosinophils in the adipose tissue and their effects on adipocyte
              function remain incompletely understood.Obesity and its associated
              metabolic disorders are serious health problems worldwide 8 .
              However, obesity is not necessarily an adverse metabolic condition
              when the excess fat is stored in adipose tissue that responds to
              insulin 9 . Adipose tissue regulates energy homeostasis through
              the storage of excess calories and the secretion of
              adipocyte-derived secretory proteins such as leptin, adiponectin,
              and resistin 10,11 . However, excessive caloric Published: xx xx
              xxxx OPEN www.nature.com/scientificreports/ 2 SCIentIfIC REPORTS |
              (2018) 8:9894 | intake induces the overexpansion of adipocytes,
              which results in inflammatory responses within adipose tissue 12
              .Obesity-related metabolic dysfunctions are associated with an
              excessiv...
            authors:
              - family: Lee
                given: Eun-Hui
              - family: Itan
                given: Michal
              - family: Jang
                given: Jinsun
              - family: Gu
                given: Hyeon-Jung
              - family: Rozenberg
                given: Perri
              - family: Mingler
                given: Melissa
              - family: Wen
                given: Ting
              - family: Yoon
                given: Jiyoung
              - family: Park
                given: Shi-Young
              - family: Roh
                given: Joo
              - family: Choi
                given: Soo
              - family: Park
                given: Woo-Jae
              - family: Munitz
                given: Ariel
              - family: Jung
                given: Yunjae
            keywords: []
            title: >-
              Eosinophils support adipocyte maturation and promote glucose
              tolerance in obesity OPEN
          source: 10.1038/s41598-018-28371-4
        status: SUCCESS
        tallies:
          10.1002/hep.26015:
            citingPublications: 125
            contradicting: 1
            doi: 10.1002/hep.26015
            mentioning: 126
            supporting: 9
            total: 136
            unclassified: 0
          10.1002/ijc.21422:
            citingPublications: 165
            contradicting: 1
            doi: 10.1002/ijc.21422
            mentioning: 132
            supporting: 0
            total: 136
            unclassified: 3
          10.1006/bmmb.1993.1059:
            citingPublications: 117
            contradicting: 0
            doi: 10.1006/bmmb.1993.1059
            mentioning: 56
            supporting: 2
            total: 58
            unclassified: 0
          10.1007/s00125-005-1735-1:
            citingPublications: 38
            contradicting: 0
            doi: 10.1007/s00125-005-1735-1
            mentioning: 38
            supporting: 1
            total: 41
            unclassified: 2
          10.1007/s00125-013-2846-8:
            citingPublications: 285
            contradicting: 2
            doi: 10.1007/s00125-013-2846-8
            mentioning: 234
            supporting: 36
            total: 278
            unclassified: 6
          10.1007/s11892-008-0032-z:
            citingPublications: 74
            contradicting: 0
            doi: 10.1007/s11892-008-0032-z
            mentioning: 53
            supporting: 0
            total: 53
            unclassified: 0
          10.1016/j.cell.2012.02.017:
            citingPublications: 1527
            contradicting: 1
            doi: 10.1016/j.cell.2012.02.017
            mentioning: 1352
            supporting: 35
            total: 1406
            unclassified: 18
          10.1016/j.cell.2014.03.066:
            citingPublications: 640
            contradicting: 7
            doi: 10.1016/j.cell.2014.03.066
            mentioning: 634
            supporting: 23
            total: 672
            unclassified: 8
          10.1016/j.celrep.2016.06.007:
            citingPublications: 90
            contradicting: 1
            doi: 10.1016/j.celrep.2016.06.007
            mentioning: 100
            supporting: 4
            total: 106
            unclassified: 1
          10.1016/j.molmet.2017.12.004:
            citingPublications: 40
            contradicting: 2
            doi: 10.1016/j.molmet.2017.12.004
            mentioning: 30
            supporting: 2
            total: 34
            unclassified: 0
          10.1038/ijo.2008.229:
            citingPublications: 421
            contradicting: 0
            doi: 10.1038/ijo.2008.229
            mentioning: 347
            supporting: 6
            total: 366
            unclassified: 13
          10.1038/mi.2014.123:
            citingPublications: 127
            contradicting: 0
            doi: 10.1038/mi.2014.123
            mentioning: 164
            supporting: 8
            total: 176
            unclassified: 4
          10.1038/nature05483:
            citingPublications: 1670
            contradicting: 1
            doi: 10.1038/nature05483
            mentioning: 1404
            supporting: 20
            total: 1449
            unclassified: 24
          10.1038/nbt.1621:
            citingPublications: 11632
            contradicting: 1
            doi: 10.1038/nbt.1621
            mentioning: 10800
            supporting: 42
            total: 10875
            unclassified: 32
          10.1038/ncb942:
            citingPublications: 261
            contradicting: 1
            doi: 10.1038/ncb942
            mentioning: 189
            supporting: 13
            total: 206
            unclassified: 3
          10.1038/nm.1964:
            citingPublications: 1706
            contradicting: 12
            doi: 10.1038/nm.1964
            mentioning: 1760
            supporting: 94
            total: 1884
            unclassified: 18
          10.1038/nm.2353:
            citingPublications: 764
            contradicting: 7
            doi: 10.1038/nm.2353
            mentioning: 986
            supporting: 50
            total: 1054
            unclassified: 11
          10.1038/nri2921:
            citingPublications: 2977
            contradicting: 5
            doi: 10.1038/nri2921
            mentioning: 2747
            supporting: 62
            total: 2923
            unclassified: 109
          10.1038/oby.2009.192:
            citingPublications: 115
            contradicting: 0
            doi: 10.1038/oby.2009.192
            mentioning: 130
            supporting: 5
            total: 136
            unclassified: 1
          10.1038/s41598-017-06397-4:
            citingPublications: 18
            contradicting: 2
            doi: 10.1038/s41598-017-06397-4
            mentioning: 23
            supporting: 0
            total: 25
            unclassified: 0
          10.1053/j.gastro.2013.04.010:
            citingPublications: 200
            contradicting: 3
            doi: 10.1053/j.gastro.2013.04.010
            mentioning: 185
            supporting: 13
            total: 208
            unclassified: 7
          10.1074/jbc.275.12.8456:
            citingPublications: 387
            contradicting: 1
            doi: 10.1074/jbc.275.12.8456
            mentioning: 278
            supporting: 19
            total: 305
            unclassified: 7
          10.1074/jbc.m109.061655:
            citingPublications: 185
            contradicting: 2
            doi: 10.1074/jbc.m109.061655
            mentioning: 163
            supporting: 6
            total: 171
            unclassified: 0
          10.1074/jbc.m114.628487:
            citingPublications: 39
            contradicting: 0
            doi: 10.1074/jbc.m114.628487
            mentioning: 29
            supporting: 0
            total: 29
            unclassified: 0
          10.1080/2162402x.2015.1056442:
            citingPublications: 69
            contradicting: 0
            doi: 10.1080/2162402x.2015.1056442
            mentioning: 66
            supporting: 7
            total: 73
            unclassified: 0
          10.1091/mbc.e02-02-0105:
            citingPublications: 5519
            contradicting: 12
            doi: 10.1091/mbc.e02-02-0105
            mentioning: 4308
            supporting: 140
            total: 4586
            unclassified: 126
          10.1093/bioinformatics/btp101:
            citingPublications: 4038
            contradicting: 0
            doi: 10.1093/bioinformatics/btp101
            mentioning: 3546
            supporting: 8
            total: 3564
            unclassified: 10
          10.1093/bioinformatics/btp120:
            citingPublications: 10003
            contradicting: 0
            doi: 10.1093/bioinformatics/btp120
            mentioning: 8338
            supporting: 8
            total: 8389
            unclassified: 43
          10.1126/science.1201475:
            citingPublications: 1030
            contradicting: 3
            doi: 10.1126/science.1201475
            mentioning: 1187
            supporting: 45
            total: 1244
            unclassified: 9
          10.1146/annurev-immunol-031210-101322:
            citingPublications: 2687
            contradicting: 1
            doi: 10.1146/annurev-immunol-031210-101322
            mentioning: 2330
            supporting: 61
            total: 2451
            unclassified: 59
          10.1146/annurev.med.53.082901.104057:
            citingPublications: 844
            contradicting: 0
            doi: 10.1146/annurev.med.53.082901.104057
            mentioning: 609
            supporting: 14
            total: 655
            unclassified: 32
          10.1172/jci15001:
            citingPublications: 432
            contradicting: 1
            doi: 10.1172/jci15001
            mentioning: 95
            supporting: 6
            total: 102
            unclassified: 0
          10.1172/jci19246:
            citingPublications: 5786
            contradicting: 20
            doi: 10.1172/jci19246
            mentioning: 4804
            supporting: 160
            total: 5100
            unclassified: 116
          10.1172/jci31021:
            citingPublications: 1058
            contradicting: 3
            doi: 10.1172/jci31021
            mentioning: 925
            supporting: 52
            total: 1011
            unclassified: 31
          10.1172/jci7901:
            citingPublications: 555
            contradicting: 1
            doi: 10.1172/jci7901
            mentioning: 378
            supporting: 13
            total: 400
            unclassified: 8
          10.1172/jci85664:
            citingPublications: 268
            contradicting: 4
            doi: 10.1172/jci85664
            mentioning: 356
            supporting: 28
            total: 394
            unclassified: 6
          10.1186/s12944-015-0123-1:
            citingPublications: 296
            contradicting: 0
            doi: 10.1186/s12944-015-0123-1
            mentioning: 237
            supporting: 4
            total: 246
            unclassified: 5
          10.1194/jlr.m008771:
            citingPublications: 57
            contradicting: 0
            doi: 10.1194/jlr.m008771
            mentioning: 50
            supporting: 4
            total: 55
            unclassified: 1
          10.1194/jlr.m800132-jlr200:
            citingPublications: 349
            contradicting: 0
            doi: 10.1194/jlr.m800132-jlr200
            mentioning: 296
            supporting: 19
            total: 317
            unclassified: 2
          10.1371/journal.pone.0134089:
            citingPublications: 69
            contradicting: 1
            doi: 10.1371/journal.pone.0134089
            mentioning: 46
            supporting: 5
            total: 52
            unclassified: 0
          10.1530/joe-16-0229:
            citingPublications: 50
            contradicting: 2
            doi: 10.1530/joe-16-0229
            mentioning: 46
            supporting: 3
            total: 51
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
    TaskInfo:
      properties:
        description:
          type: string
          title: Description
        step:
          type: integer
          title: Step
        totalSteps:
          type: integer
          title: Totalsteps
      type: object
      required:
        - description
        - step
        - totalSteps
      title: TaskInfo
    KalaParserReport:
      properties:
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        metadata:
          $ref: '#/components/schemas/SourceMetadata'
        filetype:
          type: string
          const: pdf
          title: Filetype
        citations:
          items:
            $ref: '#/components/schemas/Citation'
          type: array
          title: Citations
      type: object
      required:
        - source
        - metadata
        - filetype
        - citations
      title: KalaParserReport
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
    SourceMetadata:
      properties:
        title:
          anyOf:
            - type: string
            - type: 'null'
          title: Title
        abstract:
          anyOf:
            - type: string
            - type: 'null'
          title: Abstract
        authors:
          items:
            $ref: '#/components/schemas/AuthorSchema'
          type: array
          title: Authors
        journal:
          anyOf:
            - type: string
            - type: 'null'
          title: Journal
        volume:
          anyOf:
            - type: string
            - type: 'null'
          title: Volume
        date:
          anyOf:
            - type: string
            - type: 'null'
          title: Date
        page:
          anyOf:
            - type: string
            - type: 'null'
          title: Page
        keywords:
          items:
            type: string
          type: array
          title: Keywords
      type: object
      title: SourceMetadata
    Citation:
      properties:
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        target:
          type: string
          title: Target
        snippet:
          type: string
          title: Snippet
        refLocation:
          anyOf:
            - type: string
            - type: 'null'
          title: Reflocation
        section:
          anyOf:
            - type: string
            - type: 'null'
          title: Section
      type: object
      required:
        - source
        - target
        - snippet
      title: Citation
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
