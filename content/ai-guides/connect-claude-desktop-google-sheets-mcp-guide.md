---
title: "How to Connect Claude Desktop to Google Sheets via MCP: A Complete Setup Guide"
date: 2026-03-25
lastmod: 2026-04-11
draft: false
description: "Learn how to connect Claude Desktop to Google Sheets using the Model Context Protocol (MCP). The complete step-by-step guide — covering OAuth setup, service account configuration, and troubleshooting — is available as a paid resource."
keywords: ["Claude Desktop", "Google Sheets", "MCP", "Model Context Protocol", "AI integration", "automation", "mcp-google-sheets", "OAuth 2.0", "uvx"]
author: "Pranoti Kshirsagar"
reading_time: "3 min"
tags: ["Claude Desktop", "MCP", "Google Sheets", "AI Integration", "Automation"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "Connect WordPress to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com & MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
  - title: "How to Restore a WordPress Page from a WP Engine Backup"
    url: "/ai-guides/restore-wordpress-page-wpengine-backup/"
sidebar_product:
  label: "DIGITAL GUIDE"
  title: "Claude Connected to Google Sheets via MCP"
  bullets:
    - "Complete OAuth 2.0 setup walkthrough"
    - "Service account alternative (with org policy guidance)"
    - "5 real-world integration templates"
  details:
    - "Instant PDF delivery"
    - "Email support included"
  stripe_url: "https://buy.stripe.com/9B614n7699puePn0jm8Ra0o?utm_source=pranoti_site&utm_medium=sidebar&utm_campaign=claude_sheets_mcp"
  cta: "Get the guide — €12 →"
  footnote: "Complete setup guide + templates"
---

If you use **Claude Desktop** and want it to read, edit, and manage your Google Sheets directly, use the **Model Context Protocol (MCP)**. It is the cleanest and most secure way to do this. You do not need to copy data or export CSV files. You can use natural language commands like "update cell B5" or "list all my spreadsheets."

I built and documented this setup from start to end. The guide includes every configuration decision and the troubleshooting steps. You can get the connection running in under 30 minutes.

## What you will achieve

At the end of the full guide, Claude Desktop can **directly interact with any Google Sheet** you give it access to. It can read data ranges, write to cells, append rows, create new spreadsheets, and share them. You can do all of this from within a Claude conversation.

The connection uses [MCP (Model Context Protocol)](https://modelcontextprotocol.io/). This is an open standard from Anthropic. It connects AI assistants to external tools.

## Prerequisites

Before you start, you need:

- **Claude Desktop** — the latest version installed on macOS or Windows
- **A Google account** — a personal Gmail account or Google Workspace account both work
- **A Google Cloud project** — you can create one for free at [console.cloud.google.com](https://console.cloud.google.com/)
- **Terminal or command line access** — you must run a few commands
- **Python package manager (uv)** — the setup guide covers this

## Authentication: two options

The MCP server supports two authentication methods.

**Service account.** This is a separate Google identity. It accesses only the sheets you share with it. It does not need a browser login, and it works well for automation. Many Workspace accounts block service account key creation by default.

**OAuth 2.0 (recommended for most users).** You authenticate as yourself through a browser login. This method has no organization policy issues and needs no service account keys. The full guide walks through this approach.

---

## Get the complete guide

The full step-by-step walkthrough covers OAuth setup from the start, service account configuration, Claude Desktop configuration, and solutions to every common error. It is available as a paid guide.

[Get access →](https://thesciencetalk.com/claude-google-sheets-guide/)

---

## Related reading on The Science Talk

This guide accompanies the [full Google Sheets MCP post on The Science Talk](https://thesciencetalk.com/connect-claude-desktop-google-sheets-mcp-guide/). That post covers the background, the setup decisions, and what this integration enables in a real workflow.

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [explore the case studies](/case-studies/).*
