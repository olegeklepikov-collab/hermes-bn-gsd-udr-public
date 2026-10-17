> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# R: mcp-selected.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_tool_names_or_policy": {
    "include": [
      "btw_tool_cran_search",
      "btw_tool_cran_versions",
      "btw_tool_cran_package",
      "btw_tool_docs_package_news",
      "btw_tool_docs_package_help_topics",
      "btw_tool_docs_help_page",
      "btw_tool_docs_available_vignettes",
      "btw_tool_docs_vignette",
      "btw_tool_env_describe_data_frame",
      "btw_tool_env_describe_environment",
      "btw_tool_run_r",
      "btw_tool_sessioninfo_is_package_installed",
      "btw_tool_sessioninfo_platform",
      "btw_tool_sessioninfo_package"
    ]
  },
  "target_connection_enabled": false,
  "target_access_check_required": true
}
```
