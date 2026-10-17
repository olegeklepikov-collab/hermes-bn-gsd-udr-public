> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# ScholarSidekick: mcp-selected.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_tool_names_or_policy": {
    "include": [
      "verifyCitation",
      "auditBibliography",
      "checkRetraction",
      "checkOpenAccess",
      "resolveIdentifier",
      "formatCitation",
      "exportCitation"
    ]
  },
  "target_connection_enabled": false,
  "target_access_check_required": true
}
```
