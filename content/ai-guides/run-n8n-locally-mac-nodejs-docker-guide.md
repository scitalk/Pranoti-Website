---
title: "How to Run n8n Locally on Mac: Node.js and Docker Setup Guide"
date: 2026-06-21
lastmod: 2026-06-21
slug: "run-n8n-locally-mac-nodejs-docker-guide"
draft: false
description: "Install and run n8n locally on your Mac using Node.js or Docker. Migrate workflows from n8n Cloud, connect to Claude, and automate without limits."
keywords: ["run n8n locally on Mac", "install n8n Mac", "n8n Docker macOS setup", "n8n Node.js install", "n8n Cloud migration", "n8n Claude integration", "workflow automation self-hosted"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["n8n", "automation", "Docker", "Node.js", "self-hosting"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "How to Automate Event Registration with Stripe, Make.com and MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
  - title: "Build an AI-Powered Content Workflow for a Billion-Euro Industry"
    url: "/ai-guides/ai-content-workflow-billion-euro-industry/"
  - title: "Model Context Protocol for Non-Developers: A Practical Primer"
    url: "/ai-guides/model-context-protocol-non-developers/"
---

Running n8n locally on your Mac gives you unlimited workflow executions, full data control, and the ability to test automations before you deploy anywhere. n8n Cloud starts at €24 per month for 2,500 executions. Running it locally costs nothing beyond your existing hardware. This guide covers two installation paths (Node.js and Docker), migrating your existing Cloud workflows, connecting n8n to Claude, and the most common errors you will encounter.

## What you need to run n8n locally on Mac

- macOS 12 Monterey or later
- Node.js v20.19 or higher (Option 1), download from [nodejs.org](https://nodejs.org/)
- Docker Desktop for Mac (Option 2), download from [docker.com](https://www.docker.com/products/docker-desktop)
- Terminal access (built into macOS; search "Terminal" in Spotlight)
- 10-15 minutes

> **Which option should you choose?** Node.js is faster to set up and ideal for trying n8n for the first time. Docker is the better long-term choice. Your data persists reliably, updates are simpler, and it matches how you deploy n8n in production.

## Option 1: Install n8n via Node.js

### Step 1: Install Node.js

Download the **LTS** version from [nodejs.org](https://nodejs.org/) and run the macOS installer. Once complete, verify the installation in Terminal:

```bash
node --version
npm --version
```

Both commands must return a version number. n8n requires Node.js **v20.19 or higher** to run correctly.

### Step 2: Install n8n globally

```bash
npm install n8n -g
```

This installs n8n as a global command on your system. The download is around 300-400 MB and can take a few minutes depending on your connection.

### Step 3: Start n8n

```bash
n8n
```

n8n starts and prints output in your Terminal. Open your browser and go to:

```
http://localhost:5678
```

### Step 4: Create your account

The first time you open n8n locally, it prompts you to create an owner account with an email and password. n8n stores this locally. It sends no data to n8n servers.

> **Important:** Each time you want to use n8n, run `n8n` in Terminal first. The instance only runs while the Terminal session is active.

---

## Option 2: Install n8n via Docker

Docker runs n8n in an isolated container and keeps your workflow data safe between restarts. This is the recommended approach if you plan to use n8n regularly.

### Step 1: Install Docker Desktop

Download Docker Desktop for Mac from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) and install it. Open Docker Desktop and wait until the status indicator shows it is running before you continue.

### Step 2: Run the n8n container

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

Open your browser and go to `http://localhost:5678` to access n8n.

### Step 3: What each Docker flag does

| Flag | What it does |
|------|-------------|
| `-it` | Runs the container in interactive mode so you can see live logs in Terminal |
| `--rm` | Removes the container automatically when you stop it |
| `-p 5678:5678` | Maps port 5678 on your Mac to port 5678 inside the container |
| `-v ~/.n8n:/home/node/.n8n` | Saves all workflows, credentials, and settings to `~/.n8n` on your Mac |

The `-v` flag is the most important one. Without it, all your data disappears the moment the container stops running.

### Step 4: Access and set up n8n

The first-launch flow is identical to Option 1: create an owner account, then build and run workflows from `http://localhost:5678`.

---

## Migrate your workflows from n8n Cloud

If you have existing workflows on n8n Cloud, export and import them individually.

**Export from n8n Cloud:**

1. Go to [app.n8n.cloud](https://app.n8n.cloud/) and open a workflow
2. Click the **gear icon** in the top right corner
3. Select **Export**
4. Save the JSON file to your Mac

**Import to your local instance:**

1. Open your local n8n at `http://localhost:5678`
2. Click **Import** in the workflow editor
3. Select the JSON file you exported

Repeat for each workflow. Exports do not include credentials. Re-enter API keys and connection details in your local instance after you import.

---

## Connect n8n to Claude and other AI tools

n8n has a native Anthropic integration that lets you send prompts to Claude and use the responses as part of any workflow.

**Set up a Claude credential:**

1. In your local n8n, go to **Credentials** → **New Credential**
2. Search for **Anthropic** and select it
3. Enter your API key from [console.anthropic.com](https://console.anthropic.com/)
4. Save the credential

**Use Claude in a workflow:**

Add an **AI Agent** node or **Anthropic Chat Model** node to your canvas and select the credential you just created. Claude can then summarize content, classify data, draft text, or take action based on what upstream nodes send it.

> n8n added MCP (Model Context Protocol) support in early 2026. If you run Claude Desktop alongside your local n8n instance, the n8n MCP server lets you build and manage workflows directly from a Claude conversation, without opening the n8n editor at all.

---

## Troubleshooting

**`Error: listen EADDRINUSE :::5678` — port already in use**

Something else is occupying port 5678. Find and stop it:

```bash
lsof -i :5678
kill -9 <PID>
```

Replace `<PID>` with the process ID shown in the output. Alternatively, run n8n on a different port:

```bash
N8N_PORT=8080 n8n
```

**`n8n: command not found`**

The global npm install did not add n8n to your shell PATH. Run:

```bash
npm install n8n -g
export PATH="$PATH:$(npm prefix -g)/bin"
```

Add the `export` line to your `~/.zshrc` file to make it permanent across Terminal sessions.

**Docker container exits immediately**

Check the container logs for the cause:

```bash
docker logs $(docker ps -lq)
```

If the logs show a permission error on `~/.n8n`, fix it with:

```bash
sudo chown -R 1000:1000 ~/.n8n
```

**Workflows do not save between sessions**

If you started Docker without the `-v` flag, data is not being persisted. Stop the container and restart it with the full command from Step 2 above.

---

## Back up and maintain your local instance

All n8n data, including workflows, credentials, execution history, and the encryption key that protects your credentials, lives in `~/.n8n` on your Mac.

**Back up before every update:**

```bash
cp -r ~/.n8n ~/n8n-backup-$(date +%Y%m%d)
```

**Update n8n (Node.js install):**

```bash
npm update n8n -g
```

**Update n8n (Docker):**

```bash
docker pull n8nio/n8n
```

Then restart the container using the same command from Step 2.

---

## What you can do now

You now have a fully local n8n instance running on your Mac. Your data persists between sessions, and the instance is ready to connect to your existing tools and API credentials.

Try three things next:

- **Automate content workflows.** Pull from an RSS feed, summarize each article with Claude, and post the output to WordPress or Notion.
- **Build a personal AI assistant.** Trigger Claude via webhook from a form, email, or Slack message and route the response wherever it needs to go.
- **Test before deploying.** Build and validate complex multi-step automations locally, then move them to a cloud n8n instance or production server when ready.

## Related reading on The Science Talk

This guide pairs well with the [workflow automation walkthrough on The Science Talk](https://thesciencetalk.com/ai-academy/event-registration-automation-stripe-make-mailerlite/), a practical example of connecting Stripe, Make.com, and MailerLite that shows how the same automation-first thinking applies across different tool combinations.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
