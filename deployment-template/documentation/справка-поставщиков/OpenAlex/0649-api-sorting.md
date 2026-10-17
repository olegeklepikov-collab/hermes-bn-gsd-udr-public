> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: api-sorting

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Sort

Use the `sort` parameter to order results by a property:

```bash
# Works sorted by citation count (highest first)
https://api.openalex.org/works?sort=cited_by_count:desc

# Sources in alphabetical order
https://api.openalex.org/sources?sort=display_name
```

## Common sortable fields

| Field | Description |
|-------|-------------|
| `display_name` | Alphabetical order |
| `cited_by_count` | Number of citations |
| `works_count` | Number of works |
| `publication_date` | Publication date (works only) |
| `relevance_score` | Search relevance (requires search filter) |

## Sort direction

By default, sort is ascending. Append `:desc` for descending:

```bash
# Ascending (default)
https://api.openalex.org/works?sort=publication_date

# Descending
https://api.openalex.org/works?sort=publication_date:desc
```

## Multiple sort keys

Sort by multiple properties using commas:

```bash
# Sort by year descending, then by relevance score
https://api.openalex.org/works?search=bioplastics&sort=publication_year:desc,relevance_score:desc
```

> **Note:**
> Sorting by `relevance_score` requires an active search. An error is thrown otherwise.
