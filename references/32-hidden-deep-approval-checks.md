# Hidden and deep approval checks

Google does not publish its full internal review checklist.
Anyone who claims to know every check Google runs is
guessing. This reference separates three layers: what
Google confirms in public, what rejection patterns and
reviewer behaviour suggest, and what stays hidden inside
Google. The deep audit script checks everything in the
first two layers that a crawler can see. The third layer
cannot be checked from outside, and this reference says
so plainly.

Read `references/31-approval-check-matrix.md` for the full
split between automated checks, human-decided flags, and
checks no script can run.

## Layer 1: what Google confirms in public

These come from official Help pages and policy documents.
They are rules, not guesses.

- The site must follow the Publisher Policies and the
  Publisher Restrictions. Prohibited content cannot be
  monetised at all. Restricted content can be monetised
  only with limited demand.
- The applicant must be 18 or older, or apply through a
  parent or guardian. The applicant must own or control
  the site and be able to edit its HTML.
- Content must be original and high quality. Google
  publishes no minimum post count, no minimum word count,
  no minimum traffic level, and no universal domain age
  rule. Any checklist that states one as a Google rule is
  inventing it.
- A site review usually takes a few days and sometimes
  takes two to four weeks.
- The review looks at the whole site, not a single page.
  One violating page can hold back an otherwise clean
  site.
- Identity verification, address verification by PIN, and
  payment details are checked inside the account, not on
  the public site.
- Consent rules apply to EEA, UK, and Swiss traffic: a
  certified consent platform and Consent Mode signals
  where required.

## Layer 2: what rejection patterns suggest

These come from thousands of published rejection notices,
publisher reports, and reviewer behaviour. They are
strongly suggested patterns, not confirmed rules. Treat
each one as a risk to remove, never as a guaranteed
cause of rejection.

- Low value content. The most common rejection reason.
  Pages that repeat what every other site says, pages
  with no experience behind them, and pages that answer
  nothing fully. The signal is depth and originality,
  not length.
- Thin site. Very few pages, or pages that are mostly
  navigation and boilerplate with little real content.
  No fixed number is published, but a site with three
  short pages reads as unfinished.
- Unfinished site. Empty categories, pages under
  construction, placeholder text, broken menus, missing
  About or Contact pages, and dead links. A reviewer
  reads these as signs the site is not ready for
  visitors, let alone ads.
- No trust signals. No author identity, no way to
  contact the owner, no privacy disclosure, no dates.
  A reviewer cannot verify who runs the site.
- Copied or spun content. Text lifted from other sites,
  lightly rewritten, or mass produced without human
  review. Originality checks happen in ways no crawler
  can reproduce.
- Traffic quality doubts. Sudden traffic spikes, traffic
  from bought sources, and traffic that does not behave
  like readers. The reviewer sees signals the publisher
  cannot see.
- Policy grey areas in context. A keyword list cannot
  judge whether health claims, financial advice, or
  adult-adjacent content crosses a line. A human reads
  the page in full.
- Navigation dead ends. Pages that no menu, archive, or
  related link reaches. Orphan pages suggest the site is
  assembled for approval rather than built for readers.
- Stale site. No new content for months, an outdated
  sitemap, and old dates everywhere. Activity is a trust
  signal, not a rule.
- Ad readiness confusion. Ad code placed before approval,
  competing ad networks on the same page, or layouts
  built around ad slots with little content. The site
  should read well with no ads at all.

## Layer 3: what stays hidden

These checks exist inside Google and cannot be observed,
reproduced, or audited from outside the account.

- Account history. Previous applications, warnings,
  limits, and closures on the same account and on
  associated accounts, devices, and payment details.
- Traffic quality scoring. How Google scores the
  genuineness of the site's visitors, and which sources
  it distrusts.
- Reviewer judgement. The final call weighs the whole
  site in context. Two reviewers can weigh the same site
  differently.
- Policy interpretation updates. Enforcement emphasis
  shifts over time, and the current emphasis is not
  published in advance.
- Association signals. Links between the applicant and
  other accounts, sites, or payment profiles that Google
  treats as related.

No tool, checklist, or consultant can check Layer 3.
Any service that promises otherwise is selling
confidence it cannot deliver.

## What the deep audit checks in Layer 2

`scripts/deep_audit.py` version 2 runs these deep checks,
each labelled as a reviewer-eye signal, never as a Google
rule:

- About page depth and Contact page form presence.
- Content freshness from sitemap lastmod dates, and the
  span of content history.
- Orphan pages: sitemap pages with no internal link from
  any crawled page.
- Sitemap coverage: discovered internal URLs missing
  from the sitemap, with the note that tag, author, and
  pagination URLs are often excluded on purpose.
- Duplicate H1 texts and canonical URL collisions across
  pages.
- Pages missing date signals and author or byline
  signals.
- Sponsored link counts, as a prompt to check affiliate
  disclosure.
- Word count distribution: median length and the
  shortest page.
- Homepage structure: navigation element, footer
  element, and site search.
- Thin category and tag pages with under 50 article
  words.
- Near-duplicate article text, external link health,
  image health, ad slot counts, popup markers, and the
  full Layer 1 surface from
  `references/23-approval-clone-audit.md`.

## How to use this reference before applying

- Fix every Layer 1 failure. These are real rules.
- Remove every Layer 2 risk you can find. Read the site
  as a stranger who has never seen it and who is paid to
  be suspicious.
- Answer the Layer 3 questions honestly. If the account
  has history, or the traffic has a doubtful source, no
  site polish removes that risk. Fix the underlying
  problem first, or wait until the history is clean.
- Run the deep audit, fix the failures, read every
  flagged page in full, and complete the human checklist
  in `references/08-pre-apply-checklist.md`.
- Never present a clean script report as a promise of
  approval. The script checks the visible surface. The
  decision stays with Google.
