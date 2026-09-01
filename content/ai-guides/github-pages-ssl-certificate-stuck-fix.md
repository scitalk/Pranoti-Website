---
title: "GitHub Pages SSL Certificate Stuck? How to Force a Fix"
date: 2026-07-21
lastmod: 2026-07-21
slug: "github-pages-ssl-certificate-stuck-fix"
draft: false
description: "Your GitHub Pages SSL certificate can get stuck retrying for hours despite correct DNS. Here's the exact fix: force a fresh DNS record instead of waiting."
keywords: ["github pages ssl certificate stuck", "certificate request error github pages", "github pages https not working", "cloudflare dns github pages", "force renew github pages certificate", "github pages dns check successful no https", "letsencrypt caa record github pages"]
author: "Pranoti Kshirsagar"
reading_time: "5 min"
tags: ["GitHub Pages", "SSL/TLS", "Cloudflare", "DNS", "Hugo"]
category: "ai-integration-guides"
pillar: "AI Adoption"
sidebar_links:
  - title: "How to Rotate an Expiring GitHub Token on GitHub Pages"
    url: "/ai-guides/rotate-expiring-github-token-github-pages/"
  - title: "How to Restore a Single WordPress Page from a WP Engine Backup"
    url: "/ai-guides/restore-wordpress-page-wpengine-backup/"
  - title: "AI Content Intelligence Workflow: WordPress, GA4, Clarity, GitHub"
    url: "/perspectives/ai-content-intelligence-workflow-wordpress-ga4-clarity-github/"
---

A GitHub Pages custom domain's SSL certificate can expire and get stuck in a retry loop. GitHub's own documentation says this may take **up to 24 hours** to resolve, even when your DNS, CNAME, and CAA records are all correctly configured. This guide covers the exact fix for that stuck state. It resolves the issue in minutes rather than hours.

## What you need before starting

- A GitHub Pages site with a custom domain configured
- Access to your DNS provider's dashboard (this guide uses Cloudflare, but the principle applies to any provider)
- Repository admin access to **Settings → Pages**
- `dig` and `curl` available in a terminal, for verification

## Confirm the SSL certificate is actually stuck, not DNS

Before touching any settings, confirm the site is failing on an expired certificate rather than a DNS problem:

```bash
curl -v https://yourdomain.com/ 2>&1 | grep -iE "certificate|SSL|expire"
```

An expired cert returns something like:

```
* SSL certificate problem: certificate has expired
```

If instead you see a DNS resolution failure or connection timeout, the problem sits upstream of the certificate. This guide does not apply. Check your DNS records first.

## Rule out DNS, CNAME, and CAA misconfiguration

GitHub's certificate provisioning depends on three things being correct. Verify each one before you assume the retry loop will resolve itself.

**CNAME record**, must point your subdomain at `<username>.github.io`:

```bash
dig +short yourdomain.com CNAME
```

**Cloudflare proxy status**: if you use Cloudflare, the record must be **DNS-only (grey cloud)**, not proxied (orange cloud). A proxied record blocks GitHub from completing the Let's Encrypt HTTP-01 challenge, since the request never reaches GitHub's servers directly.

**CAA records**: if your domain has any CAA records at all, at least one must explicitly allow `letsencrypt.org`, or GitHub cannot issue a certificate:

```bash
dig +short yourdomain.com CAA
```

A permissive result looks like:

```
0 issue "letsencrypt.org"
```

Check propagation across more than one public resolver. A single resolver's cache can lag.

```bash
dig +short yourdomain.com CNAME @8.8.8.8
dig +short yourdomain.com CNAME @1.1.1.1
dig +short yourdomain.com CNAME @9.9.9.9
```

> If all three checks pass and the GitHub Pages settings page still shows **"Certificate Request Error: Certificate provisioning will retry automatically"** after 30+ minutes, the retry loop itself is the problem, not your DNS.

## When correct DNS still is not enough

GitHub's UI and docs do not make this part obvious. A correct DNS record does not guarantee that GitHub's Let's Encrypt retry queue actually re-attempts against fresh state. It can loop against a **stale cached lookup** from before you fixed your DNS, particularly after a certificate has already expired once. Simply removing and re-adding the custom domain in GitHub Pages settings is often not enough to break this loop. That step alone can leave it stuck for the same 30+ minutes with no change.

## The fix: force a fresh DNS record

Make GitHub see a **genuinely new** DNS record, not an edited one it may have already flagged as failed.

### Step 1: Delete and recreate the DNS record

In your DNS provider (this guide shows Cloudflare):

1. Delete the CNAME record for your subdomain entirely. Do not just edit it.
2. Wait about a minute.
3. Recreate it identically: same subdomain, same target (`<username>.github.io`), DNS-only/grey cloud.

Delete and recreate the record rather than edit it in place. This forces a new record rather than a modification GitHub's system may treat as the same failed lookup.

### Step 2: Confirm the new record propagated

Before you touch GitHub, verify the fresh record resolves cleanly:

```bash
dig +short yourdomain.com CNAME +noall +answer
```

Check the TTL value in the output. A low, recently reset TTL confirms you see the new record rather than a cached one.

### Step 3: Remove and re-add the custom domain on GitHub

In your repository, go to **Settings → Pages**:

1. Click **Remove** on the custom domain field.
2. Wait for the field to fully clear and the page to settle.
3. Re-type your domain (for example, `yourdomain.com`).
4. Click **Save**.

GitHub re-runs its **DNS Check** against the record you just created in Step 1, not the stale one. It should show **"DNS Check successful"** within a few minutes. Certificate issuance follows shortly after. The **Enforce HTTPS** checkbox becomes available once the cert is live.

## Troubleshooting

**Still stuck after the remove/recreate cycle.** Wait the full 24 hours GitHub's docs mention before you escalate. Some retry cycles genuinely take that long even after a clean re-trigger. If it has been stuck for multiple days with confirmed-correct DNS, [GitHub Support](https://support.github.com/) can manually re-trigger Let's Encrypt issuance. Do not remove and re-add the domain again while you wait on a support ticket. Repeated resets can push you to the back of the retry queue rather than speed things up.

**Cloudflare proxy was on and you just turned it off.** Allow a few minutes for the proxy change itself to propagate before you start the delete/recreate cycle. Doing both at once makes it hard to tell which change fixed things.

**You cannot check certificate status via the GitHub API.** Unauthenticated calls to `/repos/{owner}/{repo}/pages` return a 404, even for public repositories:

```bash
curl -s https://api.github.com/repos/owner/repo/pages
```

This result is not a sign anything is broken. That endpoint requires an authenticated token regardless of repo visibility. Use `curl -v` against your live domain for direct certificate inspection. Use the **Settings → Pages** UI for provisioning status, rather than the API.

**Extra A or AAAA records on the apex domain.** If your domain has leftover A/AAAA/ALIAS records that point elsewhere alongside the CNAME, remove them. Conflicting records at the apex or on `www` are a separate, common cause of stuck provisioning that this fix will not resolve.

**Related maintenance to check while you are in the repo settings.** If it has also been a while since you rotated the token this deploy workflow depends on, see [how to rotate an expiring GitHub token on GitHub Pages](/ai-guides/rotate-expiring-github-token-github-pages/). A stuck certificate and an expiring token are unrelated failures, but both show up as "the site is broken" with no obvious cause.

## What you can do now

You can now diagnose whether a GitHub Pages HTTPS failure is a DNS problem or a stuck retry queue. You can force a fix in minutes rather than wait out GitHub's stated 24-hour window. The same delete-and-recreate approach applies any time you must re-provision a working custom domain's certificate, for example after a domain transfer, a DNS provider migration, or a similar disruption to the record GitHub last validated against.

---
*Want more guides like this? Browse all [AI Guides](/ai-guides/) or [get in touch →](https://thesciencetalk.com/contact-us/)*
