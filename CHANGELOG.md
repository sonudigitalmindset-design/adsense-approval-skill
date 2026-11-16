# Changelog

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
