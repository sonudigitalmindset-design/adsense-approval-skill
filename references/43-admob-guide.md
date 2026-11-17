# AdMob guide

AdMob is Google's advertising platform for mobile apps. It is a
separate product from AdSense for Content, with its own account, its
own Help Center, and its own policy surface. This file covers app
setup, ad units, mediation, app-ads.txt, and the key differences from
AdSense for Content. Official claims below come from AdMob Help pages
read live on 18 November 2026. Status of those claims: OFFICIAL.

## Signing up

Source: AdMob Help, "Sign up for AdMob" (answer 7356219).

- Signup has three steps: create an AdMob account, verify the Google
  Account by phone, and enter payment details.
- Use the Google Account associated with an existing publisher account
  where one exists, so the publisher identity stays consistent.
- The country chosen at signup cannot be changed later. Choose it
  carefully, because it fixes the account's country and currency
  treatment.
- Account verification typically takes up to 24 hours, and rarely up
  to two weeks. Do not treat a wait of a few days as a rejection.

## Setting up an app and ad units

- An app is registered in AdMob and linked to its store listing (Google
  Play or the App Store) where the store supports it. Each app gets its
  own app ID.
- Ad units sit inside the app. Each ad unit has a format and a
  placement, and the app's code requests ads from the ad unit using
  the Google Mobile Ads SDK.
- The SDK must be integrated into the app before ads can serve. Ads do
  not appear by adding a snippet to a web page. AdMob is app-only.
- Test ads must be used during development. Clicking or viewing your
  own live ads during testing is invalid traffic, the same risk as on
  AdSense for Content. See `05-invalid-traffic-guide.md`.

## Mediation basics

Source: AdMob Help, "Mediation overview" (answer 13420272).

- Mediation lets an app request ads from multiple ad networks through
  AdMob, instead of from AdMob alone. The aim is higher fill and
  better competition for each impression.
- Two mechanisms are described on the page: bidding, where networks
  bid in real time for each impression, and waterfall, where networks
  are called in a fixed order until one fills the request. Hybrid
  setups combine both.
- Mediation is organised into mediation groups. Each group is defined
  by format, platform, app, ad unit, and country targeting.
- The page lists five setup steps: create a mediation group, add ad
  sources, set the bidding or waterfall order, configure the ad
  sources in their own dashboards, and test the integration before
  release.
- Mediation adds moving parts. Each ad source needs its own account,
  its own SDK adapter, and its own policy compliance. A mediation
  setup with a non-compliant ad source can put the whole app at risk.

## app-ads.txt

Sources: AdMob Help, "Set up app-ads.txt" (answer 9363762), read via
official search results on 18 November 2026, and the AdMob developer
documentation on app-ads (`developers.google.com/admob/android/app-ads`).

- app-ads.txt is the app equivalent of ads.txt. It is an IAB
  initiative that lets advertisers verify which ad sources are
  authorised to sell an app's inventory.
- It is not mandatory, but it is highly recommended. Missing
  app-ads.txt does not block ads, but it can reduce advertiser trust
  and demand.
- The file is hosted at the root of the developer website listed for
  the app. A Firebase Hosting alternative exists for developers
  without a website.
- AdMob crawls the file, with the Help page describing a 24-hour crawl
  cycle. Changes are not instant.
- The file lists authorised sellers in the same format family as
  ads.txt. Copy the lines from the AdMob account, never from another
  app's file.

## Child-directed content and families policy

Source: AdMob Help, "Comply with Google Play's families policy using
AdMob" (answer 6223431), read via official search results on 18
November 2026, and the AdMob release notes announcement of May 2026
(answer 15269273), read via official search results on 18 November
2026. Status: OFFICIAL for the Help article, REPORTED for the
announcement entry, which sits under the page's previous release
notes section.

- If an app targets children and shows ads, it must comply with Google
  Play's families policy. AdMob provides tools for this, but the
  developer remains responsible for compliance.
- Apps designed specifically for children, where only child age groups
  are selected in Play Console, receive families policy-compliant ads
  automatically for all ad requests from the app.
- Mixed-audience apps, where child and older age groups are both
  selected, must tag ad requests served to children and set the
  maximum ad content rating to G.
- All Android apps classified as Families must use a Google Play
  Families self-certified ads SDK or mediation platform when serving
  ads to children or users of unknown age. AdMob blocks ad sources
  that have not been self-certified from serving in those flows.
- The current SDK control is Tag for age treatment (TFAT). It replaces
  the older tag for child-directed treatment (TFCD) and tag for users
  under the age of consent (TFUA). TFAT values are CHILD, TEEN (new),
  and UNSPECIFIED (the default). The announcement encourages migration
  and says the legacy tags continue to work through 2026. It also
  advises consulting legal counsel on child-privacy obligations.
- The Help article copy read for this file still shows the older
  method names. Follow the current SDK documentation for the exact
  calls, and recheck the Help article before implementing.
- For the full child-directed section, including the web and YouTube
  angles, see `04-publisher-restrictions.md`.

## Key policy differences from AdSense for Content

Status: practice summary built from the AdMob Help pages above and
from `03-publisher-policies.md`. Recheck the live policy pages before
relying on any point.

- **Surface:** AdSense for Content serves ads on web pages. AdMob
  serves ads inside mobile apps through an SDK. A website cannot use
  AdMob, and an app cannot use AdSense for Content.
- **Account:** AdMob has its own account and approval flow. An
  approved AdSense account does not automatically approve an AdMob
  account, and the two balances and payment profiles are separate.
- **Store policy layer:** an app must satisfy Google Play or App Store
  policies as well as AdMob policies. A store rejection or removal
  stops ads even when the AdMob account is in good standing.
- **Families layer:** child-directed rules are a first-class policy
  surface in AdMob, with SDK tags, content ratings, and self-certified
  SDK requirements. On the web, child-directed content is handled
  through the publisher restrictions and consent rules instead.
- **Invalid traffic:** the same core rules apply. Do not click your
  own ads, do not incentivise clicks, and do not buy traffic. Test ads
  exist for development. The invalid traffic appeal form is shared
  between AdSense and AdMob. See `05-invalid-traffic-guide.md`.
- **ads.txt versus app-ads.txt:** the web uses ads.txt at the site
  root. Apps use app-ads.txt at the developer website root. The two
  files serve the same verification purpose on different surfaces.

## Before applying

- The app must be published or in a testable state with real
  functionality. A placeholder app with no content is the app
  equivalent of a thin website.
- Test ads must be used during development, and live ads must only be
  requested from the released app.
- If the app targets children or a mixed audience, the families
  compliance work comes first, before any ad integration is switched
  on.
- Set up app-ads.txt early, so the crawl has time to pick it up before
  the app scales.
