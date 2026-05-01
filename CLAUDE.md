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
├── about.md           ← draft: true (not published)
├── contact.md         ← draft: true
└── blog/              ← draft: true

layouts/               ← Hugo templates
static/                ← assets (images, CSS, JS, PDFs)
.github/workflows/     ← GitHub Actions deploy config
```

---

## DNS

- Provider: Cloudflare
- Record: `pranoti` CNAME → `scitalk.github.io`
- HTTPS enforced via GitHub Pages SSL cert
