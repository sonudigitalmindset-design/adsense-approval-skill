# Account architecture and graduation

Most publishers need exactly one AdSense account. Problems
start when that simple structure is bent: a second account to
escape a rejection, a country change handled by editing, or a
move to Ad Manager before the site needs it. This reference
explains what is fixed, what can change, and when graduation
to a bigger platform makes sense.

Read the eligibility basics in
`references/02-eligibility-and-application.md` and the
verification workflow in
`references/16-verification-and-payments-troubleshooting.md`.

## One account per payee

Google allows one AdSense account per payee. The rule is in
the Program policies and the Terms. It means one individual
or one organisation runs one account, and workarounds are
not a grey area.

- Do not create a second account after a rejection. Fix the
  site and reapply on the same account.
- Do not create a second account after a closure. A refused
  invalid traffic appeal means no new account. See
  `references/15-policy-center-and-appeals.md`.
- Do not create a second account for a second site. One
  account holds many sites. See the multi-site section below.
- Do not create an account in someone else's name to hold
  your earnings. Payee identity must match the person or
  organisation being paid, and identity verification will
  test that match.

## Multi-site structure

One account can monetise many sites. Each site goes through
its own review on the Sites page: add the site, verify
ownership, place the code, and request review. Approval of
one site does not approve the next.

- Keep each site's content and policy state independent.
  A violation on one site can affect the account, so a weak
  site is a risk to every site on the account, not only to
  itself.
- Subdomains need care. Google reviews sites at the domain
  level, and a subdomain may need to be added and reviewed
  separately. Do not assume a subdomain is covered because
  the root domain is approved. Check the Sites page and the
  live Help page for the current behaviour before placing
  code on a subdomain.
- Use one ads.txt file per domain, with the publisher line
  copied from the account. See
  `references/29-advanced-technical-implementation.md`.
- Do not move violating content to a subdomain to keep ads
  running. That is evasion, and it is treated as such.

## What is fixed after activation

Three things cannot simply be edited after an account is
activated. Google's Help pages state each of them. Verify the
current wording on the live pages before acting, because the
exact paths change.

- Payee country. The country chosen at sign-up cannot be
  changed inside the existing account. Moving countries
  means closing the existing account and creating a new
  account in the new country. Read the payments
  consequences in
  `references/28-payments-tax-and-edge-cases.md` before
  starting. For YouTube creators, contact Creator Support
  before starting the process, because the channel link
  is involved.
- Account type. Individual versus organisation is locked
  after activation. Changing type means cancelling the
  existing account and opening a new one. There is no
  difference in services or payment structure between the
  two types, so most publishers never need to change.
- Account ownership. An account cannot be transferred to
  another person. Selling a site does not transfer its
  AdSense account. The buyer needs their own account and
  their own site review.

## What can change, within limits

- Payee name. The payments profile name can be edited only
  for limited reasons, such as fixing a misspelling or
  reflecting a change from marriage, death, or a company
  merger. After identity verification, the normal edit may
  be locked and support contact may be needed. A name
  change is not a way to move an account to a new payee.
- Payment address. The address can be edited within the
  same country. Moving to a new country is not an address
  edit. It is the close and recreate path above.
- Payment method and tax information. Both can be updated
  in the account. Changes near the payment cycle cutoff
  apply to the next cycle. See
  `references/28-payments-tax-and-edge-cases.md`.
- Email and sign-in. The Google account that signs in to
  AdSense is fixed to the account. There is no supported
  path to move an AdSense account to a different Google
  account. Guard the sign-in account accordingly.

## When Ad Manager enters the picture

AdSense is the right tool for a publisher who monetises
through Google demand alone, with no direct deals, no
mediation, and no trafficking. Google publishes a comparison
of AdSense and Ad Manager. Read the live comparison before
deciding, because it is the correct entry point for stack
selection.

Ad Manager is a publisher ad server. It fits when a publisher
needs direct sold campaigns, multiple demand sources, complex
inventory rules, or team trafficking. It adds real operational
work. Moving to Ad Manager for the sake of moving is a cost
with no benefit.

Reported qualification for Ad Manager Small Business, the
free tier, is at least one million monthly pageviews tied to
an approved AdSense account. This figure comes from secondary
sources quoting Google's pages and is labelled reported.
Verify it on the live Ad Manager pages before planning
around it. Ad Manager 360 is a paid contract negotiated with
Google, not a self-serve signup.

## Multiple Customer Management (MCM)

MCM is a feature inside Ad Manager 360 that lets a parent
publisher manage a child publisher's account or inventory.
It replaced the older Scaled Partner Management program in
2021 to 2022. MCM is how smaller publishers reach Google Ad
Exchange demand through a Google Certified Publishing
Partner (GCPP).

Two delegation types exist. They work very differently, and
the choice affects who Google pays.

- Manage Account. The parent gets access to manage the
  child's own Ad Manager account. The child keeps ownership
  of the account. Google pays the child directly. The child
  can set the parent's revenue share, from 0 to 100 percent,
  to be sent automatically. A child can have only one Manage
  Account parent.
- Manage Inventory. The child delegates named inventory to
  the parent, who manages it through the parent's own Ad
  Manager account. Sites carry the parent's tags. Google
  pays the parent, and the parent pays the child under
  their commercial agreement. A child can have up to 15
  Manage Inventory parents, and can delegate different
  slices to different parents.

Facts to verify before signing anything, because partner
pages and Google pages describe them differently.

- Google does not publish a fixed traffic threshold for
  joining MCM. Eligibility is handled by Google and the
  partner. Any partner that quotes a Google threshold as
  fact should be asked for the live page.
- The revenue share is a commercial agreement between
  parent and child. The parent's share comes on top of
  Google's fees. Get the share, the payment timing, and
  the exit terms in writing before delegating.
- The child stays responsible for policy compliance on
  delegated inventory. A partner's settings do not shield
  the child from enforcement.
- Never hand over Google account credentials to a partner.
  MCM delegation happens inside Google's own invitation
  flow. A partner that asks for a password or an OTP is
  not following Google's process.

## The graduation decision, in one paragraph

Stay on AdSense while one account, Google demand, and simple
placements serve the site. Consider Ad Manager when direct
deals or multiple demand sources need an ad server and the
team can run one. Consider MCM only when Ad Exchange access
through a vetted partner is worth a revenue share and a
contract, and only after reading Google's own MCM pages.
Every step up adds power and adds work. Take it when the
site's size and deals demand it, not when a sales pitch
promises it.
