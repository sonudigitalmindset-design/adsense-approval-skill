#!/usr/bin/env python3
"""Deep approval-clone audit v2: crawl a site and check every small,
machine-checkable point a reviewer would notice.

This replicates the CHECKABLE surface of an AdSense site review. It
cannot clone Google's internal decision, judge originality, or rule
on policy compliance. Every finding here still needs a human look.
No script can match Google's decision 100 percent, because the
decision includes human judgement, account history, and traffic
quality signals that no crawler can see. This script covers the
checkable surface as fully as possible and says plainly what it
cannot judge.

Read-only. Python standard library only. Be polite: page fetches
and link checks run in parallel with a small delay per worker,
and caps limit pages, links, and images.

Usage:
    python3 scripts/deep_audit.py https://example.com
    python3 scripts/deep_audit.py https://example.com --max-pages 100 --output report.md --json report.json
"""

import argparse
import datetime
import hashlib
import http.client
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36 "
    "AdSenseDeepAudit/2.0"
)

TRUST_SLUGS = {
    "about": ["/about/", "/about-us/", "/about"],
    "contact": ["/contact/", "/contact-us/", "/contact"],
    "privacy": ["/privacy-policy/", "/privacy/", "/privacy-policy"],
    "terms": ["/terms-and-conditions/", "/terms/", "/terms-of-service/"],
    "disclaimer": ["/disclaimer/", "/disclaimer"],
}

SITEMAP_CANDIDATES = [
    "/sitemaps.xml",
    "/sitemap.xml",
    "/sitemap_index.xml",
    "/wp-sitemap.xml",
]

PLACEHOLDER_STRINGS = [
    "lorem ipsum",
    "hello world",
    "sample page",
    "just another wordpress",
    "under construction",
    "coming soon",
    "default post",
]

# Heuristic only. A match means a human must read the page, never an
# automatic verdict. Keep this list short and obvious. Matching uses
# word boundaries so "specialist" never trips the "cialis" entry.
REVIEW_PHRASES = [
    "viagra",
    "cialis",
    "online casino",
    "earn money by clicking",
    "click to earn",
    "make money fast",
    "free download crack",
    "buy followers",
    "buy traffic",
    "paid to click",
]

REVIEW_PATTERNS = [
    (phrase, re.compile(r"\b" + re.escape(phrase) + r"\b"))
    for phrase in REVIEW_PHRASES
]

# Copyright-risk signals. A match is a read-the-page flag only.
# Legitimate discussion of these topics is not a violation.
COPYRIGHT_SIGNALS = [
    "watch online free",
    "free movie download",
    "download full movie",
    "cracked apk",
    "free pdf download",
]

COPYRIGHT_PATTERNS = [
    (phrase, re.compile(r"\b" + re.escape(phrase) + r"\b"))
    for phrase in COPYRIGHT_SIGNALS
]

SKIP_LINK_SUFFIXES = (
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico",
    ".css", ".js", ".pdf", ".zip", ".mp3", ".mp4", ".xml",
)

CMP_MARKERS = {
    "Complianz": ["complianz", "cmplz-"],
    "Cookiebot": ["cookiebot"],
    "OneTrust": ["onetrust", "optanon"],
    "TrustArc": ["trustarc"],
    "Funding Choices": ["fundingchoices", "funding-choices"],
    "CookieAdmin": ["cookieadmin"],
    "CookieYes": ["cookieyes", "cky-"],
    "Iubenda": ["iubenda"],
    "Termly": ["termly"],
    "Osano": ["osano"],
}

AD_NETWORK_MARKERS = {
    "AdSense": ["adsbygoogle", "ca-pub-", "pagead2.googlesyndication.com"],
    "Google Ad Manager": ["doubleclick.net", "googletagservices.com"],
    "Amazon": ["amazon-adsystem.com"],
    "Media.net": ["media.net"],
    "Ezoic": ["ezoic"],
    "Mediavine": ["mediavine"],
    "AdThrive": ["adthrive"],
    "Monumetric": ["monumetric"],
    "Taboola": ["taboola"],
    "Outbrain": ["outbrain"],
    "PropellerAds": ["propellerads"],
}

POPUP_KEYWORDS = (
    "popup", "modal", "interstitial", "exit-intent", "exitintent",
    "newsletter-popup", "leadbox", "optin-modal",
)

SITEMAP_LASTMODS = []
SITEMAP_ERRORS = []

RESULTS = {"fail": 0, "warn": 0, "ok": 0}
CHECKS = []

LINES = []
_REAL_PRINT = print


def emit(text=""):
    LINES.append(str(text))
    _REAL_PRINT(text)


def report(level, message):
    RESULTS[level] += 1
    CHECKS.append({"level": level, "message": message})
    label = {"ok": "[OK]  ", "warn": "[WARN]", "fail": "[FAIL]"}[level]
    emit(f"{label} {message}")


def info(message):
    emit(f"      {message}")


def fetch(url, timeout):
    """GET a URL, retrying once after a transient failure.

    Returns (status, final_url, body_text, error, headers, elapsed).
    Chunked reads keep the partial body when a host closes early.
    """
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    ctx = ssl.create_default_context()
    last_error = ""
    for attempt in range(2):
        started = time.time()
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                status = resp.status
                final_url = resp.geturl()
                headers = {k.lower(): v for k, v in resp.headers.items()}
                chunks = []
                total = 0
                saw_incomplete = False
                try:
                    while total < 3_000_000:
                        chunk = resp.read(65536)
                        if not chunk:
                            break
                        chunks.append(chunk)
                        total += len(chunk)
                except http.client.IncompleteRead as exc:
                    chunks.append(exc.partial)
                    total += len(exc.partial)
                    saw_incomplete = True
                try:
                    expected = int(headers.get("content-length", "0"))
                except ValueError:
                    expected = 0
                if (saw_incomplete or (expected > 0 and total < expected)) and attempt == 0:
                    # Truncated body: retry for the full response
                    # instead of analysing a partial page. The
                    # IncompleteRead flag matters for chunked
                    # responses, which carry no Content-Length.
                    last_error = f"incomplete read ({total} of {expected} bytes)"
                    time.sleep(2)
                    continue
                raw = b"".join(chunks)
                body = raw.decode("utf-8", errors="replace")
                return status, final_url, body, None, headers, time.time() - started
        except urllib.error.HTTPError as exc:
            elapsed = time.time() - started
            headers = {k.lower(): v for k, v in exc.headers.items()} if exc.headers else {}
            if exc.code >= 500 and attempt == 0:
                last_error = f"HTTP {exc.code}"
                time.sleep(2)
                continue
            return exc.code, exc.geturl(), "", f"HTTP {exc.code}", headers, elapsed
        except Exception as exc:  # noqa: BLE001 - report any fetch failure
            last_error = str(exc)
            if attempt == 0:
                time.sleep(2)
                continue
            return None, url, "", last_error, {}, time.time() - started
    return None, url, "", last_error, {}, 0.0


def head_or_get(url, timeout):
    """Lightweight check for a link or image.

    Returns (status, error, size_bytes). HEAD first, GET fallback
    on 405/501. A status of None means the check itself failed.
    size_bytes comes from the Content-Length header when the
    server sends one, else 0.
    """
    ctx = ssl.create_default_context()
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT}, method=method
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                try:
                    size = int(resp.headers.get("content-length", "0"))
                except ValueError:
                    size = 0
                if method == "GET":
                    resp.read(65536)
                return resp.status, None, size
        except urllib.error.HTTPError as exc:
            if exc.code in (405, 501) and method == "HEAD":
                continue
            return exc.code, f"HTTP {exc.code}", 0
        except Exception as exc:  # noqa: BLE001 - report any failure
            return None, str(exc), 0
    return None, "unreachable", 0


def _fetch_named(job):
    """Fetch one labelled URL. Runs inside the worker pool."""
    label, url, timeout, delay = job
    time.sleep(delay)
    return label, fetch(url, timeout)


def _probe_trust(job):
    """Probe one trust-page slug. Runs inside the worker pool."""
    name, slug, base, timeout, delay = job
    time.sleep(delay)
    status, _, _, _, _, _ = fetch(urljoin(base, slug), timeout)
    return name, slug, status


def _fetch_page(job):
    """Fetch one sitemap page. Runs inside the worker pool."""
    page_url, timeout, delay = job
    time.sleep(delay)
    status, final_url, body, error, _, _ = fetch(page_url, timeout)
    return status, final_url, body, error


def _fetch_status(job):
    """Fetch one link for verification. Runs inside the worker pool."""
    url, timeout, delay = job
    time.sleep(delay)
    status, _, _, error, _, _ = fetch(url, timeout)
    return url, status, error


def _probe_url(job):
    """HEAD/GET probe for one link or image. Runs inside the worker pool."""
    url, timeout, delay = job
    time.sleep(delay)
    status, error, size = head_or_get(url, timeout)
    return url, status, error, size


class _PageParser(HTMLParser):
    """Collect the small points from one HTML page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts = []
        self.in_title = False
        self.title_done = False
        self.metas = {}
        self.h1_texts = []
        self.in_h1 = False
        self.h1_parts = []
        self.h2_count = 0
        self.images = []
        self.links = []
        self.canonical = None
        self.ld_json_count = 0
        self.ld_types = []
        self.in_ld_json = False
        self.ld_buffer = []
        self.skip_depth = 0
        self.content_depth = 0
        self.text_parts = []
        self.article_parts = []
        self.author_signal = False
        self.date_signal = False
        self.html_lang = ""
        self.has_charset = False
        self.has_favicon = False
        self.ad_slots = 0
        self.ad_script = False
        self.popup_markers = 0
        self.has_nav = False
        self.has_footer = False
        self.has_form = False
        self.has_search = False
        self.sponsored_count = 0
        self.mailto_count = 0
        self.comment_markers = 0
        self.related_markers = 0
        self.nofollow_count = 0
        self.updated_signal = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.html_lang = attrs.get("lang", "")
        if tag == "meta" and "charset" in attrs:
            self.has_charset = True
        if tag in ("script", "style"):
            self.skip_depth += 1
            if attrs.get("type") == "application/ld+json":
                self.ld_json_count += 1
                self.in_ld_json = True
                self.ld_buffer = []
            src = attrs.get("src", "")
            if "pagead2.googlesyndication.com" in src or "adsbygoogle" in src:
                self.ad_script = True
        if tag in ("article", "main"):
            self.content_depth += 1
        if tag == "title" and not self.title_done:
            self.in_title = True
        if tag == "meta":
            key = (attrs.get("name") or attrs.get("property") or "").lower()
            if key and key not in self.metas:
                self.metas[key] = attrs.get("content", "")
        if tag == "h1":
            self.in_h1 = True
            self.h1_parts = []
        if tag == "h2":
            self.h2_count += 1
        if tag == "img":
            self.images.append(
                (attrs.get("src", ""), attrs.get("alt"),
                 bool(attrs.get("width") and attrs.get("height")))
            )
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
            rel = attrs.get("rel", "").lower()
            if "sponsored" in rel:
                self.sponsored_count += 1
            if "nofollow" in rel:
                self.nofollow_count += 1
            if attrs["href"].lower().startswith("mailto:"):
                self.mailto_count += 1
        if tag == "nav":
            self.has_nav = True
        if tag == "footer":
            self.has_footer = True
        if tag == "form":
            self.has_form = True
            form_marks = (attrs.get("class", "") + " " + attrs.get("id", "")
                          + " " + attrs.get("role", "")).lower()
            if "search" in form_marks:
                self.has_search = True
        if tag == "input" and attrs.get("type", "").lower() == "search":
            self.has_search = True
        if tag == "link":
            rel = attrs.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = attrs.get("href")
            if "icon" in rel:
                self.has_favicon = True
        if tag == "ins" and "adsbygoogle" in attrs.get("class", "").lower():
            self.ad_slots += 1
        if tag == "time":
            self.date_signal = True
        cls = (attrs.get("class", "") + " " + attrs.get("id", "")).lower()
        if "author" in cls or "byline" in cls:
            self.author_signal = True
        if attrs.get("rel") == "author":
            self.author_signal = True
        if "comment-form" in cls or "respond" in cls:
            self.comment_markers += 1
        if "related" in cls:
            self.related_markers += 1
        if "updated" in cls or "modified" in cls:
            self.updated_signal = True
        if any(k in cls for k in POPUP_KEYWORDS):
            self.popup_markers += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip_depth = max(0, self.skip_depth - 1)
            if self.in_ld_json and tag == "script":
                self.in_ld_json = False
                joined = " ".join(self.ld_buffer)
                for match in re.findall(r'"@type"\s*:\s*"([^"]+)"', joined):
                    self.ld_types.append(match)
        if tag in ("article", "main"):
            self.content_depth = max(0, self.content_depth - 1)
        if tag == "title":
            self.in_title = False
            self.title_done = True
        if tag == "h1":
            self.in_h1 = False
            self.h1_texts.append(" ".join(self.h1_parts).strip())

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data.strip())
        if self.in_h1:
            self.h1_parts.append(data.strip())
        if self.in_ld_json:
            self.ld_buffer.append(data)
        if self.skip_depth == 0:
            self.text_parts.append(data)
            if self.content_depth > 0:
                self.article_parts.append(data)


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def collect_sitemap_urls(sitemap_url, timeout, seen, depth=0):
    """Return page URLs from a sitemap or sitemap index."""
    if depth > 2 or sitemap_url in seen:
        return []
    seen.add(sitemap_url)
    root = None
    for _ in range(3):
        status, _, body, _, _, _ = fetch(sitemap_url, timeout)
        if status != 200 or not body:
            time.sleep(1)
            continue
        try:
            root = ET.fromstring(body)
            break
        except ET.ParseError:
            # Truncated sitemap body: refetch instead of
            # silently dropping every URL in the file.
            time.sleep(1)
            continue
    if root is None:
        # Never silently drop a sitemap file: the caller
        # reports this so an incomplete crawl is visible.
        SITEMAP_ERRORS.append(sitemap_url)
        return []
    urls = []
    kind = local_name(root.tag)
    if kind == "sitemapindex":
        for child in root:
            loc = None
            for part in child:
                if local_name(part.tag) == "loc":
                    loc = (part.text or "").strip()
            if loc:
                urls.extend(collect_sitemap_urls(loc, timeout, seen, depth + 1))
    elif kind == "urlset":
        for child in root:
            for part in child:
                if local_name(part.tag) == "loc" and part.text:
                    urls.append(part.text.strip())
                if local_name(part.tag) == "lastmod" and part.text:
                    SITEMAP_LASTMODS.append(part.text.strip())
    return urls


def same_origin(url, base_netloc):
    try:
        return urlparse(url).netloc.lower() == base_netloc
    except ValueError:
        return False


def clean_link(href, page_url):
    if not href:
        return None
    href = href.strip()
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    absolute = urljoin(page_url, href)
    parsed = urlparse(absolute)
    if parsed.scheme not in ("http", "https"):
        return None
    return absolute.split("#")[0]


def shingle_set(text, size=8, cap=400):
    words = re.findall(r"[a-z0-9]+", text.lower())
    if len(words) < size:
        return set()
    hashes = set()
    for i in range(len(words) - size + 1):
        chunk = " ".join(words[i:i + size])
        hashes.add(int(hashlib.md5(chunk.encode()).hexdigest()[:8], 16))
    if len(hashes) > cap:
        ordered = sorted(hashes)
        step = len(ordered) / cap
        hashes = {ordered[int(i * step)] for i in range(cap)}
    return hashes


def jaccard(left, right):
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("url", help="Site URL, for example https://example.com")
    parser.add_argument("--timeout", type=int, default=20, help="Seconds per request")
    parser.add_argument("--max-pages", type=int, default=200, help="Max pages to crawl")
    parser.add_argument("--max-links", type=int, default=250, help="Max internal links to verify")
    parser.add_argument("--max-external", type=int, default=80, help="Max external links to verify")
    parser.add_argument("--max-images", type=int, default=100, help="Max images to verify")
    parser.add_argument("--delay", type=float, default=0.25, help="Seconds of delay per worker before each request")
    parser.add_argument("--workers", type=int, default=8, help="Parallel requests (default 8). Use 1 or 2 for fragile shared hosting")
    parser.add_argument("--output", help="Write the same report to a Markdown file")
    parser.add_argument("--json", help="Write a machine-readable JSON report")
    args = parser.parse_args()
    args.workers = max(1, args.workers)

    base = args.url if args.url.endswith("/") else args.url + "/"
    parsed_base = urlparse(base)
    netloc = parsed_base.netloc.lower()

    global print  # noqa: A001 - capture all output for --output
    print = emit

    print(f"Deep approval-clone audit v2: {base}")
    print("Read-only. This replicates checkable review points only.")
    print("It cannot judge originality, value, or policy compliance.")
    print("No script can match Google's decision 100 percent.")
    print()

    # ---- Site-level checks ----
    if parsed_base.scheme == "https":
        report("ok", "Site URL uses HTTPS.")
    else:
        report("fail", "Site URL is not HTTPS. Move the whole site to HTTPS.")

    status, final_url, home_body, error, home_headers, elapsed = fetch(base, args.timeout)
    if status != 200:
        report("fail", f"Homepage did not return HTTP 200 ({error or status}). Fix hosting first.")
        print()
        print("Result: BLOCKER - homepage unreachable.")
        return 1
    report("ok", f"Homepage returns HTTP 200 (final URL: {final_url}).")
    info(f"Homepage fetch took {elapsed:.1f}s, body {len(home_body)} chars.")
    if elapsed > 3.0:
        report("warn", "Homepage response is slow (over 3s). Speed is a user experience signal, not a Google rule.")
    if "strict-transport-security" in home_headers:
        report("ok", "HSTS header present on the homepage response.")
    else:
        info("No HSTS header on the homepage response (optional hardening).")
    if "x-content-type-options" in home_headers:
        info("X-Content-Type-Options header present.")
    else:
        info("No X-Content-Type-Options header (optional hardening).")

    # Fetch the independent site-level URLs in parallel, then
    # report them in order below so the output stays stable.
    if netloc.startswith("www."):
        alt_host = netloc[4:]
    else:
        alt_host = "www." + netloc
    alt_url = f"{parsed_base.scheme}://{alt_host}/"
    nonsense = urljoin(base, "/this-page-does-not-exist-adsense-audit-12345/")
    site_jobs = [
        ("robots", urljoin(base, "/robots.txt")),
        ("ads", urljoin(base, "/ads.txt")),
        ("nonsense", nonsense),
        ("feed", urljoin(base, "/feed/")),
        ("page2", urljoin(base, "/page/2/")),
        ("alt", alt_url),
    ]
    if parsed_base.scheme == "https":
        site_jobs.append(("http", "http://" + parsed_base.netloc + "/"))
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        site_results = dict(executor.map(
            _fetch_named,
            [(label, url, args.timeout, args.delay) for label, url in site_jobs],
        ))

    # HTTP to HTTPS redirect
    if parsed_base.scheme == "https":
        http_url = "http://" + parsed_base.netloc + "/"
        status, final_url, _, error, _, _ = site_results["http"]
        if status == 200 and final_url.startswith("https://"):
            report("ok", "HTTP version redirects to HTTPS.")
        elif status == 200:
            report("warn", "HTTP version serves content without redirecting to HTTPS.")
        else:
            info(f"HTTP version check: {error or status} (redirect behaviour unclear).")

    # www consistency
    status, final_url, _, _, _, _ = site_results["alt"]
    if status == 200 and urlparse(final_url).netloc.lower() == netloc:
        report("ok", f"Alternate host {alt_host} redirects to the canonical host.")
    elif status == 200:
        report("warn", f"Alternate host {alt_host} serves content instead of redirecting. Pick one canonical host.")
    else:
        info(f"Alternate host {alt_host} did not return 200 ({status}). Check the redirect in a browser.")

    # robots.txt, deep
    status, _, robots, _, _, _ = site_results["robots"]
    if status == 200:
        if re.search(r"User-agent:\s*\*\s*\nDisallow:\s*/\s*$", robots, re.M):
            report("fail", "robots.txt disallows all crawling.")
        else:
            report("ok", "robots.txt exists and does not block all crawling.")
        lowered_robots = robots.lower()
        if "mediapartners-google" in lowered_robots:
            blocked = bool(re.search(
                r"user-agent:\s*mediapartners-google\s*\n(?:.*\n)?\s*disallow:\s*/\s*$",
                robots, re.I | re.M))
            if blocked:
                report("fail", "robots.txt blocks the AdSense crawler (Mediapartners-Google).")
            else:
                info("robots.txt names Mediapartners-Google without a root block.")
        if "sitemap:" in lowered_robots:
            report("ok", "robots.txt names a sitemap.")
        else:
            report("warn", "robots.txt does not name a sitemap. Add a Sitemap line.")
    elif status == 404:
        report("warn", "No robots.txt found (HTTP 404).")
    else:
        report("warn", f"Could not verify robots.txt ({status}). Check it in a browser.")

    # ads.txt, deep validation
    status, _, ads_txt, _, _, _ = site_results["ads"]
    if status == 200:
        google_lines = []
        malformed = []
        reseller = 0
        for line in ads_txt.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            parts = [p.strip() for p in stripped.split(",")]
            if len(parts) >= 3 and parts[2].upper() == "RESELLER":
                reseller += 1
            if parts and parts[0].lower() == "google.com":
                google_lines.append(parts)
                if len(parts) < 3 or not re.fullmatch(r"pub-\d{16}", parts[1] or ""):
                    malformed.append(stripped)
        if google_lines and not malformed:
            ids = {p[1] for p in google_lines}
            if len(ids) > 1:
                report("warn", f"ads.txt has Google lines with {len(ids)} different publisher IDs. Keep only the account's own line.")
            elif google_lines[0][2].upper() == "DIRECT" and len(google_lines[0]) > 3 and google_lines[0][3] == "f08c47fec0942fa0":
                report("ok", "ads.txt Google line is well formed: DIRECT with the certification ID.")
            else:
                report("warn", "ads.txt Google line found but the relationship or certification ID looks off. Copy the line from the account.")
        elif google_lines:
            report("warn", f"ads.txt has {len(malformed)} malformed Google line(s). Copy the line from the account.")
        else:
            report("warn", "ads.txt exists but no Google publisher line was found.")
        if reseller:
            info(f"ads.txt has {reseller} RESELLER line(s). Each reseller is another party in the chain. Keep only resellers actually used.")
    elif status == 404:
        report("warn", "No ads.txt found (HTTP 404). Publish it after signup.")
    else:
        report("warn", f"Could not verify ads.txt ({status}). Check it in a browser.")

    # 404 behaviour, feed, pagination
    status, _, _, _, _, _ = site_results["nonsense"]
    if status == 404:
        report("ok", "A nonsense URL returns HTTP 404 (no soft 404).")
    elif status == 200:
        report("warn", "A nonsense URL returns HTTP 200 (soft 404). Missing pages should return 404.")
    else:
        info(f"Nonsense URL check returned {status}.")

    status, _, feed_body, _, _, _ = site_results["feed"]
    if status == 200 and ("<rss" in feed_body[:2000] or "<?xml" in feed_body[:2000]):
        info("RSS feed found at /feed/.")
    else:
        info("No RSS feed found at /feed/ (optional).")

    status, _, _, _, _, _ = site_results["page2"]
    if status == 200:
        info("Archive pagination /page/2/ returns 200.")
    elif status == 404:
        info("No /page/2/ archive page (fine for a small site).")
    else:
        info(f"/page/2/ check returned {status}.")

    # ---- Trust pages ----
    print()
    print("Trust pages:")
    trust_found = {}
    trust_jobs = [(name, slug) for name, slugs in TRUST_SLUGS.items() for slug in slugs]
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        trust_status = {}
        for name, slug, probed in executor.map(
            _probe_trust,
            [(name, slug, base, args.timeout, args.delay) for name, slug in trust_jobs],
        ):
            trust_status[(name, slug)] = probed
    for name, slugs in TRUST_SLUGS.items():
        found = next((slug for slug in slugs if trust_status.get((name, slug)) == 200), None)
        trust_found[name] = found
        if found:
            report("ok", f"{name}: found at {found}")
        elif name in ("about", "contact", "privacy"):
            report("fail", f"{name}: no common page found. Publish one before applying.")
        else:
            report("warn", f"{name}: no common page found. Add one if the niche needs it.")

    # Fetch the found trust-page bodies in parallel, then run
    # the disclosure and depth checks in order below.
    body_jobs = [(name, urljoin(base, trust_found[name]))
                 for name in ("privacy", "about", "contact") if trust_found[name]]
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        trust_bodies = dict(executor.map(
            _fetch_named,
            [(name, url, args.timeout, args.delay) for name, url in body_jobs],
        ))

    # Privacy disclosure keywords
    if trust_found["privacy"]:
        status, _, privacy_body, _, _, _ = trust_bodies["privacy"]
        if status == 200:
            lowered = privacy_body.lower()
            print("Privacy disclosure check:")
            for label, words in [
                ("cookies", ["cookie"]),
                ("Google", ["google"]),
                ("advertising", ["advertis"]),
                ("third parties", ["third part", "third-part"]),
                ("opt-out or Ads Settings", ["opt out", "opt-out", "ads settings"]),
            ]:
                if any(w in lowered for w in words):
                    report("ok", f"Privacy page mentions {label}.")
                else:
                    report("warn", f"Privacy page does not mention {label}. Check the wording.")

    # About depth and contact form: trust signals a reviewer reads.
    if trust_found["about"]:
        status, _, about_body, _, _, _ = trust_bodies["about"]
        if status == 200:
            about_words = len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", about_body)))
            if about_words < 100:
                report("warn", f"About page is very short (about {about_words} words of page text). A reviewer looks for a real story here.")
            else:
                info(f"About page has about {about_words} words of page text.")
    if trust_found["contact"]:
        status, _, contact_body, _, _, _ = trust_bodies["contact"]
        if status == 200:
            if "<form" in contact_body.lower():
                info("Contact page contains a form.")
            else:
                info("Contact page has no form. Email or social links can serve instead. Verify a visitor can reach the owner.")

    # CMP and ad network markers on the homepage
    print()
    print("Consent and ad code signals (homepage HTML):")
    home_lower = home_body.lower()
    found_cmps = [name for name, markers in CMP_MARKERS.items()
                  if any(m in home_lower for m in markers)]
    if found_cmps:
        report("ok", f"Consent platform marker(s) found: {', '.join(found_cmps)}. Verify the banner renders for a new visitor.")
    else:
        report("warn", "No consent platform marker found on the homepage. Consent handling may be missing; verify for EEA, UK, and Swiss visitors.")
    found_networks = [name for name, markers in AD_NETWORK_MARKERS.items()
                      if any(m in home_lower for m in markers)]
    if found_networks:
        info(f"Ad code marker(s) found: {', '.join(found_networks)}.")
    else:
        info("No ad code marker found on the homepage (expected before approval).")


    # ---- Crawl the sitemap ----
    print()
    sitemap_urls = []
    sitemap_used = None
    seen = set()
    for candidate in SITEMAP_CANDIDATES:
        candidate_url = urljoin(base, candidate)
        found = collect_sitemap_urls(candidate_url, args.timeout, seen)
        if found:
            sitemap_used = candidate
            sitemap_urls = found
            break
        time.sleep(args.delay)
    if sitemap_used:
        report("ok", f"Sitemap found at {sitemap_used} with {len(sitemap_urls)} URLs.")
    else:
        report("warn", "No common sitemap URL returned URLs. Only the homepage will be checked.")
        sitemap_urls = [base]
    if SITEMAP_ERRORS:
        report("warn", f"{len(SITEMAP_ERRORS)} sitemap files could not be read after retries, so pages may be missing from this crawl. Re-run the audit: {' '.join(SITEMAP_ERRORS)}")

    if SITEMAP_LASTMODS:
        parsed_dates = []
        for raw in SITEMAP_LASTMODS:
            try:
                parsed_dates.append(datetime.datetime.fromisoformat(raw.replace("Z", "+00:00")))
            except ValueError:
                pass
        if parsed_dates:
            newest = max(parsed_dates)
            age_days = (datetime.datetime.now(datetime.timezone.utc) - newest).days
            info(f"Sitemap newest lastmod: {newest.date()} ({age_days} days ago).")
            if age_days > 90:
                report("warn", "Sitemap newest lastmod is over 90 days old. Check that new pages are added to the sitemap.")
            oldest = min(parsed_dates)
            info(f"Sitemap oldest lastmod: {oldest.date()}.")
            span_days = (newest - oldest).days
            info(f"Sitemap content spans {span_days} days from oldest to newest lastmod.")
            if 30 < age_days <= 90:
                info("No sitemap update in over 30 days. Regular posting is a trust signal, not a Google rule.")

    # Keep same-origin HTML-ish URLs, dedupe, cap.
    pages = []
    seen_pages = set()
    excluded = 0
    for raw in sitemap_urls:
        clean = raw.split("#")[0]
        if clean in seen_pages or not same_origin(clean, netloc):
            excluded += 1
            continue
        if clean.lower().endswith(SKIP_LINK_SUFFIXES):
            excluded += 1
            continue
        if "/feed" in clean.lower() or "wp-admin" in clean.lower():
            excluded += 1
            continue
        seen_pages.add(clean)
        pages.append(clean)
        if len(pages) >= args.max_pages:
            break
    if base.rstrip("/") + "/" not in seen_pages and base not in seen_pages:
        pages.insert(0, base)
    print(f"Crawling {len(pages)} pages with {args.workers} parallel workers (cap {args.max_pages}, {excluded} sitemap URLs excluded as non-HTML or off-site).")

    trust_paths = {urlparse(urljoin(base, slug)).path for slug in trust_found.values() if slug}

    # ---- Per-page checks ----
    print()
    print("Per-page points (status, words, article words, H1, images missing alt, flags):")
    page_records = []
    internal_links = set()
    external_links = set()
    image_urls = set()
    outlink_map = {}
    # Fetch all pages in parallel, then analyse them in sitemap
    # order so the report reads the same as a sequential run.
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        fetched = list(executor.map(
            _fetch_page,
            [(page_url, args.timeout, args.delay) for page_url in pages],
        ))
    for page_url, (status, final_url, body, error) in zip(pages, fetched):
        record = {"url": page_url, "status": status, "final": final_url, "flags": []}
        if status != 200 or not body:
            record["flags"].append(f"HTTP {error or status}")
            page_records.append(record)
            print(f"[FAIL] {page_url} -> {error or status}")
            continue
        if final_url.rstrip("/") != page_url.rstrip("/"):
            record["flags"].append(f"redirects to {final_url}")
        parser_html = _PageParser()
        try:
            parser_html.feed(body)
        except Exception:  # noqa: BLE001 - malformed HTML must not stop the crawl
            pass
        title = " ".join(parser_html.title_parts).strip()
        record["title"] = title
        record["description"] = parser_html.metas.get("description", "")
        record["h1"] = len(parser_html.h1_texts)
        record["h1_texts"] = parser_html.h1_texts
        record["h2"] = parser_html.h2_count
        text = " ".join(parser_html.text_parts)
        article_text = " ".join(parser_html.article_parts)
        record["words"] = len(re.findall(r"\S+", text))
        record["article_words"] = len(re.findall(r"\S+", article_text))
        record["article_text"] = article_text
        record["lowered"] = text.lower()
        record["images"] = len(parser_html.images)
        record["images_no_alt"] = sum(1 for _, alt, _ in parser_html.images if alt is None or alt.strip() == "")
        record["images_no_dims"] = sum(1 for _, _, dims in parser_html.images if not dims)
        record["canonical"] = parser_html.canonical
        record["robots_meta"] = parser_html.metas.get("robots", "")
        record["viewport"] = "viewport" in parser_html.metas
        record["og_title"] = parser_html.metas.get("og:title", "")
        record["og_description"] = parser_html.metas.get("og:description", "")
        record["og_image"] = parser_html.metas.get("og:image", "")
        record["twitter_card"] = parser_html.metas.get("twitter:card", "")
        record["ld_json"] = parser_html.ld_json_count
        record["ld_types"] = parser_html.ld_types
        record["author"] = parser_html.author_signal
        record["date"] = parser_html.date_signal
        record["html_lang"] = parser_html.html_lang
        record["charset"] = parser_html.has_charset
        record["favicon"] = parser_html.has_favicon
        record["ad_slots"] = parser_html.ad_slots
        record["ad_script"] = parser_html.ad_script
        record["popup_markers"] = parser_html.popup_markers
        record["has_nav"] = parser_html.has_nav
        record["has_footer"] = parser_html.has_footer
        record["has_form"] = parser_html.has_form
        record["has_search"] = parser_html.has_search
        record["sponsored"] = parser_html.sponsored_count
        record["mailto"] = parser_html.mailto_count
        record["comment_markers"] = parser_html.comment_markers
        record["related_markers"] = parser_html.related_markers
        record["nofollow"] = parser_html.nofollow_count
        record["updated_signal"] = parser_html.updated_signal
        record["site_verification"] = "google-site-verification" in parser_html.metas
        record["mixed"] = len(re.findall(r'''(?:src|href)="http://''', body))
        record["trust_links"] = 0
        outlink_map[page_url] = set()
        for href in parser_html.links:
            clean = clean_link(href, page_url)
            if not clean:
                continue
            if urlparse(clean).path in trust_paths:
                record["trust_links"] += 1
            if same_origin(clean, netloc):
                if clean.lower().endswith(SKIP_LINK_SUFFIXES):
                    continue
                if "/feed" in clean.lower() or "wp-admin" in clean.lower():
                    continue
                internal_links.add(clean)
                if clean.rstrip("/") != page_url.rstrip("/"):
                    outlink_map[page_url].add(clean)
            else:
                external_links.add(clean)
        for src, _, _ in parser_html.images:
            clean = clean_link(src, page_url)
            if clean and same_origin(clean, netloc):
                image_urls.add(clean)
        flags = record["flags"]
        if not title:
            flags.append("no title")
        elif len(title) < 10:
            flags.append("title too short")
        elif len(title) > 70:
            flags.append("title long")
        title_words = re.findall(r"[a-z0-9]+", title.lower())
        stopwords = {"the", "a", "an", "and", "or", "of", "to", "in",
                     "on", "for", "with", "my", "i", "how", "vs", "is"}
        title_counts = Counter(w for w in title_words if w not in stopwords)
        if title_counts and title_counts.most_common(1)[0][1] >= 4:
            flags.append("title repeats a word 4+ times (read for stuffing)")
        if not record["description"]:
            flags.append("no meta description")
        elif len(record["description"]) < 50:
            flags.append("description short")
        elif len(record["description"]) > 160:
            flags.append("description long")
        if title and record["description"] and title.lower() == record["description"].lower():
            flags.append("description identical to title")
        if record["h1"] == 0:
            flags.append("no H1")
        elif record["h1"] > 1:
            flags.append(f"{record['h1']} H1s")
        if any(not h for h in parser_html.h1_texts):
            flags.append("empty H1")
        if record["words"] < 200:
            flags.append(f"thin ({record['words']} words)")
        if record["images_no_alt"]:
            flags.append(f"{record['images_no_alt']} images without alt")
        if "noindex" in record["robots_meta"].lower():
            flags.append("noindex")
        if not record["viewport"]:
            flags.append("no viewport")
        if not record["html_lang"]:
            flags.append("no html lang attribute")
        if not record["charset"]:
            flags.append("no charset meta")
        if not record["og_image"]:
            flags.append("no og:image")
        if not record["canonical"]:
            flags.append("no canonical")
        if record["mixed"]:
            flags.append(f"{record['mixed']} mixed-content refs")
        if record["ad_slots"] >= 6:
            flags.append(f"{record['ad_slots']} ad slots (check ad-to-content balance)")
        if record["popup_markers"]:
            flags.append(f"{record['popup_markers']} popup or modal markers (review manually)")
        if trust_paths and record["trust_links"] == 0:
            flags.append("no trust-page links on this page")
        for phrase in PLACEHOLDER_STRINGS:
            if phrase in record["lowered"]:
                flags.append(f"placeholder text: {phrase}")
        for phrase, pattern in REVIEW_PATTERNS:
            if pattern.search(record["lowered"]):
                flags.append(f"REVIEW phrase: {phrase}")
        for phrase, pattern in COPYRIGHT_PATTERNS:
            if pattern.search(record["lowered"]):
                flags.append(f"REVIEW copyright signal: {phrase}")
        if record["canonical"]:
            canon_path = urllib.parse.unquote(urlparse(record["canonical"]).path).rstrip("/")
            final_path = urllib.parse.unquote(urlparse(final_url).path).rstrip("/")
            if canon_path != final_path:
                flags.append("canonical points elsewhere")
        flag_text = ("; ".join(flags)) if flags else "clean"
        mark = "FAIL" if any(f in flag_text for f in ("no title", "no H1", "thin (", "placeholder")) else ("WARN" if flags else "OK")
        print(f"[{mark}] {page_url} | {record['words']} words | article {record['article_words']} | H1:{record['h1']} | alt-missing:{record['images_no_alt']} | {flag_text}")
        page_records.append(record)

    # ---- Cross-page findings ----
    print()
    print("Cross-page findings:")
    ok_pages = [r for r in page_records if r["status"] == 200 and "words" in r]
    failed_pages = [r for r in page_records if r["status"] != 200 or "words" not in r]
    if failed_pages:
        report("fail", f"{len(failed_pages)} sitemap URLs did not return a readable 200 page.")
        for r in failed_pages[:20]:
            print(f"      {r['url']} -> {r['status']}")
    else:
        report("ok", "Every crawled sitemap URL returned a readable 200 page.")

    titles = Counter(r.get("title", "") for r in ok_pages if r.get("title"))
    dup_titles = [t for t, c in titles.items() if c > 1]
    if dup_titles:
        report("warn", f"{len(dup_titles)} duplicate titles found.")
        for t in dup_titles[:10]:
            print(f"      {t[:100]}")
    else:
        report("ok", "No duplicate titles found.")

    descs = Counter(r.get("description", "") for r in ok_pages if r.get("description"))
    dup_descs = [d for d, c in descs.items() if c > 1]
    if dup_descs:
        report("warn", f"{len(dup_descs)} duplicate meta descriptions found.")
    else:
        report("ok", "No duplicate meta descriptions found.")

    thin = [r for r in ok_pages if r["words"] < 200]
    if thin:
        report("warn", f"{len(thin)} pages under 200 words (thin-content risk, human must judge value).")
        for r in thin[:20]:
            print(f"      {r['words']} words: {r['url']}")
    else:
        report("ok", "No crawled page is under 200 words.")

    thin_article = [r for r in ok_pages if 0 < r["article_words"] < 200]
    if thin_article:
        info(f"{len(thin_article)} pages have under 200 words inside article or main content.")
        for r in thin_article[:10]:
            print(f"      {r['article_words']} article words: {r['url']}")

    no_h1 = [r for r in ok_pages if r["h1"] == 0]
    if no_h1:
        report("fail", f"{len(no_h1)} pages have no H1.")
        for r in no_h1[:20]:
            print(f"      {r['url']}")
    multi_h1 = [r for r in ok_pages if r["h1"] > 1]
    if multi_h1:
        report("warn", f"{len(multi_h1)} pages have more than one H1.")
        for r in multi_h1[:20]:
            print(f"      {r['h1']} H1s: {r['url']}")

    no_h2 = [r for r in ok_pages if r["h2"] == 0]
    if no_h2:
        info(f"{len(no_h2)} pages have no H2 headings (structure signal only).")

    alt_total = sum(r["images_no_alt"] for r in ok_pages)
    if alt_total:
        report("warn", f"{alt_total} images across the site have no alt text.")
    else:
        report("ok", "Every image found has alt text.")
    dims_total = sum(r["images_no_dims"] for r in ok_pages)
    if dims_total:
        info(f"{dims_total} images have no width and height attributes (layout shift signal).")

    noindex_pages = [r for r in ok_pages if "noindex" in r["robots_meta"].lower()]
    if noindex_pages:
        report("warn", f"{len(noindex_pages)} crawled pages carry noindex.")
        for r in noindex_pages[:20]:
            print(f"      {r['url']}")

    no_lang = [r for r in ok_pages if not r["html_lang"]]
    if no_lang:
        report("warn", f"{len(no_lang)} pages have no html lang attribute.")
    no_canonical = [r for r in ok_pages if not r["canonical"]]
    if no_canonical:
        report("warn", f"{len(no_canonical)} pages have no canonical link.")
    no_og = [r for r in ok_pages if not r["og_image"]]
    if no_og:
        report("warn", f"{len(no_og)} pages have no og:image (share preview signal).")
    no_trust_links = [r for r in ok_pages if r["trust_links"] == 0]
    if no_trust_links and trust_paths:
        report("warn", f"{len(no_trust_links)} pages link to no trust page. Check footer navigation on every template.")
    ld_types = Counter(t for r in ok_pages for t in r["ld_types"])
    if ld_types:
        info(f"Structured data types found: {', '.join(f'{t} x{c}' for t, c in ld_types.most_common(8))}.")
    else:
        info("No JSON-LD @type values found (structured data is optional).")
    ad_pages = [r for r in ok_pages if r["ad_slots"] or r["ad_script"]]
    if ad_pages:
        info(f"{len(ad_pages)} pages carry ad code markers, {sum(r['ad_slots'] for r in ok_pages)} ad slots in total.")
    popup_pages = [r for r in ok_pages if r["popup_markers"]]
    if popup_pages:
        info(f"{len(popup_pages)} pages have popup or modal markers. Review manually for interstitial behaviour.")

    no_date = [r for r in ok_pages if not r["date"]]
    if no_date:
        info(f"{len(no_date)} pages show no <time> element (date signal).")
    no_author = [r for r in ok_pages if not r["author"]]
    if no_author:
        info(f"{len(no_author)} pages show no author or byline signal in markup.")

    # Deep trust and completeness signals
    print()
    print("Deep trust signals (reviewer-eye checks, not Google rules):")
    h1_texts_all = Counter(
        r["h1_texts"][0].strip().lower()
        for r in ok_pages if r["h1_texts"] and r["h1_texts"][0].strip()
    )
    dup_h1 = [h for h, c in h1_texts_all.items() if c > 1]
    if dup_h1:
        report("warn", f"{len(dup_h1)} H1 texts repeat across pages. Each page deserves its own heading.")
        for h in dup_h1[:10]:
            print(f"      {h[:100]}")
    else:
        info("No H1 text repeats across pages.")
    canon_urls = Counter(r["canonical"] for r in ok_pages if r["canonical"])
    dup_canon = [c for c, n in canon_urls.items() if n > 1]
    if dup_canon:
        report("warn", f"{len(dup_canon)} canonical URLs are shared by more than one page.")
        for c in dup_canon[:10]:
            print(f"      {c}")
    linked_targets = set()
    for targets in outlink_map.values():
        linked_targets |= targets
    norm = lambda u: u.rstrip("/")
    sitemap_set = {norm(u) for u in sitemap_urls}
    orphans = [r for r in ok_pages
               if norm(r["url"]) in sitemap_set
               and norm(r["url"]) != norm(base)
               and norm(r["url"]) not in {norm(t) for t in linked_targets}]
    if orphans:
        report("warn", f"{len(orphans)} sitemap {'page receives' if len(orphans) == 1 else 'pages receive'} no internal link from any crawled page (orphan risk). Link them from menus, archives, or related posts.")
        for r in orphans[:15]:
            print(f"      {r['url']}")
    else:
        info("Every crawled sitemap page receives at least one internal link.")
    discovered = {norm(u) for u in internal_links}
    not_in_sitemap = sorted(discovered - sitemap_set - {norm(base)})
    if not_in_sitemap:
        info(f"{len(not_in_sitemap)} discovered internal URLs are not in the sitemap. Tag, author, and pagination URLs are often excluded on purpose.")
        for u in not_in_sitemap[:10]:
            print(f"      {u}")
    sponsored_total = sum(r["sponsored"] for r in ok_pages)
    if sponsored_total:
        info(f"{sponsored_total} links carry rel=sponsored. Affiliate disclosure must be visible on those pages.")
    word_counts = sorted(r["words"] for r in ok_pages)
    if word_counts:
        median_words = word_counts[len(word_counts) // 2]
        shortest = min(ok_pages, key=lambda r: r["words"])
        info(f"Median page length is {median_words} words. Shortest page: {shortest['words']} words ({shortest['url']}).")
    home_record = next((r for r in ok_pages if norm(r["url"]) == norm(base)), None)
    if home_record:
        structure = []
        structure.append("navigation" if home_record["has_nav"] else "NO navigation element")
        structure.append("footer" if home_record["has_footer"] else "NO footer element")
        structure.append("site search" if home_record["has_search"] else "no site search")
        info(f"Homepage structure: {', '.join(structure)}.")
    thin_archives = [r for r in ok_pages
                     if ("/category/" in r["url"] or "/tag/" in r["url"])
                     and r["article_words"] < 50]
    if thin_archives:
        report("warn", f"{len(thin_archives)} category or tag {'page has' if len(thin_archives) == 1 else 'pages have'} under 50 article words. Empty archives look unfinished to a reviewer.")
        for r in thin_archives[:10]:
            print(f"      {r['article_words']} article words: {r['url']}")

    # Homepage gates and trust depth
    if home_record:
        if "noindex" in home_record["robots_meta"].lower():
            report("fail", "Homepage carries noindex. A noindexed homepage cannot be reviewed or ranked. Remove it before applying.")
        if home_record["site_verification"]:
            info("Homepage carries a google-site-verification meta tag (Search Console ownership signal).")
        home_links = outlink_map.get(home_record["url"], set())

        def _is_content_link(u):
            path = urlparse(u).path
            if path in trust_paths or path.rstrip("/") == "":
                return False
            return not any(seg in path for seg in ("/category/", "/tag/", "/author/", "/page/", "/feed"))

        content_links = [u for u in home_links if _is_content_link(u)]
        info(f"Homepage links to {len(content_links)} content URLs (posts or pages). A homepage that shows no content reads as a shell.")
        current_year = str(datetime.datetime.now().year)
        if current_year not in home_body:
            info("Current year not found in homepage HTML. A stale footer year is a small staleness signal.")
    thin_trust = [r for r in ok_pages
                  if urlparse(r["url"]).path in trust_paths and r["words"] < 100]
    if thin_trust:
        report("warn", f"{len(thin_trust)} trust {'page has' if len(thin_trust) == 1 else 'pages have'} under 100 words. Short trust pages read as placeholders.")
        for r in thin_trust[:10]:
            print(f"      {r['words']} words: {r['url']}")
    no_favicon = [r for r in ok_pages if not r["favicon"]]
    if no_favicon:
        info(f"{len(no_favicon)} pages have no favicon link (browser tab and bookmark signal).")
    social_domains = ("facebook.com", "instagram.com", "youtube.com",
                      "x.com", "twitter.com", "linkedin.com", "pinterest.com")
    social_links = [u for u in external_links
                    if any(urlparse(u).netloc.lower().endswith(d) for d in social_domains)]
    if social_links:
        platforms = {urlparse(u).netloc.lower() for u in social_links}
        info(f"{len(social_links)} links point to social platforms across {len(platforms)} domains. A visible social presence supports trust.")
    else:
        info("No links to major social platforms were found. A visible social presence supports trust.")
    contact_record = next((r for r in ok_pages
                           if "contact" in urlparse(r["url"]).path), None)
    if contact_record:
        if contact_record["mailto"]:
            info("Contact page lists an email address.")
        else:
            info("Contact page shows no email link. A form alone is fine, but an email address adds trust.")
    comment_pages = [r for r in ok_pages if r["comment_markers"]]
    if comment_pages:
        info(f"{len(comment_pages)} pages show comment form markers (reader engagement signal).")
    related_pages = [r for r in ok_pages if r["related_markers"]]
    if related_pages:
        info(f"{len(related_pages)} pages show related-content markers (internal linking signal).")
    nofollow_total = sum(r["nofollow"] for r in ok_pages)
    if nofollow_total:
        info(f"{nofollow_total} links carry rel=nofollow.")
    updated_pages = [r for r in ok_pages if r["updated_signal"]]
    if updated_pages:
        info(f"{len(updated_pages)} pages show updated or modified markers (freshness signal).")
    out_counts = [len(v) for v in outlink_map.values()]
    if out_counts:
        info(f"Pages link out to {sum(out_counts) / len(out_counts):.0f} internal URLs on average (lowest {min(out_counts)}).")

    # Near-duplicate content on article text
    print()
    print("Near-duplicate check (article text, shingle similarity):")
    dup_pairs = []
    shingle_cache = {}
    for record in ok_pages:
        if record["article_words"] >= 50:
            shingle_cache[record["url"]] = shingle_set(record["article_text"])
    urls = list(shingle_cache)
    for i in range(len(urls)):
        for j in range(i + 1, len(urls)):
            sim = jaccard(shingle_cache[urls[i]], shingle_cache[urls[j]])
            if sim >= 0.75:
                dup_pairs.append((sim, urls[i], urls[j]))
    if dup_pairs:
        report("warn", f"{len(dup_pairs)} page {'pair shares' if len(dup_pairs) == 1 else 'pairs share'} over 75 percent article text. Shared template text can inflate this. Read both pages of each pair.")
        for sim, left, right in sorted(dup_pairs, reverse=True)[:15]:
            print(f"      {sim:.0%}: {left} <-> {right}")
    else:
        report("ok", "No page pair shares over 75 percent article text.")

    # ---- Internal link verification ----
    print()
    links_to_check = sorted(internal_links)[: args.max_links]
    print(f"Verifying {len(links_to_check)} unique internal links (cap {args.max_links}).")
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        checked = list(executor.map(
            _fetch_status,
            [(link, args.timeout, args.delay) for link in links_to_check],
        ))
    broken = [(link, error or status) for link, status, error in checked if status != 200]
    if broken:
        report("fail", f"{len(broken)} internal links do not return 200.")
        for link, problem in broken[:30]:
            print(f"      {link} -> {problem}")
    else:
        report("ok", "Every verified internal link returns 200.")

    # ---- External link verification ----
    print()
    ext_to_check = sorted(external_links)[: args.max_external]
    print(f"Verifying {len(ext_to_check)} unique external links (cap {args.max_external}).")
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        probed_ext = list(executor.map(
            _probe_url,
            [(link, args.timeout, args.delay) for link in ext_to_check],
        ))
    ext_broken = []
    ext_unverified = []
    for link, status, error, _ in probed_ext:
        if status is not None and 200 <= status < 400:
            continue
        if status in (401, 403, 429) or status is None:
            ext_unverified.append((link, error or status))
        else:
            ext_broken.append((link, error or status))
    if ext_broken:
        report("warn", f"{len(ext_broken)} external links look broken. Check each in a browser.")
        for link, problem in ext_broken[:20]:
            print(f"      {link} -> {problem}")
    else:
        report("ok", "No verified external link is broken.")
    if ext_unverified:
        info(f"{len(ext_unverified)} external {'link' if len(ext_unverified) == 1 else 'links'} could not be verified (blocked, rate limited, or unreachable from here).")

    # ---- Image verification ----
    print()
    imgs_to_check = sorted(image_urls)[: args.max_images]
    print(f"Verifying {len(imgs_to_check)} unique same-origin images (cap {args.max_images}).")
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        probed_imgs = list(executor.map(
            _probe_url,
            [(link, args.timeout, args.delay) for link in imgs_to_check],
        ))
    broken_imgs = []
    unverified_imgs = []
    big_imgs = []
    for link, status, error, size in probed_imgs:
        if status is not None and 200 <= status < 400 and size > 1_000_000:
            big_imgs.append((link, size))
        if status is None:
            # No HTTP response at all: a flaky host looks the
            # same as a dead image from here, so report it as
            # unverified rather than broken.
            unverified_imgs.append((link, error or status))
        elif not (200 <= status < 400):
            broken_imgs.append((link, error or status))
    if broken_imgs:
        report("warn", f"{len(broken_imgs)} images do not load.")
        for link, problem in broken_imgs[:20]:
            print(f"      {link} -> {problem}")
    else:
        report("ok", "Every verified image loads.")
    if unverified_imgs:
        info(f"{len(unverified_imgs)} {'image' if len(unverified_imgs) == 1 else 'images'} could not be verified (no HTTP response; recheck in a browser before treating them as broken).")
    if big_imgs:
        report("warn", f"{len(big_imgs)} {'image is' if len(big_imgs) == 1 else 'images are'} over 1 MB. Heavy images slow pages for readers and reviewers.")
        for link, size in big_imgs[:10]:
            print(f"      {size // 1024} KB: {link}")

    # ---- Score and verdict ----
    print()
    score = max(0, 100 - 8 * RESULTS["fail"] - 2 * RESULTS["warn"])
    print(f"Summary: {RESULTS['fail']} failure(s), {RESULTS['warn']} warning(s), {RESULTS['ok']} pass(es).")
    print(f"Readiness score: {score}/100. Heuristic only: 100 minus 8 per failure and 2 per warning.")
    print("This score is NOT a Google score and predicts nothing. It only ranks how much machine-checkable work remains.")
    print("This check cannot judge: originality, content value, policy")
    print("compliance, traffic quality, account history, or Google's final decision.")
    print("Continue with the human audit in references/08-pre-apply-checklist.md.")
    if RESULTS["fail"]:
        print("Result: DO NOT APPLY YET - fix the failures above first.")
        code = 1
    else:
        print("Result: machine-checkable points pass. Human audit still required.")
        code = 0

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write("# Deep approval-clone audit report\n\n")
            handle.write(f"Site: {base}\n\n```\n")
            handle.write("\n".join(LINES))
            handle.write("\n```\n")
        _REAL_PRINT(f"Report written to {args.output}")

    if args.json:
        json_pages = []
        for record in page_records:
            json_pages.append({
                "url": record["url"],
                "status": record["status"],
                "final_url": record.get("final", ""),
                "title": record.get("title", ""),
                "description": record.get("description", ""),
                "h1_count": record.get("h1", 0),
                "h2_count": record.get("h2", 0),
                "words": record.get("words", 0),
                "article_words": record.get("article_words", 0),
                "images": record.get("images", 0),
                "images_no_alt": record.get("images_no_alt", 0),
                "canonical": record.get("canonical", ""),
                "robots_meta": record.get("robots_meta", ""),
                "viewport": record.get("viewport", False),
                "og_image": record.get("og_image", ""),
                "html_lang": record.get("html_lang", ""),
                "ad_slots": record.get("ad_slots", 0),
                "popup_markers": record.get("popup_markers", 0),
                "trust_links": record.get("trust_links", 0),
                "author_signal": record.get("author", False),
                "date_signal": record.get("date", False),
                "has_nav": record.get("has_nav", False),
                "has_footer": record.get("has_footer", False),
                "has_search": record.get("has_search", False),
                "sponsored_links": record.get("sponsored", 0),
                "mailto_links": record.get("mailto", 0),
                "comment_markers": record.get("comment_markers", 0),
                "related_markers": record.get("related_markers", 0),
                "nofollow_links": record.get("nofollow", 0),
                "updated_signal": record.get("updated_signal", False),
                "site_verification": record.get("site_verification", False),
                "favicon": record.get("favicon", False),
                "flags": record.get("flags", []),
            })
        payload = {
            "site": base,
            "tool": "deep_audit v2",
            "summary": dict(RESULTS),
            "score": score,
            "score_note": "Heuristic only. Not a Google score.",
            "checks": CHECKS,
            "sitemap": sitemap_used,
            "pages_crawled": len(page_records),
            "internal_links_verified": len(links_to_check),
            "internal_links_broken": [link for link, _ in broken],
            "external_links_verified": len(ext_to_check),
            "external_links_broken": [link for link, _ in ext_broken],
            "external_links_unverified": [link for link, _ in ext_unverified],
            "images_verified": len(imgs_to_check),
            "images_broken": [link for link, _ in broken_imgs],
            "images_unverified": [link for link, _ in unverified_imgs],
            "images_over_1mb": [link for link, _ in big_imgs],
            "near_duplicate_pairs": [
                {"similarity": round(sim, 2), "left": left, "right": right}
                for sim, left, right in dup_pairs
            ],
            "pages": json_pages,
        }
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
        _REAL_PRINT(f"JSON report written to {args.json}")

    return code


if __name__ == "__main__":
    sys.exit(main())
