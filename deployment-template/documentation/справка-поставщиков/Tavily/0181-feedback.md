> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Tavily: feedback

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.tavily.com/documentation/api-reference/endpoint/feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Feedback

> Submit feedback on how relevant and useful Tavily's results were for your task.

<Warning>
  **Beta.** This endpoint is in beta: the request shape may still change, and it may be
  temporarily unavailable during maintenance. Submit feedback on a best-effort basis —
  send it asynchronously, treat a failure as non-fatal, and never block your agent on the
  response.
</Warning>

Feedback tells Tavily how useful its results actually were for your task. It is the signal
we use to improve ranking and result quality. Submitting feedback is free — it does not
consume [API credits](https://docs.tavily.com/documentation/api-credits).

## Zero Data Retention

If your account or organization has Zero Data Retention enabled, the free-text and URL content
you send here is not stored.


## OpenAPI

````yaml POST /feedback
openapi: 3.0.3
info:
  title: Tavily Search and Extract API
  description: >-
    Our REST API provides seamless access to Tavily Search, a powerful search
    engine for LLM agents, and Tavily Extract, an advanced web scraping solution
    optimized for LLMs.
  version: 1.0.0
servers:
  - url: https://api.tavily.com/
security: []
tags:
  - name: Search
  - name: Extract
  - name: Crawl
  - name: Map
  - name: Research
  - name: Feedback
  - name: Usage
  - name: Logs
paths:
  /feedback:
    post:
      summary: Submit feedback on a search request or session
      description: >-
        Submit feedback on how relevant and useful Tavily's results were for
        your task.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                request_id:
                  type: string
                  maxLength: 200
                  description: >-
                    The search request to give feedback on, as returned in the
                    `request_id` field of the search response. When provided,
                    the feedback applies to this request.
                  example: ${OBJECT_ID}
                session_id:
                  type: string
                  maxLength: 200
                  description: >-
                    The session to give feedback on — the value you sent in the
                    `X-Session-Id` header. When `request_id` is omitted, the
                    feedback applies to the whole session. Optional if
                    `request_id` is provided.
                  example: ${OBJECT_ID}
                agent_score:
                  oneOf:
                    - type: number
                    - type: string
                      maxLength: 64
                  description: >-
                    Overall score for how relevant and useful the results were
                    for your task.
                  example: 1
                human_score:
                  oneOf:
                    - type: number
                    - type: string
                      maxLength: 64
                  description: Feedback from your end user, if you collect it.
                  example: 1
                extra_scores:
                  type: array
                  maxItems: 50
                  description: Additional labeled scores for the dimensions you care about.
                  items:
                    type: object
                    required:
                      - label
                      - value
                    properties:
                      label:
                        type: string
                        maxLength: 64
                        description: Name of the dimension being scored.
                        example: freshness
                      value:
                        oneOf:
                          - type: number
                          - type: string
                            maxLength: 64
                        description: >-
                          A numeric score, or a short string label (max 64
                          characters).
                        example: 0.8
                  example:
                    - label: freshness
                      value: 0.4
                    - label: authority
                      value: 0.9
                comment:
                  type: string
                  maxLength: 10000
                  description: Free-text explanation of the feedback.
                  example: >-
                    Results were authoritative but several were more than a year
                    old.
                response_delivered:
                  type: string
                  maxLength: 50000
                  description: The final answer you produced using the results.
                  example: Lionel Messi is an Argentine footballer born in 1987...
                used_ids:
                  type: array
                  maxItems: 100
                  items:
                    type: string
                    maxLength: 200
                  description: >-
                    IDs of the results you actually used in your answer.
                    Alternative to `used_urls`.
                  example:
                    - a3f9c2-04
                    - a3f9c2-07
                used_urls:
                  type: array
                  maxItems: 100
                  items:
                    type: string
                    maxLength: 2000
                  description: >-
                    URLs of the results you actually used in your answer.
                    Alternative to `used_ids`.
                  example:
                    - https://www.britannica.com/facts/Lionel-Messi
                used_citations:
                  type: array
                  maxItems: 100
                  items:
                    type: string
                    maxLength: 2000
                  description: The specific content snippets you quoted from the results.
                  example:
                    - >-
                      Messi is known for his exceptional dribbling skills,
                      vision, and goal-scoring ability.
                urls_scores:
                  type: array
                  maxItems: 100
                  description: Per-result feedback. Identify each result by `id` or `url`.
                  items:
                    type: object
                    description: >-
                      Feedback on a single result. Each item must include `id`
                      or `url`.
                    properties:
                      id:
                        type: string
                        maxLength: 200
                        description: >-
                          The `id` of the result, as returned in the search
                          response.
                        example: a3f9c2-04
                      url:
                        type: string
                        maxLength: 2000
                        description: >-
                          The URL of the result. Use instead of `id` when you
                          don't have the result ID.
                        example: https://www.britannica.com/facts/Lionel-Messi
                      agent_score:
                        oneOf:
                          - type: number
                          - type: string
                            maxLength: 64
                        description: Score for this specific result.
                        example: 1
                      scores:
                        type: array
                        maxItems: 20
                        description: Additional labeled scores for this result.
                        items:
                          type: object
                          required:
                            - label
                            - value
                          properties:
                            label:
                              type: string
                              maxLength: 64
                              description: Name of the dimension being scored.
                              example: freshness
                            value:
                              oneOf:
                                - type: number
                                - type: string
                                  maxLength: 64
                              description: >-
                                A numeric score, or a short string label (max 64
                                characters).
                              example: 0.8
                      comment:
                        type: string
                        maxLength: 2000
                        description: Free-text explanation of the feedback on this result.
                  example:
                    - id: a3f9c2-04
                      agent_score: 1
                      comment: Directly answered the question.
                    - url: https://example.com/stale-page
                      agent_score: -1
                      scores:
                        - label: freshness
                          value: 0.1
      responses:
        '200':
          description: Feedback accepted
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Whether the feedback was accepted.
                    example: true
                  feedback_id:
                    type: string
                    description: Unique identifier of this feedback submission.
                    example: ${OBJECT_ID}
                  response_time:
                    type: number
                    description: Response time of this feedback request in seconds.
                    example: 0.05
              example:
                success: true
                feedback_id: ${OBJECT_ID}
                response_time: 0.05
        '400':
          description: >-
            Bad Request — neither `session_id` nor `request_id` was provided, or
            a `urls_scores` item is missing both `id` and `url`.
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: object
                    properties:
                      error:
                        type: string
              example:
                detail:
                  error: Either session_id or request_id is required.
        '401':
          description: Unauthorized - Your API key is wrong or missing.
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: object
                    properties:
                      error:
                        type: string
              example:
                detail:
                  error: 'Unauthorized: missing or invalid API key.'
        '413':
          description: Payload Too Large — the request body exceeds 256 KB.
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: object
                    properties:
                      error:
                        type: string
              example:
                detail:
                  error: Request body exceeds 262144 bytes.
        '422':
          description: >-
            Unprocessable Entity — a field failed validation (e.g. a list or
            string exceeds its maximum length).
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: object
                    properties:
                      error:
                        type: string
              example:
                detail:
                  error: Validation error in request body.
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: object
                    properties:
                      error:
                        type: string
              example:
                detail:
                  error: Error when processing feedback
      security:
        - bearerAuth: []
      x-codeSamples:
        - lang: python
          label: Python SDK
          source: |-
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="${API_KEY}")
            response = tavily_client.feedback(
                request_id="${OBJECT_ID}",
                agent_score=1,
                comment="The top results answered the question directly.",
                used_ids=["a3f9c2-04"],
            )

            print(response)
        - lang: javascript
          label: JavaScript SDK
          source: |-
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "${API_KEY}" });
            const response = await tvly.feedback({
              requestId: "${OBJECT_ID}",
              agentScore: 1,
              comment: "The top results answered the question directly.",
              usedIds: ["a3f9c2-04"],
            });

            console.log(response);
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header in the form Bearer <token>, where <token>
        is your Tavily API key (e.g., Bearer tvly-YOUR_API_KEY).

````
