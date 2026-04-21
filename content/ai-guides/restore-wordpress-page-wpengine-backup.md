---
title: "How to Restore a Single WordPress Page from a WP Engine Backup"
date: 2026-03-19
lastmod: 2026-04-02
draft: false
description: "WordPress has no native single-page restore. Here is the exact workflow to extract one page from a WP Engine database dump and push it back via the REST API — without touching the rest of your site."
keywords: ["WordPress restore single page", "WP Engine backup", "WordPress REST API", "restore WordPress page", "wp_posts database", "Claude AI WordPress", "WordPress MCP"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["WordPress", "WP Engine", "REST API", "MCP", "Database"]
category: "ai-integration-guides"
sidebar_links:
  - title: "Connect WordPress to Claude Desktop via MCP"
    url: "/ai-guides/connect-wordpress-claude-desktop-mcp-guide/"
  - title: "Connect Claude Desktop to Google Sheets via MCP"
    url: "/ai-guides/connect-claude-desktop-google-sheets-mcp-guide/"
  - title: "Automate Event Registration with Stripe, Make.com & MailerLite"
    url: "/ai-guides/event-registration-automation-stripe-make-mailerlite/"
---

WordPress does not have a native "restore single page from backup" feature. WP Engine's backup system saves your entire site — database and files — as one package. To restore one page, you go into the raw database dump and extract it yourself.

This post documents exactly how I did it: extracting a single page from a WP Engine full-site database backup and restoring it to WordPress via the REST API, section by section, without touching anything else on the site.

## The problem

The page in question was my proposal writing service page — a custom-built page with 11 distinct content blocks including a hero section, lifecycle diagram, two testimonial carousels, a testimonials grid, and a contact form. During an earlier restoration attempt, only the hero block had been pushed. Everything else was missing.

> **Core challenge:** WordPress does not let you restore a single page from a backup. WP Engine saves your entire site as one package. To restore one page, you have to go into the raw database dump and extract it yourself.

## What you need before starting

- A **WP Engine full backup** downloaded locally — specifically the `mysql.sql` file inside the backup zip (typically 50–200MB)
- Access to your **WordPress REST API** — via an application password, or a connected MCP tool with write access
- **Python 3** installed locally
- The **post ID** of the page you want to restore — find it in WP Admin → Pages → Edit, where the URL contains `post=XXXXX`

> Using Claude with the WordPress MCP tool? You already have REST API write access built in — that is exactly how I pushed the restored content in this workflow.

## Step 1: Locate the database backup file

In WP Engine, go to **Sites → Backups → Download**. Unzip the archive. The file you need is `mysql.sql`, found at `wp-content/mysql.sql`. At 80MB+ it is far better to work with it via a script than trying to open it in a text editor.

## Step 2: Extract the page content from the database dump

WordPress stores all page content in the `wp_posts` table. Each page has a `post_content` field with its full Gutenberg block markup. Run this to extract the row for your specific page:

```python
import re

with open('/path/to/mysql.sql', 'r', encoding='utf-8', errors='replace') as f:
    sql = f.read()

# Replace YOUR_POST_ID with the actual ID from your WP Admin URL
pattern = r"\(YOUR_POST_ID,.*?\)(?=,\(|\s*;)"
match = re.search(pattern, sql, re.DOTALL)

if match:
    row = match.group(0)
    with open('extracted_row.txt', 'w') as out:
        out.write(row)
    print("Row extracted. Length:", len(row))
else:
    print("Post not found — check your post ID")
```

Once you have the raw row, find the `post_content` field — it is the large block of HTML/Gutenberg markup. **Copy everything from the first `<!-- wp:` to the final closing block comment**, and save it as a plain `.html` file. This is your restoration file.

## Step 3: Audit the block structure before pushing

Before pushing, scan the content to understand exactly what you are restoring. This gives you a checklist to verify after each API call:

```python
import re

with open('page_content.html', 'r') as f:
    content = f.read()

blocks = re.findall(r'<!-- wp:[^\s>]+ ', content)
print(f"Total characters: {len(content)}")
print("Block types found:")
for b in blocks:
    print(" ", b)
```

## Step 4: Push the content via the WordPress REST API

Generate an application password in **WP Admin → Users → Profile → Application Passwords**, then push:

```python
import requests
from requests.auth import HTTPBasicAuth

with open('page_content.html', 'r') as f:
    content = f.read()

response = requests.post(
    'https://yoursite.com/wp-json/wp/v2/pages/YOUR_POST_ID',
    auth=HTTPBasicAuth('your_username', 'your_application_password'),
    json={'content': content}
)

print(response.status_code)
# Always check the raw field — not rendered
print(response.json().get('content', {}).get('raw', '')[:500])
```

> Always read back the **`raw` field** from the API response — not `rendered`. The rendered version applies WordPress filters and will look different from your source. Raw shows exactly what was saved.

## Step 5: Handle large pages in accumulating sections

If your page is large — mine was **24,323 characters across 11 blocks** — push in sections. Push blocks 1–5, confirm the raw content saved correctly, then push 1–5 plus block 6, and so on. Each call replaces the entire page content, so always send the full accumulated content — not just the new section.

> **Watch out for UAGB/Spectra blocks.** These store large JSON configuration inline. A single testimonial block with images can run to 7,000+ characters on its own — plan your section splits accordingly.

## Step 6: Verify the restored page against the backup

Once all sections are pushed, read the `raw` content back and compare against your source file:

```python
response = requests.get(
    'https://yoursite.com/wp-json/wp/v2/pages/YOUR_POST_ID',
    auth=HTTPBasicAuth('your_username', 'your_application_password'),
    params={'context': 'edit'}
)

live_content = response.json()['content']['raw']

with open('page_content.html', 'r') as f:
    backup_content = f.read()

if live_content.strip() == backup_content.strip():
    print("✅ Perfect match")
else:
    print("⚠️ Differences found")
    print(f"Live: {len(live_content)} chars | Backup: {len(backup_content)} chars")
```

Pay particular attention to **testimonial blocks** — these contain long quote text stored as escaped HTML inside JSON attributes. Always verify quote text against the original SQL dump, not from memory.

## What this approach does not fix

This method restores the `post_content` field only. These sit outside that field and need separate handling:

- **Custom page CSS** stored in post meta (e.g. `_uag_custom_page_level_css`) — requires a separate meta update call
- **Yoast SEO meta fields** — title, description, and schema settings live separately
- **Featured image assignments** and **page template settings** — these are in post meta, not post content

> If your *entire site* needs restoring, use WP Engine's one-click restore instead. This manual approach is specifically for restoring a single page's content without touching anything else — no downtime, no risk to other pages.

## The result

The page was fully restored from backup: all 11 content blocks live, all testimonial quotes exact, the contact form back in its correct layout, and custom CSS intact. The process took one working session with no WP Engine support ticket, no full-site restore, and no developer access beyond the REST API.

---

## Related reading on The Science Talk

This guide accompanies the [full WP Engine page restore post on The Science Talk](https://thesciencetalk.com/restore-wordpress-page-wpengine-backup/) — covering how this situation arose, why a full restore was not an option, and what the WordPress MCP made possible.

Need help setting up Claude Desktop with your WordPress site? [Get in touch →](https://thesciencetalk.com/contact-us/)
