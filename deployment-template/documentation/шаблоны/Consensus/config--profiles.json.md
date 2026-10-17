> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Consensus: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "discovery": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true
    },
    "purpose": "Обзор без отсечения неполных метаданных; препринты отмечаются отдельно."
  },
  "peer-reviewed": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "exclude_preprints": true
    },
    "purpose": "Корпус рецензированных публикаций."
  },
  "recent": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "year_min": 2024,
      "year_max": 2026
    },
    "purpose": "Последние три календарных года; дату уточнять под вопрос."
  },
  "foundational": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "citation_min": 100
    },
    "purpose": "Поиск часто цитируемых работ; цитируемость не заменяет оценку качества."
  },
  "business": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "bus,econ,soc,psych",
      "exclude_preprints": true
    },
    "purpose": "Научные основания решений в управлении и бизнесе."
  },
  "business-field-studies": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "bus,econ,soc,psych",
      "study_types": [
        "field study",
        "longitudinal / panel data study",
        "mixed methods study",
        "case study"
      ]
    },
    "purpose": "Организационные и полевые исследования."
  },
  "economics-models": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "econ,bus",
      "study_types": [
        "theoretical, modeling, or simulation study"
      ]
    },
    "purpose": "Экономические модели; не смешивать модельный вывод и наблюдаемую причинность."
  },
  "academic": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "exclude_preprints": true
    },
    "purpose": "Общая академическая работа без ограничения дисциплины."
  },
  "systematic-reviews": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "study_types": [
        "systematic review",
        "meta-analysis"
      ]
    },
    "purpose": "Обзоры и обобщения; пригодность дизайна определяется вопросом."
  },
  "literature-reviews": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "study_types": [
        "literature review",
        "systematic review"
      ]
    },
    "purpose": "Обзор состояния темы."
  },
  "controlled-human": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "human": true,
      "controlled": true,
      "study_types": [
        "rct"
      ]
    },
    "purpose": "Контролируемые исследования на людях; не применять автоматически к экономике или истории."
  },
  "observational": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "study_types": [
        "cohort study",
        "case-control study",
        "cross-sectional study",
        "longitudinal / panel data study"
      ]
    },
    "purpose": "Наблюдаемые связи и их ограничения."
  },
  "qualitative": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "study_types": [
        "interview study",
        "field study",
        "mixed methods study",
        "case study"
      ]
    },
    "purpose": "Качественные и смешанные методы."
  },
  "historical": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "hist,art,philo,law,ling,soc",
      "study_types": [
        "historical or archival analysis"
      ]
    },
    "purpose": "Исторические и архивные исследования."
  },
  "technical": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "cs,eng,math,mat,phys"
    },
    "purpose": "Технические исследования; сохранять статус препринта."
  },
  "environment": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "env,agri,geol,geog",
      "exclude_preprints": true
    },
    "purpose": "Экологические и природные системы."
  },
  "education": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "domain": "edu,psych,soc",
      "exclude_preprints": true
    },
    "purpose": "Образование и обучение."
  },
  "clinical-guidelines": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "clinical_guideline": true,
      "medical_mode": true
    },
    "purpose": "Клинические руководства; проверять актуальность и первоисточник."
  },
  "open-access-excerpts": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "open_access": true,
      "include_full_text_chunks": true
    },
    "purpose": "Выдержки из методов и результатов доступных полных текстов.",
    "activation_condition": "Платный план; отсутствие выдержки — допустимый результат."
  },
  "excerpts-broad": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "include_full_text_chunks": true
    },
    "purpose": "Широкий поиск с доступными выдержками; часть записей имеет null.",
    "activation_condition": "Платный план."
  },
  "journal-quartiles": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "sjr_max": 2,
      "exclude_preprints": true
    },
    "purpose": "Q1–Q2 как условие выбора журнала, а не оценка отдельной статьи.",
    "activation_condition": "Использовать только когда вопрос требует такого ограничения."
  },
  "sample-filtered": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true,
      "sample_size_min": 100,
      "human": true
    },
    "purpose": "Минимальный размер выборки; неполные метаданные могут уменьшить охват.",
    "activation_condition": "Порог задаётся исследовательским вопросом."
  },
  "wide-page": {
    "params": {
      "page": "${PAGE}",
      "page_size": 100,
      "include_semantic_score": true
    },
    "purpose": "До 100 публикаций в пределах одного учётного вызова."
  },
  "second-page": {
    "params": {
      "page": "${PAGE}",
      "page_size": 20,
      "include_semantic_score": true
    },
    "purpose": "Продолжение выдачи: первая страница имеет номер 0.",
    "activation_condition": "Платный план; проверять is_end и next_page."
  }
}
```
