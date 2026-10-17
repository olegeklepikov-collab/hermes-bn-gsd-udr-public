> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: rate-limits

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.keenable.ai/rate-limits

Rate limits - Keenable
Documentation Index
Fetch the complete documentation index at:
/llms.txt
Use this file to discover all available pages before exploring further.
Skip to main content
Keenable
home page
Search...
⌘
## K
GitHub
Console
Console
Search...
Navigation
Get started
Rate limits
Documentation
Integrations
Get started
Quickstart
Authentication
Rate limits
Credits
Auto top-up
Pay per request (x402)
Tools
## MCP
## CLI
API reference
API reference
## POST
Search
## GET
Fetch
Reference
Changelog
Get started
Rate limits
Copy page
Copy page
How fast you can call search and fetch — the per-second and hourly limits for authenticated and unauthenticated requests, and how they differ from the credit allowance.
Copy page
Copy page
Keenable applies rate limits across search and fetch endpoints in accordance with the authentication
status of the request. To learn more about authentication, see
authentication
.
Authentication status
Rate limit
Authenticated
10 requests per second (per organization)
Unauthenticated
1,000 requests per hour, max 10 requests per second (per IP)
Pay per request
(x402)
50 paid requests per second per paying wallet, 100 requests per second per IP, no hourly cap
A few things worth keeping in mind:
Rate limits on authenticated requests are applied on the organization-level.
Authentication removes the hourly request cap; the per-second limit still applies.
Higher per-second limits are available on some plans.
The unauthenticated pool is shared per IP address, so its available headroom depends on other traffic from the same address.
On the pay-per-request paths, the per-IP limit counts both the unpaid request that returns the offer and the paid retry, which is why it is twice the per-wallet limit.
To increase rate limits on the authenticated tier, please
talk to us
.
Rate limits cap how
fast
you can call the API. How
much
you can call it is a separate limit: authenticated usage draws on a free allowance of 100,000 requests a month — see
credits
.
Authentication
Credits
x
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform
