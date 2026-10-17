> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Parallel: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "search-turbo": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "turbo",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 5
      }
    },
    "purpose": "Поиск; каждый запрос дополняется objective и search_queries."
  },
  "search-fast": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "fast",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 5
      }
    },
    "purpose": "Поиск; каждый запрос дополняется objective и search_queries."
  },
  "search-basic": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "basic",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 5
      }
    },
    "purpose": "Поиск; каждый запрос дополняется objective и search_queries."
  },
  "search-advanced": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "advanced",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 5
      }
    },
    "purpose": "Поиск; каждый запрос дополняется objective и search_queries."
  },
  "search-academic": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "advanced",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 8
      }
    },
    "purpose": "Общий поиск без жёсткого ограничения источников. Предпочтительные источники добавляются в objective с учётом темы, страны и дисциплины; строгий список задаётся только при требовании ограниченного корпуса.",
    "source_preferences": [
      "arxiv.org",
      "pubmed.ncbi.nlm.nih.gov",
      "pmc.ncbi.nlm.nih.gov",
      "doi.org"
    ]
  },
  "search-business": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "advanced",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 8
      }
    },
    "purpose": "Общий поиск без жёсткого ограничения источников. Предпочтительные источники добавляются в objective с учётом темы, страны и дисциплины; строгий список задаётся только при требовании ограниченного корпуса.",
    "source_preferences": [
      "sec.gov",
      "investor.gov",
      "bls.gov",
      "census.gov",
      "worldbank.org"
    ]
  },
  "search-fresh": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "fast",
      "max_chars_total": 20000,
      "advanced_settings": {
        "max_results": 5,
        "fetch_policy": {
          "max_age_seconds": 600,
          "timeout_seconds": 20,
          "disable_cache_fallback": true
        }
      }
    },
    "purpose": "Свежие страницы; дату публикации задавать отдельно."
  },
  "extract-focused": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "max_chars_total": 20000,
      "advanced_settings": {}
    },
    "purpose": "Чтение одной или нескольких страниц, PDF, страниц с динамическим содержанием."
  },
  "extract-full": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "max_chars_total": 20000,
      "advanced_settings": {
        "full_content": true
      }
    },
    "purpose": "Чтение одной или нескольких страниц, PDF, страниц с динамическим содержанием."
  },
  "extract-live": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "max_chars_total": 20000,
      "advanced_settings": {
        "full_content": true,
        "fetch_policy": {
          "max_age_seconds": 600,
          "timeout_seconds": 20,
          "disable_cache_fallback": true
        }
      }
    },
    "purpose": "Чтение одной или нескольких страниц, PDF, страниц с динамическим содержанием."
  },
  "task-lite": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "lite",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input."
  },
  "task-base": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "base",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input."
  },
  "task-core": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "core",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input."
  },
  "task-core2x": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "core2x",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input."
  },
  "task-pro": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "pro",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input."
  },
  "task-ultra": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "ultra",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input.",
    "activation_condition": "Заранее ограниченный бюджет и объём."
  },
  "task-ultra2x": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "ultra2x",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input.",
    "activation_condition": "Заранее ограниченный бюджет и объём."
  },
  "task-ultra4x": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "ultra4x",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input.",
    "activation_condition": "Заранее ограниченный бюджет и объём."
  },
  "task-ultra8x": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "processor": "ultra8x",
      "enable_events": true,
      "memory_scope_key": "hermes-bn",
      "task_spec": {
        "output_schema": {
          "type": "text",
          "description": "Ответ по-русски: факты, источники с URL, даты, ограничения и противоречия."
        }
      }
    },
    "purpose": "Исследование; вход задаётся в input.",
    "activation_condition": "Заранее ограниченный бюджет и объём."
  },
  "response-low": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "model": "parallel",
      "reasoning": {
        "effort": "low"
      }
    },
    "purpose": "Ответ с источниками; input обязателен. Поддерживает stream, previous_response_id и text.format."
  },
  "response-medium": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "model": "parallel",
      "reasoning": {
        "effort": "medium"
      }
    },
    "purpose": "Ответ с источниками; input обязателен. Поддерживает stream, previous_response_id и text.format."
  },
  "response-high": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "model": "parallel",
      "reasoning": {
        "effort": "high"
      }
    },
    "purpose": "Ответ с источниками; input обязателен. Поддерживает stream, previous_response_id и text.format."
  },
  "findall-preview": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "generator": "preview",
      "match_limit": 5,
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "Проверяемый список; objective, entity_type и match_conditions обязательны."
  },
  "findall-base": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "generator": "base",
      "match_limit": 5,
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "Проверяемый список; objective, entity_type и match_conditions обязательны."
  },
  "findall-core": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "generator": "core",
      "match_limit": 5,
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "Проверяемый список; objective, entity_type и match_conditions обязательны.",
    "activation_condition": "Бюджет перед запуском."
  },
  "findall-pro": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "generator": "pro",
      "match_limit": 5,
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "Проверяемый список; objective, entity_type и match_conditions обязательны.",
    "activation_condition": "Бюджет перед запуском."
  },
  "entity-people": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "entity_type": "people",
      "match_limit": 5
    },
    "purpose": "Быстрый подбор людей или компаний; не заменяет проверку FindAll."
  },
  "entity-companies": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "entity_type": "companies",
      "match_limit": 5
    },
    "purpose": "Быстрый подбор людей или компаний; не заменяет проверку FindAll."
  },
  "images-fast": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "fast"
    },
    "purpose": "Поиск изображений с адресами исходных страниц. Проверять права перед повторным использованием."
  },
  "images-advanced": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "mode": "advanced"
    },
    "purpose": "Поиск изображений с адресами исходных страниц. Проверять права перед повторным использованием."
  },
  "monitor-event_stream-lite": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "type": "event_stream",
      "processor": "lite",
      "frequency": "1d",
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "События или изменения готового Task Run; settings обязательны. Постоянные задания не созданы.",
    "activation_condition": "Только отдельный запрос пользователя с предметом и периодом наблюдения."
  },
  "monitor-event_stream-base": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "type": "event_stream",
      "processor": "base",
      "frequency": "1d",
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "События или изменения готового Task Run; settings обязательны. Постоянные задания не созданы.",
    "activation_condition": "Только отдельный запрос пользователя с предметом и периодом наблюдения."
  },
  "monitor-snapshot-lite": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "type": "snapshot",
      "processor": "lite",
      "frequency": "1d",
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "События или изменения готового Task Run; settings обязательны. Постоянные задания не созданы.",
    "activation_condition": "Только отдельный запрос пользователя с предметом и периодом наблюдения."
  },
  "monitor-snapshot-base": {
    "method": "POST",
    "path": "${PATH}",
    "body": {
      "type": "snapshot",
      "processor": "base",
      "frequency": "1d",
      "memory_scope_key": "hermes-bn"
    },
    "purpose": "События или изменения готового Task Run; settings обязательны. Постоянные задания не созданы.",
    "activation_condition": "Только отдельный запрос пользователя с предметом и периодом наблюдения."
  }
}
```
