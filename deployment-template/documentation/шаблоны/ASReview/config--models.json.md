> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# ASReview: models.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "elas_u4": {
    "description": "ELAS u4",
    "value": {
      "querier": "max",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.11
      },
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "official ASReview 3.0.8"
  },
  "elas_u3": {
    "description": "ELAS u3",
    "value": {
      "querier": "max",
      "classifier": "nb",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "alpha": 3.822
      },
      "balancer_param": {
        "ratio": 1.2
      },
      "feature_extractor_param": {
        "stop_words": "english"
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "official ASReview 3.0.8"
  },
  "elas_l2": {
    "description": "ELAS l2",
    "value": {
      "querier": "max",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "multilingual-e5-large",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.106,
        "max_iter": 5000
      },
      "balancer_param": {
        "ratio": 9.707
      },
      "feature_extractor_param": {
        "normalize": true,
        "model_name": "${RUNTIME_ROOT}/ASReview/cache/huggingface/hub/models--intfloat--multilingual-e5-large/snapshots/3d7cfbdacd47fdda877c5cd8a79fbcc4f2a574f3",
        "device": "cpu",
        "verbose": false
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "official ASReview 3.0.8"
  },
  "elas_h3": {
    "description": "ELAS h3",
    "value": {
      "querier": "max",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "mxbai",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.067,
        "max_iter": 5000
      },
      "balancer_param": {
        "ratio": 9.724
      },
      "feature_extractor_param": {
        "normalize": true,
        "model_name": "${RUNTIME_ROOT}/ASReview/cache/huggingface/hub/models--mixedbread-ai--mxbai-embed-large-v1/snapshots/b33106f585b9ce46904ad7443a3b52b7a63e231c",
        "device": "cpu",
        "verbose": false
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "official ASReview 3.0.8"
  },
  "logistic_tfidf": {
    "description": "Логистическая регрессия и словесные признаки для сравнения",
    "value": {
      "querier": "max",
      "classifier": "logistic",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {},
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "forest_tfidf": {
    "description": "Случайный лес для сравнения на локальных данных",
    "value": {
      "querier": "max",
      "classifier": "rf",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "n_estimators": 100,
        "n_jobs": 1
      },
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "mixed_random": {
    "description": "Максимальный приоритет с 5% случайных записей",
    "value": {
      "querier": "max_random",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.11
      },
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "mixed_uncertainty": {
    "description": "Максимальный приоритет с 5% неопределённых записей",
    "value": {
      "querier": "max_uncertainty",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.11
      },
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "uncertainty_tfidf": {
    "description": "Проверка пограничных записей",
    "value": {
      "querier": "uncertainty",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.11
      },
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "char_svm": {
    "description": "Символьные признаки для русскоязычных данных и вариаций написания",
    "value": {
      "querier": "max",
      "classifier": "svm",
      "balancer": "balanced",
      "feature_extractor": "tfidf",
      "stopper": null,
      "querier_param": {},
      "classifier_param": {
        "loss": "squared_hinge",
        "C": 0.11
      },
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "analyzer": "char_wb",
        "ngram_range": [
          3,
          5
        ],
        "min_df": 1,
        "max_features": 100000,
        "sublinear_tf": true
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "random": {
    "description": "Случайный контрольный порядок",
    "value": {
      "querier": "random",
      "classifier": null,
      "balancer": null,
      "feature_extractor": null,
      "stopper": null,
      "querier_param": {},
      "classifier_param": {},
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  },
  "top_down": {
    "description": "Исходный порядок для контрольной проверки",
    "value": {
      "querier": "top_down",
      "classifier": null,
      "balancer": null,
      "feature_extractor": null,
      "stopper": null,
      "querier_param": {},
      "classifier_param": {},
      "balancer_param": {
        "ratio": 9.8
      },
      "feature_extractor_param": {
        "ngram_range": [
          1,
          2
        ],
        "sublinear_tf": true,
        "min_df": 1,
        "max_df": 0.95
      },
      "stopper_param": {},
      "n_query": 1
    },
    "source": "Hermes BN configuration using official ASReview components"
  }
}
```
