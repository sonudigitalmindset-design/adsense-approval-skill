# Changelog

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
