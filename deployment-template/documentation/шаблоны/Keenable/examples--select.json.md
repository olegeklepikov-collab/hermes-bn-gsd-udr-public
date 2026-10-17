> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Keenable: select.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "query": "SELECT url,\n  UNNEST(SEM_EXTRACT(content,\n    monthly_requests := 'number of free API requests per monthly cycle for an authenticated organization; integer only, NULL if not stated',\n    organization_rps := 'authenticated organization requests-per-second limit; integer only, NULL if not stated',\n    evidence := 'per_field'\n  ), recursive := true)\nFROM WEB_FETCH(\n  'https://docs.keenable.ai/credits',\n  'https://docs.keenable.ai/rate-limits'\n)",
  "show_preview": false
}
```
