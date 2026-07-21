---
title: "EU AI Act Article 25: When You Become the AI 'Provider'"
date: 2026-07-21
lastmod: 2026-07-19
draft: false
description: "Under Article 25 of the EU AI Act, agencies can become the legal 'provider' of an AI system — and inherit every obligation. Here's how the flip happens."
keywords: ["EU AI Act Article 25 provider obligations", "when does a deployer become a provider", "substantial modification AI Act", "AI value chain responsibilities", "accidental AI provider agency", "EU AI Act compliance agencies", "Article 25 high-risk AI system"]
author: "Pranoti Kshirsagar"
reading_time: "6 min"
tags: ["EU AI Act", "Article 25", "AI provider", "agencies", "AI value chain"]
category: "perspectives"
sidebar_links:
  - title: "GPAI Code of Practice: Provider vs. Deployer, Explained"
    url: "/ai-guides/gpai-code-of-practice-provider-vs-deployer/"
  - title: "EU AI Act High-Risk Hiring AI: The Annex III Test"
    url: "/ai-guides/eu-ai-act-high-risk-hiring-ai-annex-iii-test/"
  - title: "EU AI Act Article 4 for Creator Agencies & Small Teams"
    url: "/perspectives/eu-ai-act-article-4-creator-agencies-small-teams/"
  - title: "EU AI Act AI System Register Template"
    url: "/ai-guides/eu-ai-act-ai-system-register-template/"
---

Most agencies I speak to have settled the EU AI Act in their heads as someone else's problem. They use AI tools, so they reason the heavy obligations sit upstream — with OpenAI, Anthropic, or whichever vendor built the model. What almost none of them have read is **Article 25**, the clause that quietly moves the provider's entire obligation set onto ordinary businesses through work they do every week.

This is the most overlooked liability transfer in the Act for creative, marketing, consulting and research agencies. It does not require you to build a model. It requires you to put a logo on something, adjust it, or point it at a new job — the exact activities agencies are paid for.

## You are probably not the "provider" you think you are

The EU AI Act splits the world into roles, and your obligations depend entirely on which one you occupy. A **provider** develops an AI system and places it on the market. A **deployer** uses one under its own authority. **Distributors** and **importers** move systems along the chain.

Agencies almost always assume they are deployers. It is the comfortable read: you licensed a tool, you use it for clients, the compliance burden belongs to whoever made it. For a genuine deployer of a high-risk system the duties are real but contained — human oversight, monitoring, using the system as instructed.

The provider role is a different weight class entirely. Providers of high-risk AI systems carry conformity assessment, technical documentation, the quality management system, registration in the EU database, and post-market monitoring. **The provider is the party the regulator holds responsible when the system causes harm.** Assuming you are a deployer when the law sees you as a provider is not a paperwork error — it is the difference between light-touch obligations and the full regime.

## The three ways Article 25 flips you into a provider

[Article 25(1)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-25) sets out exactly when a distributor, importer, deployer or other third party is "considered to be a provider" of a high-risk system and takes on the Article 16 provider obligations. There are three triggers, and each one maps onto something agencies do routinely.

| Trigger (Article 25(1)) | What it means | A typical agency version |
|---|---|---|
| **(a) Rebranding** | You put your name or trademark on a high-risk system already on the market | White-labelling a hiring or scoring tool under your own brand for a client |
| **(b) Substantial modification** | You modify a high-risk system so substantially that it stays high-risk | Re-engineering or deeply customising a system beyond its supplied configuration |
| **(c) Change of purpose** | You change the intended purpose so a system — including a general-purpose one — becomes high-risk | Wiring a general-purpose model into a CV-screening or credit-triage workflow |

Trigger (a) is the one that catches agencies off guard most. Putting your name on a high-risk system already placed on the market makes you its provider, unless your contract with the original maker allocates the obligations differently. The moment you present a tool to a client as *your* product, you may have adopted its entire legal weight.

Trigger (c) is the sleeper. It explicitly covers general-purpose AI systems that were *not* originally classified as high-risk — the everyday chat and automation models teams reach for. Point one of those at a use listed in Annex III, and you have not just deployed a tool; you have created a high-risk system and become its provider.

## What actually lands on you the moment you flip

Here is the part that turns an abstract clause into a genuine operational problem. Article 25(1) states that once you become the new provider, the original provider "shall no longer be considered to be a provider of that specific AI system." The upstream vendor steps out of the frame for that instance, and the responsibility stops with you.

You might expect the original maker to at least hand over what you need to comply. Article 25 does oblige them to cooperate and to "make available the necessary information" and reasonable technical access. But there is a carve-out: this duty does not apply where the original provider **"clearly specified that its AI system is not to be changed into a high-risk AI system."**

> If a vendor's terms say the tool must not be turned into a high-risk system, and you do it anyway, they owe you nothing — and you are the provider of something you cannot fully document.

This is where the flip bites hardest. Conformity assessment and technical documentation assume deep access to how the system was built and tested. An agency that becomes a provider through trigger (a) or (c) often has none of that, and no contractual right to demand it. You inherit the obligations without inheriting the information needed to meet them.

## The contract clause that decides who carries the risk

Article 25(4) is the quiet lever most teams never pull. It requires that a provider integrating a third party's tools, services or components into a high-risk system agree, **in writing**, the information, capabilities, technical access and other assistance needed for compliance. The one exception is tools provided under a free and open-source licence.

Read plainly, that means the paperwork you sign with your AI suppliers now decides your exposure. A written agreement that guarantees access to documentation and technical detail is the difference between a compliable position and an impossible one. No agreement, and the flip in Article 25(1) can leave you legally accountable with nothing to work from.

So before you integrate any AI tool that could touch a high-risk use, the contract is not an afterthought — it is the control. **Demand written terms covering documentation access, technical cooperation, and a clear statement of intended purpose.** Treat a vendor's refusal to provide them as the risk signal it is.

## What I'd do about it — before you touch another AI tool

The good news is that Article 25 is manageable once you stop assuming it does not apply to you. Based on the agencies I have worked with, this is the order I would tackle it in.

First, **map which of your AI uses could be high-risk in the first place.** Article 25 only flips you into a provider for high-risk systems, so this is the gate that decides whether any of it is relevant. The [Annex III test](/ai-guides/eu-ai-act-high-risk-hiring-ai-annex-iii-test/) is the fastest way to check the uses agencies most often stumble into, recruitment and scoring chief among them.

Second, **audit your work for the three triggers — name, modify, repurpose.** Go through your live client engagements and ask honestly whether you are branding, substantially modifying, or repurposing anyone's system into a high-risk use. This is a one-afternoon exercise that most teams have simply never run.

Third, **fix the contracts before the next integration.** Get the Article 25(4) written agreement in place, secure documentation and technical-access rights, and record the intended purpose of every system in [a register](/ai-guides/eu-ai-act-ai-system-register-template/) so you can prove what it was — and was not — meant to do.

None of this requires a legal department. It requires reading your own work the way a regulator would, and accepting that "we just use the tool" is not the safe harbour agencies assume it to be.

---

Article 25 is not an edge case buried in the Act for hyperscalers to worry about. It is a fairly precise description of what agencies and small teams do every single week — brand things, adapt things, repurpose things. The risk is not that the law is unreasonable; it is that the flip from user to provider happens silently, through ordinary work, and you only discover it when someone asks for the technical file you never had.

If you are integrating AI tools into client work and you are not sure which side of Article 25 you sit on, that uncertainty is itself the finding. [Get in touch →](/contact/) and we can map it before it maps you.

## Related reading on The Science Talk

This piece pairs with the [Article 4 AI-literacy explainer on The Science Talk](https://thesciencetalk.com/news/eu-ai-act-article-4-ai-literacy-research-institutes/) — useful background on how the Act's obligations reach ordinary organisations, not just AI developers.

---
*Browse all [Perspectives](/perspectives/) or [get in touch →](/contact/)*
