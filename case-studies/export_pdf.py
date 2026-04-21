#!/usr/bin/env python3
"""
Export case study pages to single square-page PDFs.
The square side = max(content width, content height) — no scaling, text is full size.

Requires: pip install playwright && python -m playwright install chromium

Usage:
  python export_pdf.py           # export all case studies
  python export_pdf.py --build   # run 'hugo' first, then export
"""

import argparse
import subprocess
import sys
import threading
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
PUBLIC_DIR = PROJECT_ROOT / "public"
OUTPUT_DIR = SCRIPT_DIR  # PDFs land in static/case-studies/

VIEWPORT_WIDTH_PX = 1200  # render width; wider than CSS max-width 1100px
PORT = 8765

SLUGS = [
    "google-sheets-mcp",
    "wordpress-claude-mcp",
    "restore-wordpress-wpengine",
]


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        print("Installing playwright...")
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        from playwright.sync_api import sync_playwright
        return sync_playwright


def run_hugo():
    print("Building Hugo site...")
    result = subprocess.run(["hugo"], cwd=PROJECT_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)
    print("Hugo build complete.\n")


def start_server(directory: Path, port: int) -> HTTPServer:
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    handler.log_message = lambda *_: None  # type: ignore[method-assign]
    server = HTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def export_one(page, slug: str, port: int):
    url = f"http://127.0.0.1:{port}/case-studies/{slug}/"
    pdf_path = OUTPUT_DIR / f"{slug}.pdf"

    page.set_viewport_size({"width": VIEWPORT_WIDTH_PX, "height": 900})
    page.goto(url)
    page.wait_for_load_state("networkidle")

    # Measure full content height at render width
    content_h = page.evaluate("document.documentElement.scrollHeight")

    # Square side = larger of width and height — no scaling, text stays full size
    side = max(VIEWPORT_WIDTH_PX, content_h)

    page.pdf(
        path=str(pdf_path),
        width=f"{side}px",
        height=f"{side}px",
        print_background=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
    )

    print(f"✓ {pdf_path.name}  ({pdf_path.stat().st_size / 1024:.1f} KB)  [{side}×{side}px]")


def export():
    if not PUBLIC_DIR.exists():
        print(f"Error: {PUBLIC_DIR} not found. Run with --build or run 'hugo' first.")
        sys.exit(1)

    server = start_server(PUBLIC_DIR, PORT)
    print(f"Serving public/ on http://127.0.0.1:{PORT}\n")

    sync_playwright = ensure_playwright()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()

        for slug in SLUGS:
            built_page = PUBLIC_DIR / "case-studies" / slug / "index.html"
            if not built_page.exists():
                print(f"⚠ Skipping {slug} — {built_page} not found")
                continue
            export_one(pg, slug, PORT)

        browser.close()

    server.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export case studies to single square-page PDFs")
    parser.add_argument("--build", action="store_true", help="Run 'hugo' first, then export")
    args = parser.parse_args()

    if args.build:
        run_hugo()

    export()
