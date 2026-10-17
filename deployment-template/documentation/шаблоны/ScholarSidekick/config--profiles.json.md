> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# ScholarSidekick: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "cite-apa": {
    "name": "formatCitation",
    "arguments": {
      "style": "apa",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-vancouver": {
    "name": "formatCitation",
    "arguments": {
      "style": "vancouver",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-ama": {
    "name": "formatCitation",
    "arguments": {
      "style": "ama",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-ieee": {
    "name": "formatCitation",
    "arguments": {
      "style": "ieee",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-cse": {
    "name": "formatCitation",
    "arguments": {
      "style": "cse",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-chicago-author-date": {
    "name": "formatCitation",
    "arguments": {
      "style": "chicago-author-date",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-chicago-note-bibliography": {
    "name": "formatCitation",
    "arguments": {
      "style": "chicago-note-bibliography",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-harvard-cite-them-right": {
    "name": "formatCitation",
    "arguments": {
      "style": "harvard-cite-them-right",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-modern-language-association": {
    "name": "formatCitation",
    "arguments": {
      "style": "modern-language-association",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-nature": {
    "name": "formatCitation",
    "arguments": {
      "style": "nature",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-the-lancet": {
    "name": "formatCitation",
    "arguments": {
      "style": "the-lancet",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-american-chemical-society": {
    "name": "formatCitation",
    "arguments": {
      "style": "american-chemical-society",
      "output": "text",
      "lang": "en-US"
    }
  },
  "cite-gost-r-7-0-5-2008": {
    "name": "formatCitation",
    "arguments": {
      "style": "gost-r-7-0-5-2008",
      "output": "text",
      "lang": "ru-RU"
    }
  },
  "cite-gost-r-7-0-5-2008-numeric": {
    "name": "formatCitation",
    "arguments": {
      "style": "gost-r-7-0-5-2008-numeric",
      "output": "text",
      "lang": "ru-RU"
    }
  },
  "citation-html": {
    "name": "formatCitation",
    "arguments": {
      "style": "apa",
      "output": "html"
    }
  },
  "citation-json": {
    "name": "formatCitation",
    "arguments": {
      "style": "apa",
      "output": "json"
    }
  },
  "chicago-footnotes": {
    "name": "formatCitation",
    "arguments": {
      "style": "chicago-note-bibliography",
      "footnote": true,
      "output": "text"
    }
  },
  "export-bib": {
    "name": "exportCitation",
    "arguments": {
      "format": "bib"
    }
  },
  "export-ris": {
    "name": "exportCitation",
    "arguments": {
      "format": "ris"
    }
  },
  "export-csl": {
    "name": "exportCitation",
    "arguments": {
      "format": "csl"
    }
  },
  "export-endnote-xml": {
    "name": "exportCitation",
    "arguments": {
      "format": "endnote-xml"
    }
  },
  "export-endnote-refer": {
    "name": "exportCitation",
    "arguments": {
      "format": "endnote-refer"
    }
  },
  "export-refworks": {
    "name": "exportCitation",
    "arguments": {
      "format": "refworks"
    }
  },
  "export-medline": {
    "name": "exportCitation",
    "arguments": {
      "format": "medline"
    }
  },
  "export-zotero-rdf": {
    "name": "exportCitation",
    "arguments": {
      "format": "zotero-rdf"
    }
  },
  "export-csv": {
    "name": "exportCitation",
    "arguments": {
      "format": "csv"
    }
  },
  "export-txt": {
    "name": "exportCitation",
    "arguments": {
      "format": "txt",
      "style": "apa"
    }
  },
  "metadata": {
    "name": "resolveIdentifier",
    "arguments": {}
  },
  "verify-reference": {
    "name": "verifyCitation",
    "arguments": {
      "screenWithLlm": false
    }
  },
  "audit-claims": {
    "name": "auditBibliography",
    "arguments": {
      "checks": [
        "retraction"
      ],
      "screenWithLlm": false
    }
  },
  "audit-bibtex": {
    "name": "auditBibliography",
    "arguments": {
      "format": "bibtex",
      "checks": [
        "retraction"
      ],
      "screenWithLlm": false
    }
  },
  "audit-ris": {
    "name": "auditBibliography",
    "arguments": {
      "format": "ris",
      "checks": [
        "retraction"
      ],
      "screenWithLlm": false
    }
  },
  "audit-csl": {
    "name": "auditBibliography",
    "arguments": {
      "format": "csl-json",
      "checks": [
        "retraction"
      ],
      "screenWithLlm": false
    }
  },
  "retraction": {
    "name": "checkRetraction",
    "arguments": {}
  },
  "open-access": {
    "name": "checkOpenAccess",
    "arguments": {}
  },
  "detect-identifiers": {
    "command": "rest",
    "name": "detect",
    "arguments": {}
  },
  "lookup-identifier": {
    "command": "rest",
    "name": "lookup",
    "arguments": {}
  },
  "styles-search": {
    "command": "rest",
    "name": "styles",
    "arguments": {
      "limit": 30
    }
  },
  "stream-apa": {
    "command": "rest",
    "name": "stream",
    "arguments": {
      "style": "apa"
    }
  },
  "format-owned-csl": {
    "command": "rest",
    "name": "format_items",
    "arguments": {
      "style": "apa",
      "output": "text"
    }
  },
  "audit-large-claims": {
    "command": "rest",
    "name": "audit_bibliography",
    "arguments": {
      "kind": "claims",
      "stop_on_error": true
    }
  },
  "audit-raw-references": {
    "command": "rest",
    "name": "audit_bibliography",
    "arguments": {
      "kind": "references",
      "stop_on_error": true
    }
  }
}
```
