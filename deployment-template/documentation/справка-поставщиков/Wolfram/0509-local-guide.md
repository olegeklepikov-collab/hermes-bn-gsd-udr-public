> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Wolfram: local-guide

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


<div class="page-width">

<div class="page-padding">

<div class="section">

<div id="view">

# Connecting to Wolfram Local MCP

This guide covers how to connect a local Wolfram Engine—such as Wolfram\|One or Mathematica—to an LLM using using Wolfram Local MCP. Starting in Version 15, the [paclet](https://resources.wolframcloud.com/PacletRepository/resources/Wolfram/AgentTools/) that powers this functionality is built into the product.

For information on how to connect to Wolfram Cloud MCP instead, go [here](https://www.wolfram.com/artificial-intelligence/mcp/cloud/wolfram-mcp-cloud/).

------------------------------------------------------------------------

## Table of Contents

- [Chat Clients (Claude Desktop, etc.)](#chat-clients)
  - [Recommended Server](#recommended-server-chat)
  - [Installation](#installation-chat)
  - [Available Tools](#available-tools-chat)
  - [Example Use Cases](#example-use-cases)
  - [Persistent Instructions](#persistent-instructions)
  - [Tips for Best Results](#tips-for-best-results)
- [AI Coding Applications (Claude Code, Cursor, VS Code, etc.)](#ai-coding-applications)
  - [Recommended Server](#recommended-server-coding)
  - [Installation](#installation-coding)
  - [Configuring AI Guidance with AGENTS.md](#configuring-ai-guidance)
  - [Best Practices](#best-practices)
  - [Security Considerations](#security-considerations)
- [Server Customization](#server-customization)
- [Troubleshooting](#troubleshooting)

------------------------------------------------------------------------

## Chat Clients

### Recommended Server

For general-purpose chat, use the **Wolfram** server (the default). It combines code execution with natural language computation.

### Installation

#### Claude Desktop

Open a Wolfram Language session and run:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/claude-desktop.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools",
"Wolfram`AgentTools`InstallMCPServer"]["ClaudeDesktop"]
```

</div>

After installation, **fully restart Claude Desktop** to load the new tools.

#### Other Chat Clients

For other MCP-compatible clients, generate the raw JSON configuration and adapt it manually:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/other-chat-clients.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools",
"Wolfram`AgentTools`MCPServerObject"]["Wolfram"]["JSONConfiguration"]
```

</div>

#### Verifying the Installation

After restarting, ask your AI assistant:

> "What is the integral of sin(x)cos(x)?"

If the AI uses Wolfram tools to compute the answer, the installation is working.

------------------------------------------------------------------------

### Available Tools

The Wolfram server provides several tools. The AI selects the appropriate one automatically based on your request—you do not need to specify which tool to use.

| Tool | Description |
|----|----|
| `WolframLanguageContext` | Semantic search across Wolfram resources (documentation, Wolfram\|Alpha, repositories and more) |
| `WolframLanguageEvaluator` | Execute Wolfram Language code |
| `WolframAlpha` | Natural language queries to Wolfram\|Alpha |
| `ReadNotebook` | Read Wolfram Notebooks (.nb) as Markdown |
| `WriteNotebook` | Convert Markdown to Wolfram Notebooks |
| `SymbolDefinition` | Look up symbol definitions in readable format |
| `CodeInspector` | Inspect code for issues and return a formatted report |
| `TestReport` | Run Wolfram Language test files (.wlt) |

------------------------------------------------------------------------

### Example Use Cases

**Mathematics and Computation**

- "Solve the equation x³ - 6x² + 11x - 6 = 0."
- "Find the eigenvalues of the matrix {{1,2},{3,4}}."
- "Compute the Taylor series of e^x around x=0 to order 5."
- "What is the derivative of log(sin(x))?"

**Data and Facts**

- "What is the population of France?"
- "How far is Mars from Earth right now?"
- "What is the boiling point of ethanol at 0.5 atm?"
- "Compare the GDP of Japan and Germany over the last 10 years."

**Visualization**

- "Plot sin(x) and cos(x) from 0 to 2pi."
- "Create a bar chart comparing the populations of the 10 largest US cities."
- "Show a 3D plot of sin(x\*y) for x and y from -pi to pi."

**Documentation Lookup**

- "How does the Wolfram Language `NestList` function work?"
- "What options does `ListPlot` support?"
- "Show me examples of using `Association` with `GroupBy`."

**Code Assistance**

- "Write a Wolfram Language function that finds all prime factors of a number."
- "How do I read a CSV file and compute column averages in Wolfram Language?"
- "Explain what this code does: `FoldList[Plus, 0, Range[10]]`"

------------------------------------------------------------------------

### Persistent Instructions

Persistent instructions are custom text your chat client sends to the AI at the start of every conversation, like standing orders.

#### Setting Them in Claude Desktop

1.  Open Claude Desktop.
2.  Go to Settings (gear icon).
3.  Select the **General** tab.
4.  Enter your instructions under the **Profile** section.
5.  Save changes.

#### Ready-to-Use Templates

*General Computational Use*

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/general-computational-use-template.txt">

    When I ask mathematical or scientific questions, use Wolfram tools to compute exact answers rather than approximating. Show the Wolfram Language code you used so I can learn from it.

    For factual questions (population, distance, chemical properties, etc.), use Wolfram|Alpha for up-to-date data.

    When producing plots or visualizations, use clear labels and legends.

</div>

*Learning Wolfram Language*

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/learning-wolfram-language-template.txt">

    I am learning Wolfram Language. When I ask how to do something:

    1. First use WolframContext to find relevant functions and documentation.
    2. Write the code using WolframLanguageEvaluator and show me the result.
    3. Explain each part of the code.
    4. Suggest related functions I might find useful.

    Prefer idiomatic Wolfram Language style. Use functional programming patterns (Map, Select, Fold, etc.) over procedural loops when appropriate.

</div>

*Research and Data Analysis*

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/research-and-data-analysis-template.txt">

    I use Wolfram tools for research and data analysis. When I ask questions:

    - Use Wolfram|Alpha for current data and facts.
    - Use WolframLanguageEvaluator for computations, statistics and visualizations.
    - Always cite the source of factual data (e.g. "According to Wolfram|Alpha...").
    - When creating visualizations, export them at high resolution.

    For statistical analysis, show the code and interpret the results in plain language. Include relevant measures of uncertainty when appropriate.

</div>

#### Tips for Customizing

- Be specific about your field or domain (e.g. "I work in signal processing").
- Mention output preferences (e.g. "Always show LaTeX-formatted equations").
- State your experience level so explanations are calibrated appropriately.
- Keep instructions concise; overly long instructions may dilute their effect.

------------------------------------------------------------------------

### Tips for Best Results

- **Be specific.** "Plot the Bessel function J0 from 0 to 20" works better than "Show me a Bessel function."
- **Ask for explanations.** "Solve this and explain each step" produces more useful responses.
- **Iterate on visualizations.** Start with a basic plot, then refine: "Make the axes larger and add a grid."
- **Combine tools.** "Look up the formula for black-body radiation and then plot it for T = 3000K, 5000K, and 7000K" uses both documentation search and code evaluation.
- **Request code.** Ask "Show me the Wolfram Language code" to see what the AI runs.

------------------------------------------------------------------------

## AI Coding Applications

### Recommended Server

For Wolfram Language development, use the **WolframLanguage** server. It gives the AI the ability to:

- Search Wolfram resources including documentation, function repository, data repository and more.
- Execute code to test implementations and verify behavior.
- Read and write notebooks (`.nb` files) as Markdown.
- Look up symbol definitions to understand existing code.
- Inspect code for potential issues and style problems.
- Run tests to validate changes against your test suite.

### Installation

All installation methods use the `InstallMCPServer` function. Open a Wolfram Language session and run the appropriate command for your application.

#### Claude Code

**Global** (available in all projects):

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/claude-code-global.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["ClaudeCode", "WolframLanguage"]
```

</div>

**Project level** (available only in a specific directory):

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/claude-code-project.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"ClaudeCode", "/path/to/project"}, "WolframLanguage"]
```

</div>

Verify from the command line:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/claude-code-verify.txt">

``` sh
claude mcp get WolframLanguage
```

</div>

#### Cline

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/cline.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Cline", "WolframLanguage"]
```

</div>

#### Copilot CLI

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/copilot-cli.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["CopilotCLI", "WolframLanguage"]
```

</div>

Verify: `copilot -i "/mcp show"`

#### Cursor

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/cursor.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Cursor", "WolframLanguage"]
```

</div>

Verify: Settings → **Tools & MCP** → confirm "WolframLanguage" is listed.

#### Gemini CLI

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/gemini-cli.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["GeminiCLI", "WolframLanguage"]
```

</div>

Verify: `gemini -i "/mcp"`

#### Google Antigravity

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/google-antigravity.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Antigravity", "WolframLanguage"]
```

</div>

Verify: Editor view → **...** menu → **Agent** panel → **MCP Servers** → **Manage MCP Servers**.

#### Kiro

**Global**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/kiro-global.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Kiro", "WolframLanguage"]
```

</div>

**Project level**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/kiro-project.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"Kiro", "/path/to/project"}, "WolframLanguage"]
```

</div>

#### OpenAI Codex

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/openai-codex.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Codex", "WolframLanguage"]
```

</div>

Verify: `codex mcp get WolframLanguage`

#### OpenCode

**Global**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/opencode-global.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["OpenCode", "WolframLanguage"]
```

</div>

**Project level**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/opencode-project.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"OpenCode", "/path/to/project"}, "WolframLanguage"]
```

</div>

Verify: `opencode mcp list`

#### Visual Studio Code

**Global**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/visual-studio-code-global.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["VisualStudioCode", "WolframLanguage"]
```

</div>

**Project level**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/visual-studio-code-project.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"][{"VisualStudioCode", "/path/to/project"}, "WolframLanguage"]
```

</div>

#### Windsurf

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/windsurf.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Windsurf", "WolframLanguage"]
```

</div>

#### Zed

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/zed.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools", "Wolfram`AgentTools`InstallMCPServer"]["Zed", "WolframLanguage"]
```

</div>

#### Other Clients

Generate the raw JSON configuration and adapt it manually:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/other-code-clients.txt">

``` wolfram
PacletSymbol["Wolfram/AgentTools","Wolfram`AgentTools`MCPServerObject"]["WolframLanguage"]["JSONConfiguration"]
```

</div>

#### Verifying the Installation

After installing, restart your coding tool and ask the AI:

> "What Wolfram Language tools do you have access to?"

The AI should list tools like `WolframLanguageEvaluator`, `WolframLanguageContext`, `TestReport`, etc.

------------------------------------------------------------------------

### Configuring AI Guidance with AGENTS.md

AI coding tools start each session with no memory of previous conversations. An `AGENTS.md` file at the root of your project gives the AI essential context about your codebase, conventions and how to use Wolfram Language tools effectively.

> **Claude Code note:** Claude Code uses `CLAUDE.md` rather than `AGENTS.md`. For projects using multiple AI coding tools, you can either put `@AGENTS.md` inside your `CLAUDE.md` to auto-include its contents or create `CLAUDE.md` as a symlink: `ln -s AGENTS.md CLAUDE.md`.

#### Why It Matters

Without guidance, the AI will not know when to use `WolframLanguageContext` to look up documentation, may miss your project's coding conventions, and will skip testing and code inspection.

#### What to Include

1.  **Tool guidance** — When and how to use each Wolfram Language tool
2.  **Project layout** — Directory structure, key files, entry points
3.  **Code style** — Naming conventions, patterns, error handling approach
4.  **Testing** — How to run tests, where test files live, test format

#### AGENTS.md Template

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/agents-md-template.txt">

``` markdown
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
```

</div>

Update `AGENTS.md` whenever you add new files or directories, establish new coding patterns, discover edge cases the AI should know about or change testing strategies.

------------------------------------------------------------------------

### Best Practices

#### Test-Driven Development

AI coding tools work well with a test-driven workflow:

1.  Write tests first describing the expected behavior.
2.  Ask the AI to implement the function to pass the tests.
3.  Run tests with `TestReport` to verify.
4.  Iterate until all tests pass.

#### Use Planning Mode

For nontrivial tasks, ask the AI to plan before implementing. Many applications support a built-in "planning mode." Use it to review the proposed approach before writing code.

#### Manage Context over Long Tasks

AI coding tools have finite context windows. For complex features spanning multiple sessions, a manual context management approach often works better than relying on automated compression.

**When to use structured sessions:**

- Features requiring more than one implementation session
- Work spanning multiple hours or days
- Tasks where maintaining accuracy is critical

**The workflow**—maintain three working documents:

| Document                  | Purpose                                      |
|---------------------------|----------------------------------------------|
| `Specs/FeatureName.md`    | Detailed specification and API design        |
| `TODO/FeatureName.md`     | Task checklist: one task per session         |
| `Progress/FeatureName.md` | Session log capturing decisions and findings |

**Spec document example**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/spec-document-example.txt">

``` Markdown
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
```

</div>

**Per-session prompt (`prompt.md`)**

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/per-session-prompt-md.txt">

``` markdown
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
```

</div>

Run each session with:

<div class="terminal-code-wrapper wolfram-c2c-wrapper" data-c2c-type="text/plain" data-c2c-file="/artificial-intelligence/mcp/local/c2c/run-each-session-with.txt">

``` sh
claude "$(cat prompt.md)"
```

</div>

Start a **fresh session** after each task rather than continuing the same conversation. Review and edit the progress file manually to ensure it captures the right context.

------------------------------------------------------------------------

### Security Considerations

The `WolframLanguageEvaluator` and `TestReport` tools execute arbitrary Wolfram Language code. This means they can read, write and delete files; make network requests; run system commands; and access environment variables.

Configure your application to **require approval** before the AI executes these tools. Most AI coding applications support approval-based permissions for this purpose.

`CodeInspector` and `ReadNotebook` read file contents that are sent to your LLM provider. If your project contains sensitive information, consider requiring approval for these tools as well.

#### Prompt Injection

If your AI coding application fetches content from the web or other untrusted sources, be aware that malicious content could instruct the AI to use other tools in unintended ways. As a general rule, if you auto-approve tools that read untrusted external content, require approval for all tools that could expose sensitive information.

------------------------------------------------------------------------

## Server Customization

For information on creating and deploying a custom MCP server, see the [AgentTools documentation](https://resources.wolframcloud.com/PacletRepository/resources/Wolfram/AgentTools/guide/AgentTools.html).

------------------------------------------------------------------------

## Troubleshooting

### Server Not Connecting

- **Fully restart** your chat client or coding application after installation. Closing the window often just minimizes it to the system tray.
- Check your client's documentation for log file locations and inspect them for errors.

### `WolframContext` Not Working as Expected

For best results, be sure you've upgraded to [Wolfram Version 15](https://www.wolfram.com/mathematica/new-in-15/). Prior to this, `WolframContext` required a separate subscription for full functionality. Without it, Wolfram\|Alpha results are not included, and documentation search accuracy is reduced. Version 15 includes everything needed.

### Computation Timeouts

By default, evaluations have a 60-second time limit. Ask the AI to increase the timeout or break the computation into smaller steps.

### Server Using the Wrong Version of Wolfram Language

The installed MCP server uses the same Wolfram Language version as the session it was installed from. To use a different version, either install the MCP server from a session running that version or manually edit the configuration file to point to a different Wolfram kernel.

------------------------------------------------------------------------

*Source: [Wolfram AgentTools Paclet Repository](https://resources.wolframcloud.com/PacletRepository/resources/Wolfram/AgentTools/) — © 2026 Wolfram Research*

</div>

</div>

</div>

</div>
