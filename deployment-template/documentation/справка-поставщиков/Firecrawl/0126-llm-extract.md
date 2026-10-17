> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Firecrawl: llm-extract

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


https://docs.firecrawl.dev/features/llm-extract

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.firecrawl.dev/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.firecrawl.dev/features/llm-extract#content-area)

**Picking the right tool.** JSON mode (this page) is right when you have **one URL** and want fields from that single page.

- For **anything beyond one URL** — multiple URLs, URL patterns, or agentic discovery — see [Agent](https://docs.firecrawl.dev/features/agent).
- Full comparison: [Choosing the Data Extractor](https://docs.firecrawl.dev/developer-guides/usage-guides/choosing-the-data-extractor).

**v2 API Change:** JSON schema extraction is fully supported in v2, but the API format has changed. In v2, the schema is embedded directly inside the format object as `formats: [{type: "json", schema: {...}}]`. The v1 `jsonOptions` parameter no longer exists in v2.

For schema validation failures and other extraction errors, see [Errors](https://docs.firecrawl.dev/api-reference/errors) — extraction-specific issues typically surface as `400` or `422` responses.

## [​](https://docs.firecrawl.dev/features/llm-extract\#scrape-and-extract-structured-data-with-firecrawl)  Scrape and extract structured data with Firecrawl

Firecrawl uses AI to get structured data from web pages in 3 steps:

1. **Set the Schema (optional):**
Define a JSON schema (using OpenAI’s format) to specify the data you want, or just provide a `prompt` if you don’t need a strict schema, along with the webpage URL.
2. **Make the Request:**
Send your URL and schema to our scrape endpoint using JSON mode. See how here:
[Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
3. **Get Your Data:**
Get back clean, structured data matching your schema that you can use right away.

This makes getting web data in the format you need quick and easy.

## [​](https://docs.firecrawl.dev/features/llm-extract\#extract-structured-data)  Extract structured data

### [​](https://docs.firecrawl.dev/features/llm-extract\#json-mode-via-/scrape)  JSON mode via /scrape

Used to extract structured data from scraped pages.

Python

Node

cURL

```
from firecrawl import Firecrawl
from pydantic import BaseModel

app = Firecrawl(
  # No API key needed to get started — add one for higher rate limits:
  # api_key="fc-YOUR-API-KEY",
)

class CompanyInfo(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

result = app.scrape(
    'https://firecrawl.dev',
    formats=[{\
      "type": "json",\
      "schema": CompanyInfo.model_json_schema()\
    }],
    only_main_content=False,
    timeout=120000
)

print(result)
```

```
import { Firecrawl } from "firecrawl";
import { z } from "zod";

const app = new Firecrawl({
  // No API key needed to get started — add one for higher rate limits:
  // apiKey: "fc-YOUR_API_KEY",
});

// Define schema to extract contents into
const schema = z.object({
  company_mission: z.string(),
  supports_sso: z.boolean(),
  is_open_source: z.boolean(),
  is_in_yc: z.boolean()
});

const result = await app.scrape("https://firecrawl.dev", {
  formats: [{\
    type: "json",\
    schema: schema\
  }],
});

console.log(result);
```

```
# No API key needed to get started — add -H "Authorization: Bearer YOUR_API_KEY" for higher rate limits:
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": [ {\
        "type": "json",\
        "schema": {\
          "type": "object",\
          "properties": {\
            "company_mission": {\
                      "type": "string"\
            },\
            "supports_sso": {\
                      "type": "boolean"\
            },\
            "is_open_source": {\
                      "type": "boolean"\
            },\
            "is_in_yc": {\
                      "type": "boolean"\
            }\
          },\
          "required": [\
            "company_mission",\
            "supports_sso",\
            "is_open_source",\
            "is_in_yc"\
          ]\
        }\
      } ]
    }'
```

Output:

## JSON

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### [​](https://docs.firecrawl.dev/features/llm-extract\#structured-data-without-schema)  Structured data without schema

You can also extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

Python

Node

cURL

```
from firecrawl import Firecrawl

app = Firecrawl(
  # No API key needed to get started — add one for higher rate limits:
  # api_key="fc-YOUR-API-KEY",
)

result = app.scrape(
    'https://firecrawl.dev',
    formats=[{\
      "type": "json",\
      "prompt": "Extract the company mission from the page."\
    }],
    only_main_content=False,
    timeout=120000
)

print(result)
```

```
import { Firecrawl } from "firecrawl";

const app = new Firecrawl({
  // No API key needed to get started — add one for higher rate limits:
  // apiKey: "fc-YOUR_API_KEY",
});

const result = await app.scrape("https://firecrawl.dev", {
  formats: [{\
    type: "json",\
    prompt: "Extract the company mission from the page."\
  }]
});

console.log(result);
```

```
# No API key needed to get started — add -H "Authorization: Bearer YOUR_API_KEY" for higher rate limits:
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": [{\
        "type": "json",\
        "prompt": "Extract the company mission from the page."\
      }]
    }'
```

Output:

## JSON

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### [​](https://docs.firecrawl.dev/features/llm-extract\#real-world-example-extracting-company-information)  Real-world example: Extracting company information

Here’s a comprehensive example extracting structured company information from a website:

Python

Node

cURL

```
from firecrawl import Firecrawl
from pydantic import BaseModel

app = Firecrawl(
  # No API key needed to get started — add one for higher rate limits:
  # api_key="fc-YOUR-API-KEY",
)

class CompanyInfo(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

result = app.scrape(
    'https://firecrawl.dev/',
    formats=[{\
        "type": "json",\
        "schema": CompanyInfo.model_json_schema()\
    }]
)

print(result)
```

```
import { Firecrawl } from "firecrawl";
import { z } from "zod";

const app = new Firecrawl({
  // No API key needed to get started — add one for higher rate limits:
  // apiKey: "fc-YOUR_API_KEY",
});

const companyInfoSchema = z.object({
  company_mission: z.string(),
  supports_sso: z.boolean(),
  is_open_source: z.boolean(),
  is_in_yc: z.boolean()
});

const result = await app.scrape("https://firecrawl.dev/", {
  formats: [{\
    type: "json",\
    schema: companyInfoSchema\
  }]
});

console.log(result);
```

```
# No API key needed to get started — add -H "Authorization: Bearer YOUR_API_KEY" for higher rate limits:
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://firecrawl.dev/",
      "formats": [{\
        "type": "json",\
        "schema": {\
          "type": "object",\
          "properties": {\
            "company_mission": {\
              "type": "string"\
            },\
            "supports_sso": {\
              "type": "boolean"\
            },\
            "is_open_source": {\
              "type": "boolean"\
            },\
            "is_in_yc": {\
              "type": "boolean"\
            }\
          },\
          "required": [\
            "company_mission",\
            "supports_sso",\
            "is_open_source",\
            "is_in_yc"\
          ]\
        }\
      }]
    }'
```

Output:

Output

```
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "Turn websites into LLM-ready data",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### [​](https://docs.firecrawl.dev/features/llm-extract\#json-format-options)  JSON format options

When using JSON mode in v2, include an object in `formats` with the schema embedded directly:`formats: [{ type: 'json', schema: { ... }, prompt: '...' }]`Parameters:

- `schema`: JSON Schema describing the structured output you want (required for schema-based extraction).
- `prompt`: Optional prompt to guide extraction (also used for no-schema extraction).
- `checkPromptInjection`: Optional boolean (default `false`). When enabled, Firecrawl scans the scraped page content for prompt injection attempts before running the extraction. See [Prompt injection detection](https://docs.firecrawl.dev/features/llm-extract#prompt-injection-detection).

**Important:** Unlike v1, there is no separate `jsonOptions` parameter in v2. The schema must be included directly inside the format object in the `formats` array.

### [​](https://docs.firecrawl.dev/features/llm-extract\#prompt-injection-detection)  Prompt injection detection

Web pages can contain hidden text crafted to hijack LLM-based extraction — for example, instructions that tell the model to ignore your schema and return attacker-controlled data. If you extract from untrusted or user-submitted URLs, you can enable an opt-in guard that checks the scraped content before your extraction runs:

```
{
  "url": "https://example.com",
  "formats": [\
    {\
      "type": "json",\
      "schema": { "type": "object", "properties": { "title": { "type": "string" } } },\
      "checkPromptInjection": true\
    }\
  ]
}
```

How it works:

- A dedicated classifier call inspects the scraped page content (it runs in parallel with the extraction, so enabling it does not slow down clean scrapes).
- If a prompt injection attempt is detected, the request fails with an HTTP `403` and the error code `SCRAPE_PROMPT_INJECTION_DETECTED` — no extraction output is returned.
- The check is billed as **+4 credits** on top of the standard JSON format cost when it runs. If the scrape fails after the check has run (including when an injection is detected and the request is blocked), **5 credits** are billed instead of the usual 0 for a failed scrape, since the classifier call still ran.

In v1, the same option is available as `jsonOptions.checkPromptInjection`. It is also exposed in all official SDKs (e.g. `checkPromptInjection` in the JS SDK, `check_prompt_injection` in the Python SDK’s v2 JSON format).

**HTML attributes are not available in JSON extraction.** JSON extraction works on the markdown conversion of the page, which only preserves visible text content. HTML attributes (e.g., `data-id`, custom attributes on elements) are stripped during conversion and the LLM cannot see them. If you need to extract HTML attribute values, use `rawHtml` format and parse attributes client-side, or use an `executeJavascript` action to inject attribute values into visible text before extraction.

## [​](https://docs.firecrawl.dev/features/llm-extract\#tips-for-consistent-extraction)  Tips for consistent extraction

If you are seeing inconsistent or incomplete results from JSON extraction, these practices can help:

- **Keep prompts short and focused.** Long prompts with many rules increase variability. Move specific constraints (like allowed values) into the schema instead.
- **Use concise property names.** Avoid embedding instructions or enum lists in property names. Use a short key like `"installation_type"` and put allowed values in an `enum` array.
- **Add `enum` arrays for constrained fields.** When a field has a fixed set of values, list them in `enum` and make sure they match the exact text shown on the page.
- **Include null-handling in field descriptions.** Add `"Return null if not found on the page."` to each field’s `description` so the model does not guess missing values.
- **Add location hints.** Tell the model where to find data on the page, e.g. `"Flow rate in GPM from the Specifications table."`.
- **Split large schemas into smaller requests.** Schemas with many fields (e.g. 30+) produce less consistent results. Split them into 2–3 requests of 10–15 fields each.
- **Avoid `minItems`/`maxItems` on arrays.** JSON Schema validation keywords like `minItems` and `maxItems` do not control how much content the scraper collects. Setting `minItems: 20` will not make the LLM return more items — it may instead hallucinate entries to satisfy the constraint. Remove these keywords and use a `prompt` instead (e.g. `"Extract ALL reviews from the page. Do not skip any."`) to guide completeness.
- **Use `"type": "array"` to extract lists of items.** If you need to extract multiple items (e.g. a list of people, products, or reviews), wrap them in an array property with an `items` block. Using `"type": "object"` for a list will return only a single item. See the array schema example below.

**Example of a well-structured schema:**

```
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": ["string", "null"],
      "description": "Full descriptive product name as shown on the page. Return null if not found."
    },
    "installation_type": {
      "type": ["string", "null"],
      "description": "Installation type from the Specifications section. Return null if not found.",
      "enum": ["Deck-mount", "Wall-mount", "Countertop", "Drop-in", "Undermount"]
    },
    "flow_rate_gpm": {
      "type": ["string", "null"],
      "description": "Flow rate in GPM from the Specifications section. Return null if not found."
    }
  }
}
```

**Example of extracting a list of items:**When a page contains multiple items (e.g. team members, products, reviews), use `"type": "array"` with `"items"` to get the full list:

```
{
  "type": "object",
  "properties": {
    "people": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "role": { "type": "string" },
          "department": { "type": "string" }
        }
      }
    }
  }
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

[Suggest edits](https://github.com/firecrawl/firecrawl-docs/edit/main/features/llm-extract.mdx) [Raise issue](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path:%20/features/llm-extract)

✕

- 👋 Hi! Power AI agents with clean web data!

- I can help with search, scrape, MCP setup, or billing.
