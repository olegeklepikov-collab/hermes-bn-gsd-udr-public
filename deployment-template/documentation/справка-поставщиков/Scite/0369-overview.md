> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: overview

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool reference

> The full Scite MCP tool catalog, grouped by task, with the access each tool requires.

The Scite MCP server exposes 25 tools across three groups. Call `tools/list` to get the live catalog with full input schemas; this page is the narrative index.

<CardGroup cols={3}>
  <Card title="Literature" icon="book-open" href="/mcp/tools/literature">
    Search papers, read full-text excerpts, and pull Smart Citations.
  </Card>

  <Card title="Evidence" icon="flask" href="/mcp/tools/evidence">
    Patents, trials, grants, FDA device and drug records, adverse events, and safety alerts.
  </Card>

  <Card title="Collections" icon="folder-open" href="/mcp/tools/collections">
    Create and maintain saved sets of papers.
  </Card>
</CardGroup>

## The catalog

| Tool | Group | What it does |
| - | - | - |
| `search_literature` | Literature | Search the scientific literature; return metadata, full-text excerpts, and Smart Citations |
| `search_patents` | Evidence | Search patent families |
| `search_clinical_trials` | Evidence | Search ClinicalTrials.gov records |
| `get_clinical_trial` | Evidence | Fetch one trial by NCT id |
| `search_grants` | Evidence | Search NIH, NSF, SBIR/STTR, Wellcome, EU, and other funders |
| `get_grant` | Evidence | Fetch one grant by id |
| `search_device510k` | Evidence | Search FDA 510(k) clearance metadata |
| `get_device510k` | Evidence | Fetch one clearance by K number |
| `search_510k_summaries` | Evidence | Search the full text of 510(k) summary PDFs |
| `get_510k_summary` | Evidence | Fetch one 510(k) summary document |
| `search_mhra` | Evidence | Search UK MHRA safety alerts and publications |
| `get_mhra_alert` | Evidence | Fetch one MHRA alert |
| `search_maude` | Evidence | Search FDA MAUDE device adverse-event reports |
| `get_maude_report` | Evidence | Fetch one MAUDE report |
| `search_faers` | Evidence | Search FDA FAERS drug adverse-event reports |
| `get_faers_report` | Evidence | Fetch one FAERS report |
| `search_drugs` | Evidence | Search FDA labels, Orange Book, and Drugs\@FDA |
| `get_drug` | Evidence | Fetch one drug record |
| `create_collection` | Collections | Create a Collection from a DOI list |
| `get_collection` | Collections | Fetch a Collection by slug |
| `search_collections` | Collections | List the Collections you can access |
| `update_collection` | Collections | Change a Collection's name, description, DOIs, or visibility |
| `delete_collection` | Collections | Permanently delete a Collection |
| `add_dois_to_collection` | Collections | Add DOIs to a Collection |
| `remove_dois_from_collection` | Collections | Remove DOIs from a Collection |

## Access requirements

Every tool above is visible in `tools/list` when your credential carries the `mcp` scope. Access is enforced when you call the tool, not when you list it, so a tool can appear in the catalog and still return an error on `tools/call`.

| Group | Requirement |
| - | - |
| Literature | A Scite premium subscription |
| Evidence | Pro, **or** the dataset's `evidence:<dataset>:mcp` scope |
| Collections | A signed-in Scite account on a premium subscription |

Organization licenses work differently from individual accounts on Evidence tools. If your account is on an organization license, reaching the Pro tier does not unlock Evidence — your license needs the explicit `evidence:<dataset>:mcp` entitlement. [Email sales](mailto:sales@scite.ai) to have one added.

When a tool call fails an access check, the server returns JSON-RPC error `-32003` with the required plan or scope in the error payload:

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": "1",
  "error": {
    "code": -32003,
    "message": "A scite pro subscription is required to use this tool. Upgrade at https://scite.ai/pricing.",
    "data": {
      "required_plan": "pro",
      "upgrade_url": "https://scite.ai/pricing"
    }
  }
}
```

<Note>
  After an upgrade, new entitlements can take up to 15 minutes to reach an active MCP session. To apply them immediately, disconnect and reconnect the Scite MCP server in your client.
</Note>

## Tool annotations

Each tool carries MCP annotations that describe its behavior. Clients use these to decide what needs confirmation.

| Annotation | Tools |
| - | - |
| `readOnlyHint: true` | All Literature and Evidence tools, plus `get_collection` and `search_collections` |
| `destructiveHint: true` | `delete_collection`, `remove_dois_from_collection` |
| `openWorldHint: false` | Every tool — results come from Scite's own datasets |

## Conventions

Two query conventions run through the catalog, and they are not the same one.

* **`search_literature`** uses named parameters: `term`, `dois`, `limit`, `offset`, and 25+ typed filters. This matches the Search API (локальный ресурс исходного примера не включён).
* **Every Evidence tool** uses the compact `q` / `f` / `p` / `s` / `sortDir` form. This matches the Evidence API (локальный ресурс исходного примера не включён).

Search-then-fetch is the intended pattern for Evidence. Search results are deliberately slim to save context; call the matching `get_*` tool only when you need fields the search result doesn't already carry.

## Related

* Scite MCP (локальный ресурс исходного примера не включён): setup, authentication, and the JSON-RPC protocol
* Prompts (локальный ресурс исходного примера не включён): the prebuilt workflows the server ships
* Glossary (локальный ресурс исходного примера не включён): Smart Citation terminology used across tool responses


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
