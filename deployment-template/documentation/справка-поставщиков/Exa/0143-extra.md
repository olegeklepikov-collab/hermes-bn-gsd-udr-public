> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Exa: extra

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Get Team Info
URL: https://exa.ai/docs/websets/api/teams/get-team-info.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Team Info

> Retrieve information about your team including concurrency usage and limits.

## Overview

The Get Team Info endpoint returns information about the authenticated team, including the team's current concurrency usage and configured limits. This is useful for monitoring your Websets API usage and understanding your rate limits.

## Response

The response includes:

- object: Always "team"
- id: Your team's unique identifier
- name: Your team's name
- concurrency: Current usage showing active and queued requests
- limits: Your team's concurrency limits

### Concurrency Fields

The `concurrency` object shows your current request state:

- active: Number of requests currently being processed
- queued: Number of requests waiting to be processed

### Limits Fields

The `limits` object shows your team's configured limits:

- maxConcurrent: Maximum number of requests that can be processed simultaneously (null means unlimited)
- maxQueued: Maximum number of requests that can wait in the queue (null means unlimited)

## OpenAPI

```yaml get /v0/teams/me
openapi: 3.1.0
info:
  title: Exa Public API
  version: 2.0.0
servers:
  - url: https://api.exa.ai
security:
  - apiKey: []
  - bearer: []
tags: []
paths:
  /v0/teams/me:
    get:
      tags:
        - Teams
      summary: Get Team Info
      description: >-
        Returns information about the authenticated team, including current
        concurrency usage and limits.
      operationId: teams-me-get
      responses:
        '200':
          description: Team information retrieved successfully
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WebsetsTeamInfo'
components:
  headers:
    XRequestId:
      description: >-
        Unique identifier for the request. Matches the `requestId` field
        returned in response bodies that carry one.
      schema:
        type: string
      example: 07e29bb1f4f1dd05f0d4b57bbcf6e4b8
  schemas:
    WebsetsTeamInfo:
      type: object
      properties:
        object:
          type: string
          const: team
          description: The object type, always `"team"`.
        id:
          type: string
          description: Unique identifier for the team.
        name:
          type: string
          description: Name of the team.
        concurrency:
          type: object
          properties:
            active:
              type: integer
              description: Number of requests currently being processed.
            queued:
              type: integer
              description: Number of requests currently queued.
          required:
            - active
            - queued
          additionalProperties: false
          description: Current concurrency usage.
        limits:
          type: object
          properties:
            maxConcurrent:
              anyOf:
                - type: integer
                - type: 'null'
              description: >-
                Maximum number of concurrent requests allowed. Null means
                unlimited.
            maxQueued:
              anyOf:
                - type: integer
                - type: 'null'
              description: Maximum number of queued requests allowed. Null means unlimited.
          required:
            - maxConcurrent
            - maxQueued
          additionalProperties: false
          description: Concurrency limits for the team.
      required:
        - object
        - id
        - name
        - concurrency
        - limits
      additionalProperties: false
  securitySchemes:
    apiKey:
      type: apiKey
      name: x-api-key
      in: header
      description: >-
        Pass your Exa API key in the x-api-key header. You can also authenticate
        with Authorization: Bearer <key>.
    bearer:
      type: http
      scheme: bearer
      description: >-
        Pass your Exa API key in the x-api-key header. You can also authenticate
        with Authorization: Bearer <key>.

```

# Batch API
URL: https://exa.ai/docs/batch/quickstart.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Batch API

> Run Exa API requests asynchronously in batches.

The Batch API is available for Enterprise customers after Exa enables it for your team. Contact sales@exa.ai to discuss Enterprise access and enablement.

The Batch API lets you submit many Exa API requests at once and retrieve their results later as a JSONL file. Instead of sending thousands of individual requests and managing rate limits and retries yourself, you send a single batch, poll its status, and download all the results in one file.

Use it for offline enrichment, backfills, or any other job that does not need an immediate response. Full request and response schemas are in the API reference.

The Batch API is in beta. Include the `Exa-Beta: batches-2026-06-06` header on every request.

## Supported requests

Each batch item must be a `POST` request to one of these routes:

| Route | Use case |
| --- | --- |
| `/search` | Run Exa search requests asynchronously |
| `/agent/runs` | Run Exa Agent requests asynchronously |

Each item needs a batch-unique `customId`. The same `customId` is returned in the results file so you can map output rows back to your input data.

## Create a batch

```bash
curl -s -X POST "https://api.exa.ai/batches" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Exa-Beta: batches-2026-06-06" \
  -H "Content-Type: application/json" \
  -d '{
    "requests": [
      {
        "customId": "row-1",
        "method": "POST",
        "url": "/search",
        "body": {
          "query": "Latest AI infrastructure funding rounds"
        }
      },
      {
        "customId": "row-2",
        "method": "POST",
        "url": "/agent/runs",
        "body": {
          "query": "Summarize recent vector database launches"
        }
      }
    ],
    "metadata": {
      "project": "weekly-digest"
    }
  }'

```

The response contains the batch ID and initial status:

## Example response

```json
{
  "id": "batch_01j7x9v0m2n4p6q8r0s2t4v6w8",
  "object": "batch",
  "status": "in_progress",
  "requestCounts": {
    "total": 2,
    "completed": 0,
    "failed": 0
  },
  "createdAt": "2026-06-06T12:00:00.000Z",
  "expiresAt": null,
  "endedAt": null,
  "resultsUrl": null,
  "metadata": {
    "project": "weekly-digest"
  }
}

```

## Check status

Poll the batch until it reaches a terminal status:

```bash
curl -s "https://api.exa.ai/batches/batch_01j7x9v0m2n4p6q8r0s2t4v6w8" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Exa-Beta: batches-2026-06-06"

```

Batch statuses are:

| Status | Meaning |
| --- | --- |
| `in_progress` | The batch is running |
| `completed` | All requests have finished and results are available |
| `cancelling` | Cancellation was requested and in-flight work is draining |
| `cancelled` | The batch was cancelled |
| `expired` | Results are no longer available |

When the batch completes, `resultsUrl` contains a download URL for the JSONL results file, and `expiresAt` is set to the end of the results retention window.

`resultsUrl` is a short-lived presigned URL. Re-fetch the batch to get a fresh URL whenever you need to download results again.

## List batches

```bash
curl -s "https://api.exa.ai/batches?limit=100" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Exa-Beta: batches-2026-06-06"

```

The response is cursor-paginated: `data` holds up to `limit` batches, and when `hasMore` is `true`, pass `nextCursor` as the `cursor` query parameter to fetch the next page.

Pass `status=completed` to list only completed batches:

```bash
curl -s "https://api.exa.ai/batches?status=completed" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Exa-Beta: batches-2026-06-06"

```

`completed` is the only supported value; any other value returns an error. Completed listings are ordered by expiry and use their own cursor, so keep sending `status=completed` on every page — completed and unfiltered cursors are not interchangeable.

```json
{
  "object": "list",
  "data": [],
  "hasMore": false,
  "nextCursor": null
}

```

## Download results

```bash
curl "$RESULTS_URL" -o results.jsonl

```

Each JSONL line contains the original `customId` and either a `response` or an `error`:

```json
{ "customId": "row-1", "response": { "statusCode": 200, "body": { "results": [] } } }
{ "customId": "row-2", "error": { "code": "API_ERROR", "message": "request failed" } }

```

## Cancel a batch

```bash
curl -X POST "https://api.exa.ai/batches/batch_01j7x9v0m2n4p6q8r0s2t4v6w8/cancel" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Exa-Beta: batches-2026-06-06"

```

## Delete a batch

```bash
curl -X DELETE "https://api.exa.ai/batches/batch_01j7x9v0m2n4p6q8r0s2t4v6w8" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Exa-Beta: batches-2026-06-06"

```

## Access

To enable the Batch API for a team, contact sales@exa.ai.

# Zero Data Retention
URL: https://exa.ai/docs/admin/security/zero-data-retention.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## Agent Instructions
> 
> The Exa API is served at https://api.exa.ai. Authenticate with `Authorization: Bearer $EXA_API_KEY` (or `x-api-key: $EXA_API_KEY`); create keys at https://dashboard.exa.ai/api-keys.
> Prefer the official SDKs, `exa-py` (`pip install exa-py`) and `exa-js` (`npm install exa-js`); both read `EXA_API_KEY` from the environment.
> Tool-using agents can call Exa without writing code through the hosted MCP server at https://mcp.exa.ai/mcp, or install the Exa agent skill with `npx skills add exa-labs/agent-skills` (skill file: https://exa.ai/docs/skill.md).
> The OpenAPI specs at https://exa.ai/docs/exa-spec.yaml and https://exa.ai/docs/team-management-spec.yaml are the source of truth for request and response schemas.

# Zero Data Retention

> Zero Data Retention availability across Exa products.

Zero Data Retention (ZDR) is available on Enterprise plans and enabled per team. Contact sales@exa.ai for details.

| Product | ZDR availability |
| --- | --- |
| Search | Available |
| Contents | Available |
| Agent | Available |
| Answer | Not currently supported |
| Websets | Not currently supported |

# List run events
URL: https://exa.ai/docs/reference/agent-api/list-run-events.md

> ## Documentation Index
> 
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List run events

> List stored Agent run events or replay them as server-sent events.

By default, this endpoint returns a paginated JSON list of stored events. Set `Accept: text/event-stream` to replay stored events as SSE. For JSON pagination, use `cursor`. For SSE replay, use `Last-Event-ID`.

## Get your Exa API key

## OpenAPI

```yaml
openapi: 3.1.0
info:
  title: Exa Public API
  version: 2.0.0
servers:
  - url: https://api.exa.ai
security:
  - apiKey: []
  - bearer: []
tags: []
paths:
  /agent/runs/{id}/events:
    get:
      tags:
        - Agent
      summary: List run events
      description: >-
        List stored events for an Agent run. Set `Accept: text/event-stream` to
        replay stored events as server-sent events. Use `cursor` for JSON
        pagination or `Last-Event-ID` for SSE replay.
      operationId: listAgentRunEvents
      parameters:
        - in: path
          name: id
          schema:
            $ref: '#/components/schemas/AgentRunId'
            description: Agent run ID.
          required: true
          description: Agent run ID.
        - in: query
          name: limit
          schema:
            type: integer
            minimum: 1
            maximum: 100
            description: Number of results per page
            default: 20
        - in: query
          name: cursor
          schema:
            type: string
            description: >-
              Cursor for pagination. Use the `nextCursor` value from the
              previous event list response.
        - $ref: '#/components/parameters/AcceptHeader'
        - $ref: '#/components/parameters/LastEventId'
      responses:
        '200':
          description: Agent run events
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentRunEventList'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/AgentRunEvent'
              examples:
                replay:
                  summary: Replayed run events
                  value: >
                    id: 2

                    event: agent_run.started

                    data: {"id":"agent_run_01j...","status":"running"}

                    id: 3

                    event: agent_run.completed

                    data:
                    {"id":"agent_run_01j...","object":"agent_run","status":"completed"}
        '400':
          description: Invalid request.
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentErrorResponse'
        '401':
          description: Team context or authentication was not found.
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentErrorResponse'
        '404':
          description: Run not found.
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentErrorResponse'
        '429':
          description: Agent run concurrency limit reached.
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentErrorResponse'
        '500':
          description: Server error or run timeout.
          headers:
            x-request-id:
              $ref: '#/components/headers/XRequestId'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentErrorResponse'
components:
  schemas:
    AgentRunId:
      type: string
      minLength: 1
      maxLength: 200
      pattern: ^[A-Za-z0-9_.:-]+$
      description: Agent run ID. New run IDs are returned with the `agent_run_` prefix.
      example: agent_run_01j7x9v0m2n4p6q8r0s2t4v6w8
    AgentRunEventList:
      type: object
      properties:
        object:
          type: string
          const: list
        data:
          type: array
          items:
            $ref: '#/components/schemas/AgentRunEvent'
        hasMore:
          type: boolean
          description: Whether there are more results
        nextCursor:
          anyOf:
            - type: string
            - type: 'null'
      required:
        - object
        - data
        - hasMore
        - nextCursor
      additionalProperties: false
    AgentRunEvent:
      type: object
      properties:
        id:
          type: string
          description: Event ID within the run.
        event:
          type: string
          enum:
            - agent_run.created
            - agent_run.started
            - agent_run.completed
            - agent_run.failed
            - agent_run.cancelled
        data:
          $ref: '#/components/schemas/JsonValue'
        createdAt:
          type: string
          format: date-time
          description: When the event was created
      required:
        - id
        - event
        - data
        - createdAt
      additionalProperties: false
    AgentErrorResponse:
      type: object
      properties:
        error:
          $ref: '#/components/schemas/AgentError'
      required:
        - error
      additionalProperties: false
    JsonValue:
      description: Any JSON value.
      oneOf:
        - type: 'null'
        - type: boolean
        - type: number
        - type: string
        - type: array
          items:
            $ref: '#/components/schemas/JsonValue'
        - type: object
          propertyNames:
            type: string
          additionalProperties:
            $ref: '#/components/schemas/JsonValue'
    AgentError:
      type: object
      properties:
        type:
          type: string
          enum:
##             - INVALID_REQUEST
##             - AUTHENTICATION_ERROR
##             - RATE_LIMIT_ERROR
##             - NOT_FOUND
##             - SERVER_ERROR
        code:
          type: string
          enum:
##             - INVALID_REQUEST
##             - TEAM_NOT_FOUND
##             - RUN_NOT_FOUND
##             - PREVIOUS_RUN_NOT_FOUND
##             - PREVIOUS_RUN_NOT_COMPLETED
##             - CONCURRENCY_LIMIT_REACHED
##             - INVALID_OUTPUT_SCHEMA
##             - INVALID_DATA_SOURCE
##             - TIMEOUT
##             - SERVER_ERROR
        message:
          type: string
      required:
        - type
        - code
        - message
      additionalProperties:
        $ref: '#/components/schemas/JsonValue'
  parameters:
    AcceptHeader:
      in: header
      name: Accept
      schema:
        description: Set to `text/event-stream` to receive server-sent events.
        type: string
        enum:
          - application/json
          - text/event-stream
      description: Set to `text/event-stream` to receive server-sent events.
    LastEventId:
      in: header
      name: Last-Event-ID
      schema:
        description: For SSE replay, return only events after this event ID.
        type: string
      description: For SSE replay, return only events after this event ID.
  headers:
    XRequestId:
      description: >-
        Unique identifier for the request. Matches the `requestId` field
        returned in response bodies that carry one.
      schema:
        type: string
      example: 07e29bb1f4f1dd05f0d4b57bbcf6e4b8
  securitySchemes:
    apiKey:
      type: apiKey
      name: x-api-key
      in: header
      description: >-
        Pass your Exa API key in the x-api-key header. You can also authenticate
        with Authorization: Bearer <key>.
    bearer:
      type: http
      scheme: bearer
      description: >-
        Pass your Exa API key in the x-api-key header. You can also authenticate
        with Authorization: Bearer <key>.

```
