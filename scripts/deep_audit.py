#!/usr/bin/env python3
"""Deep approval-clone audit: crawl a site and check every small,
machine-checkable point a reviewer would notice.

This replicates the CHECKABLE surface of an AdSense site review. It
cannot clone Google's internal decision, judge originality, or rule
on policy compliance. Every finding here still needs a human look.

Read-only. Python standard library only. Be polite: requests run
with a delay between them and a page cap.

Usage:
    python3 scripts/deep_audit.py https://example.com
    python3 scripts/deep_audit.py https://example.com --max-pages 100 --output report.md
"""

import argparse
import http.client
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36 "
    "AdSenseDeepAudit/1.0"
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
]

REVIEW_PATTERNS = [
    (phrase, re.compile(r"\b" + re.escape(phrase) + r"\b"))
    for phrase in REVIEW_PHRASES
]

SKIP_LINK_SUFFIXES = (
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico",
    ".css", ".js", ".pdf", ".zip", ".mp3", ".mp4", ".xml",
)

RESULTS = {"fail": 0, "warn": 0, "ok": 0}

LINES = []
_REAL_PRINT = print


def emit(text=""):
    LINES.append(str(text))
    _REAL_PRINT(text)


def report(level, message):
    RESULTS[level] += 1
    label = {"ok": "[OK]  ", "warn": "[WARN]", "fail": "[FAIL]"}[level]
    emit(f"{label} {message}")


def fetch(url, timeout):
    """GET a URL, retrying once after a transient failure.

    Returns (status, final_url, body_text, error). Chunked reads
    keep the partial body when a host closes early.
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
                    while total < 3_000_000:
                        chunk = resp.read(65536)
                        if not chunk:
                            break
                        chunks.append(chunk)
                        total += len(chunk)
                except http.client.IncompleteRead as exc:
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
        self.images = []
        self.links = []
        self.canonical = None
        self.ld_json_count = 0
        self.skip_depth = 0
        self.text_parts = []
        self.author_signal = False
        self.date_signal = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.skip_depth += 1
            if attrs.get("type") == "application/ld+json":
                self.ld_json_count += 1
        if tag == "title" and not self.title_done:
            self.in_title = True
        if tag == "meta":
            key = (attrs.get("name") or attrs.get("property") or "").lower()
            if key and key not in self.metas:
                self.metas[key] = attrs.get("content", "")
        if tag == "h1":
            self.in_h1 = True
            self.h1_parts = []
        if tag == "img":
            self.images.append((attrs.get("src", ""), attrs.get("alt")))
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.canonical = attrs.get("href")
        if tag == "time":
            self.date_signal = True
        cls = attrs.get("class", "").lower()
        if "author" in cls or "byline" in cls:
            self.author_signal = True
        if attrs.get("rel") == "author":
            self.author_signal = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip_depth = max(0, self.skip_depth - 1)
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
        if self.skip_depth == 0:
            self.text_parts.append(data)


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def collect_sitemap_urls(sitemap_url, timeout, seen, depth=0):
    """Return page URLs from a sitemap or sitemap index."""
    if depth > 2 or sitemap_url in seen:
        return []
    seen.add(sitemap_url)
    status, _, body, _ = fetch(sitemap_url, timeout)
    if status != 200 or not body:
        return []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
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


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("url", help="Site URL, for example https://example.com")
    parser.add_argument("--timeout", type=int, default=20, help="Seconds per request")
    parser.add_argument("--max-pages", type=int, default=200, help="Max pages to crawl")
    parser.add_argument("--max-links", type=int, default=250, help="Max internal links to verify")
    parser.add_argument("--delay", type=float, default=0.25, help="Seconds between requests")
    parser.add_argument("--output", help="Write the same report to a Markdown file")
    args = parser.parse_args()

    base = args.url if args.url.endswith("/") else args.url + "/"
    parsed_base = urlparse(base)
    netloc = parsed_base.netloc.lower()

    global print  # noqa: A001 - capture all output for --output
    print = emit

    print(f"Deep approval-clone audit: {base}")
    print("Read-only. This replicates checkable review points only.")
    print("It cannot judge originality, value, or policy compliance.")
    print()

    # ---- Site-level checks ----
    if parsed_base.scheme == "https":
        report("ok", "Site URL uses HTTPS.")
    else:
        report("fail", "Site URL is not HTTPS. Move the whole site to HTTPS.")

    status, final_url, home_body, error = fetch(base, args.timeout)
    if status != 200:
        report("fail", f"Homepage did not return HTTP 200 ({error or status}). Fix hosting first.")
        print()
        print("Result: BLOCKER - homepage unreachable.")
        return 1
    report("ok", f"Homepage returns HTTP 200 (final URL: {final_url}).")

    status, _, robots, _ = fetch(urljoin(base, "/robots.txt"), args.timeout)
    if status == 200:
        if re.search(r"User-agent:\s*\*\s*\nDisallow:\s*/\s*$", robots, re.M):
            report("fail", "robots.txt disallows all crawling.")
        else:
            report("ok", "robots.txt exists and does not block all crawling.")
    elif status == 404:
        report("warn", "No robots.txt found (HTTP 404).")
    else:
        report("warn", f"Could not verify robots.txt ({status}). Check it in a browser.")

    status, _, ads_txt, _ = fetch(urljoin(base, "/ads.txt"), args.timeout)
    if status == 200 and "google.com" in ads_txt and "pub-" in ads_txt:
        report("ok", "ads.txt exists and contains a Google publisher line.")
    elif status == 200:
        report("warn", "ads.txt exists but no Google publisher line was found.")
    elif status == 404:
        report("warn", "No ads.txt found (HTTP 404). Publish it after signup.")
    else:
        report("warn", f"Could not verify ads.txt ({status}). Check it in a browser.")

    # ---- Trust pages ----
    print()
    print("Trust pages:")
    trust_found = {}
    for name, slugs in TRUST_SLUGS.items():
        found = None
        for slug in slugs:
            status, _, _, _ = fetch(urljoin(base, slug), args.timeout)
            if status == 200:
                found = slug
                break
            time.sleep(args.delay)
        trust_found[name] = found
        if found:
            report("ok", f"{name}: found at {found}")
        elif name in ("about", "contact", "privacy"):
            report("fail", f"{name}: no common page found. Publish one before applying.")
        else:
            report("warn", f"{name}: no common page found. Add one if the niche needs it.")

    # Privacy disclosure keywords
    if trust_found["privacy"]:
        time.sleep(args.delay)
        status, _, privacy_body, _ = fetch(urljoin(base, trust_found["privacy"]), args.timeout)
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

    # Keep same-origin HTML-ish URLs, dedupe, cap.
    pages = []
    seen_pages = set()
    for raw in sitemap_urls:
        clean = raw.split("#")[0]
        if clean in seen_pages or not same_origin(clean, netloc):
            continue
        if clean.lower().endswith(SKIP_LINK_SUFFIXES):
            continue
        if "/feed" in clean.lower() or "wp-admin" in clean.lower():
            continue
        seen_pages.add(clean)
        pages.append(clean)
        if len(pages) >= args.max_pages:
            break
    if base.rstrip("/") + "/" not in seen_pages and base not in seen_pages:
        pages.insert(0, base)
    print(f"Crawling {len(pages)} pages (cap {args.max_pages}).")

    # ---- Per-page checks ----
    print()
    print("Per-page points (status, words, H1 count, images missing alt, flags):")
    page_records = []
    internal_links = set()
    for page_url in pages:
        time.sleep(args.delay)
        status, final_url, body, error = fetch(page_url, args.timeout)
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
        text = " ".join(parser_html.text_parts)
        record["words"] = len(re.findall(r"\S+", text))
        record["lowered"] = text.lower()
        record["images"] = len(parser_html.images)
        record["images_no_alt"] = sum(1 for _, alt in parser_html.images if alt is None or alt.strip() == "")
        record["canonical"] = parser_html.canonical
        record["robots_meta"] = parser_html.metas.get("robots", "")
        record["viewport"] = "viewport" in parser_html.metas
        record["og_type"] = parser_html.metas.get("og:type", "")
        record["ld_json"] = parser_html.ld_json_count
        record["author"] = parser_html.author_signal
        record["date"] = parser_html.date_signal
        record["mixed"] = len(re.findall(r'''(?:src|href)="http://''', body))
        for href in parser_html.links:
            clean = clean_link(href, page_url)
            if clean and same_origin(clean, netloc):
                if clean.lower().endswith(SKIP_LINK_SUFFIXES):
                    continue
                if "/feed" in clean.lower() or "wp-admin" in clean.lower():
                    continue
                internal_links.add(clean)
        flags = record["flags"]
        if not title:
            flags.append("no title")
        elif len(title) < 10:
            flags.append("title too short")
        elif len(title) > 70:
            flags.append("title long")
        if not record["description"]:
            flags.append("no meta description")
        elif len(record["description"]) < 50:
            flags.append("description short")
        elif len(record["description"]) > 160:
            flags.append("description long")
        if record["h1"] == 0:
            flags.append("no H1")
        elif record["h1"] > 1:
            flags.append(f"{record['h1']} H1s")
        if record["words"] < 200:
            flags.append(f"thin ({record['words']} words)")
        if record["images_no_alt"]:
            flags.append(f"{record['images_no_alt']} images without alt")
        if "noindex" in record["robots_meta"].lower():
            flags.append("noindex")
        if not record["viewport"]:
            flags.append("no viewport")
        if record["mixed"]:
            flags.append(f"{record['mixed']} mixed-content refs")
        for phrase in PLACEHOLDER_STRINGS:
            if phrase in record["lowered"]:
                flags.append(f"placeholder text: {phrase}")
        for phrase, pattern in REVIEW_PATTERNS:
            if pattern.search(record["lowered"]):
                flags.append(f"REVIEW phrase: {phrase}")
        if record["canonical"]:
            canon_path = urllib.parse.unquote(urlparse(record["canonical"]).path).rstrip("/")
            final_path = urllib.parse.unquote(urlparse(final_url).path).rstrip("/")
            if canon_path != final_path:
                flags.append("canonical points elsewhere")
        flag_text = ("; ".join(flags)) if flags else "clean"
        mark = "FAIL" if any(f in flag_text for f in ("no title", "no H1", "thin (", "placeholder")) else ("WARN" if flags else "OK")
        print(f"[{mark}] {page_url} | {record['words']} words | H1:{record['h1']} | alt-missing:{record['images_no_alt']} | {flag_text}")
        page_records.append(record)

    # ---- Cross-page findings ----
    print()
    print("Cross-page findings:")
    ok_pages = [r for r in page_records if r["status"] == 200]
    failed_pages = [r for r in page_records if r["status"] != 200]
    if failed_pages:
        report("fail", f"{len(failed_pages)} sitemap URLs did not return 200.")
        for r in failed_pages[:20]:
            print(f"      {r['url']} -> {r['status']}")
    else:
        report("ok", "Every crawled sitemap URL returned 200.")

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

    alt_total = sum(r["images_no_alt"] for r in ok_pages)
    if alt_total:
        report("warn", f"{alt_total} images across the site have no alt text.")
    else:
        report("ok", "Every image found has alt text.")

    noindex_pages = [r for r in ok_pages if "noindex" in r["robots_meta"].lower()]
    if noindex_pages:
        report("warn", f"{len(noindex_pages)} crawled pages carry noindex.")
        for r in noindex_pages[:20]:
            print(f"      {r['url']}")

    no_date = [r for r in ok_pages if not r["date"]]
    if no_date:
        print(f"      Info: {len(no_date)} pages show no <time> element (date signal).")
    no_author = [r for r in ok_pages if not r["author"]]
    if no_author:
        print(f"      Info: {len(no_author)} pages show no author or byline signal in markup.")

    # ---- Internal link verification ----
    print()
    links_to_check = sorted(internal_links)[: args.max_links]
    print(f"Verifying {len(links_to_check)} unique internal links (cap {args.max_links}).")
    broken = []
    for link in links_to_check:
        time.sleep(args.delay)
        status, _, _, error = fetch(link, args.timeout)
        if status != 200:
            broken.append((link, error or status))
    if broken:
        report("fail", f"{len(broken)} internal links do not return 200.")
        for link, problem in broken[:30]:
            print(f"      {link} -> {problem}")
    else:
        report("ok", "Every verified internal link returns 200.")

    # ---- Verdict ----
    print()
    print(f"Summary: {RESULTS['fail']} failure(s), {RESULTS['warn']} warning(s), {RESULTS['ok']} pass(es).")
    print("This check cannot judge: originality, content value, policy")
    print("compliance, traffic quality, or Google's final decision.")
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

    return code


if __name__ == "__main__":
    sys.exit(main())
