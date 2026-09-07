# Pranoti Website — Claude Instructions

## Site overview

- **URL:** https://pranoti.thesciencetalk.com
- **Stack:** Hugo static site (v0.139.0)
- **Site root:** `/Users/pranotikshirsagar/CLAUDE/Product/Pranoti_Website/`
- **GitHub repo:** https://github.com/scitalk/Pranoti-Website (public)

---

## Deployment — GitHub Pages (NOT Netlify)

The site is hosted on **GitHub Pages**. Netlify is no longer used.

Every `git push` to `main` triggers GitHub Actions automatically:
- Workflow file: `.github/workflows/deploy.yml`
- Hugo builds to the `gh-pages` branch
- Site goes live at https://pranoti.thesciencetalk.com within ~30 seconds

### Deploy workflow

```bash
git add <files>
git commit -m "describe what changed"
git push
```

That's it. No manual build or upload steps needed.

### Never do these (Netlify is gone):
- Do not reference `netlify.toml` for deploy config (it still exists but is unused)
- Do not suggest `npx netlify-cli deploy`
- Do not suggest dragging `public/` anywhere
- Do not suggest Netlify dashboard

---

## Local preview

```bash
hugo server
# Preview at http://localhost:1313
```

---

## Publishing strategy

Posts are published based on their **date field**, not `draft` status:
- `draft: false` + date in past/today → post appears immediately
- `draft: false` + future date → post hidden until that date arrives
- `draft: true` → post never appears (regardless of date)

This enables **staggered publication** for SEO strategy. Example: adding three guides on April 28 with dates Apr 28, May 1, May 4 will publish them one at a time as their dates arrive.

**Config:** `publishFuture = true` in hugo.toml enables this behavior.

---

## File editing rules

- **Never edit `public/`** — it is Hugo build output, regenerated on every build
- All changes go in: `static/`, `content/`, `layouts/`, `hugo.toml`, `data/`
- Hugo version: 0.139.0 (set in `.github/workflows/deploy.yml`)

---

## Site structure

```
content/
├── portfolio/         ← LIVE (video, shorts, podcast, trainings, scicommai, events, reports) — `proposal` category removed 2026-08-06 (commit 611034d3)
├── case-studies/      ← LIVE
├── ai-guides/         ← LIVE
├── perspectives/      ← LIVE
├── products/          ← LIVE — product pages (e.g. erc-adg-2026.md, erc-cog-2027.md, erc-stg-2027.md, erc-synergy-2026.md), rendered via layouts/products/
├── newsletter-archive/ ← LIVE — MailerLite-sourced archive, linked under main nav "About" dropdown as "Newsletter" (parent = 'about' in hugo.toml)
├── digital-content-hub/ ← LIVE — homepage-linked hub with per-series and per-episode pages (layouts/_default/digital-content-hub.html, dch-episode.html), linked in main nav as "Repository". Former standalone Content Repository page was retired and merged into this hub (commit 9bc56fd9). KNOWN BUG: series _index.md files set `layout: "dch-series"` but no such layout file exists — Hugo silently falls back rather than erroring; needs a proper dch-series layout
├── speaking.md         ← LIVE (draft: false) — linked under main nav "About" dropdown as "Speaking"
├── about.md           ← LIVE (draft: false)
├── search.md          ← LIVE (draft: false)
├── testimonials.md    ← LIVE (draft: false)
├── contact.md         ← draft: true
├── blog/              ← draft: true
├── courses/           ← still in exploration, not linked in nav — do not publish without explicit go-ahead. KNOWN BUG: layouts/courses/personal-branding.html still fires the deprecated `Purchase_intent_Personal_branding_Jun_23` event instead of the standardised `purchase_intent` format — fix before this ever publishes
└── old-portfolio-files/ ← superseded duplicates of case-studies/portfolio content, excluded from build via `build: {render: never, list: never}` — safe to ignore, candidate for deletion

layouts/               ← Hugo templates
static/                ← assets (images, CSS, JS, PDFs)
data/                  ← structured data sources (digital_content_hub.json, podcast_episodes.json, testimonials.yaml)
.github/workflows/     ← GitHub Actions deploy config
```

**Known issue:** `og_image` in `hugo.toml` points to `static/images/pranoti-og-default.png`, which doesn't exist — the live URL 404s. Needs a real default OG image added.

---

## Purchase intent tracking

Every buy button on this site must fire a `purchase_intent` GA4 event on click.

```html
onclick="gtag('event', 'purchase_intent', {'item_name': 'PRODUCT NAME', 'location': 'LOCATION'})"
```

**Location values:**
- `product_page` — buy buttons on `/products/` standalone layouts
- `sidebar_product` — buy buttons in ai-guides and perspectives sidebars

**Rules:**
- Add to every new product layout before pushing
- `item_name` must be a human-readable name matching what appears in GA4 reports
- GA4 property: `G-JLGZLS20VW`
- To make it a Key Event: GA4 Admin → Events → `purchase_intent` → toggle "Mark as key event"

**Do not use old-format events** like `Purchase_intent_Personal_branding_Jun_23` — always use the standardised `purchase_intent` event name with `item_name` and `location` params.

**UTM convention for cross-site CTAs:** links from thesciencetalk.com blog posts to Pranoti product pages carry UTM params, e.g. `?utm_source=thesciencetalk&utm_medium=blog&utm_campaign=<name>&utm_content=<postID>_body_cta`. Follow this pattern for any new cross-site CTA.

---

## Known Hugo gotchas

### Don't use `.IsMenuCurrent` for nav active-states

This site's main nav (`[menu.main]` in `hugo.toml`) is defined entirely in config, not linked to content pages via front matter `menu:` blocks. Hugo's built-in `.IsMenuCurrent "main" .` helper needs a page reference behind the menu entry to compare against — since there isn't one here, it silently always returns `false`, no matter what page you're on. It won't error, it just never matches.

**Use instead:** a plain URL-prefix check in `layouts/partials/header.html`:
```go-html-template
{{ $path := .RelPermalink }}
{{ range .Site.Menus.main }}
  {{ $isActive := and (ne .URL "/") (hasPrefix $path .URL) }}
  ...
{{ end }}
```
This is what powers the nav active-state highlighting (bold + underline + section accent color) added in commit `37b0c65`.

### Uncommitted files break the GitHub Pages build silently

Hugo builds locally using whatever is on disk, including files that were never `git add`ed. GitHub Actions builds from a fresh checkout of the repo, so it only sees committed files. If a new template (e.g. a partial referenced by another layout) is left uncommitted, the site builds fine for you locally but the Actions build fails — with no local warning beforehand. Always double check `git status` for new `layouts/` files before pushing.

### A missing `layout:` value doesn't error, it silently reuses the wrong template

If front matter sets `layout: "some-name"` and no template file with that name exists, Hugo does not error and does not fall back to a generic default. It falls back based on the page's content section, silently reusing whatever template that section normally uses — even if it's the wrong one for this page. The page renders, just wrong, with no error to flag it. (This is what happened with the `dch-series` layout gap noted in the Site structure section above.)

### Dev-only notes and filters can ship to production by accident

Temporary markers left in code while building a feature — a comment like "not linked yet, still draft" or a filter that limits output to one test item — are easy to forget about and can get committed and pushed as-is. Before pushing, check for any placeholder comments or narrowing filters that were only meant for local testing.

### Never pipe a string through `jsonify` inside a `<script>` block — it double-quotes it

Hugo (Go `html/template`) already context-escapes any `{{ }}` output placed inside a `<script>` tag: a string value is emitted as a quoted JS string literal automatically. Adding `| jsonify` on top quotes it a second time. `{{ $gaId | jsonify }}` shipped to production as `var GA_ID = "\"G-JLGZLS20VW\""`, so gtag.js was loaded with a measurement ID that had literal quote characters inside it. Google served a generic stub with no property config and silently discarded every hit. GA4 reported near-zero traffic from 2026-08-06 (commit `611034d3`, which moved GA loading into `layouts/partials/consent-banner.html`) until 2026-09-07 (commit `34a1b2d4`), while Search Console showed traffic unchanged. The 2026-08-27 consent rework (`9548c130`) did not touch the line and did not fix it.

**Rule:** inside `<script>`, write `{{ $value }}` with no filter and let Hugo quote it. Use `jsonify` only for objects/arrays, or outside script context.

**Verify after any change to the analytics partial:** build locally and check the output contains `GA_ID = "G-JLGZLS20VW"` with no inner escaped quotes:
```bash
hugo --quiet -d /tmp/pub && grep -o 'GA_ID = [^;]*;' /tmp/pub/index.html
```
Then, once live, open GA4 Realtime and confirm your own visit appears. Search Console clicks are the independent check: if GSC shows traffic and GA4 shows none, the tag is broken, not the audience.

---

## DNS

- Provider: Cloudflare
- Record: `pranoti` CNAME → `scitalk.github.io`
- HTTPS enforced via GitHub Pages SSL cert
- Anti-spoofing: `pranoti` has a null SPF record (`v=spf1 -all`) and null MX (`0 .`), rejecting any mail claiming to be from this subdomain
- Proxied through Cloudflare (confirmed via A record resolving to Cloudflare IP ranges, not GitHub Pages IPs directly)

---

## Deploy workflow caveat

A successful `git push` only means the push succeeded — it does not mean the site is live. The GitHub Actions build can fail after the push (e.g. due to the uncommitted-file issue above), leaving `gh-pages` stale while `main` looks fully pushed. Check the Actions tab after a push if the change matters immediately.
