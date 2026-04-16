---
title: "Claude and WordPress Connected via MCP — Managing Posts Without Leaving Chat"
date: 2026-03-30
draft: false
type: "case-studies"
category: "ai-automation-integration"
display_category: "AI Integration & Automation"
subtitle: "How to stop context-switching between your WordPress dashboard and Claude, and manage your entire content workflow through conversation"
description: "How to stop context-switching between WordPress dashboard and Claude by connecting them via MCP. Manage your entire content workflow — drafting, publishing, updating — through conversation. No plugins required; works with any self-hosted site."
thumbnail: "https://thesciencetalk.com/wp-content/uploads/2026/02/wordpress-claude_MCP-1.png"
pdf_url: "/case-studies/wordpress-claude-mcp.pdf"
tech_stack:
  - "Claude Desktop"
  - "claudeus-wp-mcp"
  - "Node.js"
  - "WordPress REST API"
  - "Application Passwords"
  - "Any self-hosted WordPress 5.6+"
  - "REST API must be enabled — some hosts block it by default"
metrics:
  - value: "4 hrs"
    label: "saved per post"
  - value: "100%"
    label: "works with any self-hosted site"
  - value: "∞"
    label: "workflow possibilities"
problem:
  goal: "Use Claude's analytical and creative capabilities **directly on WordPress content** — draft posts, analyse SEO, bulk-update metadata, check draft status — without ever opening the WordPress dashboard."
  reality: "Content workflows meant constant switching between Claude and the WordPress admin. Ask Claude to help draft something, copy text back, manually format in WordPress, review SEO separately, **repeat dozens of times per week**."
workflow:
  before:
    - "Draft in Claude"
    - "Copy to WordPress"
    - "Format and edit"
    - "Setup SEO"
    - "Publish"
  after:
    - "Draft, edit, approve content in Claude"
    - "Final edits and SEO setup"
    - "Publish"
misconception: "WordPress integrations require plugins or third-party tools on your server. **No.** MCP servers run locally on your computer. WordPress only needs to have its REST API enabled (built-in since 5.6) and one application password created. Zero modifications to your site's code, zero plugins, zero security risk."
blockers:
  - issue_title: "REST API disabled on host"
    issue_desc: "Some managed WordPress hosts block the REST API by default for security. Every standard MCP setup assumes it's available."
    solution: "Check hosting dashboard for REST API settings or contact support. The API is core WordPress; hosts sometimes just need it explicitly enabled in their control panel."
  - issue_title: "Application Passwords blocked by security plugins"
    issue_desc: "Wordfence and similar plugins disable this feature by default, even though it's a native WordPress feature."
    solution: "Check your security plugin settings. Find 'Application Passwords' or 'REST API' configuration and enable it for your user. Create the password once it's enabled."
  - issue_title: "Wrong path in Claude Desktop config"
    issue_desc: "Using a placeholder path instead of your actual username causes silent connection failure with no error message."
    solution: "Always use your actual system username from **whoami** (Mac) or **echo %USERNAME%** (Windows). Wrong path = immediate disconnect when Claude starts."
outcomes:
  - "List posts by status, date, or content — see drafts, scheduled, published instantly"
  - "Create and update posts directly — no copy-paste, full formatting support"
  - "Analyse SEO — get recommendations before publishing"
  - "Bulk operations — add tags, update categories, manage metadata across posts"
architecture:
  - ["Node.js installed", "lightweight runtime for the MCP server"]
  - ["WordPress Application Password", "secure auth method, created in User Profile"]
  - ["Site configuration file", "~/.wp-mcp/wp-sites.json with URL, username, and password"]
  - ["Claude Desktop MCP config", "points to local MCP server with correct system path"]
reflection: "Test the REST API first — before wasting time on configuration, verify you can reach /wp-json/ from your browser. Know your host's security posture upfront; REST API blocks and Application Password restrictions are host-specific, not WordPress bugs. Use a staging site first if you have one. And always verify your system username exactly with whoami/echo %USERNAME% — configuration fails silently on path mismatches."
cta_text: "Full step-by-step walkthrough published at thesciencetalk.com · More case studies at pranoti.thesciencetalk.com"
guide_url: "https://thesciencetalk.com/news/blog-perspectives/connect-wordpress-claude-desktop-mcp-guide/"
---
