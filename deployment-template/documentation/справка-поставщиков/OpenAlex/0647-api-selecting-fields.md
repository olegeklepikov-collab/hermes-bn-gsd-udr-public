> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: api-selecting-fields

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Select Fields

Use the `select` parameter to return only specific fields:

```bash
https://api.openalex.org/works?select=id,doi,display_name
```

Response:

```json
{
  "results": [
    {
      "id": "https://openalex.org/W1775749144",
      "doi": "https://doi.org/10.1016/s0021-9258(19)52451-6",
      "display_name": "PROTEIN MEASUREMENT WITH THE FOLIN PHENOL REAGENT"
    },
    {
      "id": "https://openalex.org/W2100837269",
      "doi": "https://doi.org/10.1038/227680a0",
      "display_name": "Cleavage of Structural Proteins during the Assembly of the Head of Bacteriophage T4"
    }
  ]
}
```

## Limitations

**Root-level fields only.** You can select top-level fields but not nested properties:

```json
// Given this structure:
{
  "id": "https://openalex.org/W2138270253",
  "open_access": {
    "is_oa": true,
    "oa_status": "bronze",
    "oa_url": "http://www.pnas.org/content/74/12/5463.full.pdf"
  }
}
```

| Query | Works? |
|-------|--------|
| `select=id,open_access` | Yes |
| `select=open_access.is_oa` | No (error) |

## Where `select` works

| Endpoint | Supported? |
|----------|------------|
| List entities (`/works`, etc.) | Yes |
| Single entity (`/works/{id}`) | Yes |
| Group by | No |
| Autocomplete | No |
