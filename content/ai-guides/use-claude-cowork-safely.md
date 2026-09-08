---
title: "Claude Cowork Safety: Permissions, Modes and What to Avoid"
date: 2026-05-26
lastmod: 2026-09-08
slug: "use-claude-cowork-safely"
draft: false
description: "Claude Cowork gives Claude direct access to your files, browser, and apps. Learn which permissions to enable, when to use each mode, and what to avoid."
keywords: ["Claude Cowork safety", "Claude Cowork permissions", "Claude Desktop computer use", "skip all approvals mode Claude", "Claude agentic AI setup", "Claude Chrome extension safety", "prompt injection Claude Cowork", "scheduled tasks Claude Desktop"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["Claude Cowork", "Claude Desktop", "agentic AI", "AI safety", "computer use"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "MCP Security Checklist for Claude Desktop Users"
    url: "/ai-guides/mcp-security-checklist-claude-desktop/"
  - title: "MCP Security in Claude Code: What Full Machine Access Really Involves"
    url: "/perspectives/claude-code-mcp-credential-security/"
  - title: "Model Context Protocol for Non-Developers: A Practical Primer"
    url: "/ai-guides/model-context-protocol-non-developers/"
---

*Last reviewed and updated on 8 September 2026 against Anthropic's official documentation. Claude Cowork has changed substantially since first publication: sessions now run in the cloud on Anthropic's servers and reach your computer through the Claude Desktop app, Cowork is available on web and mobile as well as desktop, and scheduled tasks run remotely.*

Claude Cowork is Anthropic's agentic feature for cross-app knowledge work. Cowork sessions run in the cloud on Anthropic's servers, and Claude reaches your files, browser, and apps through the Claude Desktop app. Claude can read and write local files, work across connected apps, and act in a browser. That capability is genuinely useful, but it also means Claude can make changes that are difficult to undo. This guide covers Claude Cowork safety: which permissions to grant, which modes to use for which tasks, and the configurations that introduce the most risk.

## What you need before starting

- A **paid Claude plan** (Pro, Max, Team, or Enterprise). Cowork runs on web at claude.ai and in the Claude mobile apps as well as on desktop
- **Claude Desktop** for macOS or Windows, latest version from [claude.com/download](https://claude.com/download), open and connected. This is required for local file access, browser use, and computer use, including when you drive a session from web or mobile
- A clear sense of which files and folders you want Claude to work with before you start

Cowork has a browser built into the Claude Desktop app, so you do not need to install anything for browser tasks. The separate [Claude in Chrome extension](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) is optional.

## How Cowork accesses your computer

Cowork operates across four access layers, each with a different risk profile:

- **Local files**: Claude can read, write, and permanently delete files in folders you connect on your computer, and only while the desktop app is open on that computer
- **Browser**: through the browser built into Claude Desktop, or the optional Claude in Chrome extension, Claude can open sites, read pages, click, type, and fill forms
- **Connected apps and services**: third-party integrations you authorize
- **Computer use**: direct screen interaction, where Claude clicks, types, and navigates your interface

> **Computer use is the highest-risk layer** because Claude interacts directly with whatever is on your screen. It follows the same approval-mode system as file and browser access, and Anthropic states that "when Claude uses your computer, it asks for your permission before accessing each application."

Cowork runs in one of three approval modes:

| Mode | Behavior |
|------|-----------|
| **Manually approve** | Claude pauses between steps and asks for approval before it acts. Best for sensitive work |
| **Automatically approve** | The default. Claude works continuously, but reviews each action for safety, such as checking for data exfiltration or prompt injection, and blocks anything it determines to be unsafe. This checking consumes more of your usage limit than the other modes |
| **Skip all approvals** | Claude does not pause to ask and nothing checks its actions automatically. File deletion still always requires your permission |

Scheduled tasks are a separate feature, not a fourth mode. They run remotely in the cloud on their cadence, even when your computer is asleep or the Claude Desktop app is closed, using whichever approval mode you set. Because they run remotely, they work with your connectors and the files saved to your Claude account, and cannot be tied to a folder on your computer.

## Step 1: Start a Cowork session and choose a working folder

### Open Cowork

On desktop, web, or mobile, find the message box and select **Cowork** instead of **Chat**, then describe your task. There is no separate on/off toggle. Cowork settings live at **Settings → Cowork**.

### Choose a working folder

When you connect a folder, **do not connect your entire home directory**. Create a dedicated working folder, for example `~/Claude-Work/`, and connect only that.

```
~/Claude-Work/
  ├── drafts/
  ├── research/
  └── exports/
```

This limits the blast radius if something goes wrong. You can connect additional folders on a task-by-task basis later.

## Step 2: Understand file access permissions

In a connected folder, Claude "can read, write, and permanently delete these files," in Anthropic's words. What gates each action is your approval mode, not the file operation itself, with one exception:

- **Read and write**: gated by your approval mode. In Manually approve, Claude asks before each action. In Automatically approve, Claude proceeds unless its safety check blocks the action.
- **Delete**: **Cowork always requires your explicit permission before permanently deleting any file**, in every mode, including Skip all approvals.

> **Never connect Cowork to folders that contain credentials, financial documents, or personal records.** Claude's session runs in an isolated cloud environment, but edits to a connected folder land on your real filesystem through the desktop app, not on a sandbox copy.

If you work with sensitive material, move only the specific files needed for the task into your dedicated Claude working folder, then move them out when the task is complete.

## Step 3: Browser access

On desktop, Cowork uses a browser built into the Claude Desktop app by default, with nothing to install. Claude can open sites, read pages, click, type, and fill forms.

If you prefer to use your own Chrome, the [Claude in Chrome extension](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) is a separate opt-in. You grant and revoke access per site in the extension's settings, and Anthropic's guidance is to grant site access only while a task needs it.

> Anthropic's [Claude in Chrome safety guidance](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely) recommends against using it for banking or investment management, legal documents or contracts, medical or health information, and work accounts with sensitive data, and suggests a separate browser profile without access to sensitive accounts.

## Step 4: Choose the right mode for your task

**Manually approve** is the safer default, and the one this guide recommends for almost everything. Claude pauses after each step, shows you what it plans to do next, and waits for your approval. This adds friction but gives you a real checkpoint before each action.

**Automatically approve** is the product default in the Cowork side panel. Claude keeps working without pausing for your sign-off, but reviews each action for safety, such as checking for data exfiltration or prompt injection, and blocks anything it determines to be unsafe. Anthropic notes this checking makes Auto consume more of your usage limit than the other modes. It is a reasonable middle ground for well-scoped, trusted tasks.

**Skip all approvals** removes checkpoints and the automatic safety review. Only file deletion still asks. Use it only when:

- The source files are fully trusted (your own documents, not content fetched from the web)
- The task scope is narrow and well-defined
- You actively sit at your screen and can interrupt immediately

> **Skip all approvals significantly increases prompt injection risk.** If Claude reads a malicious web page, email, or document while it runs with no safety review, no checkpoint exists to catch or pause a hijacked action. Anthropic defends against prompt injection with content classifiers and model training, but describes the residual risk as real, not zero.

The practical rule: use Manually approve by default, reach for Automatically approve for routine trusted work, and reserve Skip all approvals for short, contained tasks on fully trusted content.

## Step 5: Set up scheduled tasks safely

Scheduled tasks run remotely in the cloud on a cadence you set (hourly, daily, weekdays, weekly, or on demand), even when your computer is asleep or the Claude Desktop app is closed. Because they run remotely, they work with your connectors and the files saved to your Claude account, not with a folder on your computer. They are useful for recurring, low-stakes operations, for example generating a daily briefing or summary.

Anthropic's guidance: **"Don't schedule tasks that access sensitive files, send messages on your behalf, make purchases, or take other actions that are difficult to undo."** It also recommends starting with low-risk tasks, reviewing outputs regularly, and pausing tasks you are not using.

If a scheduled task fails silently, you may not notice until the damage is done.

## Claude Cowork Safety: What to Keep in Mind

**Prompt injection is a real attack vector.** In Anthropic's words, "a prompt injection attack occurs when malicious instructions are embedded in external content that Claude reads as part of a legitimate task." Any untrusted content that enters Claude's context, such as a web page, a shared document, or an email, can carry them. Manually approve gives you an approval step for every action. Automatically approve keeps a safety-review backstop. Skip all approvals removes both.

**Cowork activity via web and mobile is captured in the Compliance API.** Team and Enterprise owners can also stream Cowork events to their SIEM and observability tools through OpenTelemetry. (This reverses the position in an earlier version of this post, which predated that coverage.)

**You are responsible for Claude's actions.** Anthropic states plainly: "You remain responsible for all actions taken by Claude performed on your behalf." That includes published content, data modifications, purchases, and scheduled task outputs.

**Local access needs the desktop app open.** A Cowork session you start on web or mobile can read and write files in folders you have connected "only while the desktop app is open on that computer." Computer use and the built-in browser work the same way. Nothing on your machine is reachable when the desktop app is closed.

## What you can do now

With Cowork configured on the principle of least privilege, using a dedicated working folder, Manually approve as your default, and browser access scoped to the task, you are set up to use Claude's agentic capabilities without unnecessary exposure.

Good starting tasks for Cowork in Manually approve mode:

- Organizing and renaming files in your designated working folder
- Drafting and iterating on documents, with Claude reading source files you have explicitly shared
- Summarizing a set of PDFs you have moved into your working folder
- Researching across browser tabs while you actively supervise

For a broader view of securing your Claude Desktop setup, see the [MCP Security Checklist for Claude Desktop Users](/ai-guides/mcp-security-checklist-claude-desktop/).

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
