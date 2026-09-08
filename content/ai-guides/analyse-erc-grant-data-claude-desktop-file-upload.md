---
title: "How to Analyse the Full ERC Grant Dataset in Claude Desktop"
date: 2026-08-26
lastmod: 2026-08-26
draft: true
description: "Export ten years of ERC award data from the European Commission's R&I dashboard and analyse all 11,953 grants in a single Claude Desktop session, with no BI tool and no spreadsheet limits."
keywords: ["ERC grant data analysis", "Claude Desktop file upload", "ERC funded institutions", "Horizon Europe data analysis", "EC R&I dashboard export", "CORDIS data", "ERC grant strategy", "xlsx analysis Claude"]
author: "Pranoti Kshirsagar"
reading_time: "8 min"
tags: ["ERC", "Claude AI", "data analysis", "grant strategy", "Horizon Europe"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "How to Analyse ERC Grant Data Using Claude AI and Google Sheets"
    url: "/ai-guides/erc-grant-data-analysis-funded-institutions/"
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
sidebar_product:
  label: "RESOURCE KIT"
  title: "ERC Starting Grant 2027 — 47 Official Resources"
  bullets:
    - "47 verified official resources for your ERC StG 2027 application"
    - "Organised into 11 sections"
    - "Compiled by The Science Talk"
  details:
    - "Instant access"
  stripe_url: "/products/erc-starting-grant-resource-kit/"
  cta: "Get the resource kit →"
  footnote: ""
---

I have written before about [analysing ERC data with Claude and a Google Sheets connection](/ai-guides/erc-grant-data-analysis-funded-institutions/). That method works well for a few hundred grants. It stops being the right tool at a few thousand.

This guide covers the bigger version. One export, 11,953 ERC grants, ten call years, five grant types, €21.49bn of funding, analysed in a single Claude Desktop session. No BI tool, no spreadsheet, no separate pipeline per grant type.

## Why the full dataset is worth the trouble

Most people filter ERC data down to the grant they are applying for. That is a mistake. A Starting Grant applicant who only looks at Starting Grants cannot see that their target institution is strong in Consolidator and weak in Starting, or that a panel is crowded at one career stage and open at another. The schemes are a system. Reading one of them alone throws away most of the signal.

The full export also lets you check your own assumptions against ten years instead of three, which matters when two of those years turn out to be structurally odd.

## Step 1: Export from the EC R&I dashboard

Start at the ERC's [projects and statistics page](https://erc.europa.eu/projects-statistics/erc-dashboard). It links through to the European Commission's R&I Dashboard, which is the actual structured database:

[https://dashboard.tech.ec.europa.eu/qs_digit_dashboard_mt/public/sense/app/c140622a-87e0-412e-8b29-9b5ddd857e13/sheet/61a0bd1d-cd6d-4ac8-8b55-80d8661e44c0/state/analysis](https://dashboard.tech.ec.europa.eu/qs_digit_dashboard_mt/public/sense/app/c140622a-87e0-412e-8b29-9b5ddd857e13/sheet/61a0bd1d-cd6d-4ac8-8b55-80d8661e44c0/state/analysis)

The dashboard runs on Qlik Sense. It exports only what is on screen, so filters have to go on before you export, not after.

**Set the call year filter and nothing else.** This is the important instruction, and it is the opposite of what the interface encourages. If you skip the grant type filter, the export returns Starting, Consolidator, Advanced, Synergy and Proof of Concept grants together in one file. That is the file you want.

The result for call years 2016 to 2025 is an xlsx of roughly 9MB, 11,953 rows and 18 columns:

| Column group | Fields |
|---|---|
| Identity | Programme, Acronym, Project Title, Project Number |
| People and place | Researcher(s), Host Institution(s), Country, Region |
| Classification | Call, Grant Type, Domain, Panel, Call Year |
| Money and time | EU contribution, Start Date, End Date |
| Detail | Abstract, CORDIS Link |

The abstracts are the reason the file is large. They are also the reason it is worth keeping, since they let you ask questions about topic and framing, not just counts.

## Step 2: Turn on code execution

Claude reads xlsx files by running code against them, not by reading them as text. That capability is off by default.

Go to Claude settings and **enable code execution and file creation**. Without it, spreadsheet uploads either fail or get mangled into unusable text. This one setting is the difference between the method working and appearing to be impossible.

Per [Anthropic's own documentation](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai), the chat upload limit is 500MB per file and 20 files per chat, and Project files are capped at 30MB each. A 9MB ERC export sits comfortably inside both.

## Step 3: Upload and orient before you analyse

Drop the xlsx straight into a Claude Desktop conversation. Then resist the urge to ask your real question immediately.

Ask for a profile first:

> Load this file and give me a structural profile: row count, every column, and the distinct values with counts for Programme, Grant Type, Call Year and Domain. Also give me the total EU contribution, and flag any blank or zero values.

This takes one turn and saves you from every mistake in the next section. In my case it immediately surfaced that the file held all five grant types, that call years ran 2016 to 2025, and that 46 rows carry no funding figure.

## Step 4: Know which holes are real

Three things in this dataset look like broken data and are not. If you skip this step you will publish something wrong.

**Missing grant types in specific years.** Call year 2025 contains no Advanced Grants, because that call's results were not published when the export was taken. Call year 2021 contains no Proof of Concept. Any year-on-year total that includes those years will slope the wrong way for reasons that have nothing to do with research funding.

**Countries that drop to zero.** The United Kingdom records 0 or 1 core grants for call years 2021, 2022 and 2023, then 200 in 2024. Switzerland records almost nothing from 2021 to 2024, then 62 in 2025. Both match the Commission's published association dates exactly, which I cover in the [companion piece on what the gaps mean](/perspectives/erc-data-uk-switzerland-association-gap/).

**Packed institution fields.** Host institutions arrive as `University of Groningen [999989782,NL]`, and Synergy Grant rows list several hosts in one cell. Counting the raw strings gives you nonsense. Tell Claude to extract the name before the bracket, and decide explicitly whether a co-hosted Synergy grant counts once per host or splits its funding between them. There is no correct answer, but there is a wrong one, which is not choosing.

A prompt that handles all three:

> Before analysing: extract clean institution names by stripping the [ID,CC] suffix, and treat multi-host rows as one entry per host. Then tell me which call year and grant type combinations are missing entirely, and which countries have three or more consecutive years at zero.

## Step 5: Ask the questions that need the whole file

Now the analysis. These are the prompts that repay having all ten years and all five schemes in one place:

> Rank host institutions by grant count and separately by total EU contribution, for all grants and then broken down by grant type. Show where the two rankings disagree.

> For each grant type, give me mean and median EU contribution. Compare the median against the published scheme ceiling.

> Compare each country's share of Starting, Consolidator and Advanced Grants in 2016-2018 against 2023-2025, in percentage points. Exclude call year 2025 from the Advanced Grant comparison and tell me you have done so.

That last prompt is the pattern to internalise. State the known gap inside the prompt, and ask Claude to confirm it handled it. It is much harder to get a quietly wrong answer that way.

For a topic layer, the abstracts are sitting right there:

> Using the Abstract column, identify the ten most common research themes within panel PE6 across 2023-2025, and tell me which are growing.

## Step 6: Verify before you use it

Every row carries a CORDIS link. Pick five results at random from any ranking Claude produces and open them. Check the institution, the amount and the call year against the CORDIS record. This takes four minutes and is the only reason to trust the other 11,948 rows.

The EC updates the R&I database each trimester, so the whole workflow is repeatable. Re-export, re-upload, re-run the same prompts.

## What this replaces

| | Sheets MCP method | Full-file upload |
|---|---|---|
| Practical size | Hundreds of rows | Low tens of thousands |
| Grant types per pass | One | All five |
| Abstracts usable | No | Yes |
| Setup | MCP server, OAuth | One settings toggle |
| Best for | Focused, repeated slices | The whole landscape |

The Sheets method is still the better choice when you want a live, shared, filterable sheet that colleagues can open. The upload method is better when you want to understand the whole picture once.

## Related reading

- [How to Analyse ERC Grant Data Using Claude AI and Google Sheets](/ai-guides/erc-grant-data-analysis-funded-institutions/) — the smaller-scale version of this workflow
- [What Ten Years of ERC Data Shows About European Research Funding](/perspectives/erc-data-uk-switzerland-association-gap/) — the findings from this dataset
- [ERC Guidelines on AI in Grant Proposal Evaluation](https://thesciencetalk.com/services/grants-fundraising/erc-ai-grant-proposal-evaluation-guidelines/) — what the ERC's own guidance says about AI use in proposals

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
