---
title: "Renewals: From Idea to Ready-to-Use Product, Owning the Full Product Lifecycle"
tags: ["Product Management", "Claude Code", "MVP", "Product Design"]
date: 2026-10-26
aliases: ["/case-studies/renewals-subscription-tracker/"]
draft: false
layout: "longform"
subtitle: "One clear record of every recurring payment: what it costs, how the price changed, and what renews next."
category: "Product Build"
display_category: "Product Management"
tech_stack:
  - "Python"
  - "SQLite"
  - "JavaScript"
  - "Claude Code"
---

**Date:** October 2026\
**Domain Focus:** Personal and business finance, recurring payments\
**Services:** Product discovery, data modelling, product design, scope management\
**Tools:** Python, SQLite, JavaScript, Claude Code\
**Live page:** [https://pranoti.thesciencetalk.com/products/subscription-tracker/](https://pranoti.thesciencetalk.com/products/subscription-tracker/)

---

## Executive Summary

I pay for many things on repeat: software, streaming, insurance, phone, internet, gym, rent. Each one has its own vendor, price history, VAT rate and renewal cycle. The information to manage them existed, but it was scattered across PDF invoices, Excel sheets, Google Sheets and my own notes.

I wanted one overview. When I looked for an app to give me that, none fit. So I took the idea through the full product lifecycle myself: define the problem, design the data model, build the product, set the scope, and launch it.

The result is Renewals, a working product that I use. It shows every recurring commitment in one place, with its full history, its price changes and the charges that come next.

---

## Challenge: Recurring Costs With No Single View

Every subscription is different:

- **Different vendors.** Each one bills in its own way, with its own invoices.
- **Different renewal cycles.** Monthly, yearly, every two weeks, or one-off.
- **Different VAT.** Net, VAT and gross amounts do not follow one rule.
- **Prices that change.** A plan that cost one amount three years ago costs another today, often without a clear notice.
- **Different deadlines.** Each contract has its own renewal date and its own cancellation terms.

I needed answers to practical questions. What renews in the next 30 days? What has each subscription cost me over time? When did the price go up? When did I start or cancel something? What do I pay per month and per year, in total?

The answers were somewhere in my files, but in pieces. To answer one question, I had to open several sources and combine them by hand. Nothing showed a subscription's whole life in one place.

### The wrong assumption: "Surely there is an app for this"

My first assumption was that this problem was already solved. It could not be the first time someone wanted a clear overview of their subscriptions.

There are many subscription apps. The ones I checked, such as the open-source tool Wallos and the app Renewly, focus on due dates and reminders. None gave me what I needed: the full history of each commitment, its real price changes, net, VAT and gross, and business and private costs side by side.

That assumption was wrong. Thus, I built the product myself.

---

## Solution: A Product Built Around the Record, Not the Reminder

Renewals keeps one record per recurring commitment and shows it from different angles. The solution has five parts: problem definition, data model, build, data quality rules, and scope control.

### 1. Problem definition

Before I built anything, I defined what the product must do. It must answer three questions for every recurring payment:

- **What has it cost?** Every payment, in net, VAT and gross.
- **How did it change?** Every start, price change, pause and cancellation.
- **What is next?** The upcoming charges, in a list and in a calendar.

This definition decided every later choice. Features that did not help answer these questions stayed out.

### 2. Data model

The data model is the core of the product. A simple list of subscriptions with one price cannot show history. Thus, I designed five connected parts:

- **Vendors.** Who I pay, with country, VAT ID and website.
- **Subscriptions.** What I pay for, with a category.
- **Price periods.** One entry for each price. A price change adds a new period. Old periods are never edited, so the history stays complete.
- **Status history.** Started, paused, resumed, discontinued and restarted, each with a date.
- **Payments.** What was actually charged, with net, VAT and invoice number.

With this model, the product can calculate future charges from the price periods and renewal cycles. It can also show the real price change from one period to the next.

### 3. Build

The product is a local web app. It runs on my computer, makes no internet calls, and keeps all financial data on the machine. It has five views:

- **Dashboard.** Recent changes, the next 30 days, monthly and yearly totals, and a spending chart.
- **Subscriptions.** Each commitment with its full timeline: price periods, status changes and payments.
- **Calendar.** Upcoming charges by date.
- **Payments.** Every payment in net, VAT and gross, with export to CSV.
- **Vendors.** Who I pay, for which service, and how much in total.

### 4. Data quality rules

A record is only useful when it is correct. When the sources disagreed, I set clear rules:

- **One source of truth.** The invoice decides what was charged. Other sources fill gaps only where no invoice exists.
- **No silent fixes.** Each discrepancy was listed for review, not corrected without a record.
- **Reversible steps.** A backup was made before every change to the data, so each step could be undone.

### 5. Scope control

When the product worked, new questions came quickly. Can it run on my phone? Can someone else use it? Each one meant logins, hosting, data protection work for financial data, or third-party installs.

I froze the MVP. It does the job it was designed for. More features would have added risk and maintenance without a change to the core value.

---

## Impact

### Clarity in one place

I open one dashboard and see what changed recently, what renews in the next 30 days, and what I pay per month and per year. I click any subscription and see its full story.

### Price changes made visible

Because each price period is stored, price rises are clear. Some of them I did not notice before, because no single source showed them.

### A complete history

Every start, pause and cancellation has a date. I know what I stopped, when, and what it cost while it ran.

### Full lifecycle ownership

The product went from a personal pain point to a product in daily use: problem definition, data model, build, data quality, scope and launch, with one owner.

---

## Work With Me

Many teams have a clear pain point and scattered data, but no product that connects them. Good products start with the right problem definition and a clear scope, not with features.

My name is Dr. Pranoti Kshirsagar. I take ideas from problem to working product: I define what it must do, design how it holds the data, and decide what stays out.

**Get in touch:** [https://thesciencetalk.com/contact-us/](https://thesciencetalk.com/contact-us/)
