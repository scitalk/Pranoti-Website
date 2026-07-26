---
title: "Recommender Systems: Even EU Regulators Don't Agree Which Law Applies"
date: 2026-07-26
lastmod: 2026-07-19
draft: false
description: "The European Commission's own DSA review admits recommender systems sit ambiguously between the DSA and the AI Act. Here's what that means for teams building one."
keywords: ["recommender systems DSA AI Act", "which law applies recommender system EU", "DSA AI Act overlap", "recommender system compliance Europe", "algorithmic recommender EU regulation", "DSA Article 33 review"]
author: "Pranoti Kshirsagar"
reading_time: "8 min"
tags: ["DSA", "EU AI Act", "recommender systems", "regulatory overlap", "algorithmic transparency"]
category: "perspectives"
sidebar_links:
  - title: "EU CADA Sovereignty Tiers: What the Four Cloud Levels Mean"
    url: "/perspectives/eu-cada-cloud-sovereignty-tiers/"
  - title: "EU AI Act Article 25: When You Become the AI 'Provider'"
    url: "/perspectives/eu-ai-act-article-25-agency-becomes-provider/"
  - title: "Regulation as a Feature: The Case for AI Transparency"
    url: "/perspectives/regulation-as-a-feature-ai-transparency/"
---

When stakeholders tell a regulator that a rule is unclear, the regulator's usual instinct is to insist otherwise. So it is worth pausing on the fact that the European Commission's own review of the Digital Services Act names **recommender systems** as one of the most-cited areas of stakeholder ambiguity over which EU law actually applies to them — the Commission is not disputing the confusion, it is documenting it.

If you are building or operating a recommender system in the EU — a "you might also like," a personalised feed, a ranking algorithm — that admission from the regulator itself matters more than any individual law firm's read of the rules.

## Where the admission comes from

The finding sits in [Report COM(2025) 708 final](https://digital-strategy.ec.europa.eu/en/library/report-application-article-33-regulation-eu-20222065-dsa-and-interaction-regulation-other-legal), the Commission's own review under Article 91(1) of the Digital Services Act, published 17 November 2025. Its purpose was to assess how the DSA — [Regulation (EU) 2022/2065](http://data.europa.eu/eli/reg/2022/2065/oj) — interacts with other EU legal acts, including the [AI Act, Regulation (EU) 2024/1689](http://data.europa.eu/eli/reg/2024/1689/oj).

The report's central finding is that the DSA is deliberately **content-agnostic** — it regulates how intermediary services operate, not what AI does — which means it necessarily has to be read alongside other frameworks for anything AI-related. Recommender systems are one of the specific areas the report flags where stakeholders report genuine ambiguity over which regime governs, alongside dark patterns, content moderation, and product safety.

## Why a recommender system sits in the gap

The DSA imposes transparency obligations directly on recommender systems — Article 27 requires platforms to set out, in plain language, the main parameters used in their recommender systems, and Article 38 gives users of very large platforms the right to a version not based on profiling. That is a real, binding obligation, but it is a **transparency** duty aimed at the platform operator.

The AI Act, meanwhile, governs the **AI system itself** — its risk classification, its provider's obligations, its transparency duties under Article 50 where relevant. A recommender system built on an AI model can trigger AI Act obligations independent of, and in addition to, its DSA duties as a platform feature.

The two frameworks are not in conflict on paper. But the Commission's report describes exactly the practical problem this creates: stakeholders do not have a clear, single answer for "which set of obligations governs my recommender system," because the honest answer is "potentially both, assessed separately, for different reasons."

## What this costs in practice

This is not a theoretical inconvenience. The Commission's own report notes that representatives of online intermediary services report overlapping obligations consuming **15–30% of internal legal and IT resources**, precisely because teams end up running duplicate assessments rather than one clear one.

The report also flags a structural reason this will not resolve quickly: DSA enforcement follows a **country-of-origin** logic (Member State of establishment, or the Commission for very large platforms), while product-related acts including the AI Act more often follow a **country-of-destination** logic. The Commission explicitly names a "risk of parallel proceedings for the same practices" arising from this mismatch, and commits only to "promote coordination" through the European Board for Digital Services — not to eliminate the risk.

> The Commission's own conclusion: DSA and AI Act are "mostly complementary and mutually reinforcing," but a small number of overlaps — recommender systems among them — create genuine legal uncertainty. No binding precedence rules exist yet.

## When the fix is coming

The report defers resolution to two future processes: a broader **Digital Fitness Check** of EU digital law, and the **DSA evaluation due by 17 November 2027**. Until either lands, the ambiguity the Commission has already acknowledged remains the operating reality for anyone building a recommender system now.

That is a two-year-plus gap between "the regulator agrees this is unclear" and "the regulator has resolved it." Waiting for clarity is not a strategy a small team can afford to run on.

## What I would do with that gap

Treat the ambiguity as a reason for more documentation, not less. If your recommender system is AI-based, run it through both lenses independently rather than assuming one framework's compliance covers the other: check your DSA transparency duties on the main-parameter disclosure under Article 27, and separately check whether the underlying AI model triggers Article 50 transparency or a high-risk classification under the AI Act.

Where the two frameworks ask for similar things — explaining to users why they are seeing particular content, giving them a way to adjust or opt out — build one clear explanation that satisfies both readings rather than two separate, conflicting ones. And keep a record of the reasoning behind your classification decision; if enforcement diverges by country as the Commission itself warns it might, a documented rationale is the strongest position to be in.

The Commission's own report is, in a sense, a gift here: it is an official admission you can point to. "The European Commission's own review acknowledges this area is ambiguous" is a stronger position with a client or auditor than trying to argue a settled answer where none officially exists yet.

---

Most regulatory-uncertainty pieces are written by outsiders speculating about gaps. This one is different: the gap is named by the regulator that wrote both laws. If you are building a recommender system and assuming someone has already settled which EU law governs it cleanly, the Commission's own words say otherwise — plan accordingly.

If you want a second opinion on where your recommender system sits across the DSA and the AI Act, that is exactly the kind of dual-framework mapping worth doing before an audit forces the question. [Get in touch →](/contact/)

---
*Browse all [Perspectives](/perspectives/) or [get in touch →](/contact/)*
