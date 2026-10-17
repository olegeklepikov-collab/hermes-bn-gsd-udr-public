> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: cloud-guide

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


Wolfram Cloud MCP Documentation
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
Connecting to Wolfram Cloud MCP
Server URL:
https://agenttools.wolfram.com/mcp
This guide covers how to connect various LLM applications and IDEs to
Wolfram Cloud MCP
using the
Streamable HTTP transport (the current recommended standard). SSE (server-sent events) transport is
deprecated in the MCP specification but noted where still relevant.
For information on how to connect to Wolfram Local MCP instead, go
here
.
Table of Contents
ChatGPT (Web)
Claude.ai (Web/Desktop/Mobile)
Claude Desktop—Local Config Method
Claude Code (CLI)
Anthropic API (Direct Integration)
Cursor IDE
VS Code with GitHub Copilot
GitHub Copilot CLI
Other Available Registries
Troubleshooting
ChatGPT (Web)
Wolfram is available as an app in the
ChatGPT App Directory
.
Steps Using Official App
Open the
Wolfram
app
page.
If prompted, sign in to your ChatGPT account.
Review the app information, capabilities and permissions.
Click
Connect
.
Once connected, the app should appear in your available apps list.
Verify the Connection
Open a new ChatGPT conversation.
Click the
+
button (or use the Apps menu, depending on your interface).
Locate and select
Wolfram
from your available apps.
Alternatively, if your ChatGPT interface supports app mentions, invoke the app directly in a prompt.
Example Prompts
Use Wolfram to solve and graph x^2 - 5x + 6 = 0.
Use Wolfram to calculate the orbital period of a satellite 400 km above Earth.
Managing the Connection
Open
Settings
in ChatGPT.
Navigate to
Apps
.
Locate
Wolfram
in your connected apps list.
From there you can:
Review permissions
Reconnect the app
Disconnect the app
Claude.ai (Web/Desktop/Mobile)
Wolfram Cloud MCP is available as a
connector
, or
remote MCP servers can be configured as
custom connectors
brokered through your Anthropic
account. The connection originates from Anthropic's cloud infrastructure, so the server must be publicly
reachable.
Steps Using Official Connector
Visit the Wolfram official
Claude connector
## OR
navigate to
claude.ai/customize/connectors
and search
for
Wolfram
in the connector directory.
Click the link under "Used in" to add to Claude.
Click
Connect
.
Once connected, the Wolfram connector will appear in your connector list.
If you'd like to modify the tool's permissions, click the
+
button at the lower left of
the chat interface, select
Connectors
, then
Manage connectors
. We
recommend always allowing
WolframAlpha
and
WolframContext
tools, but setting
WolframLanguageEvaluator
as "Needs Approval." Without modifying permissions, you may need to
approve requests more frequently.
Enabling the Connector in a Conversation
After connecting, enable Wolfram for a specific conversation:
Click the
+
button at the lower left of the chat interface.
Select
Connectors
.
Toggle
Wolfram
on.
Steps Using Custom Connector
Open
claude.ai
and click your account menu in the lower-left corner.
Go to
Settings → Connectors
.
Click
Add custom connector
.
In the dialog, enter:
Name:
Wolfram
## URL:
https://agenttools.wolfram.com/mcp
Click
Add
.
Once connected, the connector will appear in your Connectors list and be available in conversations.
Note:
Remote connectors in Claude.ai are brokered through Anthropic's servers, not your local machine. Local MCP servers configured via
claude_desktop_config.json
are a separate mechanism. Learn more about Wolfram Local MCP
here
.
Claude Desktop—Local Config Method
For servers not yet in the Extensions directory, you can manually configure Claude Desktop via its JSON
config file.
Config file locations:
macOS:
~/Library/Application Support/Claude/claude_desktop_config.json
Windows:
%APPDATA%\Claude\claude_desktop_config.json
Option A—Direct URL (Streamable HTTP, Recommended)
Open
Settings → Developer → Edit Config
and add the following:
{
"mcpServers": {
"wolfram": {
"url": "https://agenttools.wolfram.com/mcp"
}
}
}
Option B—via
mcp-remote
Proxy (Older Claude Desktop Versions)
If your version of Claude Desktop doesn't support direct URL connections, use the
mcp-remote
npm package as a proxy. Requires Node.js.
{
"mcpServers": {
"wolfram": {
"command": "npx",
"args": ["mcp-remote", "https://agenttools.wolfram.com/mcp"]
}
}
}
After editing the config, restart Claude Desktop. Wolfram tools will appear in your conversations.
Organization-Level Tool Control (Team and Enterprise Only)
Owners can disable specific Wolfram tools across the organization:
Navigate to
Organization settings >
Connectors
.
Locate the
Wolfram
connector.
Click the connector to expand its settings.
Disable any tool calls you do not want members to invoke—for example, tools that write data or take
external actions.
Note:
When using Claude's
Research
(Advanced Research) feature with Wolfram connected, Claude may invoke Wolfram tools automatically without per-call approval. Disable write-capable tools before using
Research
if you want to restrict this behavior.
Claude Code (CLI)
Claude Code supports remote MCP servers natively via its
claude mcp add
command. HTTP
transport is the recommended option for remote servers.
Add the Server (Streamable HTTP)
claude mcp add --transport http wolfram https://agenttools.wolfram.com/mcp
Verify the Connection
claude mcp list
# or inside a session:
/mcp
Scoping Options
Scope
Flag
Description
Local (default)
(none)
Available only in the current project
Global
--scope global
Available across all projects
Project (shared)
--scope project
Stored in
.mcp.json
, committable to version control
Manual
.mcp.json
Configuration
(Team Sharing)
Create or edit
.mcp.json
in your project root:
{
"mcpServers": {
"wolfram": {
"type": "streamable-http",
"url": "https://agenttools.wolfram.com/mcp"
}
}
}
Note:
streamable-http
is accepted as an alias for
http
in JSON
configs, for compatibility with server documentation that uses the MCP spec name.
If the server disconnects mid-session, Claude Code will automatically attempt to reconnect with exponential
backoff (up to 5 attempts).
Allowlisting Specific Tools (HTTP Server)
In
.mcp.json
or
~/.claude.json
, use the
tool_configuration
field to
restrict which tools are available:
{
"mcpServers": {
"wolfram": {
"type": "http",
"url": "https://agenttools.wolfram.com/mcp",
"tool_configuration": {
"enabled": true,
"allowed_tools": ["WolframAlpha", "WolframLanguageEvaluator", "WolframContext"]
}
}
}
}
Denylisting Specific Tools
To allow all tools
except
specific ones, use
denied_tools
:
{
"mcpServers": {
"wolfram": {
"type": "http",
"url": "https://agenttools.wolfram.com/mcp",
"tool_configuration": {
"enabled": true,
"denied_tools": ["WriteNotebook", "SubmitPaclet"]
}
}
}
}
Global Permission Deny via Settings
To prevent Claude Code from ever calling a specific tool from any MCP server—including Wolfram—add it to
the
deny
list in
.claude/settings.json
or
~/.claude/settings.json
:
{
"permissions": {
"deny": ["mcp__wolfram__WriteNotebook", "mcp__wolfram__SubmitPaclet"]
}
}
Disabling Tool Search for Wolfram (Always-Load Mode)
By default, Claude Code defers loading MCP tool schemas until needed. To force Wolfram tools to always be
available at session start:
{
"mcpServers": {
"wolfram": {
"type": "http",
"url": "https://agenttools.wolfram.com/mcp",
"alwaysLoad": true
}
}
}
Anthropic API (Direct Integration)
You can connect to the Wolfram MCP server directly from the Anthropic Messages API using the
mcp_servers
parameter. This requires the beta header
mcp-client-2025-11-20
.
Note:
Only MCP tool calls are supported via this method. MCP prompts and resources require
a client-side SDK connection.
Python Example
import anthropic
client = anthropic.Anthropic()
response = client.beta.messages.create(
model="claude-sonnet-4-6",
max_tokens=1000,
messages=[
{"role": "user", "content": "What is the integral of x^2 from 0 to 5?"}
],
mcp_servers=[
{
"type": "url",
"url": "https://agenttools.wolfram.com/mcp",
"name": "wolfram",
}
],
tools=[
{
"type": "mcp_toolset",
"mcp_server_name": "wolfram"
}
],
betas=["mcp-client-2025-11-20"],
)
print(response)
JavaScript/TypeScript Example
const Anthropic = require("@anthropic-ai/sdk");
const client = new Anthropic.Anthropic();
const response = await client.beta.messages.create({
model: "claude-sonnet-4-6",
max_tokens: 1000,
messages: [
{ role: "user", content: "What is the integral of x^2 from 0 to 5?" }
],
mcp_servers: [
{
type: "url",
url: "https://agenttools.wolfram.com/mcp",
name: "wolfram",
}
],
tools: [
{
type: "mcp_toolset",
mcp_server_name: "wolfram"
}
],
betas: ["mcp-client-2025-11-20"],
});
console.log(response);
Restricting Available Tools
{
"tools": [
{
"type": "mcp_toolset",
"mcp_server_name": "wolfram",
"default_config": { "enabled": false },
"configs": {
"WolframAlpha": { "enabled": true },
"WolframLanguageEvaluator": { "enabled": true }
}
}
]
}
Cursor IDE
Cursor supports remote MCP servers via Streamable HTTP. Configuration can be global or project level.
Option A—Settings UI (Recommended)
In the side panel, click
Customize
→
MCPs
.
Choose
+New
.
Add this to the list of MCP servers:
Name:
wolfram
## URL:
https://agenttools.wolfram.com/mcp
Option B—Manual JSON Config
Global:
~/.cursor/mcp.json
Project-level:
.cursor/mcp.json
in your project root (commit to share
with team)
{
"mcpServers": {
"wolfram": {
"url": "https://agenttools.wolfram.com/mcp"
}
}
}
Option C—via
mcp-remote
Proxy (Older Cursor Versions)
{
"mcpServers": {
"wolfram": {
"command": "npx",
"args": ["mcp-remote", "https://agenttools.wolfram.com/mcp"]
}
}
}
After saving, reload the Cursor window or restart the IDE. Wolfram tools will appear in the agent's
tool list.
Tip:
Cursor reads the root key as
"mcpServers"
. Do not use
"servers"
—that is VS Code's key.
VS Code with GitHub Copilot
VS Code uses a different config key from Cursor (
"servers"
instead of
"mcpServers"
). MCP tools only work in
Agent mode
in Copilot Chat.
Prerequisites
VS Code 1.99 or later
GitHub Copilot extension installed
Copilot Chat open in
Agent mode
(select "Agent" from the mode drop-down)
Option A—Command Palette (Recommended)
Open the Command Palette (
Cmd/Ctrl+Shift+P
).
Run
MCP: Add Server…
.
Select
## HTTP
as the server type.
Paste
https://agenttools.wolfram.com/mcp
and press Enter.
Give it the name
wolfram
and choose
Global
(all workspaces) or
Workspace
(current project only).
Option B—Manual
mcp.json
Config
Global:
Run
MCP: Open User Configuration
from the Command Palette.
Workspace:
Create
.vscode/mcp.json
in your project root.
{
"servers": {
"wolfram": {
"type": "http",
"url": "https://agenttools.wolfram.com/mcp"
}
}
}
## A
Start
button will appear in the
mcp.json
file. Click it to activate the
server and discover its tools.
Important:
VS Code uses
"servers"
as the root key, not
"mcpServers"
. Copying a Cursor or Claude Desktop config without changing this key is the
most common setup mistake.
GitHub Copilot CLI
Option A—Interactive
/mcp add
In a Copilot CLI session, run:
/mcp add
When prompted:
Choose
## HTTP
as the server type.
Enter the URL:
https://agenttools.wolfram.com/mcp
Enter the name:
wolfram
Option B—Edit Config File Directly
Global:
~/.copilot/mcp-config.json
Project:
.mcp/copilot/mcp.json
{
"mcpServers": {
"wolfram": {
"type": "http",
"url": "https://agenttools.wolfram.com/mcp"
}
}
}
Save the file and restart Copilot CLI for changes to take effect.
Managing Servers
/mcp show              # list all configured servers
/mcp show wolfram      # details + available tools
/mcp disable wolfram   # disable without removing
/mcp enable wolfram    # re-enable
/mcp delete wolfram    # remove
Other Available Registries
Wolfram Cloud MCP is available through many other registries including:
Smithery.ai
MCP Install
MCP Repository
Troubleshooting
Server Not Connecting
Confirm the URL is reachable:
curl https://agenttools.wolfram.com/mcp
Ensure your network allows outbound HTTPS on port 443.
Tools Not Appearing
Make sure you're using
Agent mode
in VS Code Copilot Chat (tools are invisible in
Ask or Edit modes).
In Claude Code, run
/mcp
inside a session to see server status.
Validate your JSON config with a linter—a single misplaced comma will silently break the file.
Wrong Config Key
Claude Desktop and Cursor use
"mcpServers"
as the root key.
VS Code uses
"servers"
as the root key.
Mixing these up is the most common cross-client copy-paste mistake.
SSE vs. HTTP Transport
SSE (server-sent events) transport is deprecated in the MCP specification. Prefer
http
/
streamable-http
for all new configurations.
If a client requires SSE, use the URL as is; many servers accept both transports at the same
endpoint.
Connecting to Local Wolfram Desktop
For users wanting to connect to their
local
Wolfram Desktop, Mathematica or Wolfram
Engine application, learn more about Wolfram Local MCP
here
.
Source:
Wolfram Cloud MCP
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
