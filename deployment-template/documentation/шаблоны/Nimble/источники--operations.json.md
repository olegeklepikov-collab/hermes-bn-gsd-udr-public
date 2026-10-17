> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Nimble: operations.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "POST /v1/realtime/serp": {
    "operationId": null,
    "body": {
      "allOf": [
        {
          "$ref": "#/components/schemas/FastSerpPayload"
        }
      ],
      "examples": [
        {
          "search_engine": "google_search",
          "query": "NBA Allstar 2026",
          "country": "US",
          "locale": "en"
        }
      ]
    },
    "params": []
  },
  "POST /v2/extract/templates/run": {
    "operationId": "runExtractTemplate",
    "body": {
      "$ref": "#/components/schemas/ExtractionTemplateBody"
    },
    "params": []
  },
  "POST /v2/extract/templates/async": {
    "operationId": "runExtractTemplateAsync",
    "body": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ExtractionTemplateBody"
        },
        {
          "properties": {
            "callback_url": {
              "description": "URL to call back when async operation completes",
              "examples": [
                "https://example.com/webhook/callback"
              ],
              "type": "string"
            },
            "storage_compress": {
              "description": "Whether to compress stored data",
              "examples": [
                true
              ],
              "type": "boolean"
            },
            "storage_object_name": {
              "description": "Custom name for the stored object",
              "examples": [
                "result-2024-01-15.json"
              ],
              "type": "string"
            },
            "storage_type": {
              "description": "Type of storage to use for results",
              "examples": [
                "s3"
              ],
              "type": "string"
            },
            "storage_url": {
              "description": "URL for storage location",
              "examples": [
                "s3://bucket-name/path/to/object"
              ],
              "type": "string"
            }
          },
          "type": "object"
        }
      ]
    },
    "params": []
  },
  "POST /v2/extract/templates/batch": {
    "operationId": "runExtractTemplateBatch",
    "body": {
      "$ref": "#/components/schemas/ExtractionTemplateBatchBody"
    },
    "params": []
  },
  "GET /v2/extract/templates": {
    "operationId": "listExtractTemplates",
    "body": null,
    "params": [
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "DELETE /v2/extract/templates/{extract_template_name}": {
    "operationId": "deleteExtractTemplate",
    "body": null,
    "params": [
      {
        "name": "extract_template_name",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Extract Template Name",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/extract/templates/{extract_template_name}": {
    "operationId": "getExtractTemplate",
    "body": null,
    "params": [
      {
        "name": "extract_template_name",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Extract Template Name",
          "type": "string"
        }
      }
    ]
  },
  "PATCH /v2/extract/templates/{extract_template_name}": {
    "operationId": "updateExtractTemplate",
    "body": {
      "$ref": "#/components/schemas/JsonPatchDocument"
    },
    "params": [
      {
        "name": "extract_template_name",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Extract Template Name",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/extract/templates/{extract_template_name}/versions": {
    "operationId": "listExtractTemplateVersions",
    "body": null,
    "params": [
      {
        "name": "extract_template_name",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Extract Template Name",
          "type": "string"
        }
      },
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "GET /v2/extract/templates/{extract_template_name}/versions/{version_id}": {
    "operationId": "getExtractTemplateVersion",
    "body": null,
    "params": [
      {
        "name": "extract_template_name",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Extract Template Name",
          "type": "string"
        }
      },
      {
        "name": "version_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Version Id",
          "type": "string"
        }
      }
    ]
  },
  "POST /v2/extract/templates/generations": {
    "operationId": "generateExtractTemplate",
    "body": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/CreateExtractTemplateGenerationRequestPublicV2"
        },
        {
          "$ref": "#/components/schemas/CreateExtractTemplateRefinementRequestPublicV2"
        }
      ],
      "title": "Request"
    },
    "params": []
  },
  "GET /v2/extract/templates/generations/{generation_id}": {
    "operationId": "getExtractTemplateGeneration",
    "body": null,
    "params": [
      {
        "name": "generation_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Generation Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/tasks": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "cursor",
        "in": "query",
        "required": false,
        "schema": {
          "description": "Cursor for pagination. Use the next_cursor from the previous response.",
          "format": "uuid",
          "type": "string"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "description": "Number of tasks to return per page.",
          "examples": [
            10
          ],
          "maximum": 9007199254740991,
          "minimum": 1,
          "type": "integer"
        }
      }
    ]
  },
  "GET /v2/tasks/{task_id}": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "task_id",
        "in": "path",
        "required": true,
        "schema": {
          "description": "The unique identifier of the task.",
          "examples": [
            "${OBJECT_ID}"
          ],
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/tasks/{task_id}/results": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "task_id",
        "in": "path",
        "required": true,
        "schema": {
          "description": "The unique identifier of the task.",
          "examples": [
            "${OBJECT_ID}"
          ],
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/batches": {
    "operationId": null,
    "body": null,
    "params": []
  },
  "GET /v2/batches/{batch_id}": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "batch_id",
        "in": "path",
        "required": true,
        "schema": {
          "description": "The unique identifier of the batch.",
          "examples": [
            "${OBJECT_ID}"
          ],
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/batches/{batch_id}/progress": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "batch_id",
        "in": "path",
        "required": true,
        "schema": {
          "description": "The unique identifier of the batch.",
          "examples": [
            "${OBJECT_ID}"
          ],
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/agents": {
    "operationId": "list_agents_public_v2_api_v2_public_web_search_agents_get",
    "body": null,
    "params": [
      {
        "name": "workspace_id",
        "in": "query",
        "required": false,
        "schema": {
          "anyOf": [
            {
              "format": "uuid",
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Workspace Id"
        }
      },
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "POST /v2/agents": {
    "operationId": "create_agent_public_v2_api_v2_public_web_search_agents_post",
    "body": {
      "$ref": "#/components/schemas/WebSearchAgentCreateRequestPublicV2"
    },
    "params": []
  },
  "POST /v2/agents/runs": {
    "operationId": "create_run_with_generated_agent_public_v2_api_v2_public_web_search_agents_runs_post",
    "body": {
      "$ref": "#/components/schemas/WebSearchAgentRunCreateRequestPublicV2"
    },
    "params": []
  },
  "GET /v2/agents/templates": {
    "operationId": "list_templates_public_v2_api_v2_public_web_search_agents_templates_get",
    "body": null,
    "params": [
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "GET /v2/agents/templates/{template_name}": {
    "operationId": "get_template_public_v2_api_v2_public_web_search_agents_templates__template_name__get",
    "body": null,
    "params": [
      {
        "name": "template_name",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Template Name",
          "type": "string"
        }
      }
    ]
  },
  "DELETE /v2/agents/{agent_id}": {
    "operationId": "deactivate_agent_public_v2_api_v2_public_web_search_agents__agent_id__delete",
    "body": null,
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/agents/{agent_id}": {
    "operationId": "get_agent_public_v2_api_v2_public_web_search_agents__agent_id__get",
    "body": null,
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      }
    ]
  },
  "PATCH /v2/agents/{agent_id}": {
    "operationId": "update_agent_public_v2_api_v2_public_web_search_agents__agent_id__patch",
    "body": {
      "$ref": "#/components/schemas/JsonPatchDocument"
    },
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/agents/{agent_id}/runs": {
    "operationId": "list_runs_public_v2_api_v2_public_web_search_agents__agent_id__runs_get",
    "body": null,
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      },
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "POST /v2/agents/{agent_id}/runs": {
    "operationId": "create_run_public_v2_api_v2_public_web_search_agents__agent_id__runs_post",
    "body": {
      "$ref": "#/components/schemas/WebSearchAgentRunCreateRequestPublicV2"
    },
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/agents/{agent_id}/runs/{run_id}": {
    "operationId": "get_run_public_v2_api_v2_public_web_search_agents__agent_id__runs__run_id__get",
    "body": null,
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      },
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/agents/{agent_id}/runs/{run_id}/events": {
    "operationId": "stream_run_events_public_v2_api_v2_public_web_search_agents__agent_id__runs__run_id__events_get",
    "body": null,
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      },
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/agents/{agent_id}/runs/{run_id}/result": {
    "operationId": "get_run_result_public_v2_api_v2_public_web_search_agents__agent_id__runs__run_id__result_get",
    "body": null,
    "params": [
      {
        "name": "agent_id",
        "in": "path",
        "required": true,
        "schema": {
          "format": "uuid",
          "title": "Agent Id",
          "type": "string"
        }
      },
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/jobs": {
    "operationId": "list_jobs_public_v2_api_v2_public_jobs_get",
    "body": null,
    "params": [
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "POST /v2/jobs": {
    "operationId": "create_job_public_v2_api_v2_public_jobs_post",
    "body": {
      "$ref": "#/components/schemas/CreateJobRequestPublicV2"
    },
    "params": []
  },
  "GET /v2/jobs/runs/{run_id}": {
    "operationId": "get_run_public_v2_api_v2_public_jobs_runs__run_id__get",
    "body": null,
    "params": [
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/jobs/runs/{run_id}/artifacts": {
    "operationId": "list_run_artifacts_public_v2_api_v2_public_jobs_runs__run_id__artifacts_get",
    "body": null,
    "params": [
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/jobs/runs/{run_id}/artifacts/{artifact_id}": {
    "operationId": "get_run_artifact_public_v2_api_v2_public_jobs_runs__run_id__artifacts__artifact_id__get",
    "body": null,
    "params": [
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      },
      {
        "name": "artifact_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Artifact Id",
          "type": "integer"
        }
      }
    ]
  },
  "GET /v2/jobs/runs/{run_id}/artifacts/{artifact_id}/download-url": {
    "operationId": "get_run_artifact_download_url_public_v2_api_v2_public_jobs_runs__run_id__artifacts__artifact_id__download_url_get",
    "body": null,
    "params": [
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      },
      {
        "name": "artifact_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Artifact Id",
          "type": "integer"
        }
      }
    ]
  },
  "GET /v2/jobs/runs/{run_id}/artifacts/{artifact_id}/preview": {
    "operationId": "preview_run_artifact_public_v2_api_v2_public_jobs_runs__run_id__artifacts__artifact_id__preview_get",
    "body": null,
    "params": [
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      },
      {
        "name": "artifact_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Artifact Id",
          "type": "integer"
        }
      }
    ]
  },
  "POST /v2/jobs/runs/{run_id}/cancel": {
    "operationId": "cancel_run_public_v2_api_v2_public_jobs_runs__run_id__cancel_post",
    "body": null,
    "params": [
      {
        "name": "run_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Run Id",
          "type": "string"
        }
      }
    ]
  },
  "DELETE /v2/jobs/{job_id}": {
    "operationId": "delete_job_public_v2_api_v2_public_jobs__job_id__delete",
    "body": null,
    "params": [
      {
        "name": "job_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Job Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/jobs/{job_id}": {
    "operationId": "get_job_public_v2_api_v2_public_jobs__job_id__get",
    "body": null,
    "params": [
      {
        "name": "job_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Job Id",
          "type": "string"
        }
      }
    ]
  },
  "PATCH /v2/jobs/{job_id}": {
    "operationId": "update_job_public_v2_api_v2_public_jobs__job_id__patch",
    "body": {
      "$ref": "#/components/schemas/UpdateJobRequestPublicV2"
    },
    "params": [
      {
        "name": "job_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Job Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/jobs/{job_id}/runs": {
    "operationId": "list_job_runs_public_v2_api_v2_public_jobs__job_id__runs_get",
    "body": null,
    "params": [
      {
        "name": "job_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Job Id",
          "type": "string"
        }
      },
      {
        "name": "offset",
        "in": "query",
        "required": false,
        "schema": {
          "default": 0,
          "minimum": 0,
          "title": "Offset",
          "type": "integer"
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "maximum": 200,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        }
      }
    ]
  },
  "POST /v2/jobs/{job_id}/runs": {
    "operationId": "trigger_job_run_public_v2_api_v2_public_jobs__job_id__runs_post",
    "body": null,
    "params": [
      {
        "name": "job_id",
        "in": "path",
        "required": true,
        "schema": {
          "title": "Job Id",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/crawl": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "status",
        "in": "query",
        "required": false,
        "schema": {
          "default": "all",
          "description": "Filter crawls by their status.",
          "enum": [
            "queued",
            "running",
            "succeeded",
            "failed",
            "canceled",
            "all"
          ],
          "examples": [
            "queued"
          ],
          "type": "string"
        }
      },
      {
        "name": "cursor",
        "in": "query",
        "required": false,
        "schema": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Cursor for pagination."
        }
      },
      {
        "name": "limit",
        "in": "query",
        "required": false,
        "schema": {
          "default": 100,
          "description": "Number of crawls to return per page.",
          "examples": [
            10
          ],
          "maximum": 9007199254740991,
          "minimum": 1,
          "type": "integer"
        }
      }
    ]
  },
  "POST /v2/crawl": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/CrawlPayload"
    },
    "params": []
  },
  "DELETE /v2/crawl/{id}": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "id",
        "in": "path",
        "required": true,
        "schema": {
          "description": "The unique identifier of the crawl task.",
          "examples": [
            "${OBJECT_ID}"
          ],
          "format": "uuid",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/crawl/{id}": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "id",
        "in": "path",
        "required": true,
        "schema": {
          "description": "The unique identifier of the crawl task.",
          "examples": [
            "${OBJECT_ID}"
          ],
          "format": "uuid",
          "type": "string"
        }
      }
    ]
  },
  "GET /v2/domain-knowledge/driver": {
    "operationId": null,
    "body": null,
    "params": [
      {
        "name": "url",
        "in": "query",
        "required": false,
        "schema": {
          "description": "Target domain to resolve driver for (e.g. amazon.com).",
          "examples": [
            "amazon.com"
          ],
          "type": "string"
        }
      },
      {
        "name": "agent",
        "in": "query",
        "required": false,
        "schema": {
          "description": "Agent name to resolve driver for (e.g. nimble-ecommerce).",
          "examples": [
            "nimble-ecommerce"
          ],
          "type": "string"
        }
      }
    ]
  },
  "POST /v2/extract": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/ExtractPayload"
    },
    "params": []
  },
  "POST /v2/extract/async": {
    "operationId": null,
    "body": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ExtractPayload"
        },
        {
          "properties": {
            "callback_url": {
              "description": "URL to call back when async operation completes",
              "examples": [
                "https://example.com/webhook/callback"
              ],
              "type": "string"
            },
            "storage_compress": {
              "description": "Whether to compress stored data",
              "examples": [
                true
              ],
              "type": "boolean"
            },
            "storage_object_name": {
              "description": "Custom name for the stored object",
              "examples": [
                "result-2024-01-15.json"
              ],
              "type": "string"
            },
            "storage_type": {
              "description": "Type of storage to use for results",
              "examples": [
                "s3"
              ],
              "type": "string"
            },
            "storage_url": {
              "description": "URL for storage location",
              "examples": [
                "s3://bucket-name/path/to/object"
              ],
              "type": "string"
            }
          },
          "type": "object"
        }
      ]
    },
    "params": []
  },
  "POST /v2/extract/batch": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/ExtractBatchPayload"
    },
    "params": []
  },
  "POST /v2/map": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/MapPayload"
    },
    "params": []
  },
  "POST /v2/media": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/MediaPayload"
    },
    "params": []
  },
  "POST /v2/media/async": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/MediaAsyncPayload"
    },
    "params": []
  },
  "POST /v2/search": {
    "operationId": "search_search_post",
    "body": {
      "$ref": "#/components/schemas/SearchRequest"
    },
    "params": []
  },
  "POST /v2/serp": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/SerpPayload"
    },
    "params": []
  },
  "POST /v2/serp/async": {
    "operationId": null,
    "body": {
      "allOf": [
        {
          "$ref": "#/components/schemas/SerpPayload"
        },
        {
          "properties": {
            "callback_url": {
              "description": "URL to call back when async operation completes",
              "examples": [
                "https://example.com/webhook/callback"
              ],
              "type": "string"
            },
            "storage_compress": {
              "description": "Whether to compress stored data",
              "examples": [
                true
              ],
              "type": "boolean"
            },
            "storage_object_name": {
              "description": "Custom name for the stored object",
              "examples": [
                "result-2024-01-15.json"
              ],
              "type": "string"
            },
            "storage_type": {
              "description": "Type of storage to use for results",
              "examples": [
                "s3"
              ],
              "type": "string"
            },
            "storage_url": {
              "description": "URL for storage location",
              "examples": [
                "s3://bucket-name/path/to/object"
              ],
              "type": "string"
            }
          },
          "type": "object"
        }
      ]
    },
    "params": []
  },
  "POST /v2/serp/batch": {
    "operationId": null,
    "body": {
      "$ref": "#/components/schemas/SerpBatchPayload"
    },
    "params": []
  },
  "POST /v1/domain-health/check": {
    "operationId": "check_domain_health",
    "body": {
      "$ref": "#/components/schemas/DomainHealthCheckPayload"
    },
    "params": []
  }
}
```
