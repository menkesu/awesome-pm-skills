# Experiment frameworks

Every distinct method in the experiment digest, grouped by theme. Originators are flagged. Each entry: what it is for, when it applies or fails, steps, benchmark.

## A. Whether and when to test

**Two reasons to experiment** (Lauryn Isford) — A grow team experiments for precise metric impact or for risk mitigation. If neither is needed, ship without a test. Steps: ask whether you need precise impact; ask whether the change is risky enough to need protection; if neither, ship and measure afterward. Fails on large, dramatic changes where downside risk is real. Related: Isford shipped Airtable's Forms submitter-copy feature without a test because analysis showed it was net good and the signup lift was visible at top line.

**Experiment cost exceeds possible gain** (Stewart Butterfield) — Compare the maximum plausible upside of a trivial UI choice to the full cost of testing it (flags, instrumentation, dashboards, meetings). Steps: estimate max value difference; estimate total test cost; skip and decide by judgment if cost exceeds upside. Fails when the plausible effect is large. Slack's threads test debated 2.17 vs 2.14 messages per thread.

**One-month sample size rule** (Elena Verna) — If you cannot collect the required sample in a month, do not A/B test. Ship, compare pre vs post with staged readouts at 24 hours, 7 days and 28 days, revisit months later for retention or expansion effects, roll back if it fails. Fails for big strategic pivots or very high-traffic real estate where 0.1% means millions.

**When to start A/B testing** (Ronny Kohavi; Albert Cheng agrees) — You need tens of thousands of users at minimum; roughly 200,000 to detect 5% effects on a retail conversion metric. Below that, build the culture and platform and look only for large effects. Cheng: with consumer scale and frequency, start now with a third-party tool, because pattern matching from experience is often wrong. Fails for low-base-rate metrics, which need more users.

**Test everything** (Ronny Kohavi; Carilu Dietrich on PLG; Jackson Shuttleworth early in a feature's life) — Every change sits inside an experiment; you cannot experiment too much, only over-focus on increments. Allocate part of effort to high-risk, high-reward ideas like an investment portfolio. Fails where units are scarce or the platform makes each test costly.

**Early product: skip the test** (Adriel Frederick) — Very early, build the big things; the cost of experimentation is time, and 50/50 splits can hurt other parts of the product. As the product matures, shift toward one big bet plus many refinements.

**Ship with safety net instead of full test** (Luc Levesque, Nilan Peiris, Lauryn Isford) — For high-confidence changes, use pre-post analysis and a smaller holdout/beta aimed at detecting breakage rather than a full significance test. Steps: define what breaking looks like; run a small holdout; skip large-sample significance when you would not roll back anyway. Fails for risky changes without safety nets and for teams lacking good intuition (Peiris warns of opinion-led hubris).

**Build conviction, do not split-test your way to love** (Nilan Peiris) — Test early to build conviction, then commit to the strategic bet and track the lever rather than each experiment's payback. Peiris told a new PM to pick one change in three weeks after talking to customers, then launch and test it.

**Optimization is not discovery** (Marty Cagan) — Low-risk tests like call-to-action tweaks are optimization; teams do them because they are given feature roadmaps or fear breaking things. Distinguish the two before reporting either as innovation. Tim Holley makes a related point: near-universal A/B testing at Etsy proves causality for specific changes but can miss bigger net-new bets.

## B. Designing the test

**Hypothesis-driven A/B testing** (Brian Chesky; Chris Miller; Crystal Widjaja; Laura Schaffer) — Start with a designed treatment and stated hypothesis, not blue vs green. Steps: write hypothesis and expected outcome before building; define success criteria; add qualitative corroboration when confidence is lower. Chesky also uses occasional holdbacks and treats the product as a cohesive system. Widjaja: an idea you cannot design an experiment for is close to useless. Jackson Shuttleworth: how strong the hypothesis must be scales with how expensive the test is.

**Pre-registered validation plan** (Laura Schaffer) — Decide how you will validate before you see results; otherwise teams make the data fit the hypothesis. Harden the plan if you accept more risk.

**Variance reduction** (Ronny Kohavi) — Cap skewed metrics (nights booked, purchases), apply CUPED with pre-experiment data, and make scorecards available within a day so you need fewer users and get answers faster.

**Many arms to isolate hypotheses** (Jackson Shuttleworth) — Break a combined change into component hypotheses and give each its own arm (opt-out button separate from easier-goal fallback). Fails with low traffic.

**Decompose big-bang redesigns** (Ronny Kohavi; Laura Schaffer; Melissa Tan) — Do the redesign in steps, test along the way, launch only winners, since perhaps four of 17 changes are good. Tan: a checkout page with many changes failed and nobody knew why. Fails only when a full redesign is a deliberate bet accepting a high chance of failure.

**Redesign recovery plan** (Elena Verna) — A redesign resets you to a starting point lower than your optimized current experience. Forecast a hit at launch, do not judge on the seven-day read, and budget two to six months of optimization with the team still resourced.

**Dogfood the experiment; minimum viable experiment with mechanism** (Gina Gotthilf; Gustav Soderstrom on big MVPs) — Use each variant yourself and ensure it contains the elements that make the mechanic work. Duolingo's badge for signing up failed because no one is proud of signing up, and badges were abandoned for months. Soderstrom: when an MVP needs new UI and new algorithms, a failure may be a false negative from execution quality.

**Remove confounding variables / saturation seeding** (Nikita Bier) — Test the best, even unscalable, version so a failed test cannot be dismissed as bad execution. For a social app, saturate one dense community (one school) to judge product signal, then rely on organic spread; this is a test method, not a growth strategy. Build a reproducible testing process (a year per app down to two weeks).

**Hypothesis plus system view** (Albert Cheng) — The system matters as much as any experiment: start from a growth model, instrument in and out, and sanity-check metric definitions in the tool, or you get wonky results.

**Constant copy testing** (Jackson Shuttleworth; Tim Holley) — Build cheap copy-test infrastructure including translations and ship variants continuously. Duolingo changing Continue to Commit To My Goal was a massive win; Etsy's one-line carbon-offset message in the cart moved conversion. Fails with small user bases. Elena Verna counters: button color tests are an old tactic; pick an accessible, bright color.

## C. Trustworthiness and statistics

**Sample ratio mismatch check** (Ronny Kohavi, originator) — If the actual split differs from the intended one by more than chance, the experiment is invalid. Steps: compute the probability of the observed split (chi-square); if unlikely, distrust results; debug bots, pipeline filtering, campaign traffic, assignment placement; make the warning impossible to ignore (blank scorecard, red numbers). About 8% of Microsoft experiments had SRM.

**Twyman's law** (Ronny Kohavi) — Any figure that looks interesting is usually wrong. Treat a 10% move when normal is under 1% as a bug until data, logging, SRM and instrumentation are checked and the result replicates. A few real outliers exist (Bing ad title) and survive replication.

**Peeking and fixed horizon** (Ronny Kohavi) — Stopping at the first p below 0.05 raises false positives to around 30%. Fix duration upfront, use sequential methods designed for peeking, validate with A/A tests.

**False positive risk** (Ronny Kohavi) — One minus p is not the probability the variant is better. With an 8% prior success rate, a p below 0.05 result has a 26% chance of being false. Estimate your historical success rate, apply Bayes' rule, use stricter thresholds when priors are low.

**Replicate borderline wins** (Ronny Kohavi) — Flag 0.01 < p < 0.05, rerun, combine with Fisher's or Stouffer's method, require lower p-values (below 0.01) for shared learnings. Jason Cohen's version: with rare real winners, even a 95%-accurate test yields more false positives than true wins, so stacked small winners rarely move overall conversion; check with holdouts.

**Stat sig is not a green light** (Ramesh Johari) — Data science is accumulation of evidence; one stat-sig result that contradicts everything you know does not overturn it. Weigh against priors and ask whether test length and data can answer the question.

**Bayesian testing with priors** (Ramesh Johari) — Encode earlier tests of the same flow into a prior, combine with the new data, and credit experimenters for how much their test moved the prior (even failed ones). Fits companies running many repeated tests on similar surfaces.

**Trust as the core of the platform** (Ronny Kohavi) — The platform is a safety net and an oracle. Build automated validity checks, stop reporting when they fail, run A/A tests.

**Before, after, and one click up** (Shaun Clowes) — Before trusting a surprising result, check what happened upstream, downstream (does retention persist?), and one level up (how much of the stream, effect on revenue per customer). Trust your intuition when a result looks insanely wrong; check selection bias.

**Variant vs control, not pre vs post** (Mayur Kamat) — Blended dashboards and pre/post comparisons mislead under macro swings; analyze by cohort and against a control.

**Lower the confidence threshold** (Laura Schaffer; Brian Tolkin) — Product work does not carry pharma's cost of false positives; accept less than 95% (Tolkin: 80% in low-volume cases) to run roughly twice as many experiments, but set criteria first and corroborate qualitatively. Fails in high-stakes domains. Kohavi's false positive risk is the counterweight.

**Single failed experiment tells little** (Eric Ries) — Establish a baseline, run a series of experiments and check for implementation bugs before declaring the value proposition wrong (a JavaScript bug produced 0% signups).

## D. Readout and decision rules

**Neutral experiment policy** (Jackson Shuttleworth) — Shut down neutral experiments that add UI or cognitive load. Ship a neutral one only when you have conviction it creates a platform for later gains, then build it into V1 next time.

**Ship neutral with good intuition** (Archie Abrams) — If neutral, pick the variant you would build from a blank slate and watch long-term holdouts. Fails for teams without intuition or accountability. Opposed by Kohavi: do not ship flat results to justify effort or morale.

**Ship up-funnel lifts, discount the impact** (Archie Abrams) — Without long-term data, measure as deep in the funnel as you can, ship positive up-funnel lifts, but do not overestimate their value.

**Absolute DAU and later-day retention** (Jackson Shuttleworth) — Report incremental absolute DAUs; compare day 1, 7 and 14; day-14 impact above day-1 signals durable retention; control for novelty and recency bias.

**Guardrails with the north star** (Lauryn Isford) — Pair the north star with guardrails; when a guardrail drops, go deep into the experience that caused it. Sarah Tavel: once the core action is fixed, a feature succeeds only if the percentage of users completing it, or the count per cohort, rises.

**Tie experiments to business metrics** (Naomi Ionita) — Connect results to warehouse metrics (subscriptions, revenue, margin), not only click-through.

**Proxy metrics for retention** (Adam Fishman; Tim Holley) — Do not wait 90 days; find an early behavior that predicts retention (time to first patron, first $100 processed) and sample onboarded users qualitatively. When retention is the goal, look at return in 30, 60 and 90 days.

**A/B tests tell you what, research tells you why** (Judd Antin) — Pair experimenters with researchers from the start; after a surprising result, get evidence on why instead of re-testing endlessly.

**Perfect New Release test** (Gibson Biddle) — Customers said they wanted new releases faster, but next-day delivery moved monthly cancel rate only from about 4.5% to 4.45%, worth about $1M against about $5M of inventory cost. Steps: test what customers say they want against retention; value retained customers (saved customers x lifetime value x word-of-mouth factor); compare to cost. The word-of-mouth multiplier is debatable.

**Stated vs revealed preference** (Andrew Bosworth) — At News Feed launch users were outraged yet doubled usage. Compare what users say with what they do; separate the thing is wrong from the details are wrong. Fails without behavioral data.

**Home redesign recall vs discovery** (Gustav Soderstrom) — Separate angry feedback about changed habits from real worsening; check quant signals like traffic shifting to search; compare new cohorts with existing ones; update the hypothesis and retest.

## E. Long-term validity

**Two layers of holdouts** (Archie Abrams) — Quarterly 5% holdout from every change; for new-merchant changes, 50/50 for a few weeks, ship the winner, keep tracking the original cohort for a year. Fails for existing-user changes where cohorts are hard to hold.

**Global holdout** (Shaun Clowes) — 10% of users never see any experiment, so you can compare same-vintage cohorts. A non-persistent lift is not automatically a failed experiment.

**Long-term holdouts per surface area** (Sri Batchu) — Each surface (checkout, ads) gets its own small holdout to measure cumulative impact of a half's work and validate translation factors. Permanent holdouts have revenue costs.

**Long-term lookback, three outcomes, automated pings** (Archie Abrams) — Revisit your biggest winners one or two years later; re-read cohorts at 3, 6, 9, 12 months; classify as pull-forward, flipped, or hidden pocket; let the tool ping every experimenter. At Shopify, 30 to 40 percent of early lifts disappear. Dunning notification lifts did not last because the selected users were not committed. Jason Cohen cites the same about-a-third figure.

**Call early, watch long** (Archie Abrams) — Call at about three weeks, ship, keep the group held and re-check.

## F. Low volume, B2B and small samples

**Power analysis first** (Brian Tolkin) — Compute minimum detectable effect and runtime; accept even six months for important tests; otherwise use observational data, diff-in-diff, sister or twin cities, geo segmentation, 80% confidence, long-term holdouts, more customer conversations, then intuition.

**Fail conclusively, maximize the treatment effect** (Sri Batchu) — In B2B with tiny samples, state a strategic hypothesis, throw every plausible tactic at it so a negative is conclusive, stop for good on failure, and prune for cost if it works. Fails for cheap fast tests and when you need to isolate which tactic worked. Half-run tests get retried by every new executive.

**Small samples still give direction** (Crystal Widjaja) — With 30 data points trends hold and only precision improves. Fails when you need fine effect sizes.

**Parallel path as an experiment** (Grant Lee) — Run two ideas in parallel with equal investment for a fixed time, pick the one with unbounded upside and more energy; strong opinions weakly held.

**Customer pilot program** (Noah Weiss) — Where A/B tests are hard (multiplayer B2B), recruit diverse customers under agreement, roll out progressively, be willing to kill features before general release.

**Carve-out cohort** (Tomer Cohen) — Carve out a randomized cohort (2 million members) too small to hurt overall numbers and give a team full liberty to build for them; use observed behavior change as evidence for rollout.

## G. Cheap validation before A/B

**Assumption testing** (Teresa Torres, originator) — Break an idea into assumptions, prioritize them, run small tests for one assumption each, work across about three ideas, and compare at week's end (half a dozen to a dozen tests a week). Assumption testing is the start of delivery, not a separate phase.

**Wizard of Oz validation** (Crystal Widjaja) — Fake the experience manually (WhatsApp group plus back-end vouchers, mocked screenshot in-app messages, Typeform quiz), measure value prop and conversion, then invest engineering.

**Validate before A/B testing; cheap hacky MVP** (Laura Schaffer) — A/B testing is among the most expensive ways to validate. Use painted door and design mocks first; ship the ugliest quick version of a hypothesis; if it is not embarrassing you went too far.

**Test the extremes** (Lane Shackleton) — Launch the least and most aggressive versions right away to learn the bounds (tiny vs giant skip button).

**Chris Rock testing model** (Marc Benioff) — Test ideas in small venues, iterate on audience response, go big on what works.

**Break-even pricing model test** (Madhavan Ramanujam) — Offer structures that cost the same at typical volume and see which customers pick; the indifferent option never wins.

**Cheap ad test for positioning** (Chris Hutchins) — A few-hundred-dollar ad before building: low tap-through points to topic, description or cover; taps without conversions point to weak content.

**Value prop A/B testing** (Meltem Kuran Berkowitz) — Move to a marketer-editable platform and test problem-first, solution-first, time-saving and cost-saving angles. Laura Schaffer: let non-engineers ship experiments with drag-and-drop CMS tools.

## H. Portfolio, culture and cadence

**Experiment failure rates** (Ronny Kohavi) — About 66% fail at Microsoft, about 85% at Bing, 92% at Airbnb search; Booking and Google Ads publish 80-90%. About 10% of experiments abort on day one due to bugs. Other benchmarks: Duolingo more than 50% fail (Gina Gotthilf); Facebook about 60% success (Adriel Frederick); Instagram 60-70% positive with heavy de-risking (Bangaly Kaba); consumer products 30-50% (Albert Cheng); growth teams about 30% (Sri Batchu); 20-30% typical, over 30-40% means thinking too small (Chris Miller); 80-90% of hypotheses fail (Laura Schaffer).

**Growth as a learning machine** (Deb Liu; Laura Schaffer) — Ship more experiments and raise the hit rate: 20 experiments at 20% beat a perfect plan of four; moving to 30% means 50% more wins. Schaffer: running too few experiments is itself a major risk. Fails where each test is expensive.

**Cannonball and lead bullet portfolio** (Adriel Frederick) — Set an explicit split, for example 80% big bets and 20% small, to force fewer, better experiments. Frederick also warns of small-experiment laziness.

**Experiment-everything breeds incrementalism; learning is a win** (Ramesh Johari) — Teams judged on win counts pick incremental ideas and run tests too long. Allow bolder hypotheses, run experiments shorter, record learnings even from flat or negative tests (badges teach how attention is redirected), and be quantified rather than data-driven by putting leadership's beliefs on the table for unmeasurable effects. Learning has a price: holding out control costs samples but reveals true value.

**Prediction is not decision-making** (Ramesh Johari) — Frame models around the causal difference an action makes (incremental LTV from a promotion) rather than absolute levels.

**Inch-by-inch wins** (Ronny Kohavi) — Most wins are small and compound: Bing relevance targets about 2% a year; Airbnb's roughly 250 search relevance experiments added a 6% revenue improvement. Tom Verrilli: in high growth, favor experiments that move the business over small stat-sig wins.

**Institutional memory and surprising experiments** (Ronny Kohavi) — Keep a searchable history; a surprising experiment is one where predicted and actual differ by a large absolute amount; review surprising winners and losers quarterly; reintroduce past winners (opening search results in a new tab won at MSN and Airbnb).

**Pattern libraries** (Ronny Kohavi) — goodui.org (about 140 patterns with win rates) and the Rules of Thumb paper give ideas with known hit rates; may not generalize.

**Weekly impact and learnings review** (Ben Williams) — Weekly meeting on documented learnings and implications, not activity; monthly group-level version. Healthy signals: enthusiastic sharing, data-backed hypotheses from everyone, many people owning experiments end to end. Learnings are the means; impact follows.

**Explore and exploit at the insight level** (Albert Cheng) — Explore to find the right mountain; exploit by swarming teams on variants; a rising share of non-significant results signals over-exploitation and a return to divergent brainstorming. Use an experiment explorer tool at roughly 250+ experiments a year.

**Building an experimentation culture** (Mayur Kamat) — Install the right culture, incentives and tools; democratize results to PMs. Reviews on a platform dashboard cover metrics moved, p-value and time to significance. Fails for compliance, legal and slow-feedback decisions.

**Reward impact without metric theater** (Lauryn Isford) — Reward impact through qualitative feedback and deals won so engineers are not biased toward experiments; skipping tests is no excuse for sloppy building.

**Controversial test triage** (Amol Avasare) — Red-line tests (brand, values) are not run; merely distasteful tests need a return proportional to the cringe.

**Ethical and strategic limits** (Eric Ries) — Short-term revenue wins (more emails) can destroy a company if no principle is defended; data alone cannot decide.

## I. Platform, marketplace and paid

**Platform marginal cost to zero** (Ronny Kohavi) — Self-service setup, templated metric sets, automated analysis, and the crawl/walk/run/fly maturity model across six axes. Build vs buy is rarely binary; beginners should prefer a trustworthy vendor (Albert Cheng agrees: do not build in-house from day one). Ben Williams: do not introduce multivariate or sequential testing to beginners.

**Marketplace caveat** (Anuj Rathi) — Network effects connect buckets, and liquidity decisions may require pulling one lever toward one side, so user-level A/B tests may not work.

**Geo staging and country baskets** (Naomi Ionita; Robby Stein) — Test in smaller geos (Canada, Australia) before the US; track year-two behavior for discounts to see churn effects; keep the experience consistent across surfaces.

**Incrementality testing** (Timothy Davis; Yuriy Timen) — Attribution cannot tell whether converters would have converted anyway. Run geo experiments or conversion-lift tests and compute an incrementality-adjusted factor per platform; accept the short-term cost of pausing a channel. Not worth the effort below roughly $50K/month.

**Signs of life test and budget-sized test** (Timothy Davis) — Test a new platform with a small spend, find a sign of life, build the right creative and message, then scale. Test duration is usually set by budget; extrapolate CTR and conversion to ask for more.

**Right-size the channel test, fishing, momentum metrics** (Adam Grenier) — Half a person on a small team; one quarter maximum, directional signal within a month; define momentum metrics (room attendance growth) up front for channels without click tracking.

**Single-variable ad creative test and champion-challenger** (Jonathan Becker) — Two near-identical creatives in one ad set, compare on a leveling metric such as click-through rate, take the winner as new base and challenge it repeatedly.

**AEO control-group experiment** (Ethan Smith) — LLM answers vary run to run, so use about 200 questions (100 control, 100 test), track a couple of weeks, intervene in buckets, compare, and reproduce before trusting.

**Randomized trial of an AI tool** (Chip Huyen) — A company bucketed engineers into performance tiers and gave half of each bucket Cursor; results vary across companies.

## J. AI-specific

**Error analysis before A/B** (Shreya Shankar; Hamel Husain) — A/B tests are a form of eval, but running them on hypothesized problems wastes effort; derive hypotheses from observed failure modes.

**Test across models** (Grant Lee) — Split the workflow into steps, test models per step, align value with serving cost, retest as the leaderboard changes.

**Do not YOLO tests** (Nicole Forsgren) — Use AI to plan data, instrumentation and analysis, then validate with data science before running.

**Agent readiness gate** (Jeanne DeWitt Grosser) — Hold an agent to the same KPIs as humans (lead-to-opportunity conversion flat) before pulling people off.

**CASH growth loop with Claude** (Amol Avasare, originator) — Four evaluable stages (identify opportunities, build, test quality and brand bar, analyze); eval and hill-climb each; start with copy and small UI tweaks with a human approving. Fails for work needing cross-functional alignment.

**Growth experiment loop** (Anish Acharya) — Generate every variant, measure all, converge on the stat-sig winner, keep a long-term holdout, start the next one; bring a human in at a plateau.

**Experiment velocity shifts the bottleneck to analysis** (Sean Ellis) — AI can generate ideas, model outcome probabilities and reduce ego battles across teams.

**Thoughtfulness over volume** (Noam Segal) — Building a thousand cheap prototypes leads to burnout; as building gets cheaper, be more thoughtful about what to build.
