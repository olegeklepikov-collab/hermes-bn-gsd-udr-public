> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Dolt: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "general-work": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "general-work"
    },
    "required": [
      "question"
    ]
  },
  "software-change": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "software-change"
    },
    "required": [
      "question"
    ]
  },
  "runtime-setup": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "runtime-setup"
    },
    "required": [
      "question"
    ]
  },
  "document-work": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "document-work"
    },
    "required": [
      "question"
    ]
  },
  "exploratory-research": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "exploratory-research"
    },
    "required": [
      "question"
    ]
  },
  "systematic-review": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "systematic-review"
    },
    "required": [
      "question"
    ]
  },
  "business-research": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "business-research"
    },
    "required": [
      "question"
    ]
  },
  "dataset-audit": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "dataset-audit"
    },
    "required": [
      "question"
    ]
  },
  "research-replication": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "research-replication"
    },
    "required": [
      "question"
    ]
  },
  "research-handoff": {
    "server": "beads-dolt",
    "method": "workflow_create",
    "arguments": {
      "template": "research-handoff"
    },
    "required": [
      "question"
    ]
  },
  "tasks-ready": {
    "server": "beads",
    "method": "ready",
    "arguments": {}
  },
  "tasks-blocked": {
    "server": "beads",
    "method": "blocked",
    "arguments": {}
  },
  "tasks-stats": {
    "server": "beads",
    "method": "stats",
    "arguments": {}
  },
  "tasks-list": {
    "server": "beads",
    "method": "list",
    "arguments": {}
  },
  "sql-schema": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT table_name,column_name,data_type FROM information_schema.columns WHERE table_schema='knowledgework' ORDER BY table_name,ordinal_position"
    }
  },
  "sql-source-register": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT dataset_id,source_sha256,row_count,imported_at FROM research_sources ORDER BY imported_at DESC"
    }
  },
  "sql-dataset-counts": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT dataset_id,COUNT(*) AS records FROM research_records GROUP BY dataset_id"
    }
  },
  "sql-worktree-status": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT * FROM dolt_status"
    }
  },
  "sql-commit-history": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT commit_hash,committer,date,message FROM dolt_log LIMIT 20"
    }
  },
  "sql-branches": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT * FROM dolt_branches"
    }
  },
  "sql-table-history": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT * FROM dolt_history_research_sources LIMIT 50"
    }
  },
  "sql-source-hash-check": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT dataset_id,CHAR_LENGTH(source_sha256) AS hash_length,row_count FROM research_sources"
    }
  },
  "sql-asreview-label-counts": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT JSON_UNQUOTE(JSON_EXTRACT(payload,'$.included')) AS imported_label,COUNT(*) AS records FROM research_records GROUP BY imported_label"
    }
  },
  "sql-task-data-version": {
    "server": "dolt",
    "method": "query",
    "arguments": {
      "working_database": "${WORKING_DATABASE}",
      "working_branch": "main",
      "query": "SELECT DOLT_HASHOF('HEAD') AS version,ACTIVE_BRANCH() AS branch,DATABASE() AS database_name"
    }
  },
  "memory_list": {
    "server": "beads-dolt",
    "method": "memory_list",
    "arguments": {}
  },
  "beads_prime": {
    "server": "beads-dolt",
    "method": "beads_prime",
    "arguments": {}
  },
  "beads_export": {
    "server": "beads-dolt",
    "method": "beads_export",
    "arguments": {}
  },
  "beads_backup": {
    "server": "beads-dolt",
    "method": "beads_backup",
    "arguments": {}
  },
  "dolt_backup": {
    "server": "beads-dolt",
    "method": "dolt_backup",
    "arguments": {}
  },
  "merge_preview": {
    "server": "beads-dolt",
    "method": "merge_preview",
    "arguments": {},
    "required": [
      "source_branch",
      "target_branch"
    ]
  },
  "merge_resolve": {
    "server": "beads-dolt",
    "method": "merge_resolve",
    "arguments": {},
    "required": [
      "source_branch",
      "target_branch",
      "resolutions",
      "message"
    ]
  }
}
```
