# WordPress and Site Kit setup

The hands-on companion to
`references/19-platform-setup-guides.md`. That file covers
the platform overview, ads.txt, and sellers.json. This file
covers the actual steps of placing the AdSense code on a
WordPress site, verifying it live, and fixing the caching
and theme problems that hide code from Google.

Setup does not change approval odds. A perfectly placed
code snippet on a thin site still fails review. Place the
code correctly, then judge the site on content and trust.

## Route 1: Site Kit by Google (recommended by Google)

OFFICIAL, read on the live AdSense Help page "Connect to
AdSense and show ads on your WordPress site" on
18 November 2026
(`support.google.com/adsense/answer/7527509`): Google
highly recommends Site Kit for WordPress by Google. Site
Kit can connect the WordPress site to the AdSense account
and place the AdSense code on all pages.

What Site Kit is: a free, open source WordPress plugin
from Google. It connects AdSense, Analytics, Search
Console, and PageSpeed Insights and shows their metrics
inside the WordPress dashboard.

Setup steps, from the official page:

1. In the WordPress dashboard, open Plugins, then Add New.
2. Search for "Site Kit by Google", find the plugin, and
   click Install Now.
3. Click Activate.
4. Click Start Setup and follow the steps.
5. After setup, click Connect Service under AdSense, on
   the Site Kit dashboard or the Settings tab.
6. Follow the instructions in the plugin. Allow Site Kit
   to place the AdSense code. It places the code for the
   non-AMP and AMP versions of the site.

Two limits from the same page:

- To make ads serve, Auto ads must be enabled in the
  AdSense account. Site Kit does not have permission to
  change AdSense account settings. Enable Auto ads in
  the account, not in the plugin.
- When connecting, there is an option to show ads as
  soon as the account is activated. With visitors from
  the European Economic Area, the UK, or Switzerland,
  consider unchecking it until consent handling is in
  place, to comply with Google's EU user consent policy.
  The setting can be changed after approval.

Checking that Site Kit placed the code: in Site Kit
settings, the AdSense section should show "Code has been
placed". If it does not, the code is not on the pages,
whatever the dashboard seems to say. Check the live page
source as well, as described below.

## Route 2: manual placement

Use the manual route when Site Kit is not wanted, or when
the theme needs full control. Place the AdSense code in
the head of every page, between the opening head tag and
the closing head tag.

Ways to place it, in order of safety:

- A child theme header file. Never edit the parent theme
  directly. Theme updates overwrite parent theme files
  and silently remove the code.
- A code snippets plugin. One snippet, set to run in the
  head on the front end only.
- A header injection setting in the theme or a header
  and footer plugin. Google's Help page names the Insert
  Headers and Footers plugin, the Advanced Ads plugin,
  and the Ad Inserter plugin as partner resources. Any
  of them can place the code. Pick one and stick to it.

Never run two placement methods at once. Site Kit plus a
manual snippet means the code appears twice. Duplicated
code confuses verification and can cause ad behaviour
problems. Choose one route, remove the other completely,
and verify the live source shows the code exactly once.

## Verify the code live

Do these checks in a private browser window, logged out
of WordPress. Caches and admin views hide the truth.

1. Open the live homepage. View the page source. Search
   for the publisher ID (pub- followed by digits). It
   must appear in the head section.
2. Open one post and one page. Check the code is present
   on each. A snippet set to run only on the homepage
   fails verification on content pages.
3. Count occurrences. The AdSense script tag should
   appear once per page. Twice means two placement
   methods are active.
4. Open the ads.txt URL and confirm the file loads with
   the line copied from the account. See
   `references/19-platform-setup-guides.md`.
5. Run `scripts/site_audit.py` and confirm it finds the
   code and the ads.txt file.

## Caching pitfalls that hide code

Caching is the most common reason code placed in the
dashboard does not appear on the live site. The checks
below are practice guidance from real troubleshooting,
not Google rules.

- Page cache: a caching plugin serves a saved copy of
  each page. After placing code, purge every cache:
  the caching plugin, the host cache, and the CDN cache.
  Then re-check the live source. A purge of one layer
  while another still serves old HTML changes nothing.
- Logged-in bypass: most caches bypass logged-in users.
  The admin sees fresh pages while visitors and Google
  see cached pages. Always verify logged out.
- Minify and combine: CSS and JS minification rarely
  breaks the AdSense script tag, but aggressive
  combination or deferred loading can delay or alter it.
  If the code is present in the source but ads do not
  appear, temporarily turn off JS combination and
  deferral, purge, and re-check.
- Object and opcode caches: some hosts cache PHP output
  separately from page cache. A host-level purge or a
  short wait may be needed after a theme file edit.
- AMP versions: if the site serves AMP pages, the code
  must be present on the AMP version too. Site Kit
  handles both versions. A manual snippet placed only
  in the non-AMP header leaves AMP pages without code.
- Stale CDN edge copies: a CDN can serve old HTML for
  hours after a purge if the purge did not reach every
  edge. Check the live source from a second network or
  after a wait before concluding the code is missing.

## Theme problems

- Themes that replace the head: some page builders and
  custom themes build the head themselves and ignore the
  standard header file. A snippet hooked to the standard
  header may never print. Verify in the live source, not
  in the theme settings.
- Themes with their own ad slots: a theme ad slot and
  the AdSense code are different things. A theme slot
  without the AdSense code shows nothing. A theme slot
  plus Auto ads can double-place ads. Use one system.
- Child theme drift: after a parent theme update, check
  the child theme header still matches the parent. A
  stale child header can drop new head content.
- Maintenance and coming soon modes: any mode that shows
  visitors a holding page hides the code from Google.
  Turn it off before requesting review.

## Ads placed but not showing

From the official Site Kit page FAQ, check in this order:

1. Site Kit settings show "Code has been placed".
2. The site is added on the Sites page in AdSense.
3. Auto ads are enabled on the Ads page in AdSense.
4. The account has no outstanding actions. Identity,
   address, and tax steps block serving until complete.
5. The page is not excluded from ads in the account.
6. Consent handling is not blocking ad requests for that
   visitor. See
   `references/18-consent-and-privacy-deep-dive.md`.

If all six pass and ads still do not show, wait. Newly
approved accounts and new placements can take time
before ads appear. Do not add the code a second time to
force it.

## What not to do

- Do not paste the code into post content. It belongs in
  the head.
- Do not edit the code. Copy it exactly as the account
  shows it.
- Do not place the code on pages that should never carry
  ads, such as login, checkout, and thank you pages, if
  the account offers exclusions. Use the exclusions.
- Do not use a nulled or unknown "AdSense placement"
  plugin. A plugin with code access can inject anything
  into every page. Use Site Kit, a well known snippets
  plugin, or the child theme.
