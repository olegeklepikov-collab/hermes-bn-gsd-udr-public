> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: api-autocomplete

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Autocomplete

The autocomplete endpoint provides fast typeahead search for building user interfaces. Queries return in ~200ms.

```bash
https://api.openalex.org/autocomplete/institutions?q=flori
```

See it in action at [explore.openalex.org](https://explore.openalex.org/).

## Request format

```
/autocomplete/<entity_type>?q=<query>
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `entity_type` | Optional | `works`, `authors`, `sources`, `institutions`, `topics`, `keywords`, `concepts` (deprecated), `publishers`, or `funders` |
| `q` | Yes | The search string |

## Response format

```json
{
  "meta": {
    "count": 183,
    "db_response_time_ms": 5,
    "page": 1,
    "per_page": 10
  },
  "results": [
    {
      "id": "https://openalex.org/I33213144",
      "display_name": "University of Florida",
      "hint": "Gainesville, USA",
      "cited_by_count": 17190001,
      "entity_type": "institution",
      "external_id": "https://ror.org/02y3ad647"
    }
  ]
}
```

### Result properties

| Property | Description |
|----------|-------------|
| `id` | OpenAlex ID |
| `external_id` | Canonical external ID (DOI, ORCID, ROR, etc.) |
| `display_name` | Entity name |
| `entity_type` | `work`, `author`, `source`, `institution`, `topic`, `keyword`, `concept`, `publisher`, `funder` |
| `cited_by_count` | Citation count (for works) or sum of citations for linked works |
| `works_count` | Number of associated works (`null` for works) |
| `hint` | Additional context to help identify the result |

### The `hint` property

Hints help users distinguish between similar results:

| Entity | Hint content |
|--------|--------------|
| Work | Authors' names (e.g., "R. Alexander Pyron, John J. Wiens") |
| Author | Last known institution (e.g., "University of North Carolina, USA") |
| Source | Host organization (e.g., "Oxford University Press") |
| Institution | Location (e.g., "Gainesville, USA") |
| Concept | Description (e.g., "the study of plant species and genera") |

## ID lookups

Autocomplete detects IDs and matches them directly:

```bash
# Find author by ORCID
https://api.openalex.org/autocomplete?q=https://orcid.org/0000-0002-7436-3176

# Find source by OpenAlex ID
https://api.openalex.org/autocomplete/sources?q=S49861241
```

## Filtering autocomplete

Combine with any [filter](https://api.openalex.org/api/filtering/) or [search](https://api.openalex.org/api/searching/):

```bash
# Works from 2010 about frogs, autocomplete on "greenhou"
https://api.openalex.org/autocomplete/works?filter=publication_year:2010&search=frogs&q=greenhou
```
