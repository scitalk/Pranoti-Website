# Pranoti Website — Claude Instructions

## Site overview

- **URL:** https://pranoti.thesciencetalk.com
- **Stack:** Hugo static site (v0.139.0)
- **Site root:** `/Users/pranotikshirsagar/Documents/CLAUDE/Product/Pranoti_Website/`
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
- All changes go in: `static/`, `content/`, `layouts/`, `hugo.toml`
- Hugo version: 0.139.0 (set in `.github/workflows/deploy.yml`)

---

## Site structure

```
content/
├── portfolio/         ← LIVE (video, shorts, podcast, trainings, proposal, scicommai, events, reports)
├── case-studies/      ← LIVE
├── ai-guides/         ← LIVE
├── perspectives/      ← LIVE
├── about.md           ← LIVE (draft: false)
├── search.md          ← LIVE (draft: false)
├── testimonials.md    ← LIVE (draft: false)
├── contact.md         ← draft: true
├── blog/              ← draft: true
├── courses/           ← still in exploration, not linked in nav — do not publish without explicit go-ahead
└── old-portfolio-files/ ← superseded duplicates of case-studies/portfolio content, excluded from build via `build: {render: never, list: never}` — safe to ignore, candidate for deletion

layouts/               ← Hugo templates
static/                ← assets (images, CSS, JS, PDFs)
.github/workflows/     ← GitHub Actions deploy config
```

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

---

## DNS

- Provider: Cloudflare
- Record: `pranoti` CNAME → `scitalk.github.io`
- HTTPS enforced via GitHub Pages SSL cert
