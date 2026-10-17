> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# AlphaXiv: mcp-selected.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_tool_names_or_policy": {
    "include": [
      "answer_pdf_queries",
      "get_paper_content",
      "read_files_from_github_repository",
      "discover_papers",
      "find_researchers",
      "get_researcher",
      "get_researcher_papers",
      "resolve_researchers",
      "get_paper_notes",
      "list_annotated_papers",
      "list_library",
      "save_papers_to_folder",
      "remove_papers_from_folder",
      "move_papers_between_folders",
      "create_folder",
      "rename_folder",
      "get_for_you_feed",
      "get_hot_feed",
      "edit_private_paper_metadata",
      "list_followed_researchers",
      "follow_researcher",
      "unfollow_researcher"
    ]
  },
  "target_connection_enabled": false,
  "target_access_check_required": true
}
```
