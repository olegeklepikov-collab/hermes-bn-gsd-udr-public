> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Crossref: rate-limits

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


"{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"BreadcrumbList\",\n  \"itemListElement\": [\n    {\n      \"@type\": \"ListItem\",\n      \"item\": \"https://www.crossref.org/\",\n      \"name\": \"Home\",\n      \"position\": 1\n    },\n    {\n      \"@type\": \"ListItem\",\n      \"item\": \"https://www.crossref.org/blog/\",\n      \"name\": \"Blog\",\n      \"position\": 2\n    },\n    {\n      \"@type\": \"ListItem\",\n      \"name\": \"Announcing changes to REST API rate limits\",\n      \"position\": 3\n    }\n  ]\n}"
"{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"BlogPosting\",\n  \"author\": [\n    {\n      \"@type\": \"Person\",\n      \"name\": \"Martyn Rittman\"\n    },\n    {\n      \"@type\": \"Person\",\n      \"name\": \"Luis Montilla\"\n    }\n  ],\n  \"dateModified\": \"2026-09-17T10:14:43-04:00\",\n  \"datePublished\": \"2025-11-05T00:00:00Z\",\n  \"description\": \"\\u003cp\\u003eOur \\u003ca href=\\\"/documentation/retrieve-metadata/rest-api/\\\"\\u003eREST API\\u003c/a\\u003e makes all of the metadata we hold publicly available. It receives the majority of our API traffic, with around 1 billion hits per month. It’s …\\u003c/p\\u003e\",\n  \"headline\": \"Announcing changes to REST API rate limits\",\n  \"identifier\": \"https://doi.org/10.64000/wadve-3tj60\",\n  \"publisher\": {\n    \"@type\": \"Organization\",\n    \"name\": \"Crossref\",\n    \"url\": \"https://www.crossref.org/\"\n  },\n  \"url\": \"https://www.crossref.org/blog/announcing-changes-to-rest-api-rate-limits/\"\n}"
Announcing changes to REST API rate limits - Crossref
Menu
Home
Home
Join
Members
Documentation
Forum
Blog
Contact
Get involved
Overview
Become a member
Events
Service providers
Special programs
Working for you
Data citation
Sponsors program
Ambassadors
Working groups
Code of conduct
Fees
API Learning Hub
Find a service
Overview
Content Registration
Metadata Retrieval
Metadata Plus
Grant Linking System (GLS)
Research Organization Registry (ROR)
Open Funder Registry (OFR)
Support for Reference Linking
Similarity Check
Cited-by
Crossmark
Documentation
Overview
Setting up as a member
The Research Nexus
Metadata principles and practices
Register and maintain your records
Schema library
Reports
Crossmark
Cited-by
Similarity Check
Metadata Retrieval
About us
Overview
Operations & sustainability
Board & governance
Publications
Strategic agenda and roadmap
Our truths
Our people
Organisation chart
Jobs
Latest blog posts
2026 October 06
How Grobid uses Crossref metadata to enrich bibliographic information
Crossref members register around 37,000 records daily. All this metadata is openly shared with the global scholarly community through our free APIs. We receive over two billion calls to our API each month, signalling its use by hundreds of tools and services worldwide, supporting the discovery and assessment of scholarly metadata. As part of a new series in our blog, we will spotlight the diversity of tools and integrations that rely on Crossref metadata to serve the scholarly community. In this initial post, we chat to Luca Foppiano, the developer and maintainer of Grobid1, to learn about how Grobid uses Crossref metadata to improve the extraction and enrichment of bibliographic information from scholarly PDFs.
...Find out more
2026 September 21
2026 board election slate
On behalf of the Nominating Committee, I’m pleased to share the slate of candidates for the 2026 board election. Every active member organisation is invited to submit a ballot to elect the incoming board class.
...Find out more
2026 September 17
July 2026 board meeting summary
We’re providing a summary of the board’s July 2026 meeting. The July board meeting is our only in-person meeting. The board gathers for two days of strategic thinking and long-range planning, as well as conducting annual board business. This year, we focused on allocating surplus funds we have on hand to invest in a three-year project to redesign the content system. In a related discussion, we decided to lower content registration fees starting in 2027 because we’ve had a demonstrated history of generating surpluses, exceeding what we need to run Crossref. We also discussed the board structure, as part of our regular review of stakeholder governance. And we conducted annual board business, such as approving the audited financial statements and reviewed our risk register and mitigation plans.
The
resolutions are available
on the dedicated section of our website, which also lists the members of the Board and offers further information about our governance.
We also managed to squeeze in watching a World Cup game over dinner.
...Find out more
2026 September 15
Improving how funding connects to research outputs
Starting today, funder names deposited in Crossref metadata without an identifier will be matched to ROR IDs, to support an open and connected
Research Nexus
. Funding information is an increasingly important part of the scholarly record. The improved matching strategy supports researchers, funders, institutions, and meta-researchers, who rely on that information to understand how research is supported and what outcomes that support produces.
...Find out more
Menu
search
Blog
Home
>
Blog
>
Announcing changes to REST API rate limits
https://doi.org/10.64000/wadve-3tj60
5 minute read.
Announcing changes to REST API rate limits
Martyn Rittman
,
Luis Montilla
– 2025 November 05
In
APIs
Metadata
Standards
Our
## REST API
makes all of the metadata we hold publicly available. It receives the majority of our API traffic, with around 1 billion hits per month. It’s one of the key ways that we fulfil our mission to make research objects easy to find, cite, link, assess, and reuse. From 1 December 2025, we will be revising the rate limits for the public and polite pools of the REST API to ensure that we can maintain a stable and reliable system, and that metadata is freely available to everyone.
We haven’t changed the rate limits since the REST API was launched in 2013. In the past five years, the number of requests to the REST API has tripled and the number of metadata records has increased by a third, from 120 million to around 180 million. This means an increase in the resources needed to run it, and we’ve seen periods of instability where we haven’t been able to keep the API available for all users. We have decided that it is the right time to revisit rate limits to check that they’re in line with what our technology can provide and what our community needs. As a result, we will apply the following for the public and polite pools:
Public pool:
Request type
Rate limit
Concurrency limit
Single record
5
1
List of records (queries, filters, etc.)
1
1
Polite pool:
Request type
Rate limit
Concurrency limit
Single DOI record
10
3
List of records (queries, filters, etc.)
3
3
The rate limit is the number of total requests that can be made per second. The concurrency limit is how many requests can be running at the same time. This means that for longer-running requests you may need to wait for previous requests to finish before you can make a new one.
Here are some examples of single records requests:
https://api.crossref.org/v1/works/10.1002/cphy.cp010129
https://api.crossref.org/v1/journals/0266-612X&mailto=my@email.com
The second case here will be directed to the polite pool because an email is included using the ‘mailto’ parameter. And here are examples of requests that return lists of records:
https://api.crossref.org/v1/works?filter=from-created-date:2025-10-21T16:20,until-created-date:2025-10-21T17:00
https://api.crossref.org/v1/members/13/works&mailto=my@email.com
https://api.crossref.org/v1/works?query.bibliographic=linear+dichroism&mailto=my@email.com
The second and third examples here will use the polite pool.
Our guiding principle in making these changes is to keep all of the metadata available to everyone, all of the time. These changes to rate limits won’t restrict current users from accessing the metadata they want to retrieve, but it will make it easier for us to maintain the system now and in the future.
Which use cases do we support?
Our metadata has a broad range of applications. If you’re someone who uses the REST API, we’re glad that you are part of our community! Our mission includes making it easier to find, reuse, and assess scholarly research outputs. By using metadata, you’re helping us to fulfil that goal.
The main uses of the REST API fit into several categories. The new rate limits will continue to support these, among many others:
I have some metadata, what is the DOI?
I have a DOI, what is its metadata?
I want all of the metadata, just give me everything.
Research on a specific topic or subset of metadata, often refreshing the results every few weeks or months.
Rate limits can encourage responsible usage. The majority of API users make requests at a low rate and will not need to make any changes, however a few send spikes of large numbers of requests in a short space of time, sometimes making it difficult for others to access the service. These can be smoothed out by lower rate limits. Complex requests that search across large numbers of items put more pressure on our systems than requests for a single content item, so we have decided to set different rate limits for different types of request.
Who will be affected?
We estimate that the changes might affect around 40 users per week across the public and polite pools, and this is only for some of their requests. In all of the cases we’ve seen, the rate of requests could be slowed down and users would still be able to get the same results. In other words, the aim of these changes is to make the load on the API more predictable, not to reduce the total number of requests or amount of metadata transferred. No changes are being made to the
Metadata Plus
service or other APIs, such as the XML API and OAI-PMH endpoint.
Do I need to change how I use the API?
If you’re reading this, thank you! It’s clear that you want to be a considerate user of our services. Almost all users can continue to use the REST API in exactly the same way, you won’t need to change anything. Here is some general advice that will help you make the most of the service and ensure that you won’t encounter issues.
Use a mailto parameter. This gives you access to the polite pool meaning higher rate limits and meaning we can get in touch with you if needed. We’ll only use your address to contact you about your API requests.
Check the HTTP response status for your requests. This is always good practice and can help you identify malformed requests and where you reach rate limits.
Cache results to avoid repeatedly making the same requests. Most records don’t change on a regular basis. How often you update the cache will depend on what you are interested in, but most metadata fields rarely change.
If you are making a very high volume of requests or have very complex analysis to carry out, consider downloading the
public data file
which is made available once a year and contains all of our metadata. You can update it with recent additions using the REST API.
If you are relying on our metadata in a production service,
Metadata Plus
can provide more stability, support, and access to monthly snapshots of our entire database.
We have more
tips and tricks
for the REST API in our documentation. If you have questions, please join the conversation on our Community Forum.
Related reading
Blog
2026 public data file now available
Read more →
Blog
2025 public data file now available
Read more →
Blog
2024 public data file now available, featuring new experimental formats
Read more →
DiscourseEmbed={discourseUrl:"https://community.crossref.org/",discourseEmbedUrl:"https://www.crossref.org/blog/announcing-changes-to-rest-api-rate-limits/"},function(){var e=document.createElement("script");e.type="text/javascript",e.async=!0,e.src=DiscourseEmbed.discourseUrl+"javascripts/embed.js",(document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]).appendChild(e)}()
RSS feed
Recent blog posts
How Grobid uses Crossref metadata to enrich bibliographic information
2026 October 06
2026 board election slate
2026 September 21
July 2026 board meeting summary
2026 September 17
Improving how funding connects to research outputs
2026 September 15
Topics
Metadata
(173)
Community
(147)
Identifiers
(103)
Meetings
(76)
Member Briefing
(72)
Collaboration
(66)
Linking
(51)
Content Registration
(49)
APIs
(47)
Research Nexus
(44)
Citation
(43)
Governance
(37)
Event Data
(34)
## R&D
(34)
Board
(33)
DOIs
(33)
Annual Meeting
(29)
Interoperability
(27)
Membership
(27)
DataCite
(26)
Data
(25)
Elections
(25)
Persistence
(25)
Research Funders
(24)
## ORCID
(23)
Search
(23)
Publishing
(21)
Staff
(21)
Grant Linking System
(20)
API Case Study
(18)
Standards
(18)
Strategy
(18)
Infrastructure
(17)
Linked Data
(16)
Preprints
(16)
Research Integrity
(16)
Metadata Matching
(15)
Schema
(15)
Crossmark
(14)
Wikipedia
(14)
## XMP
(14)
Handle
(12)
News Release
(12)
Sustainability
(12)
## ROR
(11)
## RSS
(11)
Citation Formats
(10)
Metadata Manager
(10)
Archives
2026
(45)
2025
(51)
2024
(37)
2023
(31)
2022
(31)
2021
(25)
2020
(34)
2019
(37)
2018
(55)
2017
(41)
2016
(50)
2015
(23)
2014
(4)
2013
(2)
2012
(5)
2011
(6)
2010
(9)
2009
(34)
2008
(56)
2007
(91)
2006
(21)
Join the community
Get email updates
Membership
Governance
Sustainability
Services
Documentation
Status page
API Learning Hub
Community forum
Join
Contact
Jobs
Blog
The content of this site is licensed under a
Creative Commons Attribution 4.0 International License
Accessibility
Privacy
(function(e,t,n,s,o){e[t]=e[t]||{},e[t][n]=e[t][n]||{q:[],track:function(e,t,n){this.q.push({r:e,e:t,t:n||+new Date})}};var i=s.createElement(o),a=s.getElementsByTagName(o)[0];i.async=1,i.src="//outreach.crossref.org/cdnr/93/acton/bn/tracker/16781",a.parentNode.insertBefore(i,a)})(window,"ActOn","Beacon",document,"script"),ActOn.Beacon.track()
function fakeClick(){$('a[href="#tabs-metadatasearch"]').trigger("click")}var $searchstring="";jQuery(document).ready(function(e){var t,n,s,o,i,r,l,h,d=80,f=3e3,p=1170,m=algoliasearch("QSQNJS2NQU","7d7dfcf22bf2af9070353d9f5a7c89c0"),c=m.initIndex("aws-production"),u=/10\./;function a(e){return!!u.test(e)}(function(e){e.fn.writeText=function(e){var s=e.split(""),n=0,t=this;t.val(""),r=setInterval(function(){n<=s.length&&(t.val(e.substring(0,n++)),t.change())},d)}})(jQuery),n=document.getElementById("howcanwehelptop"),autocomplete("#howcanwehelptop",{hint:!1,openOnFocus:!0},[{source:autocomplete.sources.hits(c,{hitsPerPage:5}),displayKey:"title",templates:{header:function(){return a(n.value)?doi="<div class='aa-footer aa-meta-link'>It looks like you are searching for a specific DOI, do you want to <a target='_blank' href='https://search.crossref.org/?from_ui=yes&q="+n.value+"'>try this as a Metadata Search?</a></div>":doi="",doi},suggestion:function(e){return sectionValue=e._highlightResult.section.value.replace(/-/g," "),titleValue=e._highlightResult.title.value,result="<a href='"+e.url+"'><div class='autosuggest-section'>"+sectionValue+"</div><div class='autosuggest-title'>"+titleValue+"</div></a>",result},empty:function(){return`<div class="aa-empty">We don't have anything on that topic. Please try editing your search or typing something new.</div>`},footer:function(){return"<div class='aa-footer'><span class='middle'>|</span><span class='left'><a href='/site-search/?query="+n.value+"'>More results</a></span><span class='right'><a target='_blank' href='https://search.crossref.org/?from_ui=yes&q="+n.value+"'>Search metadata</a></span></div>"}}}]).on("autocomplete:selected",function(e,t){location.href=t.url}),s=document.getElementById("howcanwehelp"),h=e("#howcanwehelp").attr("placeholder"),t=[],t.push("research integrity"),t.push("persistent identifiers"),t.push("metadata enrichment"),o=0,l=t.length,i=setInterval(function(){o==l?(o=0,e("#howcanwehelp").val(""),clearInterval(i)):e("#howcanwehelp").writeText(t[o++])},f),e("#howcanwehelp").click(function(){clearInterval(r),clearInterval(i),e("#howcanwehelp").val("")}),autocomplete("#howcanwehelp",{hint:!1,openOnFocus:!0},[{source:autocomplete.sources.hits(c,{hitsPerPage:5}),displayKey:"title",templates:{header:function(){return a(s.value)?doi="<div class='aa-footer aa-meta-link'>It looks like you are searching for a specific DOI, do you want to <a target='_blank' href='https://search.crossref.org/?from_ui=yes&q="+s.value+"'>try this as a Metadata Search?</a></div>":doi="",doi},suggestion:function(e){return sectionValue=e._highlightResult.section.value.replace(/-/g," "),titleValue=e._highlightResult.title.value,result="<a href='"+e.url+"'><div class='autosuggest-section'>"+sectionValue+"</div><div class='autosuggest-title'>"+titleValue+"</div></a>",result},empty:function(){return`<div class="aa-empty">We don't have anything on that topic. Please try editing your search or typing something new.</div>`},footer:function(){return"<div class='aa-footer'><span class='middle'>|</span><span class='left'><a href='/site-search/?query="+s.value+"'>More results</a></span><span class='right'><a target='_blank' href='https://search.crossref.org/?from_ui=yes&q="+s.value+"'>Search metadata</a></span></div>"}}}]).on("autocomplete:selected",function(e,t){location.href=t.url})})
var _paq=_paq||[];_paq.push(["trackPageView"]),_paq.push(["enableLinkTracking"]),function(){t="https://crossref.matomo.cloud/",_paq.push(["setTrackerUrl",t+"piwik.php"]),_paq.push(["setSiteId","1"]);var t,n=document,e=n.createElement("script"),s=n.getElementsByTagName("script")[0];e.type="text/javascript",e.async=!0,e.defer=!0,e.src="//cdn.matomo.cloud/crossref.matomo.cloud/piwik.js",s.parentNode.insertBefore(e,s)}()
window.onUsersnapLoad=function(e){e.init()};var script=document.createElement("script");script.defer=1,script.src="https://widget.usersnap.com/global/load/${OBJECT_ID}?onload=onUsersnapLoad",document.getElementsByTagName("head")[0].appendChild(script)
