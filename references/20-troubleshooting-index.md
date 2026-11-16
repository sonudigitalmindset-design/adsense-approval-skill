# Troubleshooting index

Symptom, likely cause, and first check. Work top to bottom inside
each entry. When a fix is not listed, read the linked reference and
the live Help page for that exact message.

## Ads and code

1. Ads show as blank space.
   Likely cause: code placed but the site is still under review, an
   ad blocker is running, or the unit has no fill yet.
   First check: open the page in a private window with no blocker,
   confirm the site status in AdSense, and wait a day after a new
   unit is created.
2. AdSense code not detected.
   Likely cause: code missing from the live page, cached old page,
   or code in a template that does not render.
   First check: view live page source, clear all caches, and
   confirm the code is in the head of pages that get views.
3. Auto ads show too many ads.
   Likely cause: all formats enabled with no exclusions.
   First check: turn off formats the page does not need, exclude
   areas and pages, and preview on a phone.
4. Auto ads show too few ads.
   Likely cause: low content per page, exclusions that cover too
   much, or a new site with little traffic.
   First check: review exclusions and format settings, and add
   content before adding units.
5. Ads appear on pages where they should not.
   Likely cause: Auto ads run site-wide with no page exclusions.
   First check: add the pages to the Auto ads exclusion list.
6. Ads.txt unauthorised warning in the account.
   Likely cause: file missing, wrong publisher ID, file not at the
   root, or crawler has not rechecked yet.
   First check: open the live ads.txt URL, compare the line with
   the account, and wait a day after fixing. See
   `19-platform-setup-guides.md`.
7. Earnings dropped suddenly.
   Likely cause: traffic drop, seasonality, a policy flag, ad
   serving limited, or a broken layout after a theme change.
   First check: Policy Center, then reports by page and country,
   then recent site changes. See
   `14-optimization-and-revenue.md`.

## Application and review

8. Site under review for weeks.
   Likely cause: review queue, or the site changed during review.
   First check: confirm the verification code is still in place and
   the site is live. Reviews usually take a few days and sometimes
   2 to 4 weeks. Do not remove and re-add the site.
9. Rejected for low value content.
   Likely cause: whole-site judgement on thin, copied, or
   unoriginal pages.
   First check: audit every indexable URL, then fix or remove weak
   pages before reapplying. See
   `07-rejection-reasons-and-fixes.md`.
10. Rejected for policy violation.
    Likely cause: a named policy on a named page or site-wide.
    First check: read the exact reason, remove the violating
    content entirely, and check the rest of the site for the same
    issue.
11. Duplicate account error.
    Likely cause: an AdSense account already exists for the payee.
    First check: sign in with the original account, or close the
    old account properly before applying again. Never hold two.
12. Site already connected to another account.
    Likely cause: a previous owner or an old account holds the
    site.
    First check: remove the site from the old account, or use the
    account that already holds it.

## Policy and enforcement

13. Policy Center flag on one page.
    Likely cause: content or placement on that URL.
    First check: open the URL, fix the root cause, then request
    review from the Policy Center. See
    `15-policy-center-and-appeals.md`.
14. Ad serving limited for invalid traffic.
    Likely cause: suspicious traffic pattern or risky placements.
    First check: traffic sources and referrers, paid traffic, and
    accidental-click risks. Keep a written record.
15. Account disabled.
    Likely cause: invalid traffic or policy violation at account
    level.
    First check: read the full email and Policy Center notice, then
    prepare one careful appeal with evidence. See
    `15-policy-center-and-appeals.md`.

## Verification and payments

16. Identity verification failed.
    Likely cause: name mismatch, wrong document country, glare,
    blur, or expiry.
    First check: fix the payments profile name first, then submit
    one clean document. Do not burn attempts on the same photo. See
    `16-verification-and-payments-troubleshooting.md`.
17. PIN letter never arrived.
    Likely cause: wrong address, postal delay, or PIN not yet
    mailed.
    First check: confirm the address, wait about 3 weeks, then
    request a new PIN. Requests are limited.
18. Payment on hold.
    Likely cause: identity, PIN, tax info, payment method, or a
    self-set hold.
    First check: the account home page lists each open action.
    Complete them in order.
19. Tax form rejected.
    Likely cause: name or TIN mismatch, wrong form type, or
    incomplete treaty claim.
    First check: match the form name to the payments profile and
    the TIN to the official document, then resubmit.
20. Payment returned by the bank.
    Likely cause: wrong account number, SWIFT code, or name
    mismatch.
    First check: confirm details with the bank, fix the payment
    method, and wait for the next cycle.
21. Balance below threshold for months.
    Likely cause: low traffic or low-value traffic, not a fault.
    First check: reports by page and country, then the traffic and
    content work in `21-traffic-and-seo-basics.md`. The balance
    rolls forward. It is not lost.

## YouTube

22. YouTube Studio step 2 stuck on AdSense.
    Likely cause: a second account, a country mismatch, a name
    problem, or a disabled AdSense account.
    First check: the AdSense account status and the email from
    AdSense. Fix the AdSense side first. See
    `17-youtube-and-other-products.md`.
23. Channel meets thresholds but YPP review fails.
    Likely cause: reused content or monetisation policy issues.
    First check: remove or transform reused material, add original
    value, and reapply after real changes.

## Consent

24. No consent banner shows for EEA visitors.
    Likely cause: no CMP message published, or the message targets
    the wrong site.
    First check: Privacy and messaging in the account, message
    status, and targeting. Test from an EEA location. See
    `18-consent-and-privacy-deep-dive.md`.
25. Two cookie banners appear at once.
    Likely cause: a site banner plus the CMP banner.
    First check: keep one consent flow for advertising. Disable
    the site banner for regulated regions or remove it.
