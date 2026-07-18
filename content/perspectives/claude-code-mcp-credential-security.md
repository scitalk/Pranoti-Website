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

I've been building local MCP servers — a way to give Claude direct access to my Google Analytics, Google Sheets, and WordPress site, so I can run reports and manage content without switching tools. It's genuinely powerful. It's also the reason I spent yesterday rotating every credential on my machine.

Let me tell you what I found out the hard way.

## What Claude can access when you give it tool access

When you run Claude Code — Anthropic's CLI tool — on your machine, it runs as you. Not a sandboxed version of you. Not a restricted subprocess. You.

That means:

- It can read any file your user account can read
- It can write, modify, or delete any file you can write
- It can run shell commands — anything you could type in Terminal
- It can make network requests
- It has no mandatory filesystem boundary by default

I discovered this when I asked Claude to help me configure some credential files. It did exactly what I asked. It read the files, wrote the configuration, and helped me build the servers. What I hadn't fully reckoned with: **every file it reads becomes part of the conversation context, and that context goes to Anthropic's servers.**

In one session, Claude had read:

- My WordPress application password (plaintext, in a JSON file)
- My Google OAuth refresh tokens for Sheets and Analytics
- My Claude Desktop config file containing all my API credentials

Not maliciously. Not sneakily. I asked it to. I approved each tool call. But the result was the same: those credentials were now in a third party's logs.

## The permission prompts — what they actually protect

Claude Code does show you a prompt before executing tool calls. You see "reading this file" or "running this command" and you can approve or deny.

This is real protection. But it has limits.

The prompts show you **what is happening, not why it matters.** When you're in flow, building something, the instinct is to keep approving. And once you approve reading a credential file, the contents are already in context — no second prompt asks whether it's okay to include that in the data sent to Anthropic.

There's also no allowlist by default. The permission system doesn't say "Claude can only read files in this folder." If Claude has a reason to read `~/.ssh/id_rsa`, it can ask to. If you approve it, it reads it.

> **Note:** Anthropic has introduced a sandboxing feature that lets you define which directories and network hosts Claude can access — reducing unsolicited permission prompts by 84% in internal testing. This is worth configuring, but it is opt-in, not the default.

For power users doing serious work — running reports, managing databases, deploying code — the default setup is the reality most people are operating in.

## Who should care most

**Solopreneurs:** You likely run everything through one machine, one account. Your Google credentials, payment processor keys, client data, and domain registrar login might all be on that filesystem. Claude doesn't distinguish between files you meant to share and files you didn't.

**Scientists and researchers:** Lab data, unpublished results, IRB-sensitive participant data. If any of it sits on a machine where Claude Code runs, it can be read. Institutional review boards have almost certainly not contemplated this access model — and the EU AI Act's provisions on high-risk AI systems are only beginning to reach this territory.

**Companies:** If developers are using Claude Code on machines with production database credentials, AWS keys, or customer PII — you need a policy. Not a preference. A policy. What can Claude read? What can it run? Who approves what? [Research by Astrix Security](https://astrix.security/learn/blog/state-of-mcp-server-security-2025/) found that 53% of MCP server deployments rely on long-lived static credentials — credentials that persist as a risk indefinitely after any compromise.

## What "getting ugly" actually looks like

It's not a dramatic breach. It's quieter than that.

You're building something useful. You ask Claude to help configure a server. It reads a credentials file to understand the format. You don't think twice — it needs to see the structure. But now those credentials are in Anthropic's infrastructure.

You ask Claude to debug why something isn't connecting. It runs a test command. The command output includes an error message with a database URL and a connection string embedded in it. That goes to Anthropic too.

You're doing legitimate work. Claude is being helpful. And somewhere in that process, **the blast radius of a future Anthropic security incident just got wider.**

The credentials I rotated were all perfectly functional credentials that Claude had a legitimate reason to see. That's what makes this hard. The risk doesn't require anyone to do anything wrong.

## What I'm doing about it

After a proper audit of what happened in that session, I took these steps:

**1. Rotate first, ask questions later.**
Any credential Claude read, I rotated. WordPress application password, Google OAuth tokens — all of them. A rotated credential that was leaked is harmless. An unrotated one that was leaked is not.

**2. Move secrets to macOS Keychain.**
Keychain is the one credential store on a Mac that Claude cannot read silently. Accessing it requires an explicit shell call (`security find-generic-password`) that shows up as a visible, deniable tool call. I'm migrating all secrets there.

**3. Separate Claude's role from credential access.**
Claude writes the code. I supply the credential values. Claude doesn't need to see the actual token — only the structure of the JSON file it reads. This is a discipline change, not a technical one, but it matters.

**4. New session hygiene.**
Each new Claude Code session starts fresh. Credentials from a previous session aren't automatically re-exposed. I'm keeping sessions shorter and more focused, with a clear scope before I start.

**5. Revoke and reissue the API key.**
The API key Claude Code was using on my machine — revoked. Fresh key, issued after I'd rotated everything else. Belt and suspenders.

## The fair counterpoint

None of this means Claude Code is dangerous or that you shouldn't use it. I still use it. The productivity it enables — for the kind of solo infrastructure work I do — is real.

What it means is that **the mental model most users bring ("it's just a chat interface") is wrong once you add tool access.** You are giving a very capable, very fast process the same permissions you have. That's not a bug — it's the point. It's why it can actually do useful things.

But it requires the same intentionality you'd bring to giving SSH access to a contractor. What can they see? What can they run? What's the blast radius if something goes wrong? Those are questions worth answering before you need them, not after.

---

**Claude with tool access is not a chat interface. It's a process running as you. Treat it accordingly.**

If you're working through this at your organisation or on your own setup — [get in touch →](/contact/)

## If you found this useful

- [MCP Security Checklist for Claude Desktop Users](/ai-guides/mcp-security-checklist-claude-desktop/) — the practical five-check checklist: credential storage, server trust, scope control, and subprocess protection
- [Native Connector vs. MCP: Which Google Sheets Integration Does Your Workflow Actually Need?](/perspectives/google-sheets-claude-integration-comparison-2026/) — the security and capability trade-offs between Claude's two Sheets integration paths
- [Model Context Protocol for Non-Developers: A Practical Primer](/ai-guides/model-context-protocol-non-developers/) — what MCP actually is, and what it means when you connect it to your tools

---
*Browse all [Perspectives](/perspectives/) or [get in touch →](/contact/)*
