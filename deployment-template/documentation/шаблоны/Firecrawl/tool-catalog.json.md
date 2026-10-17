> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Firecrawl: tool-catalog.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "mcp__firecrawl__firecrawl_scrape": {
    "name": "mcp__firecrawl__firecrawl_scrape",
    "description": "\nScrape one URL and return its content: markdown by default, or HTML, links, screenshots, branding data, a targeted answer, or JSON matching a supplied schema. Use it when the request identifies a page and needs its content or defined fields. Use `firecrawl_search` when additional web sources are needed; on an authenticated session, `firecrawl_map` lists a site's URLs and `firecrawl_crawl` collects a set of pages.\n\nFirecrawl may serve recently indexed content; set `maxAge: 0` for a live fetch or a smaller `maxAge` to bound staleness. A successful response does not by itself confirm the page is still current. Browser actions can change the live page when interactive actions are enabled. Authenticated responses can include a `metadata.scrapeId` for optional scrape feedback.\n\nOn an authenticated session with Alexandria access, `firecrawl_search` with `sources` unset and `firecrawl_find_tools` can discover providers for the same fields across several pages; a matching provider returns typed records in one call. Keyless sessions have no provider matches.\n\nAlexandria mode, on an authenticated session with Alexandria access: `alexandria` selects catalogued capability execution and is mutually exclusive with `url`.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "format": "uri"
        },
        "formats": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "markdown",
              "html",
              "rawHtml",
              "screenshot",
              "links",
              "summary",
              "changeTracking",
              "branding",
              "json",
              "query",
              "audio"
            ]
          }
        },
        "jsonOptions": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string"
            },
            "schema": {
              "type": "object",
              "propertyNames": {
                "type": "string"
              },
              "additionalProperties": false,
              "properties": {},
              "required": []
            }
          },
          "additionalProperties": false,
          "required": []
        },
        "queryOptions": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string",
              "maxLength": 10000
            },
            "mode": {
              "default": "freeform",
              "type": "string",
              "enum": [
                "directQuote",
                "freeform"
              ]
            }
          },
          "required": [
            "prompt"
          ],
          "additionalProperties": false
        },
        "screenshotOptions": {
          "type": "object",
          "properties": {
            "fullPage": {
              "type": "boolean"
            },
            "quality": {
              "type": "number"
            },
            "viewport": {
              "type": "object",
              "properties": {
                "width": {
                  "type": "number"
                },
                "height": {
                  "type": "number"
                }
              },
              "required": [
                "width",
                "height"
              ],
              "additionalProperties": false
            }
          },
          "additionalProperties": false,
          "required": []
        },
        "parsers": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "pdf"
            ]
          }
        },
        "pdfOptions": {
          "type": "object",
          "properties": {
            "maxPages": {
              "type": "integer",
              "minimum": 1,
              "maximum": 10000
            }
          },
          "additionalProperties": false,
          "required": []
        },
        "onlyMainContent": {
          "type": "boolean"
        },
        "redactPII": {
          "type": "boolean"
        },
        "includeTags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeTags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "waitFor": {
          "type": "number"
        },
        "mobile": {
          "type": "boolean"
        },
        "skipTlsVerification": {
          "type": "boolean"
        },
        "removeBase64Images": {
          "type": "boolean"
        },
        "location": {
          "type": "object",
          "properties": {
            "country": {
              "type": "string"
            },
            "languages": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "additionalProperties": false,
          "required": []
        },
        "storeInCache": {
          "type": "boolean"
        },
        "zeroDataRetention": {
          "type": "boolean"
        },
        "maxAge": {
          "type": "number"
        },
        "lockdown": {
          "type": "boolean"
        },
        "proxy": {
          "type": "string",
          "enum": [
            "basic",
            "stealth",
            "enhanced",
            "auto"
          ]
        },
        "profile": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "saveChanges": {
              "type": "boolean"
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        },
        "timeout": {
          "description": "Execution timeout in milliseconds.",
          "type": "integer",
          "exclusiveMinimum": 0,
          "maximum": 9007199254740991
        },
        "requestId": {
          "description": "Idempotency key bound to one Alexandria execution payload. Generated when omitted and returned with the result.",
          "type": "string",
          "pattern": "^[A-Za-z0-9._:-]{1,128}$"
        },
        "alexandria": {
          "description": "Catalogued Alexandria capability invocation, mutually exclusive with url. One {provider, capability, options} object or an array of 1-10, with contracts available through firecrawl_search or firecrawl_find_tools. Each call may include version to pin a published workflow; omitting it uses latest. Only requestId and timeout are supported alongside alexandria. The selected contract marks required inputs and any requiresOneOf groups (at least one member per group); it may include example.request/example.response and response.key (which may differ from records). Where pagination is declared, its fields govern paging with the same filters; catalogue next is separate from provider pagination. Returns per-capability results in data.alexandria with data, records, or an error with a code; individual capabilities can fail even when the outer response succeeds. Requires an API key on a team with Alexandria enabled. Some providers require accepted terms; blocked requests return the applicable requirements.",
          "anyOf": [
            {
              "type": "object",
              "properties": {
                "provider": {
                  "description": "Provider slug, e.g. \"fred\".",
                  "type": "string",
                  "minLength": 1
                },
                "capability": {
                  "description": "Capability address as returned by search or discover, e.g. \"series/observations\".",
                  "type": "string",
                  "minLength": 1
                },
                "version": {
                  "description": "Optional published workflow version. Omit to use the latest version.",
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 128
                },
                "options": {
                  "description": "Capability options as declared by its contract.",
                  "type": "object",
                  "propertyNames": {
                    "type": "string"
                  },
                  "additionalProperties": {},
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "provider",
                "capability"
              ]
            },
            {
              "minItems": 1,
              "maxItems": 10,
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "provider": {
                    "description": "Provider slug, e.g. \"fred\".",
                    "type": "string",
                    "minLength": 1
                  },
                  "capability": {
                    "description": "Capability address as returned by search or discover, e.g. \"series/observations\".",
                    "type": "string",
                    "minLength": 1
                  },
                  "version": {
                    "description": "Optional published workflow version. Omit to use the latest version.",
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 128
                  },
                  "options": {
                    "description": "Capability options as declared by its contract.",
                    "type": "object",
                    "propertyNames": {
                      "type": "string"
                    },
                    "additionalProperties": {},
                    "properties": {},
                    "required": []
                  }
                },
                "required": [
                  "provider",
                  "capability"
                ]
              }
            }
          ]
        },
        "toolDetail": {
          "description": "URL mode only: domain discovery detail, summary by default; compact returns provider/capability/description, full includes contracts. Ignored with alexandria.",
          "type": "string",
          "enum": [
            "compact",
            "summary",
            "full"
          ]
        },
        "domainTools": {
          "description": "URL mode only: include domain-matched Alexandria tools for the page in tools on the returned document. Ignored with alexandria.",
          "type": "boolean"
        }
      },
      "additionalProperties": false,
      "required": []
    }
  },
  "mcp__firecrawl__firecrawl_map": {
    "name": "mcp__firecrawl__firecrawl_map",
    "description": "\nEnumerate URLs indexed under one website through Firecrawl without fetching each page's content. Use this when the request asks for a site's URL inventory, when several relevant pages must be located, or when the desired page URL is unknown. An optional `search` term narrows the URL list, while sitemap, subdomain, query-parameter, and result-limit options control coverage.\n\nReturns matching URLs rather than page bodies. Retrieve one page with `firecrawl_scrape`; collect content across multiple pages with `firecrawl_crawl`. Authenticated responses can include an `id` for optional map feedback.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "format": "uri"
        },
        "search": {
          "type": "string"
        },
        "sitemap": {
          "type": "string",
          "enum": [
            "include",
            "skip",
            "only"
          ]
        },
        "includeSubdomains": {
          "type": "boolean"
        },
        "limit": {
          "type": "number"
        },
        "ignoreQueryParameters": {
          "type": "boolean"
        }
      },
      "required": [
        "url"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_search": {
    "name": "mcp__firecrawl__firecrawl_search",
    "description": "\nSearch web, news, or image sources and return ranked results with query-relevant highlights. Each web result is a title, URL, and description; use `firecrawl_scrape` on a result URL when the excerpt is not enough.\n\nAuthenticated search also returns matching Alexandria data providers in data.tools (companies, people, jobs, finance and filings, public records and government spending, real estate, places and restaurants, retail and prices, package registries and developer data, news, research, and more). Prefer a provider over scraping pages when the task needs the same fields across several entities, exact figures or timestamps, provenance, or many records; use web results when they already answer the question. A search with sources: [\"web\"] omits semantic provider discovery; domainTools: true can still return website-matched tools. Web-only results use domainTools: false.\n\nOn an authenticated session, tool matches describe available capabilities; `firecrawl_find_tools` returns their contracts and `firecrawl_scrape` with an `alexandria` body executes a selected capability. Keyless sessions get no Alexandria matches in data.tools.\n\nFor a programming question, add `categories: [\"developer\"]`; its hits return in `data.web` with `category: \"developer\"`. `categories: [\"research\"]` restricts web results to research-affiliated websites; the `firecrawl_research_*` tools are a separate surface over paper abstracts and full text (PubMed, bioRxiv, medRxiv, arXiv). Query operators, domain filters, `categories`, `toolDetail` and `scrapeOptions` are described on their parameters. Returns source-type result groups and usage metadata. Authenticated responses can include an `id` for optional search feedback.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "toolDetail": {
          "description": "Compact by default. Compact returns only provider, capability and description; full includes contracts. Inspect selected compact tools with firecrawl_find_tools providers and capabilities.",
          "type": "string",
          "enum": [
            "compact",
            "summary",
            "full"
          ]
        },
        "query": {
          "description": "Query for web and semantic tool discovery. Operators include quoted phrases, `-term`, `site:host`, `inurl:term`, `intitle:term`, and `related:host`; the set is non-exhaustive. Catalogue browsing is available through firecrawl_find_tools.",
          "type": "string",
          "minLength": 1
        },
        "objective": {
          "description": "Optional broader goal for this search, if known. Avoid sensitive information.",
          "type": "string",
          "minLength": 1,
          "maxLength": 5000
        },
        "clientModel": {
          "description": "Optional model identifier, if known.",
          "type": "string",
          "minLength": 1,
          "maxLength": 128
        },
        "domainTools": {
          "description": "Include domain-matched tools for result URLs. Defaults to true when Alexandria is combined with web, news or images; semantic-only search leaves domain matching off.",
          "type": "boolean"
        },
        "highlights": {
          "description": "Return query-relevant page excerpts for web and news results when available (default). Highlights appear in web `description` and news `snippet`; otherwise, original snippets are returned. Set to false to keep the original search snippets.",
          "type": "boolean"
        },
        "limit": {
          "type": "integer",
          "minimum": 1,
          "maximum": 100
        },
        "tbs": {
          "type": "string"
        },
        "filter": {
          "type": "string"
        },
        "location": {
          "type": "string"
        },
        "includeDomains": {
          "description": "Hostnames to restrict results to. Mutually exclusive with excludeDomains.",
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1,
            "maxLength": 253,
            "pattern": "^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$"
          }
        },
        "excludeDomains": {
          "description": "Hostnames to leave out of results. Mutually exclusive with includeDomains.",
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1,
            "maxLength": 253,
            "pattern": "^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$"
          }
        },
        "sources": {
          "description": "Search sources; authenticated sessions default to web + alexandria, keyless sessions to web only. A search with sources: [\"web\"] omits semantic provider discovery; domainTools: true can still return website-matched tools. Web-only results use domainTools: false. Use [\"alexandria\"] alone for provider discovery without web results.",
          "type": "array",
          "items": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "web",
                  "images",
                  "news",
                  "alexandria",
                  "exchange"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "web",
                      "images",
                      "news",
                      "alexandria",
                      "exchange"
                    ]
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              }
            ]
          }
        },
        "categories": {
          "description": "Limit results to specific source types. `research` restricts ordinary web results to research-affiliated websites and returns page snippets, which is separate from the `firecrawl_research_*` tools that search paper abstracts and full text across biomedical (PubMed, bioRxiv, medRxiv) and arXiv literature; `pdf` searches PDF results; `developer` searches an index built for coding agents over public repositories, GitHub issues, merged pull requests, repository READMEs, and code documentation. `developer` returns hits in `data.web` with `category: \"developer\"`; the other categories also filter `data.web`.",
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "research",
              "pdf",
              "developer"
            ]
          }
        },
        "enterprise": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "default",
              "anon",
              "zdr"
            ]
          }
        },
        "scrapeOptions": {
          "description": "Attach page content for web results in the same call. These fetches ignore maxAge, so use firecrawl_scrape when you need a live fetch. scrapeOptions fetches web pages, never Alexandria provider tools.",
          "type": "object",
          "properties": {
            "formats": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "markdown",
                  "html",
                  "rawHtml",
                  "screenshot",
                  "links",
                  "summary",
                  "changeTracking",
                  "branding",
                  "json",
                  "query",
                  "audio"
                ]
              }
            },
            "jsonOptions": {
              "type": "object",
              "properties": {
                "prompt": {
                  "type": "string"
                },
                "schema": {
                  "type": "object",
                  "propertyNames": {
                    "type": "string"
                  },
                  "additionalProperties": false,
                  "properties": {},
                  "required": []
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "queryOptions": {
              "type": "object",
              "properties": {
                "prompt": {
                  "type": "string",
                  "maxLength": 10000
                },
                "mode": {
                  "default": "freeform",
                  "type": "string",
                  "enum": [
                    "directQuote",
                    "freeform"
                  ]
                }
              },
              "required": [
                "prompt"
              ],
              "additionalProperties": false
            },
            "screenshotOptions": {
              "type": "object",
              "properties": {
                "fullPage": {
                  "type": "boolean"
                },
                "quality": {
                  "type": "number"
                },
                "viewport": {
                  "type": "object",
                  "properties": {
                    "width": {
                      "type": "number"
                    },
                    "height": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "width",
                    "height"
                  ],
                  "additionalProperties": false
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "parsers": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "pdf"
                ]
              }
            },
            "pdfOptions": {
              "type": "object",
              "properties": {
                "maxPages": {
                  "type": "integer",
                  "minimum": 1,
                  "maximum": 10000
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "onlyMainContent": {
              "type": "boolean"
            },
            "redactPII": {
              "type": "boolean"
            },
            "includeTags": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "excludeTags": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "waitFor": {
              "type": "number"
            },
            "mobile": {
              "type": "boolean"
            },
            "skipTlsVerification": {
              "type": "boolean"
            },
            "removeBase64Images": {
              "type": "boolean"
            },
            "location": {
              "type": "object",
              "properties": {
                "country": {
                  "type": "string"
                },
                "languages": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "storeInCache": {
              "type": "boolean"
            },
            "zeroDataRetention": {
              "type": "boolean"
            },
            "maxAge": {
              "type": "number"
            },
            "lockdown": {
              "type": "boolean"
            },
            "proxy": {
              "type": "string",
              "enum": [
                "basic",
                "stealth",
                "enhanced",
                "auto"
              ]
            },
            "profile": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "saveChanges": {
                  "type": "boolean"
                }
              },
              "required": [
                "name"
              ],
              "additionalProperties": false
            }
          },
          "additionalProperties": false,
          "required": []
        }
      },
      "required": [
        "query"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_find_tools": {
    "name": "mcp__firecrawl__firecrawl_find_tools",
    "description": "Browse Alexandria data providers and workflows or read a selected contract. Alexandria covers companies, people, jobs, finance and filings, public records and government spending, real estate, places and restaurants, retail and prices, package registries and developer data, news, research, and more: typed, sourced records through published contracts. Prefer normal firecrawl_search for a data task; it already returns matching providers. Use this tool when the contract you need was not returned in full, to browse a category when search found nothing, or before scraping the same fields from several pages. Discovery is free. Use query for semantic discovery or urls to find providers for a website. With no arguments, browse categories, then providers and tools. Contracts describe the inputs and outputs for execution through firecrawl_scrape. nextTool identifies further discovery or pagination. Discovery does not execute providers. Use firecrawl_search when you also need web results.",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "query": {
          "description": "Semantic lookup of tools for the data you need. Selectors constrain the search.",
          "type": "string",
          "minLength": 1,
          "maxLength": 2000
        },
        "urls": {
          "minItems": 1,
          "maxItems": 100,
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^https?:\\/\\/"
          }
        },
        "providers": {
          "description": "Provider IDs returned by category browsing. Lists compact tools by default.",
          "minItems": 1,
          "maxItems": 50,
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "categories": {
          "description": "Category IDs returned by an empty call. Lists providers by default.",
          "minItems": 1,
          "maxItems": 50,
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "groups": {
          "description": "Optional group IDs for explicit group browsing.",
          "minItems": 1,
          "maxItems": 50,
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "capabilities": {
          "description": "Exact capability IDs. A selected capability expands its complete contract by default.",
          "minItems": 1,
          "maxItems": 50,
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "level": {
          "type": "string",
          "enum": [
            "categories",
            "providers",
            "groups",
            "tools"
          ]
        },
        "expand": {
          "description": "Use [\"options\", \"response\"] for inputs and output shape without example payloads; [] keeps results compact. Omit for full contracts on selected capabilities.",
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "options",
              "response",
              "examples"
            ]
          }
        },
        "limit": {
          "type": "integer",
          "minimum": 1,
          "maximum": 100
        },
        "offset": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        }
      },
      "additionalProperties": false,
      "required": []
    }
  },
  "mcp__firecrawl__firecrawl_crawl": {
    "name": "mcp__firecrawl__firecrawl_crawl",
    "description": "\nStart a multi-page crawl at a website URL, poll it to a terminal state, and return the final status and collected data. Scope can be bounded with include/exclude paths, depth, page limit, subdomain/external-link controls, sitemap handling, delay, and scrape options.\n\nCrawl results can be large; use conservative limits when full-site coverage is unnecessary. Webhooks and interactive scrape actions are unavailable in safe mode. Returns the crawl ID, status, and page data.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "prompt": {
          "type": "string"
        },
        "excludePaths": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includePaths": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "maxDiscoveryDepth": {
          "type": "number"
        },
        "sitemap": {
          "type": "string",
          "enum": [
            "skip",
            "include",
            "only"
          ]
        },
        "limit": {
          "type": "number"
        },
        "allowExternalLinks": {
          "type": "boolean"
        },
        "allowSubdomains": {
          "type": "boolean"
        },
        "crawlEntireDomain": {
          "type": "boolean"
        },
        "delay": {
          "type": "number"
        },
        "maxConcurrency": {
          "type": "number"
        },
        "deduplicateSimilarURLs": {
          "type": "boolean"
        },
        "ignoreQueryParameters": {
          "type": "boolean"
        },
        "scrapeOptions": {
          "type": "object",
          "properties": {
            "formats": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "markdown",
                  "html",
                  "rawHtml",
                  "screenshot",
                  "links",
                  "summary",
                  "changeTracking",
                  "branding",
                  "json",
                  "query",
                  "audio"
                ]
              }
            },
            "jsonOptions": {
              "type": "object",
              "properties": {
                "prompt": {
                  "type": "string"
                },
                "schema": {
                  "type": "object",
                  "propertyNames": {
                    "type": "string"
                  },
                  "additionalProperties": false,
                  "properties": {},
                  "required": []
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "queryOptions": {
              "type": "object",
              "properties": {
                "prompt": {
                  "type": "string",
                  "maxLength": 10000
                },
                "mode": {
                  "default": "freeform",
                  "type": "string",
                  "enum": [
                    "directQuote",
                    "freeform"
                  ]
                }
              },
              "required": [
                "prompt"
              ],
              "additionalProperties": false
            },
            "screenshotOptions": {
              "type": "object",
              "properties": {
                "fullPage": {
                  "type": "boolean"
                },
                "quality": {
                  "type": "number"
                },
                "viewport": {
                  "type": "object",
                  "properties": {
                    "width": {
                      "type": "number"
                    },
                    "height": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "width",
                    "height"
                  ],
                  "additionalProperties": false
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "parsers": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "pdf"
                ]
              }
            },
            "pdfOptions": {
              "type": "object",
              "properties": {
                "maxPages": {
                  "type": "integer",
                  "minimum": 1,
                  "maximum": 10000
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "onlyMainContent": {
              "type": "boolean"
            },
            "redactPII": {
              "type": "boolean"
            },
            "includeTags": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "excludeTags": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "waitFor": {
              "type": "number"
            },
            "mobile": {
              "type": "boolean"
            },
            "skipTlsVerification": {
              "type": "boolean"
            },
            "removeBase64Images": {
              "type": "boolean"
            },
            "location": {
              "type": "object",
              "properties": {
                "country": {
                  "type": "string"
                },
                "languages": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "storeInCache": {
              "type": "boolean"
            },
            "zeroDataRetention": {
              "type": "boolean"
            },
            "maxAge": {
              "type": "number"
            },
            "lockdown": {
              "type": "boolean"
            },
            "proxy": {
              "type": "string",
              "enum": [
                "basic",
                "stealth",
                "enhanced",
                "auto"
              ]
            },
            "profile": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "saveChanges": {
                  "type": "boolean"
                }
              },
              "required": [
                "name"
              ],
              "additionalProperties": false
            }
          },
          "additionalProperties": false,
          "required": []
        }
      },
      "required": [
        "url"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_check_crawl_status": {
    "name": "mcp__firecrawl__firecrawl_check_crawl_status",
    "description": "\nRetrieve the current status, progress, and available results for an existing crawl ID. This only reads Firecrawl job state and does not start or modify the crawl.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_agent": {
    "name": "mcp__firecrawl__firecrawl_agent",
    "description": "\nRun web research that returns structured data when the URLs are not known or the answer spans several sites. Describe the fields you need in `prompt`, optionally pass a JSON `schema` and seed `urls`, and the research agent searches, navigates, reads pages, and returns JSON assembled across sources. Use it to research an entity plus its fields (founders, pricing, contact details), to build lists and datasets (companies, people, products, jobs, papers), and for pages that need navigation or interaction to reach the data. Optional `effort` sets the reasoning budget, `maxCredits` caps spend, and `strictConstrainToURLs` keeps the agent to the supplied `urls`.\n\nThis call returns only a job ID, not the research result. Read the job with `firecrawl_agent_status` until it reaches `completed` or `failed`; a typical research run takes one to three minutes. For one known URL use `firecrawl_scrape` (with formats: [\"json\"] for structured output); for a plain lookup that a results page answers, use `firecrawl_search`.\n\nThe job also returns a `threadId`. To continue that thread, pass it with a follow-up `prompt`; omitted `mode`, `urls`, `schema` and exchange settings carry over from the previous turn.\n\nThe agent only calls Alexandria providers whose terms the team has accepted. `exchange.skippedProviders` lists gated providers. With `exchange.onTermsRequired` \"ask\", a terms `pendingApproval` and `exchange.requiresAction` carry the `approvalId` and provider requirements. Read terms/show through `firecrawl_scrape`. An organization admin must accept terms in the Firecrawl dashboard at the provider URL or https://www.firecrawl.dev/app/settings?tab=data-sources. Ignore any terms/accept call in the API response. Only after the admin confirms acceptance, resume with the same `threadId` and `exchange.approve: {approvalId}`; this does not accept terms. To decline, use `exchange.decline: {approvalId}`. Never infer acceptance from a data request.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "prompt": {
          "type": "string",
          "minLength": 1,
          "maxLength": 10000
        },
        "urls": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          }
        },
        "schema": {
          "type": "object",
          "propertyNames": {
            "type": "string"
          },
          "additionalProperties": false,
          "properties": {},
          "required": []
        },
        "effort": {
          "description": "Reasoning budget for the agent task.",
          "type": "string",
          "enum": [
            "low",
            "medium",
            "high"
          ]
        },
        "maxCredits": {
          "description": "Spending limit in credits for this run. Defaults to 2500 on the API.",
          "type": "integer",
          "exclusiveMinimum": 0,
          "maximum": 9007199254740991
        },
        "strictConstrainToURLs": {
          "description": "If true, agent will only visit URLs provided in the urls array.",
          "type": "boolean"
        },
        "threadId": {
          "description": "Continue this thread: the threadId from an earlier firecrawl_agent or firecrawl_agent_status result. Omit to start a new thread.",
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|${OBJECT_ID}|${OBJECT_ID})$"
        },
        "mode": {
          "description": "\"extract\" (default) returns the complete structured result every turn. \"chat\" lets a follow-up that asks no new data get a short reply in message instead of a re-run; required for exchange.requireApproval. Omitted on a follow-up keeps the previous turn's mode.",
          "type": "string",
          "enum": [
            "extract",
            "chat"
          ]
        },
        "exchange": {
          "description": "Alexandria provider settings for this turn, forwarded as the request's exchange object.",
          "type": "object",
          "properties": {
            "enabled": {
              "description": "Let the agent call Alexandria providers. On by default.",
              "type": "boolean"
            },
            "toolkits": {
              "description": "Pin up to 5 providers the agent may use, by slug. Omitted means the whole catalog.",
              "maxItems": 5,
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "maxCalls": {
              "description": "Most provider calls the agent may make in this turn.",
              "type": "integer",
              "minimum": 1,
              "maximum": 30
            },
            "requireApproval": {
              "description": "End the turn with a paid-call pendingApproval before any paid provider call. Requires mode \"chat\" on the same request, even on a follow-up.",
              "type": "boolean"
            },
            "approve": {
              "description": "Answer yes to the pendingApproval the previous turn of this thread ended on (its id, also exchange.requiresAction.approvalId). Needs threadId. For a terms offer, send it only after an organization admin confirms acceptance in the Firecrawl dashboard; this does not accept terms. callIds and always are ignored on terms offers. For paid calls, callIds picks a subset (default all) and always stops asking for the rest of the thread.",
              "type": "object",
              "properties": {
                "approvalId": {
                  "type": "string",
                  "format": "uuid",
                  "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|${OBJECT_ID}|${OBJECT_ID})$"
                },
                "callIds": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "always": {
                  "type": "boolean"
                }
              },
              "required": [
                "approvalId"
              ],
              "additionalProperties": false
            },
            "decline": {
              "description": "Answer no to that pendingApproval. Needs threadId. A declined terms offer keeps those providers out of the rest of the thread.",
              "type": "object",
              "properties": {
                "approvalId": {
                  "type": "string",
                  "format": "uuid",
                  "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|${OBJECT_ID}|${OBJECT_ID})$"
                }
              },
              "required": [
                "approvalId"
              ],
              "additionalProperties": false
            },
            "onTermsRequired": {
              "description": "What to do when a provider the agent would use needs data terms the team has not accepted. Gated providers are never called. \"skip\" (default): answer with accepted providers and list the rest in exchange.skippedProviders. \"ask\": the same, plus a terms pendingApproval and exchange.requiresAction. Read terms with terms/show; an organization admin accepts them in the Firecrawl dashboard. There is no auto-accept. Omitted on a follow-up keeps the previous turn's value.",
              "type": "string",
              "enum": [
                "skip",
                "ask"
              ]
            }
          },
          "additionalProperties": false,
          "required": []
        }
      },
      "required": [
        "prompt"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_agent_status": {
    "name": "mcp__firecrawl__firecrawl_agent_status",
    "description": "\nRetrieve progress or final results for a `firecrawl_agent` job ID. A `processing` response is non-terminal and does not contain the final research result. Check again after 15–30 seconds until the status is `completed` or `failed`; a typical research run takes one to three minutes and complex jobs can take longer. If the job cannot finish within the task's available time, use `firecrawl_search` and `firecrawl_scrape` to complete the requested output.\n\nReturns job status, progress information, and result data when completed.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_interact": {
    "name": "mcp__firecrawl__firecrawl_interact",
    "description": "\nOpen or reuse a live browser session to navigate a page, click controls, fill fields, or run browser code. Provide either `url` or `scrapeId`, and either a natural-language `prompt` or executable `code`; code can run as Bash, Python, or Node with a bounded timeout.\n\nThis acts on the live site, so actions such as form submission can create persistent external side effects. Returns execution output, stdout/stderr, exit status, and session viewing URLs.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "scrapeId": {
          "type": "string",
          "minLength": 1
        },
        "url": {
          "type": "string",
          "format": "uri"
        },
        "prompt": {
          "type": "string",
          "minLength": 1
        },
        "code": {
          "type": "string",
          "minLength": 1
        },
        "language": {
          "type": "string",
          "enum": [
            "bash",
            "python",
            "node"
          ]
        },
        "timeout": {
          "type": "number",
          "minimum": 1,
          "maximum": 300
        },
        "scrapeOptions": {
          "type": "object",
          "properties": {
            "formats": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "markdown",
                  "html",
                  "rawHtml",
                  "screenshot",
                  "links",
                  "summary",
                  "changeTracking",
                  "branding",
                  "json",
                  "query",
                  "audio"
                ]
              }
            },
            "jsonOptions": {
              "type": "object",
              "properties": {
                "prompt": {
                  "type": "string"
                },
                "schema": {
                  "type": "object",
                  "propertyNames": {
                    "type": "string"
                  },
                  "additionalProperties": false,
                  "properties": {},
                  "required": []
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "queryOptions": {
              "type": "object",
              "properties": {
                "prompt": {
                  "type": "string",
                  "maxLength": 10000
                },
                "mode": {
                  "default": "freeform",
                  "type": "string",
                  "enum": [
                    "directQuote",
                    "freeform"
                  ]
                }
              },
              "required": [
                "prompt"
              ],
              "additionalProperties": false
            },
            "screenshotOptions": {
              "type": "object",
              "properties": {
                "fullPage": {
                  "type": "boolean"
                },
                "quality": {
                  "type": "number"
                },
                "viewport": {
                  "type": "object",
                  "properties": {
                    "width": {
                      "type": "number"
                    },
                    "height": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "width",
                    "height"
                  ],
                  "additionalProperties": false
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "parsers": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "pdf"
                ]
              }
            },
            "pdfOptions": {
              "type": "object",
              "properties": {
                "maxPages": {
                  "type": "integer",
                  "minimum": 1,
                  "maximum": 10000
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "onlyMainContent": {
              "type": "boolean"
            },
            "redactPII": {
              "type": "boolean"
            },
            "includeTags": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "excludeTags": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "waitFor": {
              "type": "number"
            },
            "mobile": {
              "type": "boolean"
            },
            "skipTlsVerification": {
              "type": "boolean"
            },
            "removeBase64Images": {
              "type": "boolean"
            },
            "location": {
              "type": "object",
              "properties": {
                "country": {
                  "type": "string"
                },
                "languages": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "additionalProperties": false,
              "required": []
            },
            "storeInCache": {
              "type": "boolean"
            },
            "zeroDataRetention": {
              "type": "boolean"
            },
            "maxAge": {
              "type": "number"
            },
            "lockdown": {
              "type": "boolean"
            },
            "proxy": {
              "type": "string",
              "enum": [
                "basic",
                "stealth",
                "enhanced",
                "auto"
              ]
            },
            "profile": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "saveChanges": {
                  "type": "boolean"
                }
              },
              "required": [
                "name"
              ],
              "additionalProperties": false
            }
          },
          "additionalProperties": false,
          "required": []
        }
      },
      "additionalProperties": false,
      "required": []
    }
  },
  "mcp__firecrawl__firecrawl_interact_stop": {
    "name": "mcp__firecrawl__firecrawl_interact_stop",
    "description": "\nStop the live interact session associated with a `scrapeId` and release its resources. Returns a success confirmation.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "scrapeId": {
          "type": "string"
        }
      },
      "required": [
        "scrapeId"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_parse": {
    "name": "mcp__firecrawl__firecrawl_parse",
    "description": "\nParse one supported document into markdown, HTML, links, summary, targeted answers, or JSON matching a schema. Supported inputs include common HTML, PDF, Word, RTF, OpenDocument, and spreadsheet files; PDF parsing can be bounded with `pdfOptions.maxPages`.\n\nLocal MCP reads `filePath` from the server filesystem. Hosted MCP uses two calls: first provide `filePath` to receive upload instructions, upload locally, then call again with the returned `uploadRef`; do not send both fields together. Remote web URLs belong in `firecrawl_scrape`.\n\nSet `redactPII` to request redaction of personally identifiable information in the returned content. `zeroDataRetention` requires an eligible authenticated account; omit it for anonymous keyless use. Returns upload instructions for hosted phase one or parsed document content for the final call. Authenticated final responses can include a `data.metadata.scrapeId` for optional parse feedback.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "formats": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "markdown",
              "html",
              "rawHtml",
              "links",
              "summary",
              "json",
              "query"
            ]
          }
        },
        "jsonOptions": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string"
            },
            "schema": {
              "type": "object",
              "propertyNames": {
                "type": "string"
              },
              "additionalProperties": false,
              "properties": {},
              "required": []
            }
          },
          "additionalProperties": false,
          "required": []
        },
        "queryOptions": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string",
              "maxLength": 10000
            },
            "mode": {
              "default": "freeform",
              "type": "string",
              "enum": [
                "directQuote",
                "freeform"
              ]
            }
          },
          "required": [
            "prompt"
          ],
          "additionalProperties": false
        },
        "parsers": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "pdf"
            ]
          }
        },
        "pdfOptions": {
          "type": "object",
          "properties": {
            "maxPages": {
              "type": "integer",
              "minimum": 1,
              "maximum": 10000
            }
          },
          "additionalProperties": false,
          "required": []
        },
        "onlyMainContent": {
          "type": "boolean"
        },
        "redactPII": {
          "type": "boolean"
        },
        "includeTags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeTags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "removeBase64Images": {
          "type": "boolean"
        },
        "skipTlsVerification": {
          "type": "boolean"
        },
        "storeInCache": {
          "type": "boolean"
        },
        "zeroDataRetention": {
          "type": "boolean"
        },
        "maxAge": {
          "description": "Ignored: parse never reuses or stores indexed content.",
          "type": "number"
        },
        "proxy": {
          "type": "string",
          "enum": [
            "basic",
            "auto"
          ]
        },
        "filePath": {
          "description": "Phase 1 only: path to the local file on the caller/harness machine. Hosted MCP will not read or stat this path; it is used only to produce upload instructions.",
          "type": "string",
          "minLength": 1
        },
        "uploadRef": {
          "description": "Phase 2 only: short-lived upload reference returned by phase 1 after the local PUT upload completes.",
          "type": "string",
          "minLength": 1
        },
        "contentType": {
          "description": "Phase 1 MIME type override. If omitted, the server infers it from the file extension without reading the file.",
          "type": "string"
        },
        "declaredSizeBytes": {
          "description": "Optional phase 1 size declaration. Hosted MCP does not stat the file; provide this only if the caller already knows it.",
          "type": "integer",
          "exclusiveMinimum": 0,
          "maximum": 9007199254740991
        }
      },
      "additionalProperties": false,
      "required": []
    }
  },
  "mcp__firecrawl__firecrawl_monitor_create": {
    "name": "mcp__firecrawl__firecrawl_monitor_create",
    "description": "\nCreate a recurring scrape, crawl, or search monitor that compares each check with its retained predecessor. The simple form accepts `page`/`pages` or `queries` plus a plain-language `goal`; the advanced `body` form controls targets, schedule, change-tracking formats, judging, retention, webhook, and notifications.\n\nIn the simple form, a `goal` is required. If `queries` contains one or more non-empty values and is supplied with `page`/`pages`, `queries` create the search target and page targets are ignored. A monitor schedules future network checks and can send configured email or webhook notifications. Returns the created monitor.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "body": {
          "type": "object",
          "propertyNames": {
            "type": "string"
          },
          "additionalProperties": false,
          "properties": {},
          "required": []
        },
        "page": {
          "type": "string"
        },
        "pages": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "queries": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "searchWindow": {
          "type": "string",
          "enum": [
            "5m",
            "15m",
            "1h",
            "6h",
            "24h",
            "7d"
          ]
        },
        "maxResults": {
          "type": "integer",
          "minimum": 1,
          "maximum": 50
        },
        "includeDomains": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeDomains": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "goal": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "scheduleText": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "includeDiffs": {
          "type": "boolean"
        },
        "webhookUrl": {
          "type": "string"
        }
      },
      "additionalProperties": false,
      "required": []
    }
  },
  "mcp__firecrawl__firecrawl_monitor_list": {
    "name": "mcp__firecrawl__firecrawl_monitor_list",
    "description": "\nList monitors for the authenticated account with optional pagination controls. Returns one page of monitor records and pagination metadata.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "limit": {
          "type": "integer",
          "exclusiveMinimum": 0,
          "maximum": 9007199254740991
        },
        "offset": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        }
      },
      "additionalProperties": false,
      "required": []
    }
  },
  "mcp__firecrawl__firecrawl_monitor_get": {
    "name": "mcp__firecrawl__firecrawl_monitor_get",
    "description": "\nRetrieve one monitor by ID, including its configuration and current state. This does not run or modify the monitor.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_monitor_update": {
    "name": "mcp__firecrawl__firecrawl_monitor_update",
    "description": "\nPatch an existing monitor by ID. The body can change its name, active/paused status, schedule, targets, goal, judging, webhook, notifications, or retention; these changes affect future scheduled checks.\n\nReturns the updated monitor.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "body": {
          "type": "object",
          "propertyNames": {
            "type": "string"
          },
          "additionalProperties": false,
          "properties": {},
          "required": []
        }
      },
      "required": [
        "id",
        "body"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_monitor_delete": {
    "name": "mcp__firecrawl__firecrawl_monitor_delete",
    "description": "\nPermanently delete a monitor by ID and stop its future schedule. This operation cannot be undone and returns deletion status.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_monitor_run": {
    "name": "mcp__firecrawl__firecrawl_monitor_run",
    "description": "\nQueue an immediate check for a monitor outside its normal schedule. This starts network work for the monitor's configured targets and returns the queued check.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_monitor_checks": {
    "name": "mcp__firecrawl__firecrawl_monitor_checks",
    "description": "\nList historical checks for a monitor, optionally filtered by status and bounded by a result limit. Returns one page of check summaries and pagination metadata.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "limit": {
          "type": "integer",
          "exclusiveMinimum": 0,
          "maximum": 9007199254740991
        },
        "offset": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "status": {
          "type": "string",
          "enum": [
            "queued",
            "running",
            "completed",
            "failed",
            "partial",
            "skipped_overlap"
          ]
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_monitor_check": {
    "name": "mcp__firecrawl__firecrawl_monitor_check",
    "description": "\nRetrieve one monitor check and its page-level results, optionally filtered by page status. Pages report `same`, `new`, `changed`, `removed`, or `error`; configured goal judging can add a meaningful-change decision.\n\nMarkdown tracking returns a unified text diff, JSON tracking returns field paths with previous/current values and a current snapshot, and mixed tracking returns both. Returns one page of results plus a `next` URL when more pages exist.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "checkId": {
          "type": "string"
        },
        "limit": {
          "type": "integer",
          "exclusiveMinimum": 0,
          "maximum": 9007199254740991
        },
        "skip": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "pageStatus": {
          "type": "string",
          "enum": [
            "same",
            "new",
            "changed",
            "removed",
            "error"
          ]
        }
      },
      "required": [
        "id",
        "checkId"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_research_search_papers": {
    "name": "mcp__firecrawl__firecrawl_research_search_papers",
    "description": "\nSearch paper metadata and abstracts with a natural-language query across the indexed corpus, which spans biomedical, life-science, and clinical literature (PubMed, bioRxiv, medRxiv) alongside arXiv and other scientific sources. Optional author, category, and date filters constrain results.\n\nSeveral distinct framings of the same question surface different papers than a single query does.\n\nReturns ranked papers with canonical IDs, titles, authors, and abstracts.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "query": {
          "description": "Natural-language research topic or question, including methods, systems, conditions, populations, interventions, or outcomes when relevant.",
          "type": "string",
          "minLength": 1
        },
        "k": {
          "description": "Number of ranked papers to return (default 40).",
          "type": "integer",
          "minimum": 1,
          "maximum": 500
        },
        "authors": {
          "description": "Author substring filter(s); ALL must match (case-insensitive).",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "categories": {
          "description": "Paper category filter(s) (e.g. `cs.LG`); ALL provided values must match.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "from": {
          "description": "Inclusive lower bound on created/updated date (`YYYY-MM-DD`).",
          "type": "string"
        },
        "to": {
          "description": "Inclusive upper bound on created/updated date (`YYYY-MM-DD`).",
          "type": "string"
        }
      },
      "required": [
        "query"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_research_inspect_paper": {
    "name": "mcp__firecrawl__firecrawl_research_inspect_paper",
    "description": "\nRetrieve canonical metadata for one paper ID, such as an arXiv, PMC, PMID, or DOI identifier. Returns the title, abstract, authors, categories, source IDs, and dates as markdown.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "paperId": {
          "description": "Canonical paperId or primaryId such as `arxiv:1706.03762`, `pmcid:PMC12530322`, `pmid:40953549`, or `doi:10.1016/j.neunet.2025.108095`.",
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "paperId"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_research_related_papers": {
    "name": "mcp__firecrawl__firecrawl_research_related_papers",
    "description": "\nFind citation-graph candidates from one to ten `seed_ids`; the first ID is the primary seed and later IDs are anchors. `mode` defaults to `similar` (co-citation/bibliographic coupling); `citers` returns papers citing a seed and `references` papers cited by a seed. `intent` ranks candidates.\n\nReturns ranked candidates and the evaluated pool size.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "seed_ids": {
          "minItems": 1,
          "maxItems": 10,
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "intent": {
          "type": "string",
          "minLength": 1
        },
        "mode": {
          "type": "string",
          "enum": [
            "similar",
            "citers",
            "references"
          ]
        },
        "k": {
          "type": "integer",
          "minimum": 1,
          "maximum": 500
        },
        "rerank": {
          "description": "Apply an additional rerank over the fused candidates.",
          "type": "boolean"
        }
      },
      "required": [
        "seed_ids",
        "intent"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_research_read_paper": {
    "name": "mcp__firecrawl__firecrawl_research_read_paper",
    "description": "\nRetrieve in-body passages from one paper that are relevant to a specific question. Full text is available only for indexed papers; `k` controls the number of passages.\n\nReturns matching passages or a notice when full text is unavailable.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "paperId": {
          "description": "Canonical paperId or primaryId such as `arxiv:1706.03762`, `pmcid:PMC12530322`, `pmid:40953549`, or `doi:10.1016/j.neunet.2025.108095`.",
          "type": "string",
          "minLength": 1
        },
        "question": {
          "type": "string",
          "minLength": 1
        },
        "k": {
          "description": "Number of passages to return (default 4).",
          "type": "integer",
          "minimum": 1,
          "maximum": 50
        }
      },
      "required": [
        "paperId",
        "question"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_developer_search": {
    "name": "mcp__firecrawl__firecrawl_developer_search",
    "description": "\nSearch an index of public repositories, GitHub issues, merged pull requests, repository READMEs, and code documentation for programming questions that need external documentation or upstream evidence.\n\nReturns ranked results with an ID, source type, URL, title, and the matched passages in markdown.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "query": {
          "description": "Natural-language developer question or search phrase, including the library, error message, or API involved when relevant.",
          "type": "string",
          "minLength": 1
        },
        "k": {
          "description": "Number of ranked results to return (default 10).",
          "type": "integer",
          "minimum": 1,
          "maximum": 100
        },
        "skills": {
          "description": "Set to \"only\" to search only agent-skill files.",
          "type": "string",
          "enum": [
            "only"
          ]
        }
      },
      "required": [
        "query"
      ],
      "additionalProperties": false
    }
  },
  "mcp__firecrawl__firecrawl_credit_usage": {
    "name": "mcp__firecrawl__firecrawl_credit_usage",
    "description": "\nGet the authenticated Firecrawl team's current credit balance or historical credit consumption. Use the current view to answer how many credits remain or to check billing-period boundaries. Use the historical view for monthly usage reporting and trend analysis.\n\nThe current view returns `remainingCredits`, `planCredits`, `billingPeriodStart`, and `billingPeriodEnd`. Extra purchased or granted credits can make `remainingCredits` greater than `planCredits`. Billing-period dates may be null when the upstream billing provider has no period metadata.\n\nThe historical view returns periods sorted by start date with `startDate`, `endDate`, and `creditsUsed`. Set `byApiKey` to include separate periods per API key, identified by the optional `apiKey` field. The newest period's `endDate` can be null.\n",
    "parameters": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "view": {
          "description": "Select current balance or historical monthly usage. Defaults to current.",
          "type": "string",
          "enum": [
            "current",
            "historical"
          ]
        },
        "byApiKey": {
          "description": "Break historical usage down by API key. When view is omitted, true selects the historical view; it cannot be combined with view \"current\".",
          "type": "boolean"
        }
      },
      "additionalProperties": false,
      "required": []
    }
  }
}
```
