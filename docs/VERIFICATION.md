# Verification and provenance

## Build provenance

The v2 build was synthesized from a 340-episode research corpus and 10,567 extracted insights, as recorded during authoring. Frameworks are credited to named guests in each skill’s references; quotations include guest names and episode timestamps. These source-build totals are historical provenance, not a claim about the current number of podcast episodes.

The optional local `digests/` folder contains intermediate research inputs. Digests, transcript files, and likeness reference headshots are excluded from Git. A fresh clone includes the workflows, published references, and final illustrations.

## Text matching

```bash
python3 check_quotes.py skills --transcripts /path/to/transcripts
```

You can supply multiple skill folders, set `LENNY_TRANSCRIPTS`, or write a summary with `--report /path/to/report.json`. Python 3.9 or newer is sufficient; this checker has no third-party dependencies.

The checker scans double-quoted passages of at least six words in Markdown. It normalizes whitespace, case, curly quotation marks and apostrophes, dashes, and ellipses. If a quote contains an explicit ellipsis, every non-empty fragment must occur in order within the same transcript. It exits with a failure status for unmatched text or zero checked passages, and rejects missing or empty corpora.

A successful match establishes textual occurrence. It does **not** establish that the quoted guest said it, that the timestamp is correct, that the passage is interpreted accurately, or that a benchmark applies to a new product. Review those details against the source when adding or changing evidence.

The local v2 check is recorded in [quote-verification.json](quote-verification.json). Its transcript-file count describes the supplied local directory, which can include supplementary files; it is not used to redefine the historical 340-episode build count. The transcript corpus is not included in the report.

## Repository validation

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests
```

The validator checks the 25-skill inventory, YAML frontmatter, reference and asset files, local documentation links, plugin metadata, image manifest coverage, and exclusion of private inputs from the Git index. GitHub Actions repeats these checks without transcripts, external feeds, or model calls.

Claude Code’s own configuration check is separate:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

The v2 plugin also installed successfully as version 2.0.0 in an isolated local Claude Code configuration and appeared as enabled. The local marketplace/package contained only the manifests, core skills, README, and license; private inputs were not copied.

These are structural checks. They do not test the quality of a model’s output. For workflow changes, run a representative synthetic input through the skill and describe what happened in the pull request.

## Illustrations

The 25 watercolor cards were generated with the built-in image generation tool from private photo references and manually reviewed for guest order, labels, composition, style, and icon. They are AI-generated illustrations and do not imply endorsement. The [generation manifest](../images/generation-manifest.json) records the exact successful prompts and native dimensions. The final cards are 1086 × 1448 pixels (3:4); the prompts requested 1536 × 2048, and the outputs have not been upscaled.
