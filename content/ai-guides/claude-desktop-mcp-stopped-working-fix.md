---
title: "Claude Desktop MCP Stopped Working: How to Fix It"
date: 2026-05-05
lastmod: 2026-05-05
slug: "claude-desktop-mcp-stopped-working-fix"
draft: false
description: "Learn why your Claude Desktop MCP stopped working on May 1st, diagnose the root cause, fix the GA connector, and prevent silent breakage with version pinning."
keywords: ["Claude Desktop MCP stopped working", "MCP Google Analytics connector", "MCP version pinning", "uvx @latest updates", "Claude MCP debugging", "MCP refresh token scope", "third-party package auto-update"]
author: "Pranoti Kshirsagar"
reading_time: "~12 min"
tags: ["Claude Desktop", "MCP", "Google Analytics", "debugging", "version pinning", "OAuth"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "Connect Google Analytics GA4 to Claude Desktop via MCP"
    url: "/ai-guides/connect-google-analytics-ga4-claude-desktop-mcp/"
  - title: "Claude Desktop MCP Setup: A Beginner's Guide"
    url: "/ai-guides/claude-desktop-mcp-setup-beginners-guide/"
  - title: "Model Context Protocol for Non-Developers: A Practical Primer"
    url: "/ai-guides/model-context-protocol-non-developers/"
---

On May 1st, your Claude Desktop MCP connector stopped working. You didn't change anything. This guide explains why your MCP broke silently, how to diagnose the root cause using the Google Analytics MCP as a worked example, and how to prevent future breakage through version pinning.

## What you need before starting

- **Claude Desktop** (current version installed on your Mac or Linux machine)
- An active **Google Cloud project** with OAuth 2.0 desktop app credentials (if fixing the GA MCP specifically)
- **Access to your Claude config file** at `~/Library/Application Support/Claude/claude_desktop_config.json`
- Basic familiarity with YAML syntax and environment variables
- **5–10 minutes** for diagnosis and fix (longer if creating new OAuth credentials)

## Understanding why MCP connectors break silently

When you install an MCP server using `uvx` with the `@latest` tag, you're not downloading a pinned version—you're telling `uvx` to check PyPI every time Claude Desktop launches and fetch whatever the latest published version is.

Third-party MCP packages (like `mcp-google-analytics`) live on PyPI, not on your machine. Each time you start Claude, `uvx` queries PyPI to see if a newer version exists and silently swaps it in. If the new version introduces an API change, adds new scopes, or modifies authentication, your old credentials and configuration may no longer work.

> **This is not a Claude Desktop update.** Claude itself is not changing. A third-party developer published a new version of their MCP package, and `uvx @latest` pulled it without notifying you.

On May 1st, `mcp-google-analytics` was updated with new features that required the Google Analytics Admin API in addition to the Data API. The Admin API requires the `analytics.edit` scope, but the existing refresh token only had `analytics.readonly` scope. When Claude tried to call the Admin API method, Google's OAuth server rejected the request: **`ACCESS_TOKEN_SCOPE_INSUFFICIENT` (403).**

## Diagnosing a broken MCP: three checks

**Check 1: Look for error messages in Claude Desktop's console**

Open Claude Desktop. If your MCP is broken, you may see an error in your chat or in the debug output. The most common signature is:

```
ACCESS_TOKEN_SCOPE_INSUFFICIENT
```

This means the access token your MCP is using doesn't have permission for what it's trying to do.

**Check 2: Verify the refresh token has the right scopes**

For Google Analytics MCP specifically, your refresh token must include the `analytics.readonly` scope. If the token was created before the MCP update and the new version added Admin API calls, the token is now insufficient.

You can't see token scopes directly in your config file—they're stored in Google's OAuth server. The only way to verify is to create a new token with explicit scope declaration.

**Check 3: Check the MCP package version in your config**

Open `~/Library/Application Support/Claude/claude_desktop_config.json` and find the MCP server entry. Look for the `args` line:

```json
"args": ["mcp-google-analytics@latest"]
```

If you see `@latest`, your MCP can update automatically without warning. This is the root cause of silent breakage.

## Fixing the GA MCP connector: step-by-step

### Step 1: Create new OAuth credentials in Google Cloud

Go to [Google Cloud Console](https://console.cloud.google.com/). Create a new project or use an existing one.

Navigate to **APIs & Services** → **Credentials**. Click **+ Create Credentials** → **OAuth client ID** → **Desktop app**.

Download the JSON file. This will contain your **client_id** and **client_secret**.

### Step 2: Re-authenticate with the correct scopes

Run this command in your terminal:

```bash
python3 -c "
import webbrowser
import json
from google_auth_oauthlib.flow import InstalledAppFlow

# Update these paths to your credential file
CREDS_FILE = '/path/to/your/client_secret_*.json'
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
creds = flow.run_local_server(port=8080)

# Extract refresh token
print('Refresh token:')
print(creds.refresh_token)
"
```

A browser window will open. Sign in with the Google account that owns your Analytics property. Approve access when prompted. The script will print your new refresh token—**copy this value**.

> **Why `analytics.readonly` and not `analytics.edit`?** The GA Data API (for querying data) only needs read access. The Admin API is not needed unless you're managing GA properties, accounts, or creating new properties. For most users, `analytics.readonly` is sufficient.

### Step 3: Update your Claude config with new credentials

Open `~/Library/Application Support/Claude/claude_desktop_config.json` in your text editor. Find your MCP server entry (or create one if missing):

```json
"google-analytics-thesciencetalk": {
  "command": "/Users/yourusername/.local/bin/uvx",
  "args": ["mcp-google-analytics@0.0.3"],
  "env": {
    "GOOGLE_ANALYTICS_CLIENT_ID": "YOUR_CLIENT_ID.apps.googleusercontent.com",
    "GOOGLE_ANALYTICS_CLIENT_SECRET": "YOUR_CLIENT_SECRET",
    "GOOGLE_ANALYTICS_REFRESH_TOKEN": "YOUR_REFRESH_TOKEN",
    "GOOGLE_ANALYTICS_PROPERTY_ID": "YOUR_PROPERTY_ID"
  }
}
```

Replace:
- **`YOUR_CLIENT_ID`** — from your downloaded JSON (the `client_id` field)
- **`YOUR_CLIENT_SECRET`** — from your downloaded JSON (the `client_secret` field)
- **`YOUR_REFRESH_TOKEN`** — the token you just printed
- **`YOUR_PROPERTY_ID`** — your Google Analytics GA4 property ID (e.g., `465530700`)

> **Note the version pinning:** Instead of `mcp-google-analytics@latest`, we're using `@0.0.3`. This is intentional—see the next section.

### Step 4: Restart Claude Desktop and test

Close Claude Desktop completely. Reopen it. In your chat, try a simple query:

```
Get me the active users and sessions for the last 7 days.
```

If the MCP is fixed, you'll see data. If you see `ACCESS_TOKEN_SCOPE_INSUFFICIENT` again, double-check that your refresh token was created with the correct scopes and that you've restarted Claude after updating the config.

## Preventing future breakage: pin your package version

The root cause of May 1st's breakage was `@latest`. Every time Claude starts, `uvx` queries PyPI. If a new version exists, you silently get it. When that new version has breaking changes, your MCP breaks without warning.

**Replace `@latest` with a specific version number.**

Instead of:

```json
"args": ["mcp-google-analytics@latest"]
```

Use:

```json
"args": ["mcp-google-analytics@0.0.3"]
```

> **What version should I use?** Check [PyPI](https://pypi.org/project/mcp-google-analytics/) for the latest stable version. As of May 2026, `0.0.3` is stable. Replace `0.0.3` with whatever is current.

**Trade-offs:**

| Using `@latest` | Using a pinned version |
|---|---|
| Automatic updates (convenience) | No automatic updates (stability) |
| Silent breakage risk | You control when to upgrade |
| Latest features immediately | May miss security patches |
| Requires investigation when broken | Requires manual version bump |

**For production use or daily automation, pinning is worth the extra step.** You sacrifice early access to new features in exchange for reliability.

## Troubleshooting

**Error: `ACCESS_TOKEN_SCOPE_INSUFFICIENT`**

Cause: Your refresh token doesn't have `analytics.readonly` scope.
Fix: Create a new token following Step 2 above. Make sure the SCOPES list includes `https://www.googleapis.com/auth/analytics.readonly`.

**Error: `Invalid Credentials` or `Unauthorized`**

Cause: Your `CLIENT_ID`, `CLIENT_SECRET`, or `PROPERTY_ID` is incorrect.
Fix: Double-check each value in your config against your Google Cloud Console. Restart Claude after making changes.

**Error: `Property not found`**

Cause: Your `PROPERTY_ID` doesn't exist or isn't linked to your Google account.
Fix: Log into Google Analytics and verify the property ID. You can find it in **Admin** → **Property Settings** → **Property ID**.

**Error: MCP still not working after restart**

Cause: Claude caches the config and may not reload it immediately.
Fix: (1) Close Claude completely. (2) Wait 5 seconds. (3) Reopen Claude. Avoid force-quit if possible—a clean shutdown helps the config reload.

## What you can do now

Your GA MCP is now stable and won't break unexpectedly if you've pinned the version. You can now:

- **Query Google Analytics data** directly in Claude: "What's my top traffic source this week?"
- **Build automation** that reliably fetches GA data as part of a larger workflow
- **Set up regular reports** using scheduled Claude sessions that pull GA metrics

Next steps: If you have multiple GA properties, add them as separate MCP server entries in your config (use different `env` sections for each property). If you use other MCP tools from PyPI (Google Sheets, WordPress, etc.), apply the same version pinning pattern to prevent similar silent breakage.

## Related reading on The Science Talk

This guide accompanies the [complete GA4 MCP setup guide on The Science Talk](https://thesciencetalk.com/news/connect-google-analytics-ga4-claude-desktop-mcp/) — which walks through the initial installation step-by-step from scratch. That post assumes no prior MCP experience; this post focuses on troubleshooting and preventing breakage after initial setup.

---

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
