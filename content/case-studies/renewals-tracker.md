---
title: "Renewals: Launching a New Product from Gap to Market"
tags: ["Product Management", "Claude Code", "MVP", "Product Design"]
date: 2026-10-26
aliases: ["/case-studies/renewals-subscription-tracker/"]
draft: false
layout: "longform"
subtitle: "Conceiving, architecting, and shipping a zero-to-one financial management tool to a live, testable release."
category: "Product Build"
display_category: "0-to-1 Product Management"
tech_stack:
  - "Python"
  - "SQLite"
  - "JavaScript"
  - "Claude Code"
---

| Metadata | Details |
| --- | --- |
| **Product Initiative** | New Product Development (Zero-to-One) |
| **Role** | Solo Product Lead & Builder (Market Discovery, Schema Architecture, UX, Execution, GTM) |
| **Status** | Launched, Functional & Publicly Accessible |
| **Date** | October 2026 |
| **Domain** | Personal & Business Finance |
| **Stack** | Python, SQLite, JavaScript, Claude Code |
| **Live Product** | [Renewals Product Page & Live Demo](https://pranoti.thesciencetalk.com/products/subscription-tracker/) |

---

## Executive Summary

Managing recurring liabilities across SaaS, digital tools, telecommunications, insurance, and professional services is an operational blind spot for modern professionals and small business operators. While transaction records exist, they are scattered across vendor portals, PDF invoices, and disconnected spreadsheets, obscuring true historical expenditure and impending liabilities.

I initiated, scoped, architected, and shipped **Renewals**, an original, standalone product built to resolve this fragmentation. Rather than building another notification reminder, I identified an underserved market segment needing high-fidelity financial auditability, modeled an append-only relational schema, enforced strict MVP scope boundaries, and deployed a live, functional product that anyone can test.

This case study demonstrates my approach to **full-lifecycle product ownership**: discovering unaddressed market whitespace, formulating product strategy, designing data foundations, managing scope trade-offs, and driving technical execution from blank canvas to a publicly available release.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       FULL PRODUCT LIFECYCLE MAP                        │
├─────────────────┬──────────────────┬──────────────────┬─────────────────┤
│   1. DISCOVERY  │   2. STRATEGY    │   3. EXECUTION   │    4. LAUNCH    │
│                 │                  │                  │                 │
│ • User Friction │ • Value Prop     │ • Normalized DB  │ • Zero-Bloat    │
│ • Competitor    │ • Strict Scope   │ • Local-First UX │   MVP Cut       │
│   Teardowns     │   Guardrails     │ • Audit Quality  │ • Public Web    │
│ • Market Gap    │ • Core Metrics   │   Protocols      │   Deployment    │
└─────────────────┴──────────────────┴──────────────────┴─────────────────┘
```

---

## Phase 1: Opportunity Discovery & Market Gap Analysis

### 1. The Operational Problem

Managing 15 to 40 recurring commitments across dual personal and business profiles creates five systemic friction points:

* **Asynchronous billing cycles:** Irregular intervals (monthly, quarterly, biennial, bespoke multi-year).
* **Tax attribution friction:** Inconsistent handling of Net, Gross, and local VAT rates across cross-border vendors.
* **Undetected price creep:** Periodic contract indexations and silent tier upgrades executed without transparent notifications.
* **Dynamic contract lifecycles:** Services shifting between active, paused, negotiated, and discontinued states.
* **Renewal trap exposure:** Notice-period deadlines buried in contractual fine print.

The critical user insight was behavioral: users do not struggle to remember *when* to pay; they struggle to audit *what has changed*, *what was spent historically*, and *how tax impacts overall cash flow*.

### 2. Competitive Teardown & The "Off-the-Shelf" Fallacy

To validate the hypothesis that a new, custom product was required, I conducted a competitive teardown of available market tools, auditing open-source utilities (such as Wallos) and consumer subscription apps (such as Renewly).

| Feature / Capability | Existing Market Solutions | Renewals (The New Product Opportunity) |
| --- | --- | --- |
| **Primary Value Metric** | Event push notifications ("Due in 3 days") | Auditable financial system of record |
| **Historical Price Mutability** | Overwrites current price; destroys past baseline | Append-only price periods with change deltas |
| **Tax Audit Readiness** | Single aggregate transaction value | Explicit itemization: Net, Gross, and VAT rates |
| **Contract State Lineage** | Binary toggle (Active / Inactive) | Full lifecycle logs (Started, Paused, Resumed, Ended) |
| **Data Privacy** | Cloud hosting / third-party bank linking | Local-first, zero-exposure architectural model |

**Market Verdict:** Incumbent solutions optimized almost exclusively for **surface-level calendar alerts**, entirely ignoring **contract auditability and cost variance**. This validated the white space for a purpose-built system centered on **data fidelity**.

---

## Phase 2: Product Strategy & Scope Definition

A frequent pitfall in zero-to-one product development is premature feature bloat. To ensure delivery velocity and defensible product architecture, I established clear operational guardrails.

### The Three-Question Product North Star

Every potential feature was benchmarked against three mandatory operational questions. If an idea did not answer one of them, it was eliminated:

1. **What has it actually cost?** Complete financial audit per commitment, broken down by Net, VAT, and Gross.
2. **How has the commitment evolved?** Full visibility into status changes, pause states, and price adjustments over time.
3. **What is committed next?** Clear runway of upcoming obligations displayed in chronological and calendar views.

### Scope Discipline & MVP Containment

Once the core product worked locally, common expansion requests emerged: mobile native wrappers, multi-user authentication, and hosted cloud instances.

I executed a formal **MVP Scope Freeze**. Migrating to a hosted multi-tenant cloud at this stage would introduce authentication overhead, recurring infrastructure expenses, and security liabilities for sensitive financial data without advancing the core product value. Delivering a robust, dependable tool that solved the primary problem took precedence over feature sprawl.

---

## Phase 3: Data Architecture & System Design

A product's user experience is strictly constrained by its data model. A flat list of subscriptions cannot capture price variations or discontinuous contract states without data corruption. I engineered a normalized relational schema around five interdependent entities:

```
┌──────────────┐       1:N       ┌──────────────────┐
│   Vendors    ├────────────────►│  Subscriptions   │
└──────────────┘                 └────────┬─────────┘
                                          │
                  ┌───────────────────────┼───────────────────────┐
                  │ 1:N                   │ 1:N                   │ 1:N
                  ▼                       ▼                       ▼
       ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
       │   Price Periods    │  │   Status History   │  │  Actual Payments   │
       │ (Append-Only Logs) │  │  (Auditable State) │  │ (Reconciled Invs)  │
       └────────────────────┘  └────────────────────┘  └────────────────────┘
```

* **Vendors:** Entity-level attributes (Legal name, tax jurisdiction, VAT ID, web portal).
* **Subscriptions:** Commitment profiles tied to functional cost centers.
* **Price Periods (Append-Only):** Rather than updating existing pricing cells, rate adjustments spawn a new chronological record. This immutable design protects historical baselines and automatically surfaces real price creep.
* **Status History:** Event-driven state machine logging explicit dates for `Started`, `Paused`, `Resumed`, `Discontinued`, and `Restarted`.
* **Actual Payments:** Reconciled cash outflows tied directly to invoice references, tracking separate Net, VAT, and Gross amounts.

### Data Governance Protocols

To ensure the interface displayed credible figures rather than speculative calculations, I established explicit data ingestion standards:

* **Invoices as Single Source of Truth:** Reconciled tax invoices take precedence over credit card aggregations or informal notes.
* **Zero Silent Overwrites:** Data discrepancies were logged for deliberate resolution rather than patched silently in background routines.
* **Reversible State Migrations:** Strict backup checkpoints preceded all bulk schema modifications to prevent corruption.

---

## Phase 4: Product Delivery & UX Execution

The application was built as a clean, low-latency interface structured around five purpose-built views:

1. **Executive Dashboard:** At-a-glance visibility into near-term commitments (30-day runway), annualized projections, recent contract state adjustments, and category distribution charts.
2. **Subscription Inspector:** Unified temporal audit trails for any contract, rendering price jumps, status history, and payments on a single screen.
3. **Forecasting Calendar:** Forward-looking scheduling matrix pinpointing upcoming renewal charges by exact date.
4. **Reconciled Ledger:** Comprehensive payment history with clean CSV export capabilities for seamless bookkeeping.
5. **Vendor Directory:** Aggregated spend mapped by legal vendor entity to evaluate overall supplier concentration.

---

## Product Outcomes & Core Competencies

* **End-to-End Execution:** Owned the full product lifecycle from zero-to-one: discovered an unaddressed market need, designed the data model, managed the scope, built the application, and deployed a live public release.
* **Immediate Operational ROI:** Transitioned from manual spreadsheet synthesis to automated, single-pane portfolio visibility across recurring commitments.
* **Actionable Price Visibility:** Automatically exposed unnotified vendor price increases upon data ingestion, directly informing supplier renegotiations and cancellations.
* **Ready-to-Use Product:** Shipped a production-grade application and complete product showcase live at [Renewals Product Page](https://pranoti.thesciencetalk.com/products/subscription-tracker/).

---

## Work With Me

Most organizations suffer from the same underlying challenge: **critical operational data exists in silos, but actionable decision-making tools are missing.**

Building successful software doesn't start with code or sprawling backlogs; it starts with **problem framing, robust data foundations, and disciplined scope management.**

I am **Dr. Pranoti Kshirsagar**. I translate complex, unstructured business problems into intuitive, technically sound, and functional digital products.

* **Portfolio:** [pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/)
* **Get in touch:** [Connect via The Science Talk](https://thesciencetalk.com/contact-us/)
