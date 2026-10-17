> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: monitoring-page

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/features/monitoring-page

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/features/monitoring-page#content-area)

Page monitoring watches URLs you already know about. Each check scrapes every URL in the target, diffs it against the last retained snapshot, and reports whether the page is `same`, `changed`, `new`, `removed`, or `error`. It’s the right choice for pricing pages, changelogs, docs pages, job posts, status pages, or any known URL where a small change matters.This page covers the `scrape` target. Scheduling, goals and judging, change tracking, notifications, and pricing are shared across all monitor types. See the [Monitoring overview](https://docs.firecrawl.dev/features/monitoring).

## [​](https://docs.firecrawl.dev/features/monitoring-page\#create-a-page-monitor)  Create a page monitor

Create a monitor with a `scrape` target that lists one or more explicit URLs:

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(
  # Monitor endpoints require an API key:
  api_key="fc-YOUR-API-KEY",
)

monitor = firecrawl.create_monitor(
    name="Hacker News AI monitor",
    schedule={"text": "every 30 minutes", "timezone": "UTC"},
    goal=(
        "Alert when a new Hacker News story related to AI enters the top 10. "
        "Ignore changes to stories that are not about AI. "
        "Do not alert on changes outside the top 10."
    ),
    targets=[\
        {\
            "type": "scrape",\
            "urls": ["https://news.ycombinator.com"],\
        }\
    ],
    notification={
        "email": {
            "enabled": True,
            "recipients": ["alerts@example.com"],
            "includeDiffs": True,
        }
    },
)

print(monitor.id)
```

```
import Firecrawl from "@mendable/firecrawl-js";

const firecrawl = new Firecrawl({
  // Monitor endpoints require an API key:
  apiKey: "fc-YOUR-API-KEY",
});

const monitor = await firecrawl.createMonitor({
  name: "Hacker News AI monitor",
  schedule: { text: "every 30 minutes", timezone: "UTC" },
  goal:
    "Alert when a new Hacker News story related to AI enters the top 10. Ignore changes to stories that are not about AI. Do not alert on changes outside the top 10.",
  notification: {
    email: {
      enabled: true,
      recipients: ["alerts@example.com"],
      includeDiffs: true,
    },
  },
  targets: [\
    {\
      type: "scrape",\
      urls: ["https://news.ycombinator.com"],\
    },\
  ],
});

console.log(monitor.id);
```

```
curl -s -X POST "https://api.firecrawl.dev/v2/monitor" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Hacker News AI monitor",
    "schedule": {
      "text": "every 30 minutes",
      "timezone": "UTC"
    },
    "goal": "Alert when a new Hacker News story related to AI enters the top 10. Ignore changes to stories that are not about AI. Do not alert on changes outside the top 10.",
    "notification": {
      "email": {
        "enabled": true,
        "recipients": ["alerts@example.com"],
        "includeDiffs": true
      }
    },
    "targets": [\
      {\
        "type": "scrape",\
        "urls": ["https://news.ycombinator.com"]\
      }\
    ]
  }'
```

You can also create monitors from the Firecrawl CLI:

## CLI

```
firecrawl monitor create --name "Hacker News AI" \
  --schedule "every 30 minutes" \
  --goal "Alert when a new Hacker News story related to AI enters the top 10. Ignore changes to stories that are not about AI. Do not alert on changes outside the top 10." \
  --page https://news.ycombinator.com
```

## [​](https://docs.firecrawl.dev/features/monitoring-page\#scrape-target)  Scrape target

A `scrape` target requires `type` and a `urls` array with at least one URL. Scrape options are passed through to the underlying scrape jobs. Monitor-triggered scrapes default `maxAge` to `0`, so each check performs a fresh scrape unless you explicitly set a different `maxAge`.

Scrape target

```
{
  "type": "scrape",
  "urls": ["https://example.com/pricing"],
  "scrapeOptions": {
    "formats": ["markdown"],
    "maxAge": 0
  }
}
```

## [​](https://docs.firecrawl.dev/features/monitoring-page\#detecting-field-level-changes)  Detecting field-level changes

By default a page monitor diffs the page’s markdown. To alert only when a **specific field** changes, such as a price, a headline, an in-stock flag, or the items in a list, add a `changeTracking` format to the target’s `scrapeOptions`. See [Change tracking](https://docs.firecrawl.dev/features/monitoring#change-tracking) for JSON mode and mixed mode.

## [​](https://docs.firecrawl.dev/features/monitoring-page\#shared-configuration)  Shared configuration

- [Schedules](https://docs.firecrawl.dev/features/monitoring#schedules): cron or natural-language cadence, minimum 5 minutes.
- [Goals and judging](https://docs.firecrawl.dev/features/monitoring#goals-and-judging): alert only on meaningful changes.
- [Notifications](https://docs.firecrawl.dev/features/monitoring#notifications): webhook and email delivery.
- [Check results](https://docs.firecrawl.dev/features/monitoring#check-results): inspect each check and its per-page diffs.
- [Pricing](https://docs.firecrawl.dev/features/monitoring#pricing): 1 credit per URL per check, plus optional judging.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/features/monitoring-page.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/features/monitoring-page)

✕
