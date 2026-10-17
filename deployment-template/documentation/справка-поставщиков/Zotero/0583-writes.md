> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: writes

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Zotero Web API Write Requests | Zotero Documentation
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
Zotero Web API Write Requests
#
This page documents the write methods of the
Zotero Web API
. See the
Basics
page for basic information on accessing the API, including possible HTTP status codes not listed here.
An
API key
with write access to a given library is necessary to use write methods.
In Zotero 10+, the
local API
supports the same write methods against the local database. Writes there use a local API key granted by the user at runtime and check preconditions against local object versions; see
Local API
for the differences.
JSON Object Data
#
By default, objects returned from the API in
format=json
mode include a
data
property containing “editable JSON” — that is, all the object fields that can be modified and sent back to the server:
{
"key": "${OBJECT_KEY}",
"version": 1,
"library": { ... },
"links": { ... },
"meta": { ... },
"data": {
"key": "${OBJECT_KEY}",
"version": 1,
"itemType": "webpage",
"title": "Zotero Quick Start Guide",
"creators": [
{
"creatorType": "author",
"name": "Center for History and New Media"
}
],
"abstractNote": "",
"websiteTitle": "Zotero",
"websiteType": "",
"date": "",
"shortTitle": "",
"url": "https://www.zotero.org/support/quick_start_guide",
"accessDate": "2014-06-12T21:28:55Z",
"language": "",
"rights": "",
"extra": "",
"dateAdded": "2014-06-12T21:28:55Z",
"dateModified": "2014-06-12T21:28:55Z",
"tags": [],
"collections": [],
"relations": {}
}
}
There are two ways to make changes to the provided JSON:
Programmatic Approach
#
For programmatic access to the API, the recommended approach is to extract the editable JSON from the
data
property, make changes as necesssary, and upload just the editable JSON back to the API. For new items, an
empty template
of the editable JSON can be retrieved from the API.
This approach reduces upload bandwidth by sending only the data that is actually processed by the server. (For an even more efficient upload, the HTTP
## PATCH
method, discussed below, can be used to send only the fields that have changed.) The examples in this documentation assume programmatic access.
REST Approach
#
For more casual access, the API supports standard REST behavior, allowing the entire downloaded JSON to be reuploaded. This allows edits to be performed without writing a single line of code:
$ URL="https://api.zotero.org/users/${LIBRARY_ID}/items"
$ API_KEY="${API_KEY}"
$ curl -H "Zotero-API-Key: $API_KEY" $URL > items.json
$ vi items.json  # edit the item data
$ curl -H "Zotero-API-Key: $API_KEY" -d @items.json -v $URL
In this example, a JSON array of items is being saved to a text file, modified in a text editor, and then POSTed back to the same URL.
This approach allows a complicated task such as batch editing to be performed using only cURL and a text editor. Any objects modified in the text file will be updated on the server, while unmodified objects will be left unchanged.
A similar process can be used with PUT for individual objects:
$ URL="https://api.zotero.org/users/${LIBRARY_ID}/items/ABCD2345"
$ API_KEY="${API_KEY}"
$ curl -H "Zotero-API-Key: $API_KEY" $URL > item.json
$ vi items.json  # edit the item data
$ curl -H "Zotero-API-Key: $API_KEY" -X PUT -d @item.json -v $URL
Note that when uploading full JSON, only the
data
property is processed. All other properties (
library
,
links
,
meta
, etc.) are ignored.
Item Requests
#
Creating an Item
#
When creating a new item, first get empty JSON for the item type with an
item template request
(or use a cached version of the template). Then modify it and resubmit it to the server in an array:
POST <userOrGroupPrefix>/items
Content-Type: application/json
Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>
[
{
"itemType" : "book",
"title" : "My Book",
"creators" : [
{
"creatorType":"author",
"firstName" : "Sam",
"lastName" : "McAuthor"
},
{
"creatorType":"editor",
"name" : "John T. Singlefield"
}
],
"tags" : [
{ "tag" : "awesome" },
{ "tag" : "rad", "type" : 1 }
],
"collections" : [
## "BCDE3456", "CDEF4567"
],
"relations" : {
"owl:sameAs" : "http://zotero.org/groups/${GROUP_ID}/items/JKLM6543",
"dc:relation" : "http://zotero.org/groups/${GROUP_ID}/items/PQRS6789",
"dc:replaces" : "http://zotero.org/users/${LIBRARY_ID}/items/BCDE5432"
}
}
]
All properties other than
itemType
,
tags
,
collections
, and
relations
are optional.
Common responses
## 200 OK
The request completed. See the response JSON for status of individual writes.
400 Bad Request
Invalid type/field; unparseable JSON
409 Conflict
The target library is locked.
412 Precondition Failed
The version provided in
If-Unmodified-Since-Version
is out of date, or the provided
Zotero-Write-Token
has already been submitted.
413 Request Entity Too Large
Too many items submitted
## 200 OK
response:
{
"success": {
"0": "<itemKey>"
},
"unchanged": {},
"failed": {},
}
}
See
Creating Multiple Objects
for more information on the response format.
Creating Multiple Items
#
See
Creating Multiple Objects
.
Updating an Existing Item
#
To update an existing item, first retrieve the current version of the item:
GET <userOrGroupPrefix>/items/<itemKey>
The editable data, similar to the item data shown above in
Creating an Item
, will be found in the
data
property in the response.
The API supports two ways of modifying item data: by uploading full item data (
## PUT
) or by sending just the data that changed (
## PATCH
).
Full-item updating (PUT)
#
With
## PUT
, you submit the item’s complete editable JSON to the server, typically by modifying the downloaded editable JSON — that is, the contents of the
data
property — directly and resubmitting it:
PUT <userOrGroupPrefix>/items/<itemKey>
Content-Type: application/json
{
"key": "${OBJECT_KEY}",
"version": 1,
"itemType" : "book",
"title" : "My Amazing Book",
"creators" : [
{
"creatorType":"author",
"firstName" : "Sam",
"lastName" : "McAuthor"
},
{
"creatorType":"editor",
"name" : "Jenny L. Singlefield"
}
],
"tags" : [
{ "tag" : "awesome" },
{ "tag" : "rad", "type" : 1 }
],
"collections" : [
## "BCDE3456", "CDEF4567"
],
"relations" : {
"owl:sameAs" : "http://zotero.org/groups/${GROUP_ID}/items/JKLM6543",
"dc:relation" : "http://zotero.org/groups/${GROUP_ID}/items/PQRS6789",
"dc:replaces" : "http://zotero.org/users/${LIBRARY_ID}/items/BCDE5432"
}
}
All properties other than
itemType
,
tags
,
collections
, and
relations
are optional. Any existing fields not specified will be removed from the item. If
creators
,
tags
,
collections
, or
relations
are empty, any associated creators/tags/collections/relations will be removed from the item.
Partial-item updating (PATCH)
#
With
## PATCH
, you can submit just the properties that have actually changed, for a potentially much more efficient operation. Properties not included in the uploaded JSON are left untouched on the server. To clear a property, pass an empty string or an empty array as appropriate.
PATCH <userOrGroupPrefix>/items/<itemKey>
If-Unmodified-Since-Version: <last item version>
{
"date" : "2013"
"collections" : [
## "BCDE3456", "CDEF4567"
]
}
This would add a
date
field to the item and add it in the two specified collections if not already present. Array properties are interpreted as complete lists, so omitting a collection key would cause the item to be removed from that collection.
The
## PATCH
behavior is also available when
modifying multiple items
via
## POST
.
Both PUT and PATCH
#
Notes and attachments can be made child items by assigning the parent item’s key to the
parentItem
property. If parent and child items are created in the same
## POST
request, the child items must appear after the parent item in the array of items, with a locally created
item key
.
The item’s current version number is included in the
version
JSON property, as well as in the
Last-Modified-Version
header of single-item requests.
## PUT
and
## PATCH
requests must include the item’s current version number in either the
version
property or the
If-Unmodified-Since-Version
header. (
version
is included in responses from the API, so clients that simply modify the editable data do not need to bother with a version header.) If the item has been changed on the server since the item was retrieved, the write request will be rejected with a
412 Precondition Failed
error, and the most recent version of the item will have to be retrieved from the server before changes can be made. See
Version Numbers
for more on library and object versioning.
Common responses
204 No Content
The item was successfully updated.
400 Bad Request
Invalid type/field; unparseable JSON
409 Conflict
The target library is locked.
412 Precondition Failed
The item has changed since retrieval (i.e., the provided item version no longer matches).
Updating Multiple Items
#
See
Updating Multiple Objects
.
Deleting an Item
#
DELETE <userOrGroupPrefix>/items/<itemKey>
If-Unmodified-Since-Version: <last item version>
Common responses
204 No Content
The item was deleted.
409 Conflict
The target library is locked.
412 Precondition Failed
The item has changed since retrieval (i.e., the provided item version no longer matches).
428 Precondition Required
If-Unmodified-Since-Version
was not provided.
Deleting Multiple Items
#
Up to 50 items can be deleted in a single request.
DELETE <userOrGroupPrefix>/items?itemKey=<key>,<key>,<key>
If-Unmodified-Since-Version: <last library version>
204 No Content
Last-Modified-Version: <library version>
Common responses
204 No Content
The items were deleted.
409 Conflict
The target library is locked.
412 Precondition Failed
The library has changed since the specified version.
428 Precondition Required
If-Unmodified-Since-Version
was not provided.
Collection Requests
#
Creating a Collection
#
POST <userOrGroupPrefix>/collections
Content-Type: application/json
Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>
[
{
"name" : "My Collection",
"parentCollection" : "QRST9876"
}
]
Common responses
## 200 OK
The request completed without a general error. See the response JSON for status of individual writes.
409 Conflict
The target library is locked.
412 Precondition Failed
The version provided in
If-Unmodified-Since-Version
is out of date, or the provided
Zotero-Write-Token
has already been submitted.
Updating an Existing Collection
#
GET <userOrGroupPrefix>/collections/<collectionKey>
Editable JSON will be found in the
data
property.
PUT <userOrGroupPrefix>/collections/<collectionKey>
Content-Type: application/json
{
"key" : "${OBJECT_KEY}",
"version" : 156,
"name" : "My Collection",
"parentCollection" : false
}
Common responses
## 200 OK
The collection was updated.
409 Conflict
The target library is locked.
412 Precondition Failed
The collection has changed since retrieval (i.e., the provided collection version no longer matches).
Collection-Item Membership
#
Items can be added to or removed from collections via the
collections
property in the item JSON.
Deleting a Collection
#
DELETE <userOrGroupPrefix>/collections/<collectionKey>
If-Unmodified-Since-Version: <last collection version>
Common responses
204 No Content
The collection was deleted.
409 Conflict
The target library is locked.
412 Precondition Failed
The collection has changed since retrieval (i.e., the provided ETag no longer matches).
Deleting Multiple Collections
#
Up to 50 collections can be deleted in a single request.
DELETE <userOrGroupPrefix>/collections?collectionKey=<collectionKey>,<collectionKey>,<collectionKey>
If-Unmodified-Since-Version: <last library version>
204 No Content
Last-Modified-Version: <library version>
Common responses
204 No Content
The collections were deleted.
409 Conflict
The target library is locked.
412 Precondition Failed
The library has changed since the specified version.
Saved Search Requests
#
Creating a Search
#
POST <userOrGroupPrefix>/searches
Content-Type: application/json
Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>
[
{
"name": "My Search",
"conditions": [
{
"condition": "title",
"operator": "contains",
"value": "foo"
},
{
"condition": "date",
"operator": "isInTheLast",
"value": "7 days"
}
]
}
]
Common responses
## 200 OK
The request completed without a general error. See the response JSON for status of individual writes.
409 Conflict
The target library is locked.
412 Precondition Failed
The version provided in
If-Unmodified-Since-Version
is out of date, or the provided
Zotero-Write-Token
has already been submitted.
Deleting Multiple Searches
#
Up to 50 searches can be deleted in a single request.
DELETE <userOrGroupPrefix>/searches?searchKey=<searchKey>,<searchKey>,<searchKey>
If-Unmodified-Since-Version: <last library version>
204 No Content
Last-Modified-Version: <library version>
Common responses
204 No Content
The searches were deleted.
409 Conflict
The target library is locked.
412 Precondition Failed
The library has changed since the specified version.
Tag Requests
#
Deleting Multiple Tags
#
Up to 50 tags can be deleted in a single request.
DELETE <userOrGroupPrefix>/tags?tag=<URL-encoded tag 1> || <URL-encoded tag 2> || <URL-encoded tag 3>
If-Unmodified-Since-Version: <last library version>
204 No Content
Last-Modified-Version: <library version>
Multi-Object Requests
#
Creating Multiple Objects
#
Up to 50 collections, saved searches, or items can be created in a single request by including multiple objects in an array:
POST <userOrGroupPrefix>/collections
Content-Type: application/json
Zotero-Write-Token: <write token> or If-Unmodified-Since-Version: <last library version>
[
{
"name" : "My Collection",
"parentCollection": "QRST9876"
},
{
"name": "My Other Collection"
}
]
For
syncing
objects with predetermined keys, an
object key
can also be provided with new objects.
200
response:
Content-Type: application/json
Last-Modified-Version: <library version>
{
"successful": {
"0": "<saved object>",
"2": "<saved object>"
},
"unchanged": {
"4": "<objectKey>"
}
"failed": {
"1": {
"key": "<objectKey>",
"code": <HTTP response code>,
"message": "<error message>"
},
"3": {
"key": "<objectKey>",
"code": <HTTP response code>,
"message": "<error message>"
},
}
}
The keys of the
successful
,
unchanged
, and
failed
objects are the numeric indexes of the Zotero objects in the uploaded array. The
Last-Modified-Version
is the version that has been assigned to any Zotero objects in the
successful
object — that is, objects that were modified in this request.
Common responses
## 200 OK
The objects were uploaded.
409 Conflict
The target library is locked.
412 Precondition Failed
The version provided in
If-Unmodified-Since-Version
is out of date, or the provided
Zotero-Write-Token
has already been submitted.
Updating Multiple Objects
#
Up to 50 collections, saved searches, or items can be updated in a single request.
Follow the instructions in
Creating Multiple Objects
, but include a
key
and
version
property in each object. If modifying editable JSON returned from the API, these properties will already exist and shouldn’t be modified. As an alternative to individual
version
properties, the last-known library version can be passed via the
If-Unmodified-Since-Version
HTTP Header.
Items can also include
dateAdded
and
dateModified
properties containing timestamps in
ISO 8601 format
(e.g., “2014-06-10T13:52:43Z”). If
dateAdded
is included with an existing item, it must match the existing
dateAdded
value or else the API will return a 400 error. If a new
dateModified
time is not included with an update to existing item, the item’s
dateModified
value will be set to the current time. Editable JSON returned from the API includes
dateAdded
and
dateModified
in the correct format, so clients that are content with server-set modification times can simply ignore these properties.
POST <userOrGroupPrefix>/collections
Content-Type: application/json
[
{
"key": "${OBJECT_KEY}",
"version": 414,
"name": "My Collection",
"parentCollection": false
},
{
"key": "${OBJECT_KEY}",
"version": 416
"name": "My Subcollection",
"parentCollection": "BD85JEM4"
}
]
The response is the same as that in
Creating Multiple Objects
.
Note that
## POST
follows
## PATCH
semantics, meaning that any properties not specified will be left untouched on the server. To erase an existing property, include it with an empty string or
false
as the value.
Object Keys
#
While the server will automatically generate valid keys for uploaded objects, in some situations, such as when
syncing
or creating a parent and child item in the same request, it may be desirable or necessary to create object keys locally.
Local object keys should conform to the pattern
/[23456789ABCDEFGHIJKLMNPQRSTUVWXYZ]{8}/
.
Zotero-Write-Token
#
Zotero-Write-Token: 19a4f01ad623aa7214f82347e3711f56
Zotero-Write-Token
is an optional HTTP header, containing a client-generated random 32-character identifier string, that can be included with unversioned write requests to prevent them from being processed more than once (e.g., if a user clicks a form submit button twice). The Zotero server caches write tokens for successful requests for 12 hours, and subsequent requests from the same API key using the same write token will be rejected with a
412 Precondition Failed
status code. If a request fails, the write token will not be stored.
If using
versioned write requests
(i.e., those that include an
If-Unmodified-Since-Version
HTTP header or individual object
version
properties),
Zotero-Write-Token
is redundant and should be omitted.
In Zotero 10+, the
local API
also caches write tokens for 12 hours, but only in memory, so a token is forgotten if Zotero restarts.
Examples
#
See the
Syncing
page for an example workflow that puts together read and write methods for complete and efficient syncing of Zotero data via the API.
On this page
Zotero Web API Write Requests
JSON Object Data
Programmatic Approach
REST Approach
Item Requests
Creating an Item
Creating Multiple Items
Updating an Existing Item
Full-item updating (PUT)
Partial-item updating (PATCH)
Both PUT and PATCH
Updating Multiple Items
Deleting an Item
Deleting Multiple Items
Collection Requests
Creating a Collection
Updating an Existing Collection
Collection-Item Membership
Deleting a Collection
Deleting Multiple Collections
Saved Search Requests
Creating a Search
Deleting Multiple Searches
Tag Requests
Deleting Multiple Tags
Multi-Object Requests
Creating Multiple Objects
Updating Multiple Objects
Object Keys
Zotero-Write-Token
Examples
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
