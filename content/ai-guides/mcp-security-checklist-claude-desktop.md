---
title: "MCP Security Checklist for Claude Desktop Users"
date: 2026-05-09
lastmod: 2026-05-09
slug: "mcp-security-checklist-claude-desktop"
draft: false
description: "A practical MCP security checklist for anyone using Claude Desktop professionally — credential storage, server trust, scope control, and subprocess protection covered."
keywords: ["MCP security checklist Claude Desktop", "MCP credential storage", "Claude Desktop MCP trust", "secure MCP server installation", "macOS Keychain Claude secrets", "MCP subprocess credential scoping", "MCP security professionals"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["MCP", "Claude Desktop", "security", "credentials", "AI tool access"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "MCP Security in Claude Code: What Full Machine Access Really Involves"
    url: "/perspectives/claude-code-mcp-credential-security/"
  - title: "Model Context Protocol for Non-Developers: A Practical Primer"
    url: "/ai-guides/model-context-protocol-non-developers/"
  - title: "Claude Desktop MCP Setup: A Beginner's Guide"
    url: "/ai-guides/claude-desktop-mcp-setup-beginners-guide/"
---

MCP servers extend what Claude can do. They connect it to your files, databases, analytics tools, and third-party services. Before you install one, understand what you actually hand over and what a basic security check looks like in practice. This guide covers the five checks that matter most, written for anyone who uses Claude Desktop professionally, regardless of technical background.

## What you are actually installing

An MCP (Model Context Protocol) server is a piece of software that runs locally on your machine and gives Claude tools to interact with external systems. When you install one, Claude can use it to read files, call APIs, query databases, or take actions in connected apps.

**Anthropic does not audit or approve MCP servers.** The ecosystem has over 10,000 published servers as of 2026. The majority are community-developed and lightly reviewed. Installing an MCP server is closer to installing a browser extension than downloading software from an app store. You trust the author directly.

The security model is simple. The MCP server runs as you, with your permissions, on your machine.

---

## Check 1: Where are your credentials stored?

Most MCP setup guides instruct you to paste API keys directly into a configuration file called `claude_desktop_config.json`. This file lives at:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Open it and look for any line containing a key, token, password, or secret stored as plain text. A typical insecure pattern looks like this:

```json
{
  "mcpServers": {
    "my-tool": {
      "env": {
        "API_KEY": "sk-live-abc123youractualkey"
      }
    }
  }
}
```

**Plain text in this file is a risk.** The file is not encrypted. It can sync via cloud backup. It can end up in version control if you store your dotfiles in a Git repository.

The safer approach is to use your operating system's secure credential store:

- **macOS:** Store secrets in Keychain Access. Reference them in your terminal via `security find-generic-password`, or use a Keychain-backed MCP wrapper to surface them to Claude directly.
- **Windows:** Use Credential Manager. Access stored credentials via `cmdkey` in the command line.

Some MCP servers also support marking fields as `"sensitive": true` in their manifest. When supported, Claude Desktop routes those values through OS-level secure storage automatically. Check the documentation for any server you install.

> **Practical step:** Open your `claude_desktop_config.json` now. Move any value that looks like a key, token, or password out of plain text before you continue.

---

## Check 2: Does this MCP server deserve your trust?

Before you install any MCP server, run through these four questions:

**Where does it come from?**
Prefer servers published by the tool vendor directly (for example, the official Stripe MCP, the official GitHub MCP) or by known community maintainers with a public track record. Be cautious with servers that have no linked repository, no author identity, or no usage history.

**Is it actively maintained?**
Check the repository's last commit date. An MCP server that has not been updated in six months can have unpatched vulnerabilities or break silently as Claude Desktop updates.

**What permissions does it request?**
Read the server's documentation before you install. If an MCP server only needs to read data, it must not request write permissions. If a database MCP asks to connect as a superuser, treat that as a red flag. It must use a read-only role scoped to the minimum it needs.

**Does the source code exist and is it readable?**
For open-source servers, scan the repository for hardcoded credentials, unusual network calls, or code that reads and transmits file contents. You do not need to be a developer to spot a block of code that sends data to an unfamiliar endpoint.

> Research from 2026 found that approximately 3% of MCP servers in production contain hardcoded credentials designed to function as credential theft traps. The risk is small but real, especially with servers distributed through unofficial channels.

---

## Check 3: What can Claude see on your machine?

By default, Claude Desktop can only use the tools that your installed MCP servers provide. It does not have blanket access to your file system unless you install a filesystem MCP server.

If you install a filesystem MCP, or any MCP that accesses local files, check what root path it points at. A server configured to read `~/Documents` has access to everything in that folder, including any credentials, client data, or personal files stored there.

**Scope what each server can reach.** Claude Desktop's `claude_desktop_config.json` is global. Every server listed under `mcpServers` is available in every conversation, with no per-project isolation. (Project-scoped MCP configuration is a Claude Code feature, not a Claude Desktop one. Do not confuse the two if you use both.) Since Claude Desktop has no built-in way to limit a server to specific conversations, treat every server you add as always-on and scope its *own* permissions accordingly:

- Point filesystem servers at the narrowest folder they actually need, not your whole home directory
- Use read-only database roles and API scopes wherever the server supports them
- Remove servers you only test once you finish, rather than leave them installed indefinitely

Reserve installation for tools you trust fully and expect to use regularly. Claude Desktop has no "sandboxed for one project" middle ground today.

---

## Check 4: Are credentials leaking into subprocesses?

Each MCP server Claude Desktop launches runs as its own subprocess, with the environment variables you defined for it in `claude_desktop_config.json`. The risk is not your entire shell environment leaking in by default. It is the opposite mistake: putting more into a server's `env` block than that specific server needs, so every tool call it makes can see credentials unrelated to its job.

Keep each server's `env` entry minimal, with only the keys that server actually requires, rather than reuse one broad set of credentials across multiple `mcpServers` entries. If you also use Claude Code, note that `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is a Claude Code setting for its Bash tool and hooks. It has no effect on Claude Desktop, which does not run a general-purpose shell tool.

> If you store API keys or tokens as shell environment variables for other tools, do not assume Claude Desktop automatically isolates MCP servers from them. Check each server's own documentation for how it reads credentials.

---

## Check 5: What have you already installed?

If you have used Claude Desktop with MCP servers for a while, audit what currently runs.

Open your `claude_desktop_config.json` and list every entry under `mcpServers`. For each one, ask:

- Do I still use this?
- Do I know what credentials it holds?
- Is it still maintained?

Remove any server you no longer actively use. Unused MCP servers create an unnecessary attack surface. They hold credentials and run code even when you are not thinking about them.

For servers you keep, check whether you have rotated their credentials recently. Regenerate API keys that have not been rotated in over a year and revoke the old keys.

---

## Your security baseline: a quick-reference checklist

Use this before every new MCP server installation:

**Before installing**
- [ ] Source is identifiable — vendor, known maintainer, or public repository
- [ ] Repository is actively maintained (recent commits)
- [ ] Permissions requested match what the tool actually needs
- [ ] No hardcoded credentials or suspicious network calls in the source code

**Credential storage**
- [ ] No API keys or tokens stored in plain text in `claude_desktop_config.json`
- [ ] Sensitive values stored in macOS Keychain or Windows Credential Manager
- [ ] Each server's `env` block contains only the credentials that specific server needs

**Scope and access**
- [ ] Filesystem MCP servers scoped to the minimum required folder path
- [ ] Client or project-specific servers installed in local scope, not global
- [ ] Global-scope servers limited to general tools you trust fully

**Ongoing maintenance**
- [ ] Quarterly review of all installed MCP servers
- [ ] Unused servers removed promptly
- [ ] Credentials rotated at least annually

---

## What you can do now

Running through this checklist takes under thirty minutes for most setups. The highest-impact actions are moving plain-text credentials to Keychain, enabling subprocess environment scrubbing, and removing MCP servers you no longer use.

Security with AI tools is not about avoiding them. It is about knowing what you have installed and making deliberate choices about access. The checklist above gives you a repeatable baseline to return to as your setup evolves.

## Related reading on The Science Talk

- [How to Connect Claude Desktop to Google Sheets via MCP](https://thesciencetalk.com/news/connect-claude-desktop-google-sheets-mcp-guide/), a setup guide including OAuth credential configuration
- [How to Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP](https://thesciencetalk.com/news/connect-wordpress-claude-desktop-mcp-guide/), covering application password setup for WordPress MCP

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
