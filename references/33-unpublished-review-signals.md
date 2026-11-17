# Unpublished review signals

This reference collects the signals that rejection
patterns, reviewer behaviour, and publisher reports
suggest Google weighs during a site review, even though
Google has never published them as rules. Every signal
here carries the label INFERRED. That label is the
whole point. A signal that is inferred must never be
taught as a confirmed Google rule, and no signal here
guarantees approval or explains a rejection on its own.

Read `references/32-hidden-deep-approval-checks.md` for
the three layers of the review, and
`references/31-approval-check-matrix.md` for what a
script can and cannot check.

## Why unpublished signals still matter

A reviewer is a person with a checklist that Google does
not publish in full. The reviewer forms an impression of
the whole site in minutes: is this a real project run by
a real person, does it serve readers, and is it finished
enough to carry ads. The signals below shape that
impression. Removing a weak signal never hurts a good
site, and a site that reads as genuine, complete, and
maintained gives the reviewer nothing to doubt.

## Identity and trust signals

INFERRED: a visible human behind the site.

- A named author with a short bio on posts, and an
  author archive page that lists their work.
- An About page that tells a specific story with real
  detail, not generic mission statements.
- A Contact page with a working form, and ideally an
  email address a reader can write to.
- Links to social profiles that are active and match the
  site's name and topic.
- A Privacy page long enough to describe actual data
  handling, not three copied sentences.
- Consistent naming across the site, the author pages,
  and the social profiles.

The script checks: About depth, Contact form presence,
email links on the Contact page, social platform links,
and thin trust pages. A human must judge whether the
identity feels real.

## Content depth signals

INFERRED: content that shows experience and effort.

- Posts that include first-hand detail: numbers from
  the author's own tracking, photos from their own
  camera, mistakes they made, and results over time.
- Posts that answer the question fully instead of
  repeating the question in different words.
- Internal links between related posts, showing the
  site is one body of work rather than disconnected
  pages.
- Updated dates on posts that change over time, showing
  maintenance rather than publish and forget.
- Comments or other reader interaction, showing real
  visitors rather than an empty shell.

The script checks: article word counts, near-duplicate
text, related-content markers, updated markers, comment
markers, internal link depth, and orphan pages. A human
must judge whether the content shows real experience.

## Freshness and activity signals

INFERRED: a site that is alive and maintained.

- New content at a steady rhythm, not a burst of posts
  in one week followed by silence.
- A sitemap whose newest dates are recent, and whose
  oldest dates show history rather than a site built
  yesterday.
- A footer copyright year that matches the current year.
- No stale banners, expired offers, or dead seasonal
  content on the homepage.

The script checks: sitemap lastmod freshness and span,
current year on the homepage, and homepage content
links. A human must judge whether the rhythm looks
natural.

## Navigation and completeness signals

INFERRED: a finished site with no dead ends.

- Every sitemap page reachable through menus, archives,
  or related links. Orphan pages suggest assembly for
  approval rather than building for readers.
- No empty categories, no empty tags, and no archive
  pages that list nothing.
- A working site search, a footer with trust links on
  every template, and a navigation menu that covers the
  site's sections.
- No placeholder text, no demo content, and no pages
  that say under construction.

The script checks: orphan pages, sitemap coverage, thin
archives, homepage structure, trust links per page, and
placeholder strings. A human must walk the site as a
stranger and confirm every path works.

## Technical quality signals

INFERRED: a site that loads well and respects the reader.

- Fast pages with images sized for the web. Very heavy
  images slow every visit.
- A mobile layout that works, with a viewport tag and
  no horizontal scrolling.
- No homepage noindex, no accidental noindex on
  important pages, and no robots.txt block on the
  AdSense crawler.
- HTTPS everywhere with no mixed content, one canonical
  host, and clean redirects.
- A favicon, a language attribute, and share previews
  that render correctly.
- What the crawler sees. INFERRED. A JavaScript-rendered
  site can look complete in a browser while serving an
  empty shell to a crawler. The SlayerLegendWiki audit
  (26 August 2026) found every route returning HTTP 200
  with an empty body when fetched with a Googlebot user
  agent, which read as site-wide screens without
  publisher content. Fetch key pages with curl using a
  crawler user agent and confirm article text is present
  in the raw HTML. The deep audit script fetches raw
  HTML without running JavaScript, so its word counts
  reflect the crawler view, not the rendered view.
  Source: SlayerLegendWiki AdSense acceptance plan
  (GitHub, 26 August 2026), read 18 November 2026.

The script checks: homepage timing, image file sizes,
viewport, noindex flags, robots.txt depth, mixed
content, host consistency, favicon, language, and Open
Graph tags. A human must open the site on a phone and
read it.

## Monetisation hygiene signals

INFERRED: a site built for readers first, ads second.

- No ad code before approval, and no competing ad
  networks stacked on the same page.
- Ad slots that leave the content dominant. A page that
  is mostly ad units reads as built for clicks.
- Sponsored and affiliate links marked and disclosed,
  with disclosure visible on the page itself.
- An ads.txt file with only the account's own line and
  resellers actually used, not a copied block of
  dozens of lines.
- No popup that covers the content on arrival, and no
  interstitial that blocks reading.

The script checks: ad slot counts, ad code markers,
sponsored link counts, ads.txt line validation and
RESELLER counts, and popup markers. A human must read
the page and judge the balance.

## Account and traffic shadows

INFERRED, and NOT checkable from outside the account.

- Previous applications, warnings, and closures on the
  same account or on associated accounts, devices, and
  payment details.
- Traffic that arrives in sudden spikes, from bought
  sources, or with behaviour that does not look like
  reading.
- A domain with a history the applicant does not know
  about, including previous owners and previous policy
  problems.

No script checks these. The only honest advice is to
fix the underlying problem, use genuine promotion, and
wait until the history is clean before applying.

## How to use these signals

- Treat every INFERRED signal as a risk to remove, not
  a rule to game. Adding a fake author bio or fake
  social links creates a new trust problem instead of
  solving one.
- Run `scripts/deep_audit.py` and fix every failure.
  Decide every warning by reading the page.
- Read the site as a suspicious stranger. If anything
  feels assembled, copied, unfinished, or built only
  for approval, fix that feeling first.
- Never promise that clearing these signals guarantees
  approval. The decision stays with Google, and the
  hidden layer stays hidden.
