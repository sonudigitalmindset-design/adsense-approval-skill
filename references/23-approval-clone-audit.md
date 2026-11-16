# Approval-clone audit

How to replicate the checkable surface of an AdSense site review
point by point, using the deep audit script. This clones the
review's observable checks, not Google's internal decision. No
script can reproduce reviewer judgement, originality assessment,
or policy interpretation.

## What the clone covers

The deep audit in `scripts/deep_audit.py` crawls the sitemap and
checks every page for the small points a reviewer notices:

Site level:

- HTTPS across the site.
- Homepage reachable with HTTP 200.
- robots.txt present and not blocking all crawling.
- ads.txt present with a Google publisher line.
- Trust pages present: About, Contact, Privacy, Terms,
  Disclaimer.
- Privacy page disclosure keywords: cookies, Google,
  advertising, third parties, opt-out or Ads Settings.
- Sitemap present with reachable URLs.

Every crawled page:

- HTTP 200, with redirects noted.
- Title present, reasonable length, unique across the site.
- Meta description present, reasonable length, unique.
- Exactly one H1.
- Word count, with thin pages flagged for human judgement.
- Images without alt text, counted per page.
- Canonical tag present and self-referencing.
- Meta robots flags such as noindex.
- Viewport tag for mobile layout.
- Mixed content references on HTTPS pages.
- Placeholder and demo strings: lorem ipsum, hello world, sample
  page, under construction, and similar.
- High-risk phrases flagged for human review only, never as an
  automatic verdict.
- Structured data, author signals, and date signals, as
  information only.

Cross-page:

- Duplicate titles and duplicate descriptions.
- Pages with no H1 or with several H1s.
- Total images missing alt text.
- Internal link verification: every unique internal link checked
  for HTTP 200, up to the cap.

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
python3 scripts/deep_audit.py https://example.com --max-pages 100 --max-links 150 --output report.md
```

Options:

- `--max-pages`: cap on crawled pages. Default 200.
- `--max-links`: cap on verified internal links. Default 250.
- `--delay`: seconds between requests. Default 0.25. Raise it for
  slow or shared hosting.
- `--timeout`: seconds per request. Default 20.
- `--output`: write the same report into a Markdown file.

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

Never present these thresholds to a user as Google's rules. They
are tripwires for human attention.
