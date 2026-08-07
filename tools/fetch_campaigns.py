#!/usr/bin/env python3
"""Fetch sent MailerLite campaigns and cache them locally. Read-only.

    tools/.venv/bin/python tools/fetch_campaigns.py

Writes tools/campaigns.json (list payload + full HTML per campaign). Cached, so
re-running the archive build never needs to hit the API again.

Token: ~/.mailerlite-token or $MAILERLITE_TOKEN. Never stored in the repo.
"""

import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

BASE = "https://connect.mailerlite.com/api/campaigns"
HERE = pathlib.Path(__file__).parent
CACHE = HERE / "campaigns.json"
TOKEN_FILE = pathlib.Path.home() / ".mailerlite-token"


def token():
    if os.environ.get("MAILERLITE_TOKEN"):
        return os.environ["MAILERLITE_TOKEN"].strip()
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text().strip()
    sys.exit(f"No token. Put it in {TOKEN_FILE} or export MAILERLITE_TOKEN.")


def get(url, tok):
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {tok}",
            "Accept": "application/json",
            "User-Agent": "pranoti-newsletter-archive/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        if e.code == 403:
            detail += "\n\nIf the token has an IP allowlist, check your IP still matches: curl -s https://api.ipify.org"
        sys.exit(f"HTTP {e.code} on {url}\n{detail}")


def aud(c):
    f = c.get("filter_for_humans")
    return " ".join(map(str, f)) if isinstance(f, list) else str(f)


def is_general(c):
    """General-list sends: named General*, or targeted at Organic subscribers.
    Resends excluded — they duplicate an earlier campaign's content."""
    name = c.get("name") or ""
    if name.lower().startswith("resend"):
        return False
    return name.startswith("General") or "Organic subscribers" in aud(c)


def main():
    tok = token()

    print("Listing sent campaigns…")
    campaigns, page = [], 1
    while True:
        payload = get(f"{BASE}?filter[status]=sent&limit=50&page={page}", tok)
        batch = payload.get("data", [])
        campaigns.extend(batch)
        print(f"  page {page}: +{len(batch)} (total {len(campaigns)})")
        meta = payload.get("meta") or {}
        if not batch or (meta.get("last_page") and page >= meta["last_page"]):
            break
        page += 1
        time.sleep(0.3)

    picked = [c for c in campaigns if is_general(c)]
    picked.sort(key=lambda c: c.get("finished_at") or "")
    print(f"\n{len(campaigns)} sent, {len(picked)} on the general list.")
    print("Fetching full content (list endpoint omits the HTML)…")

    for i, c in enumerate(picked, 1):
        detail = get(f"{BASE}/{c['id']}", tok)["data"]
        email = (detail.get("emails") or [{}])[0]
        c["_html"] = email.get("content") or ""
        c["_subject"] = email.get("subject") or ""
        c["_preheader"] = email.get("preheader") or ""
        print(f"  [{i}/{len(picked)}] {(c.get('finished_at') or '')[:10]}  "
              f"{c['_subject'][:52]}  ({len(c['_html'])} chars)")
        time.sleep(0.25)

    CACHE.write_text(json.dumps(picked, indent=2))
    print(f"\nCached {len(picked)} campaigns → {CACHE}")
    print("Next: tools/.venv/bin/python tools/build_archive.py")


if __name__ == "__main__":
    main()
