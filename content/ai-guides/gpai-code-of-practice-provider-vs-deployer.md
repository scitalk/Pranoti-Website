---
title: "GPAI Code of Practice: Provider vs. Deployer, Explained"
date: 2026-07-22
lastmod: 2026-08-18
slug: "gpai-code-of-practice-provider-vs-deployer"
draft: false
featured_image: "/images/ai-guides/eu-ai-act.webp"
description: "Does the GPAI Code of Practice apply to you? It binds general-purpose AI model providers, not deployers — here's the test and what to ask your AI vendor."
keywords: ["GPAI Code of Practice apply to me", "GPAI provider vs deployer", "am I a GPAI provider EU AI Act", "GPAI Code of Practice", "AI Act Article 53", "AI Act Article 55 systemic risk", "GPAI vendor due diligence"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["EU AI Act", "GPAI", "AI regulation", "AI vendor due diligence", "AI governance"]
category: "ai-integration-guides"
pillar: "EU AI Act & Compliance"
sidebar_author_bio: true
sidebar_links:
  - title: "The Infrastructure Gap Slowing Claude Adoption in European Research"
    url: "/ai-guides/anthropic-ai-adoption-european-research/"
  - title: "AI Vendor Lock-In: The Startup Audit You Should Run Before Scale"
    url: "/ai-guides/ai-vendor-lockin-startup-audit-europe/"
  - title: "EU AI Act AI System Definition: The Official 7-Element Test"
    url: "/ai-guides/eu-ai-act-ai-system-definition-7-element-test/"
---

**Does the GPAI Code of Practice apply to you?** For most teams that build AI-powered products, the answer is no. The Code is the European Commission's voluntary compliance tool for providers of general-purpose AI models under the EU AI Act. The Commission published it on 10 July 2025 after input from more than 1,000 stakeholders. It binds model providers, not the teams that build on top of their models. This guide walks through the provider-vs-deployer test, what each of the Code's three chapters covers, and what a downstream team building on GPT, Claude, or similar models should take from it.

> **Scope note:** The Code is a voluntary tool. Under Article 53(4), providers who sign it and follow its measures can rely on it to demonstrate compliance with the AI Act's Chapter V obligations, until the Commission publishes a harmonized standard. Providers who do not sign it must demonstrate compliance another way. This is a higher evidential burden, but not a legal requirement to sign.

## What is the GPAI Code of Practice?

The GPAI Code of Practice is a voluntary tool, prepared by independent experts through a multi-stakeholder drafting process. It helps providers of general-purpose AI models comply with the AI Act's rules. The Commission's AI Office convened the process, including a kick-off Plenary event on 30 September 2024 involving nearly 1,000 participants, and received the final Code on 10 July 2025.

The Code covers three chapters: **Transparency**, **Copyright**, and **Safety and Security**, which address the obligations set out in Articles 53 and 55 of the AI Act. Under Article 53(4), providers can rely on the Code to demonstrate compliance with their Article 53(1) obligations until the Commission publishes a harmonized standard. The Commission describes this as reducing administrative burden and giving providers more legal certainty than proving compliance through other means.

It is not a law. It is the Commission's recommended route to compliance with a law that already applies. The GPAI obligations themselves came into application on 2 August 2025 regardless of whether a provider signs the Code.

## What you need before starting

- No technical setup required. This is a classification and due-diligence exercise, not an integration guide.
- Clarity on how your organization relates to a general-purpose AI model. Did you train and release it, or do you call it via API or use it embedded in a product?

## GPAI Code of Practice: are you a provider or a deployer?

The Code's overview page from [the Commission's digital-strategy site](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) draws a clear line. A **provider** develops a general-purpose AI model and places it on the market, as an API, as open weights, or embedded in a product accessible to EU users. A **deployer** uses a model someone else built, typically via API, without developing or placing that model on the market itself.

**The Code does not apply to pure deployers.** If your team calls the Claude or GPT API, fine-tunes a model for internal use, or builds a SaaS product on top of a general-purpose model without releasing that underlying model itself, you are very likely a deployer. The Code's obligations sit with your model provider, not you.

> Fine-tuning a model for your own product does not automatically make you a "provider" under the Code. The distinction turns on whether you place the underlying general-purpose model on the market, not on whether you customized it.

## What the Transparency chapter covers

The Transparency chapter applies to **all GPAI providers** and supports the Article 53 documentation duty. Its centerpiece is the **Model Documentation Form**, the standardized disclosure providers use to document a model's architecture, training compute, intended use, and other technical characteristics.

The official chapter text is published at [ec.europa.eu/newsroom/dae/redirection/document/118120](https://ec.europa.eu/newsroom/dae/redirection/document/118120).

## What the Copyright chapter covers

The Copyright chapter also applies to **all GPAI providers**. It supports the Article 53 duty to maintain and make available a policy on EU copyright law compliance. In practice, this means documenting how a provider's training data respects copyright, including how it handles rights-holder opt-outs.

The official chapter text is published at [ec.europa.eu/newsroom/dae/redirection/document/118115](https://ec.europa.eu/newsroom/dae/redirection/document/118115).

## What the Safety and Security chapter covers

This is the narrowest chapter. It applies only to providers of the most advanced GPAI models, those classified as carrying **systemic risk** under Article 55 AI Act. This is a small subset of providers: models at the frontier of capability and scale, not the majority of general-purpose models on the market.

The official chapter text is published at [ec.europa.eu/newsroom/dae/redirection/document/118119](https://ec.europa.eu/newsroom/dae/redirection/document/118119).

## Why the Code matters even if you are not a provider

Even as a downstream deployer, the Code shapes what you can reasonably expect from a model vendor. This is directly useful for procurement and due diligence.

A provider that has signed the Code and published its Model Documentation Form gives you a standardized way to check training compute, intended use, and copyright policy before you build on a model. A provider that has not signed the Code must demonstrate compliance some other way. Ask about this directly during vendor evaluation, since the evidential burden falls on them either way.

> If you assess a GPAI vendor for a client or your own organization, ask directly: has this provider signed the Code of Practice, and if not, what alternative compliance evidence do they offer? The [Commission's Code of Practice overview](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) lists confirmed signatories.

## Key dates

- **10 July 2025**: The Commission publishes the GPAI Code of Practice.
- **2 August 2025**: The Chapter V obligations for GPAI providers, which the Code supports, enter into application.
- **2 August 2026**: The Commission's enforcement powers for these obligations enter into application, including the ability to issue fines.
- **2 August 2027**: Providers of GPAI models placed on the market before 2 August 2025 must reach full compliance.

## Decision checklist

1. **Do you develop and place a general-purpose AI model on the market**, as an API, open weights, or embedded in a product? If no, the Code does not bind you directly.
2. **If yes, does your model carry systemic risk under Article 55?** This determines whether the Safety and Security chapter applies alongside Transparency and Copyright.
3. **If you are a deployer, has your model provider signed the Code?** Check the Commission's signatory list before you assume compliance.
4. **If your provider has not signed, what alternative compliance evidence have they shared with you?** Document this for your own due-diligence records.

## Troubleshooting

**"I fine-tuned a model, so I must be a provider."** Not necessarily. Fine-tuning a model for your own use does not place a new general-purpose model on the market. The test is whether you release the underlying model, not whether you customized its behavior.

**"My SaaS product uses GPT via API, so I have to sign the Code."** No. As a deployer that calls a provider's model, the Code's obligations sit with the provider, not with your product. Your interest is in confirming your provider's compliance, not in signing the Code yourself.

**"My model is small, so the Safety and Security chapter cannot apply to me."** Model size alone does not determine this. Systemic risk under Article 55 is a specific regulatory classification tied to capability and scale thresholds, not a general impression of a model's footprint.

## What you can do now

You can now correctly classify your organization as a GPAI provider or downstream deployer under the AI Act. If you are a deployer, you know exactly what to ask a model vendor during procurement or due diligence: whether they have signed the Code, what their Model Documentation Form discloses, and how they handle the copyright-policy duty.

## Related reading on The Science Talk

See also [EU AI Act Article 4: What AI Literacy Requirements Mean for European Research Institutes](https://thesciencetalk.com/news/eu-ai-act-article-4-ai-literacy-research-institutes/) on The Science Talk. It covers the parallel Article 4 AI-literacy provision, which reaches research institutes whether they are a GPAI provider or deployer. Note that the July 2026 Digital Omnibus simplified the company-level requirement after that piece was written.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](/contact/)*
