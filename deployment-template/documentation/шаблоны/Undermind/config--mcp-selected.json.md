> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Undermind: mcp-selected.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_tool_names_or_policy": {
    "include": [
      "get_orientation",
      "list_workspaces",
      "create_workspace",
      "search_papers",
      "find_papers_by_author",
      "lookup_papers_by_metadata",
      "get_paper_info",
      "read_pdfs",
      "get_pdf_download_links",
      "launch_deep_search",
      "inspect_deep_searches",
      "display_deep_search_results",
      "display_references",
      "suggest_pdf_uploads",
      "inspect_files",
      "write_file",
      "inspect_folders",
      "create_folder",
      "move_folder",
      "add_papers_to_folder",
      "remove_papers_from_folder",
      "star_papers",
      "unstar_papers",
      "move_files",
      "move_deep_searches"
    ]
  },
  "target_connection_enabled": false,
  "target_access_check_required": true
}
```
