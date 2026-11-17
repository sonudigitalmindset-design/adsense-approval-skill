# AI-assisted and scaled content

Google's stance on AI content is often misquoted. The official
position is not a ban on AI tools. It is a quality rule: content is
judged by whether it helps people, however it was produced, and
content produced at scale mainly to manipulate rankings is spam. This
file states the official position from the pages listed below, all
read live on 18 November 2026. Status of the quoted positions:
OFFICIAL.

## The official stance

Source 1: Google Search Central Blog, "Google Search's guidance about
AI-generated content", 8 February 2023
(`developers.google.com/search/blog/2023/02/google-search-and-ai-content`).

- Google rewards high-quality content however it is produced. The
  focus is on the quality of the content, not how it was produced.
- Using automation, including AI, to generate content with the primary
  purpose of manipulating ranking in search results is a violation of
  Google's spam policies.
- Appropriate use of AI or automation is not against Google's
  guidelines. The blog gives examples such as AI helping to create
  helpful content, for instance sports scores pages or weather
  forecasts produced from data.
- An AI author byline is discouraged. The blog says a byline that
  names an AI tool as the author is not the recommended approach,
  because readers expect content to be accountable to a person.
- Disclosures are useful where readers would reasonably expect to know
  how content was produced. The blog frames disclosure as a trust
  practice, not as a ranking requirement.

Source 2: Google Search Central, "Using generative AI content"
(`developers.google.com/search/docs/fundamentals/using-gen-ai-content`).

- Generative AI is useful for research, structure, and drafting, but
  the publisher remains responsible for the final page.
- Many pages produced without added value may violate the scaled
  content abuse policy, even if each page reads smoothly.
- Everything must be fact-checked, including titles, descriptions,
  structured data, and alt text. AI output invents figures, quotes,
  and sources that look plausible. Checking is not optional.
- The page points to the Search Quality Rater Guidelines sections on
  lowest-quality and scaled content abuse for how human raters judge
  this material.

Source 3: Google Search Central, "Spam Policies for Google Web
Search"
(`developers.google.com/search/docs/essentials/spam-policies`),
section "Scaled content abuse".

- Scaled content abuse is when many pages are generated for the
  primary purpose of manipulating search rankings and not helping
  users. It typically focuses on large amounts of unoriginal content
  that provides little to no value to users, no matter how it is
  created.
- The examples named on the page include using generative AI tools to
  generate many pages without adding value for users, scraping feeds
  or search results to generate many pages, stitching or combining
  content from different pages without adding value, creating multiple
  sites to hide the scaled nature of the content, and creating many
  pages where the content makes little or no sense but contains search
  keywords.
- Sites that violate the spam policies may rank lower or not appear in
  results at all.

## What this means for AdSense review

Status: INFERRED. AdSense site review and Search spam policy are
separate systems, and Google does not publish an AdSense rule that
names AI content. The link below is practice guidance built from the
rejection patterns in `07-rejection-reasons-and-fixes.md`.

- A site rejected for low value content often has the same shape as
  scaled content abuse: many pages, little original value, no tested
  experience, no added insight. The rejection reason names the outcome
  (low value), not the tool that produced it.
- Publishing raw AI output without editing, checking, or adding
  original insight is the highest-risk pattern in this file. It
  combines three rejection risks at once: thin content, invented
  facts, and no evidence of human expertise.
- AI-assisted drafting followed by real human work is a different
  pattern: the human checks every fact, adds tested experience,
  rewrites in their own voice, adds original examples or screenshots,
  and takes responsibility under their own name. That pattern is
  consistent with the official guidance above.

## A safe workflow for AI-assisted posts

Status: practice guidance, not a Google rule.

1. Use AI for a first draft, an outline, or research questions, never
   for the final published text untouched.
2. Check every number, date, name, and quote against a primary source.
   Remove anything that cannot be verified.
3. Add something only a human with experience can add: a test result,
   a screenshot from your own setup, a comparison you ran, a mistake
   you made and fixed.
4. Rewrite in your own voice. If the draft sounds like every other AI
   draft on the topic, it adds no value.
5. Put your real name on the post and stand behind it. Never use an AI
   tool name as the author.
6. Read the finished page as a stranger. If it answers the question
   fully and adds something the top results do not, it is ready. If
   it only restates the obvious, it is not.
7. Publish at a pace a human can genuinely review. Dozens of posts a
   day with no review step is the scaled pattern, whatever tool made
   them.

## Disclosure

Status: practice guidance, following the official blog's trust framing.

- A short note on the About page or in the post, stating that drafts
  may be AI-assisted and are always human-checked and edited, is a
  reasonable trust practice.
- Disclosure does not fix low-quality content. A disclosed thin page
  is still a thin page.
- Never claim a post is fully human-written when it is not, and never
  claim AI output is a tested personal experience. Both are deceptive
  authorship. See `40-eeat-and-author-trust.md`.

## What not to do

- Do not publish dozens of AI pages a day to "fill" a site before
  applying. Volume without value is the exact pattern the spam policy
  names.
- Do not spin, translate, or lightly rewrite other sites' content with
  AI and call it original.
- Do not use AI to invent statistics, reviews, testimonials, or
  credentials.
- Do not hide AI use behind a fake author identity. A made-up name
  with a stock photo is worse than an honest AI-assisted note.
