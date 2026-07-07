---
title: "AI Content Intelligence Workflow: WordPress, GA4, Clarity, GitHub"
date: 2026-05-11
lastmod: 2026-05-11
draft: false
description: "I connect Clarity, two GA4 properties, and GSC into Claude via MCP across WordPress and GitHub Pages — no spreadsheets, no downloads. Here's what changed."
keywords: ["AI content intelligence workflow", "Microsoft Clarity Claude AI", "Google Analytics MCP", "WordPress analytics AI", "GitHub Pages content strategy", "content analytics synthesis", "GA4 Claude MCP"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["Microsoft Clarity", "Google Analytics", "MCP", "content strategy", "AI workflow", "Claude AI"]
category: "perspectives"
sidebar_links:
  - title: "How to Find Content Gaps Using Clarity and Google Search Console"
    url: "/ai-guides/content-gap-analysis-clarity-gsc/"
  - title: "Connect Google Analytics GA4 to Claude Desktop via MCP"
    url: "/ai-guides/connect-google-analytics-ga4-claude-desktop-mcp/"
  - title: "Turn AI Conversations Into Business Intelligence"
    url: "/ai-guides/ai-conversations-business-intelligence/"
  - title: "Build an AI-Powered Content Workflow for a Billion-Euro Industry"
    url: "/ai-guides/ai-content-workflow-billion-euro-industry/"
---

For a long time, my content review process looked like this: open Clarity, screenshot a few heatmaps, download a GA4 report, open Google Search Console in another tab, copy numbers into a spreadsheet, and then try to make sense of it all. By the time I had everything in one place, I was too tired to think clearly about what it meant.

I run two sites — [The Science Talk](https://thesciencetalk.com), a WordPress-hosted publication, and [pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com), a Hugo static site hosted on GitHub Pages — which means two GA4 properties, two sets of Clarity data, and two content strategies that need to inform each other. Building an AI content intelligence workflow that spans both environments changed how I make content decisions. This post is the honest account of what that looks like.

This post is not a setup guide. It is a case study in what changed when I stopped exporting data and started synthesising it.

---

## The fragmented data problem

The standard analytics stack is not missing data. It is missing synthesis.

Clarity shows you where users click, scroll, and abandon. GA4 shows you where traffic comes from, how long people stay, and which pages convert. Google Search Console shows you what queries are bringing people in and which pages are ranking without earning clicks. **Each tool answers a different question — and none of them talk to each other.**

When you manage one site, this is manageable. When you manage two, with different audiences, different hosting environments, and different content types, the manual reconciliation becomes a real tax on your time. I was spending more energy assembling the picture than interpreting it. The spreadsheet was full of numbers that were waiting for someone to care about them.

The decision I kept not making was: *which content is actually working, and what should I do next?*

---

## What this content intelligence workflow looks like

I now connect three data sources directly into Claude via MCP, without downloading anything:

- **Microsoft Clarity MCP** — behavioural data: scroll depth, click maps, dead clicks, session recordings across both sites
- **Two GA4 MCP connections** — one for thesciencetalk.com (WordPress), one for pranoti.thesciencetalk.com (Hugo on GitHub Pages) — traffic, engagement, source/medium, page-level performance
- **Google Search Console** — query data, impressions, click-through rates, ranking positions

All of this lives inside a single Claude session. I do not export. I do not open a spreadsheet. I ask Claude to pull the data, compare across sources, and surface patterns I should act on.

A typical session starts with something like: *"Look at the top 20 pages on TST by sessions this month. Cross-reference with Clarity scroll depth. Flag anything where GA shows strong traffic but Clarity shows users leaving before 50% scroll."*

Claude queries each MCP connection, combines the outputs, and returns a synthesised view — not a data dump, but a ranked list of posts worth investigating, with the specific signal that flagged each one.

The shift is significant. **The AI does the heavy lifting of combining and comparing. I spend my time on the part that requires judgement.**

---

## What it changed: three real decisions

**Decision 1: A post I was about to promote — that Clarity saved me from.**

GA4 showed a guide on TST with solid session numbers and a low bounce rate. I had planned to feature it in a newsletter. When I asked Claude to pull Clarity data for the same page, it flagged that the average scroll depth was 28%. Users were landing, skimming the introduction, and leaving. The low bounce rate was an artefact of how GA4 counts sessions, not a signal of genuine engagement. I rewrote the opening section before promoting the post.

**Decision 2: A content gap that only appeared across both sites.**

I asked Claude to compare the top GSC queries driving traffic to TST against the existing content index on the Pranoti site. It identified three query clusters — around MCP setup, Claude Desktop troubleshooting, and AI workflow for researchers — where TST was ranking but the Pranoti site had no corresponding guide. Those became my next three ai-guides posts. That pattern was invisible when I was looking at each site separately.

**Decision 3: A post I had written off — that deserved a second look.**

A case study on the Pranoti site had low traffic but unusually high scroll depth and a long average session time. In isolation, I had categorised it as low-performing. When Claude cross-referenced with GSC, it showed the page was ranking on page two for several high-intent queries. The post did not need to be replaced — it needed better internal linking and a title that matched search intent more precisely. One edit, not a rewrite.

None of these were discoveries I could not have made manually. But I would not have made them in the same session, on the same afternoon, without burning two hours on spreadsheet assembly first.

---

## What it still can't do

This workflow has real limitations and I want to be direct about them.

**Clarity's click data is noisy in ways Claude cannot resolve.** Clarity records all clicks — including dead clicks, where a user taps something that is not interactive. It cannot distinguish between a user clicking a text paragraph while reading (a common reading behaviour on mobile) and a user clicking because they expect something to happen and are frustrated when it does not. Claude receives this raw signal and can interpret engaged reading as interaction interest, or frustrated tapping as positive engagement. I have to apply judgement to any click-based conclusion Claude draws.

**Cross-site comparison has limits at the query level.** Claude can compare page-level performance across both the WordPress and GitHub-hosted sites, but GSC data is scoped per property. Identifying whether a query is cannibalising traffic between TST and the Pranoti site requires me to frame the question carefully — Claude does not infer this automatically.

**Claude synthesises patterns, not causes.** If a page has declining traffic, Claude will surface the decline and cross-reference with available signals. It will not tell me definitively why. That inference still requires me to read the page, check for technical issues, look at what changed in the publishing calendar, and make a judgement call.

**The workflow depends on stable MCP connections.** GA4 and Clarity MCP connections occasionally time out or return incomplete data, particularly for date ranges longer than 90 days. When the data is incomplete, Claude does not always flag it clearly — I have received confident-sounding summaries based on partial data pulls. I now explicitly ask Claude to confirm the date range and record count before interpreting any output.

---

## Is it worth building?

Yes — with one condition: you need to already understand what each data source is telling you individually before you ask AI to synthesise across them.

This workflow does not replace analytics literacy. It removes the manual assembly tax so that your analytical energy goes into decisions rather than data wrangling. If you do not know what scroll depth signals about content quality, Claude surfacing a low scroll depth number will not help you.

**For anyone managing two or more sites — whether WordPress, Hugo on GitHub Pages, or any other combination — the cross-property synthesis alone justifies the setup time.** Patterns that are invisible when you look at each property separately become actionable when an AI can hold both contexts at once.

The setup takes an afternoon — connecting the MCP servers, testing the queries, learning how to frame requests that return useful comparisons rather than data dumps. The return is that every subsequent content review session is faster, more complete, and more likely to produce a decision I actually act on.

---

If you want the technical setup rather than the practitioner reflection, the step-by-step guide is here: [How to Find Content Gaps Using Clarity and Google Search Console](/ai-guides/content-gap-analysis-clarity-gsc/).

## Related reading on The Science Talk

This post accompanies the [knowledge work automation overview on The Science Talk](https://thesciencetalk.com/news/knowledge-work-automation-european-research/) — which covers the broader pattern of how knowledge workers are restructuring research and content workflows using AI, with examples beyond content strategy.

---
*Browse all [Perspectives](/perspectives/) or [get in touch →](/contact/)*
