# Advanced decision playbooks

Ten hard situations, each with the same shape: the symptom,
the first checks, the actions in order, what not to do, and
the stop rule that says when waiting is the correct action.
These playbooks are generic. They contain no one's account
details, and no playbook promises an outcome.

For the full method behind each playbook, follow the linked
reference. For the symptom index, start at
`references/20-troubleshooting-index.md`.

## 1. Ad serving limited

Symptom: Policy Center shows an account level ad serving
limit. Earnings drop sharply. The account stays accessible.

First checks: read the exact wording, whether it says
"account being assessed" or "invalid traffic concerns",
and the date it appeared. Check reports for the two weeks
before the limit.

Actions in order: audit traffic sources, stop every risky
source, check placements for accidental click risk, confirm
no one clicks live ads, keep publishing, keep code in place,
keep a dated log.

What not to do: do not submit the invalid traffic appeal
form, do not remove and re-add the site, do not open a
second account, do not pay anyone to lift the limit.

Stop rule: after the audit and the stops, wait for the
automatic review. The Help page states the limit typically
lasts less than 30 days but may take longer. Checking the
Policy Center weekly is enough.

Full method:
`references/24-ad-serving-limits-and-enforcement-levels.md`

## 2. Sudden earnings drop with no notice

Symptom: earnings fall sharply. The Policy Center shows no
issue. No rejection, no limit, no email.

First checks: segment reports by page, country, and device.
Check ads.txt live. Check consent handling. Check that the
site loads and ads render in a fresh browser session.
Compare with the same period last year for seasonality.

Actions in order: fix any technical break found, fix any
consent break found, then wait one full week before
concluding anything. Measurement changes can move
impression counts without moving traffic.

What not to do: do not change placements, ad load, and
blocking controls on the same day. One change at a time,
or the cause stays unknown.

Stop rule: if every check passes and the drop matches a
seasonal pattern, the correct action is to keep publishing
and review again next week.

Full method:
`references/26-advanced-reporting-and-experiments.md`

## 3. Identity verification failed, attempts exhausted

Symptom: identity verification shows failed. The upload
option is gone or locked. Ads may stop and a payment hold
may appear.

First checks: read the exact notice and the date. Confirm
the five-point name match: payments profile name, identity
document name, date of birth, address, and bank account
name. Note which document was used and whether any field
mismatched.

Actions in order: gather the matching documents, contact
support on the existing case thread, ask for a manual
review with the specific mismatch explained, and attach
the documents support asks for. Keep every reply on the
same thread.

What not to do: do not create a second account, do not
create a new payments profile to dodge the failure, do not
upload documents that do not match the profile, and do
not submit the invalid traffic appeal form for a
verification failure.

Stop rule: after the manual review request is in, wait for
the specialist reply by email. Repeated uploads to a locked
flow and repeated new tickets slow the case down.

Full method:
`references/16-verification-and-payments-troubleshooting.md`

## 4. PIN never arrives

Symptom: address verification waits on a PIN that never
arrives by post. The account shows the PIN as sent.

First checks: confirm the postal address in the payments
profile is complete and deliverable, including any flat
or building detail the local post needs. Confirm the date
the PIN was sent and how many requests have been used.

Actions in order: wait the full delivery window shown in
the account, request a replacement only when the account
offers it, and keep the address unchanged while a PIN is
in transit. Changing the address restarts the process.

What not to do: do not guess the PIN, do not enter random
numbers, and do not change the address to a different
person's address to receive the letter faster.

Stop rule: after a replacement request, wait the full
window again. PIN delivery is postal, and no support
contact speeds the post.

Full method:
`references/16-verification-and-payments-troubleshooting.md`

## 5. Payment hold with everything verified

Symptom: identity and address show complete, the balance
is above the threshold, and no payment arrives. A hold
shows on the Payments page, or no hold shows and the
payment still does not come.

First checks: list every hold on the Payments page by
name. Check tax information status. Check the payment
method: valid, primary, and name-matched. Check the Policy
Center for an account level issue. Check the payment
cycle dates.

Actions in order: fix each hold by name, one at a time,
starting with tax and payment method. If no hold shows
and the cycle window has passed, contact support with
specifics: cycle dates, balance, holds list, and payment
method status.

What not to do: do not change the payment method
repeatedly, do not close the account to "release" the
payment, and do not accept a third party's offer to
recover the payment for a fee.

Stop rule: after the holds are fixed and the support
contact is in, wait for the next cycle. Payment timing
after a fix follows the cycle, not the fix date.

Full method:
`references/28-payments-tax-and-edge-cases.md`

## 6. Repeated low value content rejections

Symptom: the Sites page rejects the site again for low
value content after fixes were made.

First checks: read the exact reason and date. Audit every
indexable URL, not only new posts. Mark each page keep,
improve, merge, or delete. Check for thin pages, copied
pages, unedited generated pages, empty categories, and
tag and archive pages that add nothing.

Actions in order: improve or remove every weak page,
publish the improved content, confirm it is live and
indexed, wait for the changes to settle, then request a
new review with a record of what changed and when.

What not to do: do not reapply with no changes, do not add
a few thin posts and reapply, do not noindex the whole
site to hide weak pages while keeping them live for
visitors, and do not apply from a second account.

Stop rule: if the audit finds nothing left to fix, the
problem is judgement, not effort. Get an honest outside
read of the site against
`references/09-content-quality-guide.md` before reapplying.

Full method:
`references/07-rejection-reasons-and-fixes.md`

## 7. Account disabled for invalid traffic

Symptom: the account is disabled. The notice cites invalid
traffic. Ad serving stops. The appeal form is offered.

First checks: read the exact notice and date. Gather the
traffic log, the source audit, and the dates of any
promotion, spike, or attack. Note whether the account was
previously limited.

Actions in order: fix every risky source and placement
first, then submit the invalid traffic appeal form once,
with dated facts, the source audit, and the corrective
steps. Keep a copy of everything submitted.

What not to do: do not submit the form twice, do not
submit with no fixes made, do not open a new account, and
do not pay an "appeal writer" who promises reinstatement.

Stop rule: after the appeal, wait for the decision. If
the appeal is refused, further appeals may not be
considered, and no new account is allowed. That is the
end of the path, and accepting it beats burning time on
workarounds that create new violations.

Full method:
`references/15-policy-center-and-appeals.md`

## 8. Site approved but ads show blank

Symptom: the site is approved, code is placed, and ad
slots stay empty or show blank space.

First checks: confirm the code is the current code from
the account, unmodified. Confirm ads.txt is live and
correct. Confirm the page loads for a logged-out visitor
in a fresh browser without an ad blocker. Confirm the
AdSense crawler can reach the page. Check the Policy
Center for a page level issue.

Actions in order: fix the first break found, then wait.
New sites can take time to fill while Google assesses
traffic. Check coverage troubleshooting in the Help
Center for the remaining causes.

What not to do: do not click the slot to test it, do not
paste code from a tutorial, and do not add more units to
a page that already fails to fill.

Stop rule: if code, ads.txt, crawler access, consent, and
Policy Center all pass, wait a week. Blank slots on a new
site usually resolve as assessment completes.

Full method:
`references/19-platform-setup-guides.md` and
`references/29-advanced-technical-implementation.md`

## 9. Moving countries or changing payee details

Symptom: the publisher moved countries, formed a company,
or needs to change the payee name, and the account does
not offer the edit.

First checks: identify exactly what needs to change:
country, account type, name, or address. Read the live
Help pages for the change, because each has a different
path.

Actions in order: for a country or account type change,
plan the close and recreate path, including the final
payment rules, before touching anything. For a name
change within the allowed reasons, use the payments
profile edit, or contact support if verification locks
it. Resubmit tax information after a name change.

What not to do: do not edit the address to fake a country
move, do not transfer the account to another person, and
do not close the old account before understanding the
final payment position.

Stop rule: after the new account is created, complete
verification patiently. Rushing verification on a new
account repeats the old account's mistakes.

Full method:
`references/27-account-architecture-and-graduation.md` and
`references/28-payments-tax-and-edge-cases.md`

## 10. A third-party offer to recover, approve, or lift

Symptom: someone offers guaranteed approval, account
recovery, limit removal, or traffic that is "AdSense
safe", usually for a fee, usually urgently.

First checks: ask for the live Google page that supports
the claim. Check whether the offer asks for account
credentials, an OTP, a verification code, or payment
before any work. Check whether the offer promises an
outcome Google does not promise.

Actions in order: decline, keep the message as evidence,
and verify the underlying question on the live Help pages
or through official support channels. Report phishing
attempts through the proper channel where one exists.

What not to do: never share a password, an OTP, a
verification code, or a recovery link. Never pay for
approval, recovery, or limit removal. Never grant account
access to a stranger.

Stop rule: there is no stop rule here, because there is
no legitimate version of the offer. Every version ends
the same way: decline and verify officially.
