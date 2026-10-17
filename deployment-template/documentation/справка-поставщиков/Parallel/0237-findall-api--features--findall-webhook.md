> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Parallel: findall-api--features--findall-webhook

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.parallel.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FindAll API Webhooks

> Receive real-time notifications on FindAll runs and candidates using webhooks

<div className="sr-only" aria-hidden="false">
  For AI agents: a documentation index is available at [https://docs.parallel.ai/llms.txt](https://docs.parallel.ai/llms.txt). The full text of all docs is at [https://docs.parallel.ai/llms-full.txt](https://docs.parallel.ai/llms-full.txt). You may also fetch any page as Markdown by appending `.md` to its URL or sending `Accept: text/markdown`.

  For Search and Extract, use `/v1/search` and `/v1/extract` for all new integrations and agent tool calls. Use `/v1beta/search` and `/v1beta/extract` only when maintaining an existing integration that already uses them. The request bodies changed too: on `/v1/extract`, `full_content`, `fetch_policy` and `excerpt_settings` go inside `advanced_settings`, and sending the v1beta top-level `excerpts`, `full_content` and `fetch_policy` to `/v1/extract` returns a 422. Do not substitute `/v1` for the documented FindAll or Ingest endpoint paths.
</div>

<Note>
  **Prerequisites:** Before implementing FindAll webhooks, read **Webhook Setup & Verification (локальный ресурс исходного примера не включён)** for critical information on:

  * Recording your webhook secret
  * Verifying HMAC signatures
  * Security best practices
  * Retry policies

  This guide focuses on FindAll-specific webhook events and payloads.
</Note>

## Overview

Webhooks allow you to receive real-time notifications when candidates are discovered, evaluated, or when your FindAll runs complete, eliminating the need for constant polling—especially useful for long-running FindAll operations that may process many candidates over time.

## Setup

To register a webhook for a FindAll run, include a `webhook` parameter in your FindAll run creation request:

<CodeGroup>
  ```bash cURL theme={"system"}
  curl --request POST \
    --url https://api.parallel.ai/v1beta/findall/runs \
    --header "Content-Type: application/json" \
    --header "x-api-key: $PARALLEL_API_KEY" \
    --data '{
      "objective": "Find all portfolio companies of Khosla Ventures",
      "entity_type": "companies",
      "match_conditions": [
        {
          "name": "khosla_ventures_portfolio_check",
          "description": "Company must be a portfolio company of Khosla Ventures."
        }
      ],
      "generator": "core",
      "match_limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhooks/findall",
        "event_types": [
          "findall.candidate.generated",
          "findall.candidate.matched",
          "findall.candidate.enriched",
          "findall.run.completed",
          "findall.run.cancelled",
          "findall.run.failed"
        ]
      }
    }
  ```

  ```python Python theme={"system"}
  import os
  import requests

  response = requests.post(
      "https://api.parallel.ai/v1beta/findall/runs",
      headers={"x-api-key": os.environ["PARALLEL_API_KEY"]},
      json={
          "objective": "Find all portfolio companies of Khosla Ventures",
          "entity_type": "companies",
          "match_conditions": [
              {
                  "name": "khosla_ventures_portfolio_check",
                  "description": "Company must be a portfolio company of Khosla Ventures."
              }
          ],
          "generator": "core",
          "match_limit": 100,
          "webhook": {
              "url": "https://your-domain.com/webhooks/findall",
              "event_types": [
                  "findall.candidate.generated",
                  "findall.candidate.matched",
                  "findall.candidate.enriched",
                  "findall.run.completed",
                  "findall.run.cancelled",
                  "findall.run.failed"
              ]
          }
      },
  )
  response.raise_for_status()
  findall_run = response.json()
  ```

  ```typescript TypeScript theme={"system"}
  const response = await fetch("https://api.parallel.ai/v1beta/findall/runs", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": ${API_KEY}!,
    },
    body: JSON.stringify({
      objective: "Find all portfolio companies of Khosla Ventures",
      entity_type: "companies",
      match_conditions: [
        {
          name: "khosla_ventures_portfolio_check",
          description: "Company must be a portfolio company of Khosla Ventures."
        }
      ],
      generator: "core",
      match_limit: 100,
      webhook: {
        url: "https://your-domain.com/webhooks/findall",
        event_types: [
          "findall.candidate.generated",
          "findall.candidate.matched",
          "findall.candidate.enriched",
          "findall.run.completed",
          "findall.run.cancelled",
          "findall.run.failed"
        ]
      }
    }),
  });

  if (!response.ok) {
    throw new Error(`FindAll request failed: ${response.status}`);
  }

  const run = await response.json();
  ```
</CodeGroup>

### Webhook Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `url` | string | Yes | Your HTTPS webhook endpoint URL. |
| `event_types` | array\[string] | Yes | Array of event types to subscribe to. See Event Types below. |

## Event Types

FindAll supports the following webhook event types:

| Event Type | Description |
| - | - |
| `findall.candidate.generated` | Emitted when a new candidate is generated and queued for evaluation |
| `findall.candidate.matched` | Emitted when a candidate successfully matches all match conditions |
| `findall.candidate.enriched` | Emitted when enrichment data has been extracted for a candidate |
| `findall.run.completed` | Emitted when a FindAll run reaches `completed` status |
| `findall.run.cancelled` | Emitted when a FindAll run is cancelled |
| `findall.run.failed` | Emitted when a FindAll run fails due to an error |

You can subscribe to any combination of these event types in your webhook configuration.

<Note>The webhook request schema also accepts `findall.candidate.unmatched` and `findall.candidate.cancelled` for compatibility, but current FindAll V1 processing does not emit either webhook event. Use SSE (локальный ресурс исходного примера не включён) to receive unmatched candidate updates.</Note>

<Note>
  For a complete guide to candidate object structure, states, and fields, see Candidates (локальный ресурс исходного примера не включён).
</Note>

## Webhook Payload Structure

Each webhook payload contains:

* `timestamp`: ISO 8601 timestamp of when the event occurred
* `type`: Event type
* `data`: Event-specific payload (FindAll Candidate or Run object)

### Candidate Events

<CodeGroup>
  ```json findall.candidate.generated theme={"system"}
  {
    "type": "findall.candidate.generated",
    "timestamp": "2025-10-27T14:56:05.619331Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "candidate_id": "candidate_2edf2301-f80d-46b9-b17a-7b4a9d577296",
      "name": "Anthropic",
      "url": "https://www.anthropic.com/",
      "description": "Anthropic is an AI safety and research company founded in 2021...",
      "match_status": "generated"
    }
  }
  ```

  ```json findall.candidate.matched theme={"system"}
  {
    "type": "findall.candidate.matched",
    "timestamp": "2025-10-27T14:57:15.421087Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "candidate_id": "candidate_478fb5ca-4581-4411-9acb-6b78b4cb5bcf",
      "name": "Vivodyne",
      "url": "https://vivodyne.com/",
      "description": "Vivodyne is a biotechnology company...",
      "match_status": "matched",
      "output": {
        "founded_after_2020_check": {
          "value": "2021",
          "type": "match_condition",
          "is_matched": true
        }
      },
      "basis": [
        {
          "field": "founded_after_2020_check",
          "citations": [
            {
              "title": "Vivodyne - Crunchbase Company Profile & Funding",
              "url": "https://www.crunchbase.com/organization/vivodyne",
              "excerpts": ["Founded in 2021"]
            }
          ],
          "reasoning": "Multiple sources indicate that Vivodyne was founded in 2021...",
          "confidence": "high"
        }
      ]
    }
  }
  ```
</CodeGroup>

### Run Events

<CodeGroup>
  ```json findall.run.completed theme={"system"}
  {
    "type": "findall.run.completed",
    "timestamp": "2025-10-27T14:58:39.421087Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "status": {
        "status": "completed",
        "is_active": false,
        "metrics": {
          "generated_candidates_count": 5,
          "matched_candidates_count": 1
        },
        "termination_reason": "match_limit_met"
      },
      "generator": "core",
      "metadata": {},
      "created_at": "2025-10-27T14:56:05.619331Z",
      "modified_at": "2025-10-27T14:58:39.421087Z"
    }
  }
  ```

  ```json findall.run.cancelled theme={"system"}
  {
    "type": "findall.run.cancelled",
    "timestamp": "2025-10-27T14:57:00.123456Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "status": {
        "status": "cancelled",
        "is_active": false,
        "metrics": {
          "generated_candidates_count": 3,
          "matched_candidates_count": 0
        },
        "termination_reason": "user_cancelled"
      },
      "generator": "core",
      "metadata": {},
      "created_at": "2025-10-27T14:56:05.619331Z",
      "modified_at": "2025-10-27T14:57:00.123456Z"
    }
  }
  ```

  ```json findall.run.failed theme={"system"}
  {
    "type": "findall.run.failed",
    "timestamp": "2025-10-27T14:57:30.789012Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "status": {
        "status": "failed",
        "is_active": false,
        "metrics": {
          "generated_candidates_count": 2,
          "matched_candidates_count": 0
        },
        "termination_reason": "error_occurred"
      },
      "generator": "core",
      "metadata": {},
      "created_at": "2025-10-27T14:56:05.619331Z",
      "modified_at": "2025-10-27T14:57:30.789012Z"
    }
  }
  ```
</CodeGroup>

## Security & Verification

For information on HMAC signature verification, including code examples in multiple languages, see the Webhook Setup Guide - Security & Verification (локальный ресурс исходного примера не включён) section.

## Retry Policy

See the Webhook Setup Guide - Retry Policy (локальный ресурс исходного примера не включён) for details on webhook delivery retry configuration.

## Best Practices

For webhook implementation best practices, including signature verification, handling duplicates, and async processing, see the Webhook Setup Guide - Best Practices (локальный ресурс исходного примера не включён) section.

## Related Topics

* **Preview (локальный ресурс исходного примера не включён)**: Test queries with 5–10 evaluated candidates before running full searches
* **Generators and Pricing (локальный ресурс исходного примера не включён)**: Understand generator options and pricing
* **Enrichments (локальный ресурс исходного примера не включён)**: Extract additional structured data for matched candidates
* **Extend Runs (локальный ресурс исходного примера не включён)**: Increase match limits without paying new fixed costs
* **Streaming Events (локальный ресурс исходного примера не включён)**: Receive real-time updates via Server-Sent Events
* **Run Lifecycle (локальный ресурс исходного примера не включён)**: Understand run statuses and how to cancel runs
* **API Reference (локальный ресурс исходного примера не включён)**: Complete endpoint documentation
