# Portfolio Page Creator — Cowork Instructions

## CONTEXT

You are working on **pranoti.thesciencetalk.com**, a Hugo static site.
The site root is: `/Users/pranotikshirsagar/Documents/CLAUDE/Product/Pranoti_Website/`

The portfolio section has 5 categories: **shorts**, **video**, **podcast**, **trainings**, **proposal**.
Each category has its own content folder, layout template, and card style on the portfolio grid page.

---

## YOUR TASK

Create `.md` content pages for each portfolio category using data from a CSV file.
**Start with shorts.** Then move to other categories if Pranoti asks.

---

## FOLDER MAP

```
Pranoti_Website/
├── content/portfolio/
│   ├── _index.md              ← portfolio landing page config
│   ├── shorts/
│   │   ├── _index.md          ← section config (don't edit)
│   │   └── {slug}.md          ← one file per guest = one page
│   ├── video/                 ← same pattern
│   ├── podcast/               ← same pattern
│   ├── trainings/             ← same pattern (some pages already exist)
│   └── proposal/              ← same pattern (some pages already exist)
├── layouts/portfolio/
│   ├── list.html              ← portfolio grid page with tab filters
│   ├── shorts/single.html     ← shorts detail page template
│   ├── video/single.html
│   ├── podcast/single.html
│   ├── trainings/single.html
│   └── proposal/single.html
└── static/images/
    ├── trainings/             ← training photos (already populated)
    └── portfolio/             ← other portfolio images
```

---

## DATA SOURCE

**CSV file:** `TST-Guest_Episode-Links_-_Guest_Season_Episode__1_.csv`
This file lives on Claude's computer at: `/mnt/user-data/uploads/TST-Guest_Episode-Links_-_Guest_Season_Episode__1_.csv`
If not found there, ask Pranoti to re-upload it.

### CSV columns

| Col | Letter | Field |
|-----|--------|-------|
| 0 | A | Release year |
| 1 | B | Guest name |
| 2 | C | Season # (e.g. S6) |
| 3 | D | Episode # in season (e.g. E4) |
| 4 | E | Episode number overall |
| 5 | F | YouTube Full Episode Link |
| 6 | G | YouTube short episode link (single short edit of full ep) |
| 7 | H | YouTube shorts #1 |
| 8 | I | YouTube shorts #2 |
| 9 | J | YouTube shorts #3 |
| 10 | K | YouTube shorts #4 |
| 11 | L | YouTube shorts #5 |
| 12 | M | YouTube shorts #6 |
| 13 | N | YouTube shorts #7 |
| 14 | O | YouTube shorts #8 |
| 15 | P | YouTube shorts #9 |
| 19 | T | Spotify episode link |

---

## TASK 1: CREATE SHORTS PAGES

### What qualifies as "has shorts"

A guest qualifies ONLY if they have data in **columns G through O** (index 6–14) that are actual YouTube Shorts URLs.

**CRITICAL:** Some guests have a link in col G (short episode link) or col H that is NOT a short — it may be a shortened edit of the full episode. Cross-check: if a guest has only ONE link and it's in col G or H with no other shorts, **flag it for Pranoti to verify** before creating a page. Guests with 2+ links across cols G–O are safe to create.

### How to handle duplicates

Some guests appear on multiple CSV rows (multiple episodes). Combine all their shorts into ONE page.

### Frontmatter template for shorts

```yaml
---
title: "Under the Microscope Shorts — {Guest Name}"
date: {YYYY-MM-DD}
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with {Guest Name}."
client: "{Guest Name}"
youtube_urls:
  - "https://youtu.be/XXXXX"
  - "https://youtu.be/YYYYY"
youtube_full: "{col F link}"
spotify: "{col T link}"
tags: ["podcast shorts", "{Season}"]
category: "shorts"
---
```

### Key fields explained

- **youtube_urls** — YAML list. The template iterates this list and embeds each as a 9:16 iframe. This is the main content.
- **youtube_full** — link to the full episode (for reference, not displayed in current template)
- **spotify** — Spotify episode link (for reference)
- **date** — approximate from season/year. Use: `{year}-{month}-01` where month = `min(1 + episode_num // 4, 12)`
- **category** — must be exactly `"shorts"` (drives the portfolio grid filter)
- **type** — must be exactly `"portfolio/shorts"` (drives Hugo template selection)

### Slug format

Kebab-case from guest name: `pascale-senellart.md`, `brian-gerardot.md`

### File location

Write each file to:
`/Users/pranotikshirsagar/Documents/CLAUDE/Product/Pranoti_Website/content/portfolio/shorts/{slug}.md`

### Name formatting

- Fix double spaces (e.g. "Andrew  Care" → "Andrew Care")
- Capitalise first letter of each word if name is all-lowercase in CSV
- Preserve original casing otherwise (e.g. "McElwee-White" stays as-is)

---

## EXISTING PAGES (DO NOT RECREATE)

These already exist in the shorts folder. Skip them:
- `andrew-care.md`
- `anna-ploszajski.md`

Check what exists BEFORE creating: `Filesystem:list_directory` on the shorts content folder.

Also check for a `clara-barker.md` — if it exists with `draft: true`, delete it. Clara Barker does NOT have real shorts.

---

## PAGES TO CREATE (29 remaining)

Create these from the CSV. All data has been verified:

1. Sebastian Maehrlein (S3, 1 short)
2. Tiffany Harte (S3, 5 shorts)
3. Susi Seibt (S4, 2 shorts)
4. Rebecca Katharina Pittkowski (S4, 1 short)
5. Andy Soder Anke (S4, 1 short)
6. Claire Dancer (S4, 2 shorts)
7. Lisa McElwee-White (S5, 1 short)
8. George Mihailescu (S5, 3 shorts)
9. Julio Terra (S5, 2 shorts)
10. Jodie Bradby (S5, 2 shorts)
11. Steven Street (S5, 2 shorts)
12. Antonio Manesco (S5, 2 shorts)
13. Doris Reiter (S6, 9 shorts)
14. Narayanan T N (S6, 3 shorts)
15. Tobias Heindel (S6, 5 shorts)
16. Armando Rastelli (S6, 5 shorts)
17. Rinaldo Trotta (S6, 1 short)
18. Jens Osterhoff (S6, 8 shorts)
19. Carlos Anton Solanas (S6, 5 shorts)
20. Pascale Senellart (S6, 8 shorts)
21. Mete Atature (S6, 8 shorts)
22. Francesca Calegari (S6, 4 shorts)
23. Emanuele Pelucchi (S6, 3 shorts)
24. Elisa Riedo (S6, 4 shorts)
25. Brian Gerardot (S6, 3 shorts)
26. Wolfgang Loeffler (S6, 2 shorts)
27. Anna Musial (S7, 1 short)
28. Martin Rejhon (S7, 2 shorts)
29. Krist V. Gerneay (S7, 2 shorts)

---

## WORKFLOW

1. **Read the CSV** from `/mnt/user-data/uploads/` (copy to Claude's computer if needed using `Filesystem:copy_file_user_to_claude`)
2. **List existing pages** in the shorts content folder
3. **Parse CSV** — extract all guests with shorts (cols G–O), group by guest name
4. **Flag ambiguous cases** — guests with only 1 link in col G or H, ask Pranoti
5. **Generate .md files** — write each directly using `Filesystem:write_file`
6. **Report** — list all created pages with guest name and short count
7. **Tell Pranoti** to run `hugo server` to preview

---

## TEMPLATE REFERENCE

The shorts single page template is at:
`layouts/portfolio/shorts/single.html`

It uses `{{ range .Params.youtube_urls }}` to loop through and embed each short as a 9:16 iframe. This is why `youtube_urls` must be a YAML list, not a single string.

The portfolio grid page (`layouts/portfolio/list.html`) filters cards by `data-category` which reads from the `.Params.category` frontmatter field. Cards without a `thumbnail` get a coral-coloured placeholder with the category name.

---

## RULES

- UK spelling in all generated text (organised, recognised, etc.)
- Positive framing in descriptions
- `category: "shorts"` exactly — drives the grid filter
- `type: "portfolio/shorts"` exactly — drives Hugo template
- Never overwrite existing `.md` files without asking
- Don't create `_index.md` — it already exists
- Date format: `YYYY-MM-DD` (Hugo requirement)
- One page per guest, all their shorts combined

---

## AFTER SHORTS: NEXT CATEGORIES

Once shorts are done, Pranoti may ask to create pages for **video**, **podcast**, etc. Same CSV, different columns. The pattern is identical:
- Read the relevant columns from CSV
- Match to the correct template frontmatter (check the `layouts/portfolio/{category}/single.html` for required fields)
- Write `.md` files to `content/portfolio/{category}/`

For **trainings**: pages already exist with images in `static/images/trainings/`. Check before creating duplicates.

---

## GIT & DEPLOYMENT SETUP

### Overview

The site uses **GitHub Pages** via GitHub Actions. Netlify is no longer used.

### Key details

- **GitHub repo:** `https://github.com/scitalk/Pranoti-Website` (public)
- **Branch:** `main` (source) → `gh-pages` (built site)
- **Hosting:** GitHub Pages at `pranoti.thesciencetalk.com`
- **Build command:** `hugo --environment production --minify` (run by GitHub Actions)
- **Hugo version:** 0.139.0 (set in `.github/workflows/deploy.yml`)
- **DNS:** Cloudflare CNAME `pranoti` → `scitalk.github.io`

### How deploys work

Every `git push` to `main` triggers GitHub Actions automatically (~30 seconds). No manual steps needed.

### .gitignore — what is excluded from Git

These files/folders are intentionally excluded and stay on your Mac only:

```
public/
.DS_Store
.netlify/
.hugo_build.lock
.trash/
.claude/
resources/_gen/
themes/
static/case-studies/*.pdf
static/case-studies/*.html
static/reports/
```

### Deploy workflow

```bash
# Check what has changed
git status

# Stage specific files
git add content/portfolio/events/new-event.md

# Or stage everything
git add .

# Commit
git commit -m "describe what changed"

# Push to GitHub → triggers GitHub Actions auto-deploy
git push
```

### Local tinkering vs deploying

- Editing files locally **never** affects GitHub or the live site
- Run `hugo server` to preview locally at `http://localhost:1313`
- Only files you explicitly `git add` + `git commit` + `git push` get deployed

### Authentication

- **GitHub username:** `scitalk`
- **Password:** Personal Access Token with `repo` + `workflow` scopes (generated at github.com/settings/tokens) — NOT your GitHub account password
- Token expiry: renew when GitHub sends reminder email
