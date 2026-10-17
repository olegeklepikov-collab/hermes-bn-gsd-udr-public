> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка Consensus: index

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Consensus

> Developer documentation for Consensus, the AI research engine.

- [What is Consensus](https://docs.consensus.app/get-started/what-is-consensus.md): Consensus is an AI search engine for research. It searches 400 million peer-reviewed papers, analyzes the results, and gives you cited answers you can trace back to the source.
- [Where do papers come from](https://docs.consensus.app/get-started/where-papers-come-from.md): Consensus has the second-largest research index in the world: abstracts and metadata for 400 million peer-reviewed papers, open-access full text, and paywalled full text through publisher partnerships, updated weekly.
- [How search works](https://docs.consensus.app/get-started/how-search-works.md): Consensus finds the most relevant papers with hybrid search, re-ranks the top 1,500 by research quality, refines the top 20 with a larger model, and only then uses AI to synthesize an answer.
- [Full text access to paywalled papers](https://docs.consensus.app/get-started/full-text-access.md): Consensus reads the whole paper, not just the abstract, including paywalled articles from major publishers, open-access PDFs, and papers you upload yourself.
- [Search basics](https://docs.consensus.app/search-basics/overview.md): Short video tutorials that show how to get the most out of Consensus search, each with the exact prompts used so you can run them yourself.
- [Find high-quality recent papers](https://docs.consensus.app/search-basics/find-high-quality-recent-papers.md): Cut through preprints and low-impact work. Stack year, journal quality, and citation filters in plain language, then visualize the results on a research timeline.
- [Find the seminal papers in a field](https://docs.consensus.app/search-basics/find-seminal-papers.md): New to a field? Surface the foundational papers, deep-read the most cited one, and map its citation graph in three searches.
- [Build a comparison table of studies](https://docs.consensus.app/search-basics/build-a-comparison-table.md): Compare interventions side by side with the same metrics. Run parallel searches, then extract sample size, session count, follow-up duration, and effect size into one table.
- [Trace citations forward and backward](https://docs.consensus.app/search-basics/trace-citations.md): Understand where a paper came from and how the field built on it. Bi-directional citation tracing using Attention Is All You Need as the anchor.
- [Snowball from one paper to a reading list](https://docs.consensus.app/search-basics/snowball-reading-list.md): Start from one paper you trust and triangulate similarity, citations, and references to find every adjacent study, then map the gaps.
- [Map the history of a research field](https://docs.consensus.app/search-basics/map-field-history.md): Get the historical arc of a field, not just a list of papers. Early foundations, key breakthroughs, and what changed in the last three years.
- [Catch up on a fast-moving field](https://docs.consensus.app/search-basics/catch-up-on-a-field.md): Fifty new papers a week and no time to read them. Build a what's-new-and-what's-strongest digest grouped by approach, then drill into the winning papers.
- [Find and fill gaps in a Collection](https://docs.consensus.app/search-basics/fill-collection-gaps.md): Run a gap analysis on a Consensus Collection, then automatically pull recent papers that cover the missing topics and populations.
- [Research an author's body of work](https://docs.consensus.app/search-basics/research-an-author.md): Map a researcher's publications, find their most influential paper, and trace its downstream impact. Useful before a meeting, a hire, or a citation.
- [Connect a method from one field to another](https://docs.consensus.app/search-basics/bridge-two-fields.md): Bridge two disciplines in one thread: establish the limits in your field, find where they show up in another, map the gaps, and find collaborators.
- [Find research gaps in your Library with Deep Search](https://docs.consensus.app/search-basics/deep-search-your-library.md): Run a comprehensive analysis across only the papers you've collected. Surface population gaps, missing study types, and follow-up questions across hundreds or thousands of papers.
- [Review a grant before you submit](https://docs.consensus.app/search-basics/grant-review.md): Upload your grant and use Deep Search to find similar studies, compare designs, identify literature gaps, and validate your effect size and sample size assumptions.
- [Check a manuscript for missing citations](https://docs.consensus.app/search-basics/manuscript-citation-check.md): Upload your manuscript and use Deep Search to find supporting and challenging studies, surface papers you missed, and do a final gut check before submitting.
- [Search private documents alongside the index](https://docs.consensus.app/search-basics/private-documents.md): Upload internal reports, proprietary data, or unpublished documents into a Collection and search them alongside 400M peer-reviewed papers, privately.
- [Research Agent](https://docs.consensus.app/core-features/research-agent.md): Research Agent is the AI research assistant behind every Pro message and Deep search in Consensus. It plans searches, chains tools, applies academic filters, and returns citation-backed answers.
- [Deep Search](https://docs.consensus.app/core-features/deep-search.md): Deep is a longer, more robust version of a Consensus search. It runs up to 20 searches in parallel, uses multiple Research Agent tools like citation crawl, and reads 50 to 100 papers before answering.
- [Citation Grounding](https://docs.consensus.app/core-features/citation-grounding.md): Citation Grounding shows the exact quote behind every citation in a Consensus answer. Hover to see the passage, click to jump to it in the paper.
- [Library](https://docs.consensus.app/core-features/library.md): My Library is where you save, organize, and work with research in Consensus. Store papers, searches, and uploaded documents in Collections, import from Zotero, and chat with everything you've collected.
- [Citation Graph](https://docs.consensus.app/core-features/citation-graph.md): Citation Graph is a visual way to explore how papers connect. Start with up to 5 seed papers you trust and discover related work through citation relationships instead of keywords.
- [MCP](https://docs.consensus.app/core-features/mcp.md): The Consensus MCP server lets Claude, ChatGPT, Cursor, and any MCP-compatible client search 400 million peer-reviewed papers from inside the conversation.
- [API](https://docs.consensus.app/core-features/api.md): The Consensus API lets you integrate research search into your own applications, agents, and workflows. One REST endpoint, 400 million papers, self-serve keys.
- [Get started with Consensus API](https://docs.consensus.app/api-get-started.md): Search over 400 million peer-reviewed research papers with the Consensus REST API.
- [Full text in the API](https://docs.consensus.app/api-full-text.md): How the Consensus API uses full text to find papers, and how to get the passages inside each paper that answer your query.
- [API plans and access](https://docs.consensus.app/api-plans-and-access.md): What each Consensus plan includes on the API: monthly calls, papers per request, pagination, full-text excerpts, and rate limits.
- [What you can build with the Consensus API](https://docs.consensus.app/api-use-cases.md)
- [Query for relevant papers.](https://docs.consensus.app/api-reference/query-for-relevant-papers.md): The supported endpoint for searching academic papers. Use this instead of the legacy `/v1/quick_search` endpoint, which is deprecated and will be removed on 2027-02-07.
- [Query for relevant papers (legacy).](https://docs.consensus.app/api-reference/query-for-relevant-papers-legacy.md): This endpoint is deprecated. Use `GET /v1/search` instead. It will be removed on 2027-02-07.
- [Get started with Consensus MCP](https://docs.consensus.app/consensus-mcp.md): The Consensus MCP server enables AI assistants like ChatGPT, Claude, Gemini Spark, and other MCP-compatible clients to search over 400 million peer-reviewed academic research papers directly from the conversation.
- [MCP plans and access](https://docs.consensus.app/mcp-plans-and-access.md): What each Consensus plan includes on the MCP server: papers per search, monthly calls, rate limits, result fields, and API key access.
- [What you can build with the Consensus MCP](https://docs.consensus.app/mcp-use-cases.md)
- [Connect Claude Desktop](https://docs.consensus.app/mcp-clients/claude-desktop.md): Add Consensus to Claude on the web or in the Claude desktop app.
- [Connect Claude Code](https://docs.consensus.app/mcp-clients/claude-code.md): Add the Consensus MCP server to Claude Code with one command.
- [Connect ChatGPT](https://docs.consensus.app/mcp-clients/chatgpt.md): Connect the Consensus app in ChatGPT.
- [Connect Codex](https://docs.consensus.app/mcp-clients/codex.md): Add the Consensus MCP server to OpenAI Codex.
- [Connect Cursor](https://docs.consensus.app/mcp-clients/cursor.md): Install the Consensus MCP server in Cursor.
- [Connect VS Code (GitHub Copilot)](https://docs.consensus.app/mcp-clients/vs-code-github-copilot.md): Add the Consensus MCP server to VS Code with GitHub Copilot.
- [Connect Windsurf](https://docs.consensus.app/mcp-clients/windsurf.md): Add the Consensus MCP server to Windsurf.
- [Connect Gemini Spark](https://docs.consensus.app/mcp-clients/gemini-spark.md): Add Consensus as a custom app for Gemini Spark.
- [Connect Microsoft 365 Copilot](https://docs.consensus.app/mcp-clients/microsoft-365-copilot.md): Connect Consensus in Microsoft 365 Copilot once your admin has added it.
- [Connect Microsoft 365 Copilot Studio](https://docs.consensus.app/mcp-clients/microsoft-365-copilot-studio.md): Add Consensus as a custom MCP tool in Microsoft Copilot Studio.
- [Connect other MCP clients](https://docs.consensus.app/mcp-clients/other-mcp-clients.md): Connect any MCP client that supports remote servers.
- [Consensus for enterprise](https://docs.consensus.app/enterprise/overview.md): Consensus is used by some of the largest research organizations in the world through the MCP server and the API. Pick the deployment shape that fits your organization, then follow the guide for your platform.
- [Connection reference](https://docs.consensus.app/enterprise/connection-reference.md): The technical facts every integration needs: the MCP endpoint, transport behavior, both authentication options, OAuth discovery documents, and the domains to allowlist.
- [Security and data handling](https://docs.consensus.app/enterprise/security.md): Consensus is SOC 2 Type II compliant and hosted on Google Cloud. What leaves your network when someone searches, what comes back, what Consensus stores, and the controls behind it. The questions IT and security teams ask before approving a connector.
- [Microsoft 365 Copilot](https://docs.consensus.app/enterprise/microsoft-365-copilot.md): For Microsoft 365 admins at universities and research institutions: approve Consensus for your tenant so it appears under Sources in Copilot Chat, without opening the app store to everyone.
- [Microsoft Copilot Studio](https://docs.consensus.app/enterprise/copilot-studio.md): Add the Consensus MCP server as a Model Context Protocol tool in Copilot Studio, with per-user OAuth or a shared API key, so your own agents can search 400 million papers.
- [AI gateways and MCP registries](https://docs.consensus.app/enterprise/gateways/overview.md): Register the Consensus MCP server in the gateway your organization already runs. The same five facts work everywhere; product pages give the exact field names.
- [TrueFoundry AI Gateway](https://docs.consensus.app/enterprise/gateways/truefoundry.md): Register the Consensus MCP server in TrueFoundry's MCP Gateway with a shared API key or per-user OAuth.
- [LiteLLM MCP Gateway](https://docs.consensus.app/enterprise/gateways/litellm.md): Add the Consensus MCP server to LiteLLM's config.yaml with a bearer token or per-user OAuth with Dynamic Client Registration.
- [Cloudflare MCP Server Portals](https://docs.consensus.app/enterprise/gateways/cloudflare.md): Add the Consensus MCP server to a Cloudflare One MCP Portal so users reach it through one Access-protected URL.
- [IBM ContextForge MCP Gateway](https://docs.consensus.app/enterprise/gateways/ibm-contextforge.md): Register the Consensus MCP server in IBM's open-source ContextForge gateway with a bearer token or per-user OAuth.
- [Azure API Management](https://docs.consensus.app/enterprise/gateways/azure-api-management.md): Expose the Consensus MCP server through Azure API Management as a passthrough MCP server, with a bearer token injected by policy.
- [AWS Bedrock AgentCore Gateway](https://docs.consensus.app/enterprise/gateways/aws-agentcore.md): Add the Consensus MCP server as an MCP target in Amazon Bedrock AgentCore Gateway with an API key credential provider.
- [Portkey MCP Gateway](https://docs.consensus.app/enterprise/gateways/portkey.md): Register the Consensus MCP server in Portkey's MCP Registry with custom headers or per-user OAuth.
- [Obot MCP Gateway](https://docs.consensus.app/enterprise/gateways/obot.md): Add the Consensus MCP server to Obot as a remote server with custom headers or spec-compliant per-user OAuth.
- [Other gateways](https://docs.consensus.app/enterprise/gateways/other-gateways.md): Kong, Solo.io agentgateway, Zuplo, Docker MCP Gateway, and Boomi AI Gateway can front the Consensus MCP server with a static bearer header; each has a caveat worth knowing.
- [What you can build with the Consensus API and MCP](https://docs.consensus.app/use-cases.md): Search and return the full text of 400+ million research papers — for internal tools, scientific agents, and custom research systems.
- [Start building with the Consensus API and MCP](https://docs.consensus.app/use-cases/get-started.md): Pick a surface, run your first filtered search, and find the guide for what you are building.
- [Best practices](https://docs.consensus.app/use-cases/best-practices.md): The five primitives every Consensus workflow is built from, and how to tell a good use case from a poor one before you build it.
- [Build internal research tools](https://docs.consensus.app/use-cases/internal-tools.md): How enterprise R&D teams, biotechs, and AI startups connect Consensus paper search to internal assistants, monitoring agents, literature tables, and scientific agents.
- [Build custom research systems](https://docs.consensus.app/use-cases/research-systems.md): How academics and research groups use the Consensus API and MCP to build literature-review, writing, and reporting workflows they can reproduce.
- [Use case library](https://docs.consensus.app/use-cases/gallery.md): Worked examples of what people build on Consensus, filterable by persona, each with the full prompt and API call behind it.
- [Find a real citation for every claim in a draft](https://docs.consensus.app/use-cases/ground-a-manuscript.md): Paste a draft section and get every empirical claim matched to a real, verifiable paper — or flagged as unsupported before a reviewer finds it.
- [Verify that every citation is real and supports its claim](https://docs.consensus.app/use-cases/citation-verification.md): Verify every reference in a document actually exists, then confirm each one says what the text citing it claims.
- [Turn a syllabus into a recommended reading list](https://docs.consensus.app/use-cases/syllabus-reading-list.md): Extract course topics and learning outcomes from a syllabus, then produce a curated reading list of recent research with summaries and discussion questions.
- [Find NIH grants for a research idea](https://docs.consensus.app/use-cases/grant-finder.md): Position a research idea against the literature, map it to the right NIH institutes and study sections, and surface NOSIs, open FOAs, and funded overlap.
- [Screen abstracts against inclusion criteria](https://docs.consensus.app/use-cases/abstract-screening.md): Apply explicit inclusion and exclusion criteria across thousands of abstracts, with a decision log a second reviewer can audit.
- [Build a PRISMA-ready search corpus](https://docs.consensus.app/use-cases/prisma-corpus.md): Assemble a reproducible, deduplicated record set with the flow counts a systematic review has to report.
- [Write the search-strategy section of your methods](https://docs.consensus.app/use-cases/search-strategy-methods.md): Turn a logged search into the reproducible methods paragraph reviewers ask for — accurate because it was recorded as it ran.
- [Find which journals to submit to](https://docs.consensus.app/use-cases/where-to-submit.md): Identify the journals actually publishing work like yours, with their quartile, so you target a realistic venue first.
- [Track how a field's terminology changed over time](https://docs.consensus.app/use-cases/terminology-shift.md): Compare old and recent literature on the same concept so you search the terms the field actually used, not just the ones it uses now.
- [Create a biomarker evidence report](https://docs.consensus.app/use-cases/biomarker-report.md): Assess the evidence for a biomarker's optimal range across Mendelian randomization, large cohorts, and trials — or establish that no evidence-based range exists.
- [Build a drug target validation dossier](https://docs.consensus.app/use-cases/target-evidence-tiers.md): Human genetics, in vitro, animal, and clinical evidence for one target in a single pass — including what contradicts it.
- [Monitor new research about a drug, device, or brand](https://docs.consensus.app/use-cases/brand-and-device-monitoring.md): Track what gets published about a drug, device, or brand, and route only the papers that change something.
- [Grade a set of papers with your own evidence rubric](https://docs.consensus.app/use-cases/evidence-grading-rubric.md): Apply your organization's standard for what counts as good evidence, consistently, across every paper on a topic.
- [Find the leading investigators in an indication](https://docs.consensus.app/use-cases/investigator-mapping.md): Rank the authors publishing most in a therapeutic area, split by region and by recent versus lifetime output.
- [Assemble a payer evidence dossier](https://docs.consensus.app/use-cases/payer-evidence-dossier.md): Pull the cost-effectiveness, burden-of-illness, and real-world evidence a reimbursement submission needs, in one pass.
- [Check whether a finding has human evidence yet](https://docs.consensus.app/use-cases/translational-readiness.md): Separate cell and animal work from human studies for a claim, and report the ratio — the number that tells you how translated a finding really is.
- [Extract numbers and formulas from full-text papers](https://docs.consensus.app/use-cases/extract-values-from-full-text.md): Pull numbers, formulas, and parameters out of papers with their measurement conditions attached.
- [Substantiate a product claim with published evidence](https://docs.consensus.app/use-cases/claim-substantiation.md): Build the evidence file behind a claim before it ships — including what contradicts it.
- [Compare candidate materials against published test data](https://docs.consensus.app/use-cases/materials-comparison.md): Search published performance data for each candidate under your actual operating conditions, and find out which combinations nobody has tested.
- [Find published work on a failure or degradation mechanism](https://docs.consensus.app/use-cases/failure-mode-scan.md): Check whether a defect you are seeing is a known mechanism with a published cause, before you spend a quarter rediscovering it.
- [Find published process conditions for a manufacturing step](https://docs.consensus.app/use-cases/process-window-precedent.md): See what temperature, time, atmosphere, and concentration ranges others have published for a process, so you start from precedent rather than from scratch.
- [Check a supplier's performance claim against independent research](https://docs.consensus.app/use-cases/supplier-claim-check.md): Test what a vendor says their material, tool, or process achieves against what the published literature independently reports.
- [Find human-factors evidence for a design decision](https://docs.consensus.app/use-cases/human-factors-evidence.md): Pull the biomechanics, ergonomics, and usability research behind a product or workstation choice, before the decision gets defended after the fact.
- [Build a reusable literature-review workflow](https://docs.consensus.app/use-cases/literature-review-skill.md): A repeatable review workflow that picks a search framework, allocates a search budget, and synthesizes findings into a research guide your whole team can run the same way.
- [Track new papers across many topics on a schedule](https://docs.consensus.app/use-cases/scheduled-research-pipeline.md): Sweep hundreds of topics on a cron, diff against the last run, and report only what changed.
- [Swap a hand-maintained paper corpus for full-text search](https://docs.consensus.app/use-cases/swap-a-paper-corpus.md): Replace a curated PubMed subset you maintain yourself with a weekly-refreshed full-text index, without rebuilding the infrastructure.
- [Add a citable evidence layer to an agent you already ship](https://docs.consensus.app/use-cases/add-an-evidence-layer.md): Give a working agent access to peer-reviewed literature as a tool, so its claims carry citations instead of assertions.
- [Answer one question with many parallel searches](https://docs.consensus.app/use-cases/parallel-search-angles.md): Decompose a research question into multiple search angles, gather evidence across all of them, and distill one cited answer.
- [Screen thousands of target-disease pairs for evidence](https://docs.consensus.app/use-cases/high-throughput-screening.md): Pull literature evidence for every pair in a large matrix — the batch workload that breaks most retrieval APIs.
- [Benchmark literature providers against your own ground truth](https://docs.consensus.app/use-cases/benchmark-retrieval.md): Build a curated query set with known-relevant papers and measure which retrieval provider actually surfaces them.

## OpenAPI Specs

- openapi (локальный ресурс исходного примера не включён)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
