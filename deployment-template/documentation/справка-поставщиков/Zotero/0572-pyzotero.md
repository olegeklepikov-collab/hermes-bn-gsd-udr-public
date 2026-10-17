> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: pyzotero

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Getting started (short version) — Pyzotero 1.15.2 documentation
Pyzotero
Getting started (short version)
Installation, testing, usage (longer version)
Installation
Optional: Command-Line Interface
Optional: MCP Server
Installing development versions
Testing
Command-Line Interface Usage
Basic Commands
Item and Attachment Commands
Tag Commands
Write Commands
DOI Index
Search Behaviour
Output Format
MCP Server
Claude Desktop Configuration
Zotero Library Tools
Semantic Scholar Tools
Write Tools
How the write tools behave
Building Documentation
Reporting issues
General Usage
Zotero
Errors
Read API Methods
Search / Request Parameters for Read API calls
Zotero.add_parameters()
Zotero.key_info()
Retrieving Items
Zotero.items()
Zotero.settings()
Zotero.count_items()
Zotero.top()
Zotero.publications()
Zotero.trash()
Zotero.deleted()
Zotero.item()
Zotero.children()
Zotero.collection_items()
Zotero.collection_items_top()
Zotero.get_subset()
Retrieving Files
Zotero.file()
Zotero.dump()
Retrieving Collections
Zotero.collections()
Zotero.collections_top()
Zotero.collection()
Zotero.collections_sub()
Zotero.all_collections()
Retrieving groups
Zotero.groups()
Retrieving Tags
Zotero.tags()
Zotero.item_tags()
Retrieving Version Information
Zotero.item_versions()
Zotero.collection_versions()
Full–Text Content
Zotero.new_fulltext()
Zotero.fulltext_item()
Zotero.set_fulltext()
The
follow()
, and
everything()
methods
Zotero.follow()
Zotero.everything()
Related generator methods
Zotero.iterfollow()
Zotero.makeiter()
Retrieving item counts
Zotero.num_items()
Zotero.num_collectionitems()
Retrieving last modified version
Zotero.last_modified_version()
The Local Zotero API
How local write access works
Server IDs
Versions
Local API keys
How-to guides
How to make your first local write
How to keep write access across sessions
How to recover from a consumed or revoked key
How to add a file attachment
Reference
Zotero.server_id
Zotero.authorize_local()
Differences from the web API
Write API Methods
Saved Searches
Zotero.searches()
Zotero.saved_search()
Zotero.delete_saved_search()
Zotero.show_operators()
Zotero.show_conditions()
Zotero.show_condition_operators()
Item Methods
Zotero.item_types()
Zotero.item_fields()
Zotero.item_creator_types()
Zotero.creator_fields()
Zotero.item_type_fields()
Zotero.item_template()
Creating and Updating Items
Zotero.create_items()
Zotero.update_item()
Zotero.update_items()
Zotero.check_items()
Uploading files
Zotero.attachment_simple()
Zotero.attachment_both()
Zotero.upload_attachments()
Deleting items
Zotero.delete_item()
Deleting tags
Zotero.delete_tags()
Adding tags
Zotero.add_tags()
Collection Methods
Zotero.create_collections()
Zotero.create_collection()
Zotero.addto_collection()
Zotero.deletefrom_collection()
Zotero.moveto_collection()
Zotero.update_collection()
Zotero.update_collections()
Zotero.collection_tags()
Zotero.delete_collection()
Notes
License
Cat Picture
Pyzotero
Getting started (short version)
Edit on GitHub
Pyzotero is a Python wrapper for the
Zotero API (v3)
.
Getting started (short version)

uv
add
pyzotero
or
pip
install
pyzotero
or
conda
install
conda-forge::pyzotero
You’ll need the ID of the personal or group library you want to access:
Your
personal library ID
is available
here
, in the section
Your
userID
for
use
in
## API
calls
For
group libraries
, the ID can be found by opening the group’s page:
https://www.zotero.org/groups/groupname
, and hovering over the
group
settings
link. The ID is the integer after
/groups/
You’ll also need
[
*
]
to get an
API key
from the Zotero
site
Are you accessing your own Zotero library? Set``library_type`` to
'user'
Are you accessing a shared group library? Set``library_type`` to
'group'
Access to your local Zotero library is available: set
local=True
. Reads need no authentication; writes require a local API key and a recent Zotero version — see
The Local Zotero API
from
pyzotero
import
Zotero
zot
=
Zotero
(
library_id
,
library_type
,
api_key
)
items
=
zot
.
top
(
limit
=
5
)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for
item
in
items
:
print
(
f
"Item:
{
item
[
'data'
][
'itemType'
]
}
| Key:
{
item
[
'data'
][
'key'
]
}
"
)
Refer to the
Errors
and
Write API Methods
.
Installation, testing, usage (longer version)

Installation

Using
uv
:
uv
add
pyzotero
Using
pip
:
pip
install
pyzotero
Using
Anaconda
:
conda
install
conda-forge::pyzotero
Optional: Command-Line Interface

Pyzotero includes an optional command-line interface for searching and querying your local Zotero library, and for managing its collections.
To install Pyzotero with the CLI:
Using
uv
:
uv
add
"pyzotero[cli]"
Using
pip
:
pip
install
"pyzotero[cli]"
If you just want to use the CLI without permanently installing Pyzotero:
Using
uvx
:
uvx
--from
"pyzotero[cli]"
pyzotero
search
-q
"your
query"
Using
pipx
:
pipx
run
--spec
"pyzotero[cli]"
pyzotero
search
-q
"your
query"
See
Command-Line Interface Usage
for usage details.
Optional: MCP Server

Pyzotero includes an optional
## MCP
server that exposes your local Zotero library and the Semantic Scholar integration.
To install Pyzotero with the MCP server:
Using
uv
:
uv
add
"pyzotero[mcp]"
Using
pip
:
pip
install
"pyzotero[mcp]"
As a standalone tool:
uv
tool
install
"pyzotero[mcp]"
CLI and MCP server together:
uv
tool
install
"pyzotero[cli,mcp]"
See
MCP Server
for configuration and the list of tools.
From a local clone, if you wish to install Pyzotero from a specific branch:
git
clone
git://github.com/urschrei/pyzotero.git
cd
pyzotero
git
checkout
main
uv
sync
The Pyzotero source tarball is also available from
PyPI
Installing development versions

Pyzotero remains in development as of 2025. Unstable development versions can be found on the
Github main branch
, and installed directly from a checked-out
main
branch on a local clone, as in the example above: specify
--dev
(uv) /
--group
dev
(pip).
Testing

Testing requires installation of the
dev
dependency group (see above).
Run
pytest
.
from the top-level directory.
Command-Line Interface Usage

The Pyzotero CLI connects to your local Zotero installation and allows you to search your library, list collections, view item types, and manage collection membership.
Basic Commands

Search for top-level items:
pyzotero
search
-q
"machine learning"
Search with full-text mode:
pyzotero
search
-q
"climate change"
--fulltext
Filter by item type:
pyzotero
search
-q
"methodology"
--itemtype
book
--itemtype
journalArticle
Search for top-level items within a collection:
pyzotero
search
--collection
## ABC123
-q
"test"
Output as JSON for machine processing:
pyzotero
search
-q
"climate"
--json
Filter by tags (multiple tags use AND logic):
pyzotero
search
-q
"topic"
--tag
"climate"
--tag
"adaptation"
Paginate results:
pyzotero
search
-q
"topic"
--limit
20
--offset
20
--json
List all collections:
pyzotero
listcollections
List available item types:
pyzotero
itemtypes
List the fields and creator types that one item type accepts:
pyzotero
listitemfields
journalArticle
Item and Attachment Commands

Get a single item by key:
pyzotero
item
## ABC123
--json
Get child items (attachments, notes) of an item:
pyzotero
children
## ABC123
--json
Get multiple items by key in a single call (up to 50):
pyzotero
subset
## ABC123
## DEF456
## GHI789
--json
Get full-text content of an attachment:
pyzotero
fulltext
## ABC123
Tag Commands

List all tags in the library:
pyzotero
tags
List tags from a specific collection:
pyzotero
tags
--collection
## ABC123
Write Commands

These commands write to your library, so they need a local API key. Run
pyzotero
authorize
once and choose “Always Allow” in Zotero’s dialog. The key is stored in
$XDG_CONFIG_HOME/pyzotero/local-api-key.json
(
~/.config/pyzotero/local-api-key.json
if that variable is unset). Setting
## PYZOTERO_LOCAL_API_KEY
in the environment takes precedence over the file.
Obtain and store a key:
pyzotero
authorize
--app-name
"My tool"
Create items from a JSON file, or from standard input:
pyzotero
createitem
item.json
cat
items.json
|
pyzotero
createitem
-
pyzotero
createitem
items.json
--collection
## FD9AUNP2
--tag
"to read"
--json
The file contains one item object, or a list of them, in Zotero’s item-data format:
[
{
"itemType"
:
"book"
,
"title"
:
"Frankenstein"
,
"creators"
:
[{
"creatorType"
:
"author"
,
"lastName"
:
"Shelley"
,
"firstName"
:
"Mary"
}],
"date"
:
"1818"
}
]
--collection
files every created item under one collection, and
--tag
, which you can repeat, tags every created item. Collections and tags that an item already has are kept. The item type and the field names of every item are checked against the library’s schema before anything is sent.
pyzotero
itemtypes
lists the item types, and
pyzotero
listitemfields
## TYPE
lists the fields of one type. Zotero accepts up to 50 items in one call.
Create a collection, at the top level or nested under
--parent
:
pyzotero
createcollection
"Frankenstein Cities"
--parent
## FD9AUNP2
Add items to a collection:
pyzotero
addtocollection
## FD9AUNP2
## ABC123
## DEF456
Remove items from a collection (the items themselves are unchanged):
pyzotero
removefromcollection
## FD9AUNP2
## ABC123
Move items from one collection to another:
pyzotero
movetocollection
--from
## FD9AUNP2
--to
## X7Y8Z9W0
## ABC123
## DEF456
Each command accepts
--json
and reports the keys it touched. The membership commands change items one at a time.
movetocollection
changes each item in one request: its membership of other collections is kept. If Zotero rejects an item that
createitem
sends, the error gives its reason and names the items that were created.
DOI Index

Output the complete DOI-to-key mapping for caching:
pyzotero
doiindex
>
doi_cache.json
This returns a JSON mapping of normalised DOIs to item keys and original DOIs, allowing external tools to cache the index and avoid repeated full-library scans.
Search Behaviour

By default,
pyzotero
search
searches only top-level item titles and metadata fields.
When the
--fulltext
flag is used, the search expands to include all full-text indexed content, including PDFs and other attachments. Since most full-text content comes from PDF attachments rather than top-level items, the CLI automatically retrieves the parent bibliographic items for any matching attachments. This ensures you receive useful bibliographic records (journal articles, books, etc.) rather than raw attachment items.
Output Format

By default, the CLI outputs human-readable text with all relevant metadata including:
Title, authors, date, publication
Volume, issue, DOI, URL
PDF attachments (with local file paths)
Use the
--json
flag to output structured JSON suitable for consumption by other tools and agents.
MCP Server

The
pyzotero-mcp
command starts an
## MCP
server over standard input and output. It exposes your local Zotero library, and the Semantic Scholar integration. This lets sandboxed applications use your library without access to the CLI. See
Installation
for how to install it.
The server is read-only unless it is started with
--enable-writes
.
Claude Desktop Configuration

Add one of the following to your Claude Desktop configuration file.
If
pyzotero-mcp
is installed:
{
"mcpServers"
:
{
"zotero"
:
{
"command"
:
"pyzotero-mcp"
}
}
}
Or, without installing, using
uvx
:
{
"mcpServers"
:
{
"zotero"
:
{
"command"
:
"uvx"
,
"args"
:
[
"--from"
,
"pyzotero[mcp]"
,
"pyzotero-mcp"
]
}
}
}
Zotero Library Tools

Tool
Description
search
Search the local Zotero library by query, item type, collection, tag, or full-text content
get_item
Get a single Zotero item by its key
get_children
Get the child items (attachments, notes) of a Zotero item
list_collections
List all collections in the library
list_tags
List all tags, optionally filtered by collection
get_fulltext
Get the full-text content of a PDF or other attachment
Semantic Scholar Tools

Tool
Description
find_related
Find semantically similar papers using SPECTER2 embeddings
get_citations
Find papers that cite a given paper
get_references
Find papers referenced by a given paper
search_semantic_scholar
Search across Semantic Scholar’s paper index
Each Semantic Scholar tool accepts a
check_library
parameter,
True
by default, which annotates each result with whether the paper is already in your local Zotero library.
Write Tools

The write tools are opt-in. To enable them:
Obtain a persistent local API key, choosing “Always Allow” in Zotero’s dialog:
pyzotero
authorize
--app-name
"Claude Desktop"
The key and the Zotero server ID are stored in
$XDG_CONFIG_HOME/pyzotero/local-api-key.json
(
~/.config/pyzotero/local-api-key.json
if that variable is unset), readable only by you. The server reads the key from that file.
Add the
--enable-writes
flag to the server’s arguments:
{
"mcpServers"
:
{
"zotero"
:
{
"command"
:
"pyzotero-mcp"
,
"args"
:
[
"--enable-writes"
]
}
}
}
Optional: to supply the key some other way, set
## PYZOTERO_LOCAL_API_KEY
in the server’s
env
block, and
## PYZOTERO_LOCAL_SERVER_ID
beside it to save one request at startup. The environment takes precedence over the key file.
pyzotero
authorize
--no-store
prints a key without writing the file.
With
--enable-writes
, the server registers these tools:
Tool
Description
list_item_fields
List the fields and creator types valid for an item type
create_item
Create a new item
update_item
Update fields on an existing item
add_tags
Add tags to an existing item
create_collection
Create a collection, optionally nested
add_to_collection
File an existing item under a collection
remove_from_collection
Remove an item from a collection; the item itself is unchanged
move_to_collection
Move an item from one collection to another in one step
add_attachment
Attach a file on disk to an existing item
delete_item
Permanently delete an item. Requires
--enable-deletes
How the write tools behave

Without
--enable-writes
, the write tools are not merely disabled: they are never registered, so they do not appear in the model’s tool list at all, and content in your library cannot induce a call to one.
add_attachment
requires an
absolute
path. The server runs as a subprocess of your MCP client, so its working directory is not yours, and a relative path would resolve somewhere unintended; relative paths are rejected. The file is copied into Zotero’s storage, and syncs with the library if sync is enabled. Attaching a file that is already attached to the item is reported as unchanged rather than duplicated.
delete_item
is behind a second flag because deletion via the local API is irreversible: items are erased outright rather than moved to the trash, and the deletion propagates on sync.
--enable-deletes
implies
--enable-writes
.
Building Documentation

If you wish to build Pyzotero’s documentation for offline use, it can be built from the
doc
directory of a local git repo by running
make
followed by the desired output format(s) (
html
,
epub
,
latexpdf
etc.)
This functionality requires Sphinx.
See the
Sphinx documentation
for full details.
Reporting issues

If you encounter an error while using Pyzotero, please open an issue on its
Github issues page
.
General Usage

Important
## A
Zotero
instance is bound to the library or group used to create it. Thus, if you create a
Zotero
instance with a
library_id
of
67
and a
library_type
of
group
, its item methods will only operate upon that group. Similarly, if you create a
Zotero
instance with your own
library_id
and a
library_type
of
user
, the instance will be bound to your Zotero library.
First, create a new Zotero instance:
class
zotero.
Zotero
(
library_id
,
library_type
[
,
api_key
,
preserve_json_order
,
locale
,
local
,
client
,
upload_timeout
,
server_id
,
local_api_key
]
)

Parameters
:
library_id
(
str
) – a valid Zotero API user ID
library_type
(
str
) – a valid Zotero API library type:
user
or
group
api_key
(
str
) – a valid Zotero API user key
preserve_json_order
(
bool
) – Load JSON returns with OrderedDict to preserve their order
locale
(
str
) – Set the
locale
, allowing retrieval of localised item types, field types, and creator types. Defaults to “en-US”.
local
(
str
) – use the local Zotero http server instead of the remote API. See
The Local Zotero API
client
(
httpx2.Client
) – the HTTP client for API requests. If it is
None
(the default), Pyzotero creates a client with its default timeout. In local mode, that client ignores proxy settings from the environment. Pyzotero sends its default headers with each request:
Authorization
(if you supply
api_key
),
Zotero-API-Version
and
User-Agent
. They replace headers of the same name on the client. Pyzotero does not change a client that you supply, and the client keeps its own proxy settings. To use the local API when your environment sets a proxy, create the client with
trust_env=False
upload_timeout
(
int/float
) – timeout in seconds for file uploads to storage (default: 120). Increase this for very large files or slow connections.
server_id
(
str
) – a local API server ID retained from a previous session. Only meaningful when
local
is
True
; see
The Local Zotero API
local_api_key
(
str
) – a persistent local API key retained from a previous session, obtained from
Zotero.authorize_local()
. Only meaningful when
local
is
True
Example:
from
pyzotero
import
Zotero
zot
=
Zotero
(
'123'
,
'user'
,
## 'ABC1234XYZ'
)
# we now have a Zotero object, zot, and access to all its methods
first_ten
=
zot
.
items
(
limit
=
10
)
# a list containing dicts of the ten most recently modified library items
Errors

Where possible, any
ZoteroError
which is raised will preserve the underlying error in its
__cause__
and
__context__
properties, should you wish to work with these directly.
The local API reuses several status codes for more than one condition, so Pyzotero
inspects the response body and raises a more specific exception. Each subclasses the
exception the status code alone would have produced, so existing handlers are unaffected:
LocalAPIKeyRequiredError
(401, subclasses
UserNotAuthorisedError
): no valid local API key. Call
Zotero.authorize_local()
.
LocalAPIDeniedError
(403, subclasses
UserNotAuthorisedError
): the user denied an authorisation request.
ServerIDMismatchError
(412, subclasses
PreConditionFailedError
): the request reached a different Zotero instance or database.
ServerIDRequiredError
(428, subclasses
PreConditionRequiredError
): a local write carried no
Zotero-Server-ID
header.
Read API Methods

Note
All search/request parameters inside square brackets are
optional
. Methods such as
Zotero.top()
,
Zotero.items()
etc. can be called with no additional parameters if you wish.
Tip
The Read API returns 25 results by default (the API documentation claims 50). In the interests of usability, Pyzotero returns 100 items by default, by setting the API
limit
parameter to 100, unless it’s set by the user. If you wish to retrieve e.g. all top-level items without specifying a
limit
parameter, you’ll have to wrap your call with
Zotero.everything()
:
results
=
zot.everything(zot.top())
.
Search / Request Parameters for Read API calls

Additional parameters may be set on Read API methods
following any required parameters
, or set using the
Zotero.add_parameters()
method detailed below.
The following two examples produce the same result:
# set parameters on the call itself
z
=
zot
.
top
(
limit
=
7
,
start
=
3
)
# set parameters using explicit method
zot
.
add_parameters
(
limit
=
7
,
start
=
3
)
z
=
zot
.
top
()
The following parameters are
optional
.
You may also set a search term here, using the ‘itemType’, ‘q’, ‘qmode’, or ‘tag’ parameters
.
This area of the Zotero Read API is under development, and may change frequently. See
the API documentation
for the most up-to-date details of search syntax usage and export format details.
Zotero.
add_parameters
(
[
format
=
None
,
itemKey
=
None
,
itemType
=
None
,
q
=
None
,
qmode
=
None
,
since
=
None
,
tag
=
None
,
sort
=
None
,
direction
=
None
,
limit
=
None
,
start
=
None
[
,
content
=
None
[
,
style
=
None
]
]
]
)

Parameters
:
format
(
str
) – “atom”, “bib”, “bibtex”, json”, “keys”, “versions”. Pyzotero retrieves and decodes JSON responses by default
Attention
Setting
format='bib'
will remove the
limit
parameter if it’s been set, as
the API does not allow a limit on bibliography output
; it instead enforces a limit of 150 items, and if the set of items you are trying to generate a bibliography for exceeds 150, an error will be raised.
Parameters
:
itemKey
(
str
) – A comma-separated list of item keys. Valid only for item requests. Up to 50 items can be specified in a single request
Search parameters:
Parameters
:
itemType
(
str
) – item type search. See the
Search Syntax
for details
q
(
str
) – Quick search. Searches titles and individual creator fields by default. Use the
qmode
parameter to change the mode. Currently supports phrase searching only
qmode
(
str
) – Quick search mode. To include full-text content in the search, use
everything
. Defaults to
titleCreatorYear
. Searching of other fields will be possible in the future
since
(
int
) – default
0
. Return only objects modified after the specified library version
tag
(
str
) –
tag search. See the
Search Syntax
for details. More than one tag may be passed by passing a list of strings – These are treated as
## AND
search terms, meaning only items which include all of the specified tags are returned. You can search for items matching any tag in a list by using
## OR
:
"tag1
## OR
tag2"
, and all items which exclude a tag:
"-tag"
.
The following parameters can be used for search requests:
Parameters
:
sort
(
str
) – The name of the field by which entries are sorted: (
dateAdded
,
dateModified
,
title
,
creator
,
type
,
date
,
publisher
,
publicationTitle
,
journalAbbreviation
,
language
,
accessDate
,
libraryCatalog
,
callNumber
,
rights
,
addedBy
,
numItems
,
tags
)
direction
(
str
) –
asc
or
desc
limit
(
int
) – 1 – 100 or None
start
(
int
) – 1 – total number of items in your library or None
If you wish to retrieve citation or bibliography entries, use the following parameters:
Parameters
:
content
(
str
) – ‘bib’, ‘html’, or one of the export formats (see below). If ‘bib’ is passed, you may
also
pass:
style
(
str
) – Any valid CSL style in the Zotero style repository
linkwrap
(
str
) – Set this to “1” to have URLs in bibliography entries (see below) wrapped in
<a>
tags.
Return type
:
list of HTML strings or None.
Note
Any parameters you set will be valid
for the next call only
. Any parameters set using
add_parameters()
will be overridden by parameters you pass in the call itself.
A note on the
content
and
style
parameters:
Example:
zot
.
add_parameters
(
content
=
'bib'
,
style
=
'mla'
)
If these are set, the return value is a list of UTF-8 formatted HTML
div
elements, each containing an item:
['<div
class="csl-entry">(content)</div>']
.
You may also set
content='citation'
if you wish to retrieve citations. Similar to
bib
, the result will be a list of one or more HTML
span
elements.
If you select one of the available
export formats
as the
content
parameter, pyzotero will in most cases return a list of unicode strings in the format you specified. The exception is the
csljson
format, which is parsed into a list of dicts. Please note that you must provide a
limit
parameter if you specify one of these export formats. Multiple simultaneous retrieval of particular formats, e.g.
content="json,coins"
is not currently supported.
If you set
format='keys'
, a newline-delimited string containing item keys will be returned
If you set
format='bibtex'
, a
bibtexparser
object containing citations will be returned. You can access the citations as a list of dicts using the
.entries
property. The bibtexparser object also implements a
dump method
, if you’d like to write your citations to a
.bib
file.
Zotero.
key_info
(
)

Returns info about the user and group library permissions associated with the current
Zotero
instance, based on the API key. Together with
Zotero.groups()
, this allows all accessible resources to be determined.
Return type
:
dict
Retrieving Items

Tip
In contrast to the v1 API, a great deal of additional metadata is now returned. In most cases, simply accessing items by referring to their
item['data']
key will suffice.
The following methods will retrieve either user or group items, depending on the value (
user
or
group
) used to create the
Zotero
instance:
Zotero.
items
(
[
search/request
parameters
]
)

Returns Zotero library items
Return type
:
list of dicts
Zotero.
settings
(
[
since
]
)

Returns synced Zotero user library settings such as feeds and PDF reading progress. Use the optional
since
parameter to specify the retrieval of changes since a known previous library version.
Return type
:
list of dicts
Zotero.
count_items
(
)

Returns a count of all items in a library / group
Return type
:
int
Zotero.
top
(
[
search/request
parameters
]
)

Returns top-level Zotero library items
Return type
:
list of dicts
Zotero.
publications
(
[
search/request
parameters
]
)

Returns the publications from the “My Publications” collection of a user’s library. Only available on
user
libraries.
Return type
:
list of dicts
Zotero.
trash
(
[
search/request
parameters
]
)

Returns library items from the library’s trash
Return type
:
list of dicts
Zotero.
deleted
(
[
search/request
parameters
]
)

Returns deleted collections, library items, tags, searches and settings (requires “since=” parameter)
Return type
:
list of dicts
Zotero.
item
(
itemID
[
,
search/request
parameters
]
)

Returns a specific item
Parameters
:
itemID
(
str
) – a zotero item ID
Return type
:
list of dicts
Zotero.
children
(
itemID
[
,
search/request
parameters
]
)

Returns the child items of a specific item
Parameters
:
itemID
(
str
) – a zotero item ID
Return type
:
list of dicts
Zotero.
collection_items
(
collectionID
[
,
search/request
parameters
]
)

Returns items from the specified collection. This does not include items in sub-collections
Parameters
:
collectionID
(
str
) – a Zotero collection ID
Return type
:
list of dicts
Zotero.
collection_items_top
(
collectionID
[
,
search/request
parameters
]
)

Returns top-level items from the specified collection.
Parameters
:
collectionID
(
str
) – a Zotero collection ID
Return type
:
list of dicts
Zotero.
get_subset
(
itemIDs
[
,
search/request
parameters
]
)

Retrieve an arbitrary set of non-adjacent items. Limited to 50 items per call.
Parameters
:
itemIDs
(
list
) – a list of Zotero Item IDs
Return type
:
list of dicts
Example of returned item data:
[{
u
'data'
:
{
u
## 'ISBN'
:
u
'0810116820'
,
u
'abstractNote'
:
u
''
,
u
'accessDate'
:
u
''
,
u
'archive'
:
u
''
,
u
'archiveLocation'
:
u
''
,
u
'callNumber'
:
u
'HIB 828.912 BEC:3g N9'
,
u
'collections'
:
[
u
## '2UNGXMU9'
],
u
'creators'
:
[{
u
'creatorType'
:
u
'author'
,
u
'firstName'
:
u
'Daniel'
,
u
'lastName'
:
u
'Katz'
}],
u
'date'
:
u
'1999'
,
u
'dateAdded'
:
u
## '2010-01-04T14:50:40Z'
,
u
'dateModified'
:
u
## '2014-08-06T11:28:41Z'
,
u
'edition'
:
u
''
,
u
'extra'
:
u
''
,
u
'itemType'
:
u
'book'
,
u
'key'
:
u
## 'VDNIEAPH'
,
u
'language'
:
u
''
,
u
'libraryCatalog'
:
u
'library.catalogue.tcd.ie Library Catalog'
,
u
'numPages'
:
u
''
,
u
'numberOfVolumes'
:
u
''
,
u
'place'
:
u
'Evanston, Ill'
,
u
'publisher'
:
u
'Northwestern University Press'
,
u
'relations'
:
{
u
'dc:replaces'
:
u
'http://zotero.org/users/${LIBRARY_ID}/items/9TXN8QUD'
},
u
'rights'
:
u
''
,
u
'series'
:
u
''
,
u
'seriesNumber'
:
u
''
,
u
'shortTitle'
:
u
'Saying I No More'
,
u
'tags'
:
[{
u
'tag'
:
u
'Beckett, Samuel'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Consciousness in literature'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'English prose literature'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Ireland'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Irish authors'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Modernism (Literature)'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Prose'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Self in literature'
,
u
'type'
:
1
},
{
u
'tag'
:
u
'Subjectivity in literature'
,
u
'type'
:
1
}],
u
'title'
:
u
'Saying I No More: Subjectivity and Consciousness in The Prose of Samuel Beckett'
,
u
'url'
:
u
''
,
u
'version'
:
792
,
u
'volume'
:
u
''
},
u
'key'
:
u
## 'VDNIEAPH'
,
u
'library'
:
{
u
'id'
:
436
,
u
'links'
:
{
u
'alternate'
:
{
u
'href'
:
u
'https://www.zotero.org/urschrei'
,
u
'type'
:
u
'text/html'
}},
u
'name'
:
u
'urschrei'
,
u
'type'
:
u
'user'
},
u
'links'
:
{
u
'alternate'
:
{
u
'href'
:
u
'https://www.zotero.org/urschrei/items/VDNIEAPH'
,
u
'type'
:
u
'text/html'
},
u
'self'
:
{
u
'href'
:
u
'https://api.zotero.org/users/${LIBRARY_ID}/items/VDNIEAPH'
,
u
'type'
:
u
'application/json'
}},
u
'meta'
:
{
u
'creatorSummary'
:
u
'Katz'
,
u
'numChildren'
:
0
,
u
'parsedDate'
:
u
'1999-00-00'
},
u
'version'
:
792
}]
See
‘Hello World’
example, above
Retrieving Files

Zotero.
file
(
itemID
[
,
search/request
parameters
]
)

Returns the raw file content of an item. This can be dumped like so:
with
open
(
'article.pdf'
,
'wb'
)
as
f
:
f
.
write
(
zot
.
file
(
## 'BM8MZJBB'
))
Parameters
:
itemID
(
str
) – a zotero item ID
Return type
:
binary string
Zotero.
dump
(
itemID
[
,
filename
,
path
]
)

A convenient wrapper around
Zotero.file()
. Writes an attachment to disk using the optional path and filename.
If neither are supplied, the file is written to the current working
directory, and a
Zotero.item()
call is first made to determine the attachment
filename. No error checking is done regarding the path. If successful, the full path including the file name is returned.
Note
HTML snapshots will be dumped as zip files. These will be named with their API item key, and a .zip extension.
# write a file to the current working directory using the stored filename
zot
.
dump
(
## 'BM8MZJBB'
)
# write the same file to a different path, with a new name
zot
.
dump
(
## 'BM8MZJBB'
,
'article_1.pdf'
,
'${USER_HOME}/pdfs'
)
Parameters
:
itemID
(
str
) – a zotero item ID
filename
(
str
) – (optional) an alternate filename
path
(
str
) – (optional) a valid path for the file
Return type
:
String
File retrieval and dumping should work for most common document, audio and video file formats. If you encounter an error,
please open an issue
.
Retrieving Collections

Zotero.
collections
(
[
search/request
parameters
]
)

Returns a library’s collections.
This includes subcollections
.
Return type
:
list of dicts
Zotero.
collections_top
(
[
search/request
parameters
]
)

Returns a library’s top-level collections.
Return type
:
list of dicts
Zotero.
collection
(
collectionID
[
,
search/request
parameters
]
)

Returns a specific collection
Parameters
:
collectionID
(
str
) – a Zotero library collection ID
Return type
:
dict
Zotero.
collections_sub
(
collectionID
[
,
search/request
parameters
]
)

Returns the sub-collections of a specific collection
Parameters
:
collectionID
(
str
) – a Zotero library collection ID
Return type
:
list of dicts
Zotero.
all_collections
(
[
collectionID
]
)

Returns either all collections and sub-collections in a flat list, or, if a collection ID is specified, that collection and all of its sub-collections. This method can be called at any collection “depth”.
Parameters
:
collectionID
(
str
) – a Zotero library collection ID (optional)
Return type
:
list of dicts
Example of returned collection data:
[{
u
'data'
:
{
u
'key'
:
u
## '5TSDXJG6'
,
u
'name'
:
u
'Critical GIS'
,
u
'parentCollection'
:
False
,
u
'relations'
:
{},
u
'version'
:
778
},
u
'key'
:
u
## '5TSDXJG6'
,
u
'library'
:
{
u
'id'
:
436
,
u
'links'
:
{
u
'alternate'
:
{
u
'href'
:
u
'https://www.zotero.org/urschrei'
,
u
'type'
:
u
'text/html'
}},
u
'name'
:
u
'urschrei'
,
u
'type'
:
u
'user'
},
u
'links'
:
{
u
'alternate'
:
{
u
'href'
:
u
'https://www.zotero.org/urschrei/collections/5TSDXJG6'
,
u
'type'
:
u
'text/html'
},
u
'self'
:
{
u
'href'
:
u
'https://api.zotero.org/users/${LIBRARY_ID}/collections/5TSDXJG6'
,
u
'type'
:
u
'application/json'
}},
u
'meta'
:
{
u
'numCollections'
:
0
,
u
'numItems'
:
1
},
u
'version'
:
778
}]
Retrieving groups

Zotero.
groups
(
[
search/request
parameters
]
)

Retrieve the Zotero group data to which the current library_id and api_key has access
Return type
:
list of dicts
Example of returned group data:
[{
u
'data'
:
{
u
'description'
:
u
''
,
u
'fileEditing'
:
u
'admins'
,
u
'hasImage'
:
1
,
u
'id'
:
169947
,
u
'libraryEditing'
:
u
'admins'
,
u
'libraryReading'
:
u
'members'
,
u
'members'
:
[
1177919
,
1408658
],
u
'name'
:
u
'smart_cities'
,
u
'owner'
:
436
,
u
'type'
:
u
'Private'
,
u
'url'
:
u
''
,
u
'version'
:
0
},
u
'id'
:
169947
,
u
'links'
:
{
u
'alternate'
:
{
u
'href'
:
u
'https://www.zotero.org/groups/${GROUP_ID}'
,
u
'type'
:
u
'text/html'
},
u
'self'
:
{
u
'href'
:
u
'https://api.zotero.org/groups/${GROUP_ID}'
,
u
'type'
:
u
'application/json'
}},
u
'meta'
:
{
u
'created'
:
u
## '2013-05-22T11:22:46Z'
,
u
'lastModified'
:
u
## '2013-05-22T11:26:50Z'
,
u
'numItems'
:
817
},
u
'version'
:
0
}]
Retrieving Tags

Zotero.
tags
(
[
search/request
parameters
]
)

Returns a library’s tags
Return type
:
list of strings
Zotero.
item_tags
(
itemID
[
,
search/request
parameters
]
)

Returns tags from a specific item
Parameters
:
itemID
(
str
) – a valid Zotero library Item ID
Return type
:
list of strings
Example of returned tag data:
[
'Authority in literature'
,
'Errata'
]
Retrieving Version Information

The
Zotero API
recommends requesting version information for all (or all changed) items and collections when implementing syncing.  The following convenience methods (which by default return an unlimited number of responses) simplify this process.
The return values of these methods associate each item / collection with the last version (or greater) at which the item / collection was modified.  By passing the keyword argument
since=versionNum
only items / collections which have been modified since
versionNum
are included in the response. Thus, an application which previously sucessfully synced with the server at
versionNum
can use these methods to determine which items / collections need to be retrieved from the server.
Zotero.
item_versions
(
[
search/request
parameters
]
)

Returns a dict containing version information for items in the library
Return type
:
dict: string -> integer
Zotero.
collection_versions
(
itemID
[
,
search/request
parameters
]
)

Returns a dict containing version information for collections in the library
Return type
:
dict: string -> integer
Example of returned version data:
{
## 'C9KW275P'
:
3915
,
## 'IB489TKM'
:
4025
}
Full–Text Content

These methods allow the retrieval of full–text content for given library items
Zotero.
new_fulltext
(
since
)

Returns a dict containing item keys and library versions newer than
since
(a library version string, e.g.
"1085"
)
rtype
:
dict: string -> integer
Example of returned data:
{
u
## '229QED6I'
:
747
,
u
## '22TGJFS2'
:
769
,
u
## '23SZWREM'
:
764
}
Zotero.
fulltext_item
(
itemID
[
,
search/request
parameters
]
)

Returns a dict containing full-text data for the given attachment item.
indexedChars
and
totalChars
are used for text documents, while
indexedPages
and
totalPages
are used for PDFs.
Example of returned data:
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
Zotero.
set_fulltext
(
itemID
,
payload
)

Set full-text data for an item
rtype
:
boolean
itemID
should correspond to an existing attachment item.
payload
: a dict containing three keys:
content
: the full-text content, and either
For text documents,
indexedChars
and
totalChars
## OR
For PDFs,
indexedPages
and
totalPages
.
Example payload:
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
The
follow()
, and
everything()
methods

These methods (currently experimental) aim to make Pyzotero a little more RESTful. Following any Read API call which can retrieve
multiple items
, calling
follow()
will repeat that call, but for the next
x
number of items, where
x
is either a number set by the user for the original call, or 50 by default. Each subsequent call to
follow()
will extend the offset.
Zotero.
follow
(
)

Returns
None
once all available items have been retrieved.
Example:
from
pyzotero
import
Zotero
zot
=
Zotero
(
library_id
,
library_type
,
api_key
)
# only retrieve a single item
# this will retrieve the most recently added/modified top-level item
first_item
=
zot
.
top
(
limit
=
1
)
# now we can start retrieving subsequent items
next_item
=
zot
.
follow
()
third_item
=
zot
.
follow
()
follow()
can thus be used to page through an entire library:
items
=
zot
.
items
()
while
items
:
for
item
in
items
:
# do stuff with the item
...
items
=
zot
.
follow
()
Zotero.
everything
(
)

Example:
from
pyzotero
import
Zotero
zot
=
Zotero
(
library_id
,
library_type
,
api_key
)
# retrieve all top-level items
toplevel
=
zot
.
everything
(
zot
.
top
())
The
everything()
method should work with all Pyzotero Read API calls which can return multiple items, but has not yet been extensively tested.
Feedback is welcomed
.
Related generator methods

The
Zotero.iterfollow()
and
Zotero.makeiter()
methods are available for users who prefer to work directly with generators:
Zotero.
iterfollow
(
)

Return type
:
a generator over the
follow()
method.
Example:
z
=
zot
.
top
(
limit
=
5
)
lazy
=
zot
.
iterfollow
()
next
(
lazy
)
# the next() call has returned the next five items
Zotero.
makeiter
(
## API
call
)

Returns a generator over a Read API method
Parameters
:
call
(
function API
) – a Pyzotero Read API method capable of returning multiple items
Return type
:
generator
Example:
gen
=
zot
.
makeiter
(
zot
.
top
(
limit
=
5
))
next
(
gen
)
# this will return the first five items
next
(
gen
)
# this will return the next five items
Warning
The
follow()
,
everything()
and
makeiter()
methods are only valid for methods which can return multiple library items. For instance, you cannot use
follow()
after an
item()
call. The generator methods will raise a
StopIteration
error when all available items retrievable by your chosen API call have been exhausted.
Retrieving item counts

If you wish to retrieve item counts for subsets of a library, you can use the following methods:
Zotero.
num_items
(
)

Returns the count of top-level items in the library
Return type
:
int
Zotero.
num_collectionitems
(
collectionID
)

Returns the count of items in the specified collection
Return type
:
int
Retrieving last modified version

If you wish to retrieve the last modified version of a user or group library, you can use the following method:
Zotero.
last_modified_version
(
)

Returns the last modified version of the library
Return type
:
int
The Local Zotero API

Setting
local=True
directs Pyzotero at the HTTP API served by a running Zotero
installation (
http://127.0.0.1:23119/api
) instead of
api.zotero.org
. It must
first be enabled in Zotero, under Settings > Advanced > “Allow other applications on
this computer to communicate with Zotero”.
Read requests need no authentication. Write requests need two things: a server ID,
which Pyzotero handles for you, and a local API key, which requires the user’s consent.
This section is organised in three parts:
How local write access works
covers the
concepts behind local write access,
How-to guides
gives step-by-step recipes
for common tasks, and
Reference
describes the attribute, the method,
and the behavioural differences from the web API.
How local write access works

Server IDs

Every local API response carries a
Zotero-Server-ID
header identifying the Zotero
instance the data came from. It persists with the user’s database. Pyzotero caches it
from the first local response and sends it back on subsequent requests, so that a
request made against a different instance — or the same one after a database restore —
is rejected with
ServerIDMismatchError
rather than silently mixing data.
You never need to fetch the ID yourself: Pyzotero obtains it automatically before the
first write. It matters to you only if your program persists data between runs, in
which case see the warning below and
How to keep write access across sessions
.
Versions

Warning
Versions reported by the local API are scoped to a server ID. They bear
no relation
to web API versions, nor to versions from any other Zotero instance, and because local
changes need no sync they are typically
lower
than the versions the local API
reported before write support was added. Any program that persists objects or versions
retrieved from the local API — for
since=
queries, or its own change tracking —
must partition that data by
server_id
, and should discard data cached against a
different one. A mismatch raises
ServerIDMismatchError
.
Local API keys

Local API keys are unrelated to zotero.org API keys: they are granted by the running
Zotero application itself, and only with the user’s consent. Requesting one makes
Zotero display a dialog offering three choices. “Allow” grants a
single-use
key:
the first successful write consumes it, and the next write fails with
LocalAPIKeyRequiredError
. “Always Allow” grants a persistent key, which
the caller may store and reuse across sessions. “Deny” raises
LocalAPIDeniedError
.
How-to guides

How to make your first local write

Create a client with
local=True
.
Call
Zotero.authorize_local()
and approve the dialog Zotero displays.
Call any write method.
from
pyzotero
import
Zotero
zot
=
Zotero
(
'0'
,
'user'
,
local
=
True
)
zot
.
authorize_local
(
'My Application'
)
# Zotero prompts the user
zot
.
create_items
([
item
])
How to keep write access across sessions

Call
Zotero.authorize_local()
and have the user choose “Always Allow”.
Check the
remember
flag on the returned dict: it is
True
only for a
persistent key. Store the key together with
Zotero.server_id
.
On a later run, pass both back to the constructor.
auth
=
zot
.
authorize_local
(
'My Application'
)
if
auth
[
'remember'
]:
save_somewhere
(
zot
.
server_id
,
auth
[
'key'
])
# on a later run
zot
=
Zotero
(
'0'
,
'user'
,
local
=
True
,
server_id
=
saved_server_id
,
local_api_key
=
saved_key
)
How to recover from a consumed or revoked key

A single-use key is consumed by the first successful write, and the user can revoke a
persistent key in Zotero’s settings. In both cases the next write raises
LocalAPIKeyRequiredError
. Catch it and re-authorise:
from
pyzotero
import
Zotero
,
LocalAPIKeyRequiredError
try
:
zot
.
create_items
([
item
])
except
LocalAPIKeyRequiredError
:
zot
.
authorize_local
(
'My Application'
)
zot
.
create_items
([
item
])
How to add a file attachment

Zotero.attachment_simple()
and
Zotero.attachment_both()
are
unavailable in local mode (see
Differences from the web API
). Build the attachment
dict yourself and pass it to
Zotero.upload_attachments()
, which works
normally:
attachment
=
{
'itemType'
:
'attachment'
,
'linkMode'
:
'imported_file'
,
'title'
:
'paper.pdf'
,
'filename'
:
'/path/to/paper.pdf'
,
'contentType'
:
'application/pdf'
,
'charset'
:
''
,
'note'
:
''
,
'tags'
:
[],
'relations'
:
{},
}
zot
.
upload_attachments
([
attachment
],
parent_item_key
)
Reference

Zotero.
server_id

The local API’s server ID, or
None
if it is not yet known. Readable and
writable: a program can persist it alongside its own data and supply it on a
later run via the
server_id
constructor argument. Pyzotero fetches it
automatically before the first write if it is not already set.
Zotero.
authorize_local
(
app_name
)

Request a local API key. Zotero displays a dialog offering “Allow” (one-time
access), “Always Allow” (persistent access) and “Deny”. On approval the key is
stored on the instance as
local_api_key
and sent with subsequent local writes.
Parameters
:
app_name
(
str
) – the caller’s display name, shown to the user in the dialog
Return type
:
dict containing a
key
string and a
remember
boolean
remember
is
True
only for a persistent key; a single-use key must be
replaced by a further call once a write has consumed it.
Raises
LocalAPIDeniedError
if the user denies the request. Zotero
rate-limits this endpoint, so it must not be called in a retry loop.
The exceptions specific to the local API —
LocalAPIKeyRequiredError
,
LocalAPIDeniedError
,
ServerIDMismatchError
and
ServerIDRequiredError
— are listed under
Errors
.
Differences from the web API

Zotero.item_template()
is unavailable: the local API implements the item
type and field endpoints, but not
/items/new
. Zotero may add it in future, in which
case the method starts working with no change to Pyzotero. Build item dicts directly and pass
them to
Zotero.create_items()
, using
Zotero.item_types()
and
Zotero.item_type_fields()
to discover the valid fields. Calling it in local
mode raises
CallDoesNotExistError
.
For the same reason
Zotero.attachment_simple()
and
Zotero.attachment_both()
, which build an attachment template internally, are
unavailable. Use
Zotero.upload_attachments()
with a hand-built attachment
dict instead: see
How-to guides
.
Keyed writes require a concurrency precondition: either a
version
on each object,
which objects retrieved from the API already carry, or an explicit
last_modified
argument. Payloads built by hand without either are rejected.
Item type and field endpoints return names in the user’s locale; the
locale
parameter is ignored.
Zotero.creator_fields()
always returns English.
Atom is not supported, and there are no rate limits on ordinary requests.
Results are not paginated by default, so
Zotero.everything()
is rarely needed.
Requests go to
127.0.0.1
, not
localhost
: Zotero listens on the IPv4 loopback
address only. The default client ignores proxy settings from the environment
(
## HTTP_PROXY
,
## ALL_PROXY
and the system proxy configuration).
For the full list, see the
local API documentation
.
Write API Methods

Saved Searches

Pyzotero allows you to retrieve, delete, or modify saved searches:
Zotero.
searches
(
)

Retrieve all saved searches. Note that this retrieves saved search
metadata
, as opposed to
content
; saved searches cannot currently (January 2019) be run using the API.
Return type
:
list of dicts
Zotero.
saved_search
(
name
,
conditions
)

Create a new saved search.
conditions
is a list of one or more dicts, each of which must contain the following three string keys:
condition
,
operator
,
value
. See the
documentation
for an example.
Parameters
:
name
(
str
) – the name of the search
conditions
(
list
) – one or more dicts containing search conditions and operators
Return type
:
dict showing creation success status
Zotero.
delete_saved_search
(
search_keys
)

Delete one or more saved searches.
search_keys
is a list of one or more search keys. These can be retrievd using
Zotero.searches()
Parameters
:
search_keys
(
list
) – list of unique saved search keys
Return type
:
None
Zotero.
show_operators
(
)

Show available saved search operators
Return type
:
list
Zotero.
show_conditions
(
)

Show available saved search conditions
Return type
:
list
Zotero.
show_condition_operators
(
condition
)

Show available operators for a given saved search condition
Parameters
:
condition
(
str
) – a valid saved search condition
Return type
:
list
Item Methods

Zotero.
item_types
(
)

Returns a dict containing all available item types
Return type
:
dict
Zotero.
item_fields
(
)

Returns a dict of all available item fields
Return type
:
dict
Zotero.
item_creator_types
(
itemtype
)

Returns a dict of all valid creator types for the specified item type
Parameters
:
itemtype
(
str
) – a valid Zotero item type. A list of available item types can be obtained by the use of
item_types()
Return type
:
dict
Zotero.
creator_fields
(
)

Returns a dict containing all localised creator fields
Return type
:
dict
Zotero.
item_type_fields
(
itemtype
)

Returns all valid fields for the specified item type
Parameters
:
itemtype
(
str
) – a valid Zotero item type. A list of available item types can be obtained by the use of
item_types()
Return type
:
list of dicts
Zotero.
item_template
(
itemtype
,
linkmode
)

Returns an item creation template for the specified item type
Parameters
:
itemtype
(
str
) – a valid Zotero item type. A list of available item types can be obtained by the use of
item_types()
linkmode
(
str
) – either None (default) or a valid Zotero linkMode value required when itemtype is attachment. A list of available link modes can be obtained by the use of
item_attachment_link_modes()
Return type
:
dict
Creating and Updating Items

Zotero.
create_items
(
items
[
,
parentid
,
last_modified
]
)

Create Zotero library items
Parameters
:
items
(
list
) – one or more dicts containing item data
parentid
(
str
) – A Parent item ID. This will cause the item(s) to become the child items of the given parent ID
last_modified
(
str/int
) – If not None will set the value of the If-Unmodified-Since-Version header.
Return type
:
list of dicts
Returns a copy of the created item(s), if successful. Use of
item_template()
is recommended in order to first obtain a dict with a structure which is known to be valid.
Before calling this method, the use of
check_items()
is encouraged, in order to confirm that the item to be created contains only valid fields.
Note that if any items contain a key field matching an existing item on the server it will be updated (any properties not in the dict will be left unmodified).
Example:
template
=
zot
.
item_template
(
'book'
)
template
[
'creators'
][
0
][
'firstName'
]
=
'Monty'
template
[
'creators'
][
0
][
'lastName'
]
=
'Cantsin'
template
[
'title'
]
=
'Maris Kundzins: A Life'
resp
=
zot
.
create_items
([
template
])
If successful,
resp
will be a dict containing the creation status of each item:
{
'failed'
:
{},
'success'
:
{
'0'
:
## 'ABC123'
},
'unchanged'
:
{}}
Zotero.
update_item
(
item
[
,
last_modified
]
)

Update an item in your library
Parameters
:
item
(
dict
) – a dict containing item data.  Fields not in item will be left unmodified.
last_modified
(
str/int
) – If not
None
, will set the value of the If-Unmodified-Since-Version header.  If unspecified/None then If-Unmodified-Since-Version will be set to the version property of item.
Return type
:
Boolean
Will return
True
if the request was successful, or will raise an error.
Example:
i
=
zot
.
items
()
# see above for example of returned item structure
# modify the latest item which was added to your library
i
[
0
][
'data'
][
'title'
]
=
'The Sheltering Sky'
i
[
0
][
'data'
][
'creators'
][
0
][
'firstName'
]
=
'Paul'
i
[
0
][
'data'
][
'creators'
][
0
][
'lastName'
]
=
'Bowles'
zot
.
update_item
(
i
[
0
])
Zotero.
update_items
(
items
[
,
last_modified
]
)

Update items in your library. The API only accepts 50 items per call, so longer updates are chunked
Parameters
:
items
(
list
) – a list of dicts containing Item data. Fields not in item will be left unmodified.
last_modified
(
int
) – optional library version, sent as
If-Unmodified-Since-Version
. Only needed when the dicts carry no
version
of their own; the local API rejects keyed writes that have neither.
Return type
:
Boolean
Will return
True
if the request was successful, or will raise an error.
Zotero.
check_items
(
items
)

Check whether items to be created on the server contain only valid keys. This method first creates a set of valid keys by calling
item_fields()
, then compares the user-created dicts to it. If any keys in the user-created dicts are unknown, a
InvalidItemFields
exception is raised, detailing the invalid fields.
deleted
is a valid key: the API returns it on trashed objects, and accepts it on write.
Parameters
:
items
(
list
) – one or more dicts containing item data
Return type
:
List. Each list item is a valid dict containing item data.
Uploading files

Warning
Attachment methods are in beta.
Zotero.
attachment_simple
(
files
[
,
parentid
]
)

Create one or more file attachment items.
Parameters
:
files
(
list
) – a list containing one or more file paths:
['/path/to/file/file.pdf',
…
]
parentid
(
string
) – a library Item ID. If this is specified, attachments will be created as child items of this ID.
Return type
:
Dict. Showing status of each requested upload.
Zotero.
attachment_both
(
files
[
,
parentid
]
)

Create one or more file attachment items, specifying names for uploaded files
Parameters
:
files
(
list
) – a list containing one or more lists or tuples in the following format:
(file
name,
file
path)
parentid
(
string
) – a library Item ID. If this is specified, attachments will be created as child items of this ID.
Return type
:
Dict. Showing status of each requested upload.
Zotero.
upload_attachments
(
attachments
[
,
parentid
,
basedir
=
None
]
)

Upload files to their corresponding attachments.  If the attachments lack the
key
property they are assumed not to exist and will be created.  The
parentid
parameter is
not compatible
with existing attachments.  In order for uploads to succeed, the filename parameter of each attachment must resolve.
This method is really only required in cases where a sync has been interrupted, leaving your library with attachment items that don’t have corresponding files attached. It
may
also work for uploading modified files, though
this is untested
.
Parameters
:
attachments
(
list
) – A list of dicts representing zotero imported files which may or may not already have their key fields filled in.
parentid
(
string
) – a library Item ID. If this is specified and key fields are not included, attachments will be created as child items of this ID.
basedir
(
string/path
) – A string or path object to which the filenames specified in attachments will be evaluated relative to.  If unspecified the filenames are evaluated as they are.
Return type
:
Dict. Showing status of each requested upload.
# example of the return type
{
'success'
:
[
attach1
,
attach2
...
],
'failure'
:
[
attach3
,
attach4
...
],
'unchanged'
:
[
attach4
,
attach5
...
]
}
Note
unlike the space-saving responses from the server, the return value here eschews the complex index / key lookup and simply passes back the
imported_file
item template populated with keys (if created successfully or passed in) corresponding to each result. This is the return type for all of these methods. Entries additionally carry the item’s current
version
(as reported by the server after the item’s final write step), so a follow-up
Zotero.update_item()
call can be made without refetching the item first.
Note
the
filename
you pass is used to locate the file on disk (relative to
basedir
, if given), so it may be a path. The API doesn’t accept a directory path in a stored-file item’s
filename
field, so only the basename is sent when the attachment item is created. Entries returned under
failure
because the server rejected the item at creation time contain the server’s reason under an
error
key, e.g.
{'code':
400,
'message':
'…'}
.
Deleting items

Zotero.
delete_item
(
item
[
,
last_modified
]
)

Delete one or more items from your library
Parameters
:
item
(
list
) – a list of one or more dicts containing item data. You must first retrieve the item(s) you wish to delete, as
version
data is required.
last_modified
(
str/int
) – If not
None
, will set the value of the If-Unmodified-Since-Version header.
Note
delete_item()
is permanent. To move an item to the trash instead, set
deleted
to
1
on it and pass it to
update_item()
. Setting
deleted
to
0
restores it.
item
=
zot
.
item
(
## 'ABC123'
)
item
[
'data'
][
'deleted'
]
=
1
zot
.
update_item
(
item
[
'data'
])
Deleting tags

Zotero.
delete_tags
(
tag_a
[
,
tag
…
]
)

Delete one or more tags from your library
Parameters
:
tag
(
string
) – the tag(s) you’d like to delete
You may also pass a list using
zot.delete_tags(*[tag_list])
Adding tags

Zotero.
add_tags
(
item
,
tag
[
,
tag
…
]
)

Add one or more tags to an item, and update it on the server
Parameters
:
item
(
dict
) – a dict containing item data
tag
(
string
) – the tag(s) you’d like to add to the item
Return type
:
list of dicts
You may also pass a list using
zot.add_tags(item,
*[tag_list])
Example:
z
=
zot
.
top
(
limit
=
1
)
# we've now retrieved the most recent top-level item
updated
=
zot
.
add_tags
(
z
[
0
],
'tag1'
,
'tag2'
,
'tag3'
)
# updated now contains a representation of the updated server item
Collection Methods

Zotero.
create_collections
(
dicts
[
,
last_modified
]
)

Create a new collection in the Zotero library
Parameters
:
dicts
(
list
) – list of dicts each containing the key
name
, with each value being a new collection name you wish to create. Each dict may optionally contain a
parentCollection
key, the value of which is the ID of an existing collection. If this is set, the collection will be created as a child of that collection.
last_modified
(
str/int
) – If not None will set the value of the If-Unmodified-Since-Version header.
Return type
:
list of dicts
Return type
:
Boolean
Zotero.
create_collection
(
dicts
[
,
last_modified
]
)

Alias for
Zotero.create_collections()
to preserve backward compatibility
Zotero.
addto_collection
(
collection
,
item
)

Add the specified item(s) to the specified collection
Parameters
:
collection
(
str
) – a collection key
item
(
dict
) – an item dict retrieved using an API call
Return type
:
Boolean
Collection keys can be obtained by a call to
collections()
(see details above).
Zotero.
deletefrom_collection
(
collection
,
item
)

Remove the specified item from the specified collection
Parameters
:
collection
(
str
) – a collection key
item
(
dict
) – a dict containing item data
Return type
:
Boolean
See the
delete_item()
example for multiple-item removal.
Zotero.
moveto_collection
(
from_collection
,
to_collection
,
item
)

Move the specified item from one collection to another, in a single request
Parameters
:
from_collection
(
str
) – the key of the collection to remove the item from
to_collection
(
str
) – the key of the collection to add the item to
item
(
dict
) – an item dict retrieved using an API call
Return type
:
Boolean
The item’s membership of other collections is unchanged. If the item is not in
from_collection
, it is still added to
to_collection
. Calling
deletefrom_collection()
followed by
addto_collection()
does not work for this: the first call changes the item’s version, so the second call fails its version check.
item
=
zot
.
item
(
## "ITEMKEY"
)
zot
.
moveto_collection
(
## "OLDCOLL"
,
## "NEWCOLL"
,
item
)
Zotero.
update_collection
(
collection
,
last_modified]
)

Update existing collection metadata (name etc.)
Parameters
:
collection
(
dict
) – a dict containing collection data, previously retrieved using one of the Collections calls (e.g.
collections()
)
Return type
:
Boolean
Zotero.
update_collections
(
collection_items
[
,
last_modified
]
)

Update multiple existing collection metadata. The API only accepts 50 collections per call, so longer updates are chunked
Parameters
:
collection_items
(
list
) – a list of dicts containing Collection data. Fields not in collection_item will be left unmodified.
last_modified
(
int
) – optional library version, sent as
If-Unmodified-Since-Version
. Only needed when the dicts carry no
version
of their own; the local API rejects keyed writes that have neither.
Return type
:
Boolean
Will return
True
if the request was successful, or will raise an error.
Zotero.
collection_tags
(
collectionID
[
,
search/request
parameters
]
)

Retrieve all tags for a given collection
Parameters
:
collectionID
(
str
) – a collection ID
Return type
:
list of strings
Examples:
# get existing collections, which will return a list of dicts
c
=
zot
.
collections
()
# rename the last collection created in the library
c
[
0
][
'name'
]
=
'Whither Digital Humanities?'
# update collection name on the server
zot
.
update_collection
(
c
[
0
])
Zotero.
delete_collection
(
collection
[
,
last_modified
]
)

Delete a collection from the Zotero library
Parameters
:
collection
(
dict
) – a dict containing collection data, previously retrieved using one of the Collections calls (e.g.
collections()
). Alternatively, you may pass a
list
of collection dicts.
last_modified
(
str/int
) – If not None will set the value of the If-Unmodified-Since-Version header.
Return type
:
Boolean
Notes

Most Read API methods return
lists
of
dicts
or, in the case of tag methods,
lists
of
strings
. Most Write API methods return either
True
if successful, or raise an error. See
zotero_errors.py
for a full listing of these.
Warning
URL parameters will supersede API calls which should return e.g. a single item:
https://api.zotero.org/users/${LIBRARY_ID}/items/ABC?start=50&limit=10
will return 10 items beginning at position 50, even though
## ABC
does not exist. Be aware of this, and don’t pass URL parameters which do not apply to a given API method.
License

Pyzotero is licensed under the
Blue Oak Model Licence
license.
Cat Picture

This is The Grinch.
Orangecat

[
*
]
This isn’t strictly true: you only need an API key for personal libraries and non-public group libraries.
© Copyright 2011 - 2026, Stephan Hügel.
Built with
Sphinx
using a
theme
provided by
Read the Docs
.
This page uses
Google Analytics
to collect statistics. You can disable it by blocking
the JavaScript coming from www.google-analytics.com.
