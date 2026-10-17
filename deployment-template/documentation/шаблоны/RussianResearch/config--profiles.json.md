> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# RussianResearch: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "elibrary-business-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "elibrary",
      "purpose": "business"
    }
  },
  "elibrary-academic-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "elibrary",
      "purpose": "academic"
    }
  },
  "elibrary-general-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "elibrary",
      "purpose": "general"
    }
  },
  "elibrary-topic": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-exact-title": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-author": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-doi": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-methods": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-reviews": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-recent-discovery": {
    "name": "search_candidates",
    "arguments": {
      "platform": "elibrary",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "elibrary-access-options": {
    "name": "source_options",
    "arguments": {
      "platform": "elibrary"
    }
  },
  "elibrary-access-request": {
    "name": "permission_request",
    "arguments": {
      "platform": "elibrary"
    }
  },
  "dissercat-business-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "dissercat",
      "purpose": "business"
    }
  },
  "dissercat-academic-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "dissercat",
      "purpose": "academic"
    }
  },
  "dissercat-general-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "dissercat",
      "purpose": "general"
    }
  },
  "dissercat-topic": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-exact-title": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-author": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-doi": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-methods": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-reviews": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-recent-discovery": {
    "name": "search_candidates",
    "arguments": {
      "platform": "dissercat",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "dissercat-access-options": {
    "name": "source_options",
    "arguments": {
      "platform": "dissercat"
    }
  },
  "dissercat-access-request": {
    "name": "permission_request",
    "arguments": {
      "platform": "dissercat"
    }
  },
  "cyberleninka-business-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "cyberleninka",
      "purpose": "business"
    }
  },
  "cyberleninka-academic-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "cyberleninka",
      "purpose": "academic"
    }
  },
  "cyberleninka-general-plan": {
    "name": "query_plan",
    "arguments": {
      "platform": "cyberleninka",
      "purpose": "general"
    }
  },
  "cyberleninka-topic": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-exact-title": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-author": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-doi": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-methods": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-reviews": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-recent-discovery": {
    "name": "search_candidates",
    "arguments": {
      "platform": "cyberleninka",
      "max_results": 5
    },
    "input_guidance": "Передайте query; для точного названия используйте кавычки, для DOI — полный DOI. Год проверяется по документу."
  },
  "cyberleninka-access-options": {
    "name": "source_options",
    "arguments": {
      "platform": "cyberleninka"
    }
  },
  "cyberleninka-access-request": {
    "name": "permission_request",
    "arguments": {
      "platform": "cyberleninka"
    }
  },
  "doi-verification": {
    "name": "resolve_doi",
    "arguments": {}
  },
  "local-import": {
    "name": "import_document",
    "arguments": {}
  },
  "local-document-info": {
    "name": "document_info",
    "arguments": {}
  },
  "local-page-reading": {
    "name": "read_pages",
    "arguments": {}
  },
  "local-fulltext-find": {
    "name": "find_in_document",
    "arguments": {}
  },
  "local-bibliography-export": {
    "name": "export_document_metadata",
    "arguments": {
      "format": "ris"
    }
  }
}
```
