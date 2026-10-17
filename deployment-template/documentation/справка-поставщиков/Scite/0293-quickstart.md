> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: quickstart

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Retrieve a paper, check its citation tally, and run your first authenticated search.

You can complete the first two steps without an account. Start with two public endpoints, then use an API key for Search.

<Steps>
  <Step title="Retrieve a paper">
    Look up publication metadata by DOI. Papers endpoints are public, so this request doesn't need an API key.

    ```bash theme={null}
    curl 'https://api.scite.ai/papers/10.1038/nature12373'
    ```

    The response includes the title, abstract, authors, journal, publication year, retraction status, and related identifiers.
  </Step>

  <Step title="Check its citation tally">
    Tallies endpoints are also public:

    ```bash theme={null}
    curl 'https://api.scite.ai/tallies/10.1038/nature12373'
    ```

    ```json theme={null}
    {
      "doi": "10.1038/nature12373",
      "total": 42,
      "supporting": 30,
      "contradicting": 2,
      "mentioning": 10,
      "unclassified": 0,
      "citingPublications": 38
    }
    ```

    `total` counts citation statements. `citingPublications` counts distinct papers, so the values can differ. See Citations & Tallies (локальный ресурс исходного примера не включён).

    <Note>
      Tally values change as Scite indexes new citation statements. Treat the numbers above as an example response shape.
    </Note>
  </Step>

  <Step title="Run an authenticated search">
    **Need an API key?** On Pro, create one in the API Console](https://scite.ai/users/me/api). Creating a key doesn't grant every optional scope; see [Authentication (локальный ресурс исходного примера не включён) for feature access. For higher limits or managed credentials, [contact sales](https://scite.ai/contact).

    `term` supports `AND`, `OR`, `NOT`, and quoted phrases.

    ```bash theme={null}
    curl -G 'https://api.scite.ai/api_partner/search' \
      -H 'Authorization: Bearer <YOUR_API_KEY>' \
      --data-urlencode 'term="machine learning" AND healthcare' \
      --data-urlencode 'limit=5' \
      --data-urlencode 'sort=date' \
      --data-urlencode 'sort_order=desc'
    ```

    The response includes a total `count` and a `hits` array. Each hit carries DOI, title, authors, journal, abstract, and citation tally where available. The Search guide (локальный ресурс исходного примера не включён) covers the 25+ filters.

    <Note>
      Pro keys support Search for evaluation. Commercial or research use requires a separate license agreement. See the Search guide (локальный ресурс исходного примера не включён).
    </Note>
  </Step>

  <Step title="Go further">
    * Install Scite in ChatGPT or Claude, use Article Galaxy for Copilot](https://marketplace.microsoft.com/en-us/product/WA200011900), or connect another MCP client: [Scite MCP (локальный ресурс исходного примера не включён)
    * Full paper metadata for any DOI: Papers & Authors (локальный ресурс исходного примера не включён)
    * Tallies for up to 500 DOIs at once: Smart Citations (локальный ресурс исходного примера не включён)
    * Screen a manuscript's reference list: Reference Check (локальный ресурс исходного примера не включён)
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
