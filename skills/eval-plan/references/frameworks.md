# Eval Plan - Frameworks

Every distinct method in the eval-plan digest, grouped by theme. Originators are credited; others who endorse the same idea are noted.

## 1. Discover what to evaluate

**1. Error analysis: open coding, axial coding, counting** (Hamel Husain and Shreya Shankar; Hamel Husain & Shreya Shankar episode). The core eval workflow, borrowed from social science and classic ML, not invented by them.
- Use for any LLM product with logged traces: once up front, then about 30 minutes a week. Fails if an LLM writes the first notes or the human lacks product context.
- Steps: sample real traces; write a note on the first thing that went wrong in each; have an LLM propose axial codes (failure categories); refine them to be specific; relabel each note; pivot-table counts; choose fixes or evaluators for the top problems.
- Benchmark: about 3-4 days upfront, then ~30 minutes a week. Aishwarya Naresh Reganti's calibration reviews are the same loop under another name.

**2. Open coding: note the most upstream error** (Hamel Husain). Record only the first thing wrong in a trace, then stop and move on. First 2-3 traces feel slow, then it speeds up. Notes like *janky* cannot be categorized later (Shreya Shankar).

**3. LLM-assisted axial coding** (Hamel Husain). Paste the CSV of notes into an LLM using the vocabulary open codes and axial codes (it already knows the method); then you refine generic categories into actionable ones. Run it after 50-100 human-labeled traces. Failure: accepting categories blindly.

**4. 'None of the above' category** (Shreya Shankar). Include it when auto-labeling notes. Its usage rate measures how incomplete the taxonomy is; review those notes and add categories.

**5. Pivot-table failure ranking** (Hamel Husain). Count per category, read examples in the top ones, and weigh severity as well as frequency. Spreadsheets suffice.

**6. Theoretical saturation** (Shreya Shankar). The stopping rule for labeling: stop when new traces stop producing new kinds of notes that would change your next step. Hamel Husain's *100 traces* is a mental unblocker; real range 15-100.

**7. Criteria drift** (Shreya Shankar, from her research paper on validating validators). Definitions of good and bad shift as you review outputs, so rubrics cannot be fully specified upfront, even by experts. Review outputs before locking criteria and revisit them periodically.

**8. Sweat the tokens as much as the pixels** (Dianne Penn). Read the model's failed trajectories in depth, like walking a UI flow; label failure type (hallucination, overconfidence) and write the pain point down. Pairs with decomposing a vague complaint into the failing layer (tool use, search, synthesis, alignment) before bringing it to engineers.

**9. Ask the model to introspect** (Cat Wu). When an agent does something unexpected, ask why; the answer exposes confusing system prompt text or missing harness steps. Also check subagents for unverified work.

**10. Five trusted model-feedback users and team-lunch vibe check** (Cat Wu). Find about five people who articulate model strengths precisely; collect everyone's vibes on a new model, turn them into hypotheses, then extract data to test them.

## 2. Build evaluators

**11. Triage: fix directly vs code eval vs LLM judge** (Hamel Husain; Aishwarya Naresh Reganti endorses). Obvious errors get prompt or code fixes; deterministic checks get code evaluators (cheaper, no meta-evaluation); only subjective, persistent failures get a judge. One-off errors get fixed; recurring emerging patterns get a metric.

**12. Narrow, binary LLM judge** (Shreya Shankar, Hamel Husain). One failure mode, a prompt describing when it applies, output pass/fail. Easier and more reliable than the original task. Avoid 1-5 and Likert scales; Hamel Husain calls them a way to dodge the decision. Typical product ends with 4-7 judges.

**13. Judge validation with a confusion matrix** (Hamel Husain, Shreya Shankar). Hand-label traces, run the judge on the same ones, build the matrix, and iterate on the prompt until both false positives and false negatives are near zero. Raw agreement misleads on rare errors (a 10 percent failure rate gives 90 percent agreement for an always-pass judge).

**14. PM smell test for judge reports** (Shreya Shankar). If an engineer reports only a percent agreement, ask for the matrix and the iteration history before accepting.

**15. Sycophancy test for judge models** (Dan Shipper). Ask the model to grade a piece of work, resubmit lightly edited versions; if grades climb each round (B+, A-, A) it lacks a real sense of quality and should not be the judge on subjective output.

**16. Human pairwise preference** (Chip Huyen). Humans compare A vs B far more reliably than they assign scores; build feedback collection and reward or judge training on comparisons. Karina Nguyen's human win-rate evals use the same idea across model versions.

**17. Expert rubric as verifier** (Brendan Foody; Garrett Lord and Edwin Chen endorse). A domain professional writes a rubric of what excellent looks like (for example a lawyer for contract redlining); a model scores outputs against items; the score is both eval and reward. In code, a unit test plays the same role. Risk: poorly designed rubrics invite reward hacking.

**18. Deterministic trigger evals** (Karina Nguyen). For decision behaviors, label conversations that should or should not trigger a feature and score pass/fail.

**19. Rubrics with a model as judge for non-verifiable domains** (Garrett Lord). Where no guaranteed answer exists, experts define a good response and a model scores it. For verifiable domains (math, physics), experts break the model, supply the ground truth and write the failing reasoning steps instead.

**20. Code-based first** (Hamel Husain). Valid JSON, length, markdown, string match: write a Python check before reaching for a judge.

## 3. Build the dataset and launch bar

**21. Hero use cases to evals to hill-climbing** (Kevin Weil). Write the question you want to be able to ask plus an amazing ideal answer, convert to evals, iterate or fine-tune until scores define a product. Teams that cannot change the model benefit less from hill-climbing.

**22. Behavior spreadsheet eval** (Karina Nguyen). PM sheet with tabs or columns: prompt, current behavior, ideal behavior, why, notes. Doubles as eval set and training data. Nick Turley agrees evals can live in a spreadsheet as articulated success criteria.

**23. User feedback to eval pipeline** (Dianne Penn). Get the exact situation, prompt and response; find the real failure (for example 80 percent invalid JSON); generate 30-40 failing examples with golden answers; check reproducibility; add to the eval repo and run per model; retire near 100 percent. A good eval is on-distribution with both failing and should-not-fail cases. Related: Evals are the new PRDs (Dianne Penn, Brendan Foody).

**24. Ten great evals** (Cat Wu). For under-defined, model-driven features such as memory, write about five to ten evals, document how to run them, record which prompt lifted success. Not every feature needs evals.

**25. Accuracy band determines product shape** (Kevin Weil). Measure success rate on your use case and choose UX and guardrails accordingly (60, 95, 99.5 percent are different products); re-measure as models change. Marily Nika: picking the launch bar is the PM's responsibility.

**26. Informal threshold: 48 of 50** (Boris Cherny, story about a PM). A list of 50 realistic use cases run through the product with a release bar set at 48.

**27. Quality bar over coverage** (Keith Coleman). When trust is the product, one bad shown output is worse than many withheld good ones; set conservative thresholds (only about 8 percent of proposed notes display) and calibrate with user feedback. Fails where recall and volume matter more.

**28. Few-shot with attached reasoning** (Sander Schulhoff). For structured tasks, expert-produced examples with reasoning pasted into the prompt lifted a medical coding task by about 70 percent. Format examples as Q:/A: pairs or XML tags. Related prompt hygiene: put long static context first so it caches.

## 4. Run in production and keep it alive

**29. Eval artifacts everywhere** (Shreya Shankar). Labeled failing traces into CI; judges on about 1,000 sampled production traces a day with a failure-rate dashboard. Teams that do this have a sharp sense of quality that acts as a moat.

**30. Evals plus production monitoring** (Kiriti Badam, Aishwarya Naresh Reganti). Evals encode known must-not-regress failures; monitoring with explicit (thumbs) and implicit (regenerate, switch-off) signals surfaces unknown ones. Recurring patterns become new eval datasets. Codex adds A/B tests and custom evals per engineer.

**31. Minimizing surprise** (Aishwarya Naresh Reganti). Review behavior every day or two; when new information per review is low, increase autonomy. Reset on model swaps or user-behavior drift.

**32. Add a metric after every incident** (Nick Turley). When reality reveals a problem, build a metric for it, measure each release and gate on regression. Real failure cases beat saturated benchmarks.

**33. Task-category hill climbing** (Roman Ugarte). Collect real tasks given to the agent, categorize, and measure per category week over week; give infra concrete failures.

**34. Virtuous improvement cycle** (Bret Taylor). Measure automated resolution rate, use AI to surface frustration and missing capabilities, add capability, re-measure (for example 65 to 75 percent).

**35. Eval-driven model swaps** (Shreya Shankar; Mike Krieger endorses a repeatable process). Baseline on the expensive model, swap in cheaper ones per use case, keep if quality holds. Capture traces to rerun on every new model.

**36. Bad vs sad** (Fiona Fung). Bad is irrecoverable; sad is a recoverable pain point. Teams define examples and goals; watch sads stack into bads. Add the swearing dashboard as a frustration proxy.

## 5. Multi-step agents and model selection

**37. Step-level evals for agents** (Chip Huyen). Evaluate each step of a deep-research style flow: query diversity, result overlap, breadth, depth, relevance, aggregation. Keep adding evals until coverage and confidence are good.

**38. Build your own benchmark** (Dan Shipper; Mike Krieger and Simon Willison echo it). A private benchmark from a real painful case (senior engineers fixing a vibe-coded app, scored against each new model; models scored about 30 of 100 until a late model hit about 62 versus high 80s for humans). Also the CEO benchmark on private meeting transcripts. Public benchmarks only cover problems already framed.

**39. Distrust public benchmarks and arenas** (Edwin Chen, Aishwarya Naresh Reganti). Leaderboards reward emojis, bolding and length; picking a model from them is model evals, not product evals. Use expert humans on real tasks and your own dataset.

**40. Evals vs ROI** (Chip Huyen). Estimate eval cost against the gain from shipping a feature; vibe-check when gain is marginal and failures are not catastrophic; be rigorous at scale or when the feature is your edge. Evals guide development by exposing weak segments or steps.

**41. Vibes before evals** (Howie Liu; Dan Shipper vibe checks). For a novel form factor, throw varied prompts, learn where it works, scope to that cluster, then write evals. Fails for incremental features or large-scale products.

## 6. Adversarial robustness and security testing

**42. Adaptive evaluation and attack success rate** (Sander Schulhoff). Measure the share of attacks that succeed using adaptive attackers (humans), not static sets. Humans broke every defense in roughly 10-30 attempts.

**43. Vendor challenge questions** (Sander Schulhoff). Ask for attack counts and adaptivity behind a catch rate, other-language performance, results when their red teamer hits their guardrail, and why they succeed where frontier labs have not.

**44. Jailbreak families to test** (Sander Schulhoff). Story and role-play framing, typos the model understands but filters miss, and obfuscation (Base64, ROT13, translation). Guardrail models are less intelligent than the model they guard.

**45. Mitigations that do work better** (Sander Schulhoff). Safety-tune on product-specific harms; fine-tune narrowly so the model can only do one task; log all inputs and outputs; run incentivized crowdsourced red-teaming rather than hourly contractors. Never promise it is patched.

## 7. Agent-assisted testing

**46. Red/green TDD with agents** (Simon Willison; Fiona Fung agrees). Tell the agent to write a failing test first, implement, rerun. Tests accumulate protection; verbose suites are fine because agents maintain them.

**47. Swarm of simulated end users and API clones** (Simon Willison, StrongDM story). Agents role-play real user requests around the clock against agent-built simulations of third-party APIs. Budget tokens; does not cover security.

**48. Peer review across models** (Zevi Arnovitz). Run multiple models' reviews on the same branch and require the implementing agent to refute or fix each finding.

**49. Check in what good looks like** (Fiona Fung). Commit specs and quality statements to the repo so automated review validates changes against them.
