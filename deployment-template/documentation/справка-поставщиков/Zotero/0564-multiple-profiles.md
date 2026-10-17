> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Zotero: multiple-profiles

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


How can I use multiple profiles in Zotero? | Zotero Documentation
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
How can I use multiple profiles in Zotero?
#
Zotero allows you to create multiple profiles, each with its own settings and associated
data directory
. This is an advanced configuration and not recommended for most users, but if you’re familiar with using multiple profiles in Firefox, Zotero works the same way and supports the same command-line flags.
A default profile is created when you first start Zotero. To create an additional profile, start Zotero from the command line and pass the
## -P
flag to open the Profile Manager:
macOS
#
Open Terminal via Spotlight or /Applications/Utilities.
Paste
/Applications/Zotero.app/Contents/MacOS/zotero -P
into the Terminal window.
Press Return
Windows
#
Open the Run dialog (Search/Cortana → type “Run” → Run (Windows 10) or Start → Run (Windows 7)
Paste
C:\\Program Files (x86)\\Zotero\\zotero.exe -P
Press Enter
Linux
#
Start Zotero via the command line, adding the
## -P
command-line flag.
The Profile Manager window should appear, allow you to select, create, and delete Zotero profiles.
When you create a new profile (e.g., “Work”), if there’s already a profile pointing to the default data directory location, Zotero will create a new data directory named after the new profile (e.g., “Zotero Work”) when you first start it. Your original data directory won’t be affected. [
Note, June 2023:
This seems to currently not always happen. If you see your existing data directory in the new profile, create a new data directory manually and point the new profile to there from the Advanced → Files and Folders pane of the Zotero preferences.]
You can open a specific profile from the command line with the
-p
flag (e.g.,
-p Work
), which may be useful for creating shortcuts that automatically open a given profile. (On a Mac, you can save
an AppleScript with command-line flags embedded
as an application in Script Editor.)
Additional configuration may be required when running
multiple instances
of Zotero at a time.
On this page
How can I use multiple profiles in Zotero?
macOS
Windows
Linux
Last updated 2023-06-13
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
