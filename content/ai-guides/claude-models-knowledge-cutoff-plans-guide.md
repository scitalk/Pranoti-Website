---
title: "Claude Models Compared: Knowledge Cutoff, Pricing and Plans"
date: 2026-10-03
lastmod: 2026-10-03
draft: false
description: "Claude models compared: knowledge cutoff, strengths and pricing for Fable, Opus, Sonnet and Haiku, plus Free, Pro, Max, Team and Enterprise plans."
keywords: ["Claude models", "Claude knowledge cutoff", "Claude Opus vs Sonnet", "Claude Fable", "Claude effort level", "Claude Pro vs Max", "Claude Enterprise pricing", "which Claude model"]
author: "Pranoti Kshirsagar"
reading_time: "8 min"
tags: ["Claude", "Claude models", "AI adoption", "pricing", "knowledge cutoff"]
category: "ai-integration-guides"
pillar: "AI Adoption"
featured_image: "/images/ai-guides_perspectives/ai-for-scientists.jpg"
sidebar_links:
  - title: "Claude Code Context Window: What Each Category Means"
    url: "/ai-guides/claude-code-context-window-breakdown-guide/"
  - title: "Use Claude Cowork Safely"
    url: "/ai-guides/use-claude-cowork-safely/"
---

This guide compares the Claude models in the chat model menu: Fable, Opus, Sonnet and Haiku, plus the older versions under "More models". It covers each model's knowledge cutoff, strengths and pricing, the Effort setting, and the differences between the Free, Pro, Max, Team and Enterprise plans.

Every fact here comes from Anthropic's own documentation, linked at the end. Figures are correct as of 3 October 2026.

## Which Claude model should I use?

- **Sonnet 5.5** for most everyday chat: writing, editing, analysis.
- **Opus 5.5** for hard reasoning and long back-and-forth work.
- **Fable 5.1** for long tasks with many steps, or dense source material.
- **Haiku 4.5** for quick lookups and short summaries.
- Leave effort on **Default** until you have a reason to change it.

## Current Claude models compared

| | Fable 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 4.5 |
|---|---|---|---|---|
| Anthropic's description | For demanding reasoning and long-horizon agentic work | For long-running agentic coding and knowledge work | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| Speed | Slower | Moderate | Fast | Fastest |
| Reliable knowledge cutoff | Jun 2026 | Jun 2026 | Jun 2026 | Feb 2025 |
| Context window | 1M tokens | 1M tokens | 1M tokens | 200K tokens |
| API price (input / output per million tokens) | $10 / $50 | $4 / $20 | $2 / $10 | $1 / $5 |

Anthropic's Claude Academy gives this task guidance:

- **Haiku:** simple questions with short answers, quick lookup or categorisation, simple summarisation.
- **Sonnet:** writing and content creation, coding, analysis that needs reasoning but is not extremely complex.
- **Opus:** deep research and analysis you will question, redirect and build on.
- **Fable:** long tasks with many connected steps, and outputs from dense source material such as long documents, charts and technical diagrams.

## Claude knowledge cutoff by model

The reliable knowledge cutoff is the date through which a model's knowledge is "most extensive and reliable". Anything after that date, the model does not know from training.

| Model | Status | Reliable knowledge cutoff |
|---|---|---|
| Fable 5.1, Opus 5.5, Sonnet 5.5 | Current | Jun 2026 |
| Opus 5 | Legacy | May 2026 |
| Fable 5, Sonnet 5, Opus 4.8, Opus 4.7 | Legacy | Jan 2026 |
| Sonnet 4.6 | Legacy | Aug 2025 |
| Opus 4.6, Opus 4.5 | Legacy | May 2025 |
| Haiku 4.5 | Current | Feb 2025 |

Two things follow from this table.

**Even the newest models are behind.** In October 2026, a June 2026 cutoff is four months old. Haiku 4.5 is more than a year and a half behind. For anything recent (prices, laws, product releases, news), make Claude check a live source.

**The same cutoff does not mean the same model.** Fable, Opus and Sonnet share a June 2026 cutoff. The difference is how well they reason with what they know, how fast they answer, and what they cost to run.

You do not need any extension for live information. Anthropic's help centre says: "There's no web search toggle. Claude searches the web when it helps." Claude in Chrome is a separate browser extension that lets Claude read, click and navigate websites with you. It is not required for search. If you let Claude act in your browser or files, read [how to use Claude Cowork safely](/ai-guides/use-claude-cowork-safely/).

## Why do older models still appear?

Anthropic labels older models **Legacy**: they "will no longer receive updates and may be deprecated in the future". Each legacy model page says you "should consider migrating" to the newer version "for improved performance".

Anthropic gives four reasons it does not retire models immediately:

- "Some users find specific models especially useful or compelling, even when new models are more capable."
- Research value, especially in comparison with newer models.
- Safety risks linked to retiring models.
- Possible model welfare concerns.

Models are eventually retired "to ensure capacity for new model releases". On the API, Anthropic gives at least 60 days' notice.

## Claude effort levels explained

Click the model name next to the send button, then **Effort**. Each model marks its recommended level as Default.

| Effort | Anthropic's guidance |
|---|---|
| Low, Medium | "Work well for routine tasks and stretch your usage further" |
| High | The best overall balance of quality and speed |
| Extra high | Long-running coding and agentic tasks. Available on Opus 4.7 and newer |
| Max | The most thorough option, for the deepest reasoning |

Higher effort means more thinking, and thinking uses tokens. That is why low effort makes your allowance last longer. Haiku 4.5 does not support the effort setting.

## Claude pricing: Free vs Pro vs Max vs Team vs Enterprise

There are two kinds of price, and they are easy to mix up.

**API prices** are per million tokens (see the model table above). Fable costs five times more per token than Sonnet. A bigger model does not necessarily use more tokens; each token costs more. This matters to you directly on Enterprise, which charges usage at API rates.

**Plan prices** are what you pay for the Claude app:

| Plan | Price (USD) | What changes |
|---|---|---|
| Free | $0 | Chat on web, desktop and mobile. Web search, file creation, memory, [connectors](/ai-guides/model-context-protocol-non-developers/), up to 5 projects. Sonnet and Haiku only |
| Pro | $20/month, or $17/month billed annually ($200 up front) | At least 5x more usage per 5-hour session than Free. Adds Opus, Claude Code, Claude in Chrome, Research, unlimited projects |
| Max | From $100/month | Choose 5x or 20x more usage per 5-hour session than Pro. Higher output limits, priority access at high traffic times |
| Team | Standard seat $25/month ($20 billed annually). Premium seat $125/month ($100 billed annually) | Single sign-on (SSO), admin controls for connectors. Standard seats get more usage than Pro; premium seats get 5x more than standard |
| Enterprise | US$20/seat/month billed annually, plus usage at API rates | Role-based access with fine-grained permissions, SCIM, audit logs, compliance API, custom data retention controls |

Fable access differs by plan. Free has none. Pro gets it through "usage credits". Max gets it within "50% of weekly limits", as do Team premium seats. Enterprise includes it.

Prices exclude tax, and Anthropic states that prices and plans "are subject to change". On Enterprise, an administrator can turn off models or effort levels for your role. If an option you expect is missing, ask your admin.

## How to choose a Claude model in practice

1. Start new chats on Sonnet 5.5 at Default effort.
2. Move to Opus 5.5 when the answer needs real reasoning, or Fable 5.1 when the task is long or the source material is dense.
3. Raise effort only when an answer is shallow. Lower it for routine tasks.
4. For anything after June 2026, ask Claude to search, and check the source it gives you.
5. On Enterprise, remember that the model you pick changes the cost per token.

## Frequently asked questions

### What is the knowledge cutoff of the latest Claude models?

Claude Fable 5.1, Opus 5.5 and Sonnet 5.5 have a reliable knowledge cutoff of June 2026. Claude Haiku 4.5 has a reliable knowledge cutoff of February 2025. Source: Anthropic's models overview.

### Which Claude model should I use?

Anthropic's Claude Academy recommends Haiku for simple questions and quick lookups, Sonnet for writing, coding and moderate analysis, Opus for deep research and analysis you will question and build on, and Fable for long tasks with many connected steps or dense source material.

### What is the difference between Claude Pro and Max?

Pro costs $20 per month, or $17 per month billed annually. Max starts at $100 per month and gives 5x or 20x more usage per 5-hour session than Pro, plus higher output limits and priority access at high traffic times. Source: claude.com/pricing, checked 3 October 2026.

### Do I need Claude in Chrome for Claude to search the web?

No. Anthropic's help centre states that there is no web search toggle and that Claude searches the web when it helps. Claude in Chrome is a separate browser extension that lets Claude read, click and navigate websites.

## Sources

- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview), Claude Platform Docs
- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations), Claude Platform Docs
- Legacy model pages: [Fable 5](https://platform.claude.com/docs/en/models/fable-5/overview), [Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview), [Opus 4.8](https://platform.claude.com/docs/en/models/opus-4-8/overview), [Opus 4.7](https://platform.claude.com/docs/en/models/opus-4-7/overview), [Opus 4.6](https://platform.claude.com/docs/en/models/opus-4-6/overview), [Opus 4.5](https://platform.claude.com/docs/en/models/opus-4-5/overview), [Sonnet 5](https://platform.claude.com/docs/en/models/sonnet-5/overview), [Sonnet 4.6](https://platform.claude.com/docs/en/models/sonnet-4-6/overview)
- [Choosing the right Claude model](https://academy.claude.com/tutorials/choosing-the-right-claude-model), Claude Academy
- [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings), Claude Help Center
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), Claude Help Center
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome), Claude Help Center
- [Commitments on model deprecation and preservation](https://www.anthropic.com/research/deprecation-commitments), Anthropic
- [Pricing](https://claude.com/pricing), Claude
