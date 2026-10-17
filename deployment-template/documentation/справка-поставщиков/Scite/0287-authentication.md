> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: authentication

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get API key

> Authenticate with an API key or Enterprise credentials.

Papers and Tallies are public and don't require an API key. All other Scite endpoints require an API key. You must create at least one API key to use Scite through code.

<Note>
  Looking for SAML, SSO, IP-based access, or OpenAthens? See Enterprise access and SSO (локальный ресурс исходного примера не включён). This page covers credentials for the Scite API.
</Note>

## Choose an authentication option

<CardGroup cols={2}>
  <Card title="API key" icon="key" href="https://scite.ai/users/me/api">
    Create a key in the API Console and send it directly with each request. No token exchange is required.
  </Card>

  <Card title="Enterprise credentials" icon="building" href="https://scite.ai/contact">
    Exchange a Scite-issued `client_id` and `client_secret` for a short-lived access token.
  </Card>
</CardGroup>

| Option | Best for | How it works |
| - | - | - |
| **API key** | Individual users and lower-volume integrations | Create a key in the API Console and send it directly with each request. |
| **Enterprise credentials** | Organizations with high-volume or managed server-to-server integrations | Exchange a Scite-issued `client_id` and `client_secret` for a two-hour access token. |

If you're an individual developer, start with a API key. Enterprise access is intended primarily for organizations that need higher usage limits or managed credentials.

## API keys

Create and manage keys in the [API Console](https://scite.ai/users/me/api). Self-service API keys require a Pro plan.

<Steps>
  <Step title="Create and copy a key">
    Choose the scopes your integration needs, then copy the key when it appears. Scite only shows the full key once.
  </Step>

  <Step title="Send the key">
    Add the key to the `Authorization` header:

    ```bash theme={null}
    export SCITE_API_KEY='<YOUR_API_KEY>'

    curl -G 'https://api.scite.ai/api_partner/search' \
      -H "Authorization: Bearer $SCITE_API_KEY" \
      --data-urlencode 'term=CRISPR' \
      --data-urlencode 'limit=1'
    ```
  </Step>
</Steps>

The API Console only shows scopes available to your account. Creating a key does not grant access to additional features. Use the narrowest scopes your integration needs.

## Enterprise credentials

Enterprise authentication is for organizations that need higher usage limits or managed server-to-server credentials. [Contact sales](https://scite.ai/contact) to get a `client_id` and `client_secret`.

<Steps>
  <Step title="Request an access token">
    Exchange your credentials at the token endpoint:

    ```bash theme={null}
    curl -X POST 'https://api.scite.ai/auth_token_users/token' \
      -H 'Content-Type: application/json' \
      -d '{
        "client_id": "<YOUR_CLIENT_ID>",
        "client_secret": "<YOUR_CLIENT_SECRET>",
        "grant_type": "client_credentials"
      }'
    ```

    The response includes an `access_token`. It expires after two hours.
  </Step>

  <Step title="Send the access token">
    Add the token to the same `Authorization` header:

    ```bash theme={null}
    curl -G 'https://api.scite.ai/api_partner/search' \
      -H 'Authorization: Bearer <ACCESS_TOKEN>' \
      --data-urlencode 'term=CRISPR' \
      --data-urlencode 'limit=1'
    ```
  </Step>
</Steps>

<Warning>
  Keep API keys and Enterprise credentials out of source control and client-side code. Store them in an environment variable or secret manager.
</Warning>

## Authentication errors

* `401 Unauthorized` means the credential is missing, invalid, expired, or revoked.
* `403 User not authorized` means the credential is valid, but the account or key lacks access to that feature.

See Errors and rate limits (локальный ресурс исходного примера не включён) for troubleshooting. For MCP clients, see Scite MCP authentication (локальный ресурс исходного примера не включён).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
