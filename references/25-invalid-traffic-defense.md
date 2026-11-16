# Invalid traffic defense

Invalid traffic is the most common reason accounts lose ad
serving. Google defines it plainly: clicks or impressions that
do not come from genuine user interest. This reference explains
where invalid traffic comes from, how to prevent it, how to
spot it early, and how to respond when it hits.

Read the Program policy rules first in
`references/05-program-policies-ads-traffic.md`. Read the
enforcement ladder in
`references/24-ad-serving-limits-and-enforcement-levels.md`.

## The one rule that governs everything

The publisher stays responsible for traffic even when a third
party caused it. A hired promoter, a viral share, a bot attack,
or a "traffic service" does not move responsibility to someone
else. Google judges the traffic on the account, not the intent
behind it. Every defense in this reference flows from that
rule: control what you can, monitor what you cannot control,
and document everything.

## Where invalid traffic comes from

- Own clicks. Clicking your own ads, including "just to test",
  including clicks from family, staff, and friends who want to
  help. Testing must never use live ad code.
- Encouraged clicks. Asking, begging, rewarding, or tricking
  users into clicking. This includes "support us by clicking",
  arrows pointing at ads, and labels that promise a reward.
- Accidental clicks. Ads placed where users tap by mistake:
  next to navigation, pagination, download buttons, close
  buttons, game controls, and sticky elements that cover
  content. Accidental clicks are still invalid traffic even
  when the placement was not meant to deceive.
- Bots and crawlers. Automated traffic that loads pages and
  triggers impressions. Some bots are legitimate search
  crawlers. Traffic from botnets, scrapers, and headless
  browsers is not.
- Click bombing. A third party deliberately clicks ads again
  and again to harm the publisher. Rare, but real, and the
  publisher still has to report and document it.
- Purchased traffic. Traffic services, traffic exchanges, paid
  to click programs, and social automation that sends visitors
  who do not genuinely want the content. Any service that
  promises "AdSense safe traffic" is selling the exact thing
  the policy forbids.
- Misleading promotion. Ads, posts, or messages that promise
  something the page does not deliver, so visitors arrive,
  bounce, and sometimes click ads on the way out. The traffic
  looks real and behaves badly.

Industry reports split invalid traffic into general invalid
traffic (simple bots, known crawlers) and sophisticated invalid
traffic (bots that mimic humans). These are industry terms
from IAB and MRC measurement standards, not Google account
labels. Google does not tell a publisher which kind it found.
Do not build a defense around guessing the kind. Build it
around sources and behaviour.

## Prevention: the traffic source audit

Run this audit before adding ads to a new site, before starting
any promotion, and once a month after approval.

- List every traffic source. Search, direct, social, referral,
  email, paid promotion, and any service that sends visitors.
  If a source cannot be named, it cannot be trusted.
- Check each source for genuine intent. Would a visitor from
  this source want this page? A mismatch between the promise
  and the page is a risk even when the visitors are human.
- Check Analytics for anomalies. Sudden spikes with no
  matching cause, one country or city dominating overnight,
  one device or browser at an impossible share, sessions of
  a few seconds with a high bounce rate, and traffic that
  arrives in sharp bursts at odd hours. Any one of these is a
  question, not a verdict. Two or more together need action.
- Segment new sources. When trialling a new promotion channel,
  watch its behaviour in Analytics for a week before judging
  it safe. A channel that sends thousands of sessions with
  near zero engagement is a liability, not growth.
- Use UTM parameters on every promotion you control, so a
  bad source can be identified and stopped by name.
- Keep a traffic log. Date, source, what changed, and what
  the reports showed. The log is the evidence base for any
  later appeal or support conversation.

## Prevention: placement and code hygiene

- Keep ads away from anything users tap by habit. Navigation,
  menus, download buttons, video controls, and form buttons
  need clear space around them with no ad in the tap path.
- Never place ads where they cover content or follow the user
  in a way that forces interaction. Use Google's own anchor
  and vignette formats instead of custom sticky code. See
  `references/13-ad-formats-and-placement.md` and
  `references/29-advanced-technical-implementation.md`.
- Never refresh ads. Publishers are not permitted to refresh
  a page or an element of a page without the user requesting
  a refresh. See the refresh rules in
  `references/29-advanced-technical-implementation.md`.
- Never modify AdSense code. Do not wrap it, delay it, hide
  it, or trigger it with custom scripts unless Google's own
  documentation for that format says so.
- Block nothing that Google needs. The AdSense crawler must
  reach pages. At the same time, use ordinary server level
  bot controls for clearly abusive automated traffic, and
  keep a record of what was blocked and why. Server controls
  are practice, not a Google requirement, and they never
  replace source discipline.

## Early warning signals in reports

Check reports weekly. These signals mean "investigate today",
not "panic".

- Click through rate jumps sharply on one page, one country,
  or one device, with no matching content change.
- Impressions surge while estimated earnings stay flat or
  fall. Volume without value is a classic invalid traffic
  shape.
- One page earns a large share of clicks from a tiny share
  of sessions.
- A new referrer appears in Analytics with high volume and
  near zero engagement.
- Earnings are deducted in the transactions view. Google
  removes invalid earnings from estimated earnings, and the
  deduction line is the visible trace. A deduction is a
  fact to investigate, not a rounding error.

Read the reporting method in
`references/26-advanced-reporting-and-experiments.md`.

## Responding to suspected invalid traffic

- Document first. Dates, the signal that appeared, the
  sources involved, screenshots of the reports, and the
  Analytics segments. Facts with dates beat explanations
  without them.
- Stop the source. Pause the promotion, block the abusive
  referrer at the server level where that is possible, and
  remove the risky placement. Stopping the source matters
  more than explaining it.
- Report suspected invalid activity to Google through the
  current reporting path in the AdSense Help Center. Find
  the live link on the Help page about invalid traffic,
  because the form address changes. Report the facts, the
  dates, and the steps already taken. Do not report with
  accusations against a named competitor unless you have
  evidence.
- For a suspected click bombing attack, keep the log running
  for every spike, consider temporarily removing ads from
  the attacked pages until the spike passes, and report the
  pattern. Removing ads from attacked pages is defensive
  practice, not a Google instruction, and it trades short
  term earnings for account safety.
- If ad serving is limited, follow
  `references/24-ad-serving-limits-and-enforcement-levels.md`.
  If the account is disabled, follow the appeal workflow in
  `references/15-policy-center-and-appeals.md`. Do not submit
  the appeal form for a limit, and do not open a second
  account after a refusal.

## What never helps

- Buying "real human traffic" from a service. If the visitors
  would not have come on their own, the traffic is not
  genuine interest, however human the sellers claim it is.
- Click exchanges, click groups, and paid to click schemes.
  These are textbook invalid traffic sources.
- Asking friends, family, or followers to click. Good
  intentions do not change the policy.
- VPN and proxy schemes to fake geography. Location signals
  that do not match real users are a detection signal, not
  a shield.
- Hiding the problem. Removing a bad source quietly without
  a log, then repeating the same promotion, teaches nothing
  and leaves no evidence for the next review.

## The honest summary

Invalid traffic defense is mostly boring work: name every
source, watch behaviour weekly, keep placements honest, and
write things down. No tool, service, or plugin can replace
that work, and Google does not publish the detection signals
it uses. A publisher who can show a clean source list, a
dated log, and quick action on anomalies is in the strongest
possible position when Google asks questions.
