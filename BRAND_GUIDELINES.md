# Brand Guidelines — pranoti.thesciencetalk.com

Reference for Claude when designing, writing, or building anything on this site. All values are derived from the live codebase.

---

## 1. Brand Identity

| | |
|---|---|
| **Site name** | Pranoti Kshirsagar |
| **Tagline** | AI Integration, Science Communication, and Research Strategy |
| **URL** | https://pranoti.thesciencetalk.com |
| **Author email** | pranoti@thesciencetalk.com |
| **LinkedIn** | https://www.linkedin.com/in/pranoti-kshirsagar/ |

**Tone:** Professional, expert, and warm — not corporate, not casual. Writes for researchers, academics, science communicators, and AI-curious professionals who value depth over hype.

---

## 2. Color Palette

### Core CSS variables (`assets/css/main.css`)

| Token | Hex | Usage |
|---|---|---|
| `--ink` | `#1c1c1c` | Primary text, dark backgrounds |
| `--ink-soft` | `#6f6f6f` | Secondary / muted text |
| `--paper` | `#faf7f2` | Main page background (warm cream) |
| `--white` | `#ffffff` | Cards, overlays |
| `--accent` | `#c76a5a` | Inline hyperlinks in body content |

### Brand greens — CTAs and structural elements

| Name | Hex | Usage |
|---|---|---|
| Forest deep | `#1A3828` | Primary CTA buttons, hero section |
| Forest mid | `#2A6048` | Secondary CTAs, hover states, case study header borders |
| Sage | `#7BBDA0` | Eyebrow text, accent highlights, architecture card text |

### Functional / status colors

| Name | Hex | Usage |
|---|---|---|
| Blocker red | `#D85A30` | Warnings, blockers in case studies |
| Blocker text | `#993C1D` | Text inside blocker callouts |
| Blocker bg | `#FAECE7` | Background of blocker callouts |
| Success bg | `#E6F4ED` | Metrics blocks, good-state backgrounds |
| Success text | `#1E4D34` | Text inside success callouts |
| Success border | `#3B8067` | Border on success callouts |
| Warning label | `#854F0B` | Warning label text |
| Warning bg | `#FFFBF0` | Background of warning callouts |
| Warning border | `#FAC775` | Border on warning callouts |
| Warning text | `#633806` | Text inside warning callouts |
| Lime CTA | `#d4ff00` | Speaking-page "Book" buttons only — do not reuse elsewhere |

### Neutrals

| Hex | Usage |
|---|---|
| `#F8F4ED` | Body and footer background |
| `#F1EFE8` | Badge backgrounds |
| `#E0DDD8` | Borders, dividers |
| `#D3D1C7` | Insight card borders |
| `#999` | Meta text, timestamps |
| `#888` | Tech stack labels |
| `#666` | Card descriptions |
| `#444` | Body copy in case studies |

---

## 3. Typography

### Font families

| Role | Font | Weights | Usage |
|---|---|---|---|
| Display / headings | **Montserrat** | 300, 400, 500, 600, 700 | Nav, section titles, buttons, eyebrow labels |
| Editorial titles | **Playfair Display** | 400, 500, 600, 700 | Article/post h1, large page headings |
| Body copy | **Inter** | 300, 400, 500, 600, 700 | Paragraphs, footer, labels |
| Monospace labels | **DM Mono** | 400, 500 | Section labels, card labels, technical annotations |

All fonts loaded via Google Fonts in `layouts/_default/baseof.html`.

### Type scale

| Element | Size | Notes |
|---|---|---|
| Hero h1 | `clamp(3rem, 8vw, 5rem)` | Home hero only |
| Page h1 | `clamp(2rem, 5vw, 3rem)` | Standard page title |
| h2 | `clamp(2rem, 4vw, 3rem)` | Section headings |
| h3 | `clamp(1.4rem, 2.5vw, 1.8rem)` | Subsections, card titles |
| Body | `1.1rem / 1.6` | Default paragraph |
| Meta / small | `0.7rem – 0.85rem` | Dates, tags, captions |
| Footer | `0.875rem` | Footer copy |

---

## 4. Layout & Spacing

### Containers

| | |
|---|---|
| Max width | `1200px` |
| Narrow (articles, posts) | `800px – 860px` |
| Medium | `900px – 1100px` |
| Horizontal padding (desktop) | `0 2rem` |
| Horizontal padding (mobile) | `0 1.25rem – 1.5rem` |

### Vertical rhythm

| | Desktop | Mobile |
|---|---|---|
| Section padding | `5rem 0` | `4rem 0` |
| Page header | `5rem 0 2rem` | — |
| Content block | `3.5rem 2rem – 5rem 2rem` | — |
| Card padding | `1.25rem – 2rem` | — |

### Responsive breakpoints

| Breakpoint | Value |
|---|---|
| Mobile | `max-width: 640px` |
| Tablet | `max-width: 768px` |
| Laptop | `max-width: 860px` |
| XL / wide | `min-width: 1600px` |

---

## 5. Component Tokens

### Navigation

- Position: fixed top
- Height: `76px` (desktop) · `53px` (mobile)
- Background: `rgba(250,247,242,0.92)` + `backdrop-filter: blur(10px)`
- Border-bottom: `1px solid rgba(0,0,0,0.08)`
- Font: Montserrat

### Buttons — outline (default)

```
border: 1.5px solid #1c1c1c
background: transparent
color: #1c1c1c
padding: 1.1rem 2.5rem
font: Montserrat, uppercase, 0.7rem, 600
hover: background #1c1c1c, color #ffffff
```

### Buttons — filled CTA

```
background: #1A3828
color: #ffffff
padding: 0.7rem 1.4rem
border-radius: 5px
font: Montserrat, 0.85rem, 600
```

### Cards

```
background: #ffffff
border: 1px solid rgba(0,0,0,0.07)
border-radius: 10px – 12px
box-shadow: 0 2px 20px rgba(0,0,0,0.05)
padding: 1.25rem – 2rem
hover: translateY(-3px) + deeper box-shadow
```

### Footer

```
background: #F8F4ED
padding: 3.5rem 2rem 2rem
border-top: 1px solid rgba(0,0,0,0.08)
font: Inter, 0.875rem
color: #444
```

### Case study headers

```
border-bottom: 2px solid #2A6048
gradient accent: linear-gradient(90deg, #2A6048, #7BBDA0)
metrics background: #E6F4ED
metric value color: #2A6048
architecture card background: #1B4332
architecture card text: #7BBDA0
```

---

## 6. Navigation Menu

| Label | Path |
|---|---|
| Perspectives | `/perspectives/` |
| AI Guides | `/ai-guides/` |
| Portfolio | `/portfolio/` |
| About | `/about/` |

---

## 7. Source Files

| File | Role |
|---|---|
| `assets/css/main.css` | All global tokens and components |
| `assets/css/case-study.css` | Case study overrides |
| `layouts/_default/baseof.html` | Font imports, `<head>` meta |
| `layouts/partials/header.html` | Navigation |
| `layouts/partials/footer.html` | Footer |
| `layouts/index.html` | Home page / hero |
| `hugo.toml` | Site config, params |
