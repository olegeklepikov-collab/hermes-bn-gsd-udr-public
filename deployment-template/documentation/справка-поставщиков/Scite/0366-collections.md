> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: collections

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Collection tools

> Create, read, and maintain saved sets of papers through MCP.

A collection is a saved, named set of papers. Seven MCP tools let an assistant build and maintain one during a conversation — group DOIs it just found, add to an existing set, or search within one.

Requires a signed-in Scite account on a premium subscription. Anonymous sessions can't use these tools, because a collection needs an owner.

## Two kinds of collection

| Kind | Created by | Membership |
| - | - | - |
| DOI-list | MCP or the Scite web app | An explicit list of DOIs |
| Saved-search | The Scite web app only | A stored query, plus manual include and exclude lists |

MCP creates DOI-list collections. `add_dois_to_collection` and `remove_dois_from_collection` work on both kinds; `create_collection` and `update_collection` handle DOI-list collections only.

For a saved-search collection, adding a DOI force-includes it so it appears even when the query wouldn't return it, and removing a DOI excludes it so it doesn't appear even when the query would.

<Note>
  A collection is a set of papers. A dashboard is a report on a collection. They aren't the same thing — see the glossary (локальный ресурс исходного примера не включён).
</Note>

## Access levels

Every collection tool checks the caller's access level.

| Level | Can |
| - | - |
| VIEWER | Read the collection |
| EDITOR | Read, update, and change DOI membership |
| ADMIN | Everything, including delete |

The creator becomes ADMIN. You reach VIEWER by owning the collection, being shared on it, being in an organization it's shared with, or — if `is_public` is set — holding the slug.

## The slug

Every tool except `create_collection` and `search_collections` identifies a collection by its `slug`. You get one from `create_collection` or `search_collections`; there's no way to look one up by name directly.

## Create

`create_collection` takes a `name` (required), and optionally a `description`, a `dois` list to seed it, and `is_public`.

```json theme={null}
{
  "name": "create_collection",
  "arguments": {
    "name": "CRISPR off-target effects",
    "description": "Papers gathered for the Q3 review",
    "dois": ["10.1038/s41586-020-2649-2", "10.1126/science.1225829"],
    "is_public": false
  }
}
```

Seeded DOIs are validated and resolved against Scite. Unknown DOIs are dropped, not rejected — the response reports how many via `unmatchedDoiCount`, so check it rather than assuming every DOI landed. An empty `dois` list creates an empty collection.

`is_public` defaults to `false`. When true, anyone holding the slug can view the collection.

The response carries `id`, `slug`, `name`, `description`, `isPublic`, `doiQueryType`, `accessType`, and DOI counts.

## Read

`get_collection` takes a `slug` and returns the collection's identity, sharing, access level, and DOI counts. Requires VIEWER.

`search_collections` lists the collections you can access, with an optional `q` to filter by a case-insensitive substring of the name. It returns `{collections: [...], total: N}`.

<Warning>
  `search_collections` filters your own collections by name. It is not a full-text search across all collections, and it doesn't search paper contents. To search the papers *inside* a collection, pass its slug to `search_literature` as `collection_slug`.
</Warning>

## Update

`update_collection` takes a `slug` plus any of `name`, `description`, `dois`, and `is_public`. Requires EDITOR or ADMIN.

It's a partial update, but the `dois` field behaves differently from the rest:

* Omit `dois` and the DOI list is left alone.
* Supply `dois` and it **replaces** the entire list.

To add or remove a few DOIs without rebuilding the list, use the membership tools below instead.

```json theme={null}
{
  "name": "update_collection",
  "arguments": {
    "slug": "crispr-off-target-effects",
    "description": "Updated after the September screen",
    "is_public": true
  }
}
```

## Change membership

`add_dois_to_collection` and `remove_dois_from_collection` both take a `slug` and a non-empty `dois` array. Both require EDITOR or ADMIN, and both are idempotent — adding a DOI already present is ignored, as is removing one that isn't there.

```json theme={null}
{
  "name": "add_dois_to_collection",
  "arguments": {
    "slug": "crispr-off-target-effects",
    "dois": ["10.1016/j.cell.2014.05.010"]
  }
}
```

Removing DOIs takes papers out of the collection. It does not delete the collection.

## Delete

`delete_collection` takes a `slug` and requires ADMIN. It returns `{deleted: true, slug: "..."}`.

<Warning>
  Deletion is permanent. The collection and its DOI membership are removed and cannot be recovered. The tool carries the MCP `destructiveHint` annotation, so a well-behaved client will ask you to confirm before calling it.
</Warning>

## Searching within a collection

Once a collection exists, `search_literature` can search inside it. Pass the slug as `collection_slug` and combine it with `term` and any other filter.

```json theme={null}
{
  "name": "search_literature",
  "arguments": {
    "collection_slug": "crispr-off-target-effects",
    "term": "mismatch tolerance",
    "limit": 10
  }
}
```

## Related

* Collections guide (локальный ресурс исходного примера не включён): the same operations over HTTP
* Literature tools (локальный ресурс исходного примера не включён): `search_literature` and its `collection_slug` filter
* Glossary (локальный ресурс исходного примера не включён): collection, dashboard, and access terminology


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
