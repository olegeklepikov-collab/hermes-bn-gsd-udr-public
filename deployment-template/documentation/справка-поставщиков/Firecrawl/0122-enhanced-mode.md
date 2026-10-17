> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: enhanced-mode

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/features/enhanced-mode

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/features/enhanced-mode#content-area)

The `proxy` parameter is deprecated. We recommend `auto` — the default — which lets Firecrawl handle proxy selection for you.

Firecrawl provides different proxy types to help you scrape websites with varying levels of complexity. Set the `proxy` parameter to control which proxy strategy is used for a request.

## [​](https://docs.firecrawl.dev/features/enhanced-mode\#proxy-types)  Proxy types

| Type | Description |
| --- | --- |
| `basic` | Standard proxies suitable for most sites |
| `enhanced` | Enhanced proxies for complex sites |
| `auto` | **Recommended.** Tries `basic` first, then retries with `enhanced` on failure |

If you do not specify a proxy, Firecrawl defaults to `auto`.

## [​](https://docs.firecrawl.dev/features/enhanced-mode\#basic-usage)  Basic usage

Set the `proxy` parameter to choose a proxy strategy. The following example uses `auto`, which lets Firecrawl decide when to escalate to enhanced proxies.

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(
  # No API key needed to get started — add one for higher rate limits:
  # api_key='fc-YOUR-API-KEY',
)

# Choose proxy strategy: 'basic' | 'enhanced' | 'auto'
doc = firecrawl.scrape('https://example.com', formats=['markdown'], proxy='auto')

print(doc.warning or 'ok')
```

```
import { Firecrawl } from 'firecrawl';

const firecrawl = new Firecrawl({
  // No API key needed to get started — add one for higher rate limits:
  // apiKey: "fc-YOUR-API-KEY",
});

// Choose proxy strategy: 'basic' | 'enhanced' | 'auto'
const doc = await firecrawl.scrape('https://example.com', {
  formats: ['markdown'],
  proxy: 'auto'
});

console.log(doc.warning || 'ok');
```

```

// Choose proxy strategy: 'basic' | 'enhanced' | 'auto'
# No API key needed to get started — add -H "Authorization: Bearer fc-YOUR-API-KEY" for higher rate limits:
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://example.com",
      "proxy": "auto"
    }'
```

## [​](https://docs.firecrawl.dev/features/enhanced-mode\#when-firecrawl-escalates)  When Firecrawl escalates

Firecrawl starts on basic proxies. If the target responds with **401, 403, or 429**, Firecrawl treats that as a sign the proxy was not good enough and retries the same URL through enhanced proxies. Other status codes, including 404 and 5xx, do not trigger an escalation, because a different proxy would not change the answer.The escalation happens at most once per request. Once a request is already on enhanced proxies, a further 401, 403, or 429 is returned to you as the result rather than retried again.You do not need to detect this or handle it. The retry is part of the same request and the response you receive is the final one.

Enhanced proxy requests cost the same as basic requests — **1 credit per request**. An escalated retry is not charged separately, so a request that starts on basic and finishes on enhanced still costs 1 credit.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/features/enhanced-mode.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/features/enhanced-mode)

✕
