---
title: "Connect Google Analytics GA4 to Claude Desktop via MCP"
date: 2026-05-01
lastmod: 2026-05-01
slug: "connect-google-analytics-ga4-claude-desktop-mcp"
draft: false
description: "Connect your GA4 property to Claude Desktop using the Google Analytics MCP server. Query traffic and performance data in plain English, without leaving Claude."
keywords: ["connect Google Analytics GA4 Claude Desktop MCP", "Google Analytics MCP server", "GA4 MCP setup", "Claude Desktop MCP configuration", "analytics-mcp pipx", "GA4 Claude integration", "monitor website performance Claude", "google-analytics-mcp install"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["google-analytics", "MCP", "claude-desktop", "GA4", "website-analytics"]
category: "ai-integration-guides"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "How to Find Content Gaps Using Clarity and Google Search Console"
    url: "/ai-guides/content-gap-analysis-clarity-gsc/"
  - title: "WordPress MCP Setup Guide"
    url: "/products/wordpress-mcp-setup-guide/"
---

Once the Google Analytics MCP server is connected to Claude Desktop, you can query your GA4 data in plain English — no dashboards, no tab-switching, no exports. Ask Claude for your top pages this week, your traffic by source, or your session counts by country, and get the answer directly in your conversation.

This guide covers the complete setup: enabling the right Google Cloud APIs, authenticating with your Google account, installing the MCP server via pipx, and adding it to Claude Desktop. It also shows how this connection feeds directly into combined workflows — including the [clarity-insights-and-seo skill](/ai-guides/) for cross-referencing behaviour data with your analytics.

---

## What you need before starting

- **Claude Desktop** installed on your Mac (download from [claude.ai/download](https://claude.ai/download))
- **Python 3.10 or higher** — check with `python3 --version` in Terminal
- **Homebrew** — the Mac package manager (install from [brew.sh](https://brew.sh) if needed)
- **pipx** — installs Python tools in isolated environments (installed in Step 2)
- **Google Cloud CLI (gcloud)** — used to authenticate with Google (installed in Step 2)
- **A Google account** with access to the GA4 property you want to connect
- **A Google Cloud project** — free to create at [console.cloud.google.com](https://console.cloud.google.com)

> **Scope note:** This guide uses the official [googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp) server, which runs locally on your machine. Your GA4 data is never sent to a third party — it goes directly from Google's API to Claude Desktop.

---

## Set up Google Cloud and authentication

### Step 1: Enable the Google Analytics APIs in Google Cloud Console

The MCP server uses two Google APIs to read your analytics data. Both need to be enabled in your Google Cloud project before authentication will work.

Go to [Google Cloud Console](https://console.cloud.google.com) and select your project (or create a new one — a free project is fine).

Enable the **Google Analytics Admin API**:
- Navigate to [APIs & Services → Library](https://console.cloud.google.com/apis/library)
- Search for **Google Analytics Admin API**
- Click **Enable**

Then enable the **Google Analytics Data API**:
- Search for **Google Analytics Data API**
- Click **Enable**

> Both APIs must be enabled. The Admin API gives Claude access to your account and property structure. The Data API is what runs reports and returns traffic data.

Note your **Google Cloud Project ID** — you'll need it in Step 5. Find it in the top bar of Google Cloud Console (format: `my-project-123456`).

---

### Step 2: Install pipx and the gcloud CLI

Open **Terminal** and run the following commands.

**Install pipx** (runs Python tools in isolated environments):

```bash
brew install pipx
pipx ensurepath
```

**Install the Google Cloud CLI**:

```bash
brew install --cask google-cloud-sdk
```

After installation, initialise gcloud:

```bash
gcloud init
```

Follow the prompts — sign in with your Google account and select the Cloud project you enabled the APIs on. This links your local gcloud tool to the right project.

---

### Step 3: Set up your Google credentials with Application Default Credentials

The MCP server authenticates using **Application Default Credentials (ADC)** — a standard Google authentication method that stores credentials locally and passes them to any tool that needs them.

You'll need an **OAuth client credentials file** from your Google Cloud project. To create one:

1. Go to **APIs & Services → Credentials** in Google Cloud Console
2. Click **Create Credentials → OAuth client ID**
3. Select **Desktop app** as the application type
4. Name it (e.g. `analytics-mcp-desktop`) and click **Create**
5. Click **Download JSON** — save the file somewhere accessible, e.g. `~/Downloads/client_secret.json`

Now run the authentication command in Terminal, pointing to that file:

```bash
gcloud auth application-default login \
  --scopes https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform \
  --client-id-file=~/Downloads/client_secret.json
```

A browser window will open. Sign in with the Google account that has access to your GA4 property and grant the requested permissions.

When complete, Terminal will print a line like:

```
Credentials saved to file: [/Users/your-username/.config/gcloud/application_default_credentials.json]
```

**Copy this full path.** You will need it in the next step.

> The `analytics.readonly` scope gives read-only access to your GA4 data. The MCP server cannot modify your analytics configuration.

---

## Connect to Claude Desktop

### Step 4: Add the Google Analytics MCP to Claude Desktop

Open the Claude Desktop configuration file. In Claude Desktop, go to **Settings → Developer → Edit Config** — this opens `claude_desktop_config.json` in your default text editor.

Add the following block inside the `mcpServers` object. If you already have other MCP servers configured (e.g. Google Sheets, WordPress), add this alongside them:

```json
{
  "mcpServers": {
    "analytics-mcp": {
      "command": "pipx",
      "args": ["run", "analytics-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/Users/your-username/.config/gcloud/application_default_credentials.json",
        "GOOGLE_PROJECT_ID": "your-cloud-project-id"
      }
    }
  }
}
```

Replace the two values:

- **`GOOGLE_APPLICATION_CREDENTIALS`** — paste the full path printed by the gcloud command in Step 3
- **`GOOGLE_PROJECT_ID`** — your Google Cloud project ID (e.g. `my-project-123456`)

Save the file.

> If your `claude_desktop_config.json` already has an `mcpServers` block, add the `"analytics-mcp"` entry inside the existing object — do not create a second `mcpServers` block.

---

### Step 5: Restart Claude Desktop and verify the connection

Fully quit Claude Desktop (**Cmd + Q**) and reopen it. This is required — the config is only read on startup.

To confirm the MCP is running, go to **Settings → Developer**. You should see **analytics-mcp** listed with a green **Running** status.

Test the connection by typing a natural-language query in any Claude conversation:

```
What Google Analytics properties do I have access to?
```

Claude will call `get_account_summaries` and return a list of your GA4 accounts and properties. Once you can see your property name, the connection is working.

---

## Query your GA4 data

### Step 6: Run your first GA4 report

With the connection verified, you can query your GA4 data directly. The MCP server supports plain English queries — Claude handles the translation to GA4 API parameters automatically.

A few queries to try:

**Top pages by sessions this week:**
```
Show me my top 10 pages by sessions for the past 7 days
```

**Traffic by source:**
```
What were my top traffic sources last month, by sessions?
```

**Real-time visitors:**
```
How many active users do I have on my site right now?
```

**Engagement by device:**
```
Break down my sessions by device category for the past 30 days
```

> When Claude asks which property to use, paste your **GA4 Property ID** — a numeric ID found in your GA4 account under **Admin → Property Settings**. It looks like `123456789`. You can also ask Claude to list your properties first using `get_account_summaries`.

---

## What you can do now

Your GA4 data is now available inside every Claude conversation. The connection enables three immediate capabilities.

**Monitor website performance without leaving Claude.** Ask for weekly session summaries, check which posts are driving traffic, or spot drops in engagement — all in plain English, without opening GA4.

**Feed analytics data into combined workflows.** The [clarity-insights-and-seo skill](/ai-guides/) cross-references Microsoft Clarity behaviour data with Google Analytics traffic data to produce content recommendations. With this MCP connected, that skill has access to your live GA4 data automatically — no manual export needed. The [content gap analysis guide](/ai-guides/content-gap-analysis-clarity-gsc/) shows how to use that combined data to find pages worth improving.

**Connect your other tools.** If you also manage your site through [WordPress connected to Claude Desktop via MCP](/ai-guides/connect-wordpress-claude-desktop-mcp-guide/), you can cross-reference your GA4 traffic data with your post archive in the same conversation — useful for identifying which posts to update or repurpose.

**Build repeatable reporting workflows.** Ask Claude to summarise your top content by sessions, bounce rate, and engagement time each Monday morning. Once you have a query that works, you can reuse it as a prompt template or feed it into a scheduled task.

---

## Troubleshooting

**`pipx: command not found` after installation**
Run `pipx ensurepath`, then close and reopen Terminal. The path update requires a new shell session.

**`analytics-mcp` shows as not running in Claude Desktop settings**
Check that `GOOGLE_APPLICATION_CREDENTIALS` in your config points to the exact file path printed by gcloud — including the full `/Users/your-username/...` prefix. A relative path or typo will prevent the server from starting.

**`Permission denied` or `Access not configured` error**
Both the Google Analytics Admin API and Google Analytics Data API must be enabled in your Google Cloud project. Go back to Step 1 and confirm both show as **Enabled** in APIs & Services.

**Claude returns no properties**
The Google account you authenticated with in Step 3 must have at least **Viewer** access to the GA4 property. In GA4, go to **Admin → Property Access Management** and confirm your account is listed.

**`invalid_client` error during gcloud auth**
The OAuth client JSON file must be a **Desktop app** type. Web app or service account credentials will not work with this authentication flow.

---

## Related reading on The Science Talk

- [How to Connect Claude Desktop to Google Sheets via MCP](https://thesciencetalk.com/news/connect-claude-desktop-google-sheets-mcp-guide/) — the same authentication and pipx pattern applied to Google Sheets, useful if you want both data sources available in Claude simultaneously
- [How to Connect Your Self-Hosted WordPress Site to Claude Desktop](https://thesciencetalk.com/news/connect-wordpress-claude-desktop-mcp-guide/) — adding a third MCP alongside GA4 so you can cross-reference traffic data with your post archive without leaving Claude

---

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
