> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Pendar: capabilities.json

Это переносимый справочный контракт/каталог. Он не содержит действующее подключение или права аккаунта. `${...}` обозначает значение целевой установки; оно заменяется с сохранением требуемого JSON-типа. Состав методов и ограничения сверяются с устанавливаемой версией.

```json
{
  "selected_mcp_tools": [
    "verify_paper",
    "survey_literature",
    "graph_hopper",
    "audit_bibliography",
    "profile_researcher",
    "find_venues"
  ],
  "mcp_authorization_url": "https://pendar.ai/mcp/oauth/authorize",
  "mcp_authentication_options": [
    "OAuth with tools:read (selected; independent Hermes BN client)",
    "Dedicated MCP API key (alternative; shown once; not created)"
  ],
  "web_app_modes": {
    "Explore Literature": "Ranked papers and digest based on abstracts",
    "Deep Research": "Cited synthesis; full texts where available; separate web workflow",
    "Validate a Claim": "Strength of evidence for one scientific sentence; differs from bibliographic verification",
    "Analyze Research Landscape": "Clusters, trends, gaps and funding; Broad/Balanced/Strict breadth",
    "Chat with Papers": "User-provided PDFs and page-grounded questions/comparison",
    "Create Literature Review": "Draft from processed PDFs; educational/review article/introduction/proposal",
    "Schedule Briefing": "Monthly email digest; separate explicit subscription/scheduling decision"
  },
  "mcp_limitations": [
    "Only public published research records",
    "No access to saved searches/reports/private PDFs",
    "No account changes",
    "Web application modes are not equivalent to the MCP methods"
  ],
  "checked_at": "2026-10-07",
  "live_mcp_catalog_pending": true
}
```
