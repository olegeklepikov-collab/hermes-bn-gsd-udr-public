> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Pendar: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "verify-reference": {
    "name": "verify_paper",
    "arguments": {}
  },
  "audit-draft": {
    "name": "audit_bibliography",
    "arguments": {
      "context": "draft"
    }
  },
  "audit-published": {
    "name": "audit_bibliography",
    "arguments": {
      "context": "published"
    }
  },
  "field-overview": {
    "name": "survey_literature",
    "arguments": {
      "papers": 5
    }
  },
  "field-counts": {
    "name": "survey_literature",
    "arguments": {
      "papers": 0
    }
  },
  "field-period": {
    "name": "survey_literature",
    "arguments": {
      "papers": 5
    },
    "required_inputs": [
      "year_from",
      "year_to"
    ]
  },
  "field-reading-list": {
    "name": "survey_literature",
    "arguments": {
      "papers": 25
    }
  },
  "network-both": {
    "name": "graph_hopper",
    "arguments": {
      "direction": "both",
      "analyze_citers": 50,
      "papers_per_direction": 5,
      "include_graph": false
    }
  },
  "impact-forward": {
    "name": "graph_hopper",
    "arguments": {
      "direction": "forward",
      "analyze_citers": 50,
      "papers_per_direction": 5,
      "include_graph": false
    }
  },
  "foundations-backward": {
    "name": "graph_hopper",
    "arguments": {
      "direction": "backward",
      "analyze_citers": 50,
      "papers_per_direction": 5,
      "include_graph": false
    }
  },
  "network-analytics": {
    "name": "graph_hopper",
    "arguments": {
      "direction": "both",
      "papers_per_direction": 0,
      "include_graph": false
    }
  },
  "network-diagram": {
    "name": "graph_hopper",
    "arguments": {
      "direction": "both",
      "analyze_citers": 50,
      "papers_per_direction": 5,
      "include_graph": true
    }
  },
  "network-wide-examples": {
    "name": "graph_hopper",
    "arguments": {
      "direction": "both",
      "analyze_citers": 100,
      "papers_per_direction": 10,
      "include_graph": false
    }
  },
  "researcher-profile": {
    "name": "profile_researcher",
    "arguments": {}
  },
  "researcher-institution": {
    "name": "profile_researcher",
    "arguments": {},
    "required_inputs": [
      "institution"
    ]
  },
  "venues-shortlist": {
    "name": "find_venues",
    "arguments": {
      "venues": 5
    }
  },
  "venues-period": {
    "name": "find_venues",
    "arguments": {
      "venues": 10
    },
    "required_inputs": [
      "year_from",
      "year_to"
    ]
  },
  "venues-wide": {
    "name": "find_venues",
    "arguments": {
      "venues": 20
    }
  }
}
```
