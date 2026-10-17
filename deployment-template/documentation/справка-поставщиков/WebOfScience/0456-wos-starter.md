> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка WebOfScience: wos-starter

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

<div class="jumbotron wicked-api-title">

<div class="container wicked-title-container">

<div class="row">

<div class="col-md-8">

# Web of Science Starter API

The Web of Science™ Starter API allows for a real-time check of bibliographic metadata such as DOI, author, source title, etc., against the Web of Science Core Collection and other Web of Science Product Databases. This enables building article-level links to the Web of Science from external systems and retrieving times-cited counts from the Web of Science.

</div>

<div class="col-md-4">

\
<img src="/images/key-icon-64.png" title="API is secured with API keys" data-align="right" />

</div>

</div>

</div>

</div>

<div class="container wicked-container">

<div class="panel panel-default">

<div class="panel-heading">

<table width="100%">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><h4 id="api-settings" class="panel-title">API Settings</h4></td>
<td style="text-align: right;"><a href="/help/api" target="_blank">Help</a></td>
</tr>
</tbody>
</table>

</div>

<div class="panel-body">

API URLs:\

</div>

</div>

<div class="panel panel-default">

<div class="panel-heading">

<table width="100%">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><h4 id="description" class="panel-title"><span data-toggle="collapse" data-target="#apidescription" role="button">Description <span class="glyphicon glyphicon-chevron-down"></span></span></h4></td>
<td style="text-align: right;"><a href="/help/api" target="_blank">Help</a></td>
</tr>
</tbody>
</table>

</div>

<div id="apidescription" class="collapse panel-collapse in">

<div class="panel-body">

> This API replaces previous [Links Article Match Retrieval (Links AMR) Service](https://help.incites.clarivate.com/LAMRService/WebServicesOverviewGroup/overview.html) and [Web of Science API Lite](https://developer.clarivate.com/apis/woslite).

This API provides REST-based programmatic access to the [Web of Science™](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) documents and journals, with JSON output format and basic search and filter capabilities. The Web of Science™ is the information and technology provider for the global scientific research community. We provide data, analytics, insights, workflow tools, and bespoke professional services to researchers and the entire research community that underpins research – universities and research institutions, national and local governments, private and public research funding organizations, publishers, and research-intensive corporations across the world.

### Who is the Web of Science Starter API for?

You can integrate this API to maintain a high quality of basic metadata, and times-cited counts of Web of Science documents and journals, including the Web of Science (Source, Citing and Cited References, Related) and Journal Citations Reports Profile URLs. It is a perfect addition for:

- **Students and Researchers** - Use this API to keep track of the times-cited count of your papers and links to the Web of Science. You may also look for native integrations of 3rd party tools.
- **Publishers and editors** - Keep track of times-cited counts of journal articles and link to the Web of Science or link the Journals to the Journal Citation Reports from your systems.
- **Librarians** - Understand which journals are the most important to your institution's and researchers' success.
- **Research managers and information analysts** - Track basic bibliometric metadata and citations to support strategy and funding decisions, as well as highlight your institution's impact on the research community.

### Subscription and access

Access to this API has different plans, including a free one. [Web of Science](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) subscribers can access the times-cited counts of articles and may have an advanced plan with 5,000 requests per day. Don't hesitate to [get in touch with us](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/web-of-science-apis-and-xml-data/) with any questions you may have.

This API uses an [API Key access](https://developer.clarivate.com/help/api-access#key_access). All APIs in our Developer Portal require registering an [application](https://developer.clarivate.com/help/application).

By requesting credentials, you agree to adhere to this Portal's [Terms of Use](https://clarivate.com/wp-content/uploads/dlm_uploads/2019/08/End-User-Terms.pdf) and [Product / Service Terms](https://clarivate.com/download/web-of-science-apis/).

#### Plans

##### Free Trial Plan

This plan is available to anyone, even if your organization does not subscribe to Web of Science. It does not return times cited and is limited to 50 requests per day. Ideal for personal and evaluation purposes.

##### Free Institutional Member Plan

Available to members of organizations that subscribe to Web of Science, this plan returns times cited and allows up to 5,000 requests per day.

##### Free Institutional Integration Plan

Designed for institutions requiring higher usage limits, this plan allows up to 20,000 requests per day. It supports seamless integration and synchronization of Web of Science documents with internal systems. Approval is limited to administrative staff of the organization.

##### Throttling Configuration

| Plan                                | Requests per Second | Requests per Day |
|-------------------------------------|---------------------|------------------|
| Free Trial Plan                     | 1                   | 50               |
| Free Institutional Member Plan      | 5                   | 5,000            |
| Free Institutional Integration Plan | 5                   | 20,000           |

### Related links

- [Code samples (GitHub)](https://github.com/clarivate?q=wosstarter&type=&language=&sort=)
- [Web of Science Documentation](https://webofscience.help.clarivate.com/en-us/Content/home.htm)
- [Web of Science - Product Page](https://clarivate.com/webofsciencegroup/solutions/web-of-science/)
- [Clarivate - Web of Science LibGuide](https://clarivate.libguides.com/home)
- [Web of Science API Release Notes](https://clarivate.com/release-notes/wos-apis/)

cortellis-np-drugs-api,cortellis-np-companies-api,cortellis-np-sources-api,cortellis-np-drugs-api-eu,cortellis-np-drugs-api-us,cortellis-np-companies-api-eu,cortellis-np-companies-api-us,cortellis-np-sources-api-us,cortellis-np-sources-api-eu

<a href="https://api.clarivate.com/swagger-ui/?apikey=${SECRET} УДАЛЁН] УДАЛЁН]&amp;url=https%3A%2F%2Fdeveloper.clarivate.com%2Fapis%2Fwos-starter%2Fswagger" class="btn btn-default" role="button" target="_blank">View Technical Documentation/ Swagger Definition »</a>

</div>

</div>

</div>

<div class="panel panel-danger custom-hide">

<div class="panel-heading">

#### Not logged in

</div>

<div class="panel-body">

You are currently not logged in, so we can't display your registered applications. Please log in first.

<a href="/login?redirect=/apis/wos-starter" class="btn btn-default">Log in »</a>

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
