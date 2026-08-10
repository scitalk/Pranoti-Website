---
title: "How to Build a Custom Bookkeeping App with Claude Cowork"
date: 2026-07-20
lastmod: 2026-07-20
slug: "build-bookkeeping-app-claude-cowork-google-sheets"
draft: false
description: "Build a free, custom bookkeeping app with Claude Cowork, Next.js and Google Sheets as the database — replace paid software without hiring a developer."
keywords: ["build a bookkeeping app with Claude Cowork", "build a custom app with Claude", "no-code app with AI", "Google Sheets as a database", "Claude Cowork Next.js tutorial", "free bookkeeping app freelancers", "Vercel Next.js deployment", "freelancer bookkeeping tool"]
author: "Pranoti Kshirsagar"
reading_time: "7 min"
tags: ["Claude Cowork", "Next.js", "Google Sheets", "Vercel", "freelancer tools"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "How to Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Custom Claude Integration for Google Workspace: Google Sheets MCP"
    url: "/case-studies/google-sheets-mcp/"
  - title: "How to Automate Event Registration with Stripe, Make.com and MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
---

Most paid bookkeeping tools charge a monthly fee for features a freelancer rarely uses. Examples are multi-user accounts, invoicing modules, and integrations you will never touch. This guide shows you how to build a bookkeeping app with Claude Cowork instead. The app is free and custom. It uses Next.js and Google Sheets as the database, deploys on Vercel, and locks behind a PIN so only you can use it. You do not need to be a developer. You need a few free accounts, an hour of focused setup, and Claude Cowork to do the actual coding.

The pattern here is not limited to bookkeeping. When you understand how to build a custom app with Claude Cowork that reads and writes to a real Google Sheet, you can apply the same approach to time tracking, inventory logs, client CRMs, or any workflow currently trapped in a spreadsheet that needs a proper interface.

## What you need before starting

- **Claude Cowork** — Claude's conversational build environment, used for the whole build described here
- A **free GitHub account** for version control and deployment triggers
- A **free Vercel account** (Hobby plan — no card required) for hosting and secret storage
- A **Google Cloud project** with the Google Sheets API enabled, for OAuth credentials
- An existing or new **Google Sheet** to act as your database
- Basic comfort running terminal commands. You will not write code by hand, but you will run the commands Claude Cowork gives you.

> This guide uses Next.js with the App Router and TypeScript. The underlying pattern (Sheets as database, OAuth for secure access, Vercel for hosting) works with any framework Claude Cowork supports.

## Step 1: Set up your accounts and API credentials

Create your Google Cloud project first. Then enable the **Google Sheets API** from the API library. Inside that project, create an **OAuth Client ID** of type "Web application". Add `http://localhost:3000/api/auth/callback` as an authorized redirect URI.

> If you have had a frustrating experience with Google **service accounts**, use an **OAuth Client** instead. A service account needs an explicit share on every sheet it touches. It behaves like a separate "user" with its own permission quirks. An OAuth Client authenticates as *you*, against your own Google account. This is simpler for a single-user app like this one.

Save your `Client ID` and `Client Secret`. You will need these as environment variables shortly. If you want to connect Claude directly to a sheet for analysis instead of building an app, see [how to connect Claude Desktop to Google Sheets via MCP](/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/). This is a lighter-weight option covered in a separate guide.

## Step 2: Design your data model in a real spreadsheet

Before you write any code, set up the Google Sheet that will act as your database. Create one tab for each type of record (for example, `Expenses` and `Income`). Add a tab that defines your categories (for example, `Category List`) so the app can read them dynamically instead of using hardcoded values.

> Duplicate your real spreadsheet into a **test copy** before development starts. Point your app at the test copy's ID until you trust the result. This is the most important habit in this whole build. It stops a bug in your code from corrupting real financial data.

## Step 3: Build your bookkeeping app with Claude Cowork

Open your project folder in Claude Cowork. Describe the app in plain language: a PIN-gated form that takes an amount, a vendor, and a category from your sheet's category tab, then saves the entry as a new row. Claude Cowork will build a Next.js project with TypeScript, create the folder structure, and write the components.

Ask Claude Cowork to break the flow into clear steps instead of one long form. For example, use an amount/vendor screen, then a category picker, then a confirm-and-save screen. This keeps each screen focused and makes the app faster to use on a phone, which matters if you log expenses while away from your desk.

## Step 4: Connect Google Sheets securely

Most tutorials skip this step, so do it properly. Your app needs a **refresh token** to talk to the Sheets API on your behalf, without you logging in again every time. Ask Claude Cowork to write a small one-time script. The script must run the OAuth flow locally and print a refresh token to your terminal.

Store the resulting values in a `.env.local` file. **Never commit this file to GitHub.**

```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REFRESH_TOKEN=your_refresh_token
SPREADSHEET_ID=your_test_spreadsheet_id
APP_PIN=your_chosen_pin
```

If a `.gitignore` file does not exist, add one that excludes `.env.local`. Confirm it works with `git status` before your first commit. You must see `.env.local` listed as ignored, not staged. See the [Next.js environment variables documentation](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables) for how these values load at build and runtime.

Your API route must check the PIN on every request, not only at login. Serverless functions do not hold session state between calls the way a traditional server does.

## Step 5: Test locally against your test spreadsheet

Run the app locally. Click through the full flow: enter an expense, save it, and confirm the row appears correctly in your **test spreadsheet**, not your real one. Check that:

- Categories load from the sheet, not from hardcoded data
- The saved row lands in the correct columns with the correct format
- The PIN gate blocks access without the correct PIN

> Verify the `SPREADSHEET_ID` in `.env.local` before every write during testing. This is the one value in this whole build that, if wrong, can silently corrupt real data instead of test data.

## Step 6: Deploy to Vercel

After local testing passes, push your repository to GitHub as a **private repo**. This app touches your financial data, so it must not be public. Then import the repository into [Vercel](https://vercel.com), which detects the Next.js framework automatically.

In the Vercel project's environment variables settings, add every value from your `.env.local` file. This time, point `SPREADSHEET_ID` at your **real** spreadsheet, not the test copy. Deploy the app. Then open the live URL on your phone and add it to your home screen so it behaves like a native app.

## Troubleshooting

**OAuth redirect URI mismatch.** The redirect URI in your Google Cloud OAuth Client must match exactly what your app requests, including the port number. If you change ports locally, update the registered URI too.

**Sheets API returns a permissions error.** With an OAuth Client, this usually means the refresh token was generated against the wrong Google account. It can also mean the token expired because the OAuth consent screen is still in "Testing" mode, which gives a short token lifespan. Regenerate the token and confirm you are logged into the correct account.

**Environment variables not read after you edit `.env.local`.** Next.js reads this file only at server start. Stop and restart `npm run dev` after any change.

**Data appears in the wrong spreadsheet.** Always check `SPREADSHEET_ID` first. This is the most common cause of "my data disappeared" panic. It is almost always set to the wrong sheet.

## What you can do now

You have replaced a recurring software subscription with a free, custom app that runs on infrastructure you control. From here, this same Claude Cowork and Google Sheets pattern extends naturally:

- Add a **reports view** that reads your Sheets data back and shows monthly totals or category breakdowns
- Add **CSV import** to load historical transactions in bulk
- Add **receipt scanning**, using an AI vision model to fill in the amount and vendor automatically from a photo

Each of these is a new conversation with Claude Cowork, where you describe the feature. The account setup, data model, and deployment pipeline you already built stay exactly the same.

## Related reading on The Science Talk

This same pattern, Claude reading and writing to a live Google Sheet, also works without you building an app at all. See [how to use Claude to analyze survey data in Google Sheets](https://thesciencetalk.com/news/claude-google-sheets-survey-data-analysis/) for a lighter-weight example, if a full deployed app is more than your use case needs.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
