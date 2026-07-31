---
title: "Claude Cowork Safety: Permissions, Modes and What to Avoid"
date: 2026-05-26
lastmod: 2026-05-26
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

Claude Cowork is Anthropic's agentic feature that lets Claude act directly on your computer — reading and writing files, navigating your browser, and interacting with connected apps. That capability is genuinely useful, but it also means Claude can make changes that are difficult to undo. This guide covers Claude Cowork safety: which permissions to grant, which modes to use for which tasks, and the configurations that introduce the most risk.

## What you need before starting

- A **paid Claude plan** (Pro, Max, Team, or Enterprise)
- **Claude Desktop** for macOS or Windows — download the latest version from [claude.ai/download](https://claude.ai/download)
- The **Claude in Chrome extension** if you want browser access (optional — install only if your tasks require it)
- A clear sense of which files and folders you want Claude to work with before you start

## How Cowork accesses your computer

Cowork operates across four access layers, each with a different risk profile:

- **Local files** — Claude can read, write, and permanently delete files in folders you share with it
- **Browser** — via the Claude in Chrome extension, Claude can read and interact with open tabs
- **Connected apps and services** — third-party integrations you authorise
- **Computer use** — direct screen interaction: Claude clicks, types, and navigates your interface

> **Computer use is the highest-risk layer** because Claude interacts directly with whatever is on your screen — but it still follows the same approval-mode system as file and browser access, asking permission before accessing each application and before destructive actions.

Cowork runs in one of three approval modes:

| Mode | Behaviour |
|------|-----------|
| **Manually Approve** | Claude pauses between steps and asks for approval before acting |
| **Automatically Approve** | Claude works continuously, but every action still gets a safety review, blocking anything flagged as unsafe |
| **Skip All Approvals** | Claude executes tasks continuously with no safety review at all |

Scheduled tasks are a separate feature, not a fourth mode — they run automated workflows on a schedule while your desktop is awake and the app is open, using whichever approval mode you've set.

## Step 1: Enable Cowork in Claude Desktop

### Step 1: Open Settings in Claude Desktop

Open Claude Desktop and navigate to **Settings → Cowork**. Toggle Cowork on. On first launch, Claude will prompt you to grant initial file access.

### Step 2: Choose a working folder

When Claude asks which folders to share, **do not share your entire home directory**. Create a dedicated working folder — for example `~/Claude-Work/` — and share only that.

```
~/Claude-Work/
  ├── drafts/
  ├── research/
  └── exports/
```

This limits the blast radius if something goes wrong. You can share additional folders on a task-by-task basis later.

## Step 2: Understand file access permissions

Claude distinguishes between three types of file actions:

- **Read** — scanning, analysing, summarising a file. Permitted automatically once a folder is shared.
- **Write** — creating, renaming, or modifying a file. Requires an explicit permission grant per session.
- **Delete** — permanent removal. Triggers a **double confirmation prompt** before Claude proceeds.

> **Never grant Cowork access to folders containing credentials, financial documents, or personal records.** Claude's file access is real — changes are made directly to your filesystem, not to a sandbox copy.

If you are working with sensitive material, move only the specific files needed for the task into your dedicated Claude working folder, then move them out when the task is complete.

## Step 3: Add browser access with Claude in Chrome

Install the [Claude in Chrome extension](https://chromewebstore.google.com/detail/claude/ppmojbbbekcahnhaeceeefkokblkifak) from the Chrome Web Store only if your tasks genuinely require it — for example, researching across tabs or filling in web forms.

Once installed, Claude can read the content of open tabs and interact with page elements. **Only grant tab access when actively running a task.** Close the extension permission when you are finished.

> Do not use Claude in Chrome on tabs containing banking, healthcare portals, or any service where unintended form submissions or clicks would cause real-world consequences.

## Step 4: Choose the right mode for your task

**Manually Approve** is the right default for almost everything. Claude pauses after each step, shows you what it plans to do next, and waits for your approval. This adds a small amount of friction but gives you a meaningful checkpoint before each action.

**Automatically Approve** is the recommended mode for continuous work you still want a safety net on. Claude keeps working without pausing for your sign-off on every step, but each action still passes through a safety review that blocks anything flagged as unsafe. This is a reasonable middle ground for well-scoped, trusted tasks.

**Skip All Approvals** removes checkpoints and safety review entirely. It is appropriate only when:

- The source files are fully trusted (your own documents, not content fetched from the web)
- The task scope is narrow and well-defined
- You are actively present at your screen and can interrupt immediately

> **Using "Skip All Approvals" significantly increases prompt injection risk.** If Claude reads a malicious web page, email, or document while operating with no safety review, there is no checkpoint at which anything can catch or pause a hijacked action. Anthropic's own documentation acknowledges that attack probability is non-zero even with classifier-based defences in place elsewhere in the product.

The practical rule: use Manually Approve by default, reach for Automatically Approve for routine trusted work, and reserve Skip All Approvals for short, contained tasks on fully trusted content.

## Step 5: Set up scheduled tasks safely

Scheduled tasks run automatically at set times while Claude Desktop is open. They are useful for recurring, low-stakes operations — for example, organising files in a designated folder or generating a daily summary from a local document.

**Do not schedule tasks that involve:**

- Sensitive or personal data processed without your supervision
- Financial operations or purchases of any kind
- Sending messages or publishing content on your behalf
- Any workflow that requires accessing credentials or authentication tokens

Anthropic explicitly flags these as high-risk scheduled task patterns. If a scheduled task fails silently, you may not notice until the damage is done.

## Claude Cowork Safety: What to Keep in Mind

**Prompt injection is a real attack vector.** Any untrusted content that enters Claude's context — a web page, a shared document, an email — can potentially contain instructions designed to hijack Claude's actions. Manually Approve mitigates this by giving you an approval step for every action; Automatically Approve keeps a safety-review backstop; Skip All Approvals removes both.

**Cowork activity is not currently captured in the Compliance API.** If you are using Claude on an Enterprise plan for regulated work, be aware that Cowork sessions are not logged in the same way as standard interactions.

**You are responsible for Claude's actions.** Anthropic's terms make clear that users bear liability for what Claude does on their behalf — including published content, data modifications, and third-party terms compliance.

**Phone access extends desktop permissions.** If you connect Claude to your mobile device, it inherits the access permissions you have granted on desktop. Review those permissions before enabling any mobile integration.

## What you can do now

With Cowork configured on the principle of least privilege — a dedicated working folder, Manually Approve as the default, and browser access granted only when needed — you are set up to use Claude's agentic capabilities without unnecessary exposure.

Good starting tasks for Cowork in Manually Approve mode:

- Organising and renaming files in your designated working folder
- Drafting and iterating on documents, with Claude reading source files you have explicitly shared
- Summarising a set of PDFs you have moved into your working folder
- Researching across browser tabs while you are actively supervising

For a broader view of securing your Claude Desktop setup, see the [MCP Security Checklist for Claude Desktop Users](/ai-guides/mcp-security-checklist-claude-desktop/).

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
