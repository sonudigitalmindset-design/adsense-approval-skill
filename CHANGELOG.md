# Changelog

## 1.12.0 — 18 November 2026

- New `docs/check-catalog.md`: every check in
  `scripts/deep_audit.py` and `scripts/site_audit.py`
  enumerated from the code, each with its status label
  and a one-line description. True count: 159 check
  instances (58 deep audit report checks, 41 deep audit
  information lines, 32 deep audit per-page flag types,
  27 site audit report checks, 1 site audit information
  line), split 16 OFFICIAL, 22 REPORTED, 78 INFERRED,
  43 INFO. The catalog states plainly that the count is
  check instances, not Google rules, and that no count
  matches Google's decision. Nothing was padded, split,
  or renamed to reach any target number.
- No remaining checker work: all genuinely new checks
  from the corrected brief landed in v1.11.0, so this
  release adds no new script checks.
- `references/32-hidden-deep-approval-checks.md` gains
  one INFERRED signal: per-screen inventory judgement,
  sourced from two dated 2026 case audits and the
  official Inventory value policy page, read
  18 November 2026.
- `references/33-unpublished-review-signals.md` gains
  one INFERRED signal: what the crawler sees on
  JavaScript-rendered sites, sourced from the
  SlayerLegendWiki audit of 26 August 2026, read
  18 November 2026. Other candidates from the fresh
  research were left out: the six-month domain-age claim
  is disputed folklore that contradicts the verified
  position, invented post-count and word-count
  thresholds contradict the published no-minimum
  position, and dead-end screen rules already live in
  ref 03.

## 1.11.0 — 18 November 2026

- `scripts/deep_audit.py` gains six genuinely new checks.
  Canonical-presence, canonical-direction, empty-title, and
  empty-description checks already existed as per-page
  flags, so they were not added again. The new checks are:
  sitemap redirect summary (warn, with final URLs),
  robots-blocked sitemap URLs (warn, approximate
  User-agent star parse, unverified when robots.txt
  cannot be fetched), noindex-in-sitemap cross-check
  (warn), Open Graph and Twitter completeness counts
  (information only, never scored), homepage cache and
  security header presence (information only), and
  canonical target verification (warn for non-200,
  capped at 50, blocked targets unverified). The JSON
  report gains matching fields. Existing checks are
  unchanged: the example.com control before and after
  shows an identical summary and identical check list.
  Fixture-server tests confirm all six checks fire, and
  a capped run on thegroundzerofit.com runs clean.
- `references/23-approval-clone-audit.md` and
  `references/31-approval-check-matrix.md` document the
  new checks with their heuristic status and the robots
  parser approximation.

## 1.10.0 — 18 November 2026

- New `references/40-eeat-and-author-trust.md`: E-E-A-T
  as a Search Central quality framework with an explicit
  boundary that it is not an AdSense approval rule, plus
  author trust signals mapped to review readiness as
  inferred practice guidance. Definitions verified on
  the live Search Central page on 18 November 2026.
- New `references/41-ai-assisted-and-scaled-content.md`:
  Google's official stance that AI content is not banned
  per se, with the scaled content abuse rule from the
  live spam policies page, the 2023 AI guidance blog,
  and the generative AI guidance page, all read on
  18 November 2026, plus a safe human-checked workflow.
- New `references/42-publisher-scams-protection.md`:
  fake approval services, buying and selling approved
  accounts, fake support numbers and phishing, and
  unrealistic guarantees. The account-transfer point is
  labelled reported from the official Help snippet and
  the filed Terms, because the direct page fetch was
  rate-limited. The rest is practical guidance.
- New `references/43-admob-guide.md`: dedicated AdMob
  guide covering signup, app setup, ad units, mediation
  basics, app-ads.txt, families policy and TFAT, and
  the key policy differences from AdSense for Content,
  verified on AdMob Help pages on 18 November 2026.
- `references/04-publisher-restrictions.md` gains a
  child-directed content section covering the web,
  AdMob, and YouTube angles, with TFAT replacing
  TFCD and TFUA.
- New `scripts/rejection_decoder.py`: a stdlib-only
  CLI that matches pasted rejection email text to the
  sections of ref 07 and prints fix checklist pointers.
  Keyword matching only, with a clear note that it
  guesses from wording and the user must read the
  actual email. Tested with sample inputs.
- `references/11-official-sources.md` gains the
  Search Central helpful-content, spam policies, and
  generative AI pages, the AI guidance blog, and the
  AdMob signup, mediation, app-ads.txt, and families
  policy pages.

## 1.9.0 — 18 November 2026

- New `references/37-india-publishers-guide.md`: wire
  transfer as the only payment method offered in India,
  verified on the live Help country table on
  18 November 2026, USD thresholds, PIN delivery notes,
  tax form and PAN guidance, and DPDP Act 2023 consent
  basics. Tax and legal points are labelled general
  information with a professional check, and secondary
  figures are labelled reported.
- New `references/38-wordpress-and-site-kit-setup.md`:
  the hands-on companion to ref 19. Site Kit setup
  steps, manual placement, live verification, caching
  pitfalls, and theme problems, verified against the
  live AdSense Help page on 18 November 2026.
- New `references/39-account-tools-after-approval.md`:
  Ad Review Center operation, blocking controls in
  narrowest-first order, site-level blocking, and
  reports orientation, verified on live Help pages on
  18 November 2026. Strategy stays in refs 14 and 26.
- New `docs/hinglish-quick-start.md`: a Roman Hinglish
  quick-start guide with no new factual claims.
- New `docs/staying-updated.md`: how to watch official
  channels, verify claimed changes, and distrust rumour
  patterns.
- `references/11-official-sources.md` gains the payment
  methods page, the Site Kit page, the blocking guide,
  and the Ad Review Center pages.

## 1.8.1 — 17 November 2026

- `references/01-history-timeline.md`: the identity
  verification entry now rests only on what was read
  directly on the live Help page. The step itself is
  official. The June 2026 rollout date is labelled as
  reported, not as read on the page.

## 1.8.0 — 17 November 2026

- New `references/34-supported-languages.md`: the full
  official supported language list read live on the
  AdSense Help page on 17 November 2026, with the
  interface footnotes, the rule against ad code on pages
  primarily in an unsupported language, and practice
  guidance for multilingual and Roman-script content.
- New `references/35-page-experience-and-core-web-vitals.md`:
  Core Web Vitals definitions, thresholds, and the 75th
  percentile field method, the six page experience
  questions, and an explicit boundary that these are
  Search signals, not AdSense approval rules.
- New `references/36-affiliate-content-and-disclosure.md`:
  the official thin affiliation definition, link
  qualification with rel=sponsored and rel=nofollow,
  regulator disclosure rules kept separate from Google
  rules, and a fix checklist.
- Identity verification upgraded from reported to
  official in `references/01-history-timeline.md` and
  `references/16-verification-and-payments-troubleshooting.md`:
  the 45-day window, the ID plus video selfie process,
  the 5 to 10 minute duration, the biometric opt-out
  with 2 to 3 business day manual review, document and
  selfie tips, and re-reviews, all read on the live
  AdSense Help page on 17 November 2026.
- `references/02-eligibility-and-application.md` gains
  the official 6-month account setup deadline and the
  live site with enough content requirement, read on the
  live AdSense Help page on 17 November 2026.
- `references/11-official-sources.md` gains nine new
  official pages: languages, unsupported languages,
  account setup, online identity verification, spam
  policies, outbound link qualification, page
  experience, Core Web Vitals, and web.dev Web Vitals.
- `scripts/deep_audit.py` gains three checks. The
  X-Robots-Tag response header is checked for noindex
  on the homepage and every crawled page, since a header
  noindex is invisible in the page HTML. Affiliate links
  are counted and cross-checked against disclosure
  wording and sponsored or nofollow qualification, as
  practice heuristics. Pages with no internal outlinks
  are flagged as navigation dead ends. The JSON output
  gains x_robots_tag, affiliate_links, and
  internal_outlinks fields.
- `scripts/deep_audit.py` also fixes a crash on sitemaps with
  date-only lastmod values. Such values are valid sitemaps,
  but the freshness math mixed timezone-aware and naive
  datetimes and raised a TypeError. Date-only values are
  now treated as UTC.
- `references/23-approval-clone-audit.md` and
  `references/31-approval-check-matrix.md` document the
  three new checks and their heuristic status.
  `docs/contents.md` and `docs/installation.md` updated
  for 36 reference files.

## 1.7.1 — 17 November 2026

- `scripts/deep_audit.py` now prints progress to stderr
  while it fetches pages and verifies links and images,
  so a long verification stage never looks stuck. The
  report file stays clean: progress lines never enter
  the `--output` report.

## 1.7.0 — 17 November 2026

- `scripts/deep_audit.py` now checks in parallel: 8
  workers by default fetch pages, run the site-level
  checks, and verify links and images at the same time.
  The report still reads in sitemap order, and results
  are identical to a sequential run. New `--workers`
  option: use 1 or 2 for fragile shared hosting.
- `references/23-approval-clone-audit.md` and
  `docs/audit-scripts.md` document the new option.

## 1.6.1 — 17 November 2026

- README trimmed to a minimal landing page: banner,
  badges, one-line pitch, a single row of guide links,
  the workflow diagram, quick start, and the honesty
  note. The terminal preview moved to
  `docs/audit-scripts.md`.

## 1.6.0 — 17 November 2026

- New `docs/` guides, each a separate page linked from
  the README: installation, understanding, usage,
  audit scripts, FAQ, contents, and contributing.
- README rewritten as a clean landing page: animated
  banner, animated workflow diagram, animated terminal
  preview, badges, and links to every guide. The full
  file table moved to `docs/contents.md`.
- New `assets/` animated SVG images: banner, workflow,
  and terminal preview. CSS keyframe animation, no
  JavaScript, no external services.

## 1.5.0 — 17 November 2026

- New `references/33-unpublished-review-signals.md`:
  the signals rejection patterns suggest a reviewer
  weighs, grouped into identity and trust, content
  depth, freshness and activity, navigation and
  completeness, technical quality, monetisation
  hygiene, and account and traffic shadows. Every
  signal is labelled INFERRED and is never taught as
  a confirmed Google rule.
- `scripts/deep_audit.py` new checks: homepage noindex
  failure, Search Console verification signal,
  homepage content links, current year staleness,
  thin trust pages, favicon coverage, social platform
  links, email links on the Contact page, comment and
  related-content markers, nofollow counts, updated
  markers, internal link depth averages, ads.txt
  RESELLER counts, and image file sizes over 1 MB
  from Content-Length. New fields flow into the JSON
  report.
- `scripts/site_audit.py`: homepage noindex is now a
  failure in the quick check.

## 1.4.0 — 17 November 2026

- `scripts/deep_audit.py` version 2: the approval clone now
  covers the full checkable surface. New site-level checks:
  HTTP to HTTPS redirect, alternate host consistency,
  response time and security headers, robots.txt AdSense
  crawler and sitemap checks, ads.txt line validation with
  publisher ID format and certification ID, soft 404
  detection, feed and pagination presence, sitemap lastmod
  freshness, and consent platform and ad network markers.
  New per-page checks: article-only word counts, H2 counts,
  empty H1s, title word repetition, description identical
  to title, HTML lang, charset, Open Graph and Twitter
  tags, missing canonical, image dimensions, ad slot
  counts, popup and modal markers, trust-page links per
  page, and copyright-risk signals. New cross-page checks:
  near-duplicate article text by shingle similarity,
  external link verification with unverified states,
  same-origin image verification, a labelled heuristic
  readiness score, and a machine-readable JSON report
  with `--json`.
- `scripts/site_audit.py`: HTML lang, favicon, consent
  markers, HTTP to HTTPS redirect, soft 404, robots.txt
  AdSense crawler and sitemap checks, and ads.txt line
  validation.
- New `references/31-approval-check-matrix.md`: every
  approval check in three groups, automated, script
  flagged human decided, and no script can check, with an
  honest statement that no tool matches Google's decision
  100 percent.
- New `references/32-hidden-deep-approval-checks.md`:
  the three layers of the review, what Google confirms,
  what rejection patterns suggest, and what stays hidden
  inside Google, with the deep trust checks the script
  now runs for each layer it can see.
- Deep trust checks in `scripts/deep_audit.py`: About
  page depth, Contact page form presence, content
  freshness and history span from sitemap dates, orphan
  pages, sitemap coverage, duplicate H1 texts, canonical
  collisions, date and author signal summaries, sponsored
  link counts, word count distribution, homepage
  structure, and thin category and tag pages.
- `scripts/deep_audit.py` reliability fixes: truncated
  responses are retried even when the server sends no
  Content-Length, truncated sitemap bodies are refetched
  instead of silently dropping URLs, sitemap files that
  still fail after retries are reported as a warning so
  an incomplete crawl is never silent, pages that return
  200 with an empty body are treated as failed reads,
  the title repetition flag ignores common stopwords,
  and images that return no HTTP response are reported
  as unverified rather than broken.
- `references/23-approval-clone-audit.md` rewritten for
  version 2, with the new options and thresholds.
- `SKILL.md` audit workflow updated for version 2 and the
  check matrix.

## 1.3.0 — 17 November 2026

- Seven new advanced reference files: ad serving limits and
  enforcement levels (verified against the live AdSense Help
  page, including the two causes, the typical less than 30
  days figure, and automatic review), invalid traffic
  defense (source audit, early warning signals, click
  bombing response), advanced reporting and experiments
  (segmentation method, experiments workflow, blocking
  controls, Auto ads controls, and a labelled report of a
  begin-to-render impression counting change), account
  architecture and graduation (one account per payee,
  locked country and account type, multi-site rules, Ad
  Manager and MCM delegation types), payments tax and edge
  cases (holds one by one, tax forms and withholding,
  final payment rules, country moves, deceased payee),
  advanced technical implementation (ads.txt at scale,
  sellers.json, consent debugging, page experience, the
  refresh ban, single-page apps, AMP, crawler access), and
  advanced decision playbooks (ten hard situations with
  checks, actions, and stop rules).
- Two new examples: a dated ad serving limit action plan
  log, and an advanced monthly review checklist.
- `SKILL.md` gains an advanced account situations workflow
  covering all seven new references and both new examples.
- `references/11-official-sources.md` gains the ad serving
  limits page, the limited ad serving vs limited ads page,
  the ad coverage troubleshooting page, and the ad
  placement policies page.
- Secondary figures in the new references (MCM thresholds,
  final payment timing, withholding rates, Ad Manager
  Small Business qualification) are labelled reported, with
  the live pages and the account's own figures stated as
  the authority.

## 1.2.0 — 17 November 2026

- New `scripts/deep_audit.py`: an approval-clone crawler that
  walks the sitemap and checks every page point by point —
  titles, descriptions, H1s, word counts, image alt text,
  canonicals, noindex flags, mixed content, placeholder text,
  duplicate titles and descriptions, and internal link
  verification — plus trust pages and Privacy disclosure
  keywords. Read-only, Python standard library only. Review
  phrases match on word boundaries (so "specialist" never trips
  a drug-name flag) and canonical comparison ignores URL
  encoding differences, both fixed after the first live run
  against thegroundzerofit.com.
- New `references/23-approval-clone-audit.md`: the clone method,
  the reviewer simulation workflow, and an honest list of what no
  crawler can judge. Script thresholds are labelled as practice
  and heuristics, never as Google rules.
- `SKILL.md` audit workflow now runs the deep audit after the
  quick checker.

## 1.1.1 — 17 November 2026

- `scripts/site_audit.py`: the title parser now reads only the
  first `<title>` element. SVG `<title>` elements inside page
  icons (for example a cookie banner's "Powered by" logo) no
  longer get appended to the reported homepage title. The live
  thegroundzerofit.com title was always clean; the "CookieAdmin
  CookieAdmin" suffix was a script bug, now fixed and verified.
- `scripts/site_audit.py`: the fetcher now reads in chunks and
  keeps the partial body when a host closes the connection early
  (IncompleteRead), instead of failing the whole check. Found on
  the same live run against thegroundzerofit.com.

## 1.1.0 — 17 November 2026

- Eleven new reference files complete the zero-to-advanced
  coverage: mistakes encyclopedia, ad formats and placement,
  optimization and revenue, Policy Center and appeals,
  verification and payments troubleshooting, YouTube and other
  products, consent and privacy deep dive, platform setup guides,
  troubleshooting index, traffic and SEO basics, and learning
  paths with FAQ.
- Two new examples: a Privacy Policy outline to adapt, and a
  fact-based policy appeal outline.
- `SKILL.md` gains workflows for formats, optimization, appeals,
  verification, YouTube, consent, platform setup, troubleshooting,
  traffic, and learning paths.
- `references/11-official-sources.md` gains the verified YouTube
  Partner Program eligibility page and the invalid traffic appeal
  form link. YouTube thresholds are now verified against the
  official Help page, not labelled unverified.
- Figures that come from secondary sources (identity verification
  window, PIN timing, tax withholding rates) are labelled
  reported, with the account's own shown deadlines and figures
  stated as the authority.

## 1.0.1 — 17 November 2026

- `scripts/site_audit.py`: retry each fetch once after a transient
  failure, and distinguish a real HTTP 404 ("not found") from a fetch
  that could not be verified. A flaky host no longer produces a false
  "no robots.txt" warning, as found on the first live run against
  thegroundzerofit.com.

## 1.0.0 — 17 November 2026

- First release.
- `SKILL.md` plus `skill.yaml` (Muse descriptor, Agent Skills
  frontmatter in `SKILL.md`).
- Eleven reference files: history timeline (2003 to 2026), eligibility
  and application, Publisher Policies, Publisher Restrictions, Program
  policies (clicks, traffic, placement, privacy), terms and payments,
  rejection reasons and fixes, pre-apply checklist, content quality
  guide, glossary, and official sources.
- Read-only site readiness checker in `scripts/site_audit.py`
  (Python standard library only).
- Audit report template in `examples/`.
- Official pages verified against live Google Help pages in
  November 2026. Recent unverified claims (for example a reported
  photo-ID step) are labelled unverified, not taught as rules.
