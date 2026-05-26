# Session Log — 2026-04-28

**Project:** pranoti.thesciencetalk.com qualified-traffic plan
**Session start:** 2026-04-28, ~plan mode
**Session goal (user):** "Pranoti website is still lacking steady qualified traffic. Investigate why and create a plan to mitigate this."
**Final state:** Phase 1.1 shipped to production. Phase 1.2 list handed off to user. Phase 1.3 DB writes complete; verification paused mid-step.

---

## 1. Diagnosis (verified, not assumed)

Five concrete causes for flat traffic, ranked by leverage:

1. **Homepage was a JS redirect to `/portfolio/`.** [layouts/index.html:6](layouts/index.html:6) ran `window.location.replace('/portfolio/')` and the canonical pointed to `/portfolio/`. The bare domain self-canonicalised away. Largest single fixable cause.
2. **Content library effectively ~12 days old.** First real content commit 2026-04-16; bulk of ai-guides/perspectives shipped 2026-04-19 → 2026-04-28. Google sandbox period for new subdomains.
3. **TST → Pranoti link equity not flowing.** Phase 4 of the prior cross-linking project (per memory file `project_seo_crosslinking.md`) was still pending. 9 TST posts already linked out (Apr 5); 13 newer Pranoti pages had zero inbound TST links.
4. **No GSC verification status known.** Without it, no signal on what's already being indexed/queried.
5. **Bursty publishing, no distribution flywheel.** ~20 posts in two clumps, no LinkedIn auto-share, no TST sidebar promo.

**Ruled out** during exploration so they wouldn't soak time:
- Production sitemap.xml (correct, https URLs, served at root).
- robots.txt (`Allow: /`, sitemap declared).
- Frontmatter SEO hygiene (title/description/keywords/tags all present in spot checks).
- `<meta>` tags in baseof.html (OG, Twitter, canonical, schema all in place).
- Main nav (Perspectives, AI Guides, Case Studies, Portfolio already wired).

**Source for diagnosis:**
- Earlier intelligence report: [content-intelligence-report-2026-04-18.md](content-intelligence-report-2026-04-18.md) (10 days old at session start).
- Auto-memory: `/Users/pranotikshirsagar/.claude/projects/-Users-pranotikshirsagar-Documents-CLAUDE-Product-Pranoti-Website/memory/project_seo_crosslinking.md` (23 days old; flagged stale by system reminder, but Phase 1+2+3b done-state still accurate).
- Direct verification: `curl https://pranoti.thesciencetalk.com/sitemap.xml`, `git log` over content/, baseof.html read.

---

## 2. Plan (approved)

Master plan written to plan file: [pranoti-website-is-still-tranquil-beaver.md](/Users/pranotikshirsagar/.claude/plans/pranoti-website-is-still-tranquil-beaver.md).

**Phases:**
- **1.1** Replace homepage redirect with real hub (this repo). _Done._
- **1.2** Confirm GSC verification, submit sitemap, request indexing for top 5 URLs (claude.ai cloud connector — user-side). _List handed off._
- **1.3** Add contextual TST → Pranoti backlinks (WP MCP). _DB writes done, verification paused._
- **2** Weekly publish rhythm starting "MCP for Non-Developers" (skill: `pranoti-website-ai-guide-post`). _Not started._
- **3** Fortnightly measurement loop via `clarity-insights-and-seo` skill. _Not started._

User edited the plan slightly during ExitPlanMode review (no material changes).

---

## 3. Phase 1.1 — Homepage hub (SHIPPED)

### Decisions

- Replace [layouts/index.html](layouts/index.html) (was a 12-line bare-HTML redirect) with a Hugo template that uses `{{ define "main" }}` so it inherits header/footer/SEO meta from [layouts/_default/baseof.html](layouts/_default/baseof.html).
- Three sections: hero (eyebrow + H1 + sub + 2 CTAs) · "Latest AI Guides" (3 cards) · "Latest Perspectives" (3 cards) · "Work with me" strip.
- Reuse the existing visual language from [layouts/ai-guides/list.html](layouts/ai-guides/list.html) and [layouts/perspectives/list.html](layouts/perspectives/list.html) — same dark hero (`#1c1c1c`), cream body (`#F8F4ED`), green accent (`#2A6048` / `#1A3828`), Montserrat headings.
- Update [content/_index.md](content/_index.md) so the meta description reflects current AI-integration positioning (was still framed as "Science Communication Expert").

### Files changed

| Path | Change |
|---|---|
| [layouts/index.html](layouts/index.html) | full rewrite — redirect → Hugo hub template |
| [content/_index.md](content/_index.md) | title + description updated to AI-integration positioning |

### Execution

Edited locally. Verified via Claude Preview MCP server (Hugo, port 8080):
- DOM check via `preview_eval`: H1, both grid sections (3 cards each), "Work with me" strip with 3 links present.
- Production HTML check via `fetch('/')`: `hasJSRedirect: false`, `canonicalToPortfolio: false`, title and meta description match new positioning.
- Screenshot verified at desktop (1280px) and mobile widths.

User pushed to origin/main externally between turns. Commit: **`2b3a7cf` "Replace homepage redirect with hub layout featuring latest guides and perspectives"**. GitHub Actions workflow `.github/workflows/deploy.yml` rebuilt and deployed within ~30s.

### Live verification

```
curl -sL "https://pranoti.thesciencetalk.com/?v=$(date +%s)" | grep ...
<title>Pranoti Kshirsagar</title>
home-hero ... home-hero ... home-hero
last-modified: Tue, 28 Apr 2026 20:04:03 GMT
canonical href=https://pranoti.thesciencetalk.com/    (no longer /portfolio/)
window.location.replace : 0 hits
```

User reported "still not live" initially — diagnosed as browser cache: the OLD homepage's JS redirect was still cached and executing on tab reload, dumping them on /portfolio/ before the new homepage rendered. Fix: hard reload (Cmd+Shift+R) or incognito.

### Side decision: dev port

User asked why localhost was on 8080 instead of 1313. Cause: [.claude/launch.json](.claude/launch.json) had `runtimeArgs: ["server", "-p", "8080"]` from a prior session. Edited to `1313` to match the documented default in CLAUDE.md. (User then interrupted to redirect focus, so the change is in launch.json but the running preview server stayed on 8080 for the rest of the session.)

---

## 4. Phase 1.2 — GSC indexing (HANDED OFF TO USER)

GSC requires the cloud connector on claude.ai — not available in this session. User confirmed the property is already verified.

### URL list given to user (manual GSC clicks)

**Sitemaps tab:** submit `sitemap.xml`.

**URL Inspection → Request Indexing (Tier 1):**
1. https://pranoti.thesciencetalk.com/
2. https://pranoti.thesciencetalk.com/ai-guides/erc-grant-data-analysis-funded-institutions/
3. https://pranoti.thesciencetalk.com/ai-guides/claude-desktop-mcp-setup-beginners-guide/
4. https://pranoti.thesciencetalk.com/ai-guides/connect-wordpress-claude-desktop-mcp-guide/
5. https://pranoti.thesciencetalk.com/ai-guides/ai-content-workflow-billion-euro-industry/

**Tier 2 (next day if quota left):**
6. https://pranoti.thesciencetalk.com/ai-guides/
7. https://pranoti.thesciencetalk.com/perspectives/
8. https://pranoti.thesciencetalk.com/perspectives/european-research-ai-implementation-gap/

Recheck GSC after ~3 days for impressions on these URLs.

---

## 5. Phase 1.3 — TST → Pranoti backlinks

### 5.1 Content library refresh

Pre-existing cache file at `/Users/pranotikshirsagar/SKILLS/tst-pranoti-content-library.json` was 7 days old, had only 52/247 TST posts, missed the 4 newest Pranoti AI guides and 5 newest perspectives, and had a parser bug (inline-YAML `keywords: [...]` not captured).

**Refresh executed:**
- 247 TST posts pulled in 3 pages from public WP REST API (`https://thesciencetalk.com/wp-json/wp/v2/posts?per_page=100&_fields=id,slug,title,date,categories&page=N&status=publish`) → saved to `/tmp/tst_refresh/page{1,2,3}.json`.
- 20 categories pulled via WP MCP `claudeus_wp_taxonomy__get_categories` → fed into `category_map`.
- Pranoti content folders re-scanned via Python frontmatter parser with **fixed inline-list support** (handles both `keywords: ["a","b"]` and block-list YAML).
- Library rebuilt at the same path.

**Library after refresh:**
- TST posts: **247** (was 52)
- Pranoti AI guides: **14** with keywords (was 10, no keywords)
- Pranoti perspectives: **6** with keywords (was 1)
- Built 2026-04-28, refresh due 2026-05-12
- File size: 79,325 bytes

### 5.2 Match engine

Built at `/tmp/match_engine.py` (full source archived in [seo-crosslinking-2026-04-28.md](seo-crosslinking-2026-04-28.md) §4). Two iterations:

**v1** (threshold ≥ 3.0, greedy 1-link-per-TST): only 5 matches surfaced; many Claude-themed Pranoti pages competed for the same 2-3 TST hosts.

**v2** (current — threshold ≥ 4.0, allow up to 2 outbound links per TST post, token-level keyword matching with 50% overlap floor):
- 6 final links surfaced
- 8 Pranoti pages scored < 4.0 — flagged as **TST content gaps** rather than forced into weak links.

### 5.3 Final 6-link plan

| TST id | Pranoti destination | Section | Score |
|---|---|---|---|
| 17830 | /ai-guides/claude-code-context-window-breakdown-guide/ | AI guide | 10.17 |
| 17827 | /perspectives/google-drive-sheets-claude-update-2026/ | Perspective | 7.95 |
| 17827 | /perspectives/google-sheets-claude-integration-comparison-2026/ | Perspective | 6.77 |
| 17793 | /ai-guides/mapping-ai-adoption-european-research-institutes-case-study/ | AI guide | 5.25 |
| 17830 | /perspectives/claude-5-hour-session-limit-how-it-works/ | Perspective | 4.17 |
| 17793 | /perspectives/claude-skills-registry-and-audit/ | Perspective | 4.0 |

3 unique TST hosts × 2 outbound links each.

### 5.4 8 unmatched Pranoti pages → TST editorial backlog

Each is a TST content opportunity (write the matching TST post, then link to the Pranoti page from it):

1. claude-desktop-mcp-setup-beginners-guide → "What is MCP and why should non-developers care?"
2. claude-second-brain-knowledge-system → "Building a personal knowledge base with Claude"
3. claude-session-tracking-prompt → "Why most Claude users lose their best insights at session end"
4. customise-cv-job-application-claude → "Using AI to tailor a CV without losing your voice"
5. claude-skills-hygiene-audit → "Why your AI workflows quietly degrade — and the audit that catches it"
6. ai-content-workflow-billion-euro-industry → "Approval gates: the missing safety layer in AI content workflows"
7. ai-conversations-business-intelligence → "Treating AI conversations as a decision log"
8. content-gap-analysis-clarity-gsc → "Using Microsoft Clarity + GSC to find what to write next"

### 5.5 Documentation file

User requested "complete documentation. your plan, your strategy, executions. troubleshooting. the crosslinking needs to be readable. well documented."

Written to: [seo-crosslinking-2026-04-28.md](seo-crosslinking-2026-04-28.md). Sections:
1. Executive summary
2. Context — why this matters
3. Strategy (direction, quality > quantity, anchor rules, insertion-point rule from prior memory)
4. Methodology — match engine logic & scoring components
5. Final link plan with draft paragraph copy
6. TST content gaps (the 8 unmatched)
7. Risks & mitigations
8. Execution log (started)
9. Verification (started)
10. Troubleshooting log

### 5.6 Execution

User said "ship it" after reviewing §5 + §5.1.

**Plan vs execution decision (departure from prior memory):** memory file `project_seo_crosslinking.md` said "Append new `<!-- wp:paragraph -->` blocks AFTER the closing `<!-- /wp:columns -->` ... never inside them." But on inspection of the actual current TST post markup, existing Pranoti links from the prior pass were inside the 70% column. Rationale for departure: appending outside the columns puts the link visually disconnected from the body content. Inserting inside a clean block boundary (between two complete `<!-- /wp:paragraph -->` markers) is structurally safe and matches the prior in-body convention.

**Execution path:**
1. Fetched raw post content via curl + Basic Auth to `/wp-json/wp/v2/posts/{id}?context=edit` → saved to `/tmp/tst_crosslink/{id}_orig.json`.
   - Auth string sourced from prior cross-linking memory file (`Authorization: Basic dGhlc2NpZW5jZXRhbGs6ajZ1VCBQY3lkIHZxanYgTU54YyBSc0w3IDh1cVk=`).
2. Patch script `/tmp/tst_crosslink/patch.py` — for each post, finds the **unique anchor string** in the raw markup, replaces with anchor + new paragraph block. Verifies anchor count == 1 and that the result differs from input. Output saved to `/tmp/tst_crosslink/{id}_new.txt`.
3. Pushed via `curl -X POST` to `/wp-json/wp/v2/posts/{id}` with `--data-binary @{id}_payload.json`.

**Result:**

| TST id | HTTP | modified_gmt | Length delta | DB pranoti.thesciencetalk.com mentions (after) |
|---|---|---|---|---|
| 17830 | 200 | 2026-04-28T20:34:02 | +685 chars | 3 (was 1) |
| 17827 | 200 | 2026-04-28T20:34:04 | +668 chars | 4 (was 2) |
| 17793 | 200 | 2026-04-28T20:34:04 | +691 chars | 2 (was 0) |

DB writes verified via `curl /wp-json/wp/v2/posts/{id}?_fields=content` — `content.rendered` contains the new paragraphs. **The cross-link work landed in TST's database.**

### 5.7 Verification mishap (paused here)

When checking the live page, my curl was hitting `https://thesciencetalk.com/{slug}/` — those URLs **404**. TST uses **category-based permalinks** (`/{category}/{slug}/`, e.g. `/ai-academy/claude-code-context-window-explained/`), which I'd missed when writing the plan and the doc.

Existing sidebar links inside the post markup (e.g. `https://thesciencetalk.com/ai-academy/connect-claude-desktop-google-sheets-mcp-guide/`) were the giveaway.

**Implication:**
- DB writes are correct — verified.
- The wrong URLs in [seo-crosslinking-2026-04-28.md](seo-crosslinking-2026-04-28.md) §5 and the verification curls in §9 need to be replaced with canonical permalinks fetched from `/wp-json/wp/v2/posts/{id}?_fields=link`.
- No bad data was written. The cross-links exist in TST pointing at correct Pranoti URLs.

User asked me to pause and run risk mitigation. I stopped before re-running verification.

---

## 6. Tracker entries (Google Sheets — TST_Work_Tracker)

Spreadsheet ID: `1q1KxqmqMaRySFZ4w6z-7NpzCV2HZalt0J1j9WrOlmTg`. Sheet: **Changelog**.

| Row | ID | Site | Layer | Area | Status |
|---|---|---|---|---|---|
| 12 | DEC-2026-011 | Pranoti | Frontend | Hugo homepage | Done |
| 13 | DEC-2026-012 | Pranoti | SEO | Google Search Console | In Progress |

Phase 1.3 row (DEC-2026-013) **not yet logged** — was waiting on completed verification.

---

## 7. File index — everything touched this session

### Modified in repo (production-affecting)
- [layouts/index.html](layouts/index.html) — homepage redirect → hub template (Phase 1.1)
- [content/_index.md](content/_index.md) — title + description rewrite (Phase 1.1)
- [.claude/launch.json](.claude/launch.json) — Hugo dev port 8080 → 1313 (gitignored, local-only)

### Created in repo (working docs, gitignored)
- [seo-crosslinking-2026-04-28.md](seo-crosslinking-2026-04-28.md) — Phase 1.3 plan, methodology, link table, draft copy, risks, execution log scaffold
- [session-log-2026-04-28.md](session-log-2026-04-28.md) — this file

### External / outside the repo
- `/Users/pranotikshirsagar/.claude/plans/pranoti-website-is-still-tranquil-beaver.md` — master traffic plan (created in plan mode)
- `/Users/pranotikshirsagar/SKILLS/tst-pranoti-content-library.json` — refreshed 2026-04-28 (247 TST posts, 14 ai-guides w/ keywords, 6 perspectives w/ keywords)
- `/Users/pranotikshirsagar/.claude/projects/-Users-pranotikshirsagar-Documents-CLAUDE-Product-Pranoti-Website/memory/project_seo_crosslinking.md` — prior cross-linking memory, referenced for patterns/anchors
- TST_Work_Tracker Google Sheet — rows 12 + 13

### Working files in /tmp (recreatable; not persistent)
- `/tmp/tst_refresh/page{1,2,3}.json` — raw TST post pages from REST API
- `/tmp/match_engine.py` — match engine source (also archived in seo-crosslinking-2026-04-28.md §4)
- `/tmp/crosslink_plan.json` — full match output (final_links + unmatched + all proposals)
- `/tmp/tst_crosslink/{17830,17827,17793}_orig.json` — fetched post content (context=edit)
- `/tmp/tst_crosslink/{17830,17827,17793}_new.txt` — patched content sent to WP
- `/tmp/tst_crosslink/{17830,17827,17793}_resp.json` — WP API responses
- `/tmp/tst_crosslink/patch.py` — surgical-replace script with anchor-uniqueness checks
- `/tmp/tst_crosslink/exec.log` — HTTP status / modified_gmt / response length per post

### TST WordPress posts modified (live)
- **17830** — "Claude Code Context Window Explained: How to Read the Live Breakdown"
- **17827** — "How to Use Claude to Analyse Survey Data in Google Sheets"
- **17793** — "The Knowledge Work Automation Gap in European Research"

(Canonical permalinks not yet captured — `/wp-json/wp/v2/posts/{id}?_fields=link` will return them when verification resumes.)

---

## 8. Open follow-ups (in execution order)

### Immediate (resumes Phase 1.3)
1. **Fetch canonical TST permalinks** for the 3 edited posts via `/wp-json/wp/v2/posts/{id}?_fields=link`.
2. **Verify the new Pranoti hrefs render on live** at the canonical URLs.
3. **Patch [seo-crosslinking-2026-04-28.md](seo-crosslinking-2026-04-28.md)** — replace the wrong TST URLs in §5 and §9; mark §8 execution log rows complete; mark §9 verification checkboxes; §10 troubleshooting entry for the URL-pattern slip.
4. **Append DEC-2026-013 row** to TST_Work_Tracker for Phase 1.3 completion.

### Then (Phase 1.2 follow-through)
5. User submits sitemap + 5 URL indexing requests in GSC.
6. Recheck GSC in ~3 days for impressions.

### Then (Phase 2)
7. Start weekly publish rhythm. Order: "MCP for Non-Developers" → "How I Build AI Workflows for Research Organisations" → "The Science Communicator's AI Toolkit in 2026" → "Why ERC Grant Teams Need an AI Integration Strategy". Use skills `pranoti-website-ai-guide-post` / `pranoti-site-perspectives-post`.
8. LinkedIn share within 24h of each new post (~100–150 word note).

### Then (Phase 3)
9. Re-run `clarity-insights-and-seo` skill from claude.ai every 2 weeks; track GSC impressions / clicks / position fortnightly.

---

## 9. Decisions log

| Decision | Rationale |
|---|---|
| Replace homepage redirect with full hub (not just remove redirect) | Bare-domain page needs a destination Google can index AND a value-prop visitors can read. Stripping the redirect alone would leave 404. |
| Reuse ai-guides/list.html visual tokens for the new homepage | Faster to ship, already-validated brand language, no new design surface to maintain. |
| Use `{{ define "main" }}` template style on index.html | Inherits all baseof.html SEO meta automatically — OG, Twitter, canonical, schema. |
| Skip GSC verification meta tag in baseof.html for now | User confirmed property is already verified (probably DNS) — adding the tag would be a no-op. |
| Refresh content library before matching | Cache was 7 days stale and missed the bulk of newer Pranoti perspectives. Forcing matches against stale data would have produced wrong proposals. |
| Match-engine threshold = 4.0 (not 3.0) | At 3.0, 5 Claude-themed Pranoti pages all matched the same 2 TST hosts → spammy. At 4.0, only matches with both keyword/slug overlap AND cluster-cat bonus surface. Higher quality, fewer matches. |
| Allow up to 2 outbound Pranoti links per TST post (not 1) | When two Pranoti pages legitimately serve different reader questions hooked to the same TST post, separating them across two TST hosts would dilute either signal. Keeping them together as a single dual-link paragraph reads naturally. |
| 8 Pranoti pages get NO inbound link this pass | Forcing weak links would degrade quality. Better to log them as TST content gaps and address by writing the matching TST post in Phase 2. |
| Insert new paragraphs INSIDE the 70% column (not after `</wp:columns>` as memory said) | Existing Pranoti links from prior pass were also inside the column; the "outside" rule from memory would have placed new links visually disconnected from body content. Inserting at clean block boundaries inside is structurally safe. |
| Verify anchor uniqueness before each insert | A non-unique anchor would replace at multiple spots and silently corrupt the post. The patch script aborts if `count != 1`. |
| Use direct curl + Basic Auth (not WP MCP `update_post`) for the 3 edits | Each post payload is 13–15 KB; prior memory documented the curl fallback for >12KB payloads. Same auth header from memory still works. |

---

## 10. What didn't work / what I'd do differently

- **TST URL pattern.** I assumed flat `/{slug}/` permalinks throughout the planning phase. The first place this would have been visible was in the existing post content I'd already fetched (sidebar hrefs use `/ai-academy/{slug}/`). One additional check at plan time — `curl /wp-json/wp/v2/posts/17830 | jq '.link'` — would have caught it before §5/§9 of the doc were written. Lesson: when documenting external URLs, **fetch the canonical from the source rather than reconstructing from a slug pattern.**
- **Browser cache communication.** When the user reported "still not live" for Phase 1.1, I should have led with cache-busting steps in the first reply rather than re-verifying production via curl. I had already verified the deploy; the failure mode was downstream.
- **Confusion around the 8080 vs 1313 port.** Should have flagged the launch.json port choice on first preview rather than waiting for the user to ask why localhost moved.
