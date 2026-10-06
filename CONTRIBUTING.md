# Contributing

Improve a workflow, its evidence, or the experience of installing and using it. For a new skill, first open an issue describing the PM job and the deliverable it would produce.

## Repository layout

```text
.claude-plugin/           Claude Code plugin and marketplace manifests
skills/<name>/
  SKILL.md               Workflow and grading rubric
  references/            Attributed frameworks and quotes
  assets/card.png        Illustrated lead team
extras/                  Optional skills outside the 25-skill collection
docs/                    Authoring, migration, and verification guides
images/                  Gallery, overview, and generation prompts/manifest
scripts/validate_repo.py Structural, link, and asset checks
check_quotes.py          Optional checks against your local transcripts
```

`digests/`, `transcripts/`, and `images/refs/` are local research inputs excluded from Git. Never commit private likeness photos, transcripts, credentials, or customer artifacts. Use synthetic examples for workflow testing.

## Editing a skill

1. Read its entire `SKILL.md` and relevant supporting references.
2. Keep the workflow focused on a concrete deliverable. Ask only for context the user has not already supplied.
3. Attribute frameworks and factual claims to the guest who introduced them. Preserve useful disagreements and their conditions.
4. Copy quotes from the source, retain the guest and timestamp, and use explicit ellipses for omissions. Write your own example questions as italic text or single-quoted text.
5. Run the skill against a representative synthetic artifact. Describe the input and observed result in your pull request.
6. Run the checks below. If you changed quotations, verify them against a local transcript corpus.

See [the authoring guide](docs/AUTHORING.md) for the full template. Local research digests are optional and are not part of a fresh clone.

## Checks

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

For quotation changes:

```bash
python3 check_quotes.py skills/price --transcripts /path/to/transcripts
```

[Verification scope and limitations](docs/VERIFICATION.md) explain what the checks establish. CI does not contain or download the transcript corpus.

## Pull requests

Describe the user problem, what changes in the resulting behavior or deliverable, and how you checked it. Include source links and timestamps for changed claims. Update the index, gallery, manifests, and migration guide when you add, rename, or remove a skill.

Be respectful, credit others, and keep reviews concrete. The existing [license](LICENSE) applies to contributions; third-party quoted material retains its original ownership.
