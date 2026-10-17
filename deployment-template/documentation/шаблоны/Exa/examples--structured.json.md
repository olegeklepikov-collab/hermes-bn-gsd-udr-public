> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Exa: structured.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "query": "${QUERY}",
  "type": "deep",
  "numResults": 2,
  "includeDomains": [
    "exa.ai/docs"
  ],
  "contents": {
    "highlights": true
  },
  "systemPrompt": "Return atomic field values exactly matching the output schema. Each field refers only to its named API operation.",
  "outputSchema": {
    "type": "object",
    "properties": {
      "search_path": {
        "type": "string",
        "pattern": "^/[A-Za-z][A-Za-z0-9/]*$",
        "maxLength": 32,
        "description": "ONLY the Search endpoint path, starting with slash."
      },
      "contents_path": {
        "type": "string",
        "pattern": "^/[A-Za-z][A-Za-z0-9/]*$",
        "maxLength": 32,
        "description": "ONLY the Contents endpoint path, starting with slash."
      }
    },
    "required": [
      "search_path",
      "contents_path"
    ],
    "additionalProperties": false
  }
}
```
