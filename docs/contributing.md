# Contributing

Fixes welcome, especially:

- A policy wording change with the live official URL and
  the date you read it.
- A broken official link, with the new live URL.
- A clearer example that does not invent a rule.
- A new check for the audit scripts that measures
  something real, with its status labelled: Google rule
  or practice heuristic.

Do not add "guaranteed approval" claims, unpublished
minimums, or workarounds that hide violations.

[Back to the main page](../README.md)

## Style rules for new files

- No markdown tables in `SKILL.md` and `references/`.
- No semicolons and no em dashes in `SKILL.md` and
  `references/`. Short sentences instead.
- Every internal `references/…` link must resolve.
- Every claim carries its status: official Help page,
  reported from a secondary source, or inferred from
  rejection patterns. Never present a reported or
  inferred claim as a confirmed Google rule.
- Live official pages win over this skill. When a page
  contradicts the skill, update the skill and record the
  change in `CHANGELOG.md`.

## Style rules for the audit scripts

- Python standard library only. No dependencies.
- Read-only. The scripts never write to the site.
- A failed fetch is reported as unverified, never as
  proof of absence.
- Thresholds are labelled as practice heuristics, never
  as Google rules.
- The readiness score is labelled heuristic only, never
  as a Google score.

## How to propose a change

1. Fork the repo and create a branch.
2. Make the change, following the style rules above.
3. Run both scripts against `https://example.com` to
   confirm they still run cleanly.
4. Open a pull request describing what changed, why, and
   the official source when the change is a policy claim.

## License

MIT. See `LICENSE`. This project is not affiliated with
Google. AdSense is a trademark of Google LLC.
