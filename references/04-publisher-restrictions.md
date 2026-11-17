# Google Publisher Restrictions: restricted content

Source of truth: Google Publisher Restrictions
(`support.google.com/adsense/answer/10437795`). Recheck the live page
before quoting the list, because categories and wording change.

## Prohibited versus restricted

- **Prohibited** content (see `03-publisher-policies.md`) gets no ads
  at all.
- **Restricted** content may carry AdSense code, but it will likely
  receive less advertising than other content, because fewer
  advertising sources are eligible to bid on it. Some restricted
  categories may receive no ads in practice.
- A site built mainly around restricted topics is a weak approval
  candidate even when nothing is prohibited. Isolate restricted pages,
  keep them a small part of the site, and expect lower demand on them.

## Restricted categories

The list below summarises the restriction categories. Wording is
paraphrased; the official page controls.

1. **Sexual content:** sexual content, sexual entertainment, sexual
   products, sexual health supplements, and sexual advice. Distinct
   from sexually explicit content, which is prohibited.
2. **Shocking content:** graphic, violent, disgusting, or distressing
   material, and prominent obscene language.
3. **Explosives:** explosives and instructions relating to them.
4. **Guns and other weapons:** firearms, firearm parts, other weapons,
   and instructions to obtain, assemble, or improve them.
5. **Tobacco:** tobacco products and related promotion.
6. **Recreational drugs:** recreational drugs, drug paraphernalia, and
   instructions for drug production or use.
7. **Alcohol:** online sale of alcohol and promotion of irresponsible
   drinking. Factual, responsible discussion is treated differently
   from sales and promotion; check the live wording.
8. **Online gambling:** online casinos, betting, and gambling
   promotion, subject to local law and certification rules.
9. **Prescription drugs:** prescription-drug sales, online pharmacies,
   unapproved drugs or supplements, and related promotion.
10. **Other restricted inventory:** categories Google adds or revises
    over time, including certain financial products, political content
    rules in specific regions, and app-related restrictions such as
    delisted apps. Always read the current page.

## How to handle a restricted niche

- Decide before building: if the whole niche is restricted, AdSense
  alone is unlikely to be a strong income source. Consider whether the
  niche is the right choice at all.
- Keep restricted pages clearly separated from the main content, with
  honest titles and no sensational framing.
- Do not mix restricted content into otherwise clean pages to chase
  traffic, and do not use restricted keywords as clickbait on clean
  pages.
- Follow local law first. A category that is legal in one country may
  be illegal in another, and AdSense availability and advertiser demand
  follow local rules.
- For health, finance, and legal topics (often called YMYL, "your
  money or your life"), restricted status is only part of the story.
  Reviewers also weigh expertise, sourcing, and accuracy heavily. See
  `09-content-quality-guide.md`.

## Common confusion

- "Restricted" does not mean "banned, but try anyway." It means fewer
  advertisers, lower fill, and lower earnings on those pages.
- "My competitor runs ads on this topic" proves nothing. Their account,
  region, page mix, and enforcement history are different, and their
  ads may be limited without it being visible.
- Removing ads from one restricted page does not make the rest of the
  site immune. Reviewers judge the whole site.

## Child-directed content

This section covers content directed at children and content in apps
and videos that reaches a child audience. The rules differ by surface,
so read the part that matches the product being used.

### On the web and in AdSense for Content

Status: general guidance, not a directly verified policy quote. The
specific ad limitations for a given page are set by the platform rules
and the law of the audience's region, so recheck the live policy pages
before relying on this summary.

Content made for children is not prohibited, but it carries extra
obligations. Child-privacy law, including the US Children's Online
Privacy Protection Act (COPPA) and equivalent rules in other regions,
limits what data can be collected from children and what advertising
can be shown to them. Google's publisher policies and consent rules
sit on top of those laws. In practice this means:

- Personalised advertising is limited or unavailable on content
  directed at children. Expect lower demand and lower earnings on
  those pages.
- Consent handling is stricter. Consent must come from a parent or
  guardian where the law requires it, and the consent flow must match
  the rules of every region the audience lives in.
- A site that mixes general content with child-directed content must
  keep the two clearly separated, with honest titles and no attempt to
  present child-directed pages as general-audience pages.
- This file is not legal advice. Child-privacy law varies by country
  and changes over time. Check the current rules with a qualified
  professional before building a child-directed site or section.

### In apps and AdMob

Source: AdMob Help, "Comply with Google Play's families policy using
AdMob" (answer 6223431), read via official search results on 18
November 2026, and the AdMob release notes announcement of May 2026
(answer 15269273), read via official search results on 18 November
2026. Status: OFFICIAL for the Help article, REPORTED for the
announcement entry.

- Apps that target children and show ads must comply with Google
  Play's families policy. AdMob provides tools for this, but the
  developer remains responsible for compliance.
- Apps designed specifically for children receive families
  policy-compliant ads automatically when only child age groups are
  selected in Play Console.
- Mixed-audience apps must tag ad requests served to children and set
  the maximum ad content rating to G.
- All Android apps classified as Families must use a Google Play
  Families self-certified ads SDK or mediation platform when serving
  ads to children or users of unknown age.
- The current SDK control is Tag for age treatment (TFAT). It replaces
  the older tag for child-directed treatment (TFCD) and tag for users
  under the age of consent (TFUA). TFAT values are CHILD, TEEN (new),
  and UNSPECIFIED (the default). The legacy tags continue to work
  through 2026, and migration is encouraged. The announcement advises
  consulting legal counsel.
- For the full AdMob treatment, see `43-admob-guide.md`.

### On YouTube

YouTube creators mark each video or channel as made for kids where
that is accurate. The designation changes which features are available
and which ads can serve. A video that a child could watch is not
automatically made for kids. The test is whether children are the
intended audience, judged by subject matter, characters, and
presentation. Mis-marking in either direction is a policy risk. See
`17-youtube-and-other-products.md` for the YouTube overview.

### What not to do

- Do not present child-directed content as general-audience content to
  get fuller ad demand. The audience declaration is a compliance
  statement, not a setting to tune for earnings.
- Do not collect data from children beyond what the law and the
  platform rules allow.
- Do not rely on an SDK tag alone for compliance. The tag, the content
  rating, the self-certified SDK, and the store declaration all have
  to match the real audience.
