# Installation

Get AdSense Approval Mastery into your assistant, or read it
directly as a human. No build step, no dependencies, no account.

[Back to the main page](../README.md)

## Muse

Copy or clone this folder into your custom skills directory as
`adsense_approval_mastery`:

```bash
git clone https://github.com/sonudigitalmindset-design/adsense-approval-skill.git
cp -r adsense-approval-skill ~/workspace/custom-skills/adsense_approval_mastery
```

Muse reads `skill.yaml` for the skill's name and description and
`SKILL.md` for the instructions. The frontmatter block at the top
of `SKILL.md` is the Agent Skills metadata. Muse ignores it and
uses `skill.yaml`.

## Claude Code and Agent Skills compatible tools

Copy or clone this folder into your skills directory, for example:

```bash
git clone https://github.com/sonudigitalmindset-design/adsense-approval-skill.git
cp -r adsense-approval-skill ~/.claude/skills/adsense-approval-mastery
```

The `SKILL.md` frontmatter (`name` + `description`) follows the
Agent Skills open format. Adjust the destination path for your
tool. Cursor, Windsurf, and others use their own skills folders.

## Use without installing

Read `SKILL.md` and the `references/` files directly. Everything
a human needs is in plain Markdown. Start with
[Understanding AdSense approval](understanding.md), then follow
the reading order in
[How to use this skill](usage.md).

## Verify the install

Ask your assistant a question the skill answers, for example:
"What are the official AdSense eligibility checks?" A correct
answer names the four checks and says Google publishes no
minimum post count, word count, or traffic level. If the answer
invents a minimum, the skill is not loaded.

You can also check the files directly. A correct install
contains `SKILL.md`, `skill.yaml`, a `references/` folder with
36 files, a `scripts/` folder with two Python scripts, and an
`examples/` folder with five templates. See the full list in
[Contents](contents.md).

## Update

Pull the latest version and copy it over the old install:

```bash
cd adsense-approval-skill
git pull
cp -r . ~/workspace/custom-skills/adsense_approval_mastery
```

Use your tool's skills path instead of the Muse path when
needed. Read `CHANGELOG.md` after updating to see what changed.

## Uninstall

Delete the skill folder from your skills directory. Nothing else
was installed, so nothing else needs removing.

## Next steps

- [Understanding AdSense approval](understanding.md): how the
  review works, in plain language.
- [How to use this skill](usage.md): workflows for a first site,
  a rejection, and an approved account.
- [Audit scripts](audit-scripts.md): the two checkers, their
  options, and how to read their reports.
- [FAQ](faq.md): the questions everyone asks, answered honestly.
