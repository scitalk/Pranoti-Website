---
title: "The ERC Projects Database: A Research Tool for ERC Proposal Writers"
date: 2026-09-10
lastmod: 2026-09-11
draft: false
layout: "longform"
subtitle: "A clean, filterable database of 11,907 ERC-funded projects that gives proposal writers their funding landscape in seconds."
category: "AI Integration"
display_category: "Data Engineering"
tech_stack:
  - "Google Sheets"
  - "Python"
  - "Hugo"
  - "GitHub Pages"
  - "Cloudflare"
  - "Google Search Console"
  - "Claude Code"
---

*Last reviewed and updated on 11 September 2026.*

**Date:** September 2026\
**Domain Focus:** Scientific Research Funding & Impact Management\
**Services:** Data cleaning, information design, web development, technical SEO\
**Tools:** Google Sheets, Python, Hugo, GitHub Pages, Cloudflare, Google Search Console, Claude Code\
**Live page:** [https://pranoti.thesciencetalk.com/erc-projects-database/](https://pranoti.thesciencetalk.com/erc-projects-database/)

---

## Executive Summary

Anyone writing an ERC proposal needs to know what the ERC has already funded in their scheme and research domain. That knowledge shapes how you position an idea, how you show it is new, and how you pitch its ambition. The data is public, but it sits in an official dashboard that makes finding it a chore.

I took the European Commission's ERC dashboard export and cleaned it: 215,153 raw data points, 46 duplicate records removed. The result is a single web page listing 11,907 funded projects from 2016 to 2025. You filter by call year, grant scheme and research domain, and read the results as simple project cards. Every filtered view has its own URL, so you can bookmark it and come back later. The page is about 40 KB, indexed by Google, and gives an applicant a clear view of their funding landscape in seconds.

---

## The Challenge

### Proposal writing starts with market research

Before writing an ERC proposal, a researcher needs answers to practical questions:

- What has the ERC funded in my domain in recent calls?
- Has a project close to my idea already been funded?
- Which institutions and countries host funded projects in my scheme?
- What do funded project titles and framings look like?

This is market research. It also gives you inspiration: reading funded projects shows how successful applicants frame ambitious ideas.

### The official source gets in the way

The ERC publishes this data through the European Commission's Qlik dashboard. It holds the information, but using it is a poor experience:

- **Information overload.** Everything is on screen at once, so the information you need is hard to find.
- **Cumbersome filters.** Narrowing results by scheme, year and domain takes effort.
- **Too many hyperlinks.** One stray click opens a new tab or window, and you start your filtered search again from scratch.
- **No saved views.** Your selections are not kept in the URL, so there is nothing to bookmark and nothing to send a colleague.

The result: researchers skip the research, or do it badly, at exactly the stage when it matters most.

---

## Strategic Solution

### 1. Collect the complete dataset

I exported the full ERC dashboard dataset: 11,953 rows across 18 columns, covering Starting, Consolidator, Advanced, Synergy and Proof of Concept grants from 2016 to 2025. That is 215,153 data points.

Pulling it through the Google Sheets API hit response-size limits, so I switched to one CSV export processed in a single pass. That keeps every row intact and removes the risk of misaligned batches.

### 2. Clean the data before anything goes on the page

The raw export looked complete but carried problems that would have misled users:

- **Duplicate records.** Grants with several host institutions were exported as a main row plus a "continuation" row with placeholder values. There were 46. Left in, they inflated the project count and double-counted funding. I removed them after confirming each one had a matching main record, so no project was lost.
- **Placeholder values stored as text.** The export writes empty cells as "-". Treating those 2,870 values as data would overstate the dataset, so I counted them as empty. That leaves 211,455 genuine data points.
- **Packed institution fields.** Host institutions were stored as a name plus an ID and country code, with several institutions in one cell for multi-host grants. Parsing them properly gives 943 distinct host institutions across 35 countries.
- **Formatting junk.** More than 500 text fields had stray line breaks or spacing, and dates needed converting to a standard format.

I also checked coverage against the ERC's own published results and found two things users need to know:

- **2025 Advanced Grants are missing.** Those grant agreements were not yet signed, so they are not in the dashboard. When a user filters for them, the page shows a note linking to the ERC's official results list.
- **The 2021 Proof of Concept round is filed under 2022.** Official EU databases list that call under its legal code, ERC-2022-PoC1. The data is correct, just labelled differently from how the ERC announced it.

### 3. Keep only what an applicant needs

Most of the 18 columns don't help someone scanning the funding landscape. I kept 12 fields and dropped abstracts, panel codes, region and call codes. The CORDIS link on every card gives the full record for anyone who wants depth. The final dataset holds 142,883 data points.

Each project card shows:

- Project acronym and full title
- Principal investigator
- Host institution and country
- Call year and grant scheme
- A direct link to the project on CORDIS

### 4. Design for quick overview, not information overload

- **Three filters that match how applicants think:** call year, grant scheme and research domain (Physical Sciences and Engineering, Life Sciences, Social Sciences and Humanities).
- **Filter options sorted by size**, so the largest schemes and domains come first. Years run newest first.
- **A clean card grid** with 24 projects per page and simple back and forward navigation, instead of thousands of rows at once.
- **Every filtered view has its own URL.** Tick 2024, Starting Grant and Life Sciences, and the address bar becomes that search. Bookmark it, share it, and it opens on the same results later.
- **CORDIS links don't disrupt your search.** Your filtered view stays intact.
- **One click on the page title resets all filters.**
- **A summary strip** shows the scale at a glance: €21,485M in EU contribution, 11,907 projects, 35 countries, 943 host institutions. Every figure comes from the cleaned data beneath it.

### 5. Build it to load fast and be found

A database this size can easily become a slow page. The first version put the entire dataset inside the page, 4.24 MB of HTML. I restructured it:

- **The dataset loads as a separate cached file**, so the page is about 40 KB.
- **The first 24 projects are built into the page itself**, with real CORDIS links, so search engines and AI tools can read the content without running scripts.
- **Structured data (Dataset, CollectionPage, BreadcrumbList)** tells search engines what the page is.
- **Deliberately not built:** thousands of thin per-project pages or hundreds of paginated pages. They would dilute the site's quality in search results and add nothing for a real user.

---

## Quantifiable Impact

| Measure | Result |
|---|---|
| Funded ERC projects, 2016 to 2025 | 11,907 |
| Raw data points collected | 215,153 |
| Genuine data points after cleaning | 211,455 |
| Data points on the page | 142,883 |
| Duplicate records removed | 46 |
| Host institutions | 943 |
| Countries | 35 |
| EU contribution covered | €21,485M |
| Page weight | 4.24 MB reduced to about 40 KB |
| Search status | Indexed by Google, Dataset rich result valid |

**For an applicant, the difference is practical.** Instead of fighting a dashboard, they open one page, pick their scheme, domain and year, and within seconds are reading the projects that define their competitive landscape. They can bookmark that view, return to it while drafting, and follow any project through to CORDIS without losing their place.

---

## Work With Me

Most research organisations already sit on valuable data: grant records, project portfolios, publication lists, funding outcomes. It stays locked in exports, spreadsheets and dashboards nobody enjoys using.

I turn that data into clean, accessible tools your audience gets value from in seconds: researchers preparing proposals, grant offices supporting applicants, funders showing their impact.

**Get in touch:** [https://thesciencetalk.com/contact-us/](https://thesciencetalk.com/contact-us/)
