# Eligibility and application

Source of truth: Google AdSense Help, "Eligibility requirements for
AdSense" (`support.google.com/adsense/answer/9724`) and "Connect your
site to AdSense" (`support.google.com/adsense/answer/7584263`). Last
checked against live pages: November 2026. Recheck before quoting.

## The four official eligibility checks

1. **Your own unique and interesting content.** Content must be
   high-quality, original, and attract an audience. Google publishes no
   minimum number of posts, words, visitors, or months online.
2. **Program policy compliance.** The site must comply with the AdSense
   Program policies before signing up. Google may change policies at any
   time, and keeping up to date is the publisher's responsibility under
   the Terms and Conditions.
3. **Age 18 or over.** Applications are accepted only from applicants
   aged 18 or over. If the creator is under 18, a parent or guardian
   may sign up using their own Google Account, and payments go to them.
4. **Access to the site's HTML.** The applicant must be able to place
   AdSense code between the `<head>` tags of the site's pages. Signing
   up with a site the applicant does not own fails verification.
   Content management systems may offer a plugin, theme setting, or
   host-partner route instead of direct code editing.

Additional practical requirements from the Help pages:

- A Google Account, and a payment country/territory where AdSense is
  available. AdSense is not open in every country, so check the
  supported list before building a plan.
- One AdSense account per payee. A duplicate account is a common
  account-level problem. Do not create a second account to work around
  a rejection or a disabled account.
- For Blogger or another host partner, a hosted AdSense account route
  exists. For YouTube, apply through the YouTube Partner Programme in
  YouTube Studio and sign up for AdSense for YouTube there. Website
  approval and YouTube approval are separate paths.

## Myths that are not official rules

| Claim | Status |
|---|---|
| You need 15, 20, or 30 posts | Not published by Google. Publish enough genuinely useful content for a whole-site review. |
| Every post needs 1,000+ words | Not published by Google. Length should match what the topic needs. |
| The domain must be 6 months old | Not a universal published rule. |
| You need a set amount of traffic | No published traffic minimum for applying. |
| You need Google Analytics or Search Console first | Neither is required to apply. Search Console helps check indexing. |
| A trick or paid service guarantees approval | No trick exists. Google reviews every site against the same rules. |

Community practice (not a rule): many publishers wait until the site
looks finished, has a clear niche, has trust pages live, and has some
pages indexed in search before applying. Treat any specific number as
an editorial habit, not a requirement.

## Application steps in order

1. Sign up at AdSense with the Google Account that will own the
   account. Add the site URL and choose the payment country carefully.
   The payment country generally cannot be changed later.
2. Add the site on the Sites page if it is not already there.
3. Choose a verification method:
   - **AdSense code snippet:** paste it into the HTML between the
     `<head>` and `</head>` tags of every page that should show ads.
     Place it on a page that gets regular views.
   - **Ads.txt snippet:** paste the code into the ads.txt file and
     upload it to the site root directory.
   - **Meta tag:** where offered, place the verification meta tag in
     the page head. It verifies ownership and displays nothing.
4. Confirm placement, click Verify, then click Request review.
5. Leave the code in place. Removing it can unverify the site.
6. Publish ads.txt at the site root. The file names the companies
   allowed to sell the site's inventory. The AdSense line includes the
   publisher ID and the word DIRECT. Verify it loads at
   `https://example.com/ads.txt` (replace with the real domain).
   Google calls ads.txt highly recommended rather than mandatory, but
   a missing or wrong file puts earnings at risk after approval.
7. Wait for the review. Google reviews the entire site, not only the
   page with the code. This usually takes a few days, but in some cases
   takes 2 to 4 weeks. Check status on the Sites page.

Two official setup facts, read on the live AdSense Help page
"Complete your AdSense account setup" on 17 November 2026:

- The site must be live and contain enough content for Google's
  specialists to evaluate. If the site is under construction,
  does not load, or is difficult to navigate, Google cannot set
  up the account.
- There are 6 months to complete the account setup steps. If the
  account is not set up after 6 months, the account is
  deactivated. This is a setup deadline, not a domain age rule.
  It says nothing about how old the domain must be before
  applying.

## Site statuses to recognise

- **Getting ready:** setup tasks are incomplete. Finish them before
  expecting a review.
- **Requires review / Needs review:** the site has not been checked
  yet. Request review once the code is verified.
- **Needs attention:** the site was reviewed and a problem was found.
  Read the reason shown next to the domain before changing anything.
- **Ready:** the site passed review and ads may serve.

Removing and re-adding a site can delay the process. Do not do it to
chase speed.

## After approval: verification and payment setup

Approval to show ads is not the end of setup. The account also needs:

- **Identity verification** when Google asks for it, inside the
  deadline shown in the account. Name and address details must match
  the documents supplied.
- **Address verification by PIN.** A PIN is mailed by post after the
  account reaches the verification earnings level shown in the
  account. Enter it inside the deadline shown. Keep the postal address
  accurate.
- **Payment details:** bank account or other payment method supported
  in the payment country, plus any tax information Google requests.
  Tax forms vary by country. For non-US publishers earning from US
  viewers, US tax withholding rules may apply; check the live tax pages
  in the account rather than relying on a blog figure.
- **Payment threshold:** the balance must reach the published payment
  threshold (US $100 or the local equivalent) before a payment is
  issued. Earnings are finalised early in the month, and payments are
  typically issued between the 21st and 26th when the threshold was
  reached. Confirm the current threshold and cycle on the live Help
  pages.

See `06-terms-and-payments.md` for the contract and payment detail.
