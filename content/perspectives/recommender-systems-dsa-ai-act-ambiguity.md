---
title: "Recommender Systems: Even EU Regulators Don't Agree Which Law Applies"
date: 2026-07-26
lastmod: 2026-07-19
draft: false
featured_image: "/images/ai-guides_perspectives/eu-ai-act.webp"
description: "The European Commission's own DSA review admits recommender systems sit ambiguously between the DSA and the AI Act. Here's what that means for teams building one."
keywords: ["recommender systems DSA AI Act", "which law applies recommender system EU", "DSA AI Act overlap", "recommender system compliance Europe", "algorithmic recommender EU regulation", "DSA Article 33 review"]
author: "Pranoti Kshirsagar"
reading_time: "8 min"
tags: ["DSA", "EU AI Act", "recommender systems", "regulatory overlap", "algorithmic transparency"]
category: "perspectives"
pillar: "EU AI Act & Compliance"
sidebar_links:
  - title: "EU CADA Sovereignty Tiers: What the Four Cloud Levels Mean"
    url: "/perspectives/eu-cada-cloud-sovereignty-tiers/"
  - title: "EU AI Act Article 25: When You Become the AI 'Provider'"
    url: "/perspectives/eu-ai-act-article-25-agency-becomes-provider/"
  - title: "Regulation as a Feature: The Case for AI Transparency"
    url: "/perspectives/regulation-as-a-feature-ai-transparency/"
---

When stakeholders tell a regulator that a rule is unclear, the regulator's usual instinct is to insist otherwise. The European Commission's own review of the Digital Services Act names **recommender systems** as one of the most-cited areas of stakeholder ambiguity. The review does not dispute the confusion. It documents it.

You may build or operate a recommender system in the EU. It could be a "you might also like" feature, a personalized feed, or a ranking algorithm. This admission from the regulator matters more than any single law firm's reading of the rules.

## Where the admission comes from

The finding sits in [Report COM(2025) 708 final](https://digital-strategy.ec.europa.eu/en/library/report-application-article-33-regulation-eu-20222065-dsa-and-interaction-regulation-other-legal). This is the Commission's own review under Article 91(1) of the Digital Services Act, published 17 November 2025. Its purpose was to assess how the DSA — [Regulation (EU) 2022/2065](http://data.europa.eu/eli/reg/2022/2065/oj) — interacts with other EU legal acts, including the [AI Act, Regulation (EU) 2024/1689](http://data.europa.eu/eli/reg/2024/1689/oj).

The report's central finding is that the DSA is deliberately **content-agnostic**. It regulates how intermediary services operate, not what AI does. This means teams must read it alongside other frameworks for anything AI-related. Recommender systems are one of the specific areas the report flags. Stakeholders report genuine ambiguity over which regime governs them, alongside dark patterns, content moderation, and product safety.

## Why a recommender system sits in the gap

The DSA imposes transparency obligations directly on recommender systems. Article 27 requires platforms to set out, in plain language, the main parameters used in their recommender systems. Article 38 gives users of very large platforms the right to a version not based on profiling. This is a real, binding obligation. But it is a **transparency** duty aimed at the platform operator.

The AI Act governs the **AI system itself**. This includes its risk classification, its provider's obligations, and its transparency duties under Article 50 where relevant. A recommender system built on an AI model can trigger AI Act obligations. These obligations apply independent of, and in addition to, its DSA duties as a platform feature.

The two frameworks do not conflict on paper. But the Commission's report describes the practical problem this creates. Stakeholders do not have a clear, single answer for "which set of obligations governs my recommender system." The honest answer is "potentially both, assessed separately, for different reasons."

## What this costs in practice

This is not a theoretical inconvenience. The Commission's own report notes that representatives of online intermediary services report overlapping obligations. These obligations consume **15–30% of internal legal and IT resources**. Teams end up running duplicate assessments rather than one clear one.

The report also flags a structural reason this problem will not resolve quickly. DSA enforcement follows a **country-of-origin** logic (Member State of establishment, or the Commission for very large platforms). Product-related acts, including the AI Act, more often follow a **country-of-destination** logic. The Commission names a "risk of parallel proceedings for the same practices" arising from this mismatch. It commits only to "promote coordination" through the European Board for Digital Services. It does not commit to eliminate the risk.

> The Commission's own conclusion: the DSA and AI Act are "mostly complementary and mutually reinforcing," but a small number of overlaps — recommender systems among them — create genuine legal uncertainty. No binding precedence rules exist yet.

## When the fix is coming

The report defers resolution to two future processes: a broader **Digital Fitness Check** of EU digital law, and the **DSA evaluation due by 17 November 2027**. Until either process concludes, the ambiguity the Commission has already acknowledged remains the operating reality for anyone building a recommender system now.

This is a two-year-plus gap between "the regulator agrees this is unclear" and "the regulator has resolved it." A small team cannot afford to wait for clarity as a strategy.

## What to do with that gap

Treat the ambiguity as a reason for more documentation, not less. If your recommender system is AI-based, run it through both lenses independently. Do not assume one framework's compliance covers the other. Check your DSA transparency duties on the main-parameter disclosure under Article 27. Separately, check whether the underlying AI model triggers Article 50 transparency or a high-risk classification under the AI Act.

The two frameworks sometimes ask for similar things. Both frameworks may require you to explain to users why they see particular content, and to give them a way to adjust or opt out. Build one clear explanation that satisfies both readings rather than two separate, conflicting ones. Keep a record of the reasoning behind your classification decision. If enforcement diverges by country as the Commission itself warns it might, a documented rationale gives you the strongest position.

The Commission's own report is, in a sense, a gift here. It is an official admission you can point to. "The European Commission's own review acknowledges this area is ambiguous" is a stronger position with a client or auditor than an argument for a settled answer where none officially exists yet.

---

Outsiders write most regulatory-uncertainty pieces by speculating about gaps. This piece is different. The regulator that wrote both laws names the gap. You may build a recommender system and assume someone has already settled which EU law governs it cleanly. The Commission's own words say otherwise. Plan accordingly.

If you want a second opinion on where your recommender system sits across the DSA and the AI Act, that is exactly the kind of dual-framework mapping worth doing before an audit forces the question. [Get in touch →](https://thesciencetalk.com/contact-us/)

---
*Browse all [Perspectives](/perspectives/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
