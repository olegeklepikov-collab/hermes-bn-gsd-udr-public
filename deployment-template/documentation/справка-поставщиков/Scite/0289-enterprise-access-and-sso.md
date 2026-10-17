> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Scite: enterprise-access-and-sso

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.scite.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise access and SSO

> Configure institutional access to Scite with SAML 2.0 SSO, OpenAthens, IP ranges, email domains, or managed user lists.

Scite supports several ways to give an organization access. Most institutions use IP ranges together with an approved email domain. Organizations that need centralized identity management can use SAML 2.0 single sign-on (SSO) or OpenAthens.

[Contact sales](https://scite.ai/contact-sales) to choose an access method or start an SSO configuration.

## Supported access methods

| Method | Best for | Setup |
| - | - | - |
| **IP ranges (CIDR)** | Access from a campus or corporate network | Provide the public IP ranges that should receive access. |
| **Email domain** | Users with an organization-managed email address | Approve one or more email domains for the organization. |
| **Approved email list** | A defined group that cannot be represented by a domain | Provide the email addresses that should receive access. |
| **SAML 2.0 SSO** | Centralized sign-in, account lifecycle management, and optional password-login restrictions | Configure a connection between your identity provider and Scite. |
| **OpenAthens (OIDC)** | Institutions that manage access through OpenAthens | Configure an OpenAthens connection with Scite. |
| **Partner autologin** | Approved partner or platform integrations | Contact Scite to discuss an integration. |

IP range and email-domain access are the most common combination and can usually be enabled quickly. SSO requires configuration and testing for each institution.

## SAML 2.0 compatibility

Scite is identity-provider agnostic. It works with standards-compliant SAML 2.0 identity providers, including Okta, Microsoft Entra ID, Shibboleth, and other institutional identity platforms. Scite has more than 14 identity-provider configurations in production.

An organization can have more than one identity-provider connection. This is useful for consortia, organizations with separate user populations, and identity-provider migrations.

## Set up SAML SSO

<Steps>
  <Step title="Send your identity-provider metadata">
    Send Scite your IdP metadata XML. It normally contains the SSO entry-point URL, issuer or entity ID, and public signing certificate.
  </Step>

  <Step title="Register Scite with your identity provider">
    Scite provides the Assertion Consumer Service (ACS) URL and other service-provider details needed to create the application in your IdP.
  </Step>

  <Step title="Configure the email attribute">
    Confirm which SAML attribute contains the user's email address. Scite can configure the attribute name for your connection.
  </Step>

  <Step title="Test before rollout">
    Complete at least one successful sign-in with a test user. Confirm that the user reaches the correct organization and that any existing Scite account is preserved.
  </Step>

  <Step title="Share your organization sign-in page">
    Your branded sign-in page follows `https://scite.ai/enterprise/{org-slug}`. Link to it from your intranet, library portal, or other member resources.
  </Step>
</Steps>

## Email attribute requirements

<Warning>
  Every SAML assertion must resolve to an email address. Sign-in fails if Scite cannot find one; there is no anonymous-account fallback.
</Warning>

Scite can read the email from a configured SAML attribute. Standard email fields such as `email`, `mail`, or an email-formatted NameID often work, but you should confirm the exact claim your IdP sends before launch.

### Microsoft Entra ID

Microsoft Entra ID configurations vary. An assertion may use a namespaced claim for email, while NameID may contain a user principal name or another identifier. Before go-live, inspect a test assertion and either:

* map the user's email address to a standard email claim; or
* tell Scite the exact attribute name that contains the email address.

This check prevents one of the most common SAML setup problems.

## Match existing Scite accounts

The email asserted by the IdP should match the email on the user's existing Scite account. Scite treats letter-case differences as the same address, but it cannot automatically link genuinely different addresses.

Before rollout, ask users with personal, legacy, or renamed email addresses to update their Scite account to the address the IdP will send. Otherwise, their first SSO sign-in may create a separate account instead of opening their existing one.

## Require SSO for your organization

Scite can require organization members to use SSO instead of a password. To prevent an organization from locking itself out, enforcement is available only after the SAML connection has completed a successful test sign-in.

Keep at least one tested administrator path available while you change identity-provider settings. Coordinate enforcement changes with Scite.

## Rotate a signing certificate

Scite supports overlapping signing certificates so organizations can rotate a certificate without planned sign-in downtime. Send the replacement certificate to Scite before the current certificate expires, test the new certificate, and remove the old certificate after the rotation is complete.

## Use SSO accounts with MCP

MCP does not authenticate directly with SAML. It uses OAuth for interactive clients or an API key for programmatic access.

When your organization is configured to retain license access on user accounts, a user can sign in to [scite.ai](https://scite.ai) through SSO once and then authorize MCP with the same account. The organization access associated with that account carries into the MCP OAuth flow.

See Scite MCP authentication (локальный ресурс исходного примера не включён) for client setup.

## Get help

[Contact sales](https://scite.ai/contact) to configure institutional access, request SAML or OpenAthens setup, plan a certificate rotation, or discuss a partner autologin integration.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
