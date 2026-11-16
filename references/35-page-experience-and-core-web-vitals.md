# Page experience and Core Web Vitals

Status: OFFICIAL. Read on the live Google Search Central
and web.dev pages on 17 November 2026. These are Search
ranking and page experience signals, NOT AdSense
approval rules. AdSense publishes no Core Web Vitals
requirement. The value for an applicant is narrower:
the same page qualities that rank well are the qualities
a human reviewer sees when opening the site. A slow,
shifting, interstitial-heavy site reads as unfinished
even when the content is fine. That last point is
inference, not a Google rule.

## What Google says about page experience

Google Search Central's page experience guide asks six
self-assessment questions:

1. Does the page have good Core Web Vitals?
2. Is the page served securely?
3. Does the page display well on mobile?
4. Does the page avoid excessive ads that distract from
   or interfere with the main content?
5. Does the page avoid intrusive interstitials?
6. How easily can visitors distinguish the main content
   of the page?

Google states that there is no single signal of a great
page experience. Core Web Vitals are used by the ranking
systems. Good scores do not guarantee top rankings.
Beyond Core Web Vitals, the other page experience
aspects do not directly help ranking, but they align
with what ranking seeks to reward. Evaluation is
generally page-specific, with some site-wide
assessments. Google Search always seeks to show the
most relevant content, even if the page experience is
sub-par. Read the live guide before acting:
https://developers.google.com/search/docs/appearance/page-experience

## Core Web Vitals, thresholds, and method

Three metrics make up Core Web Vitals. Google defines
them and their thresholds on Search Central and web.dev:

- Largest Contentful Paint (LCP) measures loading
  performance. Good is within the first 2.5 seconds.
- Interaction to Next Paint (INP) measures
  responsiveness. Good is less than 200 milliseconds.
  The web.dev guide counts exactly 200 milliseconds as
  good. The Search Central wording says less than 200
  milliseconds. Treat 200 milliseconds as the boundary
  and aim clearly below it.
- Cumulative Layout Shift (CLS) measures visual
  stability. Good is less than 0.1. The web.dev guide
  counts exactly 0.1 as good. Treat 0.1 as the boundary
  and aim clearly below it.

INP replaced First Input Delay (FID) as the
responsiveness metric in March 2024. FID no longer
counts as a Core Web Vital.

A page passes when it meets the good targets for all
three metrics at the 75th percentile of page loads,
segmented across mobile and desktop devices. This is
field data, meaning it comes from real visitors, not
from a single test run. One fast test on one fast
connection proves nothing. Google's CrUX report and the
Search Console Core Web Vitals report show the field
picture. Lab tools such as Lighthouse give repeatable
diagnostics but not the field result. In lab testing,
Total Blocking Time is the diagnostic proxy for INP,
and Time to First Byte and First Contentful Paint are
diagnostic proxies for LCP.

Stable metrics change at most once per year, and Google
gives prior notice when a change is planned.

## How to check a site

- Search Console Core Web Vitals report: field data
  for pages Google sees, grouped by URL patterns.
  This is the report that matters once the site is
  indexed.
- PageSpeed Insights: field data plus lab diagnostics
  for one URL at a time. Use it for the homepage and
  one representative post.
- Lighthouse: repeatable lab runs, useful before the
  site has field data.
- Chrome DevTools: inspect individual layout shifts
  and long tasks on the pages you are fixing.

## What this skill's scripts check, and what they cannot

The audit scripts in `scripts/` are static checks.
They cannot measure Core Web Vitals. They check the
nearby signals:

- `deep_audit.py` measures homepage fetch time and
  warns when it exceeds 3 seconds. That is a practice
  heuristic, not a Google threshold and not an LCP
  measurement.
- `deep_audit.py` counts images without width and
  height attributes. Missing dimensions are a known
  layout shift cause.
- `deep_audit.py` flags popup and modal markers.
  Only a human reading the page can judge whether a
  popup is an intrusive interstitial.
- `deep_audit.py` checks HTTPS, viewport, and mixed
  content. These match the secure and mobile questions
  in the page experience guide.

Core Web Vitals themselves need field data. Before
applying, run the field tools above on the homepage
and one post. A site with no field data yet is not
failing anything. It simply has no evidence. Fix the
obvious problems first: images without dimensions,
heavy hero images, render-blocking scripts, and
popups that cover the content.

## Ad-related experience metrics

Google is experimenting with CrUX ad metrics that
capture the number of ads, ad density, and ad weight
on a page. These are experimental and are not part of
Core Web Vitals. Their existence confirms the
direction of the page experience guide: excessive
advertising that crowds out content is a real
experience problem. The audit scripts already warn
when a page carries 6 or more ad slots. That threshold
is a practice heuristic, not a Google rule.

## Fix order for a slow or shifting site

1. Reserve space for every image and ad slot so
   content does not jump while the page loads.
2. Compress the hero image and serve it in a modern
   format. The audit flags images over 1 MB.
3. Cut render-blocking JavaScript and CSS that
   delays the first paint.
4. Reduce long tasks on the main thread so taps and
   clicks respond quickly.
5. Move popups so they do not cover the main content
   on the first screen, especially on mobile.

Re-test after each change with the field tools, not
with a single lab run. Record the before and after
numbers so the fix is evidence, not a feeling.

## Sources

- Understanding page experience, Search Central, read
  17 November 2026:
  https://developers.google.com/search/docs/appearance/page-experience
- Understanding Core Web Vitals and Google search
  results, Search Central, read 17 November 2026:
  https://developers.google.com/search/docs/appearance/core-web-vitals
- Web Vitals, web.dev, read 17 November 2026:
  https://web.dev/articles/vitals
