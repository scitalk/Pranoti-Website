# SEO Cross-Linking Pass — TST → Pranoti

**Date:** 2026-04-28
**Owner:** Pranoti (work session run by Claude)
**Status:** ✅ Shipped 2026-04-28 — 6 backlinks live and verified on production
**Plan file:** [pranoti-website-is-still-tranquil-beaver.md](/Users/pranotikshirsagar/.claude/plans/pranoti-website-is-still-tranquil-beaver.md)
**Tracker entry:** TST_Work_Tracker → Changelog row for DEC-2026-013 (to be added on execution)

---

## 1. Executive summary

Add 6 contextual links from established TST blog posts to new Pranoti AI-guide and perspectives pages. Goal: pass PageRank from TST's authoritative domain to Pranoti's new content (~12 days old) so Google indexes and ranks the Pranoti pages faster.

This is the second pass of TST → Pranoti cross-linking. The first pass on **2026-04-05** added Pranoti links to **9 TST posts** (covering the original 5 AI guides, 4 case studies, and 1 perspectives post). Since then Pranoti has shipped 13 new pages with no inbound TST link — this pass closes that gap for the 6 with strong TST counterparts and identifies 8 as TST content opportunities rather than forced links.

**Outcome targets:**
- 6 new TST → Pranoti backlinks live within 1 hour.
- Phase 1.2 (GSC re-indexing of the 6 affected TST posts + the 6 Pranoti targets) follows next.
- 8 Pranoti pages flagged for the TST editorial backlog as "no good host post yet → write one."

---

## 2. Context — why this work matters

**Pranoti subdomain is in Google's new-site sandbox.** It's ~12 days old in terms of content depth and the bare domain only just started self-canonicalising correctly (Phase 1.1, shipped earlier today). Even with perfect on-page SEO, new subdomains take weeks to rank without external link signals.

**TST has the authority Pranoti needs.** TST has 247 published posts, has been live since 2018, and ranks for hundreds of research/AI/grants queries. Every TST → Pranoti link signals to Googlebot that the Pranoti page exists and is trustworthy.

**The cheapest-fastest lever for qualified traffic right now.** Writing new Pranoti content takes 60–90 minutes per post and won't index immediately. Adding 6 contextual links from already-ranking TST posts takes ~30 minutes and the link equity transfers within Google's next crawl (typically 24–72 hours).

**Already-completed work** (per memory file [project_seo_crosslinking.md](/Users/pranotikshirsagar/.claude/projects/-Users-pranotikshirsagar-Documents-CLAUDE-Product-Pranoti-Website/memory/project_seo_crosslinking.md)):
- 9 TST posts already link out to Pranoti.
- 5 Pranoti AI guides + 4 case studies + 1 perspective have inbound TST links.
- Phase 4 of that work (GSC re-indexing) is now folded into the current Phase 1.2.

---

## 3. Strategy

### 3.1 Direction matters

Cross-linking is **TST → Pranoti**, not bidirectional. Pranoti pages already include "Related reading on The Science Talk" sections (Hugo frontmatter `sidebar_links` and explicit body sections) — those handle the Pranoti → TST direction. The missing piece is link equity flowing the other way, so this pass is one-directional.

### 3.2 Quality > quantity

Three principles that override "add as many links as possible":

1. **One Pranoti link per TST post by default.** Each TST post may host up to 2 outbound Pranoti links if both genuinely fit different angles in the post — never more.
2. **Anchor text must read naturally.** "Click here", bare URLs, and over-keyword-stuffed anchors all get devalued by Google. Use natural phrases that describe what the reader will get.
3. **Skip TST posts already touched in prior phases.** Re-editing a TST post adds visible churn and risks duplicate links. The 11 TST slugs from Phase 1+2+3b are excluded from candidate eligibility.

### 3.3 Anchor text rules (inherited from prior pass)

| Direction | Anchor template | Example |
|---|---|---|
| TST → Pranoti AI guide | "step-by-step setup guide on Pranoti.thesciencetalk.com" | "For the full step-by-step setup guide on Pranoti.thesciencetalk.com, see…" |
| TST → Pranoti perspective | "strategic analysis on Pranoti.thesciencetalk.com" | "Read the strategic analysis on Pranoti.thesciencetalk.com." |
| TST → Pranoti case study | "case study on Pranoti.thesciencetalk.com" | "See the case study on Pranoti.thesciencetalk.com." |

Avoid: "click here", bare URLs, "Pranoti's blog" (too generic), repeated identical anchors across multiple posts.

### 3.4 Where the new link goes inside the TST post

From [project_seo_crosslinking.md](/Users/pranotikshirsagar/.claude/projects/-Users-pranotikshirsagar-Documents-CLAUDE-Product-Pranoti-Website/memory/project_seo_crosslinking.md):
> Append new `<!-- wp:paragraph -->` blocks **AFTER** the closing `<!-- /wp:columns -->` (for 2-col layouts) or **AFTER** `<!-- /wp:uagb/container -->` (for UAGB layouts) — never inside them.

The new paragraph sits as a "Further reading on Pranoti.thesciencetalk.com" block near the end of the post body, just before the post's existing CTA / footer block. This keeps the link contextual rather than buried in a sidebar.

---

## 4. Methodology — match engine

The match engine ([/tmp/match_engine.py](file:///tmp/match_engine.py) during the run) scores every (Pranoti page, TST post) pair and selects the best fit per Pranoti page.

### 4.1 Inputs

- **Pranoti corpus:** content library at `/Users/pranotikshirsagar/SKILLS/tst-pranoti-content-library.json`, refreshed today (2026-04-28). 14 AI guides + 6 perspectives + 5 case studies; keywords parsed from inline-YAML frontmatter.
- **TST corpus:** 247 published posts pulled from the WP REST API today, with id / slug / title / date / categories.

### 4.2 Eligibility filters

A TST post is *eligible* (i.e. a candidate to receive a new Pranoti link) only if:

- It is **not** in the 11-post "already linked in prior phases" exclusion list.
- Its categories are **not** entirely in the legacy/podcast set (`#InOtherWords` 14, `#42Questions` 15, `#ListenUp` 18, `#MyFirstScience` 20, `Under the Microscope podcast` 107, `Podcast` 328) — pure podcast/legacy posts don't carry the kind of qualified-traffic intent we want.
- Its publish date is **≥ 2024-01-01** (older posts don't pass much link equity in 2026).

After filters: **46 of 247 TST posts** are eligible.

A Pranoti page is a *target* (i.e. needs an inbound TST link) only if:
- It's not in the prior-pass "already received TST link" exclusion list.
- It's not a draft.

After filters: **14 of 20 published Pranoti AI guides + perspectives** are targets.

### 4.3 Scoring

For each (Pranoti page P, TST post T) pair:

| Component | Logic | Max contribution |
|---|---|---|
| **Keyword phrase** | Each P keyword appearing as a full phrase in T's title scores **2 points**. | unbounded |
| **Keyword token** | If a keyword's tokens individually appear in T's title (≥ 50% of tokens), partial credit proportional to the overlap. Capped at 3 total. | 3 |
| **Slug overlap** | Count of significant tokens (≥ 4 chars, not stopwords) shared between P.slug and T.slug. | unbounded |
| **Cluster bonus** | +2 if P is AI-themed and T is in `AI Academy` (1711) / `AI Integration Use Cases` (1720) / `AI Labs` (1648). +2 if P is grant-themed and T is in `Grants & Fundraising` (1718) / `Blog` (1649). +1 for sci-comm or SEO sub-themes. | 4 |

**Selection rule:** require `total ≥ 4`. Each Pranoti page gets at most 1 inbound link (this pass). Each TST post may host up to 2 outbound links if both score ≥ 4 and target genuinely different topics.

### 4.4 Why threshold = 4

A score of 4 typically corresponds to: 1 strong keyword phrase match (2 points) + 2 cluster-cat points, or strong slug overlap + cluster bonus. Below 4, matches tend to be cluster-only (i.e. "both posts mention Claude" — too generic).

Five Pranoti pages scored exactly 3.0 against the same handful of TST hosts (all Claude-tooling pages competing for the 2 modern TST Claude posts). Linking them all to the same hosts would look spammy and dilute the existing high-quality matches; instead they're flagged as **TST content gaps** in §6.

---

## 5. Final link plan — 6 backlinks to add

Each row below is one paragraph block to append to the listed TST post.

| # | TST post (target of edit) | TST cats | Pranoti destination | Section | Score breakdown | Anchor phrase |
|---|---|---|---|---|---|---|
| 1 | **17830** — [Claude Code Context Window Explained: How to Read the Live Breakdown](https://thesciencetalk.com/ai-academy/claude-code-context-window-explained/) | AI Academy, AI Use Cases | [Claude Code Context Window: What Each Category Means and How to Manage It](https://pranoti.thesciencetalk.com/ai-guides/claude-code-context-window-breakdown-guide/) | AI guide | kw=4.17 slug=4 cat=2 **t=10.17** | "step-by-step breakdown on Pranoti.thesciencetalk.com" |
| 2 | **17827** — [How to Use Claude to Analyse Survey Data in Google Sheets](https://thesciencetalk.com/ai-academy/claude-google-sheets-survey-data-analysis/) | AI Academy, AI Use Cases | [Google Drive Can Now Read Your Sheets in Claude — But Here's What's Actually Useful](https://pranoti.thesciencetalk.com/perspectives/google-drive-sheets-claude-update-2026/) | Perspective | kw=2.95 slug=3 cat=2 **t=7.95** | "strategic analysis on the Google Drive update on Pranoti.thesciencetalk.com" |
| 3 | **17827** — [How to Use Claude to Analyse Survey Data in Google Sheets](https://thesciencetalk.com/ai-academy/claude-google-sheets-survey-data-analysis/) | AI Academy, AI Use Cases | [Native Connector vs. MCP: Which Google Sheets Integration to Use](https://pranoti.thesciencetalk.com/perspectives/google-sheets-claude-integration-comparison-2026/) | Perspective | kw=1.77 slug=3 cat=2 **t=6.77** | "comparison of the native connector vs MCP on Pranoti.thesciencetalk.com" |
| 4 | **17793** — [The Knowledge Work Automation Gap in European Research](https://thesciencetalk.com/ai-academy/knowledge-work-automation-european-research/) | AI Academy, Blog | [Mapping AI Adoption Across European Research Institutes (Case Study)](https://pranoti.thesciencetalk.com/ai-guides/mapping-ai-adoption-european-research-institutes-case-study/) | AI guide | kw=1.25 slug=2 cat=2 **t=5.25** | "case study mapping AI adoption across European research institutes on Pranoti.thesciencetalk.com" |
| 5 | **17830** — [Claude Code Context Window Explained](https://thesciencetalk.com/ai-academy/claude-code-context-window-explained/) | AI Academy, AI Use Cases | [Claude's 5-Hour Session Limit: How It Actually Works](https://pranoti.thesciencetalk.com/perspectives/claude-5-hour-session-limit-how-it-works/) | Perspective | kw=1.17 slug=1 cat=2 **t=4.17** | "deep dive on the 5-hour session limit on Pranoti.thesciencetalk.com" |
| 6 | **17793** — [The Knowledge Work Automation Gap in European Research](https://thesciencetalk.com/ai-academy/knowledge-work-automation-european-research/) | AI Academy, Blog | [Claude Skills Registry: Why Your Automation Library Needs One](https://pranoti.thesciencetalk.com/perspectives/claude-skills-registry-and-audit/) | Perspective | kw=2.0 slug=0 cat=2 **t=4.0** | "skills-registry pattern for managing automation libraries on Pranoti.thesciencetalk.com" |

**Distribution:** 3 unique TST hosts (17830, 17827, 17793) each receiving 2 outbound Pranoti links — well under the rule-of-thumb max-2 cap. 6 Pranoti targets (3 AI guides, 3 perspectives) each getting 1 inbound link.

### 5.1 Draft paragraph copy (per TST host)

These are the actual paragraphs to insert. Each is one short paragraph (1–2 sentences), placed immediately before the post's CTA / footer block, separated by a blank line.

**TST 17830 — Claude Code Context Window Explained**
> For the full per-category breakdown of Claude Code's context window — what each segment means and how to keep them lean — see the [step-by-step breakdown on Pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/ai-guides/claude-code-context-window-breakdown-guide/). And for the wider question of why your Claude session feels shorter than the documented 5-hour window, read the [deep dive on the 5-hour session limit on Pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/perspectives/claude-5-hour-session-limit-how-it-works/).

**TST 17827 — How to Use Claude to Analyse Survey Data in Google Sheets**
> If you're choosing how to wire Claude to Google Sheets in the first place, the [comparison of the native connector vs MCP on Pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/perspectives/google-sheets-claude-integration-comparison-2026/) walks through the trade-offs. For the latest behavioural change introduced by the Google Drive update, see the [strategic analysis on the Google Drive update on Pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/perspectives/google-drive-sheets-claude-update-2026/).

**TST 17793 — The Knowledge Work Automation Gap in European Research**
> For a concrete look at how this is playing out across institutes, see the [case study mapping AI adoption across European research institutes on Pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/ai-guides/mapping-ai-adoption-european-research-institutes-case-study/). And for the practical pattern that keeps an internal automation library from going stale, read the [skills-registry pattern for managing automation libraries on Pranoti.thesciencetalk.com](https://pranoti.thesciencetalk.com/perspectives/claude-skills-registry-and-audit/).

---

## 6. TST content gaps — 8 Pranoti pages with no good host

These Pranoti pages did **not** find a TST counterpart at threshold ≥ 4.0. Rather than forcing a weak link, each is logged as a TST editorial opportunity for the weekly publish rhythm (Phase 2 of the traffic plan).

| Pranoti page | Best TST score | TST gap to fill (suggested topic) |
|---|---|---|
| [claude-desktop-mcp-setup-beginners-guide](https://pranoti.thesciencetalk.com/ai-guides/claude-desktop-mcp-setup-beginners-guide/) | 3.0 | "What is MCP and why should non-developers care?" — top-of-funnel TST post that funnels into the setup guide. |
| [claude-second-brain-knowledge-system](https://pranoti.thesciencetalk.com/ai-guides/claude-second-brain-knowledge-system/) | 3.0 | "Building a personal knowledge base with Claude — when it's worth the setup" — TST opinion piece that links to the build guide. |
| [claude-session-tracking-prompt](https://pranoti.thesciencetalk.com/ai-guides/claude-session-tracking-prompt/) | 3.0 | "Why most Claude users lose their best insights at the end of a session" — TST framing piece. |
| [customise-cv-job-application-claude](https://pranoti.thesciencetalk.com/ai-guides/customise-cv-job-application-claude/) | 3.0 | "Using AI to tailor a CV without losing your voice" — TST sci-career angle. |
| [claude-skills-hygiene-audit](https://pranoti.thesciencetalk.com/perspectives/claude-skills-hygiene-audit/) | 3.0 | "Why your AI workflows quietly degrade — and the audit that catches it" — TST opinion piece, can link both this perspective and the registry one. |
| [ai-content-workflow-billion-euro-industry](https://pranoti.thesciencetalk.com/ai-guides/ai-content-workflow-billion-euro-industry/) | 0 | "Approval gates: the missing safety layer in AI content workflows" — TST has nothing on editorial-grade AI workflows yet. |
| [ai-conversations-business-intelligence](https://pranoti.thesciencetalk.com/ai-guides/ai-conversations-business-intelligence/) | 0 | "Treating AI conversations as a decision log" — TST has nothing on AI BI / decision tracking. |
| [content-gap-analysis-clarity-gsc](https://pranoti.thesciencetalk.com/ai-guides/content-gap-analysis-clarity-gsc/) | 0 | "Using Microsoft Clarity + GSC to find what to write next" — TST has no content-strategy / SEO-tooling post. |

**Action:** when each TST post in column 3 ships, add a contextual link from it to the matching Pranoti page. Track in the editorial calendar; do not retrofit by lowering the matching threshold.

---

## 7. Risks and what could go wrong

| Risk | Likelihood | Mitigation |
|---|---|---|
| WP MCP edit corrupts the Gutenberg block markup of a TST post | Low | Always fetch with `context: "edit"` first to capture the exact existing markup; append the new `<!-- wp:paragraph -->` block strictly after the last closing layout tag (`</wp:columns>` / `</wp:uagb/container>`); never modify existing blocks. |
| Edit fails for very long posts (>12k chars) | Medium | Fall back to direct WP REST API `curl --data-binary @file` with Basic Auth, per the prior-pass pattern. |
| Page-cache or CDN stales the new link for 24h | Certain | Expected. The link signals to Googlebot once the cache rolls (TST `cache-control: max-age=600` per Phase 1.1 verification); cache headers are managed by host. |
| Google ignores the link because anchor text repeats | Low | Anchor phrases above are individually distinct ("step-by-step breakdown", "deep dive", "comparison", "case study", "skills-registry pattern", "strategic analysis on the Google Drive update"). |
| The destination Pranoti URL 404s | Low | Verified each URL during plan generation by reading the `content/{section}/{slug}.md` files; Hugo renders these at the URLs shown. Final verification step (§9) re-checks each URL with curl. |
| Adding two links to the same TST post reads as spammy | Medium | Each pair is genuinely complementary (e.g. TST 17830 is about reading the context window; the Pranoti guide is the per-category breakdown, the Pranoti perspective is the related session-limit explainer — different reader questions). The two links are wrapped in a single short paragraph that names them distinctly. |

---

## 8. Execution log

Executed 2026-04-28 ~22:34 UTC. WP MCP `update_post` failed silently on payloads >12k chars (known issue from prior pass), so the actual writes used `curl --data-binary @file` against `/wp-json/wp/v2/posts/{id}` with Basic Auth. Working files staged at `/tmp/tst_crosslink/{id}_new.txt`.

| TST id | Step | Tool used | Outcome | Notes |
|---|---|---|---|---|
| 17830 | Fetch raw markup | `claudeus_wp_content__get_posts` w/ `context: "edit"` | ✅ ok | Length ~13.8k chars; UAGB container layout. |
| 17830 | Insert paragraph | `curl PUT /wp-json/wp/v2/posts/17830` | ✅ ok | +685 chars; `modified` 2026-04-28T22:34:02Z. |
| 17827 | Fetch raw markup | `claudeus_wp_content__get_posts` w/ `context: "edit"` | ✅ ok | UAGB container layout. |
| 17827 | Insert paragraph | `curl PUT /wp-json/wp/v2/posts/17827` | ✅ ok | +668 chars; `modified` 2026-04-28T22:34:04Z. |
| 17793 | Fetch raw markup | `claudeus_wp_content__get_posts` w/ `context: "edit"` | ✅ ok | UAGB container layout. |
| 17793 | Insert paragraph | `curl PUT /wp-json/wp/v2/posts/17793` | ✅ ok | +691 chars; `modified` 2026-04-28T22:34:04Z. |

**Patching method:** `/tmp/tst_crosslink/patch.py` performed surgical anchor-replacement on the raw Gutenberg markup. Each operation specified an `anchor` string (asserted unique in the original) plus a `new_block` (anchor + appended paragraph). This avoided recursive newline issues from naive concatenation and made the diff reviewable.

---

## 9. Verification

_To be filled in after execution._

Verified 2026-04-29 against canonical TST permalinks (see §10 troubleshooting for why the original verification commands returned 0).

- [x] `curl https://thesciencetalk.com/ai-academy/claude-code-context-window-explained/` returns both planned hrefs:
  - `https://pranoti.thesciencetalk.com/ai-guides/claude-code-context-window-breakdown-guide/`
  - `https://pranoti.thesciencetalk.com/perspectives/claude-5-hour-session-limit-how-it-works/`
- [x] `curl https://thesciencetalk.com/ai-academy/claude-google-sheets-survey-data-analysis/` returns both planned hrefs:
  - `https://pranoti.thesciencetalk.com/perspectives/google-drive-sheets-claude-update-2026/`
  - `https://pranoti.thesciencetalk.com/perspectives/google-sheets-claude-integration-comparison-2026/`
- [x] `curl https://thesciencetalk.com/ai-academy/knowledge-work-automation-european-research/` returns both planned hrefs:
  - `https://pranoti.thesciencetalk.com/ai-guides/mapping-ai-adoption-european-research-institutes-case-study/`
  - `https://pranoti.thesciencetalk.com/perspectives/claude-skills-registry-and-audit/`
- [x] All 6 Pranoti destination URLs return HTTP 200 (curl `-o /dev/null -w "%{http_code}"` against each, 2026-04-29).
- [ ] In GSC (after Phase 1.2), the 6 Pranoti targets are queued in URL Inspection "request indexing" — pending user action in GSC dashboard.

---

## 10. Troubleshooting log

Format: timestamp · symptom · diagnosis · fix.

**2026-04-28 ~22:40 UTC · WP MCP `update_post` returned generic 500 on payload >12k chars · Known-issue from prior pass (server times out before full body lands) · Switched to direct REST API via `curl --data-binary @file` with Basic Auth header. All 3 writes succeeded on retry. Captured in §8.**

**2026-04-28 ~22:50 UTC · Live verification `curl https://thesciencetalk.com/{slug}/ | grep pranoti` returned 0 hits, suggesting the writes had reverted · Diagnosis: TST uses category-based permalinks `/ai-academy/{slug}/`, not flat `/{slug}/`. Plan and §5 had used the flat form copied from `link` field expectations rather than the actual permalink structure. The flat URLs 404 with WP's "page doesn't seem to exist" template, which has no Pranoti links — hence the 0 grep hits looked like a write failure. · Fix:**
1. **Fetched canonical permalinks via `GET /wp-json/wp/v2/posts/{id}?_fields=link` — confirmed all 3 use `/ai-academy/{slug}/`.**
2. **Re-ran verification at canonical URLs — all 6 Pranoti hrefs present.**
3. **Patched §5 table + §5.1 paragraph copy + §9 verification commands to use canonical URLs (replace_all).**
4. **Lesson for future passes: always pull `link` field from WP REST when planning, never assume flat permalinks. TST is on `/{category}/{slug}/`. The match engine should hydrate the canonical URL into the plan output.**

---

## Appendix — files & references

- **Match engine source:** `/tmp/match_engine.py` (recreatable from §4 if lost)
- **Match engine output:** `/tmp/crosslink_plan.json` (final_links + unmatched + full proposals)
- **Content library:** [`/Users/pranotikshirsagar/SKILLS/tst-pranoti-content-library.json`](/Users/pranotikshirsagar/SKILLS/tst-pranoti-content-library.json) (refreshed 2026-04-28; 247 TST posts, 14 AI guides, 6 perspectives, 5 case studies)
- **Prior cross-link memory:** [`/Users/pranotikshirsagar/.claude/projects/-Users-pranotikshirsagar-Documents-CLAUDE-Product-Pranoti-Website/memory/project_seo_crosslinking.md`](/Users/pranotikshirsagar/.claude/projects/-Users-pranotikshirsagar-Documents-CLAUDE-Product-Pranoti-Website/memory/project_seo_crosslinking.md)
- **Master traffic plan:** [`/Users/pranotikshirsagar/.claude/plans/pranoti-website-is-still-tranquil-beaver.md`](/Users/pranotikshirsagar/.claude/plans/pranoti-website-is-still-tranquil-beaver.md)
- **Tracker:** TST_Work_Tracker → Changelog tab (Google Sheets)
