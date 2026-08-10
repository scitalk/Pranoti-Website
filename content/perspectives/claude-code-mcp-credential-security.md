---
title: "Claude Code MCP Security: What Full Machine Access Means"
date: 2026-05-06
lastmod: 2026-05-06
draft: false
description: "Claude Code MCP tool access runs with your full user permissions. Here's what I discovered about credential exposure — and the five things I changed."
keywords: ["Claude Code MCP security", "Claude Code credential security", "MCP server credential exposure", "Claude tool access permissions", "AI agent security solopreneur", "macOS Keychain Claude secrets", "Claude Code runs as you"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["Claude Code", "MCP", "security", "credentials", "AI tool access"]
category: "perspectives"
pillar: "AI Adoption"
sidebar_links:
  - title: "Native Connector vs. MCP: Which Google Sheets Integration Does Your Workflow Actually Need?"
    url: "/perspectives/google-sheets-claude-integration-comparison-2026/"
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "How to Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Model Context Protocol for Non-Developers: A Practical Primer"
    url: "/ai-guides/model-context-protocol-non-developers/"
---

I build local MCP servers. These servers give Claude direct access to my Google Analytics, Google Sheets, and WordPress site. I can run reports and manage content without switching tools. This method is powerful. It is also the reason I rotated every credential on my machine yesterday.

This article describes what I learned the hard way.

## What Claude can access when you give it tool access

When you run Claude Code, Anthropic's CLI tool, on your machine, it runs as you. It does not run as a sandboxed version of you. It does not run as a restricted subprocess. It runs as you.

That means:

- It can read any file your user account can read
- It can write, modify, or delete any file you can write
- It can run shell commands — anything you could type in Terminal
- It can make network requests
- It has no mandatory filesystem boundary by default

I discovered this when I asked Claude to help me configure some credential files. Claude did exactly what I asked. It read the files, wrote the configuration, and helped me build the servers. I did not fully understand one fact: **every file Claude reads becomes part of the conversation context. That context goes to Anthropic's servers.**

In one session, Claude read:

- My WordPress application password (plaintext, in a JSON file)
- My Google OAuth refresh tokens for Sheets and Analytics
- My Claude Desktop config file containing all my API credentials

Claude did not act maliciously or secretly. I asked it to read the files. I approved each tool call. But the result was the same. Those credentials were now in a third party's logs.

## What the permission prompts actually protect

Claude Code shows a prompt before it executes tool calls. You see messages like "reading this file" or "running this command." You can approve or deny each one.

This is real protection. But it has limits.

The prompts show you **what is happening, not why it matters.** When you work quickly on a build, the instinct is to keep approving. Once you approve a credential file for reading, the content is already in context. No second prompt asks if you want to send that data to Anthropic.

There is no allowlist by default. The permission system does not say "Claude can only read files in this folder." If Claude has a reason to read `~/.ssh/id_rsa`, it can ask to read it. If you approve the request, Claude reads the file.

> **Note:** Anthropic introduced a sandboxing feature that lets you define which directories and network hosts Claude can access. In internal testing, this feature reduced unsolicited permission prompts by 84 percent. You can configure this feature, but it is optional, not the default.

Power users do serious work: they run reports, manage databases, and deploy code. The default setup is the reality most people use.

## Who should care most

**Solopreneurs:** You likely run everything through one machine and one account. Your Google credentials, payment processor keys, client data, and domain registrar login can all be on that filesystem. Claude does not distinguish between files you meant to share and files you did not mean to share.

**Scientists and researchers:** This risk applies to lab data, unpublished results, and IRB-sensitive participant data. If any of this data sits on a machine where Claude Code runs, Claude can read it. Institutional review boards likely did not consider this access model. The EU AI Act's provisions on high-risk AI systems barely address this area yet.

**Companies:** If developers use Claude Code on machines with production database credentials, AWS keys, or customer PII, you need a policy. Not a preference. A policy. What can Claude read? What can it run? Who approves each action? [Research by Astrix Security](https://astrix.security/learn/blog/state-of-mcp-server-security-2025/) found that 53 percent of MCP server deployments rely on long-lived static credentials. These credentials stay a risk indefinitely after any compromise.

## What "getting ugly" actually looks like

It is not a dramatic breach. It is quieter than that.

You build something useful. You ask Claude to help configure a server. Claude reads a credentials file to understand the format. You do not think twice, because Claude needs to see the structure. But now those credentials are in Anthropic's infrastructure.

You ask Claude to debug why something is not connecting. Claude runs a test command. The command output includes an error message with an embedded database URL and connection string. That data goes to Anthropic too.

You do legitimate work. Claude helps you. Somewhere in that process, **the blast radius of a future Anthropic security incident grows wider.**

The credentials I rotated were all functional credentials that Claude had a legitimate reason to see. That is what makes this hard. The risk does not require anyone to do anything wrong.

## What I did about it

After a proper audit of what happened in that session, I took these steps:

**1. Rotate first, ask questions later.**
Any credential Claude read, I rotated. WordPress application password, Google OAuth tokens: all of them. A rotated credential that was leaked is harmless. An unrotated one that was leaked is not.

**2. Move secrets to macOS Keychain.**
Keychain is the one credential store on a Mac that Claude cannot read silently. To access it, Claude must make an explicit shell call (`security find-generic-password`). This call shows up as a visible, deniable tool call. I will move all secrets there.

**3. Separate Claude's role from credential access.**
Claude writes the code. I supply the credential values. Claude does not need to see the actual token. Claude needs only the structure of the JSON file it reads. This change is a discipline change, not a technical one. But it matters.

**4. New session hygiene.**
Each new Claude Code session starts fresh. Credentials from a previous session do not automatically become exposed again. I keep sessions shorter and more focused. I set a clear scope before I start each session.

**5. Revoke and reissue the API key.**
I revoked the API key Claude Code used on my machine. I issued a fresh key after I rotated everything else. This step adds an extra layer of protection.

## The fair counterpoint

None of this means Claude Code is dangerous. It does not mean you must avoid using it. I still use it. The productivity it enables for the kind of solo infrastructure work I do is real.

It means that **the mental model most users bring ("it is just a chat interface") is wrong once you add tool access.** You give a very capable, very fast process the same permissions you have. That is not a bug. It is the point. It is why Claude can do useful things.

But it requires the same care you bring when you grant SSH access to a contractor. What can they see? What can they run? What is the blast radius if something goes wrong? Answer these questions before you need them, not after.

---

**Claude with tool access is not a chat interface. It is a process that runs as you. Treat it with the same care.**

If you work through this issue at your organization or in your own setup, [get in touch →](/contact/)

## If you found this useful

- [MCP Security Checklist for Claude Desktop Users](/ai-guides/mcp-security-checklist-claude-desktop/) — the practical five-check checklist: credential storage, server trust, scope control, and subprocess protection
- [Native Connector vs. MCP: Which Google Sheets Integration Does Your Workflow Actually Need?](/perspectives/google-sheets-claude-integration-comparison-2026/) — the security and capability trade-offs between Claude's two Sheets integration paths
- [Model Context Protocol for Non-Developers: A Practical Primer](/ai-guides/model-context-protocol-non-developers/) — what MCP actually is, and what it means when you connect it to your tools

---
*Browse all [Perspectives](/perspectives/) or [get in touch →](/contact/)*
