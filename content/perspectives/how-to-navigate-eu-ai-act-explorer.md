---
title: "How to Navigate the EU AI Act Explorer"
date: 2026-08-17
draft: false
featured_image: "/images/ai-guides_perspectives/eu-ai-act.webp"
description: "A guide to the EU AI Act Explorer: how Articles, Recitals, and Annexes connect, using Article 50's transparency rules as the example."
keywords: ["EU AI Act Explorer", "how to navigate EU AI Act Explorer", "EU AI Act articles vs recitals", "EU AI Act annexes explained", "Article 50 EU AI Act", "EU AI Act Regulation 2024/1689"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["EU AI Act", "Article 50", "AI transparency", "compliance"]
category: "perspectives"
pillar: "EU AI Act & Compliance"
sidebar_links:
  - title: "EU AI Act Article 50 Is Now in Force: What Changed on 2 August 2026"
    url: "/perspectives/eu-ai-act-article-50-in-force-2026/"
  - title: "How to add AI disclosures that comply with the EU AI Act"
    url: "/ai-guides/ai-generated-content-disclosure-eu-ai-act/"
  - title: "EU AI Act Checklist for Small Business: 6 Articles That Matter"
    url: "/perspectives/eu-ai-act-checklist-small-business/"
---

The EU AI Act can feel like one more thing to track. New updates arrive. You read long documents. You search the internet for answers. Compliance can feel like this:

![Compliance confusion when tracking EU AI Act updates](/images/ai-guides_perspectives/eu-ai-act-confused-ryan-gosling.gif)

This article helps you through that process. The most important resource is the [EU AI Act Explorer](https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer), built by the European Commission. This article uses Article 50 as the example. Article 50 became enforceable on 2 August 2026. See [Article 50 Is Now in Force](/perspectives/eu-ai-act-article-50-in-force-2026/) for what that date changed.

Regulation (EU) 2024/1689, the EU AI Act, is not one document. It has three parts, and each part does a different job. A reader who looks at only one part gets an incomplete answer. This article explains how Articles, Recitals, and Annexes work together. It uses Article 50, the transparency rule, as the example, because Article 50 touches all three parts.

## The three-part structure

- **Articles (the "what"):** the binding text. Articles state the obligations. They state what a provider or a deployer must do.
- **Recitals (the "why"):** the numbered paragraphs before the Articles. Recitals explain the reason for an Article and give context for it. A Recital does not create an obligation by itself.
- **Annexes (the "how"):** technical detail. Annexes list classification criteria, documentation items, and data fields. An Article points to an Annex when the detail is too long for the Article itself.

![EU AI Act Explorer: what, why, how](/images/ai-guides_perspectives/eu-ai-act-explorer-what-why-how.jpg)

Not every Article has a matching Annex. A link between an Article and an Annex exists only when the Article names that Annex. Always check the Article text. Do not assume a link exists.

## Article 50: the binding obligations - the WHAT

Article 50 states four transparency duties. Each duty applies to a provider (the party that builds the system) or a deployer (the party that uses it):

| Provision | Who it applies to | The obligation | Key exemption |
|---|---|---|---|
| Art. 50(1) | Provider — AI systems that interact with natural persons (for example chatbots) | Design the system so it informs people that they are talking to an AI system | Not necessary if this is already obvious to a "reasonably well-informed, observant and circumspect" person. Law-enforcement systems are exempt |
| Art. 50(2) | Provider — AI systems that generate synthetic audio, image, video, or text | Mark outputs in a machine-readable format. Make outputs detectable as AI-generated. Use solutions that are "effective, interoperable, robust and reliable" as far as this is technically possible | Assistive editing functions. Content that does not substantially change deployer input. Law-enforcement systems |
| Art. 50(3) | Deployer — emotion recognition or biometric categorisation systems | Inform exposed persons about the operation of the system | Law-enforcement systems, subject to safeguards |
| Art. 50(4) | Deployer — deep fakes and AI-generated public-interest text | Disclose the artificial nature of the content in a clear and distinguishable way | Evidently artistic, satirical, or fictional work (disclosure is still necessary, in a form that does not hamper enjoyment of the work). AI-generated text that went through genuine human editorial review, with a named person who holds editorial responsibility |

Two provisions apply to all four duties. **Article 50(5)** states that this information must reach people no later than the first interaction or exposure. **Article 50(7)** gives the AI Office the task of encouraging Union-level Codes of Practice, to help standardize how providers apply the marking duty.

## Recitals: what they add and what they do not add - the WHY
A Recital explains the reason for an Article. A Recital does not add a new rule. Three Recitals apply directly to Article 50:

- **Recital 132** explains why the transparency duties exist. Certain AI systems that interact with people or generate content "may pose specific risks of impersonation or deception." For this reason, the Act requires disclosure, using the same "reasonably well-informed, observant and circumspect" test that appears in Article 50(1).
- **Recital 133** explains the technical side of the Article 50(2) marking duty. It names methods that regulators expect providers to consider: watermarks, metadata, cryptographic provenance methods, logging, and fingerprints. It states that these methods must be "sufficiently reliable, interoperable, effective and robust as far as this is technically feasible."
- **Recital 134** protects artistic and satirical work. It states that a deployer meets the deepfake disclosure duty when the disclosure "does not hamper the display or enjoyment of the work." It also states that this duty does not restrict freedom of expression or freedom of the arts.

A Recital helps you show how you met an obligation. A Recital is not a substitute for the obligation. A Recital does not override what an Article requires.

## Annex for Article 50 - the HOW

Here is the point worth remembering: Article 50 does not name a single Annex. No Annex names Article 50. The transparency duty stands on its own, with no linked checklist or classification list behind it.

This surprises people, because three Annexes get pulled into Article 50 discussions by mistake:

- **Annex III** (high-risk classification) belongs to **Article 6(2)**, not Article 50. It lists high-risk categories by area of use: biometrics, education, employment, essential services, law enforcement, and more. Emotion recognition sits in the **Biometrics** category, at Annex III point 1(c) — a system qualifies as high-risk there on its own, with no education or employment context needed.
- **Annex IV** (technical documentation) belongs to **Article 11(1)**, not Article 50. A team building the machine-readable marking solution required under Article 50(2) should not treat Annex IV as its checklist. Annex IV documents high-risk systems. Article 50(2) is a transparency duty that can apply regardless of risk classification.
- **Annex VIII** (database registration fields) belongs to **Article 49**, not Article 50. Registration applies to high-risk systems on the Annex III list. A deepfake-disclosure duty under Article 50 does not, on its own, create a registration duty.

The general rule: an Annex attaches only to the Article that names it. Article 50 does not name Annex III, IV, or VIII — so a system does not owe those Annexes just for having an Article 50 duty. It would need to separately trigger the Article that actually names the Annex (Article 6(2), 11(1), or 49). Check the Article's own text before you treat any Annex as a requirement.

## Reading checklist

- **Identify your role.** Your role as provider or deployer determines which parts of Article 50 apply to you.
- **Check the exemptions before you assume disclosure is necessary.** The "reasonably well-informed, observant and circumspect" test in Article 50(1), and the human-editorial-control exemption in Article 50(4), both depend on the facts of your setup.
- **Use Recitals to understand intent. Do not use a Recital to expand or replace an obligation.** A Recital explains why a rule exists. A Recital does not create a new duty.
- **Confirm that an Annex applies by checking the Article's own cross-reference.** Do not infer a link. Article 50 names no Annex, so do not treat Annex III, IV, or VIII as a checklist for it.

## Related reading

For the operational changes when Article 50 became enforceable on 2 August 2026, see [Article 50 Is Now in Force](/perspectives/eu-ai-act-article-50-in-force-2026/). For disclosure placement templates and the EU's official AI-content icon set, see the [full disclosure guide](/ai-guides/ai-generated-content-disclosure-eu-ai-act/).

---
*Want more guides like this? Browse all [Perspectives](/perspectives/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
