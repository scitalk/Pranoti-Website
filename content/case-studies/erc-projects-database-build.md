---
title: "Building the ERC Projects Database: 11,907 Grants, One Static Page"
date: 2026-09-10
draft: false
subtitle: "The ERC publishes this data behind a Qlik dashboard that loses your filters on a stray click. Same data, one page you can browse and bookmark."
category: "AI Integration"
display_category: "Data Engineering"
tech_stack:
  - "EC R&I Dashboard (Qlik Sense)"
  - "Python"
  - "Claude Code"
  - "Hugo"
  - "GitHub Actions"
  - "Schema.org JSON-LD"
  - "Google Search Console"
metrics:
  - value: "11,907"
    label: "ERC projects, 2016–2025"
  - value: "4.24 MB → 43 KB"
    label: "page weight after rebuild"
  - value: "€21,485M"
    label: "EU funding, reconciled"
problem:
  goal: "The ERC's grant data is already public and already on a dashboard, so the goal was never access. It was **a version a researcher would actually use** — pick a year, a scheme and a domain, and see who was funded without losing your place."
  reality: "The [official Qlik dashboard](https://dashboard.tech.ec.europa.eu/qs_digit_dashboard_mt/public/sense/app/c140622a-87e0-412e-8b29-9b5ddd857e13/sheet/61a0bd1d-cd6d-4ac8-8b55-80d8661e44c0/state/analysis) holds everything and shows too much of it at once, and **almost every element is a link**, so one stray click opens a new tab and the filters you built up are gone. **Nothing you select is held in the URL**, so there is no bookmark to return to and nothing to send a colleague."
workflow:
  before:
    - "Open the ERC's Qlik dashboard"
    - "Set filters one at a time"
    - "Click a link, land in a new tab"
    - "Go back, filters gone, start again"
  after:
    - "Open one page"
    - "Tick year, scheme, domain"
    - "Bookmark the URL, it is your view"
    - "Come back later, same set"
misconception: "\"The official dashboard number is the right number.\" The EC reports 11,908 projects and €21,487M, but **46 continuation rows for multi-institution grants each repeat their grant's full amount**, double-counting €132.7M — the reconciled figures are 11,907 projects and €21,485M."
blockers:
  - issue_title: "Version one shipped the whole database inside the HTML"
    issue_desc: "The first build inlined the full dataset into a hidden script tag. Fetched as Googlebot, the page was 4,236,868 bytes. Client-side pagination showed nine cards at a time but did nothing to the payload — every visitor downloaded all 11,953 rows to see nine of them."
    solution: "**Emit the dataset as a fingerprinted resource and fetch it.** Hugo writes `data.<hash>.json` beside the page, so the browser caches it separately and a data refresh changes the URL. The HTML dropped to **43 KB live**."
  - issue_title: "Google saw an empty page"
    issue_desc: "Raw HTML held an H1, a lede and an empty div. Every card, filter and CORDIS link was built by JavaScript, so Bing, LLM crawlers and social previews got nothing, and Search Console showed no referring URLs beyond the footer."
    solution: "**Server-render the first 24 cards with real links, then hydrate.** The template ranges over the data at build time, so crawlers and no-JS visitors get 24 projects and **24 real CORDIS links** in the document before any script runs."
  - issue_title: "Duplicate rows that were not duplicates"
    issue_desc: "11,953 rows but only 11,907 unique CORDIS IDs. The 46 extras were continuation rows — a multi-host project stored as a primary row plus one row per extra institution, with `-` in acronym, dates and contribution. A first dedupe kept the wrong twin and wrote `-` into 46 money fields."
    solution: "**Dedupe on CORDIS ID and keep the row that carries the amount**, then split the packed host field on every `[id,CC]` tag rather than the trailing one. That parse returned **943 distinct institutions, matching the ERC dashboard exactly**."
outcomes:
  - "**Every filtered view has its own URL.** Tick 2024, Starting Grant, Life Sciences and the address bar becomes that search — bookmark it, send it, open it in six months on the same set. Qlik holds no selection in its URL, so there is nothing there to save."
  - "**One indexed URL at 43 KB** with 24 crawlable projects in the source and `Dataset`, `CollectionPage` and `BreadcrumbList` schema. The Dataset rich result passes in Search Console."
  - "**A credibility strip that reconciles to the data beneath it** — €21,485M, 11,907 projects, 35 countries, 943 host institutions — every figure computed from the served file rather than copied off the dashboard."
  - "**Refreshing the database is one file.** The 1 September update added start date, end date and EU contribution per project and normalised 600 malformed fields, and shipped in a single commit."
architecture:
  - ["Data source", "**EC R&I Dashboard**, Qlik Sense, filtered by call year only — 11,953 rows × 18 columns, exported 26 Aug and re-exported 1 Sep 2026"]
  - ["Cleaning", "**46 continuation rows removed** on CORDIS ID; 2,870 `-` placeholders treated as empty; 12 of 18 columns kept, abstracts and panel codes dropped"]
  - ["Build", "**Hugo server-renders 24 cards**, emits the dataset as a fingerprinted JSON resource, and injects the Dataset, CollectionPage and Breadcrumb schema"]
  - ["Interactive layer", "**Vanilla JS, no framework** — fetch once, filter 11,907 objects in memory, render 24 cards, write the filter state into the URL"]
  - ["Deploy", "**Push to `main` → GitHub Actions → `gh-pages` → Cloudflare**, live in about 30 seconds and verified by fetching the deployed HTML"]
reflection: "This was never about getting the data — the Commission publishes all of it and the export took minutes. The real work was deciding what to leave out, six of eighteen columns and every abstract, so that what remained could be read at a glance. And every expensive mistake here was a confidence mistake rather than a skill one: the page that rendered beautifully while shipping 4 MB, the dedupe that matched on row count while writing `-` into 46 money fields."
cta_text: "Open the database, filter by your scheme, and bookmark the view — the resource kit for that scheme is one click from the hero."
guide_url: "https://pranoti.thesciencetalk.com/erc-projects-database/"
related_tst_posts:
  - title: "ERC Guidelines on AI in Grant Proposal Evaluation — The Science Talk"
    url: "https://thesciencetalk.com/services/grants-fundraising/erc-ai-grant-proposal-evaluation-guidelines/"
  - title: "How I Used GenAI to Support €1M Grant Proposals — The Science Talk"
    url: "https://thesciencetalk.com/news/ai-tools-for-proposal-writing/"
---
