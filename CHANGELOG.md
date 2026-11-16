# Changelog

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
