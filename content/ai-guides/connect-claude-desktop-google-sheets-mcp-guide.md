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

If you use **Claude Desktop** and want it to read, edit, and manage your Google Sheets directly, the **Model Context Protocol (MCP)** is the cleanest and most secure way to do it. No copy-pasting data, no exporting CSVs — just natural language commands like "update cell B5" or "list all my spreadsheets."

I built and documented this setup end-to-end — including every configuration decision and the troubleshooting rabbit holes — so you can get it running in under 30 minutes.

## What you'll achieve

By the end of the full guide, your Claude Desktop will be able to **directly interact with any Google Sheet** you give it access to — reading data ranges, writing to cells, appending rows, creating new spreadsheets, and sharing them, all from within a Claude conversation.

The connection uses [MCP (Model Context Protocol)](https://modelcontextprotocol.io/), an open standard by Anthropic for connecting AI assistants to external tools.

## Prerequisites

Before starting, you'll need:

- **Claude Desktop** — the latest version installed on macOS or Windows
- **A Google account** — personal Gmail or Google Workspace both work
- **A Google Cloud project** — free to create at [console.cloud.google.com](https://console.cloud.google.com/)
- **Terminal/command line access** — you'll need to run a few commands
- **Python package manager (uv)** — covered in the setup guide

## Authentication: two options

The MCP server supports two authentication methods:

**Service account** — a separate Google identity that accesses only the sheets you share with it. Headless (no browser login) and good for automation, but many Workspace accounts block service account key creation by default.

**OAuth 2.0 (recommended for most users)** — authenticate as yourself via a browser login. No organisation policy issues, no service account keys. This is the approach I walk through in the full guide.

---

## Get the complete guide

The full step-by-step walkthrough — OAuth setup from scratch, service account configuration, Claude Desktop config, and solutions to every common error — is available as a paid guide.

[Get access →](https://thesciencetalk.com/claude-google-sheets-guide/)

---

## Related reading on The Science Talk

This guide accompanies the [full Google Sheets MCP post on The Science Talk](https://thesciencetalk.com/connect-claude-desktop-google-sheets-mcp-guide/) — covering the background, setup decisions, and what this integration unlocks in a real workflow.

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [explore the case studies](/case-studies/).*
