# Account tools after approval

What to use inside an approved AdSense account: the Ad
Review Center, blocking controls, and reports. This file
is the operational guide. The strategy behind blocking
and reporting lives in
`references/14-optimization-and-revenue.md` and
`references/26-advanced-reporting-and-experiments.md`.
Read those before changing anything. This file does not
repeat their method.

Everything here applies after approval. None of it helps
an application. Do not touch these tools to "improve
approval odds". They only affect ads that are already
serving.

## Ad Review Center

OFFICIAL, read on the live AdSense Help pages "Ad review
center overview" and "AdSense guide to allow and block
ads on your site" on 18 November 2026
(`support.google.com/adsense/answer/13547173` and
`support.google.com/adsense/answer/180609`). The enable
and review steps come from the official follow-on pages
in the same Help section
(`support.google.com/adsense/answer/13546846` and
`support.google.com/adsense/answer/13547859`), read via
search results on 18 November 2026.

What it is: the Ad Review Center lets the publisher
review individual ads after they have appeared on the
site, and choose whether to keep showing them. It gives
transparency and control over single creatives. It is
the most precise blocking tool and the right first step
for one problem ad.

Where it lives: Brand safety in the AdSense account.
Choose the product (for example Content for AdSense for
Content ads), then Ad review center.

Enable it:

1. Sign in to the AdSense account.
2. Click Brand safety.
3. Click the product.
4. Click Ad review center.
5. Click Enable. Reviewing can start in about an hour.
   At first only ads shown since enabling appear. Over
   the next day or two, more ads appear.

How reviewing works:

- The list shows unreviewed ads that appeared in the
  last 30 days. Ads must have received at least a small
  number of impressions to be eligible for review.
- Sort by impressions to see the ads that matter most.
  Check the impression count before blocking, to
  understand the impact.
- Click an ad for the detail view: a full size preview,
  size, type, destination URL, Google Ads account, and
  related ads.
- Search by text or filter by status, ad network, and ad
  type. Search by image is also offered: upload a single
  PNG file under 3 MB to find and block an ad from its
  image.
- Mark an ad as reviewed to keep showing it without
  reviewing it again. Select all on a page marks the
  whole page as reviewed.
- Block an ad to stop it appearing again. Ads are
  blocked by creative ID. The status changes to
  Blocked. Blocking can be undone.

Limits that surprise publishers:

- Blocking in the Ad Review Center works at the product
  level, not on a site-by-site basis. A block applies
  across the product.
- There may be a delay of up to 24 hours between
  blocking an ad and the ad no longer being eligible to
  run on the site.
- An ad blocked by advertiser URL or by category may
  still appear in the Ad Review Center. The list shows
  all ads with enough impressions in the last 30 days,
  including old impressions from before the block. Such
  ads move down the list as their impressions age out.
- The Ad Review Center does not support all AdSense
  products. Check the account for what is offered.
- Creatives from the Ad Review Center may be reviewed
  and stored as required by applicable laws and
  regulations. All other uses are prohibited, including
  using creatives to train machine learning models.

Reporting a bad ad: if an ad violates Google policies,
report it in the Ad Review Center (block and report) or
through the Google Ads report-an-ad form. Reporting is
separate from blocking. A policy-violating ad should be
reported, not only blocked.

## Blocking controls

OFFICIAL, from the same Help guide read live on
18 November 2026. Google's own advice: use ad blocking
sparingly, and start with the control that blocks the
fewest ads first. Allowing all ads creates the most
competitive auction. Every block removes bidders.

The controls, narrowest first:

1. Individual ads, in the Ad Review Center. See above.
2. Advertiser URLs. Block all ads that point to a
   specific advertiser, for example a direct competitor.
   Enter the domain. This is the most precise broad
   control.
3. Sensitive categories. Block ads on sensitive topics
   such as Religion, Politics, and References to Sex
   and Sexuality. Sensitive category blocking is
   available for ads in a limited set of languages,
   regardless of the language of the site. A block does
   not guarantee such ads never appear.
4. General categories. Block broad industry groups such
   as Apparel, Internet, Real Estate, and Vehicles. The
   same limited-language caveat applies.
5. Authorized buyers. The Authorized Buyers page shows
   which buyers bid on the site's inventory. Bidding
   controls there allow or block specific buyers.
6. Ad format and auction behaviours. Controls include
   blocking user-based ads and allowing additional ad
   technology vendors. Read the ad serving settings page
   in the account before changing these.

Site-level blocking: with multiple sites, advertiser
URL, general category, and sensitive category blocks
can be set per site instead of across all sites. This
is called site-level blocking. It applies only to
AdSense for Content ads, only to those three control
types, and only one site at a time. Sites must be made
available for site-level blocking through the site
management feature. Use it when one site needs a
different blocking strategy from another, for example a
children's site and a sports site under one account.

Review blocks regularly. A block set in a launch panic
can quietly cost earnings for months. See
`references/26-advanced-reporting-and-experiments.md`
for the review cadence and the brand safety framing.

## Reports basics

Reports live in the AdSense account under Reports.
This section is the orientation only. The method is in
`references/26-advanced-reporting-and-experiments.md`
and the metric definitions are in
`references/14-optimization-and-revenue.md`.

- Start with the default report: estimated earnings,
  page views, impressions, clicks, and page RPM over
  time.
- Segment before concluding. A total that falls can
  hide a page that rose. The useful first segments are
  page URL, country, and device.
- Estimated earnings are not finalised earnings.
  Deductions for invalid traffic and adjustments can
  reduce the finalised figure. Judge months by
  finalised earnings.
- A sudden CTR jump is an investigation signal, not a
  win. Check the page for accidental click risk and
  check traffic sources before celebrating.
- Save the report views used every week. Rebuilding
  the same segments from scratch wastes the review
  hour.

## The weekly 15 minute routine

Practice guidance, not a Google rule. Once a week:

1. Open the Policy Center. Fix every flagged issue
   before its deadline.
2. Open the Ad Review Center. Review new ads with
   meaningful impressions. Block only with a concrete
   reason.
3. Glance at the saved report views. Note anything
   unusual with a date.
4. Check the account home page for open actions:
   verification, tax, payment, or consent steps.

The monthly version of this routine, with the full
checklist, is in
`examples/advanced-monthly-review-checklist.md`.
