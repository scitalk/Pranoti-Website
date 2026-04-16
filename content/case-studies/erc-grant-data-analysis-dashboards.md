---
title: "Analysing 5 Years of ERC Grant Data with Claude AI"
date: 2026-04-04
subtitle: "Turning 5 years of public ERC funding data (822 grants) into interactive dashboards in 15 minutes using Claude AI and Google Sheets MCP."
category: "AI Integration"
tech_stack:
  - "Claude AI"
  - "Google Sheets MCP"
  - "EC R&I Dashboard"
  - "CORDIS"
  - "Chart.js"
metrics:
  - value: "822"
    label: "grants analysed"
  - value: "~15 min"
    label: "raw data to dashboard"
  - value: "4"
    label: "interactive dashboards"
problem:
  goal: "Analyze 5 years of ERC grants (institutions, domains, funding) **without relying on complex BI tools**."
  reality: "Exporting, cleaning, and visualizing the EC's public data requires specialized skills most researchers lack."
workflow:
  before:
    - "Filter Qlik Sense"
    - "Export raw CSV"
    - "Clean data"
    - "Build formulas"
    - "Make static charts"
  after:
    - "Download EC data"
    - "Feed to Claude via MCP"
    - "Claude generates dashboards"
misconception: "The bottleneck wasn't finding the data—**every funded project is publicly documented**. The real barrier was having the technical capacity to clean and analyze it at scale."
blockers:
  - issue_title: "Unintuitive BI Tools"
    issue_desc: "Applying correct filters across multiple grant types in Qlik Sense is confusing."
    solution: "**Export raw CSV directly** once filters are set."
  - issue_title: "Messy raw data"
    issue_desc: "Exported datasets contain inconsistent naming and nested fields."
    solution: "**Pass data to Claude via MCP** for context-aware cleaning."
  - issue_title: "Slow multi-grant analysis"
    issue_desc: "Different grant types require separate analysis pipelines."
    solution: "Claude processed all four in a **single session**."
outcomes:
  - "**Four interactive dashboards** covering STG, COG, ADG, and SyG"
  - "**Key patterns identified**: Germany/Max Planck lead STG/COG/ADG"
  - "**Time reduced from days to ~15 minutes** (export to dashboard)"
architecture:
  - ["Data source", "EC R&I Dashboard CSV export"]
  - ["Data pipeline", "Google Sheets MCP connection"]
  - ["Analysis engine", "Claude AI for data processing"]
  - ["Output layer", "Chart.js HTML dashboards"]
  - ["Reference data", "CORDIS for cross-checking PIs"]
cta_text: "Read the full analysis: What 5 years of ERC data reveals about Europe's top research institutions."

guide_url: "https://pranoti.thesciencetalk.com/ai-guides/erc-grant-data-analysis-funded-institutions/"
related_tst_posts:
  - title: "ERC Guidelines on AI in Grant Proposal Evaluation — The Science Talk"
    url: "https://thesciencetalk.com/erc-ai-grant-proposal-evaluation-guidelines/"
  - title: "How I Used GenAI to Support €1M Grant Proposals — The Science Talk"
    url: "https://thesciencetalk.com/ai-tools-for-proposal-writing/"
---