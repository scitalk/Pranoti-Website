---
title: "EU AI Act Article 5: AI Practices You're Banned From Using"
date: 2026-07-29
lastmod: 2026-07-31
slug: "eu-ai-act-prohibited-practices-article-5"
draft: false
description: "EU AI Act Article 5 bans are already live — workplace emotion recognition, dark-pattern design, face-scraping, biometric profiling. Run the checklist."
featured_image: "/images/ai-guides_perspectives/eu-ai-act.webp"
keywords: ["EU AI Act prohibited AI practices", "banned AI Article 5", "EU AI Act Article 5", "HR emotion recognition software ban EU", "employee sentiment analysis AI Act illegal", "dark pattern AI law EU", "biometric categorisation AI Act", "AI Act compliance checklist SME"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["EU AI Act", "Article 5", "AI regulation", "prohibited practices", "workplace AI"]
category: "ai-integration-guides"
pillar: "EU AI Act & Compliance"
sidebar_links:
  - title: "EU AI Act High-Risk Hiring AI: The Annex III Test"
    url: "/ai-guides/eu-ai-act-high-risk-hiring-ai-annex-iii-test/"
  - title: "How to add AI disclosures that comply with the EU AI Act"
    url: "/ai-guides/ai-generated-content-disclosure-eu-ai-act/"
  - title: "EU AI Act AI System Definition: The Official 7-Element Test"
    url: "/ai-guides/eu-ai-act-ai-system-definition-7-element-test/"
---

The EU AI Act's **Article 5 prohibited AI practices** have applied since **2 February 2025**. These are not a future deadline. They are live red lines every organization is already bound by. Most small teams have never read Article 5 in full. They assume "prohibited practices" means something distant, such as mass surveillance, social credit systems, or government overreach. Four of the eight bans sit much closer to home, in ordinary HR, marketing, and analytics tooling.

This guide checks your team's current AI tool stack against the four prohibitions that realistically apply to a small business. It also explains why the other four almost certainly do not apply.

## What you need before starting

- A list of the AI tools your team currently uses: HR/people-ops software, employee analytics, marketing or growth tooling, any image or facial-recognition features
- No legal background required. This is a plain-English self-check, not a legal opinion.
- 10 minutes to run through the four checks below

## The 4 EU AI Act prohibited AI practices every small team should check

These are the prohibitions most likely to intersect with an ordinary SME or agency's software stack. All four have applied since 2 February 2025.

### Emotion recognition at work or in education

[Article 5(1)(f)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5) bans AI systems that infer emotions of individuals in workplace or education settings, with a narrow exception for medical or safety purposes.

**Where this shows up in practice:** HR sentiment-analysis add-ons, "employee engagement" or "mood-scoring" dashboards, call-center emotion-detection plugins layered onto call-recording software. If a tool analyzes voice tone, facial expression, or written communication to infer how staff *feel* rather than *what they said*, it likely falls inside this prohibition.

> The exception is narrow: genuine medical monitoring or safety-critical use (for example, detecting driver fatigue), not general workplace wellbeing analytics.

### Manipulative or dark-pattern AI design

[Article 5(1)(a)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5) bans AI systems that deploy subliminal or purposefully manipulative or deceptive techniques, where this materially distorts a person's behavior and causes significant harm.

**Where this shows up in practice:** AI-driven growth or conversion-optimization tooling explicitly engineered to override a user's considered judgment. This does not include ordinary personalization or recommendation, but techniques designed to bypass rational decision-making. The bar is "significant harm," so most standard marketing personalization sits outside this ban. The risk concentrates in tools built specifically to exploit psychological manipulation.

### Untargeted facial-image scraping

[Article 5(1)(e)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5) bans the creation or expansion of a facial-recognition database through untargeted scraping of facial images from the internet or CCTV footage.

**Where this shows up in practice:** this is a vendor due-diligence question more than a usage question. If you evaluate a facial-recognition or biometric-verification tool, ask directly how its training database was built. Untargeted internet or CCTV scraping is the specific practice banned, not facial recognition as a category.

### Biometric categorization by protected traits

[Article 5(1)(g)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5) bans the use of biometric data to infer or categorize someone's race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation, with an exception for lawful labeling or filtering of datasets.

**Where this shows up in practice:** biometric analytics tools that go beyond simple identity verification (confirming someone is who they claim to be) into inferring protected characteristics from biometric signals. Straightforward biometric login or attendance-verification tools are not affected. The ban targets inference of protected traits specifically.

## The 4 exceptions most small teams can skip

The remaining four Article 5 prohibitions are real but narrow. They are unlikely to intersect with an ordinary SME or agency's tools:

- **Exploitation of vulnerabilities** ([Art. 5(1)(b)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)): targeting people based on age, disability, or economic situation to materially distort their behavior and cause harm
- **Social scoring** ([Art. 5(1)(c)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)): evaluating people's social behavior to justify detrimental treatment in unrelated contexts
- **Criminal risk-profiling** ([Art. 5(1)(d)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)): predicting that someone will commit a crime based solely on profiling or personality traits, rather than objective, verifiable facts
- **Real-time biometric identification by law enforcement** ([Art. 5(1)(h)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)): banned outside narrow exceptions for trafficking, imminent threats, or serious Annex II offenses

An ordinary business does not build or buy any of these. They are worth knowing exist, not worth auditing your tool stack against.

## Two new bans just added: AI-generated non-consensual intimate images and CSAM

Article 5 is not frozen at eight prohibitions. The "AI Omnibus" amendment (Regulation (EU) 2026/1744), in force since 27 July 2026, inserted two new points into Article 5(1), **(ba)** and **(bb)**. These ban AI systems that generate or manipulate **non-consensual intimate images, video, or audio** (so-called "nudification" tools) and **child sexual abuse material**. The original eight bans did not cover these practices. The Commission's own reasoning for adding them was that existing points like (a) manipulation and (b) exploitation of vulnerabilities do not apply, since generating this material does not require manipulating the victim into anything.

These two new prohibitions apply from **2 December 2026**. They are not yet in force, but they are now part of the adopted legal text. If your stack includes any image, video, or audio generation tooling with lax content controls, flag it for a follow-up check closer to that date rather than acting on it today.

## How to check your own tool stack

Run each AI tool your team uses through these four questions:

1. **Does it infer staff or student emotions**, rather than analyze what was said or done? Check against Article 5(1)(f).
2. **Was it built specifically to override users' rational judgment**, beyond ordinary personalization? Check against Article 5(1)(a).
3. **If it does facial recognition, was its database built by untargeted scraping** of the internet or CCTV footage? Check against Article 5(1)(e).
4. **Does it infer race, political views, union membership, religion, or sexual orientation from biometric data?** Check against Article 5(1)(g).

A "no" to all four means your stack clears Article 5. A "yes" or "unsure" to any one needs a closer look before you continue to use that tool.

## What happens if you are already using a banned practice

Stop using the specific feature or tool, and document the decision, including when you identified the issue and what you changed. This is genuinely rare in ordinary SaaS, HR, and marketing tooling. Most flagged tools turn out to be standard personalization or verification features, not the practices Article 5 actually targets.

> This is a quick audit, not a compliance overhaul. Most small teams will run through all four checks and find nothing to change.

## What you can do now

You can now run your team's AI tool stack through the four checks that matter and reach a defensible answer on Article 5, without treating every analytics or HR tool as a legal risk.

This pairs with the rest of the small-team AI Act cluster. [Article 4](/perspectives/eu-ai-act-article-4-creator-agencies-small-teams/) covers the AI literacy duty for your team. [Article 25](/perspectives/eu-ai-act-article-25-agency-becomes-provider/) covers when your agency can accidentally become a "provider." [Article 50](/ai-guides/ai-generated-content-disclosure-eu-ai-act/) covers disclosure obligations. [Article 62](/ai-guides/eu-ai-act-sme-support-article-62/) covers the free support you can claim as an SME.

## Related reading on The Science Talk

See also [EU AI Act Article 4: What AI Literacy Requirements Mean for European Research Institutes](https://thesciencetalk.com/news/eu-ai-act-article-4-ai-literacy-research-institutes/) on The Science Talk, useful background on how the Act's obligations reach ordinary organizations, not just AI developers.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
