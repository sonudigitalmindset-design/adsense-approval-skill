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
import http.client
import re
import ssl
import sys
import time
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
        self.title_done = False
        self.has_viewport = False
        self.html_lang = ""
        self.has_favicon = False
        self.robots_meta = ""
        self.links = []
        self.text_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.html_lang = attrs.get("lang", "")
        if tag == "title" and not self.title_done:
            self.in_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "meta" and attrs.get("name", "").lower() == "robots":
            self.robots_meta = attrs.get("content", "")
        if tag == "link" and "icon" in attrs.get("rel", "").lower():
            self.has_favicon = True
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
            self.title_done = True

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data.strip())
        self.text_parts.append(data)


def fetch(url, timeout):
    """GET a URL, retrying once after a transient failure.

    Returns (status, final_url, body_text, error). A status of None
    means the fetch itself failed; an HTTP status means the server
    answered.
    """
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    ctx = ssl.create_default_context()
    last_error = ""
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                status = resp.status
                final_url = resp.geturl()
                chunks = []
                total = 0
                try:
                    while total < 2_000_000:
                        chunk = resp.read(65536)
                        if not chunk:
                            break
                        chunks.append(chunk)
                        total += len(chunk)
                except http.client.IncompleteRead as exc:
                    # Keep the partial body. Some hosts close the
                    # connection early, and the head of the page
                    # usually holds everything this check needs.
                    chunks.append(exc.partial)
                raw = b"".join(chunks)
                body = raw.decode("utf-8", errors="replace")
                return status, final_url, body, None
        except urllib.error.HTTPError as exc:
            if exc.code >= 500 and attempt == 0:
                last_error = f"HTTP {exc.code}"
                time.sleep(2)
                continue
            return exc.code, exc.geturl(), "", f"HTTP {exc.code}"
        except Exception as exc:  # noqa: BLE001 - report any fetch failure
            last_error = str(exc)
            if attempt == 0:
                time.sleep(2)
                continue
            return None, url, "", last_error
    return None, url, "", last_error


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
    if "noindex" in parser_html.robots_meta.lower():
        report("fail", "Homepage carries noindex. A noindexed homepage cannot be reviewed or ranked. Remove it before applying.")
    if parser_html.html_lang:
        report("ok", f"HTML lang attribute present (lang={parser_html.html_lang}).")
    else:
        report("warn", "No HTML lang attribute found.")
    if parser_html.has_favicon:
        report("ok", "Favicon link present.")
    else:
        report("warn", "No favicon link found.")
    print(f"      Homepage visible text is about {words} words (rough count).")

    lowered = text.lower()
    for marker in DEMO_MARKERS:
        if marker in lowered:
            report("warn", f"Demo/placeholder marker found on homepage: '{marker}'. Remove before applying.")

    # Consent platform marker on the homepage
    home_lower = body.lower()
    cmp_markers = ["complianz", "cmplz-", "cookiebot", "onetrust", "optanon",
                   "trustarc", "fundingchoices", "cookieadmin", "cookieyes",
                   "cky-", "iubenda", "termly", "osano"]
    if any(m in home_lower for m in cmp_markers):
        report("ok", "Consent platform marker found on the homepage. Verify the banner renders for a new visitor.")
    else:
        report("warn", "No consent platform marker found on the homepage. Check consent handling for EEA, UK, and Swiss visitors.")

    # HTTP to HTTPS redirect (when the input URL is HTTPS)
    if parsed.scheme == "https":
        status, final_url, _, error = fetch(f"http://{parsed.netloc}/", args.timeout)
        if status == 200 and final_url.startswith("https://"):
            report("ok", "HTTP version redirects to HTTPS.")
        elif status == 200:
            report("warn", "HTTP version serves content without redirecting to HTTPS.")
        else:
            report("warn", f"Could not verify the HTTP to HTTPS redirect ({error or status}).")

    # 404 behaviour
    status, _, _, _ = fetch(urljoin(base, "/this-page-does-not-exist-adsense-audit-12345/"), args.timeout)
    if status == 404:
        report("ok", "A nonsense URL returns HTTP 404 (no soft 404).")
    elif status == 200:
        report("warn", "A nonsense URL returns HTTP 200 (soft 404). Missing pages should return 404.")
    else:
        report("warn", f"Could not verify 404 behaviour ({status}).")

    # robots.txt
    status, _, robots, error = fetch(urljoin(base, "/robots.txt"), args.timeout)
    if status == 200:
        if re.search(r"User-agent:\s*\*\s*\nDisallow:\s*/\s*$", robots, re.M):
            report("fail", "robots.txt disallows all crawling. Googlebot cannot review the site.")
        else:
            report("ok", "robots.txt exists and does not block all crawling.")
        if re.search(r"user-agent:\s*mediapartners-google\s*\n(?:.*\n)?\s*disallow:\s*/\s*$", robots, re.I | re.M):
            report("fail", "robots.txt blocks the AdSense crawler (Mediapartners-Google).")
        if "sitemap:" in robots.lower():
            report("ok", "robots.txt names a sitemap.")
        else:
            report("warn", "robots.txt does not name a sitemap. Add a Sitemap line.")
    elif status == 404:
        report("warn", "No robots.txt found (HTTP 404). Add one and check it does not block Googlebot.")
    else:
        report("warn", f"Could not verify robots.txt ({error or status}). Open it in a browser to check.")

    # Sitemap
    sitemap = check_path(base, ["/sitemap.xml", "/sitemap_index.xml", "/sitemaps.xml", "/wp-sitemap.xml"], args.timeout)
    if sitemap:
        report("ok", f"Sitemap found at {sitemap}. Submit it in Search Console.")
    else:
        report("warn", "No common sitemap URL found. Publish a sitemap.")

    # ads.txt
    status, _, ads_txt, error = fetch(urljoin(base, "/ads.txt"), args.timeout)
    if status == 200 and "google.com" in ads_txt and "pub-" in ads_txt:
        google_lines = []
        malformed = False
        for line in ads_txt.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            parts = [p.strip() for p in stripped.split(",")]
            if parts and parts[0].lower() == "google.com":
                google_lines.append(parts)
                if len(parts) < 3 or not re.fullmatch(r"pub-\d{16}", parts[1] or ""):
                    malformed = True
        if google_lines and not malformed:
            first = google_lines[0]
            if first[2].upper() == "DIRECT" and len(first) > 3 and first[3] == "f08c47fec0942fa0":
                report("ok", "ads.txt Google line is well formed: DIRECT with the certification ID.")
            else:
                report("warn", "ads.txt Google line found but the relationship or certification ID looks off. Copy the line from the account.")
        else:
            report("warn", "ads.txt Google line is malformed. Copy the line from the account.")
    elif status == 200:
        report("warn", "ads.txt exists but no Google publisher line was found. Add the line from AdSense.")
    elif status == 404:
        report("warn", "No ads.txt found (HTTP 404). Publish it at the site root after signup.")
    else:
        report("warn", f"Could not verify ads.txt ({error or status}). Open it in a browser to check.")

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
