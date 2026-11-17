# Approval-clone audit

How to replicate the checkable surface of an AdSense site review
point by point, using the deep audit script. This clones the
review's observable checks, not Google's internal decision. No
script can reproduce reviewer judgement, originality assessment,
or policy interpretation. For the full list of what is
automated, what is flagged for a human, and what no script can
check, read `references/31-approval-check-matrix.md`.

Version 2 of the script adds redirect and host consistency,
ads.txt line validation, consent and ad code detection,
sitemap freshness, 404 behaviour, Open Graph and language
checks, article-only word counts, near-duplicate detection,
external link and image verification, a readiness score, and
a JSON report.

## What the clone covers

The deep audit in `scripts/deep_audit.py` crawls the sitemap and
checks every page for the small points a reviewer notices:

Site level:

- HTTPS across the site, with HTTP to HTTPS redirect checked.
- Alternate host (www or bare) redirecting to one canonical host.
- Homepage reachable with HTTP 200, with response time and
  security headers recorded.
- Homepage cache and security headers recorded as information
  only: Cache-Control, CDN or cache headers,
  Content-Security-Policy, and X-Frame-Options. Presence or
  absence is a hosting signal, never a review rule.
- robots.txt present, not blocking all crawling, not blocking
  the AdSense crawler, and naming a sitemap. Sitemap URLs
  matching a Disallow rule for User-agent star are flagged
  as a warning, using the approximate parse documented in
  the script. A robots.txt that cannot be fetched means
  unverified, never blocked.
- ads.txt present with a well formed Google publisher line:
  16-digit publisher ID, DIRECT relationship, and the
  certification ID.
- Nonsense URL returning 404, not a soft 404.
- Feed and archive pagination presence recorded.
- Trust pages present: About, Contact, Privacy, Terms,
  Disclaimer.
- Privacy page disclosure keywords: cookies, Google,
  advertising, third parties, opt-out or Ads Settings.
- Consent platform markers and ad code markers detected.
- Sitemap present with reachable URLs, and lastmod freshness
  checked.

Every crawled page:

- HTTP 200, with redirects noted.
- Title present, reasonable length, unique across the site,
  with word repetition flagged.
- Meta description present, reasonable length, unique, and
  not identical to the title.
- Exactly one H1, with empty H1s flagged, and H2 count
  recorded.
- Word count, with thin pages flagged for human judgement,
  and article-only word count recorded separately.
- Images without alt text, counted per page, and images
  without width and height attributes counted.
- Canonical tag present and self-referencing.
- Meta robots flags such as noindex, and the X-Robots-Tag
  response header checked for noindex on every page, since a
  header noindex is invisible in the page HTML.
- Affiliate links counted, with disclosure wording and
  sponsored or nofollow qualification checked as practice
  heuristics, not as Google rules.
- Internal outlink count recorded, so pages that link to no
  other internal page can be flagged as navigation dead ends.
- Viewport tag for mobile layout, HTML lang attribute, and
  charset meta.
- Open Graph title, description, and image, and Twitter card.
- Mixed content references on HTTPS pages.
- Ad slot count, with six or more slots flagged for an
  ad-to-content balance review.
- Popup and modal markers, counted for manual review.
- Trust-page links counted per page.
- Placeholder and demo strings: lorem ipsum, hello world, sample
  page, under construction, and similar.
- High-risk phrases and copyright-risk signals flagged for
  human review only, never as an automatic verdict.
- Structured data types, author signals, and date signals, as
  information only.

Cross-page:

- Duplicate titles and duplicate descriptions.
- Pages with no H1 or with several H1s.
- Pages with no lang attribute, no canonical, or no og:image.
- Sitemap URLs that redirect to a different final URL, listed
  as a warning. Sitemaps should list final URLs. Heuristic
  only, not a Google rule.
- Noindexed pages still listed in the sitemap, listed as a
  warning. A noindexed page in the sitemap sends a mixed
  signal to crawlers.
- Open Graph and Twitter completeness counts as information
  only: pages missing og:title, og:description, or
  twitter:card. Share preview signals, never a fail or a
  warning.
- Canonical target verification: same-origin canonical URLs
  not already known good from the crawl are probed, capped
  at 50. A canonical that does not return 200 is a warning.
  Blocked or rate limited targets are reported as
  unverified, never broken.
- Total images missing alt text.
- Near-duplicate article text by shingle similarity.
- Internal link verification: every unique internal link checked
  for HTTP 200, up to the cap.
- External link verification, up to the cap, with blocked links
  reported as unverified rather than broken.
- Same-origin image verification, up to the cap.
- Readiness score from 0 to 100, heuristic only, never a
  Google score.

## What the clone cannot cover

- Whether content is original, or copied and rewritten.
- Whether content is genuinely useful or only looks long.
- Whether images are licensed or stolen.
- Whether traffic is real or bought.
- Whether the niche carries restricted or prohibited content in
  context. Keyword flags are only a prompt to read.
- Whether the applicant's identity, payments, and tax details are
  correct. Those live in the account, not on the site.
- Google's final decision, which weighs factors no crawler sees.

A clean deep audit means the machine-checkable surface is ready.
It never means approval is certain.

## How to run it

```bash
python3 scripts/deep_audit.py https://example.com
python3 scripts/deep_audit.py https://example.com --max-pages 100 --max-links 150 --output report.md --json report.json
```

Options:

- `--max-pages`: cap on crawled pages. Default 200.
- `--max-links`: cap on verified internal links. Default 250.
- `--max-external`: cap on verified external links. Default 80.
- `--max-images`: cap on verified images. Default 100.
- `--delay`: seconds of delay per worker before each request.
  Default 0.25. Raise it for slow or shared hosting.
- `--workers`: parallel requests. Default 8. Page fetches,
  site-level checks, and link and image verification all run
  in parallel, and the report still reads in sitemap order.
  Use 1 or 2 for fragile shared hosting, and raise the delay
  if the host rate limits the crawl.
- `--timeout`: seconds per request. Default 20.
- `--output`: write the same report into a Markdown file.
- `--json`: write a machine-readable JSON report with every page
  record, every check, and every broken link.

The script is read-only and uses only the Python standard library.
It identifies itself in the user agent string.

## How to read the report

- FAIL means fix before applying. A failed page status, a missing
  trust page, a page with no H1, or a broken internal link are
  failures.
- WARN means fix or consciously accept. Duplicate descriptions,
  thin pages, missing alt text, and long titles are warnings.
  Each warning needs a human decision, not blind fixing.
- OK means the point passed.
- The per-page lines show the raw numbers so a fix can target the
  exact URL.
- The verdict line states whether failures remain. A pass still
  requires the human audit in
  `references/08-pre-apply-checklist.md`.

## Reviewer simulation workflow

1. Run `scripts/site_audit.py` first for the five-minute surface
   check.
2. Run `scripts/deep_audit.py` for the full crawl.
3. Fix every FAIL, starting with unreachable pages and missing
   trust pages.
4. Decide every WARN with a human reading the page. Do not pad
   thin pages with filler to pass a word count. Improve or remove
   them.
5. Read every page the script flagged for review phrases, in
   full, and judge policy fit from
   `references/03-publisher-policies.md` and
   `references/04-publisher-restrictions.md`.
6. Open the site as a stranger on a phone. The script cannot see
   layout breakage, popups, or reading flow.
7. Run the deep audit again and confirm zero failures.
8. Complete the human checklist in
   `references/08-pre-apply-checklist.md` before applying.

## Thresholds used, and their status

- Title length 10 to 70 characters: SEO practice, not a Google
  rule. A good title outside the range is fine.
- Description length 50 to 160 characters: SEO practice, not a
  Google rule.
- Thin page under 200 words: a heuristic flag, not a Google
  minimum. Short pages can be valuable. Long pages can be
  worthless. A human judges value.
- Exactly one H1: standard practice. The fix is usually a theme
  or template change, not content work.
- Near-duplicate flag at 75 percent shingle similarity: a
  heuristic. Shared template text inflates the score. Read
  both pages before calling anything a duplicate.
- Ad slot flag at 6 or more slots: a heuristic prompt to check
  ad-to-content balance, not a Google limit. The old
  three-ads-per-page limit was removed in 2016, reported.
- Homepage slow flag over 3 seconds: a user experience
  heuristic, not a Google rule.
- Affiliate disclosure flag: a page with affiliate links and
  no disclosure wording is a practice heuristic, not a Google
  rule. Disclosure rules come from regulators and affiliate
  programs, not from AdSense. See
  `references/36-affiliate-content-and-disclosure.md`.
- Affiliate qualification flag: a page with affiliate links
  and no sponsored or nofollow links at all is flagged for
  manual review. Google accepts either qualification, so the
  flag only fires when neither is present.
- Navigation dead end: a page with no internal outlinks is a
  navigation-signal heuristic, not a Google rule. Archives
  and landing pages may be dead ends on purpose.
- Sitemap redirect summary: a sitemap URL whose final URL
  differs is a hygiene heuristic, not a Google rule.
  Trailing-slash-only differences are ignored.
- Robots-blocked sitemap URLs: the script parses only the
  User-agent star group, with prefix matching, star
  wildcards, and dollar end anchors, and applies the
  longest-match rule with Allow winning ties. It is an
  approximation. A human must read robots.txt to confirm.
- Noindex-in-sitemap cross-check: a page that carries
  noindex through a meta tag or an X-Robots-Tag header and
  is still listed in the sitemap is a mixed-signal
  heuristic, not a Google rule.
- Open Graph and Twitter completeness: counts only,
  information only, never scored. Missing share tags do
  not affect the readiness score.
- Canonical target verification: a probed canonical that
  does not return 200 is a broken-signal warning. Targets
  already known good from the crawl are skipped, and the
  probe cap is 50. Blocked or rate limited targets are
  unverified, never broken.
- Readiness score, 100 minus 8 per failure and 2 per warning:
  a work-remaining rank, not a Google score, and it predicts
  nothing about approval.

Never present these thresholds to a user as Google's rules. They
are tripwires for human attention.
