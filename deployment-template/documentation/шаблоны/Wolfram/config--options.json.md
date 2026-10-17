> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Wolfram: options.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
[
  {
    "option": "Wolfram Cloud MCP",
    "status": "candidate_requires_target_selection",
    "url": "https://agenttools.wolfram.com/mcp",
    "access": "Официальный свободный анонимный режим для ограниченного личного использования",
    "scope": "Context + Alpha + LanguageEvaluator, самостоятельные запросы"
  },
  {
    "option": "Wolfram Local MCP — Wolfram",
    "status": "optional_requires_local_product",
    "tools": [
      "WolframContext",
      "WolframLanguageEvaluator",
      "WolframAlpha"
    ],
    "scope": "Общие вычисления и знания, сохраняемый сеанс"
  },
  {
    "option": "Wolfram Local MCP — WolframAlpha",
    "status": "optional_requires_local_product_and_LLMKit",
    "tools": [
      "WolframAlphaContext",
      "WolframAlpha"
    ],
    "scope": "Только Alpha; отдельный LLMKit требуется текущему установщику"
  },
  {
    "option": "Wolfram Local MCP — WolframLanguage",
    "status": "optional_requires_local_product",
    "tools": [
      "WolframLanguageContext",
      "WolframLanguageEvaluator",
      "ReadNotebook",
      "WriteNotebook",
      "SymbolDefinition",
      "CodeInspector",
      "TestReport"
    ],
    "scope": "Вычисления, местные файлы, блокноты, разработка и проверка кода"
  },
  {
    "option": "Wolfram Local MCP — WolframPacletDevelopment",
    "status": "not_needed_for_current_research_scope",
    "tools": [
      "CreateSymbolDoc",
      "EditSymbolDoc",
      "EditSymbolDocExamples",
      "CheckPaclet",
      "BuildPaclet",
      "SubmitPaclet"
    ],
    "scope": "Дополнение WolframLanguage для разработки и публикации пакетов"
  },
  {
    "option": "Wolfram Enterprise MCP / private deployment",
    "status": "optional_requires_agreement",
    "url": "https://www.wolfram.com/artificial-intelligence/mcp/enterprise/",
    "scope": "Корпоративный масштаб и управляемая инфраструктура"
  },
  {
    "option": "Wolfram|Alpha Full Results API",
    "status": "optional_requires_own_AppID_and_usage_terms",
    "url": "https://products.wolframalpha.com/api/documentation/",
    "scope": "XML/JSON, разделы ответа, допущения, уточнение, асинхронная выдача"
  },
  {
    "option": "Wolfram|Alpha LLM API",
    "status": "optional_requires_own_AppID_and_usage_terms",
    "url": "https://products.wolframalpha.com/llm-api/documentation",
    "scope": "Ответы для языковой модели, JSON и ограничение длины"
  },
  {
    "option": "Wolfram|Alpha Simple API",
    "status": "optional_requires_own_AppID_and_usage_terms",
    "url": "https://products.wolframalpha.com/simple-api/documentation",
    "scope": "Изображение страницы результатов"
  },
  {
    "option": "Wolfram|Alpha Short Answers API",
    "status": "optional_requires_own_AppID_and_usage_terms",
    "url": "https://products.wolframalpha.com/short-answers-api/documentation",
    "scope": "Короткий текстовый ответ"
  },
  {
    "option": "Wolfram|Alpha Spoken Results API",
    "status": "optional_requires_own_AppID_and_usage_terms",
    "url": "https://products.wolframalpha.com/spoken-results-api/documentation",
    "scope": "Текст для голосового ответа"
  },
  {
    "option": "Wolfram|Alpha Fast Query Recognizer API",
    "status": "optional_requires_own_AppID_and_usage_terms",
    "url": "https://products.wolframalpha.com/query-recognizer/documentation",
    "scope": "Определение пригодности запроса к Alpha"
  },
  {
    "option": "Wolfram|Alpha Summary Boxes API",
    "status": "not_needed_for_current_research_scope",
    "url": "https://products.wolframalpha.com/summary-boxes-api/documentation",
    "scope": "Краткие блоки сведений для интерфейсов"
  },
  {
    "option": "Wolfram|Alpha Instant Calculators API",
    "status": "not_needed_for_current_research_scope",
    "url": "https://products.wolframalpha.com/instant-calculators-api/documentation",
    "scope": "Формы вычислений для сайтов"
  },
  {
    "option": "CAG — Wolfram|Alpha Context API",
    "status": "optional_requires_own_CAG_key",
    "url": "https://www.wolfram.com/apis/documentation/cag/wolfram-alpha-context-api/",
    "scope": "Дополнительные фактические запросы по контексту, число результатов"
  },
  {
    "option": "CAG — Wolfram|Alpha Results API",
    "status": "optional_requires_own_CAG_key",
    "url": "https://www.wolfram.com/apis/documentation/cag/wolfram-alpha-results-api/",
    "scope": "Текст Alpha и расширенные параметры запроса"
  },
  {
    "option": "CAG — Wolfram Language Computation API",
    "status": "optional_requires_own_CAG_key",
    "url": "https://www.wolfram.com/apis/documentation/cag/wolfram-language-computation-api/",
    "scope": "Вычисление кода, maxChars, line, timeConstraint"
  },
  {
    "option": "CAG — Wolfram Language Hints API",
    "status": "optional_requires_own_CAG_key",
    "url": "https://www.wolfram.com/apis/documentation/cag/wolfram-language-hints-api/",
    "scope": "Примеры кода и документация по задаче"
  },
  {
    "option": "Wolfram Agent One API",
    "status": "not_selected_model_preserved",
    "url": "https://www.wolfram.com/apis/documentation/cag/wolfram-agent-one-api/",
    "scope": "Самостоятельный агент языковой модели, Chat Completions, потоковая выдача и аннотации вычислений"
  },
  {
    "option": "Own Wolfram Cloud APIs / wolframscript / Python client / WSTP",
    "status": "optional_requires_local_or_cloud_account_and_license",
    "url": "https://www.wolfram.com/apis/documentation/",
    "scope": "Собственные программные функции, облачные приложения и вычислительные процессы"
  }
]
```
