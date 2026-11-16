#!/usr/bin/env python3
"""Read-only AdSense readiness checker.

Fetches a site's homepage and a small set of common URLs and reports
what a reviewer would find: HTTPS, trust pages, robots.txt, sitemap,
ads.txt, viewport meta, and obvious demo content.

This is a starting point, not a verdict. It cannot judge content
quality, originality, or policy compliance. Always follow it with a
human audit using references/08-pre-apply-checklist.md.

Usage:
    python3 site_audit.py https://example.com
    python3 site_audit.py https://example.com --timeout 20

Requires only the Python standard library. Makes GET requests only.
"""

import argparse
import re
import ssl
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36 "
    "AdSenseReadinessChecker/1.0"
)

TRUST_SLUGS = {
    "about": ["/about/", "/about-us/", "/about", "/about-us"],
    "contact": ["/contact/", "/contact-us/", "/contact", "/contact-us"],
    "privacy": ["/privacy-policy/", "/privacy/", "/privacy-policy", "/privacy"],
    "terms": [
        "/terms-and-conditions/",
        "/terms-of-service/",
        "/terms/",
        "/terms-and-conditions",
        "/terms-of-service",
    ],
    "disclaimer": ["/disclaimer/", "/disclaimer"],
}

DEMO_MARKERS = [
    "hello world",
    "just another wordpress site",
    "sample page",
    "lorem ipsum",
    "coming soon",
    "under construction",
]


class _LinkTitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title_parts = []
        self.in_title = False
        self.has_viewport = False
        self.links = []
        self.text_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data.strip())
        self.text_parts.append(data)


def fetch(url, timeout):
    """GET a URL. Returns (status, final_url, body_text, error)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            raw = resp.read(2_000_000)
            body = raw.decode("utf-8", errors="replace")
            return resp.status, resp.geturl(), body, None
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl(), "", f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report any fetch failure
        return None, url, "", str(exc)


def check_path(base, paths, timeout):
    """Return the first path that returns HTTP 200, else None."""
    for path in paths:
        status, _, _, _ = fetch(urljoin(base, path), timeout)
        if status == 200:
            return path
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", help="Site URL, e.g. https://example.com")
    parser.add_argument("--timeout", type=int, default=15)
    args = parser.parse_args(argv)

    site = args.site if args.site.startswith(("http://", "https://")) else "https://" + args.site
    parsed = urlparse(site)
    base = f"{parsed.scheme}://{parsed.netloc}/"

    print(f"AdSense readiness check: {base}")
    print("Read-only check. This is not an approval verdict.\n")

    findings = []

    def report(status, message):
        mark = {"ok": "[OK]  ", "warn": "[WARN]", "fail": "[FAIL]"}[status]
        print(f"{mark} {message}")
        findings.append(status)

    # HTTPS
    if parsed.scheme == "https":
        report("ok", "Site URL uses HTTPS.")
    else:
        report("warn", "Site URL is HTTP. Check that it redirects to HTTPS.")

    # Homepage
    status, final_url, body, error = fetch(base, args.timeout)
    if status != 200:
        report("fail", f"Homepage did not return HTTP 200 ({error or status}). Fix hosting before applying.")
        print("\nResult: BLOCKER - homepage unreachable.")
        return 1
    report("ok", f"Homepage returns HTTP 200 (final URL: {final_url}).")
    if final_url.startswith("https://") and parsed.scheme == "http":
        report("ok", "HTTP redirects to HTTPS.")

    parser_html = _LinkTitleParser()
    parser_html.feed(body)
    title = " ".join(parser_html.title_parts).strip()
    text = " ".join(parser_html.text_parts)
    words = len(re.findall(r"\S+", text))

    if title:
        report("ok", f"Homepage title: {title[:100]}")
    else:
        report("warn", "Homepage has no <title> text.")
    if parser_html.has_viewport:
        report("ok", "Viewport meta tag present (mobile layout signal).")
    else:
        report("warn", "No viewport meta tag found. Check mobile layout.")
    print(f"      Homepage visible text is about {words} words (rough count).")

    lowered = text.lower()
    for marker in DEMO_MARKERS:
        if marker in lowered:
            report("warn", f"Demo/placeholder marker found on homepage: '{marker}'. Remove before applying.")

    # robots.txt
    status, _, robots, _ = fetch(urljoin(base, "/robots.txt"), args.timeout)
    if status == 200:
        if re.search(r"User-agent:\s*\*\s*\nDisallow:\s*/\s*$", robots, re.M):
            report("fail", "robots.txt disallows all crawling. Googlebot cannot review the site.")
        else:
            report("ok", "robots.txt exists and does not block all crawling.")
    else:
        report("warn", "No robots.txt found. Add one and check it does not block Googlebot.")

    # Sitemap
    sitemap = check_path(base, ["/sitemap.xml", "/sitemap_index.xml", "/sitemaps.xml", "/wp-sitemap.xml"], args.timeout)
    if sitemap:
        report("ok", f"Sitemap found at {sitemap}. Submit it in Search Console.")
    else:
        report("warn", "No common sitemap URL found. Publish a sitemap.")

    # ads.txt
    status, _, ads_txt, _ = fetch(urljoin(base, "/ads.txt"), args.timeout)
    if status == 200 and "google.com" in ads_txt and "pub-" in ads_txt:
        report("ok", "ads.txt exists and contains a Google publisher line.")
    elif status == 200:
        report("warn", "ads.txt exists but no Google publisher line was found. Add the line from AdSense.")
    else:
        report("warn", "No ads.txt found. Publish it at the site root after signup.")

    # Trust pages
    print("\nTrust pages (first matching slug that returns 200):")
    for name, slugs in TRUST_SLUGS.items():
        found = check_path(base, slugs, args.timeout)
        if found:
            report("ok", f"{name}: found at {found}")
        elif name in ("about", "contact", "privacy"):
            report("fail", f"{name}: no common page found. Publish one before applying.")
        else:
            report("warn", f"{name}: no common page found. Add one if the niche needs it.")

    fails = findings.count("fail")
    warns = findings.count("warn")
    print(f"\nSummary: {fails} blocker(s), {warns} warning(s).")
    if fails:
        print("Result: DO NOT APPLY YET - fix the blockers, then run the full checklist in references/08-pre-apply-checklist.md.")
        return 1
    print("Result: basic checks pass. Continue with the human content and policy audit before applying.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
