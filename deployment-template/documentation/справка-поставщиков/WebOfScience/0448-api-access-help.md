> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка WebOfScience: api-access-help

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

<span id="key_access"></span>

#### Accessing using an API Key

If the API you subscribe to is secured via an API Key, you will have to pass on this API Key to the API Gateway in a HTTP Header. Using `curl`, this will look as follows:

    $ curl -H 'X-ApiKey: (your API Key)' https://api.clarivate.com/desired_api/some_endpoint

If you pass on a correct API Key, the API Gateway will let you call the backend API, using the plan you selected when subscribing to the API, for your application.

**Note:** Please be aware that the API key is bound to the application (локальный ресурс исходного примера не включён) it was generated for. You should have different API keys for different applications. Do not re-use the API Keys, even if it is possible (the API Gateway cannot notice).

\
<span id="oauth2_access"></span>

#### Accessing using OAuth 2.0 Client Credentials Flow

If the API you have subscribed to is secured via the <a href="https://tools.ietf.org/html/rfc6749" target="_blank">OAuth 2.0 Client Credentials Flow</a>, you will first need to acquire an Access Token for the API before you can call any of the API end points.

Leveraging `curl`, the call has to look as follows:

    $ curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=client_credentials&client_id=(your client id)&client_secret=(your client secret)' 'https://api.clarivate.com/auth/(auth method)/api/(desired api)/token'

Please note that the same kind of request has to be used regardless of the API in the backend. The `/oauth2/token` end point is not actually provided by the backend API, but by the API Gateway. This means the authorization calls will always look the same, no matter which API (here e.g. `/desired_api/`) is to be used.

If the `POST` request was successful, you will receive an access token which is valid for a certain period of time:

`{"token_type":"bearer","access_token": "`**`db530d89558843a99ec80f639434faa8`**`","expires_in": 3600}`

In green above, the access token is highlighted. This can in turn be used for real calls to the API in the background, using the same example URL as above, this would be:

    $ curl --header 'Authorization: Bearer [СЕКРЕТ УДАЛЁН]' https://api.clarivate.com/desired_api/some_endpoint

Chances are good that this kind of authorization is automatically supported in case you are using common frameworks when implementing your application, such as Java Spring. For you, calling an API would be transparent, as long as you provide your framework with Client ID and Client Secret. This is though very implementation specific and is not covered further here.

See also:

- OAuth2 Client Credentials Flow (локальный ресурс исходного примера не включён)
- OAuth2 Resource Owner Password Grant (локальный ресурс исходного примера не включён)
- OAuth2 Implicit Grant (локальный ресурс исходного примера не включён)
- OAuth2 Authorization Code Grant (локальный ресурс исходного примера не включён)

Depending on the API and the type of authentication (auth method), wicked supports all the above OAuth2 flows.

</div>

<div class="col-md-4 col-md-push-8" style="position:fixed">

### Help Index (локальный ресурс исходного примера не включён)

#### Site Map

- [Accessing using an API Key](#key_access)
- [Accessing using OAuth 2.0 Client Credentials Flow](#oauth2_access)

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
