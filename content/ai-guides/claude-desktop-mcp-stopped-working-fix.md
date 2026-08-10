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

On May 1st, your Claude Desktop MCP connector stopped working. You did not change anything. This guide explains why your MCP broke silently. It shows how to diagnose the root cause with the Google Analytics MCP as an example. It also shows how to prevent future breakage with version pinning.

## What you need before starting

- **Claude Desktop** (current version installed on your Mac or Linux machine)
- An active **Google Cloud project** with OAuth 2.0 desktop app credentials (if fixing the GA MCP specifically)
- **Access to your Claude config file** at `~/Library/Application Support/Claude/claude_desktop_config.json`
- Basic familiarity with YAML syntax and environment variables
- **5–10 minutes** for diagnosis and fix (longer if creating new OAuth credentials)

## Understanding why MCP connectors break silently

If you install an MCP server with `uvx` and the `@latest` tag, `uvx` does not download a pinned version. Instead, `uvx` checks PyPI every time Claude Desktop starts and fetches the latest published version.

Third-party MCP packages (for example `mcp-google-analytics`) live on PyPI, not on your machine. Each time you start Claude, `uvx` queries PyPI for a newer version and installs it without notice. If the new version changes the API, adds new scopes, or changes authentication, your old credentials and configuration can stop working.

> **This is not a Claude Desktop update.** Claude itself does not change. A third-party developer published a new version of their MCP package. `uvx @latest` installed it without notice to you.

On May 1st, a new version of `mcp-google-analytics` added features that need the Google Analytics Admin API in addition to the Data API. The Admin API needs the `analytics.edit` scope. The existing refresh token had only the `analytics.readonly` scope. When Claude called the Admin API method, Google's OAuth server rejected the request: **`ACCESS_TOKEN_SCOPE_INSUFFICIENT` (403).**

## Diagnosing a broken MCP: three checks

**Check 1: Look for error messages in Claude Desktop's console**

Open Claude Desktop. If your MCP is broken, the chat or the debug output can show an error. The most common signature is:

```
ACCESS_TOKEN_SCOPE_INSUFFICIENT
```

This error means the access token your MCP uses does not have permission for the task.

**Check 2: Verify the refresh token has the right scopes**

For the Google Analytics MCP, your refresh token must include the `analytics.readonly` scope. If you created the token before the MCP update, and the new version added Admin API calls, the token is now insufficient.

You cannot see token scopes directly in your config file. Google's OAuth server stores them. To verify the scopes, create a new token with an explicit scope declaration.

**Check 3: Check the MCP package version in your config**

Open `~/Library/Application Support/Claude/claude_desktop_config.json` and find the MCP server entry. Look for the `args` line:

```json
"args": ["mcp-google-analytics@latest"]
```

If you see `@latest`, your MCP can update automatically without warning. This setting is the root cause of silent breakage.

## Fixing the GA MCP connector: step-by-step

### Step 1: Create new OAuth credentials in Google Cloud

Go to [Google Cloud Console](https://console.cloud.google.com/). Create a new project, or use an existing one.

Go to **APIs & Services** → **Credentials**. Click **+ Create Credentials** → **OAuth client ID** → **Desktop app**.

Download the JSON file. It contains your **client_id** and **client_secret**.

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

A browser window opens. Sign in with the Google account that owns your Analytics property. Approve access when the prompt appears. The script prints your new refresh token. **Copy this value.**

> **Why `analytics.readonly` and not `analytics.edit`?** The GA Data API (for data queries) needs only read access. You do not need the Admin API unless you manage GA properties, accounts, or create new properties. For most users, `analytics.readonly` is enough.

### Step 3: Update your Claude config with new credentials

Open `~/Library/Application Support/Claude/claude_desktop_config.json` in your text editor. Find your MCP server entry. If the entry is missing, create one:

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
- **`YOUR_REFRESH_TOKEN`** — the token you printed in Step 2
- **`YOUR_PROPERTY_ID`** — your Google Analytics GA4 property ID (for example `465530700`)

> **Note the version pinning.** This example uses `@0.0.3` instead of `mcp-google-analytics@latest`. This choice is intentional. See the next section.

### Step 4: Restart Claude Desktop and test

Close Claude Desktop completely. Reopen it. In your chat, try a simple query:

```
Get me the active users and sessions for the last 7 days.
```

If the MCP is fixed, you see data. If `ACCESS_TOKEN_SCOPE_INSUFFICIENT` appears again, check that you created the refresh token with the correct scopes. Also check that you restarted Claude after you updated the config.

## Preventing future breakage: pin your package version

The root cause of the May 1st breakage was `@latest`. Every time Claude starts, `uvx` queries PyPI. If a new version exists, `uvx` installs it without notice. If that new version has breaking changes, your MCP breaks without warning.

**Replace `@latest` with a specific version number.**

Instead of:

```json
"args": ["mcp-google-analytics@latest"]
```

Use:

```json
"args": ["mcp-google-analytics@0.0.3"]
```

> **What version should I use?** Check [PyPI](https://pypi.org/project/mcp-google-analytics/) for the latest stable version. As of May 2026, `0.0.3` is stable. Replace `0.0.3` with the current version.

**Trade-offs:**

| Using `@latest` | Using a pinned version |
|---|---|
| Automatic updates (convenience) | No automatic updates (stability) |
| Risk of silent breakage | You control when to upgrade |
| Immediate access to latest features | Possible delay in security patches |
| Requires investigation when broken | Requires manual version bump |

**For production use or daily automation, pin the version.** The extra step is worth the reliability, even if it delays access to new features.

## Troubleshooting

**Error: `ACCESS_TOKEN_SCOPE_INSUFFICIENT`**

Cause: Your refresh token does not have the `analytics.readonly` scope.
Fix: Create a new token. Follow Step 2 above. Make sure the SCOPES list includes `https://www.googleapis.com/auth/analytics.readonly`.

**Error: `Invalid Credentials` or `Unauthorized`**

Cause: Your `CLIENT_ID`, `CLIENT_SECRET`, or `PROPERTY_ID` is incorrect.
Fix: Check each value in your config against your Google Cloud Console. Restart Claude after you make changes.

**Error: `Property not found`**

Cause: Your `PROPERTY_ID` does not exist, or it is not linked to your Google account.
Fix: Log into Google Analytics and verify the property ID. Find it in **Admin** → **Property Settings** → **Property ID**.

**Error: MCP still not working after restart**

Cause: Claude caches the config and can fail to reload it right away.
Fix: Close Claude completely. Wait 5 seconds. Reopen Claude. If possible, avoid a force-quit. A clean shutdown helps the config reload.

## What you can do now

If you pinned the version, your GA MCP is now stable and does not break without warning. You can now:

- **Query Google Analytics data** directly in Claude: "What's my top traffic source this week?"
- **Build automation** that reliably fetches GA data as part of a larger workflow
- **Set up regular reports** with scheduled Claude sessions that pull GA metrics

Next steps: If you have multiple GA properties, add them as separate MCP server entries in your config. Use a different `env` section for each property. If you use other MCP tools from PyPI (for example Google Sheets or WordPress), apply the same version pinning pattern to prevent similar silent breakage.

## Related reading on The Science Talk

This guide accompanies the [complete GA4 MCP setup guide on The Science Talk](https://thesciencetalk.com/news/connect-google-analytics-ga4-claude-desktop-mcp/), which walks through the initial installation step by step from scratch. That post assumes no prior MCP experience. This post focuses on troubleshooting and on preventing breakage after initial setup.

---

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
