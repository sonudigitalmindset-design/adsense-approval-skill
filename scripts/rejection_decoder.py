#!/usr/bin/env python3
"""Rejection decoder: guess which AdSense rejection reason an email describes.

Reads rejection email text from a file (--file) or from stdin, matches
keywords and phrases to the sections of
references/07-rejection-reasons-and-fixes.md, and prints the fix
checklist pointers for the best-matching sections.

Honest keyword matching only. The script guesses from wording. It does
not know Google's decision, it cannot read the account, and the user
must read the actual email. If nothing matches, it says so.

Standard library only. Reads local text only. Makes no network calls.
"""

import argparse
import re
import sys

# Each entry: (section title, fix pointer, list of (phrase, weight)).
# Phrases are matched case-insensitively as substrings. Higher weights
# mark phrases that are distinctive to one reason.
SECTIONS = [
    (
        "Low value content",
        "Audit every indexable URL, delete or noindex thin pages, and "
        "rewrite kept pages with original examples, steps, or tested "
        "experience. Length alone does not fix this.",
        [
            ("low value", 5),
            ("low-value", 5),
            ("little value", 4),
            ("not enough content", 4),
            ("insufficient content", 4),
            ("thin content", 4),
            ("valuable content", 3),
            ("original content", 2),
            ("valuable inventory", 3),
            ("low quality content", 4),
            ("does not offer enough", 3),
        ],
    ),
    (
        "Site behaviour: navigation problems",
        "Fix menus on mobile and desktop, remove dead links and pages "
        "under construction, and click through the whole site as a "
        "stranger would.",
        [
            ("navigation", 4),
            ("site behaviour", 5),
            ("site behavior", 5),
            ("difficult to navigate", 4),
            ("under construction", 3),
            ("unfinished", 3),
            ("hard to navigate", 4),
        ],
    ),
    (
        "Policy violation",
        "Audit the whole site against references 03 and 04, including "
        "comments, downloads, embeds, and outbound links. Remove or "
        "rewrite the violating content itself.",
        [
            ("policy violation", 5),
            ("program policies", 4),
            ("publisher policies", 4),
            ("violates", 3),
            ("violation", 3),
            ("prohibited content", 4),
            ("does not comply", 3),
        ],
    ),
    (
        "Site down or unavailable",
        "Make the site public, fix hosting and DNS problems, remove "
        "password protection and maintenance mode, and confirm the "
        "site loads over HTTPS and robots.txt does not block Googlebot.",
        [
            ("site down", 5),
            ("unavailable", 4),
            ("could not access", 4),
            ("couldn't access", 4),
            ("cannot access", 4),
            ("not accessible", 4),
            ("unreachable", 4),
            ("could not reach", 4),
            ("site is down", 5),
            ("unable to access", 4),
        ],
    ),
    (
        "Unsupported language",
        "Check the supported-language list on the live Help pages. If "
        "the site mixes languages, make the primary language clear and "
        "consistent.",
        [
            ("unsupported language", 5),
            ("language is not supported", 4),
            ("language not supported", 4),
            ("supported language", 3),
        ],
    ),
    (
        "Duplicate account",
        "Sign in to the existing account instead of creating a new one. "
        "Do not create a second account to work around a rejection.",
        [
            ("duplicate account", 5),
            ("existing account", 4),
            ("already have an account", 4),
            ("already has an account", 4),
            ("multiple accounts", 3),
            ("another account", 2),
        ],
    ),
    (
        "Underage applicant",
        "A parent or guardian signs up using their own Google Account. "
        "Payments go to them.",
        [
            ("underage", 5),
            ("under 18", 5),
            ("under eighteen", 5),
            ("18 years", 3),
            ("parent or guardian", 4),
            ("must be 18", 4),
        ],
    ),
    (
        "Invalid traffic concerns at application stage",
        "Stop all paid-to-click, exchange, autosurf, and bot traffic. "
        "Stop asking anyone to click ads. Build genuine traffic before "
        "reapplying.",
        [
            ("invalid traffic", 5),
            ("invalid activity", 4),
            ("invalid clicks", 4),
            ("artificial traffic", 4),
            ("incentivised", 3),
            ("incentivized", 3),
            ("bot traffic", 4),
            ("click activity", 3),
        ],
    ),
]

EXAMPLES = [
    "We found your site has low value content and does not offer "
    "enough original content for our advertisers.",
    "We could not access your site. The site appears to be down or "
    "unavailable at the time of review.",
    "Your site violates our program policies. Please review the "
    "publisher policies and remove the violating content.",
    "Your application was disapproved because of invalid traffic "
    "concerns. Traffic to your site appears artificial.",
]

NOTE = (
    "NOTE: this is a guess from wording only. The script matched "
    "keywords in the pasted text to the sections of "
    "references/07-rejection-reasons-and-fixes.md. It does not know "
    "Google's decision. Always read the actual email and the reason "
    "shown on the Sites page in the AdSense account, and follow the "
    "reapply discipline in that file."
)


def score_text(text):
    """Return a list of (score, section title, fix pointer) sorted best first."""
    lowered = text.lower()
    results = []
    for title, fix, phrases in SECTIONS:
        score = 0
        hits = []
        for phrase, weight in phrases:
            if phrase in lowered:
                score += weight
                hits.append(phrase)
        if score > 0:
            results.append((score, title, fix, hits))
    results.sort(key=lambda item: -item[0])
    return results


def print_results(results):
    if not results:
        print("No rejection reason matched the pasted text.")
        print()
        print("The email may use wording this decoder does not know, "
              "or the pasted text may be too short.")
        print("Read the actual email, note the exact reason and date, "
              "and open references/07-rejection-reasons-and-fixes.md")
        print("to find the matching section by hand. The sections are:")
        for title, _fix, _phrases in SECTIONS:
            print("  - " + title)
        print()
        print(NOTE)
        return
    print("Best-matching rejection reason(s):")
    print()
    for score, title, fix, hits in results[:3]:
        print("  %s (match score %d, matched: %s)"
              % (title, score, ", ".join(hits)))
        print("    Fix: " + fix)
        print("    See: references/07-rejection-reasons-and-fixes.md, "
              "section \"%s\"" % title)
        print()
    print(NOTE)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Guess which AdSense rejection reason an email "
        "describes, from its wording. Keyword matching only; always "
        "read the actual email.")
    parser.add_argument("--file", "-f", metavar="PATH",
                        help="read the rejection email text from a file")
    parser.add_argument("--examples", action="store_true",
                        help="print built-in example rejection phrases "
                        "and exit")
    parser.add_argument("--text", "-t", metavar="TEXT",
                        help="decode this text directly instead of "
                        "reading stdin or a file")
    args = parser.parse_args(argv)

    if args.examples:
        print("Built-in example phrases (for testing):")
        print()
        for i, example in enumerate(EXAMPLES, 1):
            print("  %d. %s" % (i, example))
        print()
        print("Try one with: python3 rejection_decoder.py --text "
              "\"<phrase>\"")
        return 0

    if args.text is not None:
        text = args.text
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError as exc:
            print("Could not read file: %s" % exc, file=sys.stderr)
            return 1
    else:
        if sys.stdin.isatty():
            print("Paste the rejection email text, then press "
                  "Ctrl-D (Linux/Mac) or Ctrl-Z then Enter (Windows):")
        text = sys.stdin.read()

    text = text.strip()
    if not text:
        print("No text received. Paste the rejection email text, or "
              "use --file or --text.", file=sys.stderr)
        return 1

    # A pasted email often contains headers and footers. Matching runs
    # over the whole text; the note covers the uncertainty.
    text = re.sub(r"\s+", " ", text)
    print_results(score_text(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
