---
title: "How to Build an EU AI Act AI System Register (Free Template)"
date: 2026-07-17
lastmod: 2026-07-17
slug: "eu-ai-act-ai-system-register-template"
draft: false
featured_image: "/images/ai-guides/eu-ai-act.webp"
description: "Build an EU AI Act system register in 30 minutes, and find out whether you owe an official Article 71 EU database filing — free spreadsheet template included."
keywords: ["AI system register EU AI Act", "AI inventory template SME", "Article 71 EU AI database", "shadow AI inventory", "provider vs deployer register", "EU AI Act compliance template", "AI Act Article 49 registration"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["EU AI Act", "AI governance", "AI Act compliance", "SME", "AI inventory"]
category: "ai-integration-guides"
pillar: "EU AI Act & Compliance"
sidebar_links:
  - title: "GPAI Code of Practice: Provider vs. Deployer, Explained"
    url: "/ai-guides/gpai-code-of-practice-provider-vs-deployer/"
  - title: "EU AI Act Deadlines 2026–2028: The Current Timeline"
    url: "/ai-guides/eu-ai-act-deadlines-2026-2028-timeline/"
  - title: "EU AI Act Article 4: What Creator Agencies and Small Teams Owe"
    url: "/perspectives/eu-ai-act-article-4-creator-agencies-small-teams/"
---

Most small teams cannot answer a simple question: which AI tools are we actually using, and who is responsible for each one? This guide builds an **AI system register** — a tool-agnostic tracking sheet you can set up in a spreadsheet, Notion, or Airtable. It closes with a short self-test for whether you owe an official EU database filing under Article 71 of the EU AI Act.

## What you need before starting

- A spreadsheet, Notion database, or Airtable base — any tool with rows and columns works
- About 30 minutes of uninterrupted time
- A rough list of every department or team using AI tools, so you can ask them directly

> This guide covers the internal register only. It does not walk through the mechanics of filing an Article 71 EU database entry — very few readers of this guide will need that yet, for reasons covered in the self-test below.

## Step 1: Find every AI tool you're actually using

Most organisations underestimate their AI footprint because "shadow AI" hides in places nobody audits. Check these four sources before assuming your list is complete.

- **SaaS subscriptions** — search your existing vendor list for "AI" or "machine learning" in the product description
- **Plugins and extensions** — Microsoft Copilot in Office, Gemini in Google Workspace, and coding assistants like GitHub Copilot often get added by individuals, not IT
- **AI embedded in existing tools** — CRM, HR, accounting, and marketing platforms increasingly ship AI features as default add-ons, sometimes switched on silently
- **Internal scripts and automations** — anything your team built that calls an AI API, even a small one

Ask every team lead directly: "what AI tools do you or your tools use?" A written list rarely matches what people actually click on day to day.

## Step 2: Decide provider vs. deployer for each tool

Every AI system on your list falls into one of two roles under the EU AI Act, and the distinction changes what obligations apply to you.

- **Deployer** — you use the tool as sold, without modifying it. This covers the vast majority of SaaS AI tools most teams use.
- **Provider** — you built it, substantially modified it, or rebrand it under your own name. Under **Article 25**, a deployer can become a provider if they fine-tune a model or relabel a tool as their own product.

If you are unsure whether a tool you white-label or customise tips you into "provider" territory, the [GPAI Code of Practice: Provider vs. Deployer guide](/ai-guides/gpai-code-of-practice-provider-vs-deployer/) walks through the test in more depth.

## Step 3: Flag high-risk candidates

Most marketing, content, and general productivity tools will not qualify as high-risk. Run a quick check against the systems most likely to trigger [**Annex III**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3) — mainly tools used for:

- HR or recruitment decisions (screening, ranking candidates)
- Credit scoring or financial risk assessment
- Biometric identification

> Most stand-alone Annex III obligations were deferred to **2 December 2027** under the 2026 Omnibus amendments (2 August 2028 for AI embedded in already-regulated products). Transparency requirements under Article 50 stayed on the original 2 August 2026 timeline. Flag high-risk candidates now for awareness — there is no need to treat this as urgent compliance work yet.

## Step 4: Build your AI system register

Copy this table into your spreadsheet, Notion database, or Airtable base. One row per tool.

| Tool | Owner | Vendor | Provider or Deployer | High-risk flag (Y/N/Unsure) | Evidence/notes | Last reviewed |
|------|-------|--------|----------------------|------------------------------|-----------------|----------------|
| Example: Copilot for M365 | IT lead | Microsoft | Deployer | N | Standard productivity use, no rebranding | 2026-07-16 |

Fill in one row for every tool found in Step 1. Leave "Unsure" in the high-risk column rather than guessing — it flags the row for a closer look later, without blocking the rest of the register.

## Do you need to register with the EU?

Run this self-test before assuming you need to do anything further.

[**Article 71**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-71) requires providers of high-risk Annex III systems to register themselves and the system in the official EU database before placing it on the market. The database must be operational by **2 August 2026**, and the mechanism itself is set out in **Article 49**.

You are very likely exempt from this right now if any of the following is true:

- You are a **deployer**, not a provider, of every tool on your register
- None of your tools flagged as high-risk in Step 3
- Your organisation has not rebranded, fine-tuned, or substantially modified a third-party AI system

There is no general SME exemption from Article 71 itself, but [**Article 62**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-62) provides supportive measures for smaller organisations that do end up in scope — reduced conformity-assessment fees, simplified technical documentation, and priority access to regulatory sandboxes.

## Keep it alive

A register that is accurate once and never updated stops being useful within a quarter. Set a recurring calendar reminder to review it every three months, and add a line the moment anyone adopts a new AI tool — waiting for the next scheduled review lets shadow AI creep back in.

## What you can do now

You now have full visibility into your organisation's AI footprint, tracked in one place instead of scattered across memory and Slack threads. Based on the self-test above, you can also state with confidence whether an EU database filing applies to you — for the great majority of SMEs and agencies, it does not, yet.

Revisit the register every quarter, and treat the Article 71 self-test as a five-minute check each time rather than a one-off decision.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
