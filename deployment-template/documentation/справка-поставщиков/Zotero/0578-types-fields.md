> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: types-fields

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Zotero Web API Item Type/Field Requests | Zotero Documentation
Zotero
Groups
Documentation
Forums
Get Involved
Log In
Sign Up
Upgrade Storage
Groups
Documentation
Forums
Get Involved
Log In
Upgrade Storage
Home
Getting Started
Installation
Quick Start Guide
System Requirements
Frequently Asked Questions
Version History
Adding to Your Library
Adding Items
Adding Files
Feeds
Retrieve PDF Metadata
Importing from Other Tools
Organizing & Taking Notes
Collections and Tags
Searching
Sorting
PDF Reader
Notes
Related Items
Duplicate Detection
Citations & Bibliographies
Creating Bibliographies
Word Processor Integration
Citation Styles
Reports
Syncing & Collaboration
Data and File Syncing
Groups
My Publications
Preferences
Preferences
Connector Preferences
Languages
Knowledge Base
Troubleshooting
Getting Help
Library Data Issues
Web Saving Issues
Word Processor Plugin Issues
Data Sync Issues
File Sync Issues
File Handling Issues
Developers
Zotero Web API Item Type/Field Requests
#
For a
Zotero Web API
client to present an editing UI to its users, it must know what combinations of Zotero item types, fields, and creator types are valid. Clients can request this data from the Zotero API.
As schema changes are currently rare, clients should cache type/field data for a period of time (e.g., one hour) without making further requests. Subsequent requests for new data should then include
If-Modified-Since
headers containing the contents of the
Last-Modified
header from the original response. If no changes have occurred, the server will return a
304 Not Modified
and clients should continue to use cached data for the same period of time.
[Conditional requests — i.e.
If-Modified-Since
— are not yet implemented.]
User-friendly type/field names will be returned in English by default. Clients can request names in other languages by passing a
locale
parameter (e.g.,
GET /itemTypes?locale=fr-FR
).
Note: the entire schema, including translations for all locales, can also be downloaded as a single file at
https://api.zotero.org/schema
. See the
GitHub repository of the schema
for caching instructions.
Getting All Item Types
#
GET /itemTypes
If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT
[
{
"itemType"
:
"book"
,
"localized"
:
"Book"
},
{
"itemType"
:
"note"
,
"localized"
:
"Note"
},
(
…
)
]
Common responses
## 200 OK
304 Not Modified
No changes have occurred since
If-Modified-Since
time.
400 Bad Request
Locale not supported.
Getting All Item Fields
#
GET /itemFields
If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT
[
{
"field"
:
"title"
,
"localized"
:
"Title"
},
{
"field"
:
"url"
,
"localized"
:
## "URL"
},
(
…
)
]
Common responses
## 200 OK
304 Not Modified
No changes have occurred since
If-Modified-Since
time.
400 Bad Request
Locale not supported.
Getting All Valid Fields for an Item Type
#
Note: API consumers intending to write to the server should generally use
/items/new
combined with
/itemTypes
instead of this request.
GET /itemTypeFields?itemType=book
If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT
[
{
"field"
:
"title"
,
"localized"
:
"Title"
},
{
"field"
:
"abstractNote"
,
"localized"
:
"Abstract"
},
(
…
)
]
Common responses
## 200 OK
304 Not Modified
No changes have occurred since
If-Modified-Since
time.
400 Bad Request
Locale not supported.
Getting Valid Creator Types for an Item Type
#
GET /itemTypeCreatorTypes?itemType=book
[
{
"creatorType"
:
"author"
,
"localized"
:
"Author"
},
{
"creatorType"
:
"editor"
,
"localized"
:
"Editor"
},
(
…
)
]
Common responses
## 200 OK
304 Not Modified
No changes have occurred since
If-Modified-Since
time.
400 Bad Request
'itemType' is unspecified or invalid; locale not supported.
Getting Localized Creator Fields
#
GET /creatorFields
If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT
[
{
"field"
:
"firstName"
,
"localized"
:
"First"
},
{
"field"
:
"lastName"
,
"localized"
:
"Last"
},
{
"field"
:
"name"
,
"localized"
:
"Name"
}
]
Common responses
304 Not Modified
No changes have occurred since
If-Modified-Since
time.
400 Bad Request
Locale not supported.
Getting a Template for a New Item
#
GET /items/new?itemType=book
If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT
{
"itemType"
:
"book"
,
"title"
:
""
,
"creators"
:
[
{
"creatorType"
:
"author"
,
"firstName"
:
""
,
"lastName"
:
""
}
],
"url"
:
""
,
(...),
"tags"
:
[],
"collections"
:
[],
"relations"
:
{}
}
GET /items/new?itemType=note
If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT
{
"itemType"
:
"note"
,
"note"
:
""
,
"tags"
:
[],
"collections"
:
[],
"relations"
:
{}
}
TODO: attachment creation (see
File Uploads
)
Common responses
## 200 OK
304 Not Modified
No changes have occurred since
If-Modified-Since
time.
400 Bad Request
itemType
is unspecified or invalid.
On this page
Zotero Web API Item Type/Field Requests
Getting All Item Types
Getting All Item Fields
Getting All Valid Fields for an Item Type
Getting Valid Creator Types for an Item Type
Getting Localized Creator Fields
Getting a Template for a New Item
Last updated 2019-12-07
Edit on GitHub
Documentation
Forums
Blog
Privacy
Terms of Service
Get Involved
Developers
Jobs
Follow us
Zotero is a project of
Digital Scholar
, a nonprofit organization dedicated to the development of software and services for researchers and cultural heritage institutions, and is developed by a
global community
.
