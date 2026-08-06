# ⚖️ Legal pages — your to-do list

**Status:** pages are written and building. They are **not publishable yet** — 5 placeholders need your real details.

**Total time: about 90 minutes.** Steps 1–3 are the blockers. Everything else can wait.

---

## 🔴 BLOCKERS — do these before you deploy

### 1. Fill in your address — 5 minutes ✅ START HERE

Same address, 3 files. Find-and-replace `[STREET AND HOUSE NUMBER]` and `[POSTCODE]`.

| File | Line |
|---|---|
| `content/imprint.md` | 14, 15 |
| `content/privacy.md` | 14 |
| `content/terms.md` | 13, 63 |

> ⚠️ **A PO box is not enough.** § 5 DDG requires a real, physical, summonable address. If you don't want your home address public, get a `c/o` business address first (~€10/month) — otherwise this step blocks everything.

**Line 63 of `terms.md`** is inside the withdrawal form, written as `[ADDRESS]` — same address, one line.

---

### 2. Decide your VAT status — 10 minutes

Pick **ONE**. This affects 2 files.

**➊ If you HAVE a VAT ID:**
- `content/imprint.md` line 27 → replace `[DE XXXXXXXXX]` with your real number
- `content/terms.md` line 29 → keep only: `Prices include statutory VAT where applicable.`
- Delete the HTML comment at `imprint.md` lines 29–30

**➋ If you are a Kleinunternehmer (§ 19 UStG):**
- `content/imprint.md` line 27 → replace the whole line with: `No VAT identification number. Small business under § 19 UStG — no VAT is charged.`
- `content/terms.md` line 29 → keep only: `As a small business under § 19 UStG, no VAT is charged.`
- Delete the HTML comment at `imprint.md` lines 29–30

> 💡 Not sure? Check last year's tax return, or ask your Steuerberater. Don't guess — a wrong VAT statement on an imprint is exactly what Abmahnung letters target.

---

### 3. Add the refund waiver to Stripe — 20 minutes 🔥 MOST IMPORTANT

**Why this matters:** without it, every buyer of your €12–19 PDFs keeps a **14-day refund right, even after downloading**. The terms page alone does *not* fix this — Stripe has to collect the tick.

**For each of your 7 payment links:**

1. Go to Stripe Dashboard → **Payment Links**
2. Open the link → **Options** → **Custom fields** (or Checkout settings → Custom text / Terms of service)
3. Add a **required checkbox** with this text:

```
I expressly request that you begin performance of the contract before the end of the withdrawal period. I acknowledge that I lose my right of withdrawal once the download begins.
```

4. Set the **Terms of Service URL** to `https://pranoti.thesciencetalk.com/terms/`

**Your 7 links to update:**

- [ ] ERC Starting Grant Kit
- [ ] ERC Advanced Grant Kit
- [ ] ERC Consolidator Grant Kit
- [ ] ERC Synergy Grant Kit
- [ ] Claude WordPress MCP Guide
- [ ] Claude Google Sheets MCP Guide
- [ ] The Claude CV System

---

## 🟡 VERIFY — 15 minutes, after steps 1–3

Run the site locally:

```bash
hugo server -D
```

Then check each box:

- [ ] **Banner appears** on first load at `localhost:1313`
- [ ] **Open DevTools → Network, filter `gtag`** → nothing loads before you click
- [ ] **Click "Reject"** → banner closes, still no `gtag` request
- [ ] **Hard-refresh** → banner does NOT come back
- [ ] **Click "Accept analytics"** → now `gtag/js` loads in Network tab
- [ ] **Footer links work:** Imprint / Privacy / Cookie Policy / Terms / AI Disclosure
- [ ] **"Cookie settings" button** in the footer re-opens the banner
- [ ] **Check on your phone** — banner buttons should stack, not overflow
- [ ] **Read your own address** on `/imprint/` — typo check

---

## 🟢 RECOMMENDED — do within the month

### 4. Self-host Google Fonts — 30 minutes

Fonts currently load from Google's servers, sending every visitor's IP to Google. A Munich court (LG München I, 3 O 17493/20) awarded damages for exactly this.

**Say the word and I'll do it** — it's mechanical: download Inter + Playfair Display, drop them in `static/fonts/`, swap the `<link>` tags, delete section 4 of the privacy policy.

### 5. Have a German lawyer skim it — 30 min consult

Ask them to look at **two things only**:
- `terms.md` § 6 (withdrawal waiver)
- `terms.md` § 10 (liability limits)

The rest is standard boilerplate. I drafted these to the right structure, but I'm not a lawyer and the imprint carries real Abmahnung risk.

### 6. Delete the stale events page — 2 minutes

`static/events/index.html` is an old "The Science Talk"–branded page that bypasses your layouts entirely. No analytics on it, so not a compliance problem — just cruft.

---

## ✅ ALREADY DONE — no action needed

- Cookie banner built, Reject is equal weight to Accept
- GA4 stripped out of all 9 layout files, now loads only after consent
- Google Consent Mode v2, everything denied by default
- Consent stored 12 months, then re-asked
- 5 legal pages written, linked in the footer
- Legal pages set to `noindex` so they don't compete with your real content
- AI Disclosure page covers EU AI Act Art. 50 (applies **2 August 2026** — you're ahead of it)

---

*Created 28 July 2026. Delete this file once steps 1–3 are done.*
