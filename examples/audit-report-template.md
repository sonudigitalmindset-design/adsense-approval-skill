# Example audit report template

Copy this file, fill it in from a real audit, and keep one copy per
site and date. Never copy the example findings below into a real
report: they are placeholders showing the format.

---

# AdSense readiness audit

- Site:
- Audit date:
- Auditor:
- Script output: `python3 scripts/site_audit.py <site>` (paste or attach)

## Verdict

- [ ] Ready to apply
- [ ] Not ready yet (blockers below)

Reason in one sentence:

## Blockers (must fix before applying)

1. URL:
   Finding:
   Rule (official page):
   Fix:

## High risks (fix before applying where possible)

1. URL:
   Finding:
   Rule:
   Fix:

## Small fixes (fix when convenient)

1. URL:
   Finding:
   Fix:

## Content decisions

| URL | Decision (keep / improve / merge / delete) | Reason |
|-----|--------------------------------------------|--------|
|     |                                            |        |

## Policy checks

- [ ] Prohibited content audit done (`references/03-publisher-policies.md`)
- [ ] Restricted content audit done (`references/04-publisher-restrictions.md`)
- [ ] Traffic and placement audit done (`references/05-program-policies-ads-traffic.md`)
- [ ] Privacy disclosure checked against the live site's real tools

## Next steps

1.
2.

## Reapplication log

| Date | Action | Result |
|------|--------|--------|
|      |        |        |
