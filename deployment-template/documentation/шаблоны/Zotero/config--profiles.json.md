> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Zotero: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "status": {
    "name": "service_status",
    "arguments": {},
    "write": false
  },
  "schema": {
    "name": "schema",
    "arguments": {},
    "write": false
  },
  "item-fields": {
    "name": "schema",
    "arguments": {
      "kind": "itemFields"
    },
    "write": false
  },
  "creator-fields": {
    "name": "schema",
    "arguments": {
      "kind": "creatorFields"
    },
    "write": false
  },
  "journal-template": {
    "name": "item_template",
    "arguments": {
      "item_type": "journalArticle"
    },
    "write": false
  },
  "book-template": {
    "name": "item_template",
    "arguments": {
      "item_type": "book"
    },
    "write": false
  },
  "report-template": {
    "name": "item_template",
    "arguments": {
      "item_type": "report"
    },
    "write": false
  },
  "dataset-template": {
    "name": "item_template",
    "arguments": {
      "item_type": "dataset"
    },
    "write": false
  },
  "webpage-template": {
    "name": "item_template",
    "arguments": {
      "item_type": "webpage"
    },
    "write": false
  },
  "metadata-search": {
    "name": "query_items",
    "arguments": {
      "qmode": "titleCreatorYear",
      "top": true
    },
    "write": false
  },
  "fulltext-search": {
    "name": "query_items",
    "arguments": {
      "qmode": "everything"
    },
    "write": false
  },
  "tag-search": {
    "name": "query_items",
    "arguments": {},
    "write": false
  },
  "collection-search": {
    "name": "query_items",
    "arguments": {},
    "write": false
  },
  "saved-search-results": {
    "name": "query_items",
    "arguments": {},
    "write": false
  },
  "recent-items": {
    "name": "query_items",
    "arguments": {
      "sort": "dateModified",
      "direction": "desc",
      "top": true
    },
    "write": false
  },
  "trash": {
    "name": "query_items",
    "arguments": {
      "trash": true
    },
    "write": false
  },
  "paper-details": {
    "name": "get_item",
    "arguments": {},
    "write": false
  },
  "notes-attachments": {
    "name": "item_children",
    "arguments": {},
    "write": false
  },
  "pdf-annotations": {
    "name": "item_children",
    "arguments": {},
    "write": false
  },
  "collection-tree": {
    "name": "collections",
    "arguments": {
      "top": true
    },
    "write": false
  },
  "all-collections": {
    "name": "collections",
    "arguments": {},
    "write": false
  },
  "tags": {
    "name": "tags",
    "arguments": {},
    "write": false
  },
  "saved-searches": {
    "name": "saved_searches",
    "arguments": {},
    "write": false
  },
  "groups-readonly": {
    "name": "groups",
    "arguments": {},
    "write": false
  },
  "fulltext-slice": {
    "name": "read_fulltext",
    "arguments": {
      "length": 6000
    },
    "write": false
  },
  "fulltext-index-state": {
    "name": "fulltext_versions",
    "arguments": {},
    "write": false
  },
  "pdf-pages": {
    "name": "read_pdf_pages",
    "arguments": {
      "max_characters_per_page": 12000
    },
    "write": false
  },
  "pdf-table-image": {
    "name": "render_pdf_page",
    "arguments": {},
    "write": false
  },
  "attachment-provenance": {
    "name": "attachment_info",
    "arguments": {},
    "write": false
  },
  "paper-create": {
    "name": "create_items",
    "arguments": {},
    "write": true
  },
  "paper-correct": {
    "name": "patch_item",
    "arguments": {},
    "write": true
  },
  "collection-create": {
    "name": "create_collections",
    "arguments": {},
    "write": true
  },
  "collection-reorganize": {
    "name": "patch_collection",
    "arguments": {},
    "write": true
  },
  "search-save": {
    "name": "create_saved_searches",
    "arguments": {},
    "write": true
  },
  "search-update": {
    "name": "patch_saved_search",
    "arguments": {},
    "write": true
  },
  "research-note": {
    "name": "create_note",
    "arguments": {},
    "write": true
  },
  "lawful-pdf-import": {
    "name": "attach_file",
    "arguments": {
      "content_type": "application/pdf"
    },
    "write": true
  },
  "local-report-import": {
    "name": "attach_file",
    "arguments": {},
    "write": true
  },
  "page-highlight": {
    "name": "create_annotation",
    "arguments": {},
    "write": true
  },
  "index-real-text": {
    "name": "index_fulltext",
    "arguments": {},
    "write": true
  },
  "reversible-trash": {
    "name": "trash_item",
    "arguments": {},
    "write": true
  },
  "restore": {
    "name": "restore_item",
    "arguments": {},
    "write": true
  },
  "export-bibtex": {
    "name": "export_items",
    "arguments": {
      "format": "bibtex"
    },
    "write": false
  },
  "export-biblatex": {
    "name": "export_items",
    "arguments": {
      "format": "biblatex"
    },
    "write": false
  },
  "export-bookmarks": {
    "name": "export_items",
    "arguments": {
      "format": "bookmarks"
    },
    "write": false
  },
  "export-coins": {
    "name": "export_items",
    "arguments": {
      "format": "coins"
    },
    "write": false
  },
  "export-csljson": {
    "name": "export_items",
    "arguments": {
      "format": "csljson"
    },
    "write": false
  },
  "export-csv": {
    "name": "export_items",
    "arguments": {
      "format": "csv"
    },
    "write": false
  },
  "export-mods": {
    "name": "export_items",
    "arguments": {
      "format": "mods"
    },
    "write": false
  },
  "export-refer": {
    "name": "export_items",
    "arguments": {
      "format": "refer"
    },
    "write": false
  },
  "export-rdf_bibliontology": {
    "name": "export_items",
    "arguments": {
      "format": "rdf_bibliontology"
    },
    "write": false
  },
  "export-rdf_dc": {
    "name": "export_items",
    "arguments": {
      "format": "rdf_dc"
    },
    "write": false
  },
  "export-rdf_zotero": {
    "name": "export_items",
    "arguments": {
      "format": "rdf_zotero"
    },
    "write": false
  },
  "export-ris": {
    "name": "export_items",
    "arguments": {
      "format": "ris"
    },
    "write": false
  },
  "export-tei": {
    "name": "export_items",
    "arguments": {
      "format": "tei"
    },
    "write": false
  },
  "export-wikipedia": {
    "name": "export_items",
    "arguments": {
      "format": "wikipedia"
    },
    "write": false
  },
  "bibliography-apa": {
    "name": "export_items",
    "arguments": {
      "format": "bib",
      "style": "apa",
      "locale": "${LOCALE}"
    },
    "write": false
  },
  "bibliography-ieee": {
    "name": "export_items",
    "arguments": {
      "format": "bib",
      "style": "ieee",
      "locale": "${LOCALE}"
    },
    "write": false
  },
  "bibliography-vancouver": {
    "name": "export_items",
    "arguments": {
      "format": "bib",
      "style": "vancouver",
      "locale": "${LOCALE}"
    },
    "write": false
  },
  "bibliography-chicago": {
    "name": "export_items",
    "arguments": {
      "format": "bib",
      "style": "chicago-notes-bibliography",
      "locale": "${LOCALE}"
    },
    "write": false
  },
  "bibliography-gost": {
    "name": "export_items",
    "arguments": {
      "format": "bib",
      "style": "gost-r-7-0-5-2008",
      "locale": "${LOCALE}"
    },
    "write": false
  }
}
```
