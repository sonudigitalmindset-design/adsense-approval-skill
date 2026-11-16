# Supported languages for AdSense

Status: OFFICIAL. Read on the live AdSense Help page
"Languages Google publisher products support" on
17 November 2026:
https://support.google.com/adsense/answer/9727

## The rule in one paragraph

Google publisher products support publishers in several
different languages. You select your site's primary
language during the sign-up process. If you are approved,
Google serves relevant ads to your pages in the
appropriate language, even if your site contains multiple
supported languages. Placing Google ad code on pages with
content primarily in an unsupported language is not
permitted by the Google Publisher Policies. The same
language rule appears in the Publisher Policies Help
Center under "Unsupported languages". Read the live list
before applying. Languages are added and removed over
time, and the live page wins over this file.

## The supported list as read on 17 November 2026

These languages are allowed to be the primary language
of a site or app. The markers match the footnotes on the
official page.

- Arabic [2]
- Bengali (Bangla) [2, 3]
- Bulgarian [2]
- Catalan [2, 3]
- Chinese (simplified)
- Chinese (traditional)
- Croatian [2]
- Czech
- Danish [2]
- Dutch
- English
- Estonian [1, 2, 3]
- Filipino [2]
- Finnish [2]
- French
- German
- Greek
- Gujarati [2, 3]
- Hebrew [2]
- Hindi [2, 3]
- Hungarian
- Indonesian
- Italian
- Japanese
- Kannada [2, 3]
- Korean
- Latvian [2]
- Lithuanian [2]
- Malay [2, 3]
- Malayalam [2, 3]
- Marathi [2, 3]
- Norwegian [2]
- Polish
- Portuguese
- Punjabi [2, 3]
- Romanian [2]
- Russian
- Serbian [2]
- Slovak [2]
- Slovenian [1, 2, 3]
- Spanish (European)
- Spanish (Latin American)
- Swedish [2]
- Tamil [2]
- Telugu [2]
- Thai
- Turkish
- Ukrainian [2]
- Urdu [2, 3]
- Vietnamese

Footnotes from the official page:

- [1] The AdSense product interface and help center are
  not currently available in this language.
- [2] The Ad Manager product interface and help center
  are not currently available in this language.
- [3] The AdMob product interface and help center are
  not currently available in this language.

The footnotes describe interface availability only. A
language with markers is still a supported primary
language for AdSense content.

## Languages not on the list

Several languages are absent from the list as read on
17 November 2026, including Odia, Assamese, and Nepali.
Absence means the language cannot be the primary
language of a site or app carrying AdSense. A site whose
primary content is in an unsupported language is not
eligible with that content. The honest options are to
publish the core content in a supported language, or to
keep every page written primarily in the unsupported
language free of Google ad code. Do not place ad code on
such pages and hope the review misses it. The rule is
written in the Publisher Policies.

## Multilingual sites

A site with several supported languages is allowed.
Google states that it serves ads in the appropriate
language for each page. The primary language is chosen
once, at sign-up. Practical guidance, not a Google rule:
keep the primary language dominant across the site, keep
each page in one language where possible, and set the
HTML lang attribute on every page to the language that
page is actually written in. A page that mixes two
languages in every sentence makes its primary language
hard to determine, which matches the "language cannot be
determined" wording in the rejection reasons in
`references/07-rejection-reasons-and-fixes.md`.

## Roman script content

The official list names languages, not scripts. Hindi
written in Latin letters (Roman Hindi, often called
Hinglish) is Hindi content in a different script. Google
does not publish a rule about which script a supported
language must use. Practice guidance, not a Google rule:
if the whole site is Roman Hindi, keep it consistently
Roman Hindi, set the HTML lang attribute honestly, and
expect automated language detection to work harder than
it would on Devanagari text. Do not mix scripts
randomly on core pages. When in doubt, write the most
important pages in the script your readers actually use
and keep the language consistent within each page.

## How to check before applying

1. Open the live supported languages page and confirm
   the site's primary language is on it.
2. Read every indexed page and confirm its primary
   language. One unsupported-language section does not
   cancel a supported site, but ad code must stay off
   those pages.
3. Check the HTML lang attribute on every template.
   The deep audit in `scripts/deep_audit.py` checks
   that the attribute exists on each page. It cannot
   judge whether the value matches the content. A human
   must read the page and confirm the match.
4. If the site was rejected for an unsupported
   language, read the exact wording in the account
   before changing anything. Fix the language problem
   itself. Adding more posts in the same unsupported
   language does not fix it.

## Sources

- Languages Google publisher products support, AdSense
  Help, read 17 November 2026:
  https://support.google.com/adsense/answer/9727
- Unsupported languages, Publisher Policies Help:
  https://support.google.com/publisherpolicies/answer/10436912?hl=en
