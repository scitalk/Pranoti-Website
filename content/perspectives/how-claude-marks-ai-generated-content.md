---
title: "Claude Will Watermark Its Own Output: What Anthropic's Marking Plan Means for You"
date: 2026-08-11
lastmod: 2026-08-11
draft: false
featured_image: "/images/ai-guides/eu-ai-act.webp"
hero_light: true
description: "Anthropic published its plan to mark AI-generated content under the EU Code of Practice: embedded text watermarks and C2PA metadata. Here is what it covers, what it misses, and why it does not replace your own disclosure duty."
keywords: ["Claude watermark AI content", "how Claude marks AI-generated content", "C2PA Claude", "Anthropic Article 50 marking", "machine-readable marking AI Act", "AI watermark detection limitations"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["EU AI Act", "Article 50", "AI transparency", "watermarking", "C2PA", "Claude"]
category: "perspectives"
pillar: "EU AI Act & Compliance"
sidebar_links:
  - title: "EU AI Act Article 50 Is Now in Force: What Changed on 2 August 2026"
    url: "/perspectives/eu-ai-act-article-50-in-force-2026/"
  - title: "How to add AI disclosures that comply with the EU AI Act"
    url: "/ai-guides/ai-generated-content-disclosure-eu-ai-act/"
  - title: "The Science Talk Signs the EU Code of Practice on Transparency of AI-Generated Content"
    url: "/perspectives/the-science-talk-signs-eu-code-of-practice-ai-transparency/"
sidebar_product:
  label: "AI Integration Guide"
  title: "Connect WordPress to Claude Desktop — MCP Setup Guide"
  bullets:
    - "Read, create and update posts — using plain language"
    - "No browser switching, no copy-pasting"
    - "Fully connected in under 15 minutes"
  details:
    - "Copy-paste config for Mac & Windows"
    - "Application Password walkthrough"
    - "7 troubleshooting fixes"
    - "Security best practices"
  stripe_url: "https://buy.stripe.com/bJe28railfNSaz70jm8Ra0p?utm_source=pranoti_site&utm_medium=sidebar&utm_campaign=claude_wordpress_mcp"
  cta: "Get the guide — €17 →"
  footnote: "Instant PDF delivery"
---

Anthropic [published its plan](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) to mark AI-generated content. It signed the EU AI Act's Article 50(2) Code of Practice as a provider of generative AI models and generative AI systems. This is the Section 1 half of the framework that [we signed under Section 2](/perspectives/the-science-talk-signs-eu-code-of-practice-ai-transparency/) as a deployer. Providers build the marking infrastructure. Deployers disclose. This document shows what the provider side will put in your hands.

## What Anthropic committed to

Anthropic gives four commitments:

- **New models mark from day one.** Claude models launched in the EU on or after 2 August 2026 support machine-readable marking at launch.
- **Marking applies everywhere.** Marks cover output from supported models across Claude Platform (API), Claude, Claude Code, Claude Cowork, and Claude Tag. This is worldwide, not only in the EU.
- **Anthropic will help you detect the marks.** Anthropic will support users and other third parties to detect Claude's marks. It will give the details in "forthcoming documentation."
- **Work on older models continues.** Models released before 2 August 2026 fall under the transition period. Anthropic continues to add marking support to them.

That last point matters more than it looks. Anthropic does not name the deadline, but the trigger date that it gives matches the law exactly. Regulation (EU) 2026/1744, the AI Omnibus, inserts a new Article 111(4) into the AI Act:

> "Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, that have been placed on the market before 2 August 2026 shall take the necessary steps in order to comply with Article 50(2) by 2 December 2026."

Recital 38 of the same regulation calls this a transitional period of four months. If you use a Claude model that shipped before August 2026, assume that its output has no mark yet. The backstop date is [2 December 2026](/perspectives/eu-ai-act-article-50-in-force-2026/).

## The two techniques

**Embedded watermarks in text.** A supported Claude model weaves an imperceptible watermark into the text itself. It does not change the meaning, the quality, or the readability. Because the watermark is part of the text, it travels through copy and paste, and "may persist through some editing." Anthropic applies the watermark at the model level. Thus the watermark is present in text from all Claude products.

**Signed provenance metadata in files.** For supported file types, specifically `.svg`, `.png`, and `.jpg`, Claude attaches signed metadata that follows the [C2PA](https://c2pa.org/) open standard. If the label is present, it shows that Claude processed the file. The label also shows you if a person changed the file after Claude processed it.

Coverage is different for each route. Embedded watermarks apply when you use supported models through AWS, Google Cloud, or Microsoft Foundry. But signed provenance metadata "may not be supported on every platform." If your pipeline uses Claude through a cloud partner, examine the file metadata before you rely on it.

## The limitations are the useful part

Anthropic is unusually direct about what the marks do not prove. It documents both failure directions.

**A mark does not show that Claude wrote the content.** People use Claude to proofread, translate, summarize, and convert files. The output carries a mark even when the ideas, the text, and the data came from a human source. A person can also change the content, or mix it with other material, after Claude processed it.

**A missing mark does not show that the content is free of AI.** Anthropic gives five reasons why a true AI-generated passage can carry no detectable mark:

- A model released before marking support generated the text.
- A person heavily edited, paraphrased, translated, or mixed the text into other writing.
- The passage is very short, and gives too little text for a reliable signal.
- Format conversion, a re-save, a screenshot, or another method stripped a file's metadata.
- The platform, the feature, or the file type did not support that mark type.

The two lists together give one practical conclusion. A mark is a provenance signal, not a verdict. It is not an AI detector for a freelancer's draft. It is also not evidence for a regulator that a person wrote a given piece.

## What this does not do for your compliance

The important sentence in Anthropic's article is the last one. If you deploy Claude in your own product, "you should independently assess what Article 50 requires of your products and services."

Machine-readable marking is the Article 50(2) obligation, and it sits on providers. The deployer duty is Article 50(4), and it is more narrow than people assume. It applies to image, audio or video content that constitutes a deep fake. It also applies to text "published with the purpose of informing the public on matters of public interest."

Article 50(5) then sets the manner. It says that you must give the information "in a clear and distinguishable manner at the latest at the time of the first interaction or exposure." No human can see a watermark. Thus a watermark does not obey the clear-and-distinguishable test. When Anthropic marks its output, that mark does not put a label on your blog post.

The two mechanisms work together. The provider makes the content traceable by machine. The deployer makes it legible to a person. You still need both.

## What to do now

1. **Do not change your disclosure practice.** Nothing here reduces what you owe your audience. If your workflow already obeys [the disclosure guide](/ai-guides/ai-generated-content-disclosure-eu-ai-act/), keep it.
2. **Make a note of the model versions that you use.** If you run pinned older model IDs in production, their output probably has no mark yet. Anthropic says that it will update its article. Examine the article again before December 2026.
3. **Do a test of your file pipeline.** Anthropic names format conversion, a re-save, a screenshot, and "other means" as ways to strip a file's metadata. If provenance metadata is important to your client work, find where your pipeline removes it.
4. **Do not build an AI-detection policy on this.** By the provider's own account, neither direction of the signal is conclusive. Do not treat a missing watermark as proof that a person wrote the content.
5. **Watch for the detection documentation.** The technical guidance on how to find the marks is not available yet. That guidance is the part that makes this useful to a deployer.

## Why this matters

Anthropic wrote this Code of Practice commitment as engineering work, not as a statement of intent. The article gives a named standard, named file types, and named products. It gives a worldwide scope, not an EU-only scope. Its limitations section argues against the marketing value of the document itself.

The article also confirms the shape of the split that we described when we signed. Providers build the plumbing. Deployers tell the audience. The plumbing will not do the telling for you, and this article says so clearly.

---
*Want more guides like this? Browse all [Perspectives](/perspectives/) or [get in touch →](/contact/)*
