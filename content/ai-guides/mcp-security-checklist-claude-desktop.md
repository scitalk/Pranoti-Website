---
title: "MCP Security Checklist for Claude Desktop Users"
date: 2026-05-09
lastmod: 2026-05-09
slug: "mcp-security-checklist-claude-desktop"
draft: false
description: "A practical MCP security checklist for anyone using Claude Desktop professionally — credential storage, server trust, scope control, and subprocess protection covered."
keywords: ["MCP security checklist Claude Desktop", "MCP credential storage", "Claude Desktop MCP trust", "secure MCP server installation", "macOS Keychain Claude secrets", "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB", "MCP security professionals"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["MCP", "Claude Desktop", "security", "credentials", "AI tool access"]
category: "ai-integration-guides"
sidebar_links:
  - title: "I Gave Claude Full Access to My Machine. Here's What That Actually Means."
    url: "/perspectives/claude-code-mcp-credential-security/"
  - title: "Model Context Protocol for Non-Developers: A Practical Primer"
    url: "/ai-guides/model-context-protocol-non-developers/"
  - title: "Claude Desktop MCP Setup: A Beginner's Guide"
    url: "/ai-guides/claude-desktop-mcp-setup-beginners-guide/"
---

MCP servers extend what Claude can do — connecting it to your files, databases, analytics tools, and third-party services. Before you install one, it is worth understanding what you are actually handing over and what a basic security check looks like in practice. This guide covers the five checks that matter most, written for anyone using Claude Desktop professionally, regardless of technical background.

## What you are actually installing

An MCP (Model Context Protocol) server is a piece of software that runs locally on your machine and gives Claude tools to interact with external systems. When you install one, Claude can use it to read files, call APIs, query databases, or take actions in connected apps.

**Anthropic does not audit or approve MCP servers.** The ecosystem has over 10,000 published servers as of 2026, the majority community-developed and lightly reviewed. Installing an MCP server is closer to installing a browser extension than downloading software from an app store — you are trusting the author directly.

The security model is simple: the MCP server runs as you, with your permissions, on your machine.

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

**Plain text in this file is a risk.** The file is not encrypted, it may sync via cloud backup, and it can end up in version control if you store your dotfiles in a Git repository.

The safer approach is to use your operating system's secure credential store:

- **macOS:** Store secrets in Keychain Access. Reference them in your terminal via `security find-generic-password` or use a tool like [Keychain Secure MCP](https://mcpmarket.com/tools/skills/keychain-secure) to surface them to Claude directly.
- **Windows:** Use Credential Manager. Access stored credentials via `cmdkey` in the command line.

Some MCP servers also support marking fields as `"sensitive": true` in their manifest — when supported, Claude Desktop routes those values through OS-level secure storage automatically. Check the documentation for any server you install.

> **Practical step:** Open your `claude_desktop_config.json` now. Any value that looks like a key, token, or password should be moved out of plain text before you continue.

---

## Check 2: Does this MCP server deserve your trust?

Before installing any MCP server, run through these four questions:

**Where does it come from?**
Prefer servers published by the tool vendor directly (e.g. the official Stripe MCP, the official GitHub MCP) or by known community maintainers with a public track record. Be cautious with servers that have no linked repository, no author identity, or no usage history.

**Is it actively maintained?**
Check the repository's last commit date. An MCP server that has not been updated in six months may have unpatched vulnerabilities or break silently as Claude Desktop updates.

**What permissions does it request?**
Read the server's documentation before installing. If an MCP server only needs to read data, it should not be requesting write permissions. If a database MCP asks to connect as a superuser, that is a red flag — it should use a read-only role scoped to the minimum it needs.

**Does the source code exist and is it readable?**
For open-source servers, scan the repository for hardcoded credentials, unusual network calls, or code that reads and transmits file contents. You do not need to be a developer to spot a block of code that sends data to an unfamiliar endpoint.

> Research from 2026 found that approximately 3% of MCP servers in production contain hardcoded credentials designed to function as credential theft traps. The risk is small but real — especially with servers distributed through unofficial channels.

---

## Check 3: What can Claude see on your machine?

By default, Claude Desktop can only use the tools that your installed MCP servers provide. It does not have blanket access to your file system unless you have installed a filesystem MCP server.

If you have installed a filesystem MCP — or any MCP that accesses local files — check what root path it is pointed at. A server configured to read `~/Documents` has access to everything in that folder, including any credentials, client data, or personal files stored there.

**Scope your installations by project.** Claude Desktop supports local-scope MCP configuration, which loads a server only in the context of a specific project and stores the config in `~/.claude.json` rather than the global file. Use local scope for:

- Servers that access sensitive client data
- Servers whose credentials you do not want shared across projects
- Experimental servers you are testing

**Global scope** (the default `claude_desktop_config.json`) makes a server available in every conversation. Reserve global scope for general-purpose tools you trust fully and use daily.

---

## Check 4: Are credentials leaking into subprocesses?

When Claude Desktop runs tools — including MCP servers, the bash tool, and hooks — it spawns child processes. By default, those child processes inherit the environment variables of the parent process, which can include any credentials you have set as environment variables in your shell.

The fix is a single environment variable:

```bash
CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1
```

Setting this strips credentials from the subprocess environment before any child process is launched. To enable it permanently on macOS, add it to your shell profile:

```bash
# In ~/.zshrc or ~/.bash_profile
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1
```

Then restart your terminal and Claude Desktop.

> This setting is particularly important if you store API keys or tokens as shell environment variables. Without it, any MCP server running as a subprocess can read those values.

---

## Check 5: What have you already installed?

If you have been using Claude Desktop with MCP servers for a while, it is worth auditing what is currently running.

Open your `claude_desktop_config.json` and list every entry under `mcpServers`. For each one, ask:

- Do I still use this?
- Do I know what credentials it holds?
- Is it still maintained?

Remove any server you no longer actively use. Unused MCP servers are an unnecessary attack surface — they hold credentials and run code even when you are not thinking about them.

For servers you keep, check whether their credentials have been rotated recently. API keys that have not been rotated in over a year should be regenerated and the old keys revoked.

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
- [ ] `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` set in shell profile

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

Security with AI tools is not about avoiding them — it is about knowing what you have installed and making deliberate choices about access. The checklist above gives you a repeatable baseline to come back to as your setup evolves.

## Related reading on The Science Talk

- [How to Connect Claude Desktop to Google Sheets via MCP](https://thesciencetalk.com/news/connect-claude-desktop-google-sheets-mcp-guide/) — setup guide including OAuth credential configuration
- [How to Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP](https://thesciencetalk.com/news/connect-wordpress-claude-desktop-mcp-guide/) — covers application password setup for WordPress MCP

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
