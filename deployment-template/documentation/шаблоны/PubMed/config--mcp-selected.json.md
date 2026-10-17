> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# PubMed: mcp-selected.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_tool_names_or_policy": {
    "include": [
      "pubmed_search",
      "pubmed_summary",
      "pubmed_fetch",
      "pubmed_links",
      "pubmed_info",
      "pubmed_spell",
      "pubmed_history",
      "pubmed_citation_match",
      "pmc_metadata",
      "pmc_sections",
      "pmc_read",
      "pmc_table",
      "pmc_pdf_status",
      "pubmed_export",
      "service_status"
    ]
  },
  "target_connection_enabled": false,
  "target_access_check_required": true
}
```
