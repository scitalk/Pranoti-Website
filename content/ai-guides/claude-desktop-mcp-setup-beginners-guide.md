---
title: "Claude Desktop MCP Setup: A Beginner's Guide"
date: 2026-04-10
lastmod: 2026-04-10
draft: false
description: "Learn how to install Claude Desktop and connect your first MCP server — no coding background needed. Step-by-step for macOS and Windows."
keywords: ["Claude Desktop MCP setup", "MCP server", "Model Context Protocol", "install MCP server", "AI automation setup", "claude_desktop_config.json", "Claude Desktop beginners"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["Claude Desktop", "MCP", "Model Context Protocol", "AI setup", "automation"]
category: "ai-integration-guides"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com and MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
---

Claude Desktop becomes significantly more useful once you connect it to MCP servers — tools that give Claude access to your files, apps, and workflows directly from the chat interface. This guide covers everything you need to get Claude Desktop installed and your first MCP server connected, even if you have never edited a configuration file before.

## What you need before starting

- A computer running macOS or Windows (Claude Desktop is not available on Linux)
- Around 15–20 minutes
- An Anthropic account (free tier works)
- For most MCP servers: [Node.js](https://nodejs.org) installed (LTS version recommended)

> **Check Node.js first.** Open your terminal (macOS: search "Terminal" in Spotlight; Windows: press Windows + R, type `cmd`, press Enter) and run `node --version`. If you see a version number like `v20.x.x`, you are ready. If not, download the LTS version from nodejs.org before continuing.

---

## Step 1: Download and install Claude Desktop

Go to [claude.com/download](https://claude.com/download) and download the installer for your operating system.

- **macOS:** Open the `.dmg` file and drag Claude to your Applications folder.
- **Windows:** Run the `.exe` installer and follow the prompts.

Once installed, open Claude Desktop and sign in with your Anthropic account. You will see a standard chat interface — this is your starting point.

> Claude Desktop and the Claude.ai browser interface are separate products. MCP connections are only available in the desktop app, not the browser.

---

## Step 2: Understand what MCP servers do

MCP stands for **Model Context Protocol** — an open standard that lets Claude connect to external tools and data sources running on your machine (or hosted remotely).

Without MCP, Claude works only with text you paste into the conversation. With an MCP server connected, Claude can read files from your computer, query a spreadsheet, interact with your calendar, push content to your website, and more — with your explicit approval for each action.

Each MCP server is a small background process. Claude Desktop launches it automatically when you start the app, based on a configuration file you set up once.

---

## Step 3: Locate the configuration file

Claude Desktop reads its MCP settings from a file called `claude_desktop_config.json`. To open it:

1. In Claude Desktop, click the **Claude** menu in your system menu bar (macOS: top of screen; Windows: top of the app window)
2. Select **Settings…**
3. In the Settings window, click the **Developer** tab in the left sidebar
4. Click **Edit Config**

This opens the configuration file — or creates it if it does not exist yet. The file lives at:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

If the file is new, it will be empty or contain `{}`. That is expected.

---

## Step 4: Add your first MCP server

The most straightforward MCP server to start with is the **Filesystem server** — it gives Claude access to specific folders on your computer.

Open `claude_desktop_config.json` in a text editor (VS Code, Notepad, TextEdit) and replace the contents with the following:

**macOS:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/Desktop",
        "/Users/YOUR_USERNAME/Documents"
      ]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\YOUR_USERNAME\\Desktop",
        "C:\\Users\\YOUR_USERNAME\\Documents"
      ]
    }
  }
}
```

Replace `YOUR_USERNAME` with your actual computer username. The folder paths in `args` define which directories Claude can access — add or remove paths as needed.

> **Only grant access to folders you are comfortable with Claude reading and modifying.** Start narrow — Desktop and Documents is a sensible default. You can always expand later.

Save the file.

---

## Step 5: Restart Claude Desktop and verify

Close Claude Desktop completely (on macOS: right-click the Dock icon → Quit; on Windows: close the window and check the system tray).

Reopen it. After restarting, look for a **hammer icon** (🔨) in the bottom-right corner of the chat input box. Click it — you should see a list of tools provided by the Filesystem server, such as `read_file`, `write_file`, `list_directory`, and `search_files`.

If the hammer icon appears: your MCP server is connected and ready.

---

## Step 6: Add a second MCP server (optional but recommended)

Once you are comfortable with the config file structure, adding more servers follows exactly the same pattern — add another entry inside `"mcpServers"`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/Desktop"
      ]
    },
    "second-server-name": {
      "command": "npx",
      "args": ["...", "..."]
    }
  }
}
```

Each server gets its own key inside `mcpServers`. Restart Claude Desktop after every change to the config file.

Popular next steps from here: connecting Google Sheets, your WordPress site, or your email. See the related guides linked in the sidebar.

---

## Troubleshooting

**The hammer icon does not appear after restarting**
Check your `claude_desktop_config.json` for JSON syntax errors — a missing comma or bracket will prevent the server from loading. Paste the file contents into [jsonlint.com](https://jsonlint.com) to validate it.

**"npx is not recognised" error (Windows)**
Node.js may not be on your system PATH. Reinstall Node.js from nodejs.org, making sure to tick "Add to PATH" during installation. Then restart your computer before trying again.

**Claude says it cannot access a file I expect it to reach**
The file is probably outside the folders listed in your config. Add the folder path to the `args` array in `claude_desktop_config.json` and restart Claude Desktop.

**The server connects but Claude is not using it**
Ask Claude directly: "What tools do you have access to?" — this prompts it to list connected MCP tools and confirms the connection is active.

---

## What you can do now

With your first MCP server connected, Claude Desktop can:

- List and read files in your specified folders: *"Show me all .pdf files in my Documents folder from the last 30 days"*
- Create and save documents: *"Write a meeting summary and save it to my Desktop as meeting-notes.md"*
- Search across your files: *"Find any file containing the phrase 'project proposal'"*

Each action requires your approval — Claude will ask before reading or writing anything.

From here, the most useful next steps are connecting Claude to the specific tools you already use every day: spreadsheets, your website, your calendar. The guides in the sidebar cover those connections in detail.

---

## Related reading on The Science Talk

This guide is the entry point for MCP setup. From here, the next step is connecting Claude to specific tools — including a detailed walkthrough of [connecting Claude Desktop to Google Sheets](https://thesciencetalk.com/news/ai-integration-use-cases/connect-claude-desktop-google-sheets-mcp-guide/) and [connecting a self-hosted WordPress site to Claude Desktop](/ai-guides/connect-wordpress-claude-desktop-mcp-guide/).

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
