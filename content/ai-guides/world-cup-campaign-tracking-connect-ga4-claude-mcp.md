---
title: "World Cup Campaign Tracking: Connect GA4 to Claude via MCP"
date: 2026-06-20
lastmod: 2026-06-20
slug: "world-cup-campaign-tracking-connect-ga4-claude-mcp"
draft: false
description: "Connect GA4 to Claude via MCP and track World Cup campaign performance in plain English — ask a question, get your answer instantly. No manual exports."
keywords: ["connect GA4 to Claude via MCP", "GA4 MCP integration", "Google Analytics MCP server", "Claude GA4 dashboard", "real-time campaign tracking", "automate Google Analytics reporting", "World Cup campaign analytics"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["GA4", "MCP", "Google Analytics", "campaign tracking", "Claude Desktop"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "Connect Google Analytics GA4 to Claude Desktop via MCP"
    url: "/ai-guides/connect-google-analytics-ga4-claude-desktop-mcp/"
  - title: "AI Content Intelligence Workflow: WordPress, GA4, Clarity, GitHub"
    url: "/perspectives/ai-content-intelligence-workflow-wordpress-ga4-clarity-github/"
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
sidebar_product:
  label: "DIGITAL GUIDE"
  title: "Connect Claude Desktop to Google Sheets via MCP"
  bullets:
    - "Complete MCP setup with OAuth 2.0"
    - "Read, write, and edit Sheets from Claude"
    - "Ready-to-use reporting workflow templates"
  details:
    - "Instant PDF delivery"
    - "Email support included"
  stripe_url: "https://buy.stripe.com/9B614n7699puePn0jm8Ra0o?utm_source=pranoti_site&utm_medium=sidebar&utm_campaign=claude_sheets_mcp"
  cta: "Get the guide — €12 →"
  footnote: "Turn your live GA4 data into shareable reports"
---

When GA4 is connected to Claude via MCP, you can ask plain-English questions about your live campaign data and get answers instantly — no dashboard, no exports, no tab-switching. During the 2026 FIFA World Cup (11 June – 19 July), that speed matters: 48 teams, 104 matches, and audience attention shifting by the hour. This guide covers how to connect GA4 to Claude Desktop via MCP and which queries to run to stay on top of campaign performance throughout the tournament.

## Why Campaign Tracking Gets Harder When Everyone's Watching

Major live events compress the attention economy. During a World Cup match, organic search patterns shift, paid campaigns compete against higher CPMs, and landing page traffic can spike or collapse within minutes of a final whistle. You are not monitoring one campaign — you are watching several simultaneously while the audience's behaviour changes underneath them.

The standard workflow — log into GA4, build a report, export it, paste it into a document — takes too long when conditions are moving. By the time a manually assembled report lands in a chat or meeting, the data it describes has already changed.

The gap is not access to data. GA4 has everything you need. The gap is speed of interpretation, and that is exactly what connecting GA4 to Claude via MCP closes.

## What MCP Actually Does for GA4 and Claude

The Model Context Protocol (MCP) creates a direct, authenticated connection between Claude Desktop and the Google Analytics Data API. When you ask Claude a question, it calls your GA4 property directly and returns the answer in your conversation — no intermediary, no third-party service, no export required.

Your analytics data goes from Google's API to Claude on your machine. Nothing is stored externally or passed through another platform.

The practical effect is that GA4 stops being a dashboard you visit and becomes a data source you talk to. Instead of building a custom report to answer "which channel drove the most sessions yesterday", you type that question and get the answer in seconds.

> **Scope note:** This approach requires Claude Desktop (not claude.ai in a browser). The MCP server runs locally on your Mac and authenticates directly with your Google account.

## Step-by-Step: Connecting GA4 to Claude via MCP

If you have already completed the [Connect Google Analytics GA4 to Claude Desktop via MCP](/ai-guides/connect-google-analytics-ga4-claude-desktop-mcp/) guide, your connection is live — skip to the next section.

If you are starting from scratch, the full setup is covered in that guide. Here is a summary of what it involves:

**What you need:**
- Claude Desktop (Mac) — download from [claude.ai/download](https://claude.ai/download)
- Python 3.10 or higher
- Homebrew and pipx
- Google Cloud CLI (`gcloud`)
- A Google Cloud project with the **Google Analytics Admin API** and **Google Analytics Data API** enabled
- A Google account with Viewer access (minimum) to your GA4 property

**The configuration block** you add to `claude_desktop_config.json` (via Claude Desktop → Settings → Developer → Edit Config):

```json
{
  "mcpServers": {
    "analytics-mcp": {
      "command": "pipx",
      "args": ["run", "analytics-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/Users/your-username/.config/gcloud/application_default_credentials.json",
        "GOOGLE_PROJECT_ID": "your-cloud-project-id"
      }
    }
  }
}
```

After saving and restarting Claude Desktop, confirm the connection by typing:

```
What Google Analytics properties do I have access to?
```

Claude will list your GA4 accounts and properties. Once your property name appears, you are ready to query.

> Full authentication steps, API enablement, and troubleshooting are in the [complete setup guide](/ai-guides/connect-google-analytics-ga4-claude-desktop-mcp/).

## What You Can Ask Claude Once It's Connected

This is where the World Cup advantage becomes concrete. The queries below are designed for live-event campaign tracking — periods when you need fast answers across multiple dimensions without building a new report each time.

**Check overall campaign performance since the tournament started:**

```
Show me sessions, conversions, and bounce rate for the past 10 days,
broken down by campaign.
```

**Spot match-day traffic spikes:**

```
Show me hourly sessions for 14 June and 18 June.
Which hours had the highest traffic on each day?
```

Use the match schedule to interpret the data — peaks during or immediately after a match often indicate branded search or direct campaign response.

**Compare channels during the tournament:**

```
Break down my sessions and conversion rate by traffic source
for 11 June to today. Which channel is performing best?
```

**Identify your highest-performing World Cup landing page:**

```
Which pages on my site have had the most sessions in the past 14 days?
Show engagement rate alongside session count.
```

**Check paid vs organic split:**

```
Compare organic search sessions to paid search sessions
for the past 7 days. How has that ratio changed week on week?
```

**Monitor a specific campaign tag:**

```
Show me sessions and conversions where the utm_campaign contains "worldcup".
Break it down by day.
```

**Catch a drop before it becomes a problem:**

```
Are any of my top 5 campaigns showing a session drop of more than 20%
compared to the previous 7 days?
```

None of these require you to leave Claude, build a custom report, or wait for a scheduled export. The answer comes back in the conversation, in plain English, alongside any follow-up questions you want to ask.

> When Claude asks which property to use, paste your **GA4 Property ID** — a numeric ID found in GA4 under **Admin → Property Settings** (format: `123456789`).

## From Real-Time GA4 Insight to a Full Reporting Workflow

Querying data in Claude is fast, but the output lives inside your conversation. When you need to share performance results with a client, a team, or a stakeholder who is not in Claude, you need a format that travels.

The natural next step is connecting Claude Desktop to Google Sheets via MCP. With both connections active in the same Claude conversation, you can pull live campaign data from GA4 and write it directly into a Sheets report — without leaving Claude or copying anything manually.

That setup is covered in the [Connect Claude Desktop to Google Sheets via MCP guide](/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/), which includes the full authentication flow, configuration, and ready-to-use workflow templates.

If you are already querying your World Cup campaigns in Claude, adding the Sheets MCP turns those queries into a shareable, updatable report in one extra step.

---

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
