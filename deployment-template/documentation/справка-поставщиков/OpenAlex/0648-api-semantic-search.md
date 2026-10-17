> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка OpenAlex: api-semantic-search

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Semantic Search

Semantic search returns works whose meaning is closest to your query, even when the wording differs. A query about "predicting drug toxicity from molecular structure" finds papers using "computational toxicology" or "QSAR" — words your search never mentioned.

```bash
https://api.openalex.org/works?search.semantic=predicting drug toxicity from molecular structure
```

## Long-text queries

Semantic search shines when you have a longer description — an abstract, a grant aim, or a paragraph from a paper you're writing. The richer the input, the better the matches.

```bash
# Paste your grant aim verbatim (URL-encoded)
https://api.openalex.org/works?search.semantic=We propose to integrate single-cell RNA-seq with spatial transcriptomics to map T-cell exhaustion in solid tumors and identify novel checkpoint targets.
```

Up to **2,000 characters** are used for matching; longer input is truncated.

## Combining with filters

Most [filters](https://help.openalex.org/api/filtering/) and the [`select`](https://help.openalex.org/api/selecting-fields/) parameter work as usual:

```bash
https://api.openalex.org/works?search.semantic=mRNA vaccine immunogenicity in older adults&filter=publication_year:>2020,is_oa:true&select=id,title,relevance_score
```

Two filters are **not** supported on semantic search — they would require pre-filtering hundreds of millions of vectors and time out:

- `last_known_institutions.country_code` (and the `country_code` shorthand)
- `cited_by_count`

## How it works

OpenAlex embeds the title and abstract of every work using [GTE Large EN](https://huggingface.co/thenlper/gte-large), an open-source embedding model from Alibaba DAMO Academy, into a 1,024-dimensional vector. At query time we embed your query the same way and return the works closest by cosine similarity.

## Limits

| Constraint | Value |
|------------|-------|
| Max input length | 2,000 characters |
| Max results | 50 per query |
| Rate limit | 1 request per second |
| Pricing | See [pricing by endpoint](https://help.openalex.org/access/example-costs/) |

> **Note:**
> Only one search parameter is allowed per request: `search`, `search.exact`, or `search.semantic`.
