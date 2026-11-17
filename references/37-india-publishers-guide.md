# India publishers guide

India-specific AdSense facts: payments, tax forms, PIN
delivery, and consent law. The general rules still live in
`references/06-terms-and-payments.md`,
`references/16-verification-and-payments-troubleshooting.md`,
and `references/28-payments-tax-and-edge-cases.md`. Read
those first. This file adds only what is different or
confusing for publishers in India.

Nothing here is tax advice or legal advice. Tax and legal
points are general information. Confirm them with a
qualified professional in India before acting on them.

## Payment method: wire transfer only

OFFICIAL, read on the live AdSense Help page "Add your
payment method for AdSense or AdSense for YouTube" on
18 November 2026
(`support.google.com/adsense/answer/1714397`): the
country table lists India as Check No, EFT No, Wire Yes,
Hyperwallet No, for both AdSense and YouTube payment
accounts. Wire transfer is the only payment method
offered in India.

- Older guides that mention EFT, cheque, or Western Union
  for India are out of date. If a method is not shown on
  the "Add payment method" page, it is not available.
- Set up the method at Payments, then Payments info, then
  Manage payment methods, then Add payment method. The
  option appears once earnings reach the payment method
  selection threshold.
- The bank account name must match the payee name exactly.
  A mismatch gets the payment returned by the bank.
- Check the account number and SWIFT or BIC code with the
  bank, not from memory. Indian banks also use IFSC codes
  for domestic routing. Confirm with the bank which codes
  it needs for an incoming international wire, since
  requirements vary by bank. This is practice guidance,
  not a Google rule.
- Keep the bank account in India. Google's payments
  guidance says the bank must be in the same country as
  the payments address. Confirm this in the account
  before adding any foreign bank.

## Currency and thresholds

- Indian accounts are reported to use the US dollar
  thresholds: a 10 dollar trigger for address
  verification by PIN and a 100 dollar payment
  threshold. This is REPORTED from secondary sources.
  Confirm the figures in the account, since the account
  shows the threshold in the account currency.
- Payments are reported to be sent in US dollars and
  converted to rupees by the receiving bank at its own
  rate. This is REPORTED. Google does not set the
  conversion rate, and bank charges for receiving a wire
  vary by bank. Ask the bank about its receiving charges
  before the first payment.
- Earnings for a month are finalised in the first days of
  the following month, and payments go out in the 21st
  to 26th window when the balance has reached the
  threshold and no hold applies. See
  `references/16-verification-and-payments-troubleshooting.md`
  for the full calendar and hold list.

## Address verification and the PIN in India

The PIN process is the same worldwide. See
`references/16-verification-and-payments-troubleshooting.md`
for the full steps. India-specific notes:

- The PIN arrives by ordinary post at the payments
  address. Allow weeks for delivery. Indian postal
  delivery times vary widely by city and village.
- The address must be able to receive ordinary post.
  Check it before requesting a PIN. A wrong address
  wastes a request, and requests are limited, commonly
  reported as 3 in total.
- The PIN entry window is commonly reported as 4 months
  from the first mailing. The account shows the real
  deadline. That deadline controls, not any guide.
- If no PIN arrives after the allowed requests, the
  account may offer alternative verification, such as an
  address document. Follow what the account offers.

## Tax information: US forms, Indian identity

- Every publisher must submit tax information in the
  payments profile. Individuals outside the US generally
  use Form W-8BEN. Businesses generally use Form
  W-8BEN-E. US publishers use a different form. The
  account guides the choice.
- Without tax information, Google may withhold up to 24
  percent of worldwide YouTube earnings. With the form,
  withholding applies only to earnings from US viewers,
  at a rate set by treaty, from 0 to 30 percent. See
  `references/16-verification-and-payments-troubleshooting.md`
  and `references/28-payments-tax-and-edge-cases.md`.
- The India to US treaty rate for royalties is reported
  as 15 percent. This is REPORTED. Check the treaty
  table in the account flow and confirm with a tax
  professional.
- To claim a treaty benefit, Google requires a foreign
  tax identification number or a US tax identification
  number. For Indian publishers the foreign tax number
  is the PAN. This is REPORTED from secondary guides.
  Enter the PAN exactly as it appears on the PAN card,
  and keep the payee name matching the name on the PAN
  and the bank account. A name mismatch across PAN,
  payee name, and bank account is a common cause of
  rejected forms and returned payments.
- W-8 series forms expire, typically after three calendar
  years. This is REPORTED. Google notifies before
  expiry. Resubmit promptly to avoid new holds.
- US withholding is separate from Indian tax law. Income
  tax on AdSense earnings in India, and any GST
  questions, are Indian matters. This skill does not
  answer them. Ask a chartered accountant or tax
  professional in India.

## Consent law in India: the DPDP Act 2023

The Digital Personal Data Protection Act 2023 (DPDP Act)
is India's data protection law. The basics below are
REPORTED from secondary summaries read on 18 November
2026. They are general information, not legal advice.
The Act and its Rules are long, and implementation is
phased. Check the current position with a legal
professional before relying on any detail.

- The Act was passed by Parliament in August 2023 and
  received presidential assent on 11 August 2023.
- It covers digital personal data. The individual the
  data belongs to is the data principal. The entity
  deciding why and how data is processed is the data
  fiduciary. A website owner with visitors is usually a
  data fiduciary for the data the site collects.
- Processing generally needs consent that is free,
  specific, informed, and unambiguous, given after a
  clear notice. Consent can be withdrawn. Some
  processing is allowed without consent for specified
  legitimate uses.
- Data principals have rights including access to
  information about their data, correction and erasure,
  grievance redressal, and withdrawing consent.
- Processing the personal data of children, defined as
  anyone under 18, needs verifiable parental consent.
  This matters for any site aimed at children.
- The DPDP Rules 2025 were reported as notified in
  November 2025, with the main duties on data
  fiduciaries and the rights of data principals phased
  in, reported as taking effect in May 2027. Confirm the
  current dates before quoting them.
- Practical steps for a publisher, as practice guidance:
  keep a clear Privacy Policy in plain language, explain
  what data the site collects and why, name a contact
  for privacy questions and grievances, honour consent
  withdrawal, and do not collect data the site does not
  need. For advertising consent, the certified CMP rules
  for EEA, UK, and Swiss traffic still apply separately.
  See `references/18-consent-and-privacy-deep-dive.md`.

## Common India mistakes

- Expecting EFT, cheque, or PayPal. Only wire transfer
  is offered in India.
- Adding a bank account in another person's name. The
  name must match the payee name.
- Entering SWIFT or BIC details from memory. Confirm
  them with the bank.
- Leaving the tax form until the threshold. Withholding
  applies when earnings are finalised, so waiting costs
  money.
- Using a different name spelling on the PAN, the payee
  profile, and the bank account. Keep one exact legal
  name everywhere.
- Copying another publisher's ads.txt line. Copy the line
  from the publisher's own account. See
  `references/19-platform-setup-guides.md`.
