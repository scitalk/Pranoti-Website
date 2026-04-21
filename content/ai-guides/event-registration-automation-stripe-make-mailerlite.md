---
title: "How to Automate Event Registration with Stripe, Make.com and MailerLite"
date: 2026-04-04
lastmod: 2026-04-04
draft: false
description: "Build a fully automated event registration workflow using Stripe, Make.com and MailerLite. Step-by-step guide — no manual work, no missed onboarding emails."
keywords: ["event registration automation", "Stripe Make.com MailerLite", "automate webinar registration", "Make.com Stripe webhook", "MailerLite automation trigger", "no-code event workflow"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["Stripe", "Make.com", "MailerLite", "automation", "event registration"]
category: "ai-integration-guides"
sidebar_links:
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Connect Your Self-Hosted WordPress Site to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Restore a Single WordPress Page from a WP Engine Backup"
    url: "/ai-guides/restore-wordpress-page-wpengine-backup/"
---

Knowledge workers running multiple paid online events — workshops, webinars, guidance sessions — spend a disproportionate amount of time on registration admin: manual emails, spreadsheet updates, copy-pasting registrant details. This guide documents a clean, reliable automated registration pipeline using Stripe, Make.com, and MailerLite that eliminates that overhead entirely. Every paid registration triggers a full onboarding sequence automatically, from payment confirmation to inbox — without any manual steps after the initial build.

## What you will have at the end

By the end of this setup, every paid registration will automatically trigger a complete onboarding experience. The moment a payment clears in Stripe, Make.com catches it, identifies which event the registrant purchased, and tells MailerLite to add them to the correct group and fire the right automation sequence.

Your registrant receives an onboarding email within seconds of paying. You get the data, the revenue, and none of the admin.

## What you need before starting

- **A Stripe account** — with at least one active payment link or product set up
- **A Make.com account** — the free plan supports this workflow
- **A MailerLite account** — with at least one group and one automation created
- **A MailerLite API key** — found in your MailerLite account settings under Integrations

> **Scope note:** This guide covers the core registration-to-onboarding flow. It does not include cancellation handling, refund webhooks, or multi-currency routing — those are separate workflow extensions you can add once the base scenario is working.

## The stack

Three tools connected in sequence:

- **Stripe** — payment processing and the trigger point for the entire workflow
- **Make.com** (free plan) — the automation layer connecting Stripe to MailerLite
- **MailerLite** — subscriber management and automated email sequences

Make.com sits entirely in the backend. Your registrant moves from your landing page to the Stripe checkout to their inbox. The automation runs invisibly in between.

## The workflow logic

The Make.com scenario has **2 modules and 1 filter**:

- **Module 1 (Stripe)** — watches for new events
- **Filter** — passes only successful payments through
- **Router** — directs each registration to the correct MailerLite group based on which event was purchased
- **Module 2 (MailerLite)** — creates or updates the subscriber, adds them to the group, and triggers the automation

> **Why the Router matters:** Without a Router, you would need a separate Make.com scenario for every single event. The Router is what makes this setup scalable — once in place, **adding a new event takes less than five minutes**. You simply add a new route with the new group name.

## Step-by-step setup

### Step 1: Set up your Stripe payment link with metadata

The key to routing registrations to the correct MailerLite group is **Stripe metadata**. In your Stripe dashboard, go to **Payment Links → Create a link**. Under Advanced options, find the **Metadata** section and add:

- **Key:** `Mailerlite_Group`
- **Value:** the exact name of your MailerLite group (e.g. `Your_Event_Name_Month_Year`)

Do this for every event payment link. The value must match your MailerLite group name exactly — spelling, capitalisation, underscores.

### Step 2: Create your MailerLite group and automation

In MailerLite, go to **Subscribers → Groups → Add Group**. Name it to match exactly what you put in your Stripe metadata. Then build your automation: go to **Automations → Create automation**, set the trigger to **"When subscriber is added to a group"**, and select your new group.

**Activate the automation before you go live** — Make.com will add the subscriber correctly, but the automation only fires if it is active at the moment they are added.

### Step 3: Create the Make.com scenario

Log into Make.com and click **Create a new scenario**. Add Module 1 — search for Stripe and select **Watch Events**. Connect your Stripe account and set the event type to **Payment Intent**. Make.com will generate a webhook URL — copy it.

Then go to your **Stripe dashboard → Developers → Webhooks → Add endpoint**, paste the URL, and select **payment_intent.succeeded** as the event to listen to.

### Step 4: Add the filter

Between Module 1 and Module 2, click the small circle on the connection line to **add a filter**. Set two conditions using the token picker (always pick from the dropdown — never type manually):

- **Condition 1:** `data → object → payment_status` equals `paid`
- **Condition 2:** `data → object → metadata → Mailerlite_Group` exists

Set both with **AND logic**.

> **Token picker tip.** Make.com flattens Stripe's data structure visually. Manually typed field paths often reference the wrong context and silently fail. Always navigate through the dropdown — it takes 30 extra seconds and saves hours of debugging.

### Step 5: Add the Router

After the filter, add a **Router** module. For each Route, set a filter:

- Left side: `metadata → Mailerlite_Group`
- Operator: Equal to
- Right side: the group name for that route

When you add a new event in the future, you simply **add a new Route** to this Router. The rest of the scenario stays untouched.

### Step 6: Add Module 2 — MailerLite: create or update subscriber

At the end of each Route, add a **MailerLite Classic: Create or Update Subscriber** module. Connect your MailerLite account via API key and map the fields:

- **Email** → `receipt_email`
- **Name** → `shipping → name`
- **Group** → select from dropdown
- **Autoresponders** → **Yes**
- **Resubscribe** → **No**

> **Critical setting:** **Autoresponders: Yes** is the single most important setting in this entire workflow. Without it, the subscriber gets added to the group but the automation does not fire. The onboarding email never sends. Double-check this before you test.

### Step 7: Test the full flow

Click **Run once** in Make.com, then make a test payment via your Stripe payment link using a test card (no real charge). Watch each module show a green tick. Check MailerLite — the test subscriber should appear in the correct group with the automation active.

If the filter blocks the event, confirm your Stripe metadata key is spelled exactly as `Mailerlite_Group` and the group name matches precisely.

### Step 8: Activate the scenario

Once the test passes, **toggle the scenario to ON** using the switch at the bottom left of the scenario editor. Make.com will now watch for Stripe events continuously — no action required. Every paid registration triggers the full flow automatically from this point forward.

## What you can do now

With this workflow active, you can:

- **Add a new event in under five minutes** — create the Stripe link with new metadata, create the MailerLite group and automation, add a Route in Make.com
- **Run multiple events simultaneously** with zero extra admin — each Router route handles its own group independently
- **Track conversion data directly in Stripe** — see payment volume, drop-off at checkout, and revenue per event
- **Personalise every onboarding sequence per event** — each MailerLite automation is independent and fully customisable
- **Resubscribe returning registrants safely** — the Resubscribe: No setting prevents duplicate sequences without losing the subscriber record

## Troubleshooting

**Filter blocking all events**

Almost always caused by incorrect token mapping. Delete both filter conditions and re-add them fresh by navigating through the token picker: `Stripe → Raw Webhook Data → data → object → payment_status`. Never type paths manually.

**Subscriber added but automation does not fire**

Check two things: confirm **Autoresponders is set to Yes** in the MailerLite module, and confirm the automation is **active** in MailerLite. A paused or draft automation will not trigger even when subscribers are added correctly.

**Wrong group receiving the registration**

The Stripe metadata value and the MailerLite group name must be **identical** — same capitalisation, same underscores, no spaces. A mismatch means the Router filter lets the event through to the wrong route or no route at all.

**How to check Make.com logs**

In your scenario, click **History** in the left panel. Each run shows a full trace — which modules processed, what data passed through, and where it stopped. **Always check the logs before changing your scenario config** — the error message tells you exactly what went wrong.

---
## Related reading on The Science Talk

This guide accompanies the [full event registration automation post on The Science Talk](https://thesciencetalk.com/event-registration-automation-stripe-make-mailerlite/) — covering the context behind building this workflow, the decisions made along the way, and how it fits into a broader no-code automation stack.

*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
