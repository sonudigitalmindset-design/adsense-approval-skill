# Check catalog

Every check in `scripts/deep_audit.py` and
`scripts/site_audit.py`, enumerated from the code, with the
status label of each check and a one-line description of what
it measures. This catalog matches the scripts as of version
1.12.0, 18 November 2026. If a listed check is not in the
code, it does not belong here. If the code gains a check,
this catalog must gain it too.

## How the count works

One check means one decision point in the code that produces
its own verdict line, its own information line, or its own
per-page flag type. Where one code block emits ok, warn, and
fail variants of the same decision, it counts once. Where a
loop emits one verdict line per item, each item counts
separately, because each produces its own line in the
report. The per-page line mark (FAIL, WARN, or OK) is
derived from the flags and is not a separate check. The
readiness score and the verdict line are computed from
check outcomes and are not checks. The JSON report mirrors
check outcomes and adds no new checks.
`scripts/rejection_decoder.py` is not an audit checker. It
matches keywords to `references/07-rejection-reasons-and-fixes.md`
and is excluded from this catalog.

## Totals

- `scripts/deep_audit.py`: 58 report checks, 41 information
  lines, 32 per-page flag types. Total 131.
- `scripts/site_audit.py`: 27 report checks, 1 information
  line. Total 28.
- Combined total: 159 check instances across both scripts.
- Status totals: 16 OFFICIAL, 22 REPORTED, 78 INFERRED,
  43 INFO.

Read the total honestly. It counts check instances, not
Google rules. `site_audit.py` repeats the quick subset of
the deep audit on purpose, so unique signals are fewer
than 159. Most checks are INFERRED practice heuristics or
INFO lines. Only 16 mirror a published Google rule. No
count of checks, however large, matches Google's decision,
because the decision includes judgement, account history,
and traffic quality that no crawler can see. Do not pad,
split, or rename checks to reach any target number.

## Status labels

- OFFICIAL: the check mirrors a rule or directive stated
  on a live Google Help, Search Central, or Publisher
  Policies page, or the ads.txt specification Google
  documents. The source page is listed in
  `references/11-official-sources.md`.
- REPORTED: the check mirrors a rejection-reason category
  or a pattern widely reported by publishers. See
  `references/07-rejection-reasons-and-fixes.md`.
- INFERRED: a practice heuristic built by this skill. It
  is a tripwire for human attention, never a Google rule.
  Thresholds in these checks are the skill's own.
- INFO: the script reports the fact without judging it.
  Information lines never affect the readiness score.

## deep_audit.py: report checks, site level

In code order. Each item is one decision point.

1. [INFERRED] HTTPS scheme: the input URL uses HTTPS, else
   a fail.
2. [REPORTED] Homepage returns 200: the homepage must
   answer HTTP 200, else a fail and the run stops. Mirrors
   the site down or unavailable rejection category.
3. [INFERRED] Homepage slow: a homepage fetch over 3
   seconds warns as a user experience signal.
4. [INFO] HSTS header: an ok when the HSTS header is
   present, information only when absent. Never affects
   the score.
5. [OFFICIAL] Homepage X-Robots-Tag noindex: a fail when
   the homepage response header carries noindex, because a
   noindexed homepage cannot be reviewed or ranked.
6. [INFERRED] HTTP to HTTPS redirect: the HTTP version
   must redirect to HTTPS, else a warn, with an
   information line when the behaviour is unclear.
7. [INFERRED] Alternate host redirect: the www or bare
   alternate host must redirect to the canonical host,
   else a warn.
8. [OFFICIAL] robots.txt root block: a fail when
   robots.txt disallows all crawling, because the crawler
   cannot review a fully blocked site.
9. [OFFICIAL] Mediapartners-Google block: a fail when
   robots.txt blocks the AdSense crawler at the root.
10. [INFERRED] robots.txt names a sitemap: a warn when no
    Sitemap line is present.
11. [INFERRED] robots.txt reachable: a warn when
    robots.txt returns 404 or cannot be verified.
12. [OFFICIAL] ads.txt Google line: the Google line must
    be well formed with a 16-digit publisher ID, a DIRECT
    relationship, and the certification ID. Multiple IDs,
    malformed lines, and missing lines warn.
13. [INFERRED] Nonsense URL 404: a nonsense URL must
    return 404, not a soft 200.
14. [REPORTED] Trust page About: the page must exist at a
    common slug, else a fail.
15. [REPORTED] Trust page Contact: the page must exist at
    a common slug, else a fail.
16. [REPORTED] Trust page Privacy: the page must exist at
    a common slug, else a fail.
17. [REPORTED] Trust page Terms: the page must exist at a
    common slug, else a warn.
18. [REPORTED] Trust page Disclaimer: the page must exist
    at a common slug, else a warn.
19. [OFFICIAL] Privacy mentions cookies: a warn when the
    Privacy page does not mention cookies.
20. [OFFICIAL] Privacy mentions Google: a warn when the
    Privacy page does not mention Google.
21. [OFFICIAL] Privacy mentions advertising: a warn when
    the Privacy page does not mention advertising.
22. [OFFICIAL] Privacy mentions third parties: a warn when
    the Privacy page does not mention third parties.
23. [OFFICIAL] Privacy mentions opt-out or Ads Settings: a
    warn when the Privacy page mentions neither.
24. [INFERRED] About page depth: a warn when the About
    page has under 100 words of page text.
25. [OFFICIAL] Consent platform markers: a warn when no
    consent platform marker is found on the homepage,
    because consent handling is required for EEA, UK, and
    Swiss traffic.
26. [INFERRED] Sitemap found: a warn when no common
    sitemap URL returns URLs, in which case only the
    homepage is checked.
27. [INFERRED] Sitemap files unreadable: a warn when a
    sitemap file cannot be read after retries, so the
    crawl may be incomplete.
28. [INFERRED] Sitemap lastmod stale: a warn when the
    newest lastmod is over 90 days old.

## deep_audit.py: report checks, cross-page

In code order. Each item is one decision point.

29. [REPORTED] Failed sitemap URLs: a fail when any
    crawled sitemap URL does not return a readable 200
    page.
30. [INFERRED] Duplicate titles: a warn when the same
    title appears on more than one page.
31. [INFERRED] Duplicate descriptions: a warn when the
    same meta description appears on more than one page.
32. [INFERRED] Thin pages: a warn for pages under 200
    words, as a thin-content risk for human judgement.
33. [INFERRED] No H1: a fail for pages with no H1.
34. [INFERRED] Multiple H1s: a warn for pages with more
    than one H1.
35. [INFERRED] Images missing alt text: a warn with the
    site-wide total.
36. [INFERRED] Meta noindex pages: a warn listing crawled
    pages that carry meta noindex.
37. [INFERRED] Header noindex pages: a warn listing
    crawled pages that carry noindex through the
    X-Robots-Tag header.
38. [INFERRED] Affiliate links without disclosure: a warn
    for pages with affiliate links and no disclosure
    wording, labelled a practice heuristic.
39. [INFERRED] No html lang: a warn for pages with no lang
    attribute.
40. [INFERRED] No canonical: a warn for pages with no
    canonical link.
41. [INFERRED] No og:image: a warn for pages with no
    og:image, as a share preview signal.
42. [INFERRED] No trust-page links: a warn for pages that
    link to no trust page.
43. [INFERRED] Sitemap redirects: a warn listing sitemap
    URLs whose final URL differs. Added in v1.11.0.
44. [INFERRED] Robots-blocked sitemap URLs: a warn
    listing sitemap URLs matching a Disallow rule for
    User-agent star, using an approximate parse. Added in
    v1.11.0.
45. [INFERRED] Noindex in sitemap: a warn listing
    noindexed pages still listed in the sitemap. Added in
    v1.11.0.
46. [INFERRED] Duplicate H1 texts: a warn when the same
    H1 text repeats across pages.
47. [INFERRED] Shared canonical URLs: a warn when one
    canonical URL is shared by more than one page.
48. [INFERRED] Orphan pages: a warn for sitemap pages
    receiving no internal link from any crawled page.
49. [INFERRED] Thin archives: a warn for category or tag
    pages with under 50 article words.
50. [OFFICIAL] Homepage meta noindex: a fail when the
    homepage carries meta noindex.
51. [INFERRED] Thin trust pages: a warn for trust pages
    under 100 words.
52. [INFERRED] Navigation dead ends: a warn for crawled
    pages linking to no other internal page.
53. [INFERRED] Near-duplicate pairs: a warn for page pairs
    sharing over 75 percent article text by shingle
    similarity.
54. [REPORTED] Internal links broken: a fail listing
    verified internal links that do not return 200,
    capped at 250 by default.
55. [INFERRED] External links broken: a warn listing
    verified external links that look broken, capped at
    80 by default.
56. [INFERRED] Images broken: a warn listing verified
    same-origin images that do not load, capped at 100 by
    default.
57. [INFERRED] Images over 1 MB: a warn listing verified
    images larger than 1 MB.
58. [INFERRED] Canonical targets broken: a warn listing
    probed same-origin canonical targets that do not
    return 200, capped at 50. Added in v1.11.0.

## deep_audit.py: information lines

In code order. Each item reports a fact without judging
it. None of these affects the readiness score.

1. [INFO] Homepage fetch time and body size.
2. [INFO] X-Content-Type-Options header presence.
3. [INFO] Homepage Cache-Control header value or absence.
   Added in v1.11.0.
4. [INFO] Homepage CDN or cache header presence. Added in
   v1.11.0.
5. [INFO] Content-Security-Policy header presence. Added
   in v1.11.0.
6. [INFO] X-Frame-Options header presence. Added in
   v1.11.0.
7. [INFO] ads.txt RESELLER line count.
8. [INFO] RSS feed presence at /feed/.
9. [INFO] Archive pagination /page/2/ status.
10. [INFO] Contact page form presence.
11. [INFO] Ad code markers found on the homepage.
12. [INFO] Sitemap newest lastmod date and age.
13. [INFO] Sitemap oldest lastmod date.
14. [INFO] Sitemap content span in days.
15. [INFO] No sitemap update in over 30 days.
16. [INFO] Pages with under 200 article words.
17. [INFO] Pages with no H2 headings.
18. [INFO] Images with no width and height attributes.
19. [INFO] Structured data types found.
20. [INFO] Pages carrying ad code markers and total ad
    slots.
21. [INFO] Pages with popup or modal markers.
22. [INFO] Pages with no time element.
23. [INFO] Pages with no author or byline signal.
24. [INFO] Open Graph and Twitter completeness counts:
    pages missing og:title, og:description, or
    twitter:card. Added in v1.11.0.
25. [INFO] Discovered internal URLs not in the sitemap.
26. [INFO] Total links carrying rel=sponsored.
27. [INFO] Median page length and shortest page.
28. [INFO] Homepage structure: navigation, footer, and
    site search.
29. [INFO] Homepage google-site-verification meta tag.
30. [INFO] Homepage content link count.
31. [INFO] Current year missing from homepage HTML.
32. [INFO] Pages with no favicon link.
33. [INFO] Links to social platforms.
34. [INFO] Contact page email link presence.
35. [INFO] Pages with comment form markers.
36. [INFO] Pages with related-content markers.
37. [INFO] Total links carrying rel=nofollow.
38. [INFO] Pages with updated or modified markers.
39. [INFO] Average internal outlinks per page.
40. [INFO] External links that could not be verified.
41. [INFO] Images that could not be verified.

## deep_audit.py: per-page flag types

In code order. Each item is one flag pattern appended to a
page record. A page line shows FAIL when its flags include
no title, no H1, a thin flag, or a placeholder flag, WARN
when it has any other flags, and OK when it has none.

1. [REPORTED] HTTP error: the page did not return 200.
2. [INFERRED] Redirects to: the final URL differs from
   the requested URL.
3. [INFERRED] No title.
4. [INFERRED] Title too short: under 10 characters.
5. [INFERRED] Title long: over 70 characters.
6. [INFERRED] Title repeats a word 4+ times: possible
   stuffing, read the title.
7. [INFERRED] No meta description.
8. [INFERRED] Description short: under 50 characters.
9. [INFERRED] Description long: over 160 characters.
10. [INFERRED] Description identical to title.
11. [INFERRED] No H1.
12. [INFERRED] Multiple H1s: the count is shown.
13. [INFERRED] Empty H1.
14. [INFERRED] Thin: under 200 words.
15. [INFERRED] Images without alt: the count is shown.
16. [INFERRED] Noindex: meta robots noindex on the page.
17. [INFERRED] X-Robots-Tag noindex header.
18. [INFERRED] No viewport.
19. [INFERRED] No html lang attribute.
20. [INFERRED] No charset meta.
21. [INFERRED] No og:image.
22. [INFERRED] No canonical.
23. [INFERRED] Mixed-content refs: the count of http://
    src or href values is shown.
24. [INFERRED] Ad slots: 6 or more slots, check
    ad-to-content balance.
25. [INFERRED] Popup or modal markers: the count is
    shown, review manually.
26. [INFERRED] No trust-page links on this page.
27. [REPORTED] Placeholder text: one of 7 demo strings
    found in page text.
28. [INFERRED] REVIEW phrase: one of 10 high-risk phrases
    found with word-boundary matching, read the page.
29. [INFERRED] REVIEW copyright signal: one of 5
    copyright-risk phrases found, read the page.
30. [INFERRED] Canonical points elsewhere: the canonical
    path differs from the final URL path.
31. [INFERRED] Affiliate links without disclosure
    wording.
32. [INFERRED] Affiliate links with no sponsored or
    nofollow qualification.

## site_audit.py: report checks

In code order. This script checks the homepage and a small
set of common URLs. It is the quick subset of the deep
audit, so most checks below repeat a deep audit check on
the homepage only.

1. [INFERRED] HTTPS scheme: a warn when the input URL is
   HTTP.
2. [REPORTED] Homepage returns 200: a fail and the run
   stops when the homepage does not answer 200.
3. [INFERRED] HTTP to HTTPS redirect: an ok when the HTTP
   version redirects, a warn when it serves content or
   cannot be verified.
4. [INFERRED] Homepage title: a warn when the homepage
   has no title text.
5. [INFERRED] Viewport: a warn when no viewport meta tag
   is found.
6. [OFFICIAL] Homepage noindex: a fail when the homepage
   carries meta noindex.
7. [INFERRED] HTML lang: a warn when no lang attribute is
   found.
8. [INFERRED] Favicon: a warn when no favicon link is
   found.
9. [REPORTED] Demo marker "hello world": a warn when
   found on the homepage.
10. [REPORTED] Demo marker "just another wordpress
    site": a warn when found on the homepage.
11. [REPORTED] Demo marker "sample page": a warn when
    found on the homepage.
12. [REPORTED] Demo marker "lorem ipsum": a warn when
    found on the homepage.
13. [REPORTED] Demo marker "coming soon": a warn when
    found on the homepage.
14. [REPORTED] Demo marker "under construction": a warn
    when found on the homepage.
15. [OFFICIAL] Consent platform markers: a warn when no
    consent marker is found on the homepage.
16. [INFERRED] 404 behaviour: a warn when a nonsense URL
    does not return 404.
17. [OFFICIAL] robots.txt root block: a fail when
    robots.txt disallows all crawling.
18. [OFFICIAL] Mediapartners-Google block: a fail when
    robots.txt blocks the AdSense crawler.
19. [INFERRED] robots.txt names a sitemap: a warn when no
    Sitemap line is present.
20. [INFERRED] robots.txt reachable: a warn when
    robots.txt returns 404 or cannot be verified.
21. [INFERRED] Sitemap found: a warn when no common
    sitemap URL returns 200.
22. [OFFICIAL] ads.txt Google line: the Google line must
    be well formed with a 16-digit publisher ID, a DIRECT
    relationship, and the certification ID.
23. [REPORTED] Trust page About: the page must exist at a
    common slug, else a fail.
24. [REPORTED] Trust page Contact: the page must exist at
    a common slug, else a fail.
25. [REPORTED] Trust page Privacy: the page must exist at
    a common slug, else a fail.
26. [REPORTED] Trust page Terms: the page must exist at a
    common slug, else a warn.
27. [REPORTED] Trust page Disclaimer: the page must exist
    at a common slug, else a warn.

## site_audit.py: information lines

1. [INFO] Homepage visible word count, rough count.

## Keeping this catalog honest

- When a script gains, loses, or changes a check, update
  this catalog in the same release and record the change
  in `CHANGELOG.md`.
- When a label changes because a rule is verified on a
  live official page or proves unreliable, update the
  label and the source note here.
- Never count a check twice under two names. Never split
  one decision into several entries to raise the total.
  The total is whatever the code contains, no more.
- A high count is not a quality claim. A script with 159
  checks and a clean report can still face rejection for
  reasons no check can see. See
  `references/31-approval-check-matrix.md` for what no
  script can check.
