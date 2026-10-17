> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Scite: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "literature": {
    "purpose": "Поиск литературы с логическими операторами",
    "command": "call",
    "name": "search_literature",
    "arguments": {
      "limit": 10,
      "offset": 0
    }
  },
  "recent": {
    "purpose": "Литература за указанный период; даты задаются явно",
    "command": "call",
    "name": "search_literature",
    "arguments": {
      "limit": 10,
      "offset": 0
    }
  },
  "reviews": {
    "purpose": "Обзоры и метаанализы; тип проверяется по статье",
    "command": "call",
    "name": "search_literature",
    "arguments": {
      "paper_type": "Review",
      "limit": 10
    }
  },
  "supporting": {
    "purpose": "Поиск работ с поддерживающими цитированиями",
    "command": "call",
    "name": "search_literature",
    "arguments": {
      "supporting_from": 1,
      "limit": 10
    }
  },
  "contrasting": {
    "purpose": "Поиск работ с противоположными цитированиями",
    "command": "call",
    "name": "search_literature",
    "arguments": {
      "contrasting_from": 1,
      "limit": 10
    }
  },
  "editorial-audit": {
    "purpose": "Метаданные DOI и редакционные сообщения",
    "command": "call",
    "name": "search_literature",
    "arguments": {}
  },
  "paper-sections": {
    "purpose": "Выдержки по методам, результатам и ограничениям: dois + term",
    "command": "call",
    "name": "search_literature",
    "arguments": {}
  },
  "fulltext": {
    "purpose": "Доступный полный текст частями; проверять source/contentDenied/hasMore",
    "command": "call",
    "name": "read_fulltext",
    "arguments": {
      "length": 8000,
      "offset": 0
    }
  },
  "citation-network": {
    "purpose": "Сеть цитирований: направление меняется in/out/both",
    "command": "call",
    "name": "citation_graph",
    "arguments": {
      "depth": 1,
      "direction": "both",
      "max_edges": 100,
      "include_intent": true,
      "include_snippets": true
    }
  },
  "bibliography": {
    "purpose": "Библиография по подтверждённым DOI",
    "command": "call",
    "name": "bibliography",
    "arguments": {
      "format": "bibtex"
    }
  },
  "source-ledger": {
    "purpose": "Сохранение решений включения/исключения источников",
    "command": "call",
    "name": "report_citations",
    "arguments": {}
  },
  "citation-audit": {
    "purpose": "Аудит источников текущего сеанса",
    "command": "call",
    "name": "citation_report",
    "arguments": {}
  },
  "patents": {
    "purpose": "Патенты и патентные семейства",
    "command": "call",
    "name": "search_patents",
    "arguments": {
      "p": 1
    }
  },
  "grants": {
    "purpose": "Исследовательские гранты",
    "command": "call",
    "name": "search_grants",
    "arguments": {
      "p": 1
    }
  },
  "clinical-trials": {
    "purpose": "Зарегистрированные исследования",
    "command": "call",
    "name": "search_clinical_trials",
    "arguments": {
      "p": 1
    }
  },
  "drug-records": {
    "purpose": "Официальные данные FDA о препаратах",
    "command": "call",
    "name": "search_drugs",
    "arguments": {
      "p": 1
    }
  },
  "device-clearances": {
    "purpose": "Решения FDA по устройствам",
    "command": "call",
    "name": "search_device510k",
    "arguments": {
      "p": 1
    }
  },
  "device-documents": {
    "purpose": "Текст документов FDA 510(k)",
    "command": "call",
    "name": "search_510k_summaries",
    "arguments": {
      "p": 1
    }
  },
  "drug-event-reports": {
    "purpose": "Сообщения FAERS; не частота или доказательство причинности",
    "command": "call",
    "name": "search_faers",
    "arguments": {
      "p": 1
    }
  },
  "device-event-reports": {
    "purpose": "Сообщения MAUDE; не доказательство причинности",
    "command": "call",
    "name": "search_maude",
    "arguments": {
      "p": 1
    }
  },
  "safety-alerts": {
    "purpose": "Официальные предупреждения MHRA",
    "command": "call",
    "name": "search_mhra",
    "arguments": {
      "p": 1
    }
  },
  "collections": {
    "purpose": "Поиск доступных подборок по имени",
    "command": "call",
    "name": "search_collections",
    "arguments": {}
  },
  "collection-record": {
    "purpose": "Метаданные и видимость известной подборки",
    "command": "call",
    "name": "get_collection",
    "arguments": {}
  },
  "collection-papers": {
    "purpose": "Поиск внутри подборки по collection_slug",
    "command": "call",
    "name": "search_literature",
    "arguments": {
      "limit": 10
    }
  },
  "private-collection": {
    "purpose": "Создание закрытой подборки по заданию пользователя",
    "command": "call",
    "name": "create_collection",
    "arguments": {
      "is_shared_with_org": false,
      "is_shared_publicly": false
    }
  },
  "add-papers": {
    "purpose": "Добавление DOI в явно выбранную подборку",
    "command": "call",
    "name": "add_dois_to_collection",
    "arguments": {}
  },
  "collection-notes": {
    "purpose": "Чтение заметок явно выбранной подборки",
    "command": "call",
    "name": "list_collection_notes",
    "arguments": {}
  },
  "collection-files": {
    "purpose": "Список файлов явно выбранной подборки",
    "command": "call",
    "name": "list_collection_files",
    "arguments": {}
  },
  "review-workflow": {
    "purpose": "Обзор литературы",
    "command": "prompt",
    "name": "literature-review",
    "arguments": {}
  },
  "claim-workflow": {
    "purpose": "Проверка научного утверждения",
    "command": "prompt",
    "name": "fact-check-claim",
    "arguments": {}
  },
  "screening-workflow": {
    "purpose": "Отбор исследований по критериям",
    "command": "prompt",
    "name": "systematic-review-screen",
    "arguments": {}
  },
  "reference-workflow": {
    "purpose": "Проверка библиографической записи",
    "command": "prompt",
    "name": "verify-bibliography",
    "arguments": {}
  },
  "paper-metadata": {
    "purpose": "Публичные метаданные DOI",
    "command": "rest",
    "name": "getPaper",
    "arguments": {}
  },
  "papers-bulk": {
    "purpose": "Пакет метаданных; JSON-массив DOI, до 500",
    "command": "rest",
    "name": "getPapersBulk",
    "arguments": {}
  },
  "tally": {
    "purpose": "Публичные показатели цитирований DOI",
    "command": "rest",
    "name": "getTally",
    "arguments": {}
  },
  "tallies-bulk": {
    "purpose": "Пакет показателей; JSON-массив DOI, до 500",
    "command": "rest",
    "name": "getTalliesBulk",
    "arguments": {}
  },
  "section-tally": {
    "purpose": "Цитирования по разделам статьи",
    "command": "rest",
    "name": "getSectionTally",
    "arguments": {}
  },
  "tallies-aggregate": {
    "purpose": "Сумма показателей для массива DOI",
    "command": "rest",
    "name": "getAggregateTally",
    "arguments": {}
  },
  "pmid-to-doi": {
    "purpose": "Разрешение PMID в DOI",
    "command": "rest",
    "name": "resolvePmidToDoi",
    "arguments": {}
  },
  "paper-recommendations": {
    "purpose": "Связанные работы по DOI; доступ зависит от ключа",
    "command": "rest",
    "name": "getRecommendedPapers",
    "arguments": {}
  },
  "author-publications": {
    "purpose": "Публикации автора по полученному authorSlug",
    "command": "rest",
    "name": "getAuthorPapers",
    "arguments": {}
  },
  "author-statistics": {
    "purpose": "Статистика автора по полученному authorSlug",
    "command": "rest",
    "name": "getAuthorStats",
    "arguments": {}
  },
  "journal-statistics": {
    "purpose": "Показатели журнала по ISSN",
    "command": "rest",
    "name": "getJournalTallies",
    "arguments": {}
  },
  "assistant-task": {
    "purpose": "Статус созданного задания Assistant; требуется разрешение",
    "command": "rest",
    "name": "getAssistantTask",
    "arguments": {}
  },
  "reference-check-task": {
    "purpose": "Статус задания Reference Check; требуется разрешение",
    "command": "rest",
    "name": "getReferenceCheckResult",
    "arguments": {}
  }
}
```
