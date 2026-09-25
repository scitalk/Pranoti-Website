---
title: "The ERC Projects Database: A Research Tool for ERC Proposal Writers"
date: 2026-09-10
lastmod: 2026-09-25
draft: false
layout: "longform"
subtitle: "A clean, filterable database of 12,133 ERC-funded projects that gives proposal writers their funding landscape in seconds."
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

*Last reviewed and updated on 25 September 2026.*

**Date:** September 2026\
**Domain Focus:** Scientific Research Funding & Impact Management\
**Services:** Data cleaning, information design, web development, technical SEO\
**Tools:** Google Sheets, Python, Hugo, GitHub Pages, Cloudflare, Google Search Console, Claude Code\
**Live page:** [https://pranoti.thesciencetalk.com/erc-projects-database/](https://pranoti.thesciencetalk.com/erc-projects-database/)

---

## Executive Summary

An ERC proposal writer must know what the ERC already funds in their scheme and research domain. This knowledge shapes how they position an idea, show that it is new, and present its ambition. The data is public, but it is in an official dashboard where it is difficult to find.

This case study shows the ERC Projects Database, a single web page. The source is the European Commission's ERC dashboard export. I cleaned 238,842 raw data points and found no duplicate records. The page lists 12,133 funded projects from 2016 to 2025. Users filter by call year, grant scheme and research domain, and read the results as simple project cards. Each filtered view has its own URL, so users can bookmark it.

The page is about 157 KB (18 KB compressed), and Google indexes it. It gives an applicant a clear view of their funding landscape in seconds.

---

## Challenge: Information Overload and Poor UX/UI

Before scientists write and submit a proposal to a European Research Council (ERC) grant scheme, they must know what the ERC already funds in their scheme and domain. They need answers to practical questions. What does the ERC fund in my domain in recent calls? Is a funded project already close to my idea? Which institutions and countries host funded projects in my scheme? How do funded projects frame their titles and ideas?

This is market research. It is also a source of ideas, because funded projects show how successful applicants frame ambitious ideas.

The ERC publishes this data through the European Commission's Qlik dashboard. The dashboard holds the information, but it is difficult to use, for four reasons:

- **Information overload.** All information is on the screen at the same time, so the necessary information is hard to find.
- **Difficult filters.** It takes effort to limit the results by scheme, year and domain.
- **Too many hyperlinks.** One accidental click opens a new tab or window. Then the user must start the filtered search again.
- **No saved views.** The URL does not keep the selections. Thus, users cannot bookmark a view or send it to a colleague.

The result is that researchers do not do the research, or do it badly. This occurs at the stage where the research is most important.

---

## Solution: A dynamic database that is easy to navigate

The ERC Projects Database is one page that shows each funded ERC project from 2016 to 2025. It has three filters and simple project cards. It does not replace CORDIS or the ERC dashboard. It gives applicants a fast overview, and a link to CORDIS for the full record.

The solution has six parts: data collection, data cleaning, coverage examination, field selection, page design, and page structure for speed and search visibility.

### 1. Complete dataset

I exported the full ERC dashboard dataset on 21 September 2026: 13,269 rows in 18 columns. The dataset covers Starting, Consolidator, Advanced, Synergy and Proof of Concept grants from 2015 to 2025. That is 238,842 data points. I removed the 1,089 projects from the 2015 call, so the database starts at 2016.

The Google Sheets API had response-size limits. Thus, I used one CSV export and processed it in a single pass. All rows stay complete, and batches cannot become misaligned.

### 2. Data cleaning

The raw export looked complete, but it had problems that can mislead users:

- **Duplicate records.** A row is a duplicate only when all of its fields match another row. The export had 0 duplicates. Some projects use the same acronym, but they are different projects, so I kept them all.
- **Partner rows.** The export showed grants with multiple host institutions as a main row plus a "partner" row. The partner row had no acronym, title or funding. The export had 47 of these rows. They increased the project count. I made sure that each one had a matching main record before I removed it. Thus, no project was lost.
- **Placeholder values stored as text.** The export writes empty cells as "-". I counted these 3,718 values as empty, so they do not increase the size of the dataset. That leaves 235,123 genuine data points.
- **Combined institution fields.** Each host institution field had a name, an ID and a country code. Multi-host grants had several institutions in one cell. I removed the IDs and country codes from each name, also inside multi-host cells. The database covers 943 host institutions, the ERC's own count, in 35 countries.
- **Format errors.** 750 text fields, not including abstracts, had unwanted line breaks or spaces. The dates needed a standard format.

### 3. Coverage examination

I compared the coverage with the ERC's own published results. Users must know two facts:

- **2025 Advanced Grants.** The first export did not have these grants, because the ERC did not sign the grant agreements yet. The September 2026 export has 223 of them.
- **The 2021 Proof of Concept round is under 2022.** Official EU databases list that call under its legal code, ERC-2022-PoC1. The data is correct, but the label is different from the ERC announcement.

### 4. Only the fields an applicant needs

Most of the 18 columns do not help a user who scans the funding landscape. I kept 11 fields and removed abstracts, region, project numbers and the columns that the page can calculate from the call and panel codes. The final dataset has 133,463 data points. Each project card shows:

- **Project.** The acronym and full title.
- **Researcher.** The principal investigator.
- **Host.** The host institution and country.
- **Call.** The call year and grant scheme.
- **CORDIS link.** A direct link to the full project record.

### 5. Design for a quick overview

The page design shows the funding landscape without information overload:

- **Three filters.** The filters are call year, grant scheme and research domain. The domains are Physical Sciences and Engineering, Life Sciences, and Social Sciences and Humanities. These filters agree with how applicants think.
- **Sorted filter options.** The largest schemes and domains are first. The newest year is first.
- **Card grid.** The page shows 24 projects at a time, with back and forward navigation. It does not show thousands of rows at the same time.
- **Shareable URLs.** When a user selects 2024, Starting Grant and Life Sciences, the address bar becomes that search. The user can bookmark or share it, and it opens on the same results later.
- **Stable search.** CORDIS links do not change the filtered view.
- **One-click reset.** A click on the page title resets all filters.
- **Summary strip.** The page shows the scale at a glance: €22,062M in EU contribution, 12,133 projects, 35 countries, 943 host institutions.

### 6. Structure for speed and search

A database of this size can easily make a slow page. The first version had the full dataset inside the page, 4.24 MB of HTML. I changed the structure:

- **Separate data file.** The dataset loads as a separate cached file, so the page is about 157 KB (18 KB compressed).
- **Server-rendered first page.** The first 24 projects are in the page itself, with real CORDIS links. Thus, search engines and AI tools can read the content without scripts.
- **Structured data.** Dataset, CollectionPage and BreadcrumbList markup tells search engines what the page is.
- **Pages not made.** I did not make thousands of thin per-project pages or hundreds of paginated pages. These pages decrease the quality of the site in search results. They give no value to a real user.

---

## Impact

### Faster research for applicants

An applicant does not need a difficult dashboard. They open one page and select their scheme, domain and year. In seconds, they read the projects that define their competitive landscape. They can bookmark that view and use it again while they write. They can open each project on CORDIS and keep their place on the page.

### Reliable data

The page covers 12,133 funded ERC projects from 2016 to 2025. It includes 943 host institutions, 35 countries and €22,062M in EU contribution. Of the 238,842 raw data points, 235,123 are genuine data points after cleaning, and 133,463 are on the page. I removed 47 partner rows, so the project count and the funding totals are correct.

### Speed and visibility

The page weight decreased from 4.24 MB to about 157 KB (18 KB compressed). Google indexes the page, and the Dataset rich result is valid. Thus, applicants can find the tool through search, and it loads quickly.

---

## Community Response

I announced the ERC Projects Database in a [LinkedIn post](https://lnkd.in/p/e34AfqQP). In one week, the post got 199 reactions, 14 comments and 14 reposts. The post shows the figures from the first export (11,907 projects and €21.5 billion).

![LinkedIn post that announced the ERC Projects Database, with a screenshot of the filters and project cards](/images/case-studies/erc-projects-database-linkedin-post.png)

---

## Work With Me

Most research organizations already have valuable data: grant records, project portfolios, publication lists and funding outcomes. This data stays in exports, spreadsheets and dashboards that are difficult to use.

My name is Dr. Pranoti Kshirsagar, and I design clean, easy tools from this data that give value to your audience in seconds. These audiences include researchers who prepare proposals, grant offices that support applicants, and funders that show their impact.

**Get in touch:** [https://thesciencetalk.com/contact-us/](https://thesciencetalk.com/contact-us/)
