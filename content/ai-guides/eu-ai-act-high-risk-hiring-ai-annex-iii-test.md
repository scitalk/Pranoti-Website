---
title: "EU AI Act High-Risk Hiring AI: The Annex III Test"
date: 2026-07-18
lastmod: 2026-07-18
slug: "eu-ai-act-high-risk-hiring-ai-annex-iii-test"
draft: false
featured_image: "/images/ai-guides/eu-ai-act.webp"
description: "Run this 3-step EU AI Act test to check if your recruitment or HR software counts as high-risk hiring AI under Annex III, before 2 December 2027."
keywords: ["EU AI Act high-risk hiring AI", "Annex III employment", "AI Act recruitment compliance", "high-risk AI recruitment tool test", "Article 6 AI Act classification", "AI Act HR compliance small agency", "AI hiring tool compliance 2027"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["EU AI Act", "Annex III", "AI hiring", "HR compliance", "high-risk AI"]
category: "ai-integration-guides"
pillar: "EU AI Act & Compliance"
sidebar_links:
  - title: "How to Build an AI System Register"
    url: "/ai-guides/eu-ai-act-ai-system-register-template/"
  - title: "GPAI Code of Practice: Provider vs Deployer"
    url: "/ai-guides/gpai-code-of-practice-provider-vs-deployer/"
  - title: "EU AI Act Deadlines 2026–2028 Timeline"
    url: "/ai-guides/eu-ai-act-deadlines-2026-2028-timeline/"
---

Recruitment and HR tools are the single most common place agencies and small teams run into **EU AI Act high-risk hiring AI** status. **Annex III** of [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) names employment AI directly, and the classification test is more mechanical than it looks once you know the three questions to ask. This guide walks through the actual 3-step test, using only the AI Act's own text.

## What you need before starting

- A list of every AI tool that touches recruitment, hiring, or staff management
- For each tool: whether you built it, customised it, or use it off-the-shelf
- Basic clarity on whether you are the **provider** or **deployer** of each tool

> If you're unsure of the provider/deployer distinction, read the [GPAI Code of Practice: provider vs deployer guide](/ai-guides/gpai-code-of-practice-provider-vs-deployer/) first — the Annex III test below assumes you already know which role you hold.

## The Annex III employment test

[**Annex III, Category 4**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3) of the AI Act covers two groups of AI systems used in employment. Both are named explicitly, so there is no need to guess whether your tool "counts."

**4(a) — Recruitment and selection:** systems used "to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates."

**4(b) — Work management:** systems used to determine "the terms of work-related relationships, the promotion or termination of work-related contractual relationships, to allocate tasks based on individual behaviour or personal traits or characteristics or to monitor and evaluate the performance and behaviour" of staff.

If your tool does any of the above, it sits inside Category 4 by default. [**Article 6(2)**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6) of the AI Act states plainly: "AI systems referred to in Annex III shall be considered to be high-risk."

## Step 1: Check if your tool matches 4(a) or 4(b)

Go through your tool list from the prerequisites and sort each one.

**Likely 4(a) — recruitment:**
- CV screening or keyword-matching software
- AI that ranks or scores job applicants
- Targeted job-ad placement tools using candidate profiling

**Likely 4(b) — work management:**
- Performance-monitoring dashboards with AI scoring
- AI-driven task allocation or shift scheduling based on staff behaviour
- Tools that flag staff for promotion, warning, or termination review

**Usually outside Category 4:**
- Generic writing tools used to draft a job advert (no candidate analysis)
- General-purpose chat assistants used for internal admin, not decisions

> A tool can fall into Category 4 even if a human makes the final call. The Act classifies based on the AI system's function, not on whether a person reviews the output afterwards.

**Worked example:** A three-person hiring agency uses an applicant-tracking system with a built-in "smart match" score that ranks candidates against a job description. Even though a recruiter still picks who gets interviewed, the scoring function itself falls under 4(a) — the Act looks at what the AI does, not what the human does afterwards.

## Step 2: Run the Article 6(3) exemption test

[**Article 6(3)**](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6) allows a Category 4 system to be treated as *not* high-risk if it meets one of four narrow conditions:

1. It performs a narrow procedural task
2. It improves the result of a previously completed human activity
3. It detects decision-making patterns without replacing or influencing human assessment
4. It performs a preparatory task before a human-led assessment

Most recruitment and HR tools fail all four. A CV-ranking tool that scores and orders candidates is not "narrow procedural" — it shapes the outcome. A performance-monitoring tool that flags staff for review is not "preparatory" in the Act's sense, because its output directly feeds a decision.

> Document your reasoning either way. **Article 6(4)** requires providers claiming an exemption to record that assessment *before* placing the system on the market, and to register it accordingly.

**Worked example:** A tool that only spell-checks and reformats CVs before a recruiter reads them could plausibly qualify as a "narrow procedural task" (condition 1) — it doesn't rank, filter, or evaluate anyone. A tool that scores candidates against a job description and orders them by fit does not qualify under any of the four conditions.

## Step 3: Check the profiling override

Even if a tool clears Step 2, Article 6(3) contains a hard override: systems that perform **profiling of natural persons** "shall always be considered to be high-risk," with no exemption available.

Most candidate-scoring and behaviour-monitoring tools profile by default — they build a picture of a person from data points to predict or evaluate them. If your tool ranks candidates by fit score, flags "flight risk" employees, or predicts performance from behavioural data, it profiles. The exemption test in Step 2 does not apply once profiling is present.

**Worked example:** A performance-monitoring tool that combines login times, task completion rates, and message tone to produce an "engagement risk" score for each employee is profiling — it builds a predictive picture of a specific person from multiple data points. That score being visible only to a manager doesn't change the classification.

## Step 4: Know what happens if you land in high-risk

If your tool sits in Category 4 with no valid exemption, it is high-risk under the Act. The core obligations — risk management, technical documentation, human oversight, and registration — are real, but they are not this guide's focus.

Two practical points for now:

- **Registration** happens under **Article 49(2)**, in the EU database for high-risk systems.
- **Timing has moved.** Following the Digital Omnibus package, obligations for stand-alone Annex III high-risk systems (which includes employment AI) now apply from **2 December 2027**, not the earlier August 2026 date some sources still quote.

> Use this window. A tool classified as high-risk today doesn't need full compliance today — but the documentation trail (Steps 1–3 above) is worth building now, while the reasoning is fresh. Start with the [AI system register template](/ai-guides/eu-ai-act-ai-system-register-template/) to log each tool's classification.

## Troubleshooting

**"We just use a chatbot to draft job ads."**
If the tool only generates text and doesn't analyse, filter, or score candidates, it's unlikely to fall inside Category 4(a). Re-check if you later add a screening or ranking feature.

**"Our ATS has an AI ranking feature we've never switched on."**
Classification depends on function available for use, not just active use in your workflow. If the feature exists and could screen or rank candidates, treat it as in scope and document the decision either way.

**"We're a sub-processor, not the tool builder."**
You may still be a **deployer** under the Act even without building the tool. Deployer obligations are lighter than provider obligations, but registration and oversight duties still apply to high-risk systems you put into use.

## What you can do now

Every recruitment and HR AI tool on your list can now be sorted into one of three states: **high-risk with no exemption**, **exempt with documented reasoning**, or **outside Category 4 entirely**. That classification is the foundation for everything else the Act requires.

Two immediate next steps:

- Log each tool's classification in your [AI system register](/ai-guides/eu-ai-act-ai-system-register-template/), including which Article 6(3) exemption (if any) applies
- Check the [EU AI Act deadlines timeline](/ai-guides/eu-ai-act-deadlines-2026-2028-timeline/) to confirm the December 2027 date against any tool-specific timelines

## FAQ: EU AI Act and hiring AI

### Is an ATS ranking or scoring feature high-risk under the EU AI Act?
Yes, if it analyses, filters, or evaluates candidates. Annex III Category 4(a) covers this directly, and the Article 6(3) exemptions rarely apply to a scoring or ranking function.

### Does the EU AI Act apply if a human still makes the final hiring decision?
Yes. Classification depends on what the AI system does, not on whether a human reviews or overrides its output afterwards.

### When do high-risk obligations for hiring AI actually take effect?
**2 December 2027** for stand-alone Annex III systems, following the Digital Omnibus package's revised timeline. Systems embedded in regulated products follow a later date, 2 August 2028.

### Is a general-purpose AI assistant used to draft job ads high-risk?
Usually not, if it only generates text and doesn't analyse, filter, or score candidates. It becomes in scope the moment a screening or ranking feature is added or switched on.

### Can a small agency be a deployer without building the AI tool itself?
Yes. Buying or licensing a third-party recruitment tool makes you a deployer, not a provider, but deployer obligations — including registration duties for high-risk systems — still apply.

## Related reading on The Science Talk

This guide accompanies the [EU AI Act Article 4 post on The Science Talk](https://thesciencetalk.com/news/eu-ai-act-article-4-ai-literacy-research-institutes/) — background on the AI literacy duty that applies to anyone using these tools, including HR staff and recruiters.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
