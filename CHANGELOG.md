# Changelog

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
