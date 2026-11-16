# Complete approval check matrix

This reference lists every check involved in an AdSense site
review, split into three groups: checks a script can run,
checks a script can only flag for a human, and checks no
script can run at all. It is the honest answer to the
question of whether automated checking can match Google's
review 100 percent.

Read the audit method in
`references/23-approval-clone-audit.md` and the human
checklist in `references/08-pre-apply-checklist.md`.

## The honest answer about 100 percent

No tool can match Google's approval decision 100 percent.
The decision includes human judgement of content value and
originality, account history the reviewer can see and a
crawler cannot, traffic quality signals from Google's own
systems, and policy interpretation that changes with
context. Anyone who promises a tool that clones the
decision is selling a story, not a check.

What a tool can match 100 percent is the checkable surface:
every page, every link, every tag, every file, and every
measurable signal a reviewer can see from outside the
account. `scripts/deep_audit.py` version 2 covers that
surface as fully as possible. The groups below show exactly
where automation ends and human judgement begins.

## Group A: fully automated checks

`scripts/deep_audit.py` runs all of these. A failure here is
a fact, not an opinion.

Site level:

- Homepage returns HTTP 200 over HTTPS.
- HTTP version redirects to HTTPS.
- Alternate host (www or bare) redirects to one canonical
  host.
- Homepage response time and body size recorded.
- Security headers recorded (HSTS, X-Content-Type-Options).
- robots.txt exists, does not block all crawling, does not
  block the AdSense crawler, and names a sitemap.
- ads.txt exists and the Google line is well formed: a
  16-digit publisher ID, DIRECT relationship, and the
  certification ID. Malformed lines and conflicting IDs
  are flagged.
- Nonsense URL returns 404, not a soft 404.
- RSS feed and archive pagination presence recorded.
- All five trust pages found at common slugs: About,
  Contact, Privacy, Terms, Disclaimer.
- Privacy page mentions cookies, Google, advertising,
  third parties, and opt-out or Ads Settings.
- Consent platform markers detected on the homepage.
- Ad code markers detected on the homepage.
- Sitemap found, URL count recorded, newest and oldest
  lastmod dates recorded, stale sitemap flagged.

Per page, for every sitemap URL:

- HTTP status and redirect behaviour.
- Title present, length within the 10 to 70 character
  practice range, and word repetition flagged.
- Meta description present, length within the 50 to 160
  character practice range, and identical-to-title flagged.
- Exactly one H1, with empty H1s flagged, and H2 count
  recorded.
- Word count, with under 200 words flagged as thin, and
  article-only word count recorded separately.
- Images counted, missing alt text counted, and missing
  width and height attributes counted.
- Canonical link present and pointing at the same page,
  with URL encoding differences ignored.
- Meta robots noindex flagged.
- X-Robots-Tag response header checked for noindex on
  every page. A header noindex hides the page from
  review just like a meta tag, and it is invisible in
  the page HTML.
- Viewport meta, HTML lang attribute, and charset meta
  present.
- Open Graph title, description, and image present, and
  Twitter card present.
- JSON-LD structured data present, with @type values
  recorded.
- Author or byline signal and date signal recorded.
- Mixed-content references counted.
- Ad slot count recorded, with six or more slots flagged
  for an ad-to-content balance review.
- Popup and modal markers counted for manual review.
- Trust-page links counted per page, with pages that link
  to no trust page flagged.
- Placeholder and demo strings flagged.
- Review phrases flagged with word-boundary matching, so
  substrings never trip a flag.
- Copyright-risk signals flagged for a human read.

Cross-page:

- Duplicate titles and duplicate meta descriptions found.
- Thin pages listed.
- Pages with no H1, multiple H1s, no lang, no canonical,
  or no og:image listed.
- Near-duplicate article text found by shingle similarity
  over 75 percent, with the warning that shared template
  text can inflate the score.
- Every unique internal link verified, capped, with
  broken links listed.
- External links verified, capped, with blocked or rate
  limited links reported as unverified rather than broken.
- Same-origin images verified, capped, with broken images
  listed.
- A readiness score from 0 to 100, computed as 100 minus
  8 per failure and 2 per warning, labelled heuristic
  only and never presented as a Google score.
- A machine-readable JSON report with every page record,
  every check, and every broken link.

`scripts/site_audit.py` runs the quick subset: HTTPS,
homepage title and viewport, HTML lang, favicon, demo
markers, consent markers, HTTP to HTTPS redirect, 404
behaviour, robots.txt depth, sitemap presence, ads.txt
line validation, and trust pages.

## Group B: script flags, human decides

The script finds these. Only a human reading the page can
judge them.

- Whether flagged review phrases are violations or
  legitimate discussion. A fitness article that mentions
  a drug name in a warning is not the same as a page
  selling it.
- Whether near-duplicate pages are true duplicates or
  shared template text around different content.
- Whether popup and modal markers are harmful
  interstitials or harmless newsletter boxes.
- Whether ad density harms the reader on a specific page.
  The slot count is a number. The experience is a judgement.
- Whether thin pages are genuinely low value or short
  pages that fully answer a narrow question.
- Whether images without alt text are decorative or
  meaningful.
- Whether external links are trustworthy. A link that
  returns 200 can still point at a violating page.
- Whether the Privacy disclosure wording is accurate for
  the site's actual data handling. Keyword presence is
  not legal accuracy.
- Whether affiliate disclosure wording is visible to a
  reader. The script finds the words. Only a human can
  judge whether the disclosure sits near the top of the
  page or is buried where nobody reads it.
- Whether affiliate links are qualified with sponsored
  or nofollow. The script flags pages with neither.
  A human confirms each paid link carries the right
  value.
- Whether a navigation dead end page is a real problem.
  The script flags pages with no internal outlinks. A
  landing page may be a dead end on purpose. A post
  with no related links is a missed chance for readers
  and crawlers.
- Whether the consent banner actually renders and works
  for a new visitor. A marker in HTML is not a working
  banner.

## Group C: no script can check

These decide real reviews, and they live outside any
crawler's reach.

- Originality. Whether the content is genuinely written,
  tested, and owned, or copied, spun, or pasted from
  elsewhere. Plagiarism checking needs comparison against
  the web, and even then a human must judge the result.
- Content value. Whether a page fully answers its
  question, adds experience, and earns its place. Word
  count is not value.
- Policy interpretation. Whether content falls under a
  prohibited or restricted category in context. Keyword
  lists cannot read context.
- Traffic quality. Whether visitors are genuine, where
  they come from, and how they behave. Only Google's own
  systems and the publisher's analytics can show this.
- Account history. Previous applications, warnings,
  limits, and closures on the account and on associated
  accounts. A crawler sees a site, not an account.
- Identity and payment truth. Whether the payee is who
  the documents say, and whether the bank account matches.
  Verification happens inside Google's systems.
- Reviewer judgement. The final call is a human decision
  on the whole site, informed by all of the above. Two
  reviewers can weigh the same site differently, and no
  checklist removes that.

For the three-layer split between confirmed public
checks, patterns suggested by rejections, and checks
that stay hidden inside Google, read
`references/32-hidden-deep-approval-checks.md`.

## How to use the matrix

- Run `scripts/site_audit.py` first for the quick verdict.
- Run `scripts/deep_audit.py` for the full checkable
  surface, with `--output` for the readable report and
  `--json` for the machine-readable record.
- Fix every Group A failure. Decide every Group A warning
  by reading the page.
- Work through every Group B flag by opening the page as
  a stranger would.
- Answer every Group C question honestly before applying,
  using `references/08-pre-apply-checklist.md`,
  `references/09-content-quality-guide.md`, and the policy
  references. If any Group C answer is uncomfortable, the
  site is not ready, however clean the script output looks.

## Keeping the matrix honest

When Google changes a rule, the matrix must change with
it. When a new checkable signal appears, add it to Group
A with a label that says whether it is a Google rule or a
practice heuristic. When a check proves unreliable, move
it to Group B or remove it, and record the change in
`CHANGELOG.md`. A matrix that claims certainty it does
not have is worse than no matrix at all.
