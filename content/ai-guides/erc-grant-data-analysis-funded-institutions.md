---
title: "How to Analyse ERC Grant Data Using Claude AI and Google Sheets"
date: 2026-04-04
lastmod: 2026-04-04
draft: false
description: "Turn five years of public ERC funding data into interactive dashboards using Claude AI and Google Sheets MCP — from raw export to finished analysis in 15 minutes."
keywords: ["ERC grant data analysis", "Claude AI Google Sheets", "ERC funded institutions dashboard", "Horizon Europe data", "Google Sheets MCP data analysis", "CORDIS data download", "ERC grant strategy"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["ERC", "Claude AI", "Google Sheets MCP", "data analysis", "grant strategy"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com and MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
sidebar_product:
  label: "RESOURCE KIT"
  title: "ERC Starting Grant 2027 — 51 Official Resources"
  bullets:
    - "51 verified official resources for your ERC StG 2027 application"
    - "Organised into 11 sections"
    - "Compiled by The Science Talk"
  details:
    - "Instant access"
  stripe_url: "/products/erc-starting-grant-resource-kit/"
  cta: "Get the resource kit →"
  footnote: ""
---

The European Commission publishes detailed data on every ERC-funded project. This data includes host institution, PI, country, funding amount, project dates, abstract, and CORDIS link. All of it is public and downloadable. Almost no one uses it, including researchers, grant advisors, and research development offices. This guide shows how to find the data, export it from the official EC database, and build interactive dashboards with Claude AI and a Google Sheets MCP connection. The whole process takes about 15 minutes.

## Why this data matters

The ERC budget for 2021–2027 is **€16 billion**. That is 17% of the entire Horizon Europe budget. Since 2007, the ERC funded more than **18,000 projects** and distributed **€32.5 billion**. The ERC evaluated over 140,000 proposals and supported more than 10,000 researchers across 97 nationalities. ERC grantees published over 200,000 journal articles, filed more than 2,200 patents, and founded over 400 startups. ERC grantees won 15 Nobel Prizes, 6 Fields Medals, and 12 Wolf Prizes.

The breakdown by grant type:

| Grant type | Projects | Total funding |
|---|---|---|
| Starting Grant (STG) | 7,341 | €10.8 billion |
| Advanced Grant (ADG) | 4,303 | €10 billion |
| Consolidator Grant (COG) | 4,136 | €8.2 billion |
| Synergy Grant (SyG) | 306 | €3.2 billion |
| Proof of Concept | 2,397 | €358 million |

This is a large dataset. It can show you which institutions win grants, which scientific domains dominate, how funding concentrates by country and region, and how the landscape changed over time. For anyone working on ERC applications, or advising researchers who are, this is useful competitive intelligence.

Many people assume this level of detail is not public. It is. The EC database contains everything: institution name, PI, CORDIS project link, abstract, funding amount, project start and end date, project status, country, and region, for every funded project. Access was never the problem. The problem was the capacity to analyze the data at scale.

## What you need before starting

- **Claude Desktop** — with the [Google Sheets MCP](/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/) connected and working
- **A Google account** — to store the downloaded data in Sheets
- **Access to the EC R&I Dashboard** — no login required, publicly accessible

## Finding and downloading the data

Start at the [ERC projects and statistics page](https://erc.europa.eu/projects-statistics/erc-dashboard). This page links to the European Commission's R&I Dashboard, the actual structured database.

Direct link to the R&I Dashboard:
[https://dashboard.tech.ec.europa.eu/qs_digit_dashboard_mt/public/sense/app/c140622a-87e0-412e-8b29-9b5ddd857e13/sheet/61a0bd1d-cd6d-4ac8-8b55-80d8661e44c0/state/analysis](https://dashboard.tech.ec.europa.eu/qs_digit_dashboard_mt/public/sense/app/c140622a-87e0-412e-8b29-9b5ddd857e13/sheet/61a0bd1d-cd6d-4ac8-8b55-80d8661e44c0/state/analysis)

The dashboard runs on **Qlik Sense**, a business intelligence platform. It is powerful, but not easy to use if you have not used it before. Before you export data, apply your filters first. Qlik exports only the data visible on screen. Set your grant type and call year filters before you select the export button. For this workflow, filter by grant type (STG, COG, or ADG) and call years 2021–2024.

After you set the filters, use the export option (usually a download icon, or right-click on the data table) and export as **CSV or Excel**. The file will include: host institution, PI name, country, region, scientific domain (PE/LS/SH), funding amount, project start and end dates, project status, abstract, and CORDIS link.

Export one file for each grant type. Upload each file to its own tab in Google Sheets. This keeps the analysis clean and lets Claude handle each grant type independently.

Note on the PDFs: the call result PDFs the ERC releases for individual calls contain only a text list of awardees. These PDFs have limited fields and no structured data. The R&I database contains far more data. If you worked from PDFs before, this workflow will significantly expand what you can do.

## Connecting Claude to your data

If you have not set up the Google Sheets MCP connection, follow the [full setup guide here](/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/) first. After you connect it, Claude Desktop reads and writes directly to your spreadsheet. You do not need to copy and paste or upload CSV files.

Open Claude Desktop. Confirm the MCP connection is active. Share the spreadsheet URL or tab name in your prompt so Claude knows which data to work with.

## Prompting Claude to clean, analyse, and build the dashboard

This step saves the most time. Cleaning data, building pivot analysis, and creating charts can take hours in Excel or Sheets alone. Claude does all of this in a single session.

This prompt structure works well:

```
I've uploaded ERC Starting Grant data (2021–2024) to this Google Sheet: [URL or tab name].

Please:
1. Clean the data — remove duplicates, standardise institution names, handle blank fields
2. Analyse: top 10 host institutions by grant count, breakdown by country, breakdown by scientific domain (PE/LS/SH), average funding amount
3. Build an interactive HTML dashboard using Chart.js with filterable tables, a country breakdown chart, and an institution ranking chart

Output the dashboard as a self-contained HTML file.
```

Repeat this prompt for COG and ADG. Adjust the sheet reference each time. You can complete all three dashboards in one session.

The interactive element matters. A static chart gives you one fixed view. An interactive dashboard lets you filter by country, drill into specific institutions, and explore from multiple angles. This is where the real strategic value is.

## What the data shows

Across 822 grants in the 2021–2024 period, a few clear patterns emerge. **Germany dominates.** German institutions account for 151 Starting Grants, 98 Consolidator Grants, and 87 Advanced Grants, by a considerable margin. The Max Planck Society alone hosts 32 STG, 10 COG, and 13 ADG. This makes it the single most successful research organization across all three grant types. France (led by CNRS), the Netherlands, Sweden, and Switzerland follow. **CNRS leads in Synergy Grants**, and appears in 12 of the 77 projects in the 2022–2024 period. **Life Sciences dominates** across all grant types, and represents 37–57% of funded projects depending on the scheme.

These patterns are strategically useful. If you understand which institutions consistently win, which domains are over-represented, and how success concentrates geographically, you gain a meaningful edge before you write a single word of a proposal. This applies to applicants and to the advisors who support them.

## What you can do now

After you build the dashboards, you can benchmark your target host institution against national and European peers. You can identify whether your scientific domain is over-represented or under-represented in recent cohorts. You can track how the competitive landscape shifts across call years. The EC updates its R&I database each trimester, so you can repeat this workflow. Download a fresh export, run the same prompts, and refresh the dashboards.

The same approach works for any EC program with data on the R&I platform, including Horizon Europe projects, EIC funding, and MSCA grants. The data exists. The tools to work with it at scale now exist too.

---
## Related reading on The Science Talk

For broader context on why ERC funding patterns matter and how AI is changing grant strategy, see these related posts.

- [ERC Guidelines on AI in Grant Proposal Evaluation](https://thesciencetalk.com/services/grants-fundraising/erc-ai-grant-proposal-evaluation-guidelines/) — what the ERC's own guidance says about AI use in proposals
- [How I Used GenAI to Support €1M Grant Proposals](https://thesciencetalk.com/news/ai-tools-for-proposal-writing/) — practical application of Claude in a real proposal workflow
- [ERC Advanced Grant 2026 — What the data shows](https://thesciencetalk.com/services/grants-fundraising/erc-advanced-grant-2026/) — funded institutions, domains, and patterns for ADG applicants
- [ERC Starting Grant 2027 — Competitive landscape analysis](https://thesciencetalk.com/services/grants-fundraising/erc-starting-grant-2027/) — STG funding patterns and what they reveal for 2027 applicants
- [NotebookLM Data Tables: Relevance for Scientists and SciComm](https://thesciencetalk.com/news/notebooklm-data-tables-scicomm-scientists/) — how NotebookLM compares to Claude for structured data work

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
