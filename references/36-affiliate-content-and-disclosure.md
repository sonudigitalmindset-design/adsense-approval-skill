# Affiliate content and disclosure

Status: OFFICIAL for the Search Central spam policy and
link qualification rules, read live on 17 November
2026. The Search rules are NOT AdSense approval rules,
but a site that lives by them is easier to review and
harder to mistake for a thin site. The link between
thin affiliate content and an AdSense low-value-content
decision is inference from rejection patterns, not a
Google statement. Disclosure rules from regulators are
labelled separately below.

## Thin affiliation

Google's spam policies for web search define thin
affiliation as publishing content with product affiliate
links where the product descriptions and reviews are
copied directly from the original merchant without any
original content or added value. The policy covers
cookie-cutter pages distributed across a network of
sites, where each site adds nothing of its own.

The same policy says that not every site in an
affiliate program is a thin affiliate. Good affiliate
sites add value, for example with additional
information about price, original product reviews,
rigorous testing and ratings, navigation of products
or categories, and product comparisons. The line is
value added by the publisher. Copying the merchant's
text and adding a buy button does not cross it.

Read the live policy before acting:
https://developers.google.com/search/docs/essentials/spam-policies

## Qualifying outbound links

Google's guide to qualifying outbound links states that
regular links need no rel attribute. Three values
matter for publishers:

- rel="sponsored" for advertisements or paid
  placements. Google urges publishers to mark paid
  links with sponsored or nofollow.
- rel="ugc" for user-generated content links, such as
  links in comments and forum posts. The value can be
  removed for consistently high-quality contributors.
- rel="nofollow" when the other values do not apply
  and the publisher would rather Google not associate
  the site with the linked page.

Multiple values can be combined on one link. Links
marked with these values are generally not followed,
but the linked pages may still be found through
sitemaps or other links. The link spam policy states
that paid links are not a violation as long as they
are qualified with rel="nofollow" or rel="sponsored".

REPORTED: a link spam update in July 2021 urged
publishers to use rel="sponsored" on affiliate links
specifically. This comes from secondary summaries of
the update, not from a page read live for this file.
The qualification rule itself is official and is
enough to act on. Use rel="sponsored" on every
affiliate link. It is the value Google designed for
paid placements.

Read the live guide before acting:
https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links

## Disclosure to readers

Link qualification tells Google the link is paid.
Disclosure tells the reader. Both are needed.

In the United States, the Federal Trade Commission
requires clear and conspicuous disclosure of paid
relationships, including affiliate commissions. This
is a regulator rule, not a Google rule. Other markets
have their own regulators and their own rules. Check
the current rules for the market the site publishes
in, and read the current guidance before relying on
any summary.

Affiliate programs add their own requirements.
Amazon Associates, for example, has its own
disclosure wording requirement in its operating
agreement. Read the current agreement for the exact
text. Program rules change, and the live agreement
wins over any summary.

Practice guidance, not a Google rule: place a short
disclosure near the top of the page, before the first
affiliate link, in plain words a reader cannot miss.
One line is enough when it is visible. A disclosure
buried at the bottom of a long page, hidden in a
footer, or written in vague words does not serve the
reader. Do not present an affiliate review as an
independent test when the product was never tested.
That is a trust problem first and a policy problem
second.

## What the audit script checks

The deep audit in `scripts/deep_audit.py` runs three
affiliate checks. All three are practice heuristics,
never Google rules:

1. It counts outbound links to known affiliate
   networks and large affiliate programs, including
   Amazon, Flipkart, Impact, ShareASale, Commission
   Junction, Awin, ClickBank, Digistore24, JVZoo,
   Skimlinks, Partnerize, and Tradedoubler.
2. It flags a page that carries affiliate links but
   no disclosure wording. The wording list includes
   affiliate, commission, we may earn, paid link,
   sponsored link, and similar phrases. A human must
   judge whether the disclosure found is visible or
   buried.
3. It flags a page that carries affiliate links with
   no sponsored and no nofollow links at all. Google
   accepts either qualification, so the check only
   flags when neither is present.

A page with affiliate links and a visible disclosure
passes the check. A page with no affiliate links is
unaffected. A failed fetch is unverified, never proof
that a link or disclosure is absent.

## Fix checklist

1. Write original reviews from real use or real
   research. Never copy merchant descriptions.
2. Add value the merchant page does not have: a
   comparison, a price history note, a test result,
   or a clear recommendation with reasons.
3. Mark every affiliate link with rel="sponsored".
4. Place a short disclosure near the top of every
   page that carries affiliate links.
5. Keep the ratio honest. A site whose every page is
   an affiliate page with no other content reads as a
   thin affiliate site. Publish useful content that
   earns no commission alongside the affiliate pages.

## Sources

- Spam Policies for Google Web Search, Search
  Central, read 17 November 2026:
  https://developers.google.com/search/docs/essentials/spam-policies
- Qualify your outbound links, Search Central, read
  17 November 2026:
  https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links
