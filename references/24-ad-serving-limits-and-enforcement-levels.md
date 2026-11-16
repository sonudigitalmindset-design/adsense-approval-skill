# Ad serving limits and enforcement levels

An ad serving limit is not the same as a closed account. It is a
temporary cap on how many ads Google shows on an account while
traffic quality is assessed or while invalid traffic concerns are
reviewed. This reference explains the levels of enforcement, what
each notice means, and what to do while a limit is in place.

Read the enforcement basics first in
`references/15-policy-center-and-appeals.md` and the traffic rules
in `references/05-program-policies-ads-traffic.md`.

## What an ad serving limit is

Google's Help page on ad serving limits states the definition in
one sentence. Google may sometimes place a limit on the number of
ads an AdSense account can show. The limit has two causes.

- Account being assessed. Ad serving is temporarily limited while
  Google assesses traffic quality. Google reviews and updates the
  limit automatically as it monitors traffic. Google states it
  cannot say how long this assessment will take.
- Invalid traffic concerns. Ad serving is limited because Google
  identified invalid traffic concerns in the account. Google
  reviews and updates the limit automatically as it monitors
  traffic, and encourages the publisher to make sure ad traffic
  complies with the AdSense Program policies.

Three facts from the same Help page matter for every decision.

- The limit typically impacts publishers for less than 30 days,
  but it may take longer in some cases. Thirty days is a typical
  figure, not a deadline and not a promise.
- The account stays fully accessible during a limit. Reports,
  payment settings, and site management keep working. Details of
  the account level enforcement appear in the Policy Center.
- If Google detects invalid activity or other issues during the
  limit, the account may face further enforcement or permanent
  closure. A limit is a warning state, not a safe state.

The Help page describes automatic review. It does not describe a
button, form, or request path to ask for a faster lift. Advice
that promises a manual lift, a support shortcut, or a fixed
removal date is not supported by Google's own documentation.

## Limited ad serving is not limited ads

Two similar phrases mean different things. Google's Help page
"Limited ad serving vs. limited ads" separates them.

- Limited ad serving caps how many ads show on an account. It is
  the limit described above.
- Limited ads (LTD) restrict what data can be used to serve ads.
  Limited ads disable the collection, sharing, and use of personal
  data for ad personalisation. Limited ads appear where consent
  is missing or declined, and where regulation requires it.

A publisher can have both at once: a cap on ad volume and a
restriction on personalisation. Check which one applies before
acting, because the fixes are different. Limited ad serving is
answered with traffic quality work. Limited ads are answered
with consent work in `references/18-consent-and-privacy-deep-dive.md`.

## The enforcement ladder

Enforcement rises in steps. Each step is wider than the last.

- Page level. Ad serving stops on one page or a small set of
  pages. The rest of the site keeps serving. Fix the flagged
  pages before the deadline shown in the Policy Center.
- Site level. Ad serving stops on one whole site. Other sites on
  the same account keep serving. Fix the site, then request a
  review from the Policy Center where the notice offers one.
- Account level. Ad serving is limited or stopped across the
  whole account. This is where ad serving limits sit, and where
  suspensions sit.
- Account closure. The account is disabled. For invalid traffic,
  one appeal form exists and further appeals may not be
  considered after a decision. For policy violations, the notice
  states whether an appeal path exists.

A page level flag that is ignored can grow into a site or account
level action. The cheapest fix is always at the lowest level,
fixed early.

## What to do while a limit is in place

Work through this list in order. Keep a dated log of every
change, using `examples/ad-serving-limit-action-plan.md`.

- Read the exact Policy Center wording. Note whether it says
  "account being assessed" or "invalid traffic concerns", the
  date it appeared, and any deadline shown. Do not guess the
  cause from earnings alone.
- Audit traffic sources for the two weeks before the limit.
  Check referrers, countries, devices, and new sources in
  Analytics. Look for sudden spikes, single-source surges, and
  traffic that arrived just before the limit started. Read
  `references/25-invalid-traffic-defense.md` for the full audit.
- Stop every risky source at once. Pause paid promotion, traffic
  services, social automation, and any new source you cannot
  vouch for. Do not buy traffic to "prove" quality. New
  unvetted traffic during a limit makes assessment harder.
- Check placements for accidental click risk. Remove ads near
  navigation, download buttons, pagination, and game controls.
  Read the placement rules in
  `references/13-ad-formats-and-placement.md`.
- Check that no one on the team clicks ads or tests with live
  ad code. Use Google's publisher toolbar preview or test
  pages without live code where the console offers them, and
  never click a live ad to check it works.
- Keep publishing useful content and keep the ad code in place.
  The Help page does not ask publishers to remove code during
  a limit, and removing the site or re-adding it does not
  speed review.
- Do not open a second account. One account per payee is a
  Program policy rule, and a second account during a limit
  creates a circumvention problem on top of the original one.
- Wait for the automatic review. Check the Policy Center once
  a week for a status change, not every hour. If the limit
  passes 30 days, keep the log going and keep traffic clean.
  There is no published escalation that shortens the wait.

## What not to do during a limit

- Do not submit the invalid traffic appeal form for a limit.
  The form is for disabled accounts. A limited account is not
  disabled, and the Help page for limits describes automatic
  review, not an appeal.
- Do not remove and re-add the site, change the payee, or
  create a new payments profile to escape the limit. These
  moves do not reset traffic history and can create new
  verification problems.
- Do not pay anyone who promises to lift a limit. No third
  party can change Google's traffic assessment.
- Do not change many things at once and then claim one of
  them fixed it. Change risky sources first, then placements,
  then nothing. A clean log beats a busy log.

## Telling a limit apart from other low fill causes

Earnings can fall without a limit. Before assuming a limit,
check each of these.

- Policy Center. A limit shows as an account level issue. No
  issue there means the cause is elsewhere.
- ads.txt. A missing or wrong publisher line can cut demand.
  Check the live ads.txt file and compare the line with the
  account. See `references/19-platform-setup-guides.md`.
- Consent. Missing or broken consent handling in the EEA, the
  UK, or Switzerland produces limited ads and lower fill. See
  `references/18-consent-and-privacy-deep-dive.md`.
- Crawler access. If the AdSense crawler cannot reach pages,
  ads may not serve well. Do not block the AdSense crawler
  (Mediapartners-Google) in robots.txt. See `references/29-advanced-technical-implementation.md`.
- Seasonality and demand. Advertiser demand moves through the
  year. Compare with the same period last year before calling
  a normal dip a penalty.
- Measurement changes. Google changes how impressions are
  counted from time to time. A reported move to begin-to-render
  counting is noted in
  `references/26-advanced-reporting-and-experiments.md`. Judge
  by earnings and RPM trends, not by raw impression counts
  alone.

## When a limit lifts

When the Policy Center clears the issue, do not celebrate by
adding aggressive placements or new traffic sources the same
day. Reintroduce one change at a time, watch reports for two
weeks, and keep the traffic log running. Google states it may
put a limit back if issues return or if it lacks enough
information to judge. A limit that lifted once can return.

## Sources

- Ad serving limits, AdSense Help:
  https://support.google.com/adsense/answer/9437976?hl=en
- Limited ad serving vs. limited ads, AdSense Help:
  https://support.google.com/adsense/answer/14668281?hl=en
- Troubleshoot ad coverage issues, AdSense Help:
  https://support.google.com/adsense/answer/16906718?hl=en

Recheck these pages before quoting a duration or a procedure.
The pages win over this reference when they disagree.
