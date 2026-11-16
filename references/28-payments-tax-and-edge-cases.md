# Payments, tax, and edge cases

Most payment problems are verification problems in disguise.
This reference covers the holds that block payment, the tax
forms that affect withholding, the edge cases that catch
experienced publishers, and what support can and cannot do.

Read the terms and payment basics in
`references/06-terms-and-payments.md` and the troubleshooting
workflow in
`references/16-verification-and-payments-troubleshooting.md`.
Figures from secondary sources are labelled reported, and the
account's own shown figures always win.

## The payment cycle, stated carefully

Earnings finalise after the month ends. Payment runs in the
21st to 26th window of the following month, reported. Changes
to payment details made before about the 20th typically apply
to that month's payment, reported. The payment threshold is
US $100 or the local equivalent. A balance below the threshold
carries forward. These are the standard figures. The account's
Payments page shows the figures that govern a real payment,
and it wins over any remembered number.

## Holds, one by one

A hold blocks payment until its cause is fixed. Holds can
stack. Fixing one hold does not clear the others. The
Payments page lists active holds. Check it before assuming
a payment is late.

- Identity hold. Identity verification is incomplete or
  failed. Fix it through the verification flow in the
  account, with documents that match the payments profile
  exactly. See
  `references/16-verification-and-payments-troubleshooting.md`.
- Address hold. The PIN has not been entered. The PIN is
  mailed after earnings reach about $10 equivalent,
  reported. Entry windows and re-request counts are shown
  in the account and are reported in
  `references/16-verification-and-payments-troubleshooting.md`.
- Payment method hold. No valid payment method is on file,
  or the method failed. The bank account name must match
  the payee name. In India the payment method is wire
  transfer only, reported.
- Tax information hold. Tax forms are missing or incomplete.
  See the tax section below.
- Policy hold. A policy action on the account blocks
  payment. The Policy Center states the cause. No payment
  fix clears a policy hold. The policy issue must be fixed
  first.

When a payment does not arrive, list the holds before doing
anything else. "Payment is late" is not a diagnosis. "One
hold, tax information, since 12 March" is.

## Tax forms and withholding

Tax information is collected in the account, and it affects
withholding on some earnings. The forms depend on who the
payee is.

- US persons submit Form W-9.
- Non-US individuals submit Form W-8BEN.
- Non-US entities submit Form W-8BEN-E.
- Treaty benefits are claimed on the form where a tax treaty
  applies. The India to US treaty royalties rate is reported
  at 15 percent. Verify the current treaty position on the
  live tax pages and with a tax adviser, not from memory.
- Without tax information, withholding of up to 24 percent
  on worldwide YouTube earnings is reported. US tax
  withholding mainly bites YouTube earnings, which are
  treated as royalties. Keep tax information current in all
  cases, and read the live tax Help pages for the current
  scope.

Practical rules that prevent most tax problems.

- Submit tax information as soon as the account asks for
  it. Do not wait for the first payment to approach.
- Resubmit tax information after a payee name change,
  because the tax form name is copied from the payments
  profile. This is reported practice from Google's Help
  pages. Verify the current instruction on the live page.
- Keep the legal name identical across the payments
  profile, the tax form, the bank account, and the identity
  document. A mismatch in any one of them can stall payment
  or verification.
- This skill is not tax advice. Treaty claims, entity
  classification, and withholding questions belong to a
  qualified tax adviser in the publisher's country.

## Closing an account and the final payment

Closing an account is a one-way action. Read the live Help
page on closing an account before starting, and contact
support about the unpaid balance where the page advises it.

- A final payment is issued when the balance is above the
  cancellation threshold and verification is complete.
  The cancellation threshold is reported at $10 or the
  local equivalent, and the final payment is reported to
  arrive within about 90 days after the end of the month
  of closure. Both figures are reported. The live Help
  page and the account's own messages govern a real case.
- A failed payment returns to the balance. A wire transfer
  that is cancelled by the bank is credited back, and the
  payment method must be fixed before the next cycle.
- Accounts terminated for Terms violations are treated
  differently under the Terms. Support wording in the
  individual case governs whether any balance is paid.
  Do not generalise one case's outcome into a rule.
- Never close an account to escape a limit, a failed
  verification, or a policy flag. Closure does not reset
  history, and a new account for the same payee is not
  allowed after a termination.

## Edge cases that catch experienced publishers

- Country moves. The payee country cannot be changed
  inside an existing account. The path is close and
  recreate, with the final payment rules above. See
  `references/27-account-architecture-and-graduation.md`.
- Account type changes. Individual versus organisation is
  locked after activation. The path is cancel and reapply.
  There is no difference in services or payment structure
  between the types.
- Payee name changes. Limited to fixing a misspelling or
  reflecting marriage, death, or a company merger. After
  identity verification, the edit may be locked and support
  contact may be needed. Resubmit tax information after a
  name change.
- Reporting currency. The currency is chosen at sign-up.
  Changing it is not offered in the account. Verify the
  current position on the live Help page before planning
  around a currency change.
- Deceased payee. Google has a separate process through
  support for a deceased publisher's account. Do not
  attempt to transfer the account or keep operating it
  under the deceased payee's name. Contact support and
  follow the process they describe.
- Multiple payments profiles. Creating extra profiles to
  dodge a failed verification is not advised. A new
  profile can inherit the failed state of the old one,
  and the tangle takes longer to unwind than the original
  problem. Fix verification on the profile that holds the
  earnings.
- Bank changes. Update the payment method before the
  cycle cutoff, and confirm the new method shows as the
  primary method. A payment sent to a closed bank account
  returns to the balance, but the cycle is lost.

## What support can and cannot do

Support can explain a hold, confirm what a notice means,
route a case to a specialist team, and describe the
correct process. Support cannot promise a timeline that
Google does not publish, bypass identity verification,
change a policy decision by chat alone, or lift a limit
on request. Outcomes arrive by email on the case thread.
Keep every case thread in one place, reply on the same
thread, and keep the dated log described in
`references/15-policy-center-and-appeals.md`.

## The pre-payment checklist

Run this before every payment cycle when a payment matters.

- No holds on the Payments page.
- Identity verification complete.
- PIN entered and address verification complete.
- Payment method valid, primary, and name-matched.
- Tax information submitted and current.
- Balance above the threshold.
- Policy Center clear of account level issues.

If all seven pass and no payment arrives in the cycle
window, the next step is a support contact with the
specifics: the cycle dates, the balance, the holds list,
and the payment method status. General complaints without
specifics get general answers.
