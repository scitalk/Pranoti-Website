---
title: "Analysing 5 Years of ERC Grant Data with Claude AI"
date: 2026-04-04
draft: false
type: "case-studies"
category: "ai-automation-integration"
display_category: "AI Integration & Automation"
subtitle: "Five years of public ERC funding data turned into interactive dashboards in 15 minutes — using Claude AI and a Google Sheets MCP connection."
description: "Starting, Consolidator, Advanced, and Synergy Grant data downloaded from the EC R&I database, cleaned and analysed by Claude via Google Sheets MCP, and visualised as interactive Chart.js dashboards. From raw export to finished analysis in 15 minutes."
thumbnail: ""
pdf_url: ""
tech_stack:
  - "Claude Desktop"
  - "Google Sheets MCP"
  - "EC R&I Dashboard (Qlik Sense)"
  - "CORDIS"
  - "Chart.js"
  - "HTML"
metrics:
  - value: "822"
    label: "grants analysed (2021–2024)"
  - value: "~15 min"
    label: "raw data to finished dashboards"
  - value: "4"
    label: "interactive dashboards produced"
problem:
  goal: "Understand which institutions win ERC grants, which domains dominate, and how funding is distributed — **without spending days in a BI tool**."
  reality: "The EC publishes granular data on every funded project but it lives in Qlik Sense — a platform most researchers and grant advisors have never used. Cleaning, analysing, and visualising the export has historically required **data skills most people don't have time to develop**."
workflow:
  before:
    - "Navigate Qlik Sense to find the right dataset"
    - "Export and manually clean raw data"
    - "Build analysis formula by formula in a spreadsheet"
    - "Create static charts"
    - "Repeat for each grant type"
  after:
    - "Download filtered export from EC R&I dashboard"
    - "Claude reads, cleans, and analyses via Google Sheets MCP"
    - "Interactive Chart.js dashboard generated — all four grant types in one session"
misconception: "'Detailed ERC grant data isn't publicly available.' **It is.** Every funded project is documented — institution, PI, country, funding, dates, abstract, CORDIS link — in a freely downloadable EC database. The bottleneck was never access. It was **the capacity to analyse it at scale**."
blockers:
  - issue_title: "Qlik Sense is not intuitive for first-time users"
    issue_desc: "Non-obvious how to apply the right filters and export a clean dataset across multiple grant types."
    solution: "**Apply all filters before exporting** — Qlik exports whatever is currently visible. Learn the filter panel first."
  - issue_title: "Raw export needs structuring before any insight emerges"
    issue_desc: "Inconsistent institution naming and mixed grant types require cleaning before analysis is possible."
    solution: "**Claude via Google Sheets MCP** cleans and structures the data in context — no manual formula work."
  - issue_title: "Four dashboards would normally take days to build"
    issue_desc: "STG, COG, ADG, and SyG each have different structures and institution profiles — typically separate pipelines."
    solution: "Claude handled all four in a **single session** with filterable tables, country breakdowns, and institution drill-downs."
outcomes:
  - "Four interactive dashboards covering STG, COG, ADG, and SyG for call years 2021–2024"
  - "Funding patterns identified: Germany and Max Planck lead STG/COG/ADG; CNRS leads Synergy; Life Sciences dominates across all types"
  - "Analysis time reduced from days to ~15 minutes"
  - "Reusable workflow — repeatable each trimester as the EC updates its R&I database"
architecture:
  - ["EC R&I Dashboard (Qlik Sense)", "public database of all ERC-funded projects; filtered by grant type and call year, exported as CSV"]
  - ["Google Sheets MCP", "connects Claude Desktop directly to the spreadsheet; Claude reads, cleans, and structures the raw export in context"]
  - ["Claude AI", "performs cross-grant comparisons, institution ranking, domain breakdowns, and funding aggregations"]
  - ["Chart.js HTML dashboards", "interactive, filterable, embeddable; one per grant type with country and institution drill-downs"]
  - ["CORDIS", "cross-checks project abstracts, PI names, and institutional affiliations where R&I export fields were ambiguous"]
reflection: "The data was always public. What changed is the capacity to work with it without a data team. Connecting Claude to a live spreadsheet via MCP removed the last barrier between public EC data and actionable grant intelligence — and the workflow is repeatable for any Horizon Europe programme."
cta_text: "Full step-by-step guide — how to download EC data, connect Claude via Google Sheets MCP, and build interactive dashboards in one session."
guide_url: "https://pranoti.thesciencetalk.com/ai-guides/erc-grant-data-analysis-funded-institutions/"
---
