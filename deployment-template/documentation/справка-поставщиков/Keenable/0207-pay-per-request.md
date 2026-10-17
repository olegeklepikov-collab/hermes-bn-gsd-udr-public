> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Keenable: pay-per-request

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.keenable.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pay per request (x402)

> Call search and fetch with no account and no API key: each request pays $0.01 in USDC on Base over the x402 protocol.

[x402](https://www.x402.org) is an open payment protocol built on HTTP `402 Payment Required`. Keenable accepts it on its own paths, so an agent with a wallet can search and fetch without signing up, holding a key, or topping up a balance: every request pays for itself.

**\$0.01 per request**, in USDC on Base (`eip155:8453`). The buyer needs USDC only — no ETH for gas, because the payment is a signed transfer authorization (EIP-3009) that the payment network submits on your behalf.

If you call Keenable regularly, an API key (локальный ресурс исходного примера не включён) is the better deal: prepaid credits (локальный ресурс исходного примера не включён) cost \$4 per 1,000 requests rather than \$10, and keyed rate limits (локальный ресурс исходного примера не включён) can be raised. x402 is for agents that have no account and no key.

## Endpoints

| Endpoint | Method | Path | Same parameters and response as |
| - | - | - | - |
| Search | `GET`, `POST` | `/v1/x402/search` | `/v1/search` (локальный ресурс исходного примера не включён) |
| Fetch | `GET` | `/v1/x402/fetch` | `/v1/fetch` (локальный ресурс исходного примера не включён) |

`GET` search takes its parameters in the query string; `POST` takes the same JSON body as `/v1/search`.

An API key sent to these paths is ignored — for keyed access, call `/v1/search` and `/v1/fetch`. The `webql` and `realtime_content` search modes (локальный ресурс исходного примера не включён) are available with an API key only and answer `403` here.

## How a paid call works

<Steps>
  <Step title="Ask">
    Call the endpoint without payment. The answer is `402`, with the offer in the `PAYMENT-REQUIRED` header as base64-encoded JSON. The same offer is mirrored in the body.
  </Step>

  <Step title="Pay">
    Sign one of the `accepts` options and send the same request again with the signed payload in the `PAYMENT-SIGNATURE` header.
  </Step>

  <Step title="Receive">
    Keenable verifies the payment, runs the request and settles the payment on-chain. The result is returned only after settlement succeeds, with the receipt — including the transaction hash — in the `PAYMENT-RESPONSE` header.
  </Step>
</Steps>

The offer looks like this:

```bash theme={"system"}
curl -i "https://api.keenable.ai/v1/x402/search?query=typescript+best+practices"
```

```json theme={"system"}
{
  "x402Version": 2,
  "error": "Payment required",
  "resource": { "url": "https://api.keenable.ai/v1/x402/search" },
  "accepts": [
    {
      "scheme": "exact",
      "network": "eip155:8453",
      "amount": "10000",
      "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      "payTo": "0x…",
      "maxTimeoutSeconds": 300,
      "extra": { "name": "USD Coin", "version": "2" }
    }
  ]
}
```

`amount` is in USDC base units (6 decimals), so `10000` is \$0.01. `asset` is the USDC contract on Base. A signed payment stays valid for `maxTimeoutSeconds`.

## Using an x402 client

Any standard x402 v2 client handles the ask–pay–receive loop for you. With the official [`@x402/fetch`](https://www.npmjs.com/package/@x402/fetch) package:

```bash theme={"system"}
npm install @x402/fetch @x402/evm viem
```

```typescript theme={"system"}
import { wrapFetchWithPaymentFromConfig, decodePaymentResponseHeader } from "@x402/fetch";
import { ExactEvmScheme } from "@x402/evm/exact/client";
import { privateKeyToAccount } from "viem/accounts";

const account = privateKeyToAccount(process.env.WALLET_PRIVATE_KEY as `0x${string}`);

const fetchWithPayment = wrapFetchWithPaymentFromConfig(fetch, {
  schemes: [{ network: "eip155:8453", client: new ExactEvmScheme(account) }],
});

const query = "typescript best practices";
const res = await fetchWithPayment(
  `https://api.keenable.ai/v1/x402/search?query=${encodeURIComponent(query)}`,
);

const { results } = await res.json();
const receipt = decodePaymentResponseHeader(res.headers.get("PAYMENT-RESPONSE")!);
console.log(results.length, receipt.transaction);
```

The wallet behind `account` needs a USDC balance on Base and nothing else. Keep that balance small: a client signs whatever amount the offer asks for, so check the offer — or set a spending limit in your client — before giving an agent a funded key.

## What is charged

* A request is charged only once it has succeeded and its payment has settled.
* A response of `400` or above is never charged: bad parameters, a page that cannot be fetched, an upstream failure.
* If settlement fails after the request ran, the answer is `402 Payment settlement failed` and the result is withheld. Retry with a new payment.
* Each signed payment is good for one request. Sending the same signature again is rejected.

## Limits

| Limit | Value |
| - | - |
| Paid requests per paying wallet | 50 per second |
| Requests per IP | 100 per second |
| Hourly cap | none |

The per-IP limit counts both halves of a paid call — the unpaid request that returns the offer and the paid retry — which is why it is twice the wallet limit. A `429` carries `Retry-After`. See rate limits (локальный ресурс исходного примера не включён) for how this compares to keyed and keyless access.

## Errors

| Status | Meaning |
| - | - |
| `402` | Payment required — the offer, a payment that was rejected, or a settlement that failed |
| `403` | The requested search mode needs an API key (`webql`, `realtime_content`) |
| `429` | Rate limit exceeded, per wallet or per IP |
| `451` | Unavailable for legal reasons — pay-per-request access is not offered in Cuba, Iran, North Korea, Syria, or the Crimea, Donetsk and Luhansk regions of Ukraine |
| `503` | Payments are temporarily unavailable — retry shortly, or use an API key |

A `451` is returned before any offer is made, so nothing is signed or charged.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
