---
title: "How to Build an EU AI Act AI System Register (Free Template)"
date: 2026-07-17
lastmod: 2026-08-02
slug: "eu-ai-act-ai-system-register-template"
draft: false
featured_image: "/images/ai-guides_perspectives/eu-ai-act.webp"
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

Most small teams cannot answer a simple question. Which AI tools do we actually use, and who is responsible for each one? This guide builds an **AI system register**. It is a tracking sheet you can create in a spreadsheet, Notion, or Airtable. It ends with a short self-test for whether you owe an official EU database filing under Article 71 of the EU AI Act.

## What you need before starting

- A spreadsheet, Notion database, or Airtable base — any tool with rows and columns works
- About 30 minutes of uninterrupted time
- A rough list of every department or team using AI tools, so you can ask them directly

> This guide covers the internal register only. It does not explain how to file an Article 71 EU database entry. Very few readers of this guide need that yet. The self-test below explains why.

## Step 1: Find every AI tool you use

Most organizations underestimate their AI footprint because "shadow AI" hides in places nobody audits. Check these four sources before you assume your list is complete.

- **SaaS subscriptions** — search your existing vendor list for "AI" or "machine learning" in the product description
- **Plugins and extensions** — individuals, not IT, often add Microsoft Copilot in Office, Gemini in Google Workspace, and coding assistants like GitHub Copilot
- **AI embedded in existing tools** — CRM, HR, accounting, and marketing platforms increasingly ship AI features as default add-ons, sometimes switched on silently
- **Internal scripts and automations** — anything your team built that calls an AI API, even a small one

Ask every team lead directly: "What AI tools do you or your tools use?" A written list rarely matches what people click on day to day.

## Step 2: Decide provider vs. deployer for each tool

Every AI system on your list falls into one of two roles under the EU AI Act. The role changes what obligations apply to you.

- **Deployer** — you use the tool as sold, without modifying it. This covers most SaaS AI tools that teams use.
- **Provider** — you built it, substantially modified it, or rebrand it under your own name. Under **Article 25**, a deployer becomes a provider if it fine-tunes a model or relabels a tool as its own product.

If you are unsure whether a tool you white-label or customize tips you into "provider" territory, read the [GPAI Code of Practice: Provider vs. Deployer guide](/ai-guides/gpai-code-of-practice-provider-vs-deployer/). It covers the test in more depth.

## Step 3: Flag high-risk candidates

Most marketing, content, and general productivity tools do not qualify as high-risk. Run a quick check against the systems most likely to trigger [**Annex III**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3), mainly tools used for:

- HR or recruitment decisions (screening, ranking candidates)
- Credit scoring or financial risk assessment
- Biometric identification

> The 2026 Omnibus amendments deferred most stand-alone Annex III obligations to **2 December 2027** (2 August 2028 for AI embedded in already-regulated products). Transparency requirements under Article 50 stayed on the original 2 August 2026 timeline. Flag high-risk candidates now for awareness. Do not treat this as urgent compliance work yet.

## Step 4: Build your AI system register

Copy this table into your spreadsheet, Notion database, or Airtable base. Use one row per tool.

| Tool | Owner | Vendor | Provider or Deployer | High-risk flag (Y/N/Unsure) | Evidence/notes | Last reviewed |
|------|-------|--------|----------------------|------------------------------|-----------------|----------------|
| Example: Copilot for M365 | IT lead | Microsoft | Deployer | N | Standard productivity use, no rebranding | 2026-07-16 |

Fill in one row for every tool found in Step 1. Leave "Unsure" in the high-risk column rather than guessing. This flags the row for a closer look later, without it blocking the rest of the register.

## Do you need to register with the EU?

Run this self-test before you assume you need to do anything further.

[**Article 71**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-71) requires providers of high-risk Annex III systems to register themselves and the system in the official EU database before they place it on the market. Article 71 applies from **2 August 2026**. **Article 49** sets out the registration mechanism itself.

You are very likely exempt from this right now if any of the following is true:

- You are a **deployer**, not a provider, of every tool on your register
- None of your tools were flagged as high-risk in Step 3
- Your organization has not rebranded, fine-tuned, or substantially modified a third-party AI system

There is no general SME exemption from Article 71 itself. But [**Article 62**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-62) provides supportive measures for smaller organizations that do end up in scope, such as reduced conformity-assessment fees and priority access to regulatory sandboxes. Simplified technical documentation sits separately, in Article 11(1), which lets SMEs, start-ups, and small mid-caps file the Annex IV elements on a simplified Commission form.

## Keep it alive

A register that is accurate once and never updated stops being useful within a quarter. Set a recurring calendar reminder to review it every three months. Add a line the moment anyone adopts a new AI tool. If you wait for the next scheduled review, shadow AI can creep back in.

## What you can do now

You now have full visibility into your organization's AI footprint, tracked in one place instead of scattered across memory and Slack threads. Based on the self-test above, you can also state with confidence whether an EU database filing applies to you. For most SMEs and agencies, it does not, yet.

Revisit the register every quarter. Treat the Article 71 self-test as a five-minute check each time rather than a one-off decision.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
