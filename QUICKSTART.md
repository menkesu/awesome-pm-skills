# Quickstart

## 1. Install a skill

Follow the [installation instructions](README.md#install) for your assistant. Start with one skill that matches work you already have. You can add the rest later.

## 2. Bring an artifact and a goal

For example, after installing `price`:

```text
We sell a B2B support product to teams of 10–100 agents. We currently charge
$39 per seat. Here’s our pricing page and the last quarter’s conversion data.
Grade our packaging, identify the biggest issue, and propose a test we can
run in two weeks. We cannot change billing infrastructure this quarter.
```

With the Claude Code plugin, start with `/awesome-pm-skills:price`. With a standalone Claude Code or Cursor installation, use `/price`. In Codex, use `$price`.

Other useful starting prompts:

| Skill | Prompt |
|---|---|
| `spec` | Here’s our draft PRD. Grade it, then rewrite the weakest sections. |
| `eval-plan` | These 30 support-agent outputs include failures. Cluster the errors and design an eval suite. |
| `pmf-check` | Here’s our PMF survey export. Diagnose the strongest segment and recommend what to do next. |
| `exec-comms` | Turn these notes into an executive update with a clear decision request. |
| `hard-conversations` | Help me prepare feedback for a colleague. Separate observations from assumptions. |

## 3. Review the result

Check assumptions, source attributions, and the proposed next actions. The skills provide a structured starting point; your customer evidence and constraints determine whether a recommendation fits. Benchmarks cited from an episode describe that context, not a universal target.

## Local Claude Code plugin check

From the cloned repository, run:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
claude --plugin-dir .
```

In that session, invoke `/awesome-pm-skills:price` and provide a sample artifact. The plugin should expose 25 skills. Manifest validation checks configuration; a live task checks how the model follows a workflow.

## Updating an installation

For the marketplace installation, update the marketplace and plugin through Claude Code’s plugin manager. Restart the session as required by the client.

For copied skills, pull the latest repository version, compare it with any local edits, and copy the selected folders again. V1 names and folder locations changed: see [Upgrading from v1](docs/MIGRATION.md).

## Troubleshooting

- **Skill missing:** check that the destination contains `<skill>/SKILL.md`, not an extra nested `skills/` folder. Start a fresh session if your client has not refreshed discovery.
- **Duplicate skills:** remove one of the duplicate plugin/personal/project installations after checking for your own edits.
- **Generic output:** provide an artifact, a clear goal, and constraints. Ask the assistant to use the skill’s routing table and deliverable template.
- **Using a web chat:** attach the skill and references explicitly; automatic local discovery is an editor/agent feature.

Browse the [skill index](SKILLS-INDEX.md) or [illustrated gallery](images/README.md).
