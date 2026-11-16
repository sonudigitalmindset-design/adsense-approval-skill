# Platform setup guides

How to place AdSense code and supporting files on the common
platforms. These are setup steps, not approval shortcuts. The site
still has to pass the whole-site review.

## WordPress

- Place the AdSense code in the head of every page. Use a child
  theme header, a code snippets plugin, or the official Site Kit
  by Google plugin. Do not edit the parent theme directly, since
  updates overwrite it.
- Site Kit by Google is Google's official WordPress plugin. It can
  place the AdSense code, connect Search Console and Analytics,
  and show earnings in the dashboard. It does not change approval
  odds by itself.
- Use one SEO plugin. Two SEO plugins active at once duplicate
  meta tags, descriptions, and sitemaps, which confuses reviewers
  and search engines.
- Use one caching setup. After placing code, clear every cache
  (plugin, host, and CDN) and check the live page source shows the
  code.
- Publish ads.txt at the domain root. Use a dedicated ads.txt
  plugin or upload the file by FTP. Verify it at the live ads.txt
  URL in a browser. See the ads.txt section below.
- Keep WordPress, themes, and plugins updated. An outdated site
  with security warnings fails the trust test.
- Remove unused themes and plugins. A bloated install slows the
  site and widens the attack surface.

## Blogger

- Blogger has built-in AdSense integration under Earnings. The
  platform places the code for you.
- A custom domain works with AdSense on Blogger, but the domain
  must be connected and the site must be reachable at that domain.
- Blogger themes control ad placement through layout gadgets. Keep
  gadgets tidy and remove empty widgets that show as blank boxes.
- ads.txt on Blogger: add it through Settings, Search preferences,
  custom ads.txt, where the option is offered. Verify it at the
  live URL.

## Static and custom-built sites

- Add the AdSense code to the shared head template so every page
  carries it.
- Add ads.txt as a real file at the site root in the build output.
  Check the deploy includes it. Static hosts sometimes need an
  explicit rule for dot-free text files.
- Add a sitemap and robots.txt by hand or with the generator the
  framework offers. Keep one canonical sitemap and point
  robots.txt at it.
- Test the built site, not the development preview. The review
  sees the deployed pages.

## Hosted builders (Wix, Squarespace, Webflow, Shopify)

- Each builder has a custom code or header injection setting. Use
  it for the AdSense code. The setting name differs by platform.
  Read the builder's own help for the current location.
- ads.txt support varies. Some builders offer it directly, some
  need a redirect or a DNS-level workaround, and some do not
  support it at all. Check before choosing a builder for an
  ad-funded site.
- Keep the builder's own cookie banner from conflicting with the
  certified CMP. One consent flow must govern advertising consent.
  See `18-consent-and-privacy-deep-dive.md`.

## ads.txt setup

ads.txt (Authorized Digital Sellers) is an IAB Tech Lab standard
from 2017. It lists the accounts allowed to sell the site's ad
inventory. Buyers check it before bidding.

- Create a plain text file named exactly ads.txt, UTF-8, no BOM,
  no .html extension.
- Add the Google line from the AdSense account, in this form:
  `google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0`
  Replace the zeros with the real publisher ID from the account.
  Copy the line from the account, never from another site. A line
  copied from another site authorises that publisher's account.
- Add one line per seller. Keep every line the partner supplied,
  exactly as supplied. Never invent a line.
- Upload the file to the domain root so it loads at
  `https://example.com/ads.txt`. Not a subdirectory, not a
  subdomain, unless a subdomain declaration is used.
- Open the live URL in a browser and confirm it shows plain text.
  Check the account's ads.txt status after a day. Crawlers take
  time to recheck.
- Keep the file current. Remove lines for partners you no longer
  work with, and add lines when a new partner starts.
- A missing ads.txt file does not block approval by itself, but it
  reduces buyer trust and demand. Publish it as soon as the
  account exists.

## sellers.json

- sellers.json is the exchange-side complement to ads.txt,
  introduced by IAB Tech Lab in 2019. Each ad system publishes a
  file listing its seller accounts. Buyers cross-check ads.txt
  against sellers.json to verify the supply chain.
- Publishers do not create sellers.json. Google publishes it.
- In the AdSense account settings, publishers choose whether
  their name and domain appear in Google's sellers.json or stay
  confidential. Showing business details makes inventory more
  transparent to buyers. Either choice is allowed.
- Every DIRECT line in ads.txt should be an account the publisher
  owns. Every RESELLER line should come from a real partner.

## Site verification methods

When adding a site in AdSense, Google offers verification by:

- AdSense code snippet in the page head, on pages that get regular
  views.
- ads.txt file containing the publisher line.
- Meta tag in the page head, where offered.

Any one method verifies ownership. The code snippet method also
prepares the site for Auto ads. Leave the chosen verification in
place while the review runs.

## After setup, verify live

1. View the page source on the live site and find the AdSense
   code.
2. Open the ads.txt URL and read the file.
3. Open robots.txt and the sitemap and confirm they load.
4. Open the site on a phone and check layout, menus, and consent
   banner.
5. Run `scripts/site_audit.py` and fix every blocker before
   applying.
