# Advanced reporting and experiments

Beginner optimization watches total earnings. Advanced work
segments reports until the story appears, tests one change at
a time, and treats blocking controls as brand safety tools.
This reference explains the reporting method, the experiments
workflow, and the honest limits of every lever.

Read the basics first in
`references/14-optimization-and-revenue.md`. Read the traffic
defense method in `references/25-invalid-traffic-defense.md`
before acting on any anomaly found in reports.

## The metrics that matter, defined once

- Impressions. Ad requests that produced a counted ad
  impression. Counting methodology can change, so compare
  impressions only within the same methodology period.
- Clicks. Genuine user clicks on ads. Clicks from invalid
  traffic are deducted, so estimated earnings can fall even
  when clicks look high.
- Click through rate (CTR). Clicks divided by impressions.
  A sudden CTR jump is an investigation signal, not a win.
- Cost per click (CPC). Average earnings per click. CPC
  reflects advertiser demand for the audience and topic, not
  publisher effort alone.
- Page RPM. Estimated earnings per 1,000 page views. The
  best single number for comparing pages, because it folds
  fill, clicks, and CPC together.
- Impression RPM. Estimated earnings per 1,000 ad
  impressions. Useful for comparing ad units and placements
  on the same pages.
- Estimated earnings. Not finalised earnings. Deductions for
  invalid traffic and adjustments can reduce the finalised
  figure. Judge months by finalised earnings, and days by
  direction, not by exact cents.

Never quote a third-party RPM benchmark as a fact. RPM varies
by niche, country mix, season, device mix, consent state, and
demand. The only honest benchmark is the site's own history.

## Segment before you conclude

A total that falls can hide a page that rose. Segment every
important question by at least one dimension before acting.

- By page URL. Find pages with high impressions and low page
  RPM, and pages with high CTR. Low RPM pages may have
  consent gaps, weak demand for the topic, or poor placement.
  High CTR pages may have accidental click risk. Check both
  kinds by opening the page as a visitor.
- By country. Country mix drives CPC more than any placement
  tweak. A traffic shift toward lower demand countries lowers
  RPM without any policy problem. Do not chase geography with
  VPN schemes or bought traffic. See
  `references/25-invalid-traffic-defense.md`.
- By device. Mobile and desktop behave differently. A
  placement that works on desktop can cover content or sit
  in a tap path on mobile. Check every change on a phone
  sized view.
- By ad unit and format. Compare units on similar pages.
  A unit that earns little may be below the fold on a page
  nobody scrolls, or on a page with weak demand.
- By date, same period last year. Demand moves seasonally.
  A dip that matches last year's dip is usually demand, not
  a penalty. A dip with no seasonal match needs the checks
  in `references/24-ad-serving-limits-and-enforcement-levels.md`.

## Experiments: test one variable at a time

AdSense Experiments let a publisher A/B test ad settings,
for example Auto ads on versus off, or one ad load setting
against another. The workflow matters more than the tool.

- State the question in one sentence. "Does a lower ad load
  keep earnings while improving experience?" is a question.
  "Make more money" is not.
- Change one variable. One setting, one format, one
  placement. Two changes at once make the result unreadable.
- Run long enough for a real sample. Small sites need weeks,
  not days. Ending early on a lucky day produces a false
  winner.
- Judge by total earnings and user experience together.
  A setting that raises earnings and raises bounce rate or
  covers content is a short term win and a long term risk.
- Record the winner, the dates, the traffic level, and the
  result. Then test the next variable. A log of tested
  changes beats a memory of hunches.

Find the current Experiments controls in the Optimization
section of the AdSense account, and verify the exact steps
on the live Help page before running a test. Console layout
changes, and this reference does not freeze it.

## Blocking controls: brand safety, not a revenue lever

Blocking controls let a publisher block advertiser URLs,
general ad categories, sensitive categories, and ad networks.
They exist to protect the brand and the audience, not to
raise earnings.

- Block a category or advertiser only for a brand or audience
  reason, for example a category that clashes with the site's
  values or upsets readers.
- Every block removes demand. Broad blocking lowers fill and
  CPC, because fewer advertisers compete for the space.
- Review blocks every few months. A block set during a
  launch panic can quietly cost earnings for a year.
- Never block categories to "force" higher paying ads. That
  is not how the auction works, and the usual result is
  lower earnings, not higher.

## Auto ads advanced controls

Auto ads place formats automatically, but the publisher still
controls the shape of the result.

- Ad load. The ad load setting trades ad quantity against
  user experience. More ads do not always mean more earnings,
  because heavy pages lose readers and invite accidental
  clicks. Test ad load with an experiment, not by feel.
- Format toggles. Anchor, vignette, side rail, in-page, and
  multiplex formats can be switched on or off individually.
  A format that annoys readers on one niche can work well
  on another. Judge by earnings plus bounce and scroll
  behaviour, not by earnings alone.
- Page exclusions. Pages that should never carry ads, such
  as login, checkout, thank you, and policy pages, can be
  excluded. Excluding low value pages also keeps the account
  focused on pages that earn honestly.
- Vignette behaviour. Vignette ads show on navigation between
  pages. If readers complain about interruptions, test the
  format off before assuming it is harmless.

## A note on impression counting changes

Google changes how impressions are counted from time to time
to match industry measurement standards. A move to
begin-to-render counting, where an impression counts only
when the ad has loaded and begun to render, has been reported
for February 2027 from a Google email shared publicly. This
is reported, not verified against a live Help page at the
time of writing. Verify the current methodology on the live
Help page before explaining an impression drop.

The practical lesson survives any single change. When
impressions fall but traffic, earnings, and RPM hold steady,
suspect a measurement change before suspecting a penalty.
When impressions and earnings fall together, run the checks
in `references/24-ad-serving-limits-and-enforcement-levels.md`.

## The monthly review cadence

Run the monthly review in
`examples/advanced-monthly-review-checklist.md`. The short
form is: Policy Center first, then reports by page, country,
and device, then blocking controls, then ads.txt and consent
checks, then one experiment decision. One focused hour a
month catches most problems while they are still small.
