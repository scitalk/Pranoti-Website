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
pillar: "AI Adoption"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com and MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
sidebar_product:
  label: "DIGITAL GUIDE"
  title: "Claude Connected to Google Sheets via MCP"
  bullets:
    - "Step-by-step OAuth 2.0 setup"
    - "Service account + password authentication patterns"
    - "5 ready-to-use integration examples"
  details:
    - "Instant PDF delivery"
    - "Email setup support"
  stripe_url: "https://buy.stripe.com/9B614n7699puePn0jm8Ra0o?utm_source=pranoti_site&utm_medium=sidebar&utm_campaign=claude_sheets_mcp"
  cta: "Get the guide — €12 →"
  footnote: "Complete setup guide"
---

Claude Desktop becomes much more useful when you connect it to MCP servers. MCP servers are tools that give Claude access to your files, apps, and workflows directly from the chat interface. This guide shows you how to install Claude Desktop and connect your first MCP server. You do not need experience with configuration files.

## What you need before starting

- A computer running macOS or Windows (Claude Desktop is not available on Linux)
- Around 15–20 minutes
- An Anthropic account (free tier works)
- For most MCP servers: [Node.js](https://nodejs.org) installed (LTS version recommended)

> **Check Node.js first.** Open your terminal. On macOS, search for "Terminal" in Spotlight. On Windows, press Windows + R, type `cmd`, and press Enter. Run `node --version`. If you see a version number like `v20.x.x`, you are ready. If not, download the LTS version from nodejs.org before you continue.

---

## Step 1: Download and install Claude Desktop

Go to [claude.com/download](https://claude.com/download) and download the installer for your operating system.

- **macOS:** Open the `.dmg` file and drag Claude to your Applications folder.
- **Windows:** Run the `.exe` installer and follow the prompts.

Once installed, open Claude Desktop and sign in with your Anthropic account. You will see a standard chat interface. This is your starting point.

> Claude Desktop and the Claude.ai browser interface are separate products. MCP connections are only available in the desktop app, not the browser.

---

## Step 2: Understand what MCP servers do

MCP stands for **Model Context Protocol**. It is an open standard. It lets Claude connect to external tools and data sources on your machine or on a remote host.

Without MCP, Claude works only with text you paste into the conversation. With an MCP server connected, Claude can read files from your computer, query a spreadsheet, interact with your calendar, push content to your website, and do more. Claude asks for your approval before each action.

Each MCP server is a small background process. Claude Desktop starts it automatically when you open the app, based on a configuration file you configure once.

---

## Step 3: Locate the configuration file

Claude Desktop reads its MCP settings from a file called `claude_desktop_config.json`. To open it:

1. In Claude Desktop, click the **Claude** menu in your system menu bar (macOS: top of screen; Windows: top of the app window)
2. Select **Settings…**
3. In the Settings window, click the **Developer** tab in the left sidebar
4. Click **Edit Config**

This opens the configuration file. If the file does not exist yet, Claude Desktop creates it. The file location is:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

If the file is new, it will be empty or contain `{}`. That is expected.

---

## Step 4: Add your first MCP server

The **Filesystem server** is the simplest MCP server to start with. It gives Claude access to specific folders on your computer.

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

Replace `YOUR_USERNAME` with your actual computer username. The folder paths in `args` define which directories Claude can access. Add or remove paths as needed.

> **Only grant access to folders you trust Claude to read and change.** Start narrow. Desktop and Documents is a good default. You can expand access later.

Save the file.

---

## Step 5: Restart Claude Desktop and verify

Close Claude Desktop completely. On macOS, right-click the Dock icon and select Quit. On Windows, close the window and check the system tray.

Reopen it. After the restart, look for a **hammer icon** (🔨) in the bottom-right corner of the chat input box. Click it. You should see a list of tools from the Filesystem server, such as `read_file`, `write_file`, `list_directory`, and `search_files`.

If the hammer icon appears, your MCP server is connected and ready.

---

## Step 6: Add a second MCP server (optional but recommended)

After you learn the config file structure, you can add more servers the same way. Add another entry inside `"mcpServers"`:

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

Popular next steps include connecting Claude to Google Sheets, your WordPress site, or your email. See the related guides in the sidebar.

---

## Troubleshooting

**The hammer icon does not appear after restarting**
Check your `claude_desktop_config.json` for JSON syntax errors. A missing comma or bracket prevents the server from loading. Paste the file contents into [jsonlint.com](https://jsonlint.com) to check it.

**"npx is not recognised" error (Windows)**
Node.js can be missing from your system PATH. Reinstall Node.js from nodejs.org. During installation, select "Add to PATH". Then restart your computer and try again.

**Claude says it cannot access a file I expect it to reach**
The file is probably outside the folders listed in your config. Add the folder path to the `args` array in `claude_desktop_config.json` and restart Claude Desktop.

**The server connects but Claude is not using it**
Ask Claude directly: "What tools do you have access to?" This prompts Claude to list connected MCP tools and confirms the connection is active.

---

## What you can do now

With your first MCP server connected, Claude Desktop can:

- List and read files in your specified folders: *"Show me all .pdf files in my Documents folder from the last 30 days"*
- Create and save documents: *"Write a meeting summary and save it to my Desktop as meeting-notes.md"*
- Search across your files: *"Find any file containing the phrase 'project proposal'"*

Each action requires your approval. Claude asks before it reads or writes anything.

From here, the most useful next step is to connect Claude to the tools you already use every day: spreadsheets, your website, your calendar. The guides in the sidebar cover those connections in detail.

---

## Related reading on The Science Talk

This guide is the entry point for MCP setup. The next step is to connect Claude to specific tools. See the detailed walkthrough for [connecting Claude Desktop to Google Sheets](https://thesciencetalk.com/ai-academy/connect-claude-desktop-google-sheets-mcp-guide/) and for [connecting a self-hosted WordPress site to Claude Desktop](/ai-guides/connect-wordpress-claude-desktop-mcp-guide/).

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
