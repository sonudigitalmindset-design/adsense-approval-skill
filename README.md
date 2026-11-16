# AdSense Approval Mastery

A skill that teaches Google AdSense approval end to end: the full
history from the 2003 launch to today, the current eligibility rules,
every policy layer, the mistakes that get sites rejected, and the
habits that keep an approved account safe.

It is built for AI assistants (Muse, Claude Code, Cursor, and other
Agent Skills compatible tools) and for humans who want one honest,
well-sourced place to learn AdSense approval.

**No approval is promised.** Google decides every application. This
skill separates official rules from community practice and myths, and
points at the live official pages as the source of truth.

## What is inside

| File | What it covers |
|---|---|
| `SKILL.md` | The skill itself: how to audit, apply, fix rejections, and stay compliant |
| `skill.yaml` | Muse skill descriptor (name, title, description, category) |
| `references/01-history-timeline.md` | AdSense history, 2003 to today, with confirmed vs reported dates |
| `references/02-eligibility-and-application.md` | The 4 official eligibility checks, myths, and application steps |
| `references/03-publisher-policies.md` | Prohibited content and behaviour (no ads) |
| `references/04-publisher-restrictions.md` | Restricted content (fewer ads) |
| `references/05-program-policies-ads-traffic.md` | Invalid traffic, click encouragement, traffic sources, placement, privacy |
| `references/06-terms-and-payments.md` | Terms, revenue share history, verification, holds, terminations |
| `references/07-rejection-reasons-and-fixes.md` | Every common rejection reason and its fix plan |
| `references/08-pre-apply-checklist.md` | Tick-box checklist to run before every application |
| `references/09-content-quality-guide.md` | Originality, AI content, copyright, YMYL, trust signals |
| `references/10-glossary.md` | Plain-language definitions with examples |
| `references/11-official-sources.md` | Every official link, with a 2-minute verification habit |
| `references/12-mistakes-encyclopedia.md` | 52 mistakes that get sites rejected or accounts closed |
| `references/13-ad-formats-and-placement.md` | Auto ads, ad units, and placement rules for every format |
| `references/14-optimization-and-revenue.md` | Metrics, experiments, blocking controls, and honest earnings levers |
| `references/15-policy-center-and-appeals.md` | Enforcement levels, fix workflow, and the invalid traffic appeal |
| `references/16-verification-and-payments-troubleshooting.md` | Identity, PIN, payment methods, tax info, and holds |
| `references/17-youtube-and-other-products.md` | YPP, AdSense for Search, AdMob, and Ad Manager |
| `references/18-consent-and-privacy-deep-dive.md` | Certified CMP, Funding Choices, TCF, Consent Mode, disclosures |
| `references/19-platform-setup-guides.md` | WordPress, Blogger, static sites, builders, ads.txt, sellers.json |
| `references/20-troubleshooting-index.md` | 25 symptoms with likely cause and first check |
| `references/21-traffic-and-seo-basics.md` | Legitimate traffic, Search Console, and durable growth |
| `references/22-learning-paths.md` | Zero-to-advanced reading paths with checks, plus FAQ |
| `references/23-approval-clone-audit.md` | Deep crawl method: every checkable review point, and its limits |
| `scripts/site_audit.py` | Read-only readiness checker (Python standard library only) |
| `scripts/deep_audit.py` | Deep approval-clone crawler: every page, every small point |
| `examples/audit-report-template.md` | Report template for one site audit |
| `examples/privacy-policy-outline.md` | Privacy Policy structure to adapt, with ad disclosure |
| `examples/policy-appeal-outline.md` | Fact-based appeal structure for invalid traffic cases |

## Install

### Muse

Copy or clone this folder into your custom skills directory as
`adsense_approval_mastery`:

```bash
git clone https://github.com/sonudigitalmindset-design/adsense-approval-skill.git
cp -r adsense-approval-skill ~/workspace/custom-skills/adsense_approval_mastery
```

Muse reads `skill.yaml` for the skill's name and description and
`SKILL.md` for the instructions. The frontmatter block at the top of
`SKILL.md` is the Agent Skills metadata; Muse ignores it and uses
`skill.yaml`.

### Claude Code / Agent Skills compatible tools

Copy or clone this folder into your skills directory, for example:

```bash
git clone https://github.com/sonudigitalmindset-design/adsense-approval-skill.git
cp -r adsense-approval-skill ~/.claude/skills/adsense-approval-mastery
```

The `SKILL.md` frontmatter (`name` + `description`) follows the Agent
Skills open format. Adjust the destination path for your tool
(Cursor, Windsurf, and others use their own skills folders).

### Use without installing

Read `SKILL.md` and the `references/` files directly. Everything a
human needs is in plain Markdown. No build step, no dependencies.

## Use the readiness checker

```bash
python3 scripts/site_audit.py https://example.com
```

It is read-only: it fetches the homepage, robots.txt, sitemap,
ads.txt, and common trust-page URLs, and reports blockers and
warnings. It cannot judge content quality or policy compliance, so
always follow it with the human audit in
`references/08-pre-apply-checklist.md`.

## Use the deep approval-clone audit

```bash
python3 scripts/deep_audit.py https://example.com --output report.md
```

It crawls the sitemap and checks every page point by point:
titles, descriptions, H1s, word counts, image alt text, canonicals,
noindex flags, mixed content, placeholder text, duplicate titles,
and every internal link. It replicates the checkable surface of a
review, not Google's decision. See
`references/23-approval-clone-audit.md` for the method and limits.

## Learning path

The full zero-to-advanced path, with a check at each level, is in
`references/22-learning-paths.md`: beginner, preparing a first
site, applying, running ads, optimization, and advanced
multi-product work.

New to AdSense? Read in this order:

1. `references/01-history-timeline.md` — how we got here
2. `references/10-glossary.md` — the vocabulary
3. `references/02-eligibility-and-application.md` — what Google
   actually requires, and what it does not
4. `references/03-publisher-policies.md` and
   `references/04-publisher-restrictions.md` — what can and cannot
   carry ads
5. `references/05-program-policies-ads-traffic.md` — the rules that
   close accounts
6. `references/09-content-quality-guide.md` — how to write content
   that passes
7. `references/08-pre-apply-checklist.md` — the final check
8. `references/07-rejection-reasons-and-fixes.md` — only if rejected

## Keeping it current

AdSense policies change. Before quoting a current rule, recheck the
live official pages listed in `references/11-official-sources.md`.
When a page contradicts this skill, the page wins: update the skill
and record the change in `CHANGELOG.md`.

Last verified against live official pages: **17 November 2026**.

## Contributing

Fixes welcome, especially:

- A policy wording change with the live official URL and the date
  you read it
- A broken official link, with the new live URL
- A clearer example that does not invent a rule

Do not add "guaranteed approval" claims, unpublished minimums, or
workarounds that hide violations.

## License

MIT. See `LICENSE`. This project is not affiliated with Google.
AdSense is a trademark of Google LLC.
