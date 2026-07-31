---
title: "How to Rotate an Expiring GitHub Token on GitHub Pages"
date: 2026-07-14
lastmod: 2026-07-14
slug: "rotate-expiring-github-token-github-pages"
draft: false
description: "Rotate an expiring GitHub personal access token without breaking your GitHub Pages deploy — update the macOS Keychain, verify a push, then revoke the old one."
keywords: ["rotate GitHub personal access token", "expiring GitHub token", "GitHub Pages deploy", "macOS Keychain git credential", "gh CLI re-authenticate", "GitHub Actions GITHUB_TOKEN", "fine-grained personal access token"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["GitHub", "GitHub Pages", "personal access token", "macOS Keychain", "Hugo"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "MCP Security Checklist for Claude Desktop Users"
    url: "/ai-guides/mcp-security-checklist-claude-desktop/"
  - title: "MCP Security in Claude Code: What Full Machine Access Really Involves"
    url: "/perspectives/claude-code-mcp-credential-security/"
  - title: "How to Run n8n Locally on Mac: Node.js and Docker Setup Guide"
    url: "/ai-guides/run-n8n-locally-mac-nodejs-docker-guide/"
---

Your GitHub personal access token is about to expire, and your site runs on GitHub Pages. The reassuring part first: your automated deploys keep working regardless. This guide shows exactly where the token is actually used, how to rotate it, and how to revoke the old one safely — so a routine token expiry never turns into a broken site.

## What you need before starting

- A GitHub account with a repository already deploying to GitHub Pages
- Terminal access on macOS (the Keychain steps are Mac-specific)
- Permission to create tokens on your GitHub account
- About 10 minutes

> This guide assumes your site auto-deploys from a `main` branch push via GitHub Actions — the standard setup for Hugo and other static-site generators on GitHub Pages.

## Why your GitHub Pages deploy is not at risk

The single most useful thing to understand: your **personal access token never touches the deploy pipeline**. GitHub Actions authenticates with its own automatically generated `GITHUB_TOKEN`.

That token is created fresh at the start of every workflow run, scoped to that one repository, and expires the moment the run finishes. It is not your personal token, and you never manage it.

So when a workflow builds your Hugo site and publishes to the `gh-pages` branch, it uses the built-in `GITHUB_TOKEN` — not the personal token sitting in your laptop's credential store. Your expiring token has no effect on it.

> Your personal access token only matters for actions **you** run from your own machine — pushing commits, pulling, or using the `gh` CLI. Everything the server does on its own is covered by [`GITHUB_TOKEN`](https://docs.github.com/en/actions/concepts/security/github_token).

## Where your personal token is actually used

Before changing anything, confirm where the token lives. There are only three realistic places.

**1. The git remote URL.** Check whether a token is embedded directly in the remote:

```bash
git remote -v
```

A clean HTTPS remote looks like `https://github.com/your-username/your-repo.git`. If you instead see a long token string inside the URL, that is where it is stored and where it must be replaced.

**2. The macOS Keychain.** If your remote is clean, macOS is almost certainly caching your credentials through the `osxkeychain` helper. Confirm it:

```bash
git config --get credential.helper
```

If this returns `osxkeychain`, that is the one place your token is stored locally.

**3. The `gh` CLI.** If you use GitHub's command-line tool, it holds its own separate token:

```bash
gh auth status
```

If this returns `command not found`, you do not have `gh` installed and can skip its steps entirely.

## Step 1: Create the replacement token

You do not renew an existing token — you **create a new one** and swap it in. GitHub recommends [fine-grained personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), which you can limit to specific repositories and permissions.

### Create the token

1. Go to **GitHub → Settings → Developer settings → Personal access tokens**
2. Choose **Fine-grained tokens**, then **Generate new token**
3. Set an **expiration** — fine-grained tokens must expire within 366 days
4. Under **Repository access**, select only the repository your site lives in
5. Grant **Contents: Read and write** permission — enough to push commits

Copy the token immediately. GitHub shows it once and never again.

> Set a calendar reminder for a week before the new expiry date. Rotating on your own schedule is far calmer than rotating the day a push suddenly fails.

## Step 2: Update the token where macOS caches it

If a token was embedded in your remote URL (case 1 above), reset the remote to a clean HTTPS URL first:

```bash
git remote set-url origin https://github.com/your-username/your-repo.git
```

Now handle the Keychain. The simplest approach is to let the next push prompt you. First clear the stale credential:

```bash
git credential-osxkeychain erase
host=github.com
protocol=https
```

Press **Return twice** after the last line. The next time you push, git asks for your username and password — paste the **new token** as the password. macOS stores it in the Keychain automatically.

If you prefer a visual route, open **Keychain Access**, search for `github.com`, delete the existing internet-password entry, and let the next push recreate it with the new token.

## Step 3: Re-authenticate the gh CLI (if you use it)

Skip this step entirely if `gh auth status` returned `command not found`.

If you do use `gh`, refresh its authentication with the new token:

```bash
gh auth login
```

Follow the prompts, choose **HTTPS**, and paste the new token when asked. To confirm:

```bash
gh auth status
```

A green check mark confirms the CLI now holds the new token.

## Step 4: Confirm a push still deploys

Verify the new token works **before** you revoke the old one. Make a trivial change, commit, and push:

```bash
git commit --allow-empty -m "Verify token rotation"
git push
```

If the push succeeds without an authentication error, the new token is working. Open the **Actions** tab on your repository and watch the workflow run go green — that confirms the full path from your machine to a live deploy.

> The empty commit triggers your normal deploy workflow without changing any content. It is the safest possible test push.

## Step 5: Revoke the old token

Only now — with the new token confirmed working — remove the old one.

1. Go to **GitHub → Settings → Developer settings → Personal access tokens**
2. Find the expiring token in the list
3. Select **Delete** (or **Revoke**)

Revoking last means you always have one working token in place. If you revoke first and something is misconfigured, you lock yourself out of pushing until you rotate again.

## Troubleshooting

**"remote: Invalid username or password" after rotating**
The Keychain is still serving the old token. Run the `git credential-osxkeychain erase` block from Step 2, then push again and paste the new token.

**Push succeeds but Keychain still shows the old token**
You may have two entries. Open Keychain Access, search `github.com`, and delete every matching internet-password entry, then push once to recreate a single clean entry.

**"gh: command not found"**
You do not have the GitHub CLI installed. This is normal — skip Step 3 completely. It changes nothing about your deploy.

**The token expired before you rotated it**
No harm done. Your GitHub Pages site stays live because the last deploy already published, and future deploys use `GITHUB_TOKEN`. Simply create a new token (Step 1) and update the Keychain (Step 2) to restore your ability to push.

## What you can do now

You have a working replacement token, a verified deploy, and a cleanly revoked old token — with zero downtime for your site. More importantly, you now know that token expiry is a local-machine housekeeping task, not a threat to your published site.

Turn it into a routine: rotate a week before expiry, test with an empty commit, then revoke. Set the reminder once and a task that used to feel risky becomes a two-minute habit.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
