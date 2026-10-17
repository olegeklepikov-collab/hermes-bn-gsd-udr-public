> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Crossref: profiles.json

Это переносимый шаблон параметров. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "status": {
    "name": "service_status",
    "arguments": {}
  },
  "doi-record": {
    "name": "work_get",
    "arguments": {}
  },
  "doi-current": {
    "name": "work_get",
    "arguments": {
      "refresh": true
    }
  },
  "doi-exists": {
    "name": "doi_exists",
    "arguments": {}
  },
  "doi-agency": {
    "name": "doi_agency",
    "arguments": {}
  },
  "doi-batch": {
    "name": "works_batch",
    "arguments": {}
  },
  "bibliographic-match": {
    "name": "bibliographic_match",
    "arguments": {}
  },
  "general-search": {
    "name": "works_search",
    "arguments": {}
  },
  "title-author-year": {
    "name": "bibliographic_match",
    "arguments": {
      "rows": 5
    },
    "required_inputs": [
      "citation"
    ],
    "purpose": "Поиск кандидатов по названию, авторам и году; проверка данных, а не автоматическое принятие первого результата"
  },
  "journal-articles": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:journal-article"
      ]
    }
  },
  "books": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:book"
      ]
    }
  },
  "book-chapters": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:book-chapter"
      ]
    }
  },
  "conference-papers": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:proceedings-article"
      ]
    }
  },
  "reports": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:report"
      ]
    }
  },
  "dissertations": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:dissertation"
      ]
    }
  },
  "preprints": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:posted-content"
      ]
    }
  },
  "datasets": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:dataset"
      ]
    }
  },
  "grants": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:grant"
      ]
    }
  },
  "standards": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:standard"
      ]
    }
  },
  "peer-reviews": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "type:peer-review"
      ]
    }
  },
  "recent-publications": {
    "name": "works_search",
    "arguments": {
      "sort": "published",
      "order": "desc"
    }
  },
  "recent-deposits": {
    "name": "works_search",
    "arguments": {
      "sort": "deposited",
      "order": "desc"
    }
  },
  "created-window": {
    "name": "works_search",
    "arguments": {
      "rows": 10
    },
    "filter_templates": [
      "from-created-date:{from_date}",
      "until-created-date:{until_date}"
    ]
  },
  "index-window": {
    "name": "works_search",
    "arguments": {
      "rows": 10,
      "sort": "indexed",
      "order": "asc"
    },
    "filter_templates": [
      "from-index-date:{from_date}",
      "until-index-date:{until_date}"
    ]
  },
  "cursor-page": {
    "name": "works_search",
    "arguments": {
      "cursor": "*",
      "rows": 100
    }
  },
  "journal-works": {
    "name": "works_search",
    "arguments": {
      "scope": "journals"
    }
  },
  "publisher-member-works": {
    "name": "works_search",
    "arguments": {
      "scope": "members"
    }
  },
  "funder-works": {
    "name": "works_search",
    "arguments": {
      "scope": "funders"
    }
  },
  "prefix-works": {
    "name": "works_search",
    "arguments": {
      "scope": "prefixes"
    }
  },
  "type-works": {
    "name": "works_search",
    "arguments": {
      "scope": "types"
    }
  },
  "with-abstracts": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-abstract:true"
      ]
    }
  },
  "with-tdm-links": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-full-text:true",
        "full-text.application:text-mining"
      ]
    }
  },
  "with-orcid": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-orcid:true"
      ]
    }
  },
  "with-affiliations": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-affiliation:true"
      ]
    }
  },
  "with-funding": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-funder:true"
      ]
    }
  },
  "grant-number-search": {
    "name": "works_search",
    "arguments": {},
    "filter_templates": [
      "award.number:{award_number}"
    ]
  },
  "outbound-references": {
    "name": "work_references",
    "arguments": {
      "limit": 25
    }
  },
  "typed-relations": {
    "name": "work_relations",
    "arguments": {}
  },
  "preprint-relations": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "relation.type:is-preprint-of"
      ]
    }
  },
  "dataset-relations": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "relation.type:is-supplemented-by"
      ]
    }
  },
  "related-to-doi": {
    "name": "works_search",
    "arguments": {},
    "filter_templates": [
      "relation.object:{target_doi}"
    ]
  },
  "funding-and-authors": {
    "name": "work_funding",
    "arguments": {}
  },
  "licenses-and-text-links": {
    "name": "work_licenses_links",
    "arguments": {}
  },
  "corrections-and-retractions": {
    "name": "work_updates",
    "arguments": {}
  },
  "retraction-records": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "update-type:retraction"
      ]
    }
  },
  "correction-records": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "update-type:correction"
      ]
    }
  },
  "crossmark-records": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-update-policy:true"
      ]
    }
  },
  "journal-catalog": {
    "name": "entities_search",
    "arguments": {
      "entity": "journals"
    }
  },
  "journal-record": {
    "name": "entity_get",
    "arguments": {
      "entity": "journals"
    }
  },
  "member-catalog": {
    "name": "entities_search",
    "arguments": {
      "entity": "members"
    }
  },
  "member-record": {
    "name": "entity_get",
    "arguments": {
      "entity": "members"
    }
  },
  "funder-catalog": {
    "name": "entities_search",
    "arguments": {
      "entity": "funders"
    }
  },
  "funder-record": {
    "name": "entity_get",
    "arguments": {
      "entity": "funders"
    }
  },
  "prefix-record": {
    "name": "entity_get",
    "arguments": {
      "entity": "prefixes"
    }
  },
  "type-catalog": {
    "name": "entities_search",
    "arguments": {
      "entity": "types"
    }
  },
  "type-record": {
    "name": "entity_get",
    "arguments": {
      "entity": "types"
    }
  },
  "license-catalog": {
    "name": "entities_search",
    "arguments": {
      "entity": "licenses"
    }
  },
  "counts-by-type-year": {
    "name": "works_facets",
    "arguments": {
      "facets": {
        "type-name": "*",
        "published": 20
      }
    }
  },
  "counts-by-publisher": {
    "name": "works_facets",
    "arguments": {
      "facets": {
        "publisher-name": 20
      }
    }
  },
  "counts-by-license": {
    "name": "works_facets",
    "arguments": {
      "facets": {
        "license": 20
      }
    }
  },
  "random-sample": {
    "name": "works_sample",
    "arguments": {
      "sample": 10
    }
  },
  "citation-style-catalog": {
    "name": "citation_styles",
    "arguments": {}
  },
  "export-json": {
    "name": "export_records",
    "arguments": {
      "format": "json"
    }
  },
  "export-csv": {
    "name": "export_records",
    "arguments": {
      "format": "csv"
    }
  },
  "xml-doi": {
    "name": "xml_doi_lookup",
    "arguments": {}
  },
  "xml-bibliographic-match": {
    "name": "xml_citation_match",
    "arguments": {}
  },
  "openurl-doi": {
    "name": "openurl_lookup",
    "arguments": {}
  },
  "openurl-metadata-match": {
    "name": "openurl_lookup",
    "arguments": {}
  },
  "data-citations": {
    "name": "data_citations",
    "arguments": {
      "rows": 20,
      "page": "${PAGE}"
    }
  },
  "dataset-cited-by": {
    "name": "data_citations",
    "arguments": {
      "rows": 20,
      "page": "${PAGE}"
    },
    "required_inputs": [
      "object_id"
    ]
  },
  "publication-datasets": {
    "name": "data_citations",
    "arguments": {
      "rows": 20,
      "page": "${PAGE}"
    },
    "required_inputs": [
      "subject_id"
    ]
  },
  "data-citations-window": {
    "name": "data_citations",
    "arguments": {
      "rows": 20,
      "page": "${PAGE}"
    },
    "required_inputs": [
      "from_created_date",
      "until_created_date"
    ]
  },
  "data-citations-member": {
    "name": "data_citations",
    "arguments": {
      "rows": 20,
      "page": "${PAGE}"
    },
    "required_inputs": [
      "member_id"
    ]
  },
  "transform-csl-json": {
    "name": "metadata_transform",
    "arguments": {
      "format": "csl-json"
    }
  },
  "transform-bibtex": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibtex"
    }
  },
  "transform-ris": {
    "name": "metadata_transform",
    "arguments": {
      "format": "ris"
    }
  },
  "transform-bibliography": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibliography"
    }
  },
  "transform-rdf": {
    "name": "metadata_transform",
    "arguments": {
      "format": "rdf"
    }
  },
  "transform-turtle": {
    "name": "metadata_transform",
    "arguments": {
      "format": "turtle"
    }
  },
  "transform-unixref": {
    "name": "metadata_transform",
    "arguments": {
      "format": "unixref"
    }
  },
  "transform-unixsd": {
    "name": "metadata_transform",
    "arguments": {
      "format": "unixsd"
    }
  },
  "bibliography-apa": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibliography",
      "style": "apa",
      "locale": "${LOCALE}"
    }
  },
  "bibliography-ieee": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibliography",
      "style": "ieee",
      "locale": "${LOCALE}"
    }
  },
  "bibliography-vancouver": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibliography",
      "style": "springer-vancouver",
      "locale": "${LOCALE}"
    },
    "purpose": "Vancouver: вариант Springer из действующего каталога Crossref; фактическое имя springer-vancouver."
  },
  "bibliography-chicago": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibliography",
      "style": "chicago-notes-bibliography",
      "locale": "${LOCALE}"
    }
  },
  "bibliography-gost": {
    "name": "metadata_transform",
    "arguments": {
      "format": "bibliography",
      "style": "gost-r-7-0-5-2008",
      "locale": "${LOCALE}"
    }
  },
  "oai-identify": {
    "name": "oai_discovery",
    "arguments": {
      "verb": "Identify"
    }
  },
  "oai-formats": {
    "name": "oai_discovery",
    "arguments": {
      "verb": "ListMetadataFormats"
    }
  },
  "oai-sets": {
    "name": "oai_discovery",
    "arguments": {
      "verb": "ListSets"
    }
  },
  "oai-identifiers": {
    "name": "oai_discovery",
    "arguments": {
      "verb": "ListIdentifiers"
    }
  },
  "with-license-metadata": {
    "name": "works_search",
    "arguments": {
      "filters": [
        "has-license:true"
      ]
    },
    "purpose": "Есть сведения о лицензии; не все такие лицензии открытые. Проверять URI, версию и дату действия."
  }
}
```
