---
title: "Claude Code Context Window: What Each Category Means and How to Manage It"
date: 2026-04-19
lastmod: 2026-04-19
draft: false
description: "Learn what each category in Claude Code's context window breakdown means and how to use it to manage long sessions effectively."
keywords: ["Claude Code context window", "context window breakdown", "MCP tools deferred", "Claude Desktop token management", "context window categories", "Claude Code session management", "token budget optimisation"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["Claude Code", "Claude Desktop", "context management", "MCP tools", "token optimisation"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com and MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
  - title: "Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
sidebar_product:
  label: "DIGITAL GUIDE"
  title: "Claude + Google Sheets via MCP"
  bullets:
    - "Connect Claude Desktop to Google Sheets in under 30 minutes"
    - "Read, write, and update sheets with plain-language prompts"
    - "Automate reporting and data tasks without formulas"
  details:
    - "Step-by-step setup guide, no coding required"
    - "Works with Claude Desktop on Mac and Windows"
  stripe_url: "https://buy.stripe.com/9B614n7699puePn0jm8Ra0o?utm_source=pranoti_site&utm_medium=sidebar&utm_campaign=claude_sheets_mcp"
  cta: "Get the guide — €12 →"
  footnote: "Instant PDF delivery. Lifetime access."
---

Claude Desktop now shows a live context window breakdown in the session interface. You do not need a terminal command to see it. You can see how full your context window is, which categories use the most tokens, and how much free space remains. This guide explains what each category in the breakdown means. It also explains what to do when the numbers start to climb.

This post describes the breakdown panel. It covers what triggers the panel, how to read each row, and four actions you can do during a long session to extend your working budget.

## What is the context window?

The context window is Claude's working memory for a session. Every message you type, every response Claude generates, every file you read, and every tool you call takes space in a fixed budget measured in tokens. One token is about four characters of English text. A single research paper or grant document can use tens of thousands of tokens. A long afternoon session uses tokens even faster.

The standard Claude Code context window has 200,000 tokens. This sounds like a large amount, but it fills fast when you combine conversation history, loaded tools, custom instructions, and document contents. When the window nears capacity, Claude starts to compress earlier parts of the conversation. At this point, response quality starts to drop.

## How to access the breakdown

In an active Claude Code session in Claude Desktop, find the context window indicator at the top of the session. It shows your current usage as a fraction and a percentage, for example **161.3k / 200.0k (81%)**. Click it to open the full breakdown panel. The panel shows a token count for each category.

You can also run the `/context` command in the terminal. This shows a similar breakdown with more optimization suggestions.

## How to read the breakdown: what each category means

The example below shows a breakdown mid-session, at 161,300 tokens used out of a 200,000-token window (81% full). Each category below matches a row in the panel.

![Claude Code context window breakdown panel showing token usage by category](https://thesciencetalk.com/wp-content/uploads/2026/04/Screenshot-2026-04-15-at-13.15.10-1024x812.png)

### Messages — conversation history

**What it is:** Everything you typed and everything Claude replied. This is the full conversation history.

**Why it matters:** This is almost always the largest category. It also grows the fastest during a long session. You cannot reduce what is already there. You can stop it from growing further if you run `/compact` before the window fills.

**Typical percentage:** 60–80% in extended sessions.

### System prompt — core operating instructions

**What it is:** Claude Code's core operating instructions. The system loads these automatically at the start of every session.

**Why it matters:** This overhead is fixed. You cannot reduce it. It defines how Claude behaves, what tools Claude can use, and how Claude approaches coding tasks.

**Typical percentage:** 1–3%.

### Skills — custom instructions

**What it is:** Custom instructions you loaded, for example a `CLAUDE.md` file in your project folder.

**Why it matters:** You can optimize this category. Remove redundant instructions or split a large `CLAUDE.md` file into smaller, session-specific files to reduce it directly.

**Typical percentage:** 1–5%, depending on how many custom instruction files you loaded.

### MCP tools — actively used integrations

**What it is:** Tool definitions for the MCP integrations you actively used in this session, for example Google Drive, Canva, and MailerLite. Each connected integration adds its tool schema to the budget the moment you call it.

**Why it matters:** This shows you which tools are currently loaded and adding to your token usage.

**Typical percentage:** 0.5–3%, depending on how many tools you called.

### MCP tools (deferred) — connected but unused

**What it is:** Tool definitions for every MCP integration you connected but did not call in this session. Claude loads these tools in advance so they stay ready when needed. They use budget whether or not you use them.

**Why it matters:** This is often the largest optimization available. If you have integrations connected that you will not need in the current session, disconnect them to free this space immediately.

**Typical percentage:** 20–50% in sessions with many connected MCP servers. This can be the biggest contributor to context usage before you even start working.

### System tools (deferred) — built-in tools

**What it is:** Built-in Claude Code tools (file operations, bash commands, search) that Claude loaded but did not yet call. Like deferred MCP tools, these tools stay ready in the background.

**Why it matters:** This overhead is fixed. You cannot reduce it.

**Typical percentage:** 3–6%.

### Autocompact buffer — reserved space

**What it is:** Reserved space, about 13,000 tokens. The system holds this space back so Claude can finish its current response when auto-compaction triggers.

**Why it matters:** Most users did not know this buffer existed. It explains why sessions seem to compact slightly before the window is technically full. This overhead is fixed. You cannot optimize it.

**Typical percentage:** 15–20%.

### Free space — remaining budget

**What it is:** Remaining budget before compaction triggers. At 0%, the window is at capacity.

**Why it matters:** If this reaches single digits, act now. Compact manually or disconnect unused integrations.

**Typical percentage:** This varies throughout the session. You want at least 20–30% free when you start complex tasks.

## Four strategies to extend your context budget

Once you can see where your tokens go, you can act on it. Here are four approaches, ordered from quickest to most structural.

### 1. Disconnect unused MCP integrations

If the "MCP tools (deferred)" category uses 30–50% of your window, and you find integrations you will not need in this session, disconnect them. This frees space immediately and does not lose any work.

How to do it: Open Claude Desktop settings. Go to the MCP integrations panel. Toggle off the servers you do not use. The change takes effect right away.

### 2. Run `/compact` manually before the window fills

Auto-compaction triggers when the window reaches capacity, but you can run it before that point. This action compresses the oldest parts of the conversation into a summary and frees space to continue.

How to do it: Type `/compact` in the Claude Code session and press Enter. Claude summarizes the conversation history and resumes with a clean slate.

When to use it: Use this before you start a new, complex task if your context usage is already above 70%.

### 3. Split large `CLAUDE.md` files into session-specific instructions

If your "Skills" category uses 5–10% of your window, and you have one large `CLAUDE.md` file with instructions for multiple workflows, split it into smaller files. Load only the instructions relevant to the current session.

How to do it: Create separate `CLAUDE.md` files for different project types or workflows. Place them in subdirectories. Load them selectively with path-scoped rules.

### 4. Start a new session for unrelated tasks

If you finish one task and are about to start a fully unrelated one, exit the current session and start fresh. This gives you a clean context window and does not carry over irrelevant conversation history.

How to do it: Exit the current session (press Ctrl+C or type `exit`), then start a new one with `claude`.

## What happens when the window fills: auto-compaction

If you reach the limit without action, Claude Code triggers auto-compaction automatically. This action compresses the oldest parts of the conversation into a summary and frees space to continue. The threshold is the total window size minus the Autocompact Buffer shown in the breakdown.

If auto-compaction fails three times in a row, the circuit breaker stops it. You must then run `/compact` manually.

If you use the context breakdown regularly, you see the window fill in time to compact on your own schedule, not on Claude's.

## When to consider upgrading your context window

If you regularly hit the 200,000-token limit despite active management, note that the Max, Team, and Enterprise plans for Claude Code support a 1,000,000-token context window. This applies to Sonnet 4.6 and later, and Opus 4.6 and later (including Opus 4.8 and Sonnet 5). This removes the limit for most long-form research and writing workflows.

Evaluate the upgrade if you work with large document sets, run extended multi-phase sessions, or use several MCP integrations at the same time.

Pro plan users have more limited access to the 1M context window. You may need to enable extra usage to unlock it. Check the current option under your plan settings in Claude Code, because how the platform shows this option has changed as the feature rolled out more broadly.

## Related reading on The Science Talk

This guide accompanies the [full context window breakdown post on The Science Talk](https://thesciencetalk.com/ai-academy/claude-code-context-window-explained/). That post includes a detailed walkthrough of each category with visual examples and real-world session data.

---

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
