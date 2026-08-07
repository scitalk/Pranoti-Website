#!/usr/bin/env python3
"""Convert cached campaigns into draft Hugo pages + a triage table.

    tools/.venv/bin/python tools/build_archive.py [--limit N]

Reads tools/campaigns.json (from fetch_campaigns.py). Writes:
  content/newsletter-archive/<date>-<slug>.md   every one draft: true
  tools/triage.md                               review table

Email HTML is converted to Markdown so .Content is real text — that is what
makes the RSS feed and search indexing work. An iframe would leave both empty.
"""

import argparse
import json
import pathlib
import re
import sys
import urllib.parse

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
CACHE = HERE / "campaigns.json"
OUTDIR = ROOT / "content" / "newsletter-archive"

MERGE_TAG = re.compile(r"\{\$[a-z_]+\}")

# Footer / chrome text that should not become archive content.
JUNK_PATTERNS = [
    re.compile(p, re.I)
    for p in (
        r"unsubscribe",
        r"you.{0,20}receiving this",
        r"update your preferences",
        r"view (this )?(email )?in (your )?browser",
        r"sent (via|by) mailerlite",
        r"^\s*powered by\s*$",
    )
]


# Where the newsletter ends and the email chrome begins. Everything from the
# first of these onward is dropped.
FOOTER_START = [
    re.compile(p, re.I)
    for p in (
        r"you received this email",
        r"you.{0,25}receiving this",
        r"find under the microscope podcast on your preferred platform",
        r"the science talk\s+e7",          # postal address block
        r"\b\d{5}\s+mannheim",
        r"^e7,\s*8",                       # street address, standalone line
        r"^#{0,6}\s*the science talk\s*$", # sender sign-off heading
        r"^\s*thesciencetalk\s*$",
        r"sent (via|by) mailerlite",
    )
]

# Forward/share CTA blocks — boilerplate, not part of the newsletter's writing.
SHARE_CTA = [
    re.compile(p, re.I)
    for p in (
        r"forward this email",
        r"^found this useful\??$",
        r"^\[forward\]\(mailto:",
    )
]


class EmailConverter(MarkdownConverter):
    """Standard conversion; layout tables are unwrapped before we get here."""


def unwrap_tracking(url):
    """MailerLite wraps links in click-tracking redirects; recover the target."""
    if not url:
        return url
    if "click.mailerlite.com" in url or "/lt.php" in url:
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        for key in ("url", "l", "target"):
            if key in qs and qs[key][0].startswith("http"):
                return qs[key][0]
    return url


def clean_html(raw):
    soup = BeautifulSoup(raw, "html.parser")

    for tag in soup(["style", "script", "head", "meta", "title", "noscript"]):
        tag.decompose()

    # Tracking pixels and spacer images.
    for img in soup.find_all("img"):
        src = img.get("src", "")
        w, h = str(img.get("width", "")), str(img.get("height", ""))
        if w in ("1", "0") or h in ("1", "0") or "open.gif" in src or not src:
            img.decompose()

    # Hidden preheader text — duplicates the subject line.
    for el in soup.find_all(style=True):
        if el.attrs is None or el.parent is None:
            continue  # already decomposed as a descendant of an earlier match
        s = (el.get("style") or "").replace(" ", "").lower()
        if "display:none" in s or "max-height:0" in s or "opacity:0" in s:
            el.decompose()

    for a in soup.find_all("a", href=True):
        a["href"] = unwrap_tracking(a["href"])

    # Unwrap layout tables BEFORE markdownify sees them: it suppresses
    # paragraph breaks inside cells, which flattens older emails into one blob.
    for tag in soup.find_all(["table", "tbody", "thead", "tfoot", "tr", "td", "th"]):
        tag.unwrap()

    return str(soup)


def cut_footer(md):
    """Drop everything from the first footer marker onward."""
    lines = md.split("\n")
    for i, ln in enumerate(lines):
        probe = re.sub(r"[\[\]\(\)\*_>#!]", " ", ln).strip()
        if probe and any(p.search(probe) for p in FOOTER_START):
            return "\n".join(lines[:i]).strip()
    return md


def strip_junk(md):
    lines, kept = md.split("\n"), []
    for ln in lines:
        probe = re.sub(r"[\[\]\(\)\*_>#!]", "", ln).strip()
        if probe and any(p.search(probe) for p in JUNK_PATTERNS):
            continue
        kept.append(ln)
    md = "\n".join(kept)
    md = MERGE_TAG.sub("", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"^[\s|>*_-]+$", "", md, flags=re.M)  # leftover rules
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def strip_share_cta(md):
    """Drop 'Found this useful? Forward this email...' blocks, any wording."""
    blocks = md.split("\n\n")
    kept = []
    for b in blocks:
        probe = re.sub(r"[\[\]\(\)\*_>#!]", " ", b).strip()
        if any(p.search(probe) for p in SHARE_CTA):
            continue
        kept.append(b)
    return "\n\n".join(kept)


def to_markdown(raw):
    md = EmailConverter(heading_style="ATX").convert(clean_html(raw))
    md = strip_junk(cut_footer(md))
    md = strip_share_cta(md)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def slugify(s, fallback):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:70]
    return s or fallback


def make_description(preheader, body):
    """Meta description: preheader if it reads as one, else the opening of the body."""
    ph = (preheader or "").strip()
    if 40 <= len(ph) <= 200:
        return ph

    plain = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)          # images: drop entirely
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)     # links: keep link text
    plain = re.sub(r"[#*_>`]", "", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) <= 160:
        return plain
    cut = plain[:160].rsplit(" ", 1)[0]
    return cut + "…"


# Confirmed duplicates / unwanted sends, dropped from the archive entirely.
# campaign_id -> reason (kept here so a re-run stays consistent).
EXCLUDED = {
    "166406476143789916": "byte-identical resend of 2025-09-21 workshop invite, smaller batch",
    "172236263394379356": "same body as 2025-11-27 05:46 NanoBananaPro, subject-only variant",
    "194962387786270287": "2026-08-05 LinkedIn/Article 50 resend, dropped per review",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="convert only the first N (sampling)")
    args = ap.parse_args()

    if not CACHE.exists():
        sys.exit(f"No cache at {CACHE}. Run tools/fetch_campaigns.py first.")

    campaigns = json.loads(CACHE.read_text())
    campaigns = [c for c in campaigns if c["id"] not in EXCLUDED]
    campaigns.sort(key=lambda c: c.get("finished_at") or "")
    if args.limit:
        campaigns = campaigns[: args.limit]

    OUTDIR.mkdir(parents=True, exist_ok=True)
    rows, seen_subjects = [], {}

    for seq, c in enumerate(campaigns, 1):
        body = to_markdown(c.get("_html") or "")
        sent = (c.get("finished_at") or "")[:19].replace(" ", "T")
        date = sent[:10]
        subject = c.get("_subject") or c.get("name") or "(untitled)"
        slug = slugify(subject, c["id"])
        fname = f"{date}-{slug}.md"

        words = len(re.sub(r"[#*\[\]()_>`!-]", " ", body).split())
        description = make_description(c.get("_preheader"), body)

        front = "\n".join(
            [
                "---",
                f"title: {json.dumps(subject)}",
                f"description: {json.dumps(description)}",
                f"date: {sent}",
                "draft: true",
                f"sequence: {seq}",
                f'campaign_id: "{c["id"]}"',
                f"campaign_name: {json.dumps(c.get('name') or '')}",
                f"preheader: {json.dumps(c.get('_preheader') or '')}",
                f"sent_count: {(c.get('stats') or {}).get('sent', 0)}",
                "---",
                "",
            ]
        )
        (OUTDIR / fname).write_text(front + body + "\n")

        flags = []
        if words < 60:
            flags.append("SHORT — check conversion")
        if subject in seen_subjects:
            flags.append(f"duplicate subject of {seen_subjects[subject]}")
        seen_subjects.setdefault(subject, date)
        for addr in set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", body)):
            if addr not in ("pranoti@thesciencetalk.com", "contact@thesciencetalk.com"):
                flags.append(f"email addr: {addr}")

        rows.append((date, subject, words, (c.get("stats") or {}).get("sent", 0),
                     "; ".join(flags), fname))

    with (HERE / "triage.md").open("w") as f:
        f.write(f"# Newsletter archive triage — {len(rows)} campaigns\n\n")
        f.write("All files are `draft: true`. Mark any that should NOT be published.\n\n")
        f.write("| # | Date | Subject | Words | Sent | Flags |\n")
        f.write("|---|---|---|---|---|---|\n")
        for i, (date, subj, words, sent, flags, _) in enumerate(rows, 1):
            f.write(f"| {i} | {date} | {subj[:65].replace('|', '/')} | {words} | "
                    f"{sent} | {flags} |\n")

    flagged = sum(1 for r in rows if r[4])
    print(f"{len(rows)} drafts → {OUTDIR}")
    print(f"{flagged} flagged for review")
    print(f"Triage table: {HERE / 'triage.md'}")


if __name__ == "__main__":
    main()
