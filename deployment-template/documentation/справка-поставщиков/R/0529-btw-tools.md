> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка R: btw-tools

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Tools: Register tools from btw — btw_tools • btw
Skip to contents
btw
1.5.0
Reference
Changelog
Light
Dark
Auto
Tools: Register tools from btw
Source:
R/tools.R
btw_tools.Rd
The
btw_tools()
function provides a list of tools that can be registered
with an ellmer chat via
chat$register_tools()
that allow the chat to
interface with your computational environment. Chats returned by
this function have access to the tools:
Group: agent
Name
Description
btw_tool_agent_subagent()
Delegate a task to a specialized assistant that can work independently with its own conversation thread.
Group: cran
Name
Description
btw_tool_cran_package()
Describe a CRAN package.
btw_tool_cran_search()
Search for an R package on CRAN.
btw_tool_cran_versions()
List a CRAN package's release versions and dates.
Group: docs
Name
Description
btw_tool_docs_available_vignettes()
List available vignettes for an R package.
btw_tool_docs_help_page()
Get help page from package.
btw_tool_docs_package_help_topics()
Get available help topics for an R package.
btw_tool_docs_package_news()
Read the release notes (NEWS) for a package.
btw_tool_docs_vignette()
Get a package vignette in plain text.
Group: env
Name
Description
btw_tool_env_describe_data_frame()
Show the data frame or table or get information about the structure of a data frame or table.
btw_tool_env_describe_environment()
List and describe items in the R session's global environment.
Group: files
Name
Description
btw_tool_files_edit()
Edit a text file using hashline references for precise, targeted modifications.
btw_tool_files_list()
List files or directories in the project.
btw_tool_files_patch()
Apply a patch envelope that adds, updates, deletes, or moves files atomically.
btw_tool_files_read()
Read the contents of a text file.
btw_tool_files_replace()
Find and replace exact string occurrences in a text file.
btw_tool_files_search()
Search code files in the project.
btw_tool_files_write()
Write content to a text file.
Group: git
Name
Description
btw_tool_git_branch_checkout()
Switch to a different git branch.
btw_tool_git_branch_create()
Create a new git branch.
btw_tool_git_branch_list()
List git branches in the repository.
btw_tool_git_commit()
Stage files and create a git commit.
btw_tool_git_diff()
View changes in the working directory or a commit.
btw_tool_git_log()
Show the commit history for a repository.
btw_tool_git_status()
Show the status of the git working directory.
Group: github
Name
Description
btw_tool_github()
Execute R code that calls the GitHub API using gh().
Group: ide
Name
Description
btw_tool_ide_read_current_editor()
Read the contents of the editor that is currently open in the user's IDE.
Group: pkg
Name
Description
btw_tool_pkg_check()
Run comprehensive package checks.
btw_tool_pkg_coverage()
Compute test coverage for an R package.
btw_tool_pkg_document()
Generate package documentation.
btw_tool_pkg_load_all()
Load package code to verify it loads correctly.
btw_tool_pkg_test()
Run testthat tests for an R package.
Group: run
Name
Description
btw_tool_run_r()
Run R code.
Group: sessioninfo
Name
Description
btw_tool_sessioninfo_is_package_installed()
Check if a package is installed in the current session.
btw_tool_sessioninfo_package()
Verify that a specific package is installed, or find out which packages are in use in the current session.
btw_tool_sessioninfo_platform()
Describes the R version, operating system, language and locale settings for the user's system.
Group: skills
Name
Description
btw_tool_skill()
Load a skill's specialized instructions and list its bundled resources.
Group: web
Name
Description
btw_tool_web_read_url()
Read a web page and convert it to Markdown format.
Usage
btw_tools
(
...
)
Arguments
...
Optional names of tools or tool groups to include when registering
tools. By default all btw tools are included. For example, use
"docs"
to
include only the documentation related tools, or
"env", "docs", "session"
for the collection of environment, documentation and session
tools, and so on.
The names provided can be:
The name of a tool, such as
"btw_tool_env_describe_data_frame"
.
The name of a tool group, such as
"env"
, which will include all tools
in that group.
The tool name without the
btw_tool_
prefix, such as
"env_describe_data_frame"
.
Value
Registers the tools with
chat
, updating the
chat
object in
place. The
chat
input is returned invisibly.
Examples
# requires an ANTHROPIC_API_KEY
ch
<-
ellmer
::
chat_anthropic
(
)
#>
Using
model
=
"claude-sonnet-5"
.
# register all of the available tools
ch1
<-
ch
$
clone
(
)
ch1
$
register_tools
(
btw_tools
(
)
)
#>
Warning:
GitHub tools are not available because you are not authenticated with the gh
#>
package.
#>
ℹ
Run `gh::gh_whoami()` to check your authentication status.
#>
ℹ
Run `gitcreds::gitcreds_set()` or set the GITHUB_PAT environment variable to
#>
authenticate.
#>
This warning is displayed once per session.
# or register only the tools related to fetching documentation
ch2
<-
ch
$
clone
(
)
ch2
$
register_tools
(
btw_tools
(
"docs"
)
)
# ensure that the current tools persist
ch3
<-
ch
$
clone
(
)
ch3
$
register_tools
(
c
(
ch3
$
get_tools
(
)
,
btw_tools
(
)
)
)
On this page
Developed by
Garrick Aden-Buie
,
Simon Couch
, Joe Cheng, Posit Software, PBC.
Site built with
pkgdown
2.2.1.
