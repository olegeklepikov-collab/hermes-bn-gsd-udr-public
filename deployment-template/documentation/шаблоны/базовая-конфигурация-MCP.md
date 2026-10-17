> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Базовая конфигурация MCP

Все подключения выключены до установки программ и собственной авторизации. OAuth-клиенты, токены и состояния входа не переносятся. Команды местных переходников нужно установить отдельно и указать их исполняемые пути. Переменные являются обозначениями шаблона, а не обещанием автоматической подстановки конкретной версией Hermes.

```json
{
  "model": {
    "provider": "${MODEL_PROVIDER}",
    "default": "${MODEL_NAME}"
  },
  "mcp_servers": {
    "firecrawl": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer ${FIRECRAWL_API_KEY}"
      },
      "tools": {
        "exclude": [
          "firecrawl_feedback",
          "firecrawl_search_feedback"
        ]
      }
    },
    "exa": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "url": "https://mcp.exa.ai/mcp?tools=web_search_exa%2Cweb_fetch_exa%2Cweb_search_advanced_exa%2Cagent_run",
      "headers": {
        "x-api-key": "${EXA_API_KEY}"
      }
    },
    "tavily": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "command": "${TAVILY_MCP_COMMAND}",
      "args": []
    },
    "keenable": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "url": "https://api.keenable.ai/mcp",
      "headers": {
        "X-API-Key": "${KEENABLE_API_KEY}",
        "X-Keenable-Title": "${KEENABLE_API_KEY}"
      }
    },
    "keenable-select": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "url": "https://select.keenable.ai/mcp",
      "headers": {
        "X-API-Key": "${KEENABLE_SELECT_API_KEY}"
      }
    },
    "nimble": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "url": "https://mcp.nimbleway.com/mcp",
      "headers": {
        "Authorization": "Bearer ${NIMBLE_API_KEY}",
        "X-Client-Source": "${NIMBLE_API_KEY}"
      },
      "tools": {
        "exclude": [
          "nimble_agents_delete",
          "nimble_extract_templates_generate",
          "nimble_extract_templates_generation_status",
          "nimble_extract_templates_update_from_template"
        ]
      }
    },
    "nimble-docs": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 180,
      "url": "https://docs.nimbleway.com/mcp",
      "tools": {
        "exclude": [
          "submit_feedback"
        ]
      }
    },
    "parallel-search": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "url": "https://search.parallel.ai/mcp?mode=fast",
      "headers": {
        "Authorization": "Bearer ${PARALLEL_SEARCH_API_KEY}"
      }
    },
    "parallel-task": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "url": "https://task-mcp.parallel.ai/mcp",
      "headers": {
        "Authorization": "Bearer ${PARALLEL_TASK_API_KEY}"
      }
    },
    "consensus": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "url": "https://mcp.consensus.app/mcp",
      "headers": {
        "Authorization": "Bearer ${CONSENSUS_API_KEY}"
      }
    },
    "scite": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 90,
      "url": "https://api.scite.ai/mcp",
      "auth": "oauth",
      "tools": {
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
      }
    },
    "undermind": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 240,
      "url": "https://mcp.undermind.ai/mcp",
      "auth": "oauth",
      "tools": {
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
      }
    },
    "alphaxiv": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 240,
      "url": "https://api.alphaxiv.org/mcp/v1",
      "auth": "oauth",
      "tools": {
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
      }
    },
    "semanticscholar": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 150,
      "command": "${SEMANTICSCHOLAR_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "author_batch",
          "author_search",
          "author_details",
          "author_papers",
          "paper_autocomplete",
          "paper_batch",
          "paper_search",
          "paper_bulk_search",
          "paper_match_title",
          "paper_details",
          "paper_authors",
          "paper_citations",
          "paper_references",
          "snippet_search",
          "recommend_by_examples",
          "recommend_for_paper",
          "dataset_diffs",
          "dataset_releases",
          "dataset_release",
          "dataset_manifest",
          "service_status"
        ]
      }
    },
    "pubmed": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 150,
      "command": "${PUBMED_MCP_COMMAND}",
      "args": [],
      "tools": {
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
      }
    },
    "russianresearch": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 150,
      "command": "${RUSSIANRESEARCH_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "source_options",
          "query_plan",
          "search_candidates",
          "resolve_doi",
          "import_document",
          "document_info",
          "read_pages",
          "find_in_document",
          "export_document_metadata",
          "permission_request"
        ]
      }
    },
    "webofscience": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 150,
      "command": "${WEBOFSCIENCE_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "capability_catalog",
          "query_plan",
          "access_request"
        ]
      }
    },
    "pendar": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "url": "https://pendar.ai/mcp",
      "auth": "oauth",
      "tools": {
        "include": [
          "verify_paper",
          "survey_literature",
          "graph_hopper",
          "audit_bibliography",
          "profile_researcher",
          "find_venues"
        ]
      }
    },
    "scholarsidekick": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "url": "https://scholar-sidekick.com/api/mcp",
      "tools": {
        "include": [
          "verifyCitation",
          "auditBibliography",
          "checkRetraction",
          "checkOpenAccess",
          "resolveIdentifier",
          "formatCitation",
          "exportCitation"
        ]
      }
    },
    "wolfram": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "url": "https://agenttools.wolfram.com/mcp",
      "tools": {
        "include": [
          "WolframContext",
          "WolframAlpha",
          "WolframLanguageEvaluator"
        ]
      }
    },
    "rstats": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 600,
      "command": "${RSTATS_MCP_COMMAND}",
      "args": [],
      "tools": {
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
      }
    },
    "zotero": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 150,
      "command": "${ZOTERO_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "schema",
          "item_template",
          "groups",
          "query_items",
          "get_item",
          "item_children",
          "collections",
          "tags",
          "saved_searches",
          "fulltext_versions",
          "read_fulltext",
          "attachment_info",
          "read_pdf_pages",
          "render_pdf_page",
          "export_items",
          "create_items",
          "patch_item",
          "create_collections",
          "patch_collection",
          "create_saved_searches",
          "patch_saved_search",
          "create_note",
          "attach_file",
          "create_annotation",
          "index_fulltext",
          "trash_item",
          "restore_item"
        ]
      }
    },
    "crossref": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 150,
      "command": "${CROSSREF_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "works_search",
          "work_get",
          "works_batch",
          "bibliographic_match",
          "doi_agency",
          "doi_exists",
          "work_references",
          "work_relations",
          "work_updates",
          "work_funding",
          "work_licenses_links",
          "entities_search",
          "entity_get",
          "works_facets",
          "works_sample",
          "metadata_transform",
          "citation_styles",
          "export_records",
          "xml_doi_lookup",
          "xml_citation_match",
          "openurl_lookup",
          "data_citations",
          "oai_discovery"
        ]
      }
    },
    "openalex": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 180,
      "url": "https://mcp.openalex.org/mcp",
      "auth": "oauth",
      "tools": {
        "include": [
          "search_works",
          "get_work",
          "resolve_references",
          "list_citations",
          "search_entities",
          "get_entity",
          "group_works",
          "analyze_works",
          "find_keywords",
          "keyword_search",
          "read_docs",
          "check_oql",
          "calculate_works"
        ]
      }
    },
    "openalex-api": {
      "enabled": false,
      "connect_timeout": 30,
      "tool_timeout": 180,
      "command": "${OPENALEX_API_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "list_entities",
          "get_entity",
          "batch_entities",
          "group_entities",
          "semantic_search",
          "autocomplete",
          "read_abstract",
          "work_links",
          "work_metrics",
          "citations",
          "translate_query",
          "execute_query",
          "classify_text",
          "download_content",
          "content_structure",
          "read_content",
          "read_pdf_pages",
          "render_pdf_page",
          "export_results",
          "save_query"
        ]
      }
    },
    "asreview": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 600,
      "command": "${ASREVIEW_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "model_catalog",
          "inspect_dataset",
          "prepare_dataset",
          "create_project",
          "list_projects",
          "project_info",
          "list_records",
          "get_record",
          "set_protocol",
          "get_protocol",
          "configure_model",
          "train_rank",
          "next_records",
          "propose_decisions",
          "record_decision",
          "progress",
          "decision_history",
          "sample_audit",
          "export_dataset",
          "export_project",
          "import_project",
          "simulate",
          "simulation_report",
          "compare_decisions",
          "set_review_status",
          "plot_progress",
          "read_documentation",
          "create_demo"
        ]
      }
    },
    "beads": {
      "enabled": false,
      "connect_timeout": 60,
      "tool_timeout": 180,
      "command": "${BEADS_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "blocked",
          "claim",
          "close",
          "comment",
          "comments",
          "create",
          "dep",
          "list",
          "note",
          "ready",
          "reopen",
          "show",
          "stats",
          "update"
        ]
      }
    },
    "dolt": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 180,
      "command": "${DOLT_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "add_dolt_test",
          "alter_table",
          "create_dolt_branch",
          "create_dolt_branch_from_head",
          "create_dolt_commit",
          "create_table",
          "describe_table",
          "exec",
          "get_dolt_merge_status",
          "list_dolt_branches",
          "list_dolt_commits",
          "list_dolt_diff_changes_by_table_name",
          "list_dolt_diff_changes_in_date_range",
          "list_dolt_diff_changes_in_working_set",
          "list_dolt_remotes",
          "merge_dolt_branch",
          "merge_dolt_branch_no_fast_forward",
          "move_dolt_branch",
          "query",
          "remove_dolt_test",
          "run_dolt_tests",
          "select_active_branch",
          "select_version",
          "show_create_table",
          "show_tables",
          "stage_all_tables_for_dolt_commit",
          "stage_table_for_dolt_commit",
          "unstage_all_tables",
          "unstage_table"
        ]
      }
    },
    "beads-dolt": {
      "enabled": false,
      "connect_timeout": 45,
      "tool_timeout": 300,
      "command": "${BEADS_DOLT_MCP_COMMAND}",
      "args": [],
      "tools": {
        "include": [
          "service_status",
          "beads_prime",
          "beads_search",
          "memory_set",
          "memory_get",
          "memory_list",
          "issue_history",
          "issue_graph",
          "provenance_record",
          "provenance_list",
          "workflow_templates",
          "workflow_create",
          "beads_export",
          "beads_backup",
          "beads_restore_copy",
          "import_records",
          "export_query",
          "dolt_backup",
          "dolt_restore_copy",
          "link_task_data",
          "read_documentation",
          "merge_preview",
          "merge_resolve"
        ]
      }
    }
  }
}
```
