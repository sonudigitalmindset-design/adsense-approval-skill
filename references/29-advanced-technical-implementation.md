# Advanced technical implementation

AdSense code is simple to paste and easy to break. This
reference covers the technical layer that sits under every
account: ads.txt at scale, sellers.json, consent debugging,
page experience, the refresh ban, and crawler access.

Read the platform setup basics in
`references/19-platform-setup-guides.md` and the consent
deep dive in `references/18-consent-and-privacy-deep-dive.md`.

## ads.txt at scale

ads.txt is a text file at the domain root that declares
which sellers may sell the site's inventory. The AdSense
line has this form.

- google.com, pub-XXXX, DIRECT, f08c47fec0942fa0

Copy the line from the AdSense account, never from another
site. The publisher ID in the line must be the account's
own ID. A line copied from a tutorial or a neighbour's site
authorises the wrong seller.

Rules that prevent most ads.txt failures.

- One file per domain, at the root, served as plain text.
  A file buried in a subfolder or behind a redirect chain
  may not be found.
- Include every direct seller the site uses, one line each.
  A missing line cuts demand from that seller.
- Re-check the live file after every account change, domain
  change, or migration. A file that was correct last year
  can carry a stale ID today.
- Watch for CDN and cache staleness. After publishing or
  editing ads.txt, fetch the live URL in a fresh browser
  session and confirm the new content, not a cached copy.
- Subdomains that are separate sites need their own files
  where Google treats them separately. See
  `references/27-account-architecture-and-graduation.md`.
- Apps use app-ads.txt, the same idea for app inventory.
  Keep the two files separate and correct for their own
  platform.

## sellers.json, read but not written

sellers.json is an exchange-side file. Publishers do not
create it. Google publishes its own sellers.json, and
advertisers use it together with ads.txt to verify the
supply chain: the ads.txt line names the seller, and the
sellers.json entry confirms the seller's identity and type.

What a publisher needs to know.

- The seller ID in Google's sellers.json entry is the
  publisher ID. It must match the ads.txt line.
- The seller type entry reflects whether the account is a
  publisher or an intermediary. It is set by Google's
  records, not by the publisher.
- A mismatch between ads.txt and sellers.json is a buyer
  trust problem. It is fixed by correcting ads.txt to the
  account's own line, not by editing anything on the
  exchange side.
- Do not pay anyone to "fix" sellers.json. There is nothing
  for a publisher to fix there.

## Consent debugging

Consent failures show up as limited ads, lower fill, and
policy flags. Debug in this order.

- Confirm a certified CMP loads on every page that serves
  ads, before ad requests fire. A CMP that loads after the
  ad call cannot gate the call.
- Confirm the consent state is readable by Google's tags.
  In a browser, check that the TCF consent string is
  present where TCF applies, and that Consent Mode signals
  fire with the states the visitor chose. The four Consent
  Mode v2 signals are ad_storage, ad_user_data,
  ad_personalization, and analytics_storage.
- Test as a new visitor. Clear consent storage or use a
  fresh browser profile, and confirm the banner appears,
  the choices work, and declining still loads the page
  with limited ads rather than breaking the layout.
- Test from a regulated region where possible. Consent
  behaviour for EEA, UK, and Swiss visitors is the
  behaviour that matters for the certified CMP rule.
- Check Funding Choices diagnostics where Funding Choices
  is the CMP. The Privacy and messaging section shows
  message performance and errors.
- One CMP only. Two consent plugins active at once can
  fight over the consent state, load duplicate banners,
  or leave one banner invisible while its scripts still
  run. Keep the CMP that is configured and rendering,
  and deactivate the other.

## Page experience and ad layout

Ads affect the experience numbers Google measures. The
fixes are layout choices, not code tricks.

- Reserve space for ad slots. A slot that pops into
  existence late pushes content down and creates layout
  shift. A minimum height on the slot container, set in
  the site's own CSS, keeps the layout stable. This is
  ordinary web practice, not a modification of ad code.
- Keep the heaviest ad formats above the fold in check.
  A page that loads three large formats before content
  reads as an ad page, not a content page, whatever the
  word count says.
- Use the Auto ads ad load control and format toggles
  instead of custom scripts to shape ad density. See
  `references/26-advanced-reporting-and-experiments.md`.
- Test every template on a phone sized view. Sticky
  elements, anchor ads, and vignette ads interact with
  mobile navigation in ways desktop testing never shows.
- Do not lazy load AdSense code with custom scripts.
  AdSense code must not be modified, wrapped, delayed, or
  triggered by custom logic unless Google's own
  documentation for that format says so. Lazy loading
  guidance published for Ad Manager tags does not transfer
  to AdSense code. When in doubt, load the code as Google
  serves it and shape density with account settings.

## The refresh ban

AdSense prohibits refreshing ads. The Ad placement policies
state it plainly: publishers are not permitted to refresh a
page or an element of a page without the user requesting a
refresh. The ban covers three cases.

- Ads on pages or placements that auto-redirect.
- Ads on pages or placements that auto-refresh.
- Ads displayed for a preset time, such as a pre-roll,
  before users can view content like videos, games, or
  downloads.

A full page reload caused by the user navigating or
manually refreshing the browser is a normal new page load
and is permitted. A timer, a script, or a rotation that
reloads an ad slot is not.

Ad Manager is different. Ad Manager allows refresh, but
only with declared inventory. Publishers must declare
which inventory refreshes, with the trigger and interval,
and failure to declare is itself a policy violation.
Verify the current declaration rules on the live Ad
Manager Help pages before implementing refresh anywhere.
Never apply Ad Manager refresh practice to AdSense code.

## Single-page apps and dynamic pages

Single-page apps change content without a full page load.
That creates a refresh trap: firing a new ad request on
every virtual navigation looks like refreshing without a
user requested page load.

- Treat one real page load as one ad load, unless Google's
  own documentation for the framework or format describes
  a supported pattern.
- Do not re-trigger AdSense code on route changes with
  custom scripts.
- Where an app genuinely needs dynamic ad behaviour, the
  honest path is to read the live AdSense and Ad Manager
  documentation for the pattern, or to keep the monetised
  surface on ordinary multi-page navigation.

## AMP pages

AMP pages can carry AdSense through the amp-ad element
with the AdSense type. The requirements are the same as
everywhere else: valid AMP, correct publisher ID, ads.txt
in place, and policy compliant content.

AMP's role has shrunk. Google no longer requires AMP for
Top Stories eligibility, reported. Do not build a new site
around AMP for approval reasons. Maintain AMP only where
it already serves real traffic, and keep its ad setup
identical in policy terms to the main site.

## Crawler access

Google's crawlers must reach the pages that carry ads.

- Do not block the AdSense crawler in robots.txt. The
  crawler identifies itself as Mediapartners-Google.
  Blocking it starves the review and the ad matching.
- Do not put ad code on pages that require login, sit
  behind a paywall with no crawler access, or render only
  after heavy client side work that a crawler cannot
  follow. If a reviewer cannot see the content, the page
  cannot be approved.
- Check server logs or Search Console for crawl errors
  after a migration. A redirect chain, a firewall rule,
  or a changed hostname can silently cut crawler access.
- A Cloudflare challenge page shown to automated fetches
  can block review tooling. If a checker reports a
  challenge page, verify the page in a real browser
  before concluding the site is broken.

## The technical pre-flight

Before any new template, theme, or plugin goes live on a
monetised site, run this short list.

- ads.txt live and correct.
- Ad code unmodified and in the right templates.
- No auto-refresh, auto-redirect, or preset-time ad gate.
- One CMP, loading before ad requests, tested as a new
  visitor.
- Crawler access open, robots.txt checked.
- Layout stable on a phone sized view, with space
  reserved for slots.
- No ad near a tap target, download button, or close
  button.

A template that passes this list rarely causes a technical
policy problem. A template that fails it will cause one
sooner or later, however good the content is.
