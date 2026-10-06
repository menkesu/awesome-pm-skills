---
name: metrics
description: Builds your north star metric, a metric tree with owned input metrics and guardrails, and a review cadence, as a one-page metrics spec you can paste into a doc. Use it when you ask 'what should our north star be', 'which metric should this team goal on', 'our dashboard is a mess', 'how do we measure AI productivity', 'activation metric', 'OKR metrics', 'vanity metrics', or 'metrics review cadence'. Draws on 254 insights from 118 Lenny's Podcast guests incl. Sarah Tavel, Crystal Widjaja and Jessica Lachs.
---

# Metrics: North Star, Metric Tree, Review Cadence

![metrics: lead guest team](assets/card.png)

Turn a fuzzy 'what should we measure' into one north star, a tree of inputs each team can actually move, guardrails against gaming, and a ritual that changes decisions. Built from 254 insights from 118 Lenny's Podcast guests. **Lead team:** Sarah Tavel, Crystal Widjaja, Jessica Lachs.

## When to use
- You need a north star or a team goal and the candidates are sign-ups, MAU, GMV, revenue, or 'engagement'.
- A team's goal metric moves too slowly (retention, LTV) to iterate against.
- The dashboard has 40 charts and nobody can say which one changes a decision.
- Teams own funnel stages, or many teams compete for the same engineers, and you need one currency to compare projects.
- You are measuring something new: an AI feature, AI-assisted engineering, a community, a zero-to-one bet.
- Numbers disagree across tools, or 'active' means three things.
- You want to grade an existing OKR sheet, metrics doc, event spec, or board deck. If a file is attached, read it first and work on it.

## Step 1 - Diagnose (ask before answering)
Read any attached artifact (OKRs, dashboard export, event spec, PRD, survey CSV) first. Then ask only what you cannot infer, max 4:
1. **What kind of business is this?** Consumer social or habit, marketplace, B2B multiplayer or PLG, sales-led B2B, AI assistant or agent, internal tool. *Routes the north star play: core action vs happy transactions vs team activation vs pipeline dollars.*
2. **What stage and how many teams?** Zero-to-one, post-PMF, or scaled with many teams. *Early stage uses qualitative signal and one core action; scale needs a tree and a translation layer.*
3. **What decision must this metric drive next?** A team goal, a roadmap tradeoff, a board update, or a go/no-go. *Measurement exists to reduce uncertainty for the next decision (John Cutler), so the decision picks the metric.*
4. **What does the customer get when the product works, and what data do you already trust?** *Value units become the north star; untrusted data sends you to the instrumentation audit first.*

## Step 2 - Pick the play
| If... (situation) | Use | From | Why |
|---|---|---|---|
| Consumer product, unsure what to optimize | **Core action by reach x return propensity**, then top-down sanity check | Sarah Tavel (Hierarchy of Engagement) | Replaces sign-ups and MAU with the action that proves a user understood the product and will return |
| Marketplace | **Happy GMV** + **liquidity / market-health proxy** + a quality guardrail | Sarah Tavel; Benjamin Lauzier; Nickey Skarstad | GMV is vanity; track transactions that make a side happy enough to retain |
| B2B multiplayer or seat-based product | **Team or workspace activation** tied to retention or upgrade | Lauryn Isford; Noah Weiss; Naomi Gleit | The unit that adopts is the team, not the user |
| Post-PMF, need a north star everyone accepts | **Value-exchange loop** + the north-star checklist (units of value, not a ratio, not revenue) | Itamar Gilad; Sean Ellis | Separates value created (north star) from value captured (revenue KPI) |
| Many teams, competing projects | **Metric tree + translation layer to one currency** | Itamar Gilad; Sri Batchu; Jessica Lachs | Lets you compare a landing-page test with a logistics fix in one unit |
| Outcome is slow (retention, LTV) | **Goal on short-term proxy inputs, validated by experiment** | Jessica Lachs; Jackson Shuttleworth (CURR); Bill Carr | You cannot iterate weekly on a quarterly outcome |
| Metric is easy to game | **Counter-metrics / OEC pairing** | Ronny Kohavi; Paige Costello; Shweta Shrivastava | Revenue paired with trust or experience; safety paired with progress |
| AI feature or AI-assisted work | **Intent bucketing, end-to-end velocity, SPACE** and never token or LOC counts | Julie Zhuo; Nicole Forsgren; Mike Krieger; Fiona Fung | Clicks no longer show intent; output proxies are gameable |
| Data is untrusted or metrics disagree | **Instrumentation audit + data dictionary**, event properties not just events | Hila Qu; Crystal Widjaja; Vijay Iyengar | Garbage in, garbage out: fix data before choosing tools |
| Zero-to-one with a handful of users | **Qualitative signal first**, one or two jobs nailed | Aparna Chennapragada; Tanguy Crusson | Formal CTR or MAU on tiny samples is false precision |

## Step 3 - Run it

### Play A: Find the north star (consumer, marketplace, B2B)
1. **List every candidate action** you can measure today (like, follow, click-through, time on site, create, invite, transact). Tavel's Pinterest team did exactly this.
2. **Bottoms-up:** for each action compute (a) % of users who complete it, (b) probability a user who did it this week returns next week. Rank. Pinning users returned more than 90% of the time, which made weekly active pinners the north star.
3. **Top-down:** ask what the product is for. If a user never does this action, have they understood it? Does it help *both* sides of the network? (YouTube's core action ended up subscribing, not watching.)
4. **Apply the checklist** (Sean Ellis): counts units of value delivered, not a ratio, can go up and to the right forever, correlates with revenue without being revenue. Start from the must-have value in the PMF survey. Time-box the team conversation to about 30 minutes.
5. **Add a time window** to capture frequency (weekly rides, monthly purchases, weekly tickets). Amazon purchases and Uber rides are units of value; a $1,000 and a $10 purchase each deliver 'I needed something'.
6. **Commit and pin it:** exactly one metric, stable for at least six months (Isford), then re-derive when you outgrow it. The exact threshold matters less than shared clarity (Gleit: 7 vs 10 matters little; Adriel Frederick on Facebook's 10 friends in 14 days: nothing magic about the number, a discrete goal with a deadline made the org chase it).
7. **Done when:** every roadmap item can state how it moves the metric, and a new teammate can recite the definition (who counts, what action, what window).

### Play B: Metric tree and input metrics
1. Draw two trees (Gilad): the north star (value created) and the top business KPI (value captured, e.g. revenue or profit). Look for middle metrics that appear in both.
2. **Map the customer journey** and instrument speed, quality and ease at each step (Bill Carr). An input is a metric about the customer experience that a team can control (selection, price, speed). Measure each input two ways and refine.
3. **Give each team a local metric it directly influences**, then have data/finance build conversion factors into the north star (Batchu at Instacart: monthly active orders; at Ramp: dollars of SQL pipeline). Refresh the factors every six months. Do not use the translation to settle gaps under about 5 to 10 percent: use judgment.
4. For multi-sided businesses, quantify levers in a **common currency** (Lachs: if price drops $1, what volume? if delivery time drops one minute?) and keep an inventory of options with expected return and timeframe.
5. **Prefer 2 to 3 simple metrics over one composite.** DoorDash's merchant health score of 0.35 meant nothing; first-order-within-7-days plus photo coverage and accurate hours covered about 95% of the value. Never build a weighted index (Carr, Lachs).
6. **Volume plus efficiency:** pick one of each (Batchu). Funnel owners get absolute counts through their stage, not their local rate, because rate owners are tempted to make the previous step harder (Archie Abrams).

### Play C: Guardrails and fail states
1. For the north star ask: *how would a team raise this by hurting users?* Add a counter-metric for each answer (Kohavi: retention, time to a successful click, percent of successful sessions).
2. Price the harm: Kohavi's team modeled the lifetime cost of an unsubscribe and over half of email campaigns went net negative.
3. Pair every safety or risk metric with a progress metric; Waymo pairs safety with undue slowing and strands because a system is perfectly safe if it never moves.
4. Add **fail-state goals** (Lachs: orders never delivered; Jeff Weinstein: a stacked 'users having a bad day' chart, one log line per bad-day reason). Averages hide these, and they drive churn.
5. Check the OEC passes the directional test: if half the room thinks an increase is good and half bad, redefine it (Kohavi).

### Play D: Instrumentation sanity (before you trust any chart)
1. **Audit:** list key actions in the product, then check each is tracked correctly; publish a data dictionary of event names and properties (Hila Qu).
2. **Count properties per event** (Widjaja): many events with one or zero properties is the symptom of bad tracking. Add context such as location, surge, voucher, how many drivers were on screen.
3. **Start small:** about 20 events, not a months-long documentation project (John Cutler); track from servers by default since client SDKs drop 20 to 30 percent of web events (Vijay Iyengar); define 'active' once, instrument it, codify it (Manik Gupta).
4. **Fix data holes:** ask what data you are missing, e.g. users who cannot log in are not in your denominator (Lachs). Never let null mean something (Ayo Omojola).
5. For attribution, start with first or last touch but capture every input from day one; no single source of truth, triangulate with MMM and surveys only above roughly $100K/month and three-plus channels (Austin Hay, Jonathan Becker, Yuriy Timen).

### Play E: AI metrics
1. **AI assistant or agent:** bucket conversations by intent with an LLM and track which use cases grow or shrink (Julie Zhuo). Measure whether people got work done, not time spent (Mike Krieger).
2. **AI-assisted engineering:** measure idea-to-customer or idea-to-experiment time, and disclose that AI and DevEx work both contributed (Nicole Forsgren). Use SPACE with at least three dimensions and add trust. Treat lines of code, PR counts and token spend as motion, not progress (Fiona Fung, Max Schoening, Molly Graham, Forsgren).
3. **Time to value** instead of time saved (Inbal Shani); for a delegation product the bar is task completion you can walk away from, not 90 percent (Roman Ugarte).
4. **Autonomous systems:** benchmark against human performance and pair with a progress counter-metric (Shweta Shrivastava).

### Play F: Review cadence (metrics that change decisions)
1. **Weekly business review** (Ian McAllister): each owner presents variances and trends and answers probing questions; cascade the same routine down. Run it tight.
2. **Daily numbers** posted by a bot into a team channel (Daniel Lereya); at Monday.com this exposed that AI features reached only a few thousand of 250,000 accounts and led to opening them to 98 percent of customers within two weeks.
3. **One shared metrics page**, live in meetings, simple feeling-laden names (Weinstein: companies with zero support tickets). If it is not there, nobody looks at it.
4. **Segment every drop** before reacting: region, device, demographic, use case (Robby Stein), and look at the distribution, not the average (Lachs: a referral channel was bimodal, real users plus fraud).
5. **Close the loop on every shipped project:** what was the metric, what was the target, what moved (Varun Parmar). Drop any metric that never changes what you do (Widjaja).

## Where the experts disagree
- **One north star vs no universal north star.** Camp A (Lauryn Isford, Sean Ellis, Sarah Tavel, Tim Holley) wants one singular metric for rallying and cross-team clarity. Camp B (Merci Grace, Karri Saarinen) warns no single metric fits every business and rejects per-feature numbers. *Use A when teams are fragmenting and you need a rallying point; B when your product is many parts used differently, then goal on inputs and 'customers agree the problem is solved'.* Default: one north star, 2 to 3 inputs, no per-feature targets.
- **Composite or paired metrics vs strictly simple ones.** Camp A (Jessica Lachs, Bill Carr) kills weighted indexes: if people cannot discuss it across the company it is a bad metric. Camp B (Ronny Kohavi, Lauryn Isford's activation family) uses a deliberately constructed evaluation criterion or metric family. *Use A for team goals and exec reporting; B only for experiments, and as a constraint or a set of paired metrics, never a coefficient soup.* Default: separate metrics with explicit guardrails.
- **Goal on retention vs goal on its inputs.** Lachs says retention is a terrible thing to goal on because it barely moves short term; Jackson Shuttleworth points Duolingo teams at CURR, next-day return of existing users, as the retention lever with the most DAU leverage. *Use CURR-style short-horizon retention if a daily-use product gives fast feedback; otherwise proxy inputs validated by experiment.* Default: a short-horizon proxy, re-validated against the long-term outcome each half.
- **Metric-led vs judgment-led.** Camp A (Carr, Batchu, McAllister) runs the company through inputs and weekly reviews. Camp B (Josh Miller, Bob Baxley, Maggie Crowley, Shaun Clowes, Tobi Lutke, Mike Krieger) says metrics are a compass, a consequence, or a cockpit instrument, never the driver. *Use A when you have volume and cheap experiments; B in zero-to-one, craft-heavy or AI-assistant products.* Default: instrument everything, decide with judgment, talk to users for the why.
- **Revenue-adjacent vs value-unit north star.** Sean Ellis, Itamar Gilad and Tavel: count units of customer value, not revenue. Sri Batchu and Tim Holley run on pipeline dollars or GMS. *Use value units for consumer, marketplace and PLG; pipeline dollars for sales-led B2B where the buyer is not the user.* Default: value unit as north star, revenue as the paired KPI.

## Deliverable
Fill this in and paste it into your doc:

```markdown
# Metrics One-Pager: <product / team>   (owner, date, review date +6 months)

## North star
- Metric: <count of units of value, with time window>   e.g. weekly active X
- Definition: who counts, which action, what window, which event names
- Why this one: <reach x return propensity evidence; what a user who never does it has missed>
- Replaces (vanity metrics we stop reporting): <...>

## Counter-metrics / guardrails
| Guardrail | Protects against | Threshold |
|---|---|---|

## Metric tree (inputs teams can move)
| Input metric | Owning team | Lever | Translation to north star | Target | Review |
|---|---|---|---|---|---|

## Fail-state metrics
- <rare disaster outcome> -> goal, owning cross-functional team

## Instrumentation gaps
- Events missing / properties missing / definitions to codify / data holes

## Cadence
- Daily numbers: <channel, bot>   Weekly review: <owner, 60 min, variances + trends>
- Per shipped project: metric, target, actual
- North star re-derived on: <date>

## Metrics we stop watching (and why)

## Next 3 actions
1. <this week>   2. <this month>   3. <by next review>
```

## Grade existing work
Score each criterion 1 to 5 (5 = best). Output a score per criterion, the total out of 40, and the top 3 fixes with the guest behind each.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Value-based north star | Revenue, MAU, sign-ups, or downloads | Engagement count, loosely tied to value | Count of value units with a time window, validated against retention (Tavel, Ellis, Gilad) |
| One and stable | Many co-equal metrics, changes quarterly | One metric, informal | One metric, stable 6+ months, review date set (Isford) |
| Inputs and ownership | Teams own outputs they cannot move | Some input metrics, unclear owners | Tree with owned inputs and a translation to the north star (Carr, Batchu, Gilad) |
| Simplicity | Weighted composite or fitness function | Mixed | 2 to 3 metrics anyone can explain (Lachs, Carr) |
| Guardrails | None | Guardrail named, no threshold | Counter-metric per gaming risk plus fail-state goals (Kohavi, Lachs, Costello) |
| Data trust | Many events with no properties, conflicting definitions | Dictionary exists, gaps known | Audited spec, server-side core events, one codified definition of active (Qu, Widjaja, Gupta) |
| Insight, not observation | Dashboards as entertainment | Segments reviewed ad hoc | Every metric tied to a decision; drops segmented; distributions over averages (Widjaja, Stein, Lachs) |
| Cadence and loop-closing | No ritual | Monthly review | Daily numbers, weekly review, post-ship target vs actual (McAllister, Lereya, Parmar) |

## Red flags
- **Vanity metrics as the goal:** sign-ups, MAU, GMV, impressions, rankings (Tavel, Eli Schwartz, Krithika Shankarraman).
- **Composite scores with coefficients** that nobody can explain (Lachs, Carr).
- **Goaling on a quarterly outcome** you cannot move this sprint (Lachs).
- **Local conversion-rate ownership,** which rewards making the prior step harder (Archie Abrams).
- **Metrics as entertainment:** reviewed, never acted on (Widjaja).
- **Averages only:** a 3 percent adoption number can be 100 percent of someone's business (Tom Verrilli); a bimodal channel looks mediocre (Lachs).
- **Single aggregate metric overriding the customer:** Twitter's feed toggle quietly reverting to ranked, Groupon's email frequency creep (Kayvon Beykpour, Eric Ries).
- **Counting motion:** tokens, lines of code, PRs, or feature usage as success (Fiona Fung, Max Schoening, Paige Costello: using the feature is teaching to the test).
- **Copying benchmarks** with different definitions of visitor, signup, activation (Elena Verna).
- **Chasing adoption before basics:** no quality bar but an adoption dashboard (Matt MacInnis).

## Receipts
- "When a user completes this action, it's clear that they both understand the utility of the product, they understand what that product is all about, and it's an action that, if they perform the action, they're very likely to come back." — Sarah Tavel, Lenny's Podcast (00:05:45)
- "Retention is a terrible thing to goal on because it's almost impossible to drive in a meaningful way in the short term, and yet you want to be able to experiment and iterate quickly." — Jessica Lachs, Lenny's Podcast (00:44:45)
- "real news is information that changes what you do in the real world." — Crystal Widjaja, Lenny's Podcast (00:41:17)
- "So we took it as an article of faith that if we can just improve these inputs, the outputs will take care of themselves." — Bill Carr, Lenny's Podcast (01:00:03)
- "the North Star metric measures how much value we create for the market." — Itamar Gilad, Lenny's Podcast (00:27:02)
- "But I just think the overlap of most valuable things you can do with a product, and for things that happen to be fully quantifiable, it's like maybe 20% which leaves 80% of a value space unaddressable" — Tobi Lütke, Lenny's Podcast (00:18:39)

## Go deeper
- `references/frameworks.md` - every framework in this skill, how to run it
- `references/quotes.md` - verified quotes with timestamps
- Related skills:
  - `pmf-check` - when the must-have value that feeds your north star is not yet established
  - `growth-model` - to turn the metric tree into loops, activation and retention diagnosis
  - `experiment` - to validate that a proxy input really moves the output, and to run guardrails properly
  - `prioritize` - to turn the tree into a confidence-scored roadmap and OKRs
  - `eval-plan` - for the quality side of AI features once the business metric is set
