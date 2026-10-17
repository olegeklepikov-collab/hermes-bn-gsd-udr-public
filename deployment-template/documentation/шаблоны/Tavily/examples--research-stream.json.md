> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Tavily: research-stream.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "input": "Use the attached synthetic fixture and the official Tavily Search documentation. Return the fixture_value from the file and the three supported Search topics. Cite sources. The fixture is created test data, not real business information.",
  "model": "mini",
  "citation_format": "numbered",
  "output_length": "short",
  "include_domains": [
    "docs.tavily.com"
  ],
  "exclude_domains": [
    "reddit.com",
    "quora.com"
  ],
  "files": [
    {
      "name": "public-fixture.json",
      "data": "eyJmaXh0dXJlX3ZhbHVlIjogNDIsICJmaXh0dXJlX25hbWUiOiAiSGVybWVzIEJOIHN5bnRoZXRpYyBpbnRlZ3JhdGlvbiBmaXh0dXJlIiwgIm5vdF9yZWFsX2J1c2luZXNzX2RhdGEiOiB0cnVlfQ==",
      "type": "base64"
    }
  ],
  "output_schema": {
    "properties": {
      "fixture_value": {
        "type": "integer",
        "description": "Numeric fixture_value read from the attached public-fixture.json file."
      },
      "topics": {
        "type": "array",
        "description": "The supported Tavily Search topic names from the official documentation.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "fixture_value",
      "topics"
    ]
  }
}
```
