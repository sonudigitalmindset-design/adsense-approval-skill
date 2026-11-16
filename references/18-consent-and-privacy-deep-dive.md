# Consent and privacy deep dive

Consent rules for advertising, the certified CMP requirement, and
the privacy disclosures every AdSense site needs. This is general
information about Google's requirements, not legal advice. Privacy
law changes often. Confirm decisions with a qualified professional
when the stakes are real.

## The core rule

Google's EU User Consent Policy requires publishers to get legally
valid consent from visitors in the European Economic Area, the UK,
and Switzerland before using cookies or personal data for
personalised advertising and measurement. The policy implements
the GDPR and the ePrivacy Directive for Google's ad products.

## The certified CMP requirement

- Since 16 January 2024, publishers serving ads to EEA and UK
  visitors must use a Google-certified Consent Management Platform
  integrated with the IAB Transparency and Consent Framework (TCF).
- Switzerland was added on 31 July 2024.
- A certified CMP shows a standard consent dialog, records the
  choice, and produces a TCF consent string that Google's ad code
  reads. A homemade banner is not a certified CMP, even when it
  looks similar.
- Without a valid consent signal, Google serves only
  non-personalised ads to that traffic, and revenue from those
  visitors drops sharply. Repeated non-compliance can lead to
  enforcement.
- The requirement applies when the site can be visited from those
  regions, which is true for almost every public website.

## Funding Choices: Google's free certified CMP

- Funding Choices is Google's own certified CMP. It lives in the
  AdSense account under Privacy and messaging.
- Setup: create a European regulations (GDPR) message, target the
  site, publish it. Google serves the prompt to EEA, UK, and Swiss
  visitors through the existing AdSense code. No separate banner
  code is needed for those visitors.
- Offer a real choice: consent, do not consent, and manage
  options. A banner with only an Accept button is not valid
  consent.
- Let visitors change or withdraw consent later, through the
  controls in the message or a privacy settings link.
- Funding Choices also offers messages for US state privacy laws.
  Enable them when the site has US traffic and the account offers
  the option.
- Third-party certified CMPs (for example Cookiebot, OneTrust,
  CookieYes, and Didomi) also meet the requirement. Pick one CMP
  and configure it properly. Do not run two consent banners at
  once.

## TCF v2.2 and Consent Mode v2

- TCF v2.2 is the current version of the IAB framework. Certified
  CMPs must use it. Older TCF versions are no longer accepted.
- Google Consent Mode v2 sends four consent signals: ad_storage,
  ad_user_data, ad_personalization, and analytics_storage. For EEA
  traffic, these must default to denied until the visitor chooses.
- When Funding Choices is used, Google wires Consent Mode
  automatically for its own tags. With a third-party CMP, check
  that Consent Mode is configured and that tags fire only after
  consent.
- Test from an EEA location or with a VPN: the CMP banner must
  appear on first visit before ad and analytics tags set cookies.

## Non-personalised ads

- When a visitor declines consent, Google can still serve
  non-personalised ads, which use contextual signals instead of
  personal data.
- Non-personalised ads earn less on average, but they keep the
  page compliant and keep some revenue.
- Publishers can also choose to serve only non-personalised ads to
  all EEA traffic. That is a business choice, not a compliance
  shortcut for skipping the CMP.

## The Privacy Policy disclosure

Every AdSense site needs a Privacy Policy that, in plain language:

- Names the site operator and how to contact them.
- Explains that third-party vendors, including Google, use cookies
  to serve and measure ads based on visits to this and other
  sites.
- Explains that Google's use of advertising cookies enables it and
  its partners to serve ads based on visits.
- Tells users they can opt out of personalised advertising through
  Google Ads Settings, and links to it.
- Describes any other data the site collects: contact forms,
  comments, newsletters, and analytics, with what is stored and
  why.
- States how users can ask for access, correction, or deletion of
  their data, and how consent choices can be changed.
- Carries a last-updated date and is updated when practices
  change.

Do not copy a template unchanged. A policy that describes
practices the site does not follow, or omits practices it does
follow, is worse than a short honest one. See
`examples/privacy-policy-outline.md` for a structure to adapt.

## US state privacy laws

- Several US states have privacy laws giving residents rights over
  personal data, including opt-out rights for sale and sharing.
- Google offers US-state messages in Funding Choices and a
  restricted data processing setting for affected traffic.
- Do not guess which states apply. Read the current Funding
  Choices help and, for a site with real US traffic, get
  professional advice.

## Children and sensitive data

- Do not serve personalised ads on content directed at children.
  Google treats child-directed content under strict rules,
  including COPPA in the US.
- Never collect data from children knowingly, and never build
  content designed to attract children while running personalised
  ads.
- Do not pass sensitive personal data (health, precise location,
  or similar) to advertising systems. Keep analytics and ad data
  separate from any sensitive collection.

## Consent checklist before applying

- Privacy Policy published with the advertising disclosure.
- Certified CMP configured and published for EEA, UK, and Swiss
  traffic.
- CMP banner tested from a regulated region.
- Ad and analytics tags gated behind consent in those regions.
- Consent choices changeable after the first visit.
- Policy text matches what the site actually does.
