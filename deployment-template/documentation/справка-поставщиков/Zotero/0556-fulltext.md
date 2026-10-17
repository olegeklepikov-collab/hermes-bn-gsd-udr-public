> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: fulltext

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Zotero Web API Full-Text Content Requests | Zotero Documentation
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
Zotero Web API Full-Text Content Requests
#
This page documents the methods to access full-text content of Zotero items via the
Zotero Web API
. See the
Basics
page for basic information on accessing the API, including possible HTTP status codes not listed here.
These methods are also available in the
local API
. In Zotero 10+, the versions returned are local versions rather than server versions.
Getting new full-text content
#
GET <userOrGroupPrefix>/fulltext?since=<version>
Content-Type: application/json
Last-Modified-Version: <library version>
{
"<itemKey>"
:
<
version
>
,
"<itemKey>"
:
<
version
>
,
"<itemKey>"
:
<
version
>
}
For each item with a full-text content version greater than stored locally, get the item’s full-text content, as described below.
Common responses
## 200 OK
Full-text content was successfully retrieved.
400 Bad Request
The 'since' parameter was not provided.
Getting an item’s full-text content
#
GET <userOrGroupPrefix>/items/<itemKey>/fulltext
<itemKey>
should correspond to an existing attachment item.
Content-Type: application/json
Last-Modified-Version: <version of item's full-text content>
{
"content"
:
"This is full-text content."
,
"indexedPages"
:
50
,
"totalPages"
:
50
}
indexedChars
and
totalChars
are used for text documents, while
indexedPages
and
totalPages
are used for PDFs.
Common responses
## 200 OK
Full-text content was found for the given item.
404 Not Found
The item wasn't found, or no full-text content was found for the given item.
Setting an item’s full-text content
#
PUT <userOrGroupPrefix>/items/<itemKey>/fulltext
Content-Type: application/json
{
"content"
:
"This is full-text content."
,
"indexedChars"
:
26
,
"totalChars"
:
26
}
<itemKey>
should correspond to an existing attachment item.
For text documents, include
indexedChars
and
totalChars
. For PDFs, include
indexedPages
and
totalPages
.
Common responses
204 No Content
The item's full-text content was updated.
400 Bad Request
Invalid JSON was provided.
404 Not Found
The item wasn't found or was not an attachment.
Searching for items by full-text content
#
See the
q
and
qmode
search parameters
.
On this page
Zotero Web API Full-Text Content Requests
Getting new full-text content
Getting an item’s full-text content
Setting an item’s full-text content
Searching for items by full-text content
Last updated 2026-07-29
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
