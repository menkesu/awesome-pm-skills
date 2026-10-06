# Upgrading from v1

V2 replaces the original topic-oriented collection with 25 workflows organized around PM jobs. This is a new layout and naming scheme; the mappings below are suggested replacements, not exact copies of the old workflows.

## Choose replacements

| V1 folder | Suggested v2 skill(s) |
|---|---|
| `ai-product-patterns` | [ai-product-bets](../skills/ai-product-bets/SKILL.md), [eval-plan](../skills/eval-plan/SKILL.md) |
| `ai-startup-building` | [ai-prototype](../skills/ai-prototype/SKILL.md), [ai-product-bets](../skills/ai-product-bets/SKILL.md) |
| `career-growth` | [career](../skills/career/SKILL.md) |
| `confident-speaking` | [exec-comms](../skills/exec-comms/SKILL.md) |
| `continuous-discovery` | [customer-interviews](../skills/customer-interviews/SKILL.md), [validate-idea](../skills/validate-idea/SKILL.md) |
| `culture-craft` | [hire](../skills/hire/SKILL.md), [craft-review](../skills/craft-review/SKILL.md), [ship-faster](../skills/ship-faster/SKILL.md) |
| `decision-frameworks` | [decide](../skills/decide/SKILL.md) |
| `design-first-dev` | [ai-prototype](../skills/ai-prototype/SKILL.md), [craft-review](../skills/craft-review/SKILL.md) |
| `exec-comms` | [exec-comms](../skills/exec-comms/SKILL.md) |
| `exp-driven-dev` | [experiment](../skills/experiment/SKILL.md) |
| `growth-embedded` | [growth-model](../skills/growth-model/SKILL.md) |
| `influence-craft` | [influence](../skills/influence/SKILL.md) |
| `jtbd-building` | [customer-interviews](../skills/customer-interviews/SKILL.md) |
| `launch-execution` | [launch](../skills/launch/SKILL.md) |
| `metrics-frameworks` | [metrics](../skills/metrics/SKILL.md) |
| `okr-frameworks` | [prioritize](../skills/prioritize/SKILL.md) |
| `positioning-craft` | [position](../skills/position/SKILL.md) |
| `prioritization-craft` | [prioritize](../skills/prioritize/SKILL.md) |
| `quality-speed` | [craft-review](../skills/craft-review/SKILL.md), [ship-faster](../skills/ship-faster/SKILL.md) |
| `ship-decisions` | [decide](../skills/decide/SKILL.md), [ship-faster](../skills/ship-faster/SKILL.md) |
| `stakeholder-craft` | [influence](../skills/influence/SKILL.md), [hard-conversations](../skills/hard-conversations/SKILL.md) |
| `strategic-build` | [spec](../skills/spec/SKILL.md), [prioritize](../skills/prioritize/SKILL.md) |
| `strategic-pm` | [strategy](../skills/strategy/SKILL.md), [decide](../skills/decide/SKILL.md) |
| `strategic-storytelling` | [position](../skills/position/SKILL.md), [exec-comms](../skills/exec-comms/SKILL.md) |
| `strategy-frameworks` | [strategy](../skills/strategy/SKILL.md) |
| `user-feedback-system` | [customer-interviews](../skills/customer-interviews/SKILL.md), [pmf-check](../skills/pmf-check/SKILL.md) |
| `workplace-navigation` | [influence](../skills/influence/SKILL.md), [hard-conversations](../skills/hard-conversations/SKILL.md), [career](../skills/career/SKILL.md) |
| `zero-to-launch` | [validate-idea](../skills/validate-idea/SKILL.md), [ai-prototype](../skills/ai-prototype/SKILL.md), [launch](../skills/launch/SKILL.md) |
| `one-step-better-ai-pm` | Retained in [extras/one-step-better-ai-pm](../extras/one-step-better-ai-pm/SKILL.md), outside the main plugin. |

## Update an installation

1. Back up any skill copies you customized. Record which personal or project directory you installed them into.
2. Install v2 using the [current instructions](../README.md#install). The plugin loads only the 25 folders under `skills/`.
3. Compare your old copies with the replacements, then remove obsolete v1 folders from your assistant’s skills directory. Installing v2 does not remove them automatically.
4. Start a new session and invoke a skill explicitly to confirm it is available.

The `exec-comms` name is retained but its workflow was rewritten. Old installed copies with that name can conflict with v2, so choose which one to keep.

## Optional daily skill

The GenAI PM daily skill remains available separately:

```bash
mkdir -p ~/.agents/skills
cp -R awesome-pm-skills/extras/one-step-better-ai-pm ~/.agents/skills/
```

For standalone Claude Code, use `~/.claude/skills/` instead. Read its prerequisites before running it; unlike the core collection, it accesses an external feed and needs a subscriber email.

## Find original v1 content

V1 remains in Git history at the pre-v2 commit `53530ef`. To inspect it without replacing your current checkout:

```bash
git worktree add ../awesome-pm-skills-v1 53530ef
```

The old root-level skill paths and image paths are removed in v2. Update bookmarks and integrations to `skills/<name>/SKILL.md`.
