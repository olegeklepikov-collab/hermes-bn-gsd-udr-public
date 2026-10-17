> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка WebOfScience: developer-application-help

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="container">

<div class="navbar-header">

<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>

<a href="/" class="pull-left" target="_blank"><img src="/content/images/wicked-40.png" title="wicked project home" style="margin-top: 5px; margin-right: 5px;" /></a>

</div>

<div id="navbar" class="collapse navbar-collapse">

- Home (ссылка на локальный ресурс исходного примера; в переносимом пакете не поставляется)
- APIs (локальный ресурс исходного примера не включён)
- Applications (ссылка на локальный ресурс исходного примера; в переносимом пакете не поставляется)
- Contact (локальный ресурс исходного примера не включён)
- Content (локальный ресурс исходного примера не включён)

<!-- -->

- Log in (локальный ресурс исходного примера не включён)

</div>

</div>

<div class="container" style="padding-top: 50px">

<div class="row">

<div class="col-md-8">

<span id="subscriptions"></span>

#### Subscriptions

On the specific application page, the subscriptions an application has are displayed, including the API credentials (either API Key or Client ID and Secret). You can use the revela button (<span class="glyphicon glyphicon-eye-open"></span>) to show the credentials for this application and API. Also the authentication type ("Auth Type") is displayed, which is important when deciding on how to access the API programmatically (локальный ресурс исходного примера не включён).

\
<span id="app_name"></span>

#### Application Name

In the second section you may change the friendly name of the Application. Please note that the friendly name of the application is **only** used inside the API Portal for making it easier to identify a client application. It does not have any impact whatsoever on the logic behind; for that, the application ID is used.

In contrast to the friendly name, the application ID **can not be changed**. The ID is additionally also unique over the entire API Portal installation. It is not possible for two different developers/users to create an applications with identical application IDs.

\
<span id="owners"></span>

#### Owners

For a discussion of Application Owners, please see the page on application ownership (локальный ресурс исходного примера не включён).

\
<span id="why_applications"></span>

#### Why Applications?

After signing up and logging in to this API Portal, you will want to subscribe to an API. In order to do that, the API Portal forces you to create an "Application" which serves as the consumer, or client, of the API. The "Application" is the entity you tie a subscription to, and **not to your user**.

\
<span id="how_to_use"></span>

#### How to use an API

Let us look at the following diagram which shows how the intended use of an API which is published within an API Portal looks like:

<img src="/images/help/application-usage.png" class="center-block" />

- As a developer ("DEV" in the diagram), I visit the API Portal (I log in, I look around,...) and find the API which I want to use for the Application ("APP" in the diagram) I am currently developing.
- Inside the API Portal, I register my application (using the applications page (ссылка на локальный ресурс исходного примера; в переносимом пакете не поставляется)), so that the API Portal knows my application. It just needs an ID and a name of your application, nothing more.
- After registrering your application, you can subscribe to an API **for this application**.
- The API Portal will generate credentials (API Keys, OAuth Client ID/Secret) for your application, which you in turn use in your APP to actually access the API, via the API Gateway.

This enables the API Portal to create an abstract notion of applications inside the API Portal, and does not tie the subscriptions directly to the developer.

</div>

<div class="col-md-4 col-md-push-8" style="position:fixed">

### Help Index (локальный ресурс исходного примера не включён)

#### Site Map

- [Subscriptions](#subscriptions)
- [Application Name](#app_name)
- [Owners](#owners)
- [Why Applications?](#why_applications)
- [How to use an API](#how_to_use)

</div>

</div>

</div>

------------------------------------------------------------------------

<div class="container">

<table width="100%">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left; color: #999999;"><div class="col-xs-6">
©
<span></span>
</div>
<div class="col-xs-6 text-right">
<a href="https://clarivate.com/legal-center/terms-of-business">Terms of use</a>      <a href="https://clarivate.com/privacy-center/notices-policies/privacy-policy">Privacy policy</a>
</div>
<br />
</td>
<td style="text-align: right; color: #999999;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

</div>
