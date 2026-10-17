> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Scite: mcp-selected.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_tool_names_or_policy": {
    "include": [
      "search_literature",
      "read_fulltext",
      "citation_graph",
      "bibliography",
      "report_citations",
      "citation_report",
      "get_more_tools",
      "search_patents",
      "search_grants",
      "get_grant",
      "search_clinical_trials",
      "get_clinical_trial",
      "search_drugs",
      "get_drug",
      "search_device510k",
      "get_device510k",
      "search_510k_summaries",
      "get_510k_summary",
      "search_faers",
      "get_faers_report",
      "search_maude",
      "get_maude_report",
      "search_mhra",
      "get_mhra_alert",
      "search_collections",
      "get_collection",
      "list_collection_notes",
      "list_collection_files",
      "get_collection_file",
      "get_collection_file_download_url",
      "create_collection",
      "add_dois_to_collection",
      "create_collection_note",
      "update_collection",
      "update_collection_note",
      "upload_collection_file"
    ]
  },
  "target_connection_enabled": false,
  "target_access_check_required": true
}
```
