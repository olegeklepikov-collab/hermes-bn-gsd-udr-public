> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Pendar: web-workflows.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "Explore Literature": {
    "url": "https://pendar.ai/app/chat/",
    "guide": "Help → User guides → What is Explore Literature?",
    "price_as_listed": 3,
    "prompt": "${PROMPT}"
  },
  "Deep Research": {
    "url": "https://pendar.ai/app/chat/",
    "guide": "Help → User guides → What is Deep Research?",
    "price_as_listed": 12,
    "prompt": "${PROMPT}"
  },
  "Validate a Claim": {
    "url": "https://pendar.ai/app/chat/",
    "price_as_listed": 3,
    "prompt": "${PROMPT}"
  },
  "Analyze Research Landscape": {
    "url": "https://pendar.ai/app/chat/",
    "price_as_listed": 7,
    "breadth_options": [
      "Broad",
      "Balanced",
      "Strict"
    ],
    "default_breadth": "Balanced",
    "prompt": "${PROMPT}"
  },
  "Chat with Papers": {
    "url": "https://pendar.ai/app/chat/",
    "price_as_listed": "PDF upload: 1 per run; other costs depend on current product",
    "prompt": "${PROMPT}"
  },
  "Create Literature Review": {
    "url": "https://pendar.ai/app/chat/",
    "price_as_listed": "7 up to 15 papers; +1 per five extra papers",
    "formats": [
      "Simplify",
      "Review article",
      "Introduction for a scientific paper",
      "Literature review for an NSF/NIH proposal"
    ],
    "prompt": "${PROMPT}"
  },
  "Schedule Briefing": {
    "url": "https://pendar.ai/app/newsletters/calendar/",
    "price_as_listed": "Up to 3 briefings free for 6 months; 6 briefings advertised at $4/month",
    "activated": false,
    "instructions": "${INSTRUCTIONS}"
  }
}
```
