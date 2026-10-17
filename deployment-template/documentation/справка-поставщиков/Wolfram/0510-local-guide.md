> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: local-guide

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Wolfram Local MCP Documentation
## WOLFRAM
Products
Wolfram|One
The definitive Wolfram Language and notebook experience
Mathematica
The original technical computing environment
System Modeler
Multidomain modeling and simulation of complex systems
Compute Services
Use with Mathematica and Wolfram|One
AI Access
Use with Mathematica and Wolfram|One
Finance Platform
Wolfram|Alpha Notebook Edition
Application Server
Enterprise Private Cloud
Wolfram Engine
Wolfram Player
Wolfram Cloud App
Wolfram Player App
More mobile apps
Wolfram|Alpha
Wolfram|Alpha Website
Wolfram|Alpha APIs
AI Products
Wolfram AI Ecosystem
Wolfram Foundation Tool
Wolfram Cloud MCP
Wolfram Local MCP
Agent One API
CAG Component APIs
Core Technologies of Wolfram Products
Wolfram Language
Computable Data
Wolfram Notebooks
Linguistic Understanding
Additional Deployment Options
Wolfram Cloud
Wolfram Web Engine
wolframscript
WSTPServer
Group & Organizational Licensing
All Products
Consulting & Solutions
We deliver solutions for the AI era—combining symbolic computation, data-driven insights and deep technical expertise
Wolfram Consulting
Data Science, Finance & Business
Artificial Intelligence
Data Science
Healthcare
Real Estate
Engineering
Civil Engineering
Automotive Engineering
Sustainable Energy
Science & Technology
AgTech
Biosciences
Environmental Science
Food Science
Quantum Computation
Social and Behavioral Sciences
More Wolfram Solutions
Technology for Education
Research Universities
Colleges & Teaching Universities
High Schools
Resources for Students
Education Initiatives
Next-Gen EdTech
Computer-Based Math
More Solutions for Education
Contact Us
Learning
& Support
Get Started
Wolfram Language Introduction
Fast Intro for Programmers
Fast Intro for Math Students
Wolfram Language Documentation
More Learning
Highlighted Core Areas
Demonstrations
YouTube
Daily Study Groups
Wolfram Schools and Programs
Books
Grow Your Skills
Wolfram U
Courses in computing, science, life and more
Community
Learn, solve problems and share ideas.
Blog
News, views and insights from Wolfram
Resources for
Software Developers
Tech Support
Contact Us
Support FAQs
Support FAQs
Contact Us
Company
About Wolfram
Career Center
All Sites & Resources
Connect & Follow
Contact Us
Work with Us
Student Ambassador Initiative
Wolfram for Startups
Student Opportunities
Jobs Using Wolfram Language
Educational Programs for Adults
Summer School
Winter School
Educational Programs for Youth
Middle School Camp
High School Research Program
Computational Adventures
Read
Stephen Wolfram's Writings
Wolfram Blog
Wolfram Tech | Books
Wolfram Media
Complex Systems
Educational Resources
Wolfram MathWorld
Wolfram in STEM
Wolfram Challenges
Wolfram Problem Generator
Wolfram Initiatives
Wolfram Science
Wolfram Foundation
History of Mathematics Project
Events
Stephen Wolfram Livestreams
Online & In-Person Events
Contact Us
Connect & Follow
For AIs
Wolfram Cloud
Your Account
Your Account
User Portal
Wolfram Cloud
Search
Close
Navigation Menu
Products
Wolfram|One
Mathematica
System Modeler
Compute Services
Use with Mathematica and Wolfram|One
AI Access
Use with Mathematica and Wolfram|One
Finance Platform
Wolfram|Alpha Notebook Edition
Application Server
Enterprise Private Cloud
Wolfram Engine
Wolfram Player
Wolfram Cloud App
Wolfram Player App
More mobile apps
Wolfram|Alpha
Wolfram|Alpha Website
Wolfram|Alpha APIs
AI Products
Wolfram AI Ecosystem
Wolfram Foundation Tool
Wolfram Cloud MCP
Wolfram Local MCP
Agent One API
CAG Component APIs
Core Technologies
Wolfram Language
Computable Data
Wolfram Notebooks
Linguistic Understanding
Additional Deployment Options
Wolfram Cloud
Wolfram Web Engine
wolframscript
WSTPServer
Group &
Organizational Licensing
All Products
Consulting & Solutions
Wolfram Consulting
Data Science, Finance & Business
Artificial Intelligence
Data Science
Healthcare
Real Estate
Engineering
Civil Engineering
Automotive Engineering
Sustainable Energy
Science & Technology
AgTech
Biosciences
Environmental Science
Food Science
Quantum Computation
Social and Behavioral Sciences
More Wolfram Solutions
Technology for Education
Research Universities
Colleges & Teaching Universities
High Schools
Resources for Students
Education Initiatives
Next-Gen EdTech
Computer-Based Math
More Solutions for Education
Contact Us
Learning & Support
Get Started
Wolfram Language Introduction
Fast Intro for Programmers
Fast Intro for Math Students
Wolfram Language Documentation
Grow Your Skills
Wolfram U
Courses in computing, science, life and more
Community
Learn, solve problems and share ideas.
Blog
News, views and insights from Wolfram
Resources for
Software Developers
Tech Support
Contact Us
Support FAQs
More Learning
Highlighted Core Areas
Demonstrations
YouTube
Daily Study Groups
Wolfram Schools and Programs
Books
Support FAQs
Contact Us
Company
About Wolfram
Career Center
All Sites & Resources
Connect & Follow
Contact Us
Work with Us
Student Ambassador Initiative
Wolfram for Startups
Student Opportunities
Jobs Using Wolfram Language
Educational Programs for Adults
Summer School
Winter School
Educational Programs for Youth
Middle School Camp
High School Research Program
Computational Adventures
Read
Stephen Wolfram's Writings
Wolfram Blog
Wolfram Tech | Books
Wolfram Media
Complex Systems
Educational Resources
Wolfram MathWorld
Wolfram in STEM
Wolfram Challenges
Wolfram Problem Generator
Wolfram Initiatives
Wolfram Science
Wolfram Foundation
History of Mathematics Project
Events
Stephen Wolfram Livestreams
Online & In-Person Events
Contact Us
Connect & Follow
For AIs
Wolfram Cloud
Your Account
User Portal
Enable JavaScript to interact with content and submit forms on Wolfram websites.
Learn how
Connecting to Wolfram Local MCP
This guide covers how to connect a local Wolfram Engine—such as Wolfram|One or Mathematica—to an LLM using
using Wolfram Local MCP. Starting in Version 15, the
paclet
that
powers this functionality is built into the product.
For information on how to connect to Wolfram Cloud MCP instead, go
here
.
Table of Contents
Chat Clients (Claude Desktop, etc.)
Recommended Server
Installation
Available Tools
Example Use Cases
Persistent Instructions
Tips for Best Results
AI Coding Applications (Claude Code, Cursor, VS Code, etc.)
Recommended Server
Installation
Configuring AI Guidance with AGENTS.md
Best Practices
Security Considerations
Server Customization
Troubleshooting
Chat Clients
Recommended Server
For general-purpose chat, use the
Wolfram
server (the default). It combines code
execution with natural language computation.
Installation
Claude Desktop
Open a Wolfram Language session and run:
PacletSymbol["Wolfram/AgentTools",
"Wolfram`AgentTools`InstallMCPServer"]["ClaudeDesktop"]
After installation,
fully restart Claude Desktop
to load the new tools.
Other Chat Clients
For other MCP-compatible clients, generate the raw JSON configuration and adapt it manually:
PacletSymbol["Wolfram/AgentTools",
"Wolfram`AgentTools`MCPServerObject"]["Wolfram"]["JSONConfiguration"]
Verifying the Installation
After restarting, ask your AI assistant:
"What is the integral of sin(x)cos(x)?"
If the AI uses Wolfram tools to compute the answer, the installation is working.
Available Tools
The Wolfram server provides several tools. The AI selects the appropriate one automatically based on your
request—you do not need to specify which tool to use.
Tool
Description
WolframLanguageContext
Semantic search across Wolfram resources (documentation, Wolfram|Alpha, repositories and more)
WolframLanguageEvaluator
Execute Wolfram Language code
WolframAlpha
Natural language queries to Wolfram|Alpha
ReadNotebook
Read Wolfram Notebooks (.nb) as Markdown
WriteNotebook
Convert Markdown to Wolfram Notebooks
SymbolDefinition
Look up symbol definitions in readable format
CodeInspector
Inspect code for issues and return a formatted report
TestReport
Run Wolfram Language test files (.wlt)
Example Use Cases
Mathematics and Computation
"Solve the equation x³ - 6x² + 11x - 6 = 0."
"Find the eigenvalues of the matrix {{1,2},{3,4}}."
"Compute the Taylor series of e^x around x=0 to order 5."
"What is the derivative of log(sin(x))?"
Data and Facts
"What is the population of France?"
"How far is Mars from Earth right now?"
"What is the boiling point of ethanol at 0.5 atm?"
"Compare the GDP of Japan and Germany over the last 10 years."
Visualization
"Plot sin(x) and cos(x) from 0 to 2pi."
"Create a bar chart comparing the populations of the 10 largest US cities."
"Show a 3D plot of sin(x*y) for x and y from -pi to pi."
Documentation Lookup
"How does the Wolfram Language
NestList
function work?"
"What options does
ListPlot
support?"
"Show me examples of using
Association
with
GroupBy
."
Code Assistance
"Write a Wolfram Language function that finds all prime factors of a number."
"How do I read a CSV file and compute column averages in Wolfram Language?"
"Explain what this code does:
FoldList[Plus, 0, Range[10]]
"
Persistent Instructions
Persistent instructions are custom text your chat client sends to the AI at the start of every
conversation, like standing orders.
Setting Them in Claude Desktop
Open Claude Desktop.
Go to Settings (gear icon).
Select the
General
tab.
Enter your instructions under the
Profile
section.
Save changes.
Ready-to-Use Templates
General Computational Use
When I ask mathematical or scientific questions, use Wolfram tools to compute exact answers rather than approximating. Show the Wolfram Language code you used so I can learn from it.
For factual questions (population, distance, chemical properties, etc.), use Wolfram|Alpha for up-to-date data.
When producing plots or visualizations, use clear labels and legends.
Learning Wolfram Language
I am learning Wolfram Language. When I ask how to do something:
1. First use WolframContext to find relevant functions and documentation.
2. Write the code using WolframLanguageEvaluator and show me the result.
3. Explain each part of the code.
4. Suggest related functions I might find useful.
Prefer idiomatic Wolfram Language style. Use functional programming patterns (Map, Select, Fold, etc.) over procedural loops when appropriate.
Research and Data Analysis
I use Wolfram tools for research and data analysis. When I ask questions:
- Use Wolfram|Alpha for current data and facts.
- Use WolframLanguageEvaluator for computations, statistics and visualizations.
- Always cite the source of factual data (e.g. "According to Wolfram|Alpha...").
- When creating visualizations, export them at high resolution.
For statistical analysis, show the code and interpret the results in plain language. Include relevant measures of uncertainty when appropriate.
Tips for Customizing
Be specific about your field or domain (e.g. "I work in signal processing").
Mention output preferences (e.g. "Always show LaTeX-formatted equations").
State your experience level so explanations are calibrated appropriately.
Keep instructions concise; overly long instructions may dilute their effect.
Tips for Best Results
Be specific.
"Plot the Bessel function J0 from 0 to 20" works better than "Show
me a
Bessel function."
Ask for explanations.
"Solve this and explain each step" produces more useful
responses.
Iterate on visualizations.
Start with a basic plot, then refine: "Make the axes
larger
and add a grid."
Combine tools.
"Look up the formula for black-body radiation and then plot it for
## T =
3000K, 5000K, and 7000K" uses both documentation search and code evaluation.
Request code.
Ask "Show me the Wolfram Language code" to see what the AI runs.
AI Coding Applications
Recommended Server
For Wolfram Language development, use the
WolframLanguage
server. It gives the AI
the
ability to:
Search Wolfram resources including documentation, function repository, data repository and more.
Execute code to test implementations and verify behavior.
Read and write notebooks (
.nb
files) as Markdown.
Look up symbol definitions to understand existing code.
Inspect code for potential issues and style problems.
Run tests to validate changes against your test suite.
Installation
All installation methods use the
InstallMCPServer
function. Open a Wolfram Language
session
and run the appropriate command for your application.
Claude Code
Global
(available in all projects):
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["ClaudeCode", "WolframLanguage"]
Project level
(available only in a specific directory):
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"ClaudeCode", "/path/to/project"}, "WolframLanguage"]
Verify from the command line:
claude mcp get WolframLanguage
Cline
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Cline", "WolframLanguage"]
Copilot CLI
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["CopilotCLI", "WolframLanguage"]
Verify:
copilot -i "/mcp show"
Cursor
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Cursor", "WolframLanguage"]
Verify: Settings →
Tools & MCP
→ confirm "WolframLanguage" is listed.
Gemini CLI
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["GeminiCLI", "WolframLanguage"]
Verify:
gemini -i "/mcp"
Google Antigravity
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Antigravity", "WolframLanguage"]
Verify: Editor view →
...
menu →
Agent
panel →
## MCP
Servers
→
Manage MCP Servers
.
Kiro
Global
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Kiro", "WolframLanguage"]
Project level
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"Kiro", "/path/to/project"}, "WolframLanguage"]
OpenAI Codex
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Codex", "WolframLanguage"]
Verify:
codex mcp get WolframLanguage
OpenCode
Global
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["OpenCode", "WolframLanguage"]
Project level
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"OpenCode", "/path/to/project"}, "WolframLanguage"]
Verify:
opencode mcp list
Visual Studio Code
Global
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["VisualStudioCode", "WolframLanguage"]
Project level
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"VisualStudioCode", "/path/to/project"}, "WolframLanguage"]
Windsurf
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Windsurf", "WolframLanguage"]
Zed
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Zed", "WolframLanguage"]
Other Clients
Generate the raw JSON configuration and adapt it manually:
PacletSymbol["Wolfram/AgentTools","Wolfram`AgentTools`MCPServerObject"]["WolframLanguage"]["JSONConfiguration"]
Verifying the Installation
After installing, restart your coding tool and ask the AI:
"What Wolfram Language tools do you have access to?"
The AI should list tools like
WolframLanguageEvaluator
,
WolframLanguageContext
,
TestReport
, etc.
Configuring AI Guidance with AGENTS.md
AI coding tools start each session with no memory of previous conversations. An
AGENTS.md
file at the root of your project gives the AI essential context about your codebase, conventions and
how
to use Wolfram Language tools effectively.
Claude Code note:
Claude Code uses
CLAUDE.md
rather than
AGENTS.md
. For projects using multiple AI coding tools, you can either put
@AGENTS.md
inside your
CLAUDE.md
to auto-include its contents or create
CLAUDE.md
as a symlink:
ln -s AGENTS.md CLAUDE.md
.
Why It Matters
Without guidance, the AI will not know when to use
WolframLanguageContext
to look up documentation, may miss your project's coding
conventions,
and will skip testing and code inspection.
What to Include
Tool guidance
— When and how to use each Wolfram Language tool
Project layout
— Directory structure, key files, entry points
Code style
— Naming conventions, patterns, error handling approach
Testing
— How to run tests, where test files live, test format
AGENTS.md Template
# AGENTS.md
## Overview
Brief description of what your project does.
## Development
Always use the WolframLanguageContext tool when working with Wolfram Language code to look up documentation and find relevant functions before writing code.
When you make changes to source code, write and run tests using the TestReport tool and check your work with the CodeInspector tool.
## Project Structure
- `Kernel`-Main source files
- `MyPaclet.wl`-Entry point
- `Utilities.wl`-Helper functions
- `Tests`-Test files (.wlt)
- `Documentation`-Notebooks and docs
## Code Style
- Use `UpperCamelCase` for public function names
- Use `lowerCamelCase` for internal function names
- Use `Enclose/Confirm` for error handling:
{```wl
myFunction[arg_] := Enclose[
Module[{result},
result = ConfirmBy[computation[arg], StringQ];
result
]
];
```}
## Writing Tests
Write tests in this format:
{```wl
VerificationTest[
input,
expected,
TestID -> "DescriptiveTestID"
]
```}
Test files go in the `Tests/` directory with a `.wlt` extension.
## Key Patterns
Describe any project-specific patterns, conventions or architectural decisions that the AI should follow.
Update
AGENTS.md
whenever you add new files or directories, establish new coding
patterns,
discover edge cases the AI should know about or change testing strategies.
Best Practices
Test-Driven Development
AI coding tools work well with a test-driven workflow:
Write tests first describing the expected behavior.
Ask the AI to implement the function to pass the tests.
Run tests with
TestReport
to verify.
Iterate until all tests pass.
Use Planning Mode
For nontrivial tasks, ask the AI to plan before implementing. Many applications support a built-in
"planning mode." Use it to review the proposed approach before writing code.
Manage Context over Long Tasks
AI coding tools have finite context windows. For complex features spanning multiple sessions, a
manual
context management approach often works better than relying on automated compression.
When to use structured sessions:
Features requiring more than one implementation session
Work spanning multiple hours or days
Tasks where maintaining accuracy is critical
The workflow
—maintain three working documents:
Document
Purpose
Specs/FeatureName.md
Detailed specification and API design
TODO/FeatureName.md
Task checklist: one task per session
Progress/FeatureName.md
Session log capturing decisions and findings
Spec document example
# Feature: CSV Import with Schema Validation
## Requirements
- Parse CSV files into lists of Associations
- Support custom column type specifications
- Validate data against provided schema
- Return Failure objects for invalid data
## API Design
CSVImportValidated[file, schema]
(* returns {<|...|>, ...} or Failure *)
## Schema Format
<|"Name" →  "String", "Age" →  "Integer", "Score" → "Real"|>
## Edge Cases
- Empty files return {}
- Missing columns return Failure["MissingColumn", ...]
- Type mismatches return Failure["TypeError", ...]
Per-session prompt (
prompt.md
)
## Context
@TODO/CSVImportValidated.md
@Specs/CSVImportValidated.md
@Progress/CSVImportValidated.md
## Instructions
1. Choose the next incomplete task from the task list.
2. Study the specification requirements for that task.
3. Implement the task.
4. Append a progress report to Progress/CSVImportValidated.md.
5. Mark the task complete in TODO/CSVImportValidated.md.
6. Commit your changes.
7. Stop and wait for user input.
IMPORTANT: Complete only ONE task per session.
Run each session with:
claude "$(cat prompt.md)"
Start a
fresh session
after each task rather than continuing the same
conversation. Review
and edit the progress file manually to ensure it captures the right context.
Security Considerations
The
WolframLanguageEvaluator
and
TestReport
tools execute arbitrary
Wolfram
Language code. This means they can read, write and delete files; make network requests; run system
commands;
and access environment variables.
Configure your application to
require approval
before the AI executes these tools.
Most AI
coding applications support approval-based permissions for this purpose.
CodeInspector
and
ReadNotebook
read file contents that are sent to your
## LLM
provider. If your project contains sensitive information, consider requiring approval for these
tools as
well.
Prompt Injection
If your AI coding application fetches content from the web or other
untrusted sources, be aware that malicious content could instruct the AI to use other tools in
unintended
ways. As a general rule, if you auto-approve tools that read untrusted external content, require
approval
for all tools that could expose sensitive information.
Server Customization
For information on creating and deploying a custom MCP server, see the
AgentTools documentation
.
Troubleshooting
Server Not Connecting
Fully restart
your chat client or coding application after installation.
Closing the
window often just minimizes it to the system tray.
Check your client's documentation for log file locations and inspect them for errors.
WolframContext
Not Working as Expected
For best results, be sure you've upgraded to
Wolfram Version 15
. Prior to this,
WolframContext
required a separate subscription for full functionality. Without it, Wolfram|Alpha results are not included, and documentation search accuracy is reduced. Version 15 includes everything needed.
Computation Timeouts
By default, evaluations have a 60-second time limit. Ask the AI to increase the timeout or break
the
computation into smaller steps.
Server Using the Wrong Version of Wolfram
Language
The installed MCP server uses the same Wolfram Language version as the session it was installed
from. To
use a different version, either install the MCP server from a session running that version or
manually edit
the configuration file to point to a different Wolfram kernel.
Source:
Wolfram
AgentTools Paclet Repository
— © 2026 Wolfram Research
Products
Wolfram|One
Mathematica
AI Access
Compute Services
System Modeler
Wolfram|Alpha Notebook Edition
Wolfram|Alpha Pro
Mobile Apps
Wolfram Engine
Wolfram Player
Volume & Site Licensing
Server Deployment Options
Consulting
Wolfram Consulting
Repositories
Data Repository
Function Repository
Community Paclet Repository
Neural Net Repository
Prompt Repository
Wolfram Language Example Repository
Notebook Archive
Wolfram GitHub
Learning
Wolfram U
Wolfram Language Documentation
Webinars & Training
Educational Programs
Wolfram Language Introduction
Fast Introduction for Programmers
Fast Introduction for Math Students
Books
Wolfram Community
Wolfram Blog
Public Resources
Wolfram|Alpha
Wolfram Problem Generator
Wolfram Challenges
Computer-Based Math
Computational Thinking
Computational Adventures
Demonstrations Project
Wolfram Data Drop
MathWorld
Wolfram Science
Wolfram Media Publishing
Customer Resources
Store
Product Downloads
User Portal
Your Account
Organization Access
Support FAQ
Contact Support
Company
About Wolfram
Careers
Contact
Events
Wolfram Community
Wolfram Blog
Facebook
## X
Twitch
LinkedIn
YouTube
Wolfram
Legal
&
Privacy Policy
WolframAlpha.com
|
WolframCloud.com
Facebook
## X
Twitch
LinkedIn
YouTube
Wolfram
©
2026
Wolfram
©
2026
Wolfram
|
Legal
&
Privacy Policy
|
English
English
Español
Français
