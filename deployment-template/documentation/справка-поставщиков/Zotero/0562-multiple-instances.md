> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: multiple-instances

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


How can I open multiple instances of Zotero and save to or cite from a specific instance? | Zotero Documentation
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
How can I open multiple instances of Zotero and save to or cite from a specific instance?
#
You can start multiple instances of Zotero at the same time as long as they’re pointing to
different profile and data directories
. On Windows and Linux, the
-no-remote command-line flag
may also be required.
Additional configuration may be required for browser and word processor integration, as described below.
Note that using multiple instances of Zotero will use more memory, so depending on how much RAM you have in your computer, using multiple instances at the same time may be slower than using a single instance with more data.
Zotero Connector
#
By default, when running multiple copies of Zotero (either by using multiple profiles or running Zotero in separate OS accounts), the Zotero Connector will save items to the first opened instance. To point a specific Zotero Connector installation to a specific Zotero profile, you can set the
extensions.zotero.httpServer.port
hidden pref
in Zotero and the
connector.url
pref in the connector. Incrementing the port number by 1 for one pair (Zotero profile + connector installation) is sufficient.
Word Processor Integration
#
Word
#
Word for Mac (Zotero 6) / Word for Windows
#
The Word plugin should automatically connect to the correct Zotero instance on a multi-user system. It’s not possible to point the Word plugin at a specific instance of Zotero within the same OS user account.
Word for Mac (Zotero 7)
#
Open the user’s
Word Startup folder
and create a
ZoteroPort.txt
file containing the port number you’ve configured in
extensions.zotero.httpServer.port
.
Google Docs
#
Google Docs integration relies on the Zotero Connector being configured to connect to a specific Zotero instance, as described above.
LibreOffice
#
The LibreOffice plugin uses a fixed HTTP port to connect to Zotero and cannot currently be configured, so it will connect to the first opened instance.
On this page
How can I open multiple instances of Zotero and save to or cite from a specific instance?
Zotero Connector
Word Processor Integration
Word
Word for Mac (Zotero 6) / Word for Windows
Word for Mac (Zotero 7)
Google Docs
LibreOffice
Last updated 2023-08-06
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
