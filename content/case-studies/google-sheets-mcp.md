---
title: "Custom Claude Integration for Google Workspace: Google Sheets MCP"
date: 2026-04-03
subtitle: "Eliminate constant CSV downloads and copy-paste friction to Claude reading, writing, and creating Google Sheets autonomously."
category: "AI Integration"
tech_stack:
  - "Claude Desktop"
  - "mcp-google-sheets"
  - "Google Sheets API"
  - "Google Drive API"
  - "OAuth 2.0"
  - "uvx"
  - "Google Workspace Business Standard"
  - "Native Drive connector — Docs only, not Sheets"
metrics:
  - value: "5 steps"
    label: "eliminated from every data task"
  - value: "0 €"
    label: "ongoing cost"
  - value: "All sheets"
    label: "accessible — not just one"
problem:
  goal: "Deep integration of Claude across all business workflows. Not a one-off connection — a flexible, reusable bridge between Claude and **any Google Sheet**, for any task: grants database, social media analysis, webinar tracking, client data."
  reality: "Every time data needed to move between Claude and a spreadsheet, it required a **full manual loop** — downloading, converting, uploading, sharing, then copying results back out. Slow, error-prone, and capacity-draining."
workflow:
  before:
    - "Export CSV from source"
    - "Download to local machine"
    - "Upload to Google Drive"
    - "Open as Google Sheet"
    - "Copy-paste into Claude"
  after:
    - "Tell Claude what to do with the sheet"
    - "Claude reads, writes, or creates directly"
    - "Done"
misconception: "Claude.ai has a native Google Drive connector — so surely it can access Google Sheets? **No.** The native Drive connector is limited to Google Docs only. Claude cannot read cell contents, write to cells, or create new spreadsheets through it. For any real Sheets integration, a dedicated MCP server is required — in Claude Desktop, configured separately from claude.ai entirely."
blockers:
  - issue_title: "Service account key creation blocked"
    issue_desc: "Google Workspace org policy had JSON key downloads disabled. Every standard tutorial assumes this works."
    solution: "Switched to **OAuth 2.0 Client ID** (Desktop app type) — bypasses org policy entirely, uses personal auth instead of service account keys."
  - issue_title: "Google Drive API not enabled"
    issue_desc: "mcp-google-sheets requires both Sheets API and Drive API. Enabling only one causes silent failures with no useful error message."
    solution: "Explicitly enabled **both APIs** in GCP Library — Sheets API and Drive API. They don't auto-enable each other."
  - issue_title: "uvx not resolving in Claude Desktop config"
    issue_desc: "Using 'uvx' as the command caused silent launch failures with no error output to debug from."
    solution: "Replaced with the **full absolute path** to uvx (e.g. /Users/name/.local/bin/uvx). Resolved immediately."
outcomes:
  - "Read cell contents directly — no upload, no copy-paste"
  - "Write and update cells without manually touching the sheet"
  - "Create brand new spreadsheets from scratch on command"
  - "Works across all sheets — grants database, social media analysis, webinar tracking, and more"
architecture:
  - ["Google Cloud project", "Sheets API + Drive API both enabled explicitly"]
  - ["OAuth 2.0 Client ID", "(Desktop app) — consent screen configured, personal email as test user"]
  - ["mcp-google-sheets added to claude_desktop_config.json", "full absolute uvx path, OAuth credentials in env block"]
  - ["One-time browser auth flow", "token saved automatically, no repeat login needed"]
reflection: "Start with OAuth from day one — even without org policy restrictions, it's more portable and avoids the security risk of stored JSON key files. Treat Claude Desktop and claude.ai as completely separate systems from the start — different configs, different MCP connections, nothing shared. Always use absolute paths in Claude Desktop configs; 'uvx' alone is a silent failure waiting to happen."
cta_text: "Full step-by-step walkthrough published at thesciencetalk.com · More case studies at pranoti.thesciencetalk.com"
guide_url: "https://pranoti.thesciencetalk.com/ai-integration-guides/connect-claude-desktop-google-sheets-mcp-guide/index.html"
related_tst_posts:
  - title: "How to Connect Claude Desktop to Google Sheets via MCP — full post on The Science Talk"
    url: "https://thesciencetalk.com/ai-academy/connect-claude-desktop-google-sheets-mcp-guide/"
---
