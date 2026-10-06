---
name: ship-faster
description: Diagnoses why your product team ships slowly and produces a velocity plan with a baseline, a bottleneck map, the top 3 interventions and a stop-doing list. Use it when you say 'we're too slow', 'how do we ship faster', 'projects keep slipping', 'too many meetings', 'approvals take forever', 'our releases are scary', 'velocity', 'cycle time', 'we hired more people and nothing got faster' or 'AI made coding fast but we still ship slowly'. Draws on 226 Lenny's Podcast guests including Farhan Thawar, Nicole Forsgren and Melissa Perri.
---

# Ship Faster

![ship-faster: lead guest team](assets/card.png)

Find the one bottleneck that actually slows your team, then fix it with the smallest intervention that moves a measured number. Built from 760 insights from 226 Lenny's Podcast guests. **Lead team:** Farhan Thawar (Shopify engineering), Nicole Forsgren (DORA, SPACE, Frictionless), Melissa Perri (Escaping the Build Trap).

## When to use
- Projects slip, estimates are wrong, or work expands to fill whatever time you give it
- Decisions wait on meetings, approval chains, escalations or one busy leader
- Releases are rare, big and scary; builds are flaky; deploys need babysitting
- Headcount grew but output did not (or 'we need more engineers' is the default answer)
- Too many priorities in flight, nobody can say what the top one is
- The org grew past the founder and roadmaps, rituals and ownership are inconsistent
- AI coding tools made writing code fast but features still take months to reach users

## Step 1 — Diagnose (ask before answering)
If the user attached anything (roadmap, project list, calendar export, DORA or release data, retro notes, org chart), read it first and infer what you can. Then ask at most these four:
1. **What does slow look like, with one example?** Take a recent change that should have taken 1-2 weeks and ask for the dates: idea, decided, defined, in production. *Why:* the stage with the longest wait picks the play (Nikita Miller's velocity heuristic, Ravi Mehta's latency test).
2. **How big and how mature is the org?** Engineers, PMs, number of teams, founder-led or not. *Why:* under ~10 engineers the cure is focus and time-boxes; past ~50 engineers or 100-150 people it is ownership, platform and operating model.
3. **How often do you release, and what breaks when you do?** Deploy frequency, lead time from commit to production, incident or rollback rate. *Why:* routes to the DORA and developer-experience play versus the decision-latency play.
4. **Are AI coding tools in use, and where does the extra code pile up?** Review, QA, legal, launch? *Why:* routes to the AI-era bottleneck play.

State your diagnosis in one sentence before you recommend anything: *the slowest stage is X, because Y, evidenced by Z.* If you cannot, you are guessing, so go get the dates.

## Step 2 — Pick the play
| If… (situation) | Use | From | Why |
|---|---|---|---|
| Decisions sit in meetings, approvals, escalations | **Decision-latency cut** (DRI, one blocking approver, five-day escalation, personal SLA, three closing questions) | Brian Halligan, Paige Costello, Hari Srinivasan, Claire Vo, Alisa Cohn | Pace is set by decisiveness, not hours worked |
| Releases rare or scary, builds flaky, long approval windows | **DORA baseline + DevEx friction audit** | Nicole Forsgren, David Singleton | Speed and stability move together; small frequent changes beat batching |
| Projects slip, scope blobs, 'one more sprint' | **Appetite + shaping + hill chart + 10% working version** | Ryan Singer, Jason Fried, Nan Yu | Fixes the input to the factory instead of pressuring the team |
| Too many projects, hiring did not help | **Cut the load: barrels, single-threaded owners, deliberate understaffing** | Brian Chesky, Keith Rabois, Bill Carr, Matt MacInnis | Throughput is capped by empowered owners, not bodies |
| Scaled org: inconsistent roadmaps, PMs doing admin, output over outcomes | **Product operating model + product ops (start with one person)** | Melissa Perri, Denise Tilles, Marty Cagan | Process is not the enemy at scale; missing structure is |
| Teams collide, ownership is blurry, org chart shows up in the product | **Conway restructure + single-threaded program owners** | Dhanji R. Prasanna, Bill Carr, Brian Halligan | You ship your org structure |
| Rewrite, quality or tech-debt temptation is stalling shipping | **Choose two, no side-by-side rewrite, delete code** | Dylan Field, Camille Fournier, Maggie Crowley, Farhan Thawar | Protects the quality bar without freezing change |
| AI sped up coding but not output | **Find the slowest part of the system; automate the path to production** | Brian Balfour, Dan Shipper, Sherwin Wu, Cat Wu | Adding capacity in one stage moves the bottleneck |

If two rows match, run the earlier row first. Decision latency is usually the cheapest to fix and the fastest to show.

## Step 3 — Run it
### Play 0 — Baseline (always, within one week)
1. **Latency test.** Pick a trivial change (button text). Time it from 'we think this is worth making' to 'we have results' (Ravi Mehta). Then pick 3 items that should have taken 1-2 weeks and record actual dates to production; if one resurfaces two quarters later, you have a velocity problem (Nikita Miller).
2. **PM decision velocity.** Time from 'we need to do X' to defined to decided (Nikita Miller).
3. **DORA four.** Lead time (commit to production), deployment frequency, mean time to restore, change fail rate. Compare to the dora.dev tiers (Nicole Forsgren).
4. **Meeting load.** Hours per week ICs spend in meetings. Shopify's ICs fell to about 3 (from 5-6) and managers to 6-7 after a reset (Farhan Thawar).
5. **WIP.** Count active projects against engineers. If you cannot name the top priority, stop here and run Play D.
6. **Ask the people.** Ask a handful of developers about their tools, process and biggest barriers (Nicole Forsgren); engineers know whether the team is effective and why not (Will Larson).
Deliverable: a stage-by-stage wait-time map (idea → decided → defined → built → reviewed → released → learned) with a number on each arrow.

### Play A — Decision-latency cut
1. List the last 10 decisions that took over a week. For each: who blocked, who was informed, what was the real deadline.
2. **One DRI per cross-functional initiative**, with power to direct people outside their org; once they decide, it is disagree and commit with no escalation path (Brian Halligan, Casey Winters).
3. **Cap reviews:** one blocking approver, at most three reviewers, and the host removes attendees above ten and writes decision notes instead (Paige Costello).
4. **Five-day rule:** anything unresolved after five days moves to the next level up (Hari Srinivasan).
5. **Personal SLA:** publish your own turnaround on approvals; when someone defers to the next meeting, ask *when can we actually decide, and how much information do we need?* (Claire Vo).
6. **Close every meeting** with Alisa Cohn's three questions: what did we decide, who does what by when, who else needs to know.
7. **Move status out of meetings** into a feed or async update; reserve meetings for solving problems (Farhan Thawar, Megan Cook).
8. **Once a year, run Meetingageddon:** admins delete recurring internal meetings with 3+ people (not 1:1s, interviews or external), ban new recurring ones for two weeks, re-add only what is needed (Farhan Thawar).
9. **Pull dates in:** tell leaders every deadline moves one time-horizon step faster (year to half, half to quarter, month to week) (Claire Vo).
10. Low-stakes decision? Decide by gut or delegate (Brandon Chu). Two-way door? State an opinion and let people react (Mihika Kapoor).
Done when: median decision latency from Play 0 drops by half and IC meeting hours fall.

### Play B — DORA baseline + DevEx friction audit
1. Take the dora.dev quick check; pick the 1-2 weakest capabilities (automated testing, CI/CD, trunk-based development, loosely coupled architecture), not a toolchain to buy (Nicole Forsgren).
2. Run a listening tour; look for the smells: builds breaking, flaky tests, slow environment provisioning, hard to switch projects, people refusing internal moves (Nicole Forsgren).
3. Pick a quick win that developers feel directly (a paper cut). Staff a small pilot: a couple of engineers plus a PM or TPM for comms. Share results (Nicole Forsgren).
4. Remove batching: kill mandatory multi-week change-approval windows; invest in automated tests and CI/CD so speed does not cost stability.
5. Targets to aim at, not copy blindly: Stripe runs tests in about 15 minutes in parallel with review, reruns after merge, then about 30 minutes to auto-deploy, so user feedback can be answered the same day (David Singleton). Good product teams release about 20 times a day (Marty Cagan).
6. Add a one-click paper-cuts button to every internal tool and a monthly rotating survey sample (David Singleton). When metrics show a systemic problem, call a code yellow with a champion who can pull in help (Farhan Thawar).
7. To win exec support, quantify time for feature delivery, time to first PR, time to steady-state productivity, and code review time versus peers (Nicole Forsgren). Warn them of the J-curve: quick wins, then a dip while telemetry is built, then compounding.
8. Delete before optimizing: dropping obsolete tests saved more than test selection; run a maintenance-cost audit and remove features that cost more than they earn (Dhanji R. Prasanna, Jay Baxter).
Done when: lead time and deploy frequency improve while change fail rate does not rise.

### Play C — Appetite, shaping and time-boxes
1. For every big project, replace the estimate with an **appetite**: the maximum time the business will spend. Six weeks is a ceiling, not a target; 1-3 weeks is fine (Ryan Singer, Jason Fried).
2. **Shape first.** Hand builders one whole shaped idea, not 100 tickets. Symptoms of missing shaping: a blob request like 'calendar', engineers pushing back after the Figma, mid-build questions with no sense of getting warmer (Ryan Singer).
3. **Nine-box kickoff:** builders sketch nine chunks of implementation; more than about ten parts means you are back in ticket land (Ryan Singer).
4. **Working version at 10% of the budget** that tests the key hypothesis; use it internally (Nan Yu).
5. **Track on a hill chart.** At the time limit, work still uphill (still figuring it out) gets killed (Jason Fried) or, in Singer's softer circuit breaker, pulled back into shaping before any reinvestment.
6. Cut scope, never quality: remove elements until the core is the one-week project (Gaurav Misra). Ship the simplest V1 and add one tested layer at a time (Jackson Shuttleworth).
7. Keep deadlines rare and treat each one as a P0 that engineers cannot be pulled from (Nan Yu). For external stakeholders, commit dates only for the phase in front of you (Annie Pearl).
Done when: slipped projects fall, and nothing ships as 'milestone one of a half-baked thing' (Vijay Iyengar).

### Play D — Cut the load
1. Put every project anyone is working on in one sheet (Brian Chesky). Count projects per engineer.
2. Cut hard. Airbnb cut about 80% of projects; Shopify went from about 40 priorities in a quarter to three in the COVID crisis (Brian Chesky, Brandon Chu).
3. Ask each owner for their top priority, then check that engineers and top talent are actually staffed on it (Tomer Cohen).
4. **Single-thread:** one goal per team per morning, other asks absorbed by rotating production engineers (Geoff Charles); one leader owns a persistent program with dedicated resources, which needs service-based architecture first (Bill Carr).
5. **Count your barrels** (people who take an initiative from start to success). Add barrels before ammunition (Keith Rabois).
6. **Deliberately understaff** each project; overstaffing breeds politics (Matt MacInnis). Hire only when a capacity calculator shows red for multiple quarters and cutting meetings does not fix it (Timothy Davis).
7. Keep known valuable work in supply, or people invent work-like activity (Stewart Butterfield).
Done when: every team can name one top priority and its owner, and in-flight projects fit capacity.

### Play E — Scaling org: product operating model
1. Sample 5+ teams: what are you working on, and what is the most important thing you could do? Try to ladder answers into one strategy; if you cannot, strategy is missing at the top (Melissa Perri).
2. Audit the four parts of the product operating model: strategy tied to company goals, org design (PM coverage and skill), product operations, culture and incentives that reward value over output (Melissa Perri).
3. Standardize interfaces (roadmap format, time horizons, cadences with sales) and leave team-internal rituals like stand-ups alone (Melissa Perri).
4. **Product ops starts with one person** on the highest-leverage pillar: business data and insights for high-growth companies, process and governance for enterprises in transformation. PMs keep decisions; a ratio of one to one is wrong (Melissa Perri, Denise Tilles).
5. If org problems are blamed on training, look first at how goals are set and strategy is deployed (Melissa Perri). If you run Scrum, ask of each ritual whether it serves shipping and learning; drop what does not.
6. Add a rhythm: weekly project update with a demo, a six-week review of every project with leadership, nothing ships without the group lead's approval (Farhan Thawar, Archie Abrams).
7. Check Conway's law: if a silo blocks shared work, change the structure before expecting a new technical strategy to take hold (Dhanji R. Prasanna).
Done when: roadmaps roll up, leaders can see what is happening without asking, and PM time on admin falls.

### Play F — AI-era bottleneck
1. Map the whole system (design, PM, engineering, review, QA, IT, legal, procurement) and attack the slowest part; speeding up only coding moves the bottleneck (Brian Balfour, Dan Shipper).
2. Automate the path to production: agent patches lint errors, restarts CI, handles deploy toil; track PRs merged per engineer (Sherwin Wu).
3. Build a corner of the product where an idea can reach users by end of week and de-emphasize multi-quarter cross-team roadmap alignment there (Cat Wu).
4. Port, do not reinvent, when a reference implementation exists: Sora Android went from zero to employee launch in 18 days (Alexander Embiricos).
5. Guard against fast demos masquerading as deployment: widen beta circles, label unused work alpha, use a research preview label and keep shipping (Aparna Chennapragada, Simon Willison, Nan Yu, Jenny Wen).
6. Benchmark yourself: how would an AI-native company execute this, and are we as fast? (Howie Liu)
Done when: idea-to-user time from Play 0 shrinks, not just PR count.

## Where the experts disagree
- **Go fast vs slow down to go fast.** **Camp A** (Varun Parmar, Nan Yu, Cat Wu, Laura Modi, Farhan Thawar): speed beats everything in unproven markets; be first to hit the brick wall; manufacture deadlines. **Camp B** (Bangaly Kaba, Karri Saarinen, Bill Carr, John Zeratsky, Peter Deng): planned understanding, thinking and systems raise win rate and velocity a year later. → *Use A when decisions are two-way doors, iteration is cheap and the market is unproven; B after product-market fit, when building in the wrong direction compounds, or when shipping is irreversible.* **Default:** spend a day to a week on what to build, then go fast on how.
- **Estimates vs appetite.** **Camp A** (Ryan Singer, Jason Fried, Vijay Iyengar, Nan Yu): the time box is the input, scope flexes, no estimating. **Camp B** (Annie Pearl, Varun Parmar): commit dates only to the phase in front of you, and benchmark stage cycle times (P0 problem, P1 solution, P2 post-ship check). → *Use A inside a team that has shaped work and a protected builder pair; B when sales and marketing need dates.* **Default:** appetite for the build, phase-level dates for the outside world.
- **Process: enemy or enabler.** **Camp A** (Eeke de Milliano, Jeremy Henrickson, Matt MacInnis, Keith Coleman): process lowers variance but drags your best people to the average; keep it minimal. **Camp B** (Melissa Perri, Krithika Shankarraman, Claire Hughes Johnson, Naomi Gleit): scale needs a roadmapping tool, 20% and 80% reviews, a canonical doc. → *Use A for 0-to-1 and under ~10 engineers; B once people far from context need to see the work.* **Default:** standardize interfaces, never team-internal rituals.
- **Small teams and fewer PMs vs more structure.** **Camp A** (Tom Verrilli, Kevin Weil, Marty Cagan, Matt Mochary, Adam Mosseri): every added head adds coordination cost; default to no PM or PM-light. **Camp B** (Robby Stein, Andrew Ambrosino, Molly Graham, Elizabeth Stone): breakthrough products need real teams; specialties still matter. → *Use A with high-context engineers and designers; B when the customer base or scope outgrows them.* **Default:** add barrels, not ammunition, and let a red capacity calculator justify any hire.

## Deliverable
Produce this and paste-ready:
```markdown
# Velocity Plan: <team> — <date>
**Diagnosis (one sentence):** The slowest stage is ___ because ___, evidenced by ___.

## Baseline
| Metric | Today | Target (90 days) | Source |
|---|---|---|---|
| Idea → production on a 1-2 week item | | | dates |
| Decision latency (needed → decided) | | | |
| Lead time / deploy frequency / MTTR / change fail rate | | | |
| IC meeting hours per week | | | calendar |
| Projects in flight per engineer | | | project sheet |

## Bottleneck map
idea →(__d)→ decided →(__d)→ defined →(__d)→ built →(__d)→ reviewed →(__d)→ released →(__d)→ learned

## Top 3 interventions
| # | Play | Change (specific) | Owner | Start | Success metric | Rollback if |
|---|---|---|---|---|---|---|

## Stop list (delete or ban)
- Meetings: ___  - Projects: ___  - Approvals: ___  - Rituals: ___

## Guardrails
Stability metric that must not worsen: ___ . One-way doors that keep a gate: ___ .

## Cadence
Weekly update (demo or video): ___ . Six-week review: ___ . Next baseline re-measure: ___ .

## Next 3 actions
1. (this week) ___  2. (this month) ___  3. (this quarter) ___
```

## Grade existing work
Score a velocity plan, roadmap or process doc 1 / 3 / 5 per criterion.
| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Evidence of bottleneck | Opinions only | Some numbers, no stage map | Dated stage waits, one named slowest stage |
| Speed and stability together | Speed only | Mentions quality | Pairs lead time with change fail rate and MTTR (Forsgren) |
| Decision rights | Committees, shared owners | Owners on some items | One DRI per initiative, capped approvers, escalation clock |
| Time-boxing | Estimates and open-ended dates | Deadlines, no scope flex | Appetite, shaped scope, working version early (Singer, Nan Yu) |
| Focus | Many equal priorities | Top priority named | Top priority staffed; projects cut to capacity (Chesky, Cohen) |
| Feedback loop | Quarterly releases | Weekly releases | Idea to user in days; same-day response to feedback (Singleton) |
| Change plan | Big-bang reorg or tool purchase | Pilot with no success metric | Small quick win, J-curve expectation, re-measure date (Forsgren) |
| Cadence | Ad hoc | Monthly review | Weekly demo update plus six-week review (Thawar) |
Output: score per criterion, total out of 40, and the top 3 fixes, each tied to the guest and framework behind it.

## Red flags
- Buying a DevOps toolchain instead of fixing capabilities (Nicole Forsgren)
- Mandatory two-week change-approval windows that cause batching (Nicole Forsgren)
- Adding headcount without adding barrels (Keith Rabois); hiring ahead of a hypothesis (Meltem Kuran Berkowitz)
- Fake speed: skipping stages or lowering quality instead of changing the approach (Daniel Lereya)
- Speeding up one stage and not the system (Brian Balfour); AI coding with no review capacity (Dan Shipper)
- A fixed six-week deadline slapped onto an unshaped project (Ryan Singer)
- A side-by-side rewrite estimated at six months that took two and a half years (Maggie Crowley, Camille Fournier)
- Pace set by the weekly meeting calendar (Claire Vo); a daisy chain of approvals (Paige Costello)
- Scrum by the book, SAFe as a plug-and-play map, and product owners as order-takers (Melissa Perri)
- Blaming training when goals and strategy deployment are the problem (Melissa Perri)
- Reviews at the 99% mark that only rubber-stamp (Krithika Shankarraman)

## Receipts
> "speed and stability move together." — Nicole Forsgren, Lenny's Podcast (00:15:19)

> "If you just accelerate one part of the system, you're just going to move to the bottleneck to another part and your actual product output, the output of the system doesn't accelerate, either." — Brian Balfour, Lenny's Podcast (01:18:19)

> "pace is sometimes governed not by how hard people work, but how decisive they are. If you want to improve the speed of a company, then make faster decisions." — Brian Chesky, Lenny's Podcast (00:47:22)

> "This is not an estimate of time, it's an appetite, which is a radically different approach." — Jason Fried, Lenny's Podcast (00:34:21)

> "the ratio of barrels to ammunition is what dictates the number of important initiatives that can be pursued simultaneously." — Keith Rabois, Lenny's Podcast (00:17:50)

> "I've met a lot of organizations that think most of their issues are in the training of their people. And 99% of the time, I see that it's actually in the way that they're setting their goals and deploying their strategy." — Melissa Perri, Lenny's Podcast (20:57)

## Go deeper
- `references/frameworks.md` — every framework in this skill, how to run it
- `references/quotes.md` — verified quotes with timestamps
- Related skills:
  - `spec` — when a project needs shaping into a written, graded spec before the build starts
  - `prioritize` — when the answer is cutting the roadmap, not speeding it up
  - `agent-workflow` — when AI agents are the new capacity and you need lanes, plan mode and an autonomy ladder
  - `metrics` — when you need a metric tree and review cadence around cycle time and outcomes
