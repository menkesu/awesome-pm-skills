---
name: eval-plan
description: Builds an eval plan for an AI feature - error analysis on real traces, failure-mode ranking, code checks and binary LLM judges validated against human labels, CI tests, production monitoring, and a launch bar. Use when you ask how do we eval this, how do I test an AI feature, our LLM outputs are inconsistent, are the evals good enough, LLM-as-judge, hallucinations, or what accuracy is good enough to launch. Draws on 41 Lenny's Podcast guests incl. Hamel Husain, Shreya Shankar and Sander Schulhoff.
---

# Eval Plan

![eval-plan: lead guest team](assets/card.png)

Turn a vague 'the AI feels off' into a ranked list of failure modes, a small set of trustworthy evaluators, and a CI + monitoring plan you can paste into a doc. Built from 169 insights from 41 Lenny's Podcast guests. **Lead team:** Hamel Husain, Shreya Shankar, Sander Schulhoff.

## When to use
- You are shipping (or already shipped) an LLM feature and quality is judged by vibes, anecdotes or the loudest complaint.
- An engineer says *we have evals, 75% agreement* and you cannot tell whether that is good.
- Users say vague things like 'it hallucinates' or 'it doesn't follow instructions' and nobody knows what to fix first.
- You need a launch bar for a probabilistic feature (is 70% or 80% good enough?).
- You are about to swap models or cut inference cost and need proof quality holds.
- Your feature takes untrusted input or calls tools, and someone is selling you a guardrail.
- You are writing the spec for an AI feature and want the eval to be the requirements.

## Step 1 - Diagnose (ask before answering)
If the user attached traces, logs, a PRD, a judge prompt or a CSV of outputs, read them first and infer what you can. Then ask at most 4 of:
1. **Do you have logged real traces (inputs + outputs), and roughly how many per day?** No traces routes to the pre-launch play; thousands per day unlocks online judges.
2. **What is the stage and the stakes?** Novel form factor still being found, vs a core or high-stakes feature at scale. This decides vibes-first vs evals-first (Howie Liu and Chip Huyen vs Hamel Husain and Shreya Shankar).
3. **Is it a single call, a multi-step agent, or a feature taking untrusted input / using tools?** Routes to step-level evals or security testing.
4. **Who can judge 'good' (domain expert on the team?) and what exists today (judge prompts, dashboards, thumbs data)?** Decides who does the labeling and whether to grade existing work.

## Step 2 - Pick the play
| If... (situation) | Use | From | Why |
|---|---|---|---|
| You have traces and no systematic quality process | **Error analysis** (open code, axial code, count) | Hamel Husain, Shreya Shankar | Grounds every later eval in real failures; the fix list falls out of a pivot table |
| A top failure is subjective and survives a clear prompt instruction | **Narrow binary LLM judge + confusion matrix** | Shreya Shankar, Hamel Husain | One failure mode, pass/fail, validated against human labels |
| A failure is checkable by code (valid JSON, length, string match) | **Code-based evaluator** | Hamel Husain | Cheaper and needs no meta-evaluation |
| No traces yet (pre-launch) or a fuzzy feature like memory | **Hero use cases to evals**, 30-40 failing examples, ten great evals | Kevin Weil, Dianne Penn, Cat Wu | You can write the eval before the product; it is the spec |
| Brand-new form factor, use cases not converged | **Vibes first, evals after convergence** | Howie Liu, Dan Shipper | Evals need a scaffold and known use cases to test against |
| Multi-step agent or deep-research style flow | **Step-level evals + task-category hill climbing** | Chip Huyen, Roman Ugarte | End-to-end scores hide which step broke |
| Professional / subjective domain, no unit test | **Expert rubric as verifier** | Brendan Foody, Garrett Lord | An expert writes what excellent contains; a model scores against it |
| High traffic in production | **Online judges + implicit signals** | Shreya Shankar, Kiriti Badam | Evals cover known failures; monitoring finds unknown ones |
| Untrusted input, agents with tools, vendor guardrail pitch | **Adaptive red teaming + vendor questions** | Sander Schulhoff | Static test sets and 99 percent claims are meaningless |

## Step 3 - Run it

### Play A - Error analysis (the default; do this first when you have traces)
Budget: about 3-4 days of upfront work, then about 30 minutes a week (Shreya Shankar).
1. **Sample ~100 real traces** from your observability tool. 100 is a mental unblocker; the real stopping rule is theoretical saturation, when new notes stop changing your next step (Shreya Shankar). Expect anywhere from 15 to 100.
2. **Open code by hand.** For each trace write only the first, most upstream thing that went wrong, then move on. Notes must be specific enough to categorize later; *janky* is useless. The person must hold product/domain context. Do not let an LLM do this step (Shreya Shankar, Hamel Husain): it lacks product context and will say the trace looks fine.
3. **Axial code.** Export the notes as CSV, tell any LLM to create axial codes from the open codes, then rewrite its generic categories into specific, actionable ones (*capability limitation* becomes something a team can fix).
4. **Label every note** with one category, always including a *none of the above* option. Heavy use of it means your taxonomy is incomplete (Shreya Shankar).
5. **Pivot-table the counts.** Rank by frequency, then re-rank for severity: a rare failure that is really bad can outrank a common mild one (Hamel Husain). Read examples in the top categories.
6. **Expect criteria drift.** Your idea of good will change as you read more outputs, so review before locking rubrics and revisit them periodically (Shreya Shankar).
7. **Triage each top failure** (Play B, step 1). Sanity check for ownership: decompose vague complaints into the failing layer (tool use, retrieval, synthesis) before handing to engineers (Dianne Penn).

Done when: a ranked failure-mode table exists with counts, severity and a fix type for each.

### Play B - Triage, build and validate evaluators
1. **Fix directly** if the fix is obvious (a missing formatting instruction goes in the prompt). Not every failure needs an eval; one-off errors get fixed, recurring patterns get metrics (Aishwarya Naresh Reganti).
2. **Code check** if deterministic. Try this first.
3. **LLM judge** only for subjective failures that persist despite clear instructions. Typical apps end with just 4-7 judges (Shreya Shankar).
4. **Write the judge narrowly:** one failure mode, a prompt listing when it applies, output true/false. No 1-5 or Likert scales: *what is 3.2 vs 3.7?* (Hamel Husain).
5. **Validate against humans.** Hand-label a set of traces, run the judge on the same set, and build the 2x2 confusion matrix. Report false positives and false negatives separately and iterate until both approach zero. Never use raw agreement: with a 10 percent failure rate, an always-pass judge scores 90 percent (Hamel Husain).
6. **Test the judge model for sycophancy** before trusting it on subjective output: resubmit lightly edited work and see whether grades inflate each round (Dan Shipper).
7. **PM smell test.** When an engineer says only *75 percent agreement*, ask: show me the confusion matrix, and what iterations reduced both error types? If they cannot, send it back (Shreya Shankar).
8. Where raters struggle with absolute scores, collect A-vs-B comparisons; humans are much better at them (Chip Huyen).

Done when: each judge has a confusion matrix with both off-diagonal cells small, and a named owner.

### Play C - No traces yet: write the eval as the spec
1. **Hero use cases.** For each, write the question and an amazing ideal answer; these become the evals (Kevin Weil). Evals are the new PRDs (Dianne Penn, Brendan Foody).
2. **Behavior spreadsheet.** Columns: prompt, current behavior, ideal behavior, why, notes (Karina Nguyen). For trigger decisions, add ground-truth labels of conversations that should or should not trigger the feature.
3. **From fuzzy feedback to an eval.** Get the exact situation, prompt and response; find what the complaint really is; generate 30-40 failing examples with golden answers; confirm they reproduce; run on every model version; retire from focus near 100 percent (Dianne Penn). Check the set is on-distribution and includes cases where the model should not fail.
4. **Ten great evals** beat hundreds for an under-defined feature; record how to run them and which prompt raised the pass rate (Cat Wu).
5. **Set the launch bar explicitly.** Accuracy determines product shape: build a different product at 60, 95 or 99.5 percent (Kevin Weil). Choosing the threshold is the PM's call (Marily Nika). One concrete precedent: a 50-case list of realistic use cases, ship-ready at 48 of 50 (Boris Cherny's story).
6. After beta, reshape any synthetic set with real user behavior (Karina Nguyen).

### Play D - Wire it into CI and production
1. Labeled failing traces become regression tests in CI. Keep them in the repo.
2. Run each validated judge on sampled production traces (about 1,000 a day) and chart the failure rate (Shreya Shankar).
3. Add implicit signals to pick traces: regenerate clicks, feature switch-offs, abandonment (Kiriti Badam). Fiona Fung's swearing dashboard is the cheap frustration proxy.
4. **Add a metric after every incident**, measure it each release, and gate on regression (Nick Turley).
5. When a few days of review show no new distribution patterns, you are calibrated enough to give the AI more autonomy; re-calibrate after model swaps or behavior shifts (Aishwarya Naresh Reganti).
6. Once baselines exist, try cheaper models per use case and keep them only if quality holds (Shreya Shankar).

### Play E - Agents, security and expert domains
- **Multi-step flows:** evaluate each step (query diversity, retrieval overlap and breadth, aggregation, summary), not only the final answer (Chip Huyen). Group real tasks by category and track success per category weekly (Roman Ugarte).
- **Security:** measure attack success rate with adaptive attackers, not static datasets; humans broke 100 percent of defenses in about 10-30 attempts (Sander Schulhoff). Ask any guardrail vendor: how many attacks produced the catch rate, was it adaptive, does it work in other languages, what happens when your own red teamer attacks it, and why can you do what frontier labs cannot. Log all inputs and outputs. Treat injection as mitigatable, never patched.
- **Expert domains:** have a professional write the rubric like a professor's grading rubric, then score rubric item by item (Brendan Foody, Garrett Lord). Keep each item binary.

## Where the experts disagree
1. **Evals first vs vibes first.** *Camp A* (Hamel Husain, Shreya Shankar, Dylan Field, Kevin Weil): grounded evals from the start. *Camp B* (Howie Liu, Dan Shipper; Chip Huyen on ROI): vibes for novel products, rational to skip when the gain is marginal (80 to 85 percent). *Use A when* you are at scale, failures are costly, or the feature is your edge; *B when* the form factor is unsettled or the feature is non-core. Our default: vibes while discovering use cases, error analysis the moment you have real traces. Note Hamel Husain's counter: coding agents work on vibes only because developers are domain experts who dogfood all day.
2. **Evals vs production monitoring.** *Camp A* (Hamel Husain, Shreya Shankar): systematic error analysis and judges. *Camp B* (Aishwarya Naresh Reganti, Kiriti Badam): evals for known failures plus monitoring for unknown ones; Codex adds custom evals per engineer. *Use A when* you can read the traces; *B when* volume is high and customization is wide. Default: both, with recurring monitoring patterns promoted into evals.
3. **Binary checks vs rich quality bars.** *Camp A* (Hamel Husain, Shreya Shankar): narrow pass/fail per failure mode. *Camp B* (Edwin Chen): quality is a rich subjective bar, not a checklist, and generic proxies mislead; Brendan Foody and Garrett Lord reconcile this with expert rubrics. *Use A for* operational failures; *B for* creative or professional output. Default: expert-written rubric, scored item by item as pass/fail.
4. **Do guardrails work?** *Camp A* (Sander Schulhoff): no, adaptive humans break everything and prompt defenses fail. *Camp B*: security vendors claiming 99 percent catch rates. *Use A's* tests to judge any claim; limit blast radius instead of trusting a filter.

## Deliverable
```markdown
# Eval Plan: <feature>
**Owner / date / stage:** ... | **Stakes:** low / medium / catastrophic-at-scale | **Evals-vs-vibes call + reason:** ...

## 1. Data
Source of traces: ... | Sample size annotated: ... | Saturation reached? y/n | Annotator with domain context: ...

## 2. Failure modes (ranked)
| # | Failure mode | Count | Severity | Fix type (prompt / code check / judge) | Owner |
|---|---|---|---|---|---|

## 3. Evaluators
| Failure mode | Type | Definition (one failure, pass/fail) | Human-labeled N | False pos | False neg | Status |
|---|---|---|---|---|---|---|

## 4. Launch bar
Metric(s) and threshold: ... | Accuracy band and product shape: ... | Hero cases (N, pass target): ...

## 5. Pipeline
CI: labeled failing traces as tests | Online: judge on ~N sampled traces/day, dashboard | Implicit signals: ... | Add a metric after every incident: y/n

## 6. Agents / security (if applicable)
Step-level evals: ... | Adaptive red-team plan: ... | Logging: all inputs and outputs

## 7. Cadence
Upfront: ~3-4 days | Weekly: ~30 min on new samples | Re-calibrate on: model swap, new user behavior

## Open risks / criteria drift log
...

## Next 3 actions
1. ...
2. ...
3. ...
```

## Grade existing work
Score each 1-5 (1 / 3 / 5 shown), total /40, then give the top 3 fixes with the guest behind each.
| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Grounded in real failures | Tests invented at a desk | Some traces reviewed ad hoc | Open/axial coding on real traces, saturation reached (Hamel Husain, Shreya Shankar) |
| Human context in labeling | LLM writes the notes | Mixed | Domain-context human wrote the notes; LLM only clusters |
| Failure-mode ranking | One blended quality score | Categories, no counts | Counts plus severity, with fix type per failure |
| Evaluator design | Likert scales or generic metrics (cosine, hallucination score) | Some binary checks | Code checks first; narrow binary judges, 4-7 total |
| Judge validation | None, or raw agreement only | Agreement plus spot checks | Confusion matrix, both error types near zero (Shreya Shankar) |
| Launch bar and product shape | No threshold | Threshold with no rationale | Explicit bar tied to accuracy band and stakes (Kevin Weil, Marily Nika) |
| Pipeline | Manual, one-off | CI or monitoring, not both | CI regressions plus sampled online judges plus a metric per incident (Nick Turley) |
| Maintenance and drift | Set and forget | Occasional refresh | Weekly review, criteria revisited, re-calibrated on model swaps |
Output: scores table, total, top 3 fixes, and one line on whether the evals are trustworthy enough to gate a release.

## Red flags
- Writing tests before looking at data (Hamel Husain: most teams go off the rails here).
- Buying a tool and expecting it to eval for you; generic metrics like cosine similarity and hallucination score (Hamel Husain).
- Using an LLM for the open-coding step (Shreya Shankar).
- Likert-scale judges and unvalidated judges; reporting agreement without a confusion matrix (Hamel Husain, Shreya Shankar).
- Picking a model from LM Arena or Artificial Analysis and calling it evals; those are model evals (Aishwarya Naresh Reganti). Crowd leaderboards reward emojis and length (Edwin Chen).
- Building a judge for everything instead of fixing the prompt first (Shreya Shankar).
- Trusting a guardrail with a 99 percent claim, or prompt-based defenses like telling the model to ignore malicious instructions (Sander Schulhoff).
- Role prompts such as 'you are a world-class expert' as an accuracy lever (Sander Schulhoff).
- Claiming dogfooding replaces evals when your team is not the domain expert (Hamel Husain).
- Treating evals as a one-time project; a new model or new user behavior resets calibration (Aishwarya Naresh Reganti).

## Receipts
> "The answer is, just write down the first thing that you see that's wrong, the most upstream error. Don't worry about all the errors, just capture the first thing that you see that's wrong, and stop, and move on." — Hamel Husain, Lenny's Podcast (00:22:38)

> "That's just in most cases, that's a weasel way of not making a decision." — Hamel Husain, Lenny's Podcast (00:52:16)

> "if you only have the error 10% of the time, then you can easily have 90% agreement by just having a judge say it passes all the time." — Hamel Husain, Lenny's Podcast (00:57:55)

> "They don't have this matrix and they haven't iterated to make sure that these two types of errors have gone down to zero, then it's a bad smell. Go and ask them to go fix that." — Shreya Shankar, Lenny's Podcast (00:59:56)

> "If the model gets it right 60% of the time, you build a very different product than if the model gets it right 95% of the time versus if the model gets it right 99.5% of the time." — Kevin Weil, Lenny's Podcast (00:18:16)

> "you can patch a bug, but you can't patch a brain." — Sander Schulhoff, Lenny's Podcast (00:40:49)

## Go deeper
- `references/frameworks.md` - every framework in this skill, how to run it
- `references/quotes.md` - verified quotes with timestamps
- Related skills:
  - `ai-product-bets` - hand off when the question is which AI feature to build, not how to evaluate it.
  - `experiment` - hand off for A/B tests and trustworthiness checks once evals gate the release.
  - `metrics` - hand off to turn failure rates and resolution rates into a north star and metric tree.
  - `spec` - hand off to write the PRD that wraps the eval as the requirement.
