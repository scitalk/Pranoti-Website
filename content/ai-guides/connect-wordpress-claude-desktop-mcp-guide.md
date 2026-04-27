---
title: "How to Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
date: 2026-02-10
lastmod: 2026-04-02
draft: false
description: "Step-by-step guide to connecting any self-hosted WordPress site to Claude Desktop using the Model Context Protocol. Manage posts, drafts, and SEO through natural language — no plugins required."
keywords: ["Claude Desktop", "WordPress MCP", "Model Context Protocol", "Claude WordPress integration", "AI content management", "self-hosted WordPress", "claudeus-wp-mcp"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["Claude Desktop", "WordPress", "MCP", "AI Integration", "Automation"]
category: "ai-integration-guides"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com & MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
  - title: "How to Restore a WordPress Page from a WP Engine Backup"
    url: "/ai-guides/restore-wordpress-page-wpengine-backup/"
sidebar_product:
  label: "DIGITAL GUIDE"
  title: "Connect Your WordPress Site to Claude Desktop"
  bullets:
    - "Complete WordPress REST API setup"
    - "Application Password configuration (WordPress 5.6+)"
    - "5 ready-to-use content workflow templates"
  details:
    - "Instant PDF delivery"
    - "Email support included"
  stripe_url: "https://buy.stripe.com/bJe28railfNSaz70jm8Ra0p"
  cta: "Get the guide — €17 →"
  footnote: "Complete setup guide + workflow examples"
---

What if you could create, edit, and manage your WordPress posts without ever opening your browser? With **Claude Desktop and the Model Context Protocol (MCP)**, you can connect your self-hosted WordPress site directly to Claude — and manage your entire content workflow through natural language conversation.

## What the integration enables

- "Show me all draft posts"
- "Create a new draft about European AI regulation"
- "Change the title of post 1234 to…"
- "Analyse the SEO of my latest published post"
- "Add the tag 'Horizon Europe' to all posts from 2025"
- "List all images uploaded this month"

The MCP server exposes tools covering read, write, bulk operations, SEO analysis, and media management — all accessible directly from a Claude conversation. No plugins to configure on your WordPress side. No third-party dashboard to learn.

## What you need before starting

- **Claude Desktop** — latest version on macOS or Windows
- **A self-hosted WordPress site** — works with WP Engine, SiteGround, Kinsta, and other managed hosts
- **HTTPS enabled** — required for WordPress Application Passwords to appear
- **Terminal / Command Prompt access** — for a small number of commands
- **Node.js v22+** — installed during setup

No prior cloud experience needed. The companion guide walks through each of these from scratch, including the gotchas that trip most people up the first time.

## The setup: seven steps

The setup covers installing Node.js, creating a WordPress Application Password, verifying your REST API, creating the site configuration file, finding your system username, configuring Claude Desktop, and verifying the connection. The whole thing takes about 15 minutes.

The most common failure point is the Claude Desktop config file — the path to your credentials file must contain your exact system username. The guide includes copy-paste commands for both Mac and Windows so there is no guesswork.

## Common errors — all covered in the guide

- Application Passwords section missing from WordPress profile
- REST API not accessible or returning an error
- Server showing as "disconnected" in Claude Desktop
- Authentication errors after correct password entry
- Claude seeing the server but not using it
- Config changes not taking effect after restart
- Apache-based host blocking authentication headers

The complete step-by-step guide — every configuration file, authentication step, and fix for the errors above — is on The Science Talk.

[Read the full guide on The Science Talk →](https://thesciencetalk.com/news/blog-perspectives/connect-wordpress-claude-desktop-mcp-guide/)
