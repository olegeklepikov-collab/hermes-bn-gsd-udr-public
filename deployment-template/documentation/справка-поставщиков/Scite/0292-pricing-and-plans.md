> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: pricing-and-plans

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing and plans

> Compare Scite plans, API access, MCP credits, usage limits, and options for organizations.

Scite offers individual, team, and organization plans. The right plan depends on whether you use Scite directly, connect it to an AI client through MCP, or build with the REST API.

<Note>
  Prices below are in USD and exclude taxes, discounts, and promotions. See the [Scite pricing page](https://scite.ai/pricing) for current checkout pricing.
</Note>

## Individual and team plans

| Plan | Price | Best for | Developer access |
| - | -: | - | - |
| **Free** | \$0 | Trying Scite and using public data | Public Papers and Tallies endpoints don't require an API key. |
| **Basic** | $20 monthly or $144 annually | Individual researchers using Scite and its AI integrations | Includes 250 MCP credits per month. It doesn't include a self-service REST API key. |
| **Pro** | $50 monthly or $480 annually | Advanced research and API evaluation | Includes 2,500 MCP credits per month and self-service API key access. |
| **Team** | $50 per user monthly or $480 per user annually | Teams that want Pro access under one subscription | Includes Pro access and 2,500 MCP credits per user per month. |

Annual prices are billed once per year. The annual equivalents are $12 per month for Basic and $40 per month for Pro or Team.

<CardGroup cols={2}>
  <Card title="Compare plans" icon="tags" href="https://scite.ai/pricing">
    Review current features, promotions, and billing options.
  </Card>

  <Card title="Create an API key" icon="key" href="https://scite.ai/users/me/api">
    Pro users can create, rotate, and revoke self-service keys in the API Console.
  </Card>
</CardGroup>

## API access and licensing

A Pro subscription provides a self-service API key for evaluation. It doesn't grant unrestricted commercial, production, or research use of every endpoint or dataset.

* Commercial or research use of Search requires a separate license agreement.
* Search snippets are redacted when you use a self-service Pro key.
* Evidence datasets such as patents, grants, clinical trials, drugs, devices, and safety records require dataset-specific scopes.
* Rate limits and available scopes depend on your account and agreement.

See Authentication (локальный ресурс исходного примера не включён) to compare credential types. See Errors and rate limits (локальный ресурс исходного примера не включён) to handle missing scopes and usage limits.

## Organization and Enterprise plans

Organization and Enterprise plans use custom pricing. They can include higher limits, managed `client_id` and `client_secret` credentials, additional API or Evidence scopes, pooled usage, SSO, and organization-wide access.

[Contact sales](https://scite.ai/contact-sales) to discuss commercial use, production integrations, custom datasets, or an organization license.

## Common questions

### Is API access included with Basic?

No. Basic includes MCP credits for supported AI integrations, but self-service REST API keys require Pro.

### Do API requests have a public per-call price?

Scite doesn't publish a separate pay-as-you-go API rate. Self-service evaluation access is tied to Pro. Commercial terms, higher limits, and expanded scopes are quoted based on the integration.

### Are MCP credits and API limits the same?

No. MCP credits apply to Scite tools used through MCP clients. REST API limits are enforced separately and vary by endpoint and account. A self-service API key shares its owner's plan allowance.

### Which plan do I need for Evidence datasets?

Access through the Scite product and access through the REST API are licensed separately. REST API access to Evidence datasets requires the corresponding dataset scope. [Contact sales](https://scite.ai/contact) to add one to your account.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
