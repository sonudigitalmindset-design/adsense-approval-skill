---
name: adsense-approval-mastery
description: Teach and apply Google AdSense approval rules from 2003 to today, audit a site before applying, fix rejections, and keep an approved account policy safe. Use when the user asks about AdSense approval, eligibility, policies, rejection reasons, or staying compliant.
---

# AdSense Approval Mastery

## Decide what the user needs

- Ask whether the user wants to learn the rules, audit a site before applying, fix a rejection, keep an approved account safe, choose ad formats, improve earnings, handle a policy flag or appeal, fix verification or payments, or learn about YouTube and other AdSense products when the request does not say.

- Explain in the language the user writes in and keep official rules, community practice, and myths in separate words so they never blend.

- Never promise approval, a review date, or an earning figure. Google decides approval and does not publish a minimum post count, word count, traffic level, or domain age.

- Recheck the official pages in `references/11-official-sources.md` before you state a current rule as fact. Policies change and Google says keeping up to date is the publisher's responsibility.

## Separate official rules from myths

- Treat only Google AdSense Help, the Google Publisher Policies, the Google Publisher Restrictions, the AdSense Program policies, and the AdSense Terms and Conditions as the source of truth.

- Label anything from a blog, forum, video, or course as community practice or unverified when Google has not published it.

- Correct these myths plainly when they appear. There is no official 15 post rule, no official 1000 word rule, no universal six month domain rule, no official traffic minimum, and no trick that forces fast approval.

- Read the full history in `references/01-history-timeline.md` before you teach how a rule changed. Do not guess a year. Mark a date as approximate when the source does not confirm it.

## Audit a site before applying

- Run the read only checker in `scripts/site_audit.py` against the live site first and treat its output as a starting point, not a verdict.

- Run the deep approval-clone audit in `scripts/deep_audit.py` to crawl the sitemap and check every page point by point: titles, descriptions, H1s, word counts, image alt text, canonicals, noindex flags, mixed content, placeholder text, duplicate titles, and every internal link. Read `references/23-approval-clone-audit.md` for the method, the thresholds, and what the clone cannot judge. Fix every failure, decide every warning by reading the page, and never present the script thresholds as Google's rules.

- Check the eligibility basics from `references/02-eligibility-and-application.md`. The applicant must be 18 or older or apply through a parent or guardian, must own or control the site and its HTML, must publish original high quality content, and must follow the Program policies.

- Check every page a reviewer can reach, not only the homepage. Remove demo content, empty categories, broken links, under construction pages, and placeholder text before applying.

- Check the trust pages from `references/08-pre-apply-checklist.md`. Publish About, Contact, and Privacy pages in your own words and link them from the header or footer on every screen size. Add Terms and a Disclaimer where the niche needs them.

- Check the Privacy page for the advertising disclosure. It must explain that third parties including Google use cookies to serve and measure ads and that users can manage ad personalisation. Do not copy a template unchanged.

- Check navigation, mobile layout, page speed, and HTTPS by opening the site on a phone sized view as a stranger would. Fix menus that do not work and content that ads or popups cover.

- Check content quality with `references/09-content-quality-guide.md`. Every indexed post must fully answer its question with original detail, real examples, or tested experience. Merge or delete thin, copied, spun, or unedited auto generated pages.

- Check the whole site against the prohibited list in `references/03-publisher-policies.md` and the restricted list in `references/04-publisher-restrictions.md`. Include comments, downloads, embeds, outbound links, and pages outside the main niche.

- Check the ad and traffic rules in `references/05-program-policies-ads-traffic.md` before any code goes live. Never click your own ads, never ask others to click, never buy click traffic, and never place ads where they mislead or sit next to download buttons.

- Report findings as blockers, high risks, and small fixes. Name the exact URL for each finding and say which official rule it touches. End with a clear apply or do not apply yet recommendation and the reason.

## Apply in the right order

- Follow the application steps in `references/02-eligibility-and-application.md`. Add the site in AdSense, place the verification code in the head of pages that get regular views or verify through ads.txt or a meta tag, click Verify, then click Request review.

- Leave the verification code in place while the review runs. Removing it can unverify the site.

- Publish the ads.txt file at the site root with the publisher ID line from the AdSense account. Check it at the live ads.txt URL after publishing.

- Expect a review of the entire site that usually takes a few days and in some cases takes 2 to 4 weeks. Do not remove and re-add the site to chase speed.

- Keep publishing useful content and fixing issues while waiting. Do not apply from a second account for the same payee to work around a rejection.

## Fix a rejection and reapply

- Read the exact reason shown on the Sites page in AdSense and the date of the decision before you change anything. Use `references/07-rejection-reasons-and-fixes.md` to match the reason to a fix plan.

- Treat low value content as a whole site judgement, not one bad post. Audit every indexable URL, mark each keep, improve, merge, or delete, and fix or remove every weak page before reapplying.

- Do not reapply with no changes or with only a few more thin posts. Rapid resubmission with no real fix extends the loop.

- Fix policy violations by removing the content or the file, not only by removing ads from the page.

- Wait until the fix is live, indexed, and verified in your own browser before you request a new review. Record what changed, the date, and the URLs so the next review starts from facts.

## Keep an approved account safe

- Check the Policy Center regularly and fix every flagged issue before its deadline. A page level flag can grow into a site or account level action when ignored.

- Monitor traffic sources, sudden click or impression spikes, and unusual referrers. The publisher stays responsible for traffic even when a third party caused it.

- Keep ads labelled, keep advertising from exceeding content on a page, and keep ads away from deceptive placements, popups, and auto refreshing pages.

- Keep consent handling correct for visitors in the EEA, the UK, and Switzerland. Use a Google certified consent management platform where consent is required and keep the privacy disclosure current.

- Keep identity and payment details accurate. Complete identity verification and address PIN verification inside the deadlines Google shows in the account. Read `references/06-terms-and-payments.md` before you advise on payments, thresholds, or holds.

- Never advise a workaround that hides a violation, such as cloaking, a second account for the same payee, or moving violating content to a subdomain to keep ads running.

## Help with formats, optimization, appeals, and verification

- Recommend ad formats from `references/13-ad-formats-and-placement.md`. Explain Auto ads and manual units, the formats inside each, and the placement rules that apply to all of them. Never promise that one format earns more than another.

- Advise on earnings from `references/14-optimization-and-revenue.md`. Judge changes by total earnings and user experience together, test one variable at a time with experiments, and treat blocking controls as brand-safety tools, not revenue levers. Never quote a third-party RPM benchmark as a fact.

- Handle policy flags and appeals from `references/15-policy-center-and-appeals.md`. Read the exact notice first, fix the root cause, and build an appeal from dated facts and log evidence. Use `examples/policy-appeal-outline.md` as a structure, never as copied text. Warn that further appeals may not be considered after a decision.

- Fix verification and payment problems from `references/16-verification-and-payments-troubleshooting.md`. Check the five-point name match first, follow the deadlines shown in the account, and never advise creating a second account or a new payments profile to dodge a failed verification.

- Answer YouTube and other product questions from `references/17-youtube-and-other-products.md`. Keep AdSense for Content, AdSense for YouTube, AdSense for Search, AdMob, and Ad Manager separate, and state YPP thresholds only as verified on the live Help page.

- Answer consent questions from `references/18-consent-and-privacy-deep-dive.md`. Require a certified CMP for EEA, UK, and Swiss traffic, and adapt `examples/privacy-policy-outline.md` to the site instead of copying it unchanged.

- Set up a site from `references/19-platform-setup-guides.md`. Place code, publish ads.txt with the line copied from the account, and verify every file live before applying.

- Diagnose any symptom from `references/20-troubleshooting-index.md` first, then read the linked reference for the full fix.

- Build traffic honestly from `references/21-traffic-and-seo-basics.md`. Never recommend bought traffic, click exchanges, bots, or any scheme that pays people to visit or click.

- Teach the whole journey from `references/22-learning-paths.md`. Match the level to the user, from complete beginner to advanced multi-product work, and use the checks at each level before moving on.

## Teach the history and the terms

- Teach from `references/01-history-timeline.md` for the story from the March 2003 precursor and the 18 June 2003 launch to the 2024 move to per impression payment and the present day.

- Teach terms from `references/10-glossary.md`. Define each term in one plain sentence and give one real example before you move on.

- Teach the difference between prohibited content, restricted content, and Program policy violations. Prohibited content gets no ads. Restricted content gets fewer ads. Program policy violations cover clicks, traffic, placement, and behaviour.

- Teach the payment story from `references/06-terms-and-payments.md` without inventing figures. State the threshold and timing only as shown on the current official pages and mark older figures as historical.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [AdSense Help Center](https://support.google.com/adsense/) for eligibility, site review, payments, and troubleshooting. Carry the exact question into the browser task and verify the answer on the live page.

- [Google Publisher Policies](https://support.google.com/admob/answer/10502938?hl=en) for prohibited content and behaviour. Verify the current category list on the live page before you quote it. Google is migrating these policies to a new Publisher Policies Help Center, so follow the live redirect when it changes.

- [AdSense Program policies](https://support.google.com/adsense/answer/48182?hl=en) for clicks, impressions, traffic sources, and ad behaviour. Verify the current wording on the live page before you quote it.

- [AdSense Terms and Conditions](https://support.google.com/adsense/answer/9724?hl=en) for the entry point to the current terms. Open the Terms link from the live AdSense Help page or from the AdSense account so you read the version for the publisher's country.

## Alternatives for better results

- Check indexing in Google Search Console before applying so the review sees the same pages a visitor sees.

- Fix the site on a staging copy or one section at a time when the live site already gets traffic, then verify the live result.

- Ask the user for the exact rejection wording and a screenshot of the Sites page when the reason is unclear, instead of guessing the cause.
