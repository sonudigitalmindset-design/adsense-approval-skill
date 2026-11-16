# Audit scripts

Two read-only Python checkers. Both use only the Python
standard library. No dependencies, no installation, no
account, no writes to the site.

[Back to the main page](../README.md)

## Quick checker

```bash
python3 scripts/site_audit.py https://example.com
```

The quick checker runs in under a minute. It checks HTTPS,
the homepage title and viewport, the HTML language
attribute, the favicon, the homepage noindex flag, demo
markers, consent platform markers, the HTTP to HTTPS
redirect, 404 behaviour, robots.txt depth including the
AdSense crawler and the sitemap line, ads.txt line
validation, sitemap presence, and the five trust pages:
About, Contact, Privacy, Terms, and Disclaimer.

Use it for a first look. A clean quick check means the
basics are in place. It never means the site is ready.

## Deep approval-clone audit

```bash
python3 scripts/deep_audit.py https://example.com --output report.md --json report.json
```

The deep audit crawls the sitemap and checks every
machine-checkable point a reviewer can see from outside
the account: redirect and host consistency, ads.txt line
validation, consent and ad code signals, sitemap
freshness, 404 behaviour, titles, descriptions, H1s, word
counts and article-only word counts, image alt text and
dimensions, canonicals, noindex flags, viewport, language,
Open Graph and Twitter tags, mixed content, ad slot
counts, popup markers, trust-page links, placeholder text,
review phrases, duplicate titles, near-duplicate article
text, orphan pages, sitemap coverage, trust page depth,
social and contact signals, and verification of internal
links, external links, and images.

The full method, the thresholds, and the limits are in
[`references/23-approval-clone-audit.md`](../references/23-approval-clone-audit.md).
The split between automated checks, human-decided flags,
and checks no script can run is in
[`references/31-approval-check-matrix.md`](../references/31-approval-check-matrix.md).

## Options

- `--max-pages`: cap on crawled pages. Default 200.
- `--max-links`: cap on verified internal links.
  Default 250.
- `--max-external`: cap on verified external links.
  Default 80.
- `--max-images`: cap on verified images. Default 100.
- `--delay`: seconds between requests. Default 0.25.
  Raise it for slow or shared hosting.
- `--timeout`: seconds per request. Default 20.
- `--output`: write the report into a Markdown file.
- `--json`: write a machine-readable JSON report with
  every page record, every check, and every broken link.

Lower the caps for a faster run on a large site, or when
the host drops connections. A capped run still checks
every crawled page. Only the link and image verification
is capped.

## How to read the report

- **FAIL** means fix before applying. A failed page
  status, a missing trust page, a homepage noindex, a
  page with no H1, or a broken internal link are
  failures.
- **WARN** means fix or consciously accept. Duplicate
  descriptions, thin pages, missing alt text, and long
  titles are warnings. Each warning needs a human
  decision, not blind fixing.
- **OK** means the point passed.
- **Readiness score** runs from 0 to 100 and is computed
  as 100 minus 8 per failure and 2 per warning. It is a
  work-remaining rank, not a Google score, and it
  predicts nothing about approval. Never present it as
  one.
- **Unverified** means the check itself could not get an
  answer, usually because the host blocked the request
  or dropped the connection. Unverified is not broken.
  Recheck in a browser before acting.

## What the scripts cannot do

No script can match Google's decision 100 percent. The
scripts cannot judge originality, content value, policy
compliance in context, traffic quality, or account
history. A clean report means the machine-checkable
surface is ready. It never means approval is certain.
Always follow a clean report with the human audit in
[`references/08-pre-apply-checklist.md`](../references/08-pre-apply-checklist.md).

## Troubleshooting

- **A run is slow.** The host may be dropping
  connections, and the script retries. Raise `--delay`
  and lower the caps.
- **A sitemap file could not be read.** The script says
  so as a warning and the crawl may miss pages. Re-run
  the audit.
- **Images show as unverified.** The host closed the
  connection without a response. Open one in a browser.
  If it loads, the host is flaky, not the image.
- **A flag looks wrong.** Read the page. Keyword flags
  are prompts to read, never verdicts. Shared template
  text can inflate the near-duplicate score.

## Next steps

- [How to use this skill](usage.md): the workflows.
- [`references/32-hidden-deep-approval-checks.md`](../references/32-hidden-deep-approval-checks.md):
  the confirmed, suggested, and hidden layers of the
  review.
- [`references/33-unpublished-review-signals.md`](../references/33-unpublished-review-signals.md):
  the inferred signals, each labelled.
