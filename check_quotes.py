"""Check quoted passages against an explicitly supplied local transcript corpus.

Usage: python3 check_quotes.py skills --transcripts /path/to/transcripts
Checks double-quoted passages of six or more words in Markdown. Whitespace,
case, and common punctuation are normalized; ellipses split fragments.
This verifies textual occurrence, not the speaker, timestamp, or interpretation.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sys


def norm(text):
    for before, after in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                          ("—", "-"), ("–", "-"), ("…", "...")]:
        text = text.replace(before, after)
    return re.sub(r"\s+", " ", text).strip().lower()


def passages(text):
    text = text.replace("“", '"').replace("”", '"')
    for match in re.finditer(r'"([^"\n]{20,})"', text):
        quote = match.group(1)
        if len(quote.split()) >= 6:
            yield text.count("\n", 0, match.start()) + 1, quote


def matches(quote, corpus):
    fragments = [norm(part.strip(" .,\t\n"))
                 for part in re.split(r"\.\.\.|…", quote)]
    fragments = [part for part in fragments if part]
    # All fragments must occur, in order, in a single transcript.
    for transcript in corpus:
        position = 0
        for fragment in fragments:
            found = transcript.find(fragment, position)
            if found < 0:
                break
            position = found + len(fragment)
        else:
            if fragments:
                return True
    return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folders", nargs="*", type=Path, default=[Path("skills")])
    parser.add_argument("--transcripts", type=Path,
                        default=os.environ.get("LENNY_TRANSCRIPTS"),
                        help="Directory of .txt transcripts (or set LENNY_TRANSCRIPTS)")
    parser.add_argument("--report", type=Path, help="Write a JSON verification summary")
    args = parser.parse_args(argv)
    if not args.transcripts or not args.transcripts.is_dir():
        parser.error("provide an existing transcript directory with --transcripts or LENNY_TRANSCRIPTS")
    sources = sorted(args.transcripts.rglob("*.txt"))
    if not sources:
        parser.error("the transcript directory contains no .txt files")
    corpus = [norm(p.read_text(encoding="utf-8", errors="replace")) for p in sources]
    if not any(corpus):
        parser.error("the transcript corpus is empty")
    files = set()
    for folder in args.folders:
        if not folder.exists():
            parser.error(f"input does not exist: {folder}")
        files.update([folder] if folder.is_file() else folder.rglob("*.md"))
    if not files:
        parser.error("no Markdown files found")
    total = 0
    failures = []
    for path in sorted(files):
        for line, quote in passages(path.read_text(encoding="utf-8")):
            total += 1
            if not matches(quote, corpus):
                failures.append({"file": str(path), "line": line, "quote": quote})
                print(f"NOT MATCHED [{path}:{line}]: {quote[:180]}")
    report = {"transcript_files": len(sources), "markdown_files": len(files),
              "quotes_checked": total, "quotes_matched": total - len(failures),
              "failures": failures,
              "scope": "Normalized text matching only; attribution and timestamps require source review."}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{'OK' if not failures else 'FIX NEEDED'}: {total-len(failures)}/{total} passages matched across {len(files)} Markdown files and {len(sources)} transcripts")
    return int(bool(failures) or not total)


if __name__ == "__main__":
    sys.exit(main())
