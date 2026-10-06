# Ship Faster — Frameworks

Every framework below comes from the Lenny's Podcast digest for this skill. Format: **Name** (originator, episode) — what it is for; when it applies or fails; steps; benchmark; who else endorses it.

## 1. Measuring speed

**DORA four key metrics** (Nicole Forsgren, Nicole Forsgren episodes) — Software delivery performance is two speed metrics (lead time for changes, deployment frequency) and two stability metrics (mean time to restore, change fail rate). Applies to any software team; DORA found no statistically significant difference between small and large companies (only retail was better). Steps: measure lead time as code committed to code running in production; measure deployment frequency; measure mean time to restore; measure change fail rate (percentage of changes causing incidents or needing human intervention); compare to low, medium, high and elite tiers and track progress. The dora.dev quick check gives your tier and typical constraints for your industry.

**Speed and stability move together** (Nicole Forsgren) — Smaller changes shipped more often shrink blast radius and speed debugging; large-batch releases create merge-conflict mudballs. Mandatory two-week change-approval windows (ITIL style) were an old wives' tale and cause batching. Steps: push small changes frequently; remove batching causes such as long approval waits; invest in automated testing and CI/CD. Endorsed by David Singleton (Stripe ships constantly with high uptime) and Marty Cagan (quarterly releases mean you cannot learn). Counter-view: Nick Turley keeps rigorous gated process only for frontier model releases.

**DevOps as capabilities, not a toolchain** (Nicole Forsgren) — Speed and stability come from technical, architectural, cultural and lean-management capabilities (automated testing, CI/CD, trunk-based development, loosely coupled architecture, cloud). Steps: take the quick check; identify weak capabilities; pick those to improve; measure with SPACE-style balanced metrics.

**Latency test** (Ravi Mehta, Ravi Mehta episode) — Time how long it takes to go from believing a simple change (button text) is worth making to getting results. Attack the biggest delays in that cycle. Companion: Nikita Miller's heuristic (pick 1-2 week items and check actual time to production; if one resurfaces two quarters later you have a velocity problem; for PMs the issue is usually decision velocity: idea to defined to decided).

**Time to outcomes** (Itamar Gilad) — The right speed metric is time to outcomes, not time to production; get the right bits to production, not just bits. Steps are learning milestones: state the goal metric and current value, pick an idea, plan a sequence of validation steps (mockup usability test, prototype, A/B test) in parallel where possible.

**Stage-gated cycle-time benchmarking** (Varun Parmar, Varun Parmar episode) — Velocity is golf against yourself. Stage-gate work (P-strat idea pitch, P0 problem definition, P1 solution definition, P2 post-ship metric check), size it (small under a month, medium, large), record time per stage, and publish average, median and variance so teams benchmark each other. Fails when work flows through meetings and Slack rather than a system.

**IC meeting hours** (Farhan Thawar) — Track hours individual contributors spend in meetings weekly. After the meeting reset and moving announcements into a feed, Shopify ICs fell to about three hours (from five to six) and managers to six to seven.

**Operating tempo signals** (Keith Rabois; Sri Batchu; Keith Yandell) — Thriving companies fix, ship and measure problems found at one board meeting by the next (Ramp was ready to ship cards in 3 months versus 9-12 for the industry). Ramp tracks days since founding in every board meeting; Yandell argues that pulling the roadmap forward a week compounds enough to lap competitors one week behind.

**Tempo framework** (Patrick Campbell, Patrick Campbell episode) — Tempo, a shared definition of good shipping frequency per org, matters more than org design. Steps: set a mission metric and principles; have each org leader define what good shipping looks like (launches per month and quarter); discuss the gap in one-on-ones and remove blockers; connect cross-team dependencies.

## 2. Developer experience

**DevEx: flow state, cognitive load, feedback loops** (Nicole Forsgren, Nicole Forsgren 2.0) — Three reinforcing pillars. Assess how often developers reach flow, the cognitive load of plumbing and tooling, and shorten feedback loops. Short lead times protect the mental model: failures surfacing within a day still find the developer in context.

**Frictionless seven-step process** (Nicole Forsgren) — Start the journey (listening tour, synthesize, visualize workflow and tools); get a quick win; use data to optimize (data foundation, surveys); decide strategy and priority; sell the strategy (feedback, why now); drive change at your scope (grassroots, top-down or middle); evaluate, show value and loop. New initiatives start at step one.

**Smells your team could move faster** (Nicole Forsgren) — Builds breaking, flaky tests, long processes, slow environment provisioning, high cost of switching tasks or projects, people declining internal moves. Speed gains have diminishing returns, and high cognitive load can make speed gains bad.

**First-week developer check** (Nicole Forsgren) — Is the productivity problem written down? Find any existing signal. If none, ask a handful of developers about tools, process and biggest barriers.

**Quick wins at local vs global scope** (Nicole Forsgren) — Staff a small pilot (a couple of engineers plus a PM, PgM or TPM for comms); fix paper cuts developers feel directly; share wins; with top-down backing pick globally scoped wins.

**J-curve of DevEx gains** (Nicole Forsgren) — Early wins look big, a dip follows when infrastructure and telemetry must be built, then benefits compound. Set expectations with leadership. Also: treat the DevEx program as a product with MVPs, comms and sunsetting of metrics that no longer drive decisions.

**Business case for moving faster** (Nicole Forsgren) — Ask what leaders fear (reliability); show good technical practices keep stability; collect time for feature delivery, time to first PR, time to steady-state productivity, code review time; do back-of-the-napkin math versus peers; convert to a value calculation.

**Process changes beat rebuilds** (Nicole Forsgren) — One company avoided a mainframe replatform by replacing a printed-and-walked approval with an email. Find the process everyone hates and check whether a process change removes the delay.

**Stripe change pipeline and paper cuts** (David Singleton, David Singleton episode) — Tests run in about 15 minutes in parallel with human review, rerun after merge for 15 more, then about 30 minutes to auto-deploy. Aim to close feedback within 24 hours. Auto-deploy with automated monitoring removed babysitting; auto-merge checkbox removed a human step; a crying-octopus button in every dev tool captures paper cuts; a monthly survey of a rotating sample plus usage data sets the dev-productivity roadmap; selective test execution keeps test time flat as the codebase grows.

**Portfolio approach to build time** (Dhanji R. Prasanna) — Test selection halved test runs; deleting obsolete tests or offloading to cloud saved two to three times that. Eliminate the work before optimizing it.

**Code yellow** (Farhan Thawar) — When metrics show a systemic problem, declare a code yellow with a champion who can tap anyone on the shoulder to fix the infrastructure.

**Pair programming and one-hour delete** (Farhan Thawar) — The most underutilized management tool in engineering. Two people, one computer; use for important code, incidents, unblocking; about four to eight hours a week at Shopify. Fails for pathfinding. One-hour variant: if the feature cannot be written in an hour, delete the code, keep the tests, restart.

**Delete Code Club and maintenance-cost audit** (Farhan Thawar; Jay Baxter) — Dedicate a team at hack days to deleting code (Shopify finds a million-plus lines). Periodically list incremental wins, estimate maintenance cost, delete those where cost exceeds gain.

## 3. Decisions, meetings and approvals

**Three questions to end every meeting** (Alisa Cohn) — What did we decide, who needs to do what by when, who else needs to know. Reserve 5-10 minutes; in large meetings sample two or three people; make follow-up someone's job.

**Meetingageddon** (Farhan Thawar) — Once a year, delete recurring internal meetings with more than two people (not 1:1s, interviews, external), two-week ban on new recurring meetings, re-add only what is needed at the right cadence. Move status updates out of chat into a feed.

**Clock speed one click faster** (Claire Vo) — Every deadline is pulled in one time-horizon step. Corollary: do not let 'we'll decide next meeting' set pace; decide now or tomorrow where possible. Personal SLA: leaders in the approval path hold themselves to fast turnaround. Related: Brian Chesky's bias for action (name an owner, check back in an hour); Matt Mochary's written pre-reads cut a three-hour exec meeting to 45 minutes.

**DRI and single-threaded owner** (Casey Winters; Brian Halligan; Naomi Gleit) — One driver per cross-functional initiative, with enough power to direct people outside their org; shared ownership means over- or under-watering. Once decided, disagree and commit with no escalation path. Gleit adds a single-threaded owner for every work stream, recursively, and one canonical project doc. Best-person-as-DRI regardless of function (Garrett Lord). DACI plus operating rhythms (Melissa Tan).

**One blocking approver and review limits** (Paige Costello) — One accountable approver per review, no more than three reviewers, host removes attendees above ten and writes better decision notes.

**Five-day escalation** (Hari Srinivasan) — Unresolved after five days moves up a level; add a raise-your-hand loop where leads flag blockers instantly and leaders resolve them (Varun Parmar).

**20% and 80% review** (Krithika Shankarraman) — A transparent forum with two checkpoints: 20% on what, for whom, rough approach; 80% when artifacts exist but slack remains. Never review at 99%. Related: three check-in moments (first principles, approach and architecture, ship-readiness) at bigger orgs (Nickey Skarstad); beta-to-GA leader review (Geoff Charles); never block a ship waiting for a leader's calendar (Kevin Weil).

**GSD weekly updates plus six-week reviews** (Farhan Thawar; Archie Abrams) — Weekly per-project updates with video or demo; every six weeks, review every project with leadership; nothing ships without the group lead's okay-to. Use check-ins to pair on problems, not as a gotcha. Demo culture keeps debate about the experience, not status.

**One-way vs two-way doors; no, then go** (Mihika Kapoor; Tom Verrilli) — Most software decisions reverse cheaply, so state an opinion and anchor people around it. Enumerate what could go wrong, then move anyway. Fails for irreversible or safety-critical launches; Ethan Evans adds 'fear the headline' where failure would be news.

**Manufacture momentum** (Laura Modi; Nick Turley) — Set arbitrary but explicit launch dates; run a daily release sync with every decision-maker at small scale and set the team's resting heartbeat; retire it when it stops scaling. Ask 'is it maximally accelerated?' to find critical path.

## 4. Scoping and time-boxing

**Appetite (fixed time, variable scope)** (Ryan Singer; Jason Fried; Vijay Iyengar) — Decide the maximum time the business will spend, then shape a version that fits. Six weeks is a maximum. Fails if you impose a deadline on an unshaped giant project, or adopt six weeks without shaping. Iyengar: make the time box the input to planning, not rigid six weeks for everything.

**Shaping and the paper shredder** (Ryan Singer) — Hand builders one whole shaped idea instead of splitting it into 100 tickets. Signs of missing shaping: blob request, engineering pushback on the Figma or PRD, mid-build questions with no getting warmer. Pilot with a 3-6 week problem important to everyone; shape within the window before engineering frees up.

**Nine-box kickoff** (Ryan Singer) — Builders draw nine chunks of implementation; six weeks is 30 days, about four days per box; seven plus or minus two keeps the whole thing in one head. Seniors review juniors' approach.

**Hill charts and kill at deadline; circuit breaker** (Jason Fried; Ryan Singer) — Plot work uphill (figuring out) versus downhill (execution). At the time limit, unfinished uphill work almost certainly dies (Fried); Singer's softer version pulls it back into shaping before any reinvestment. Singer warns that cutting scope at the deadline is not free if it removes what made the thing valuable.

**Working version at 10% of time** (Nan Yu) — By 10% of the budget have something that tests the key hypothesis; first version is a best guess; deadlines are rare and P0; speed and quality are not a trade-off for experts. Widening circles of beta users (internal, early access, betas, GA) gives feedback.

**Deadline trap** (Daniel Lereya) — Time-box by calendar rather than effort; more time creates assumptions and invented features. Build shared infrastructure, then run a hackathon where each developer builds one item in a day (4 months compressed). Fake speed skips stages; real speed works only on what moves the needle.

**Cut scope, not quality; simplest V1** (Gaurav Misra; Jackson Shuttleworth) — Remove every element and ask if it is still useful; ship that core. Strip to the core hypothesis, ship, and add one tested layer at a time. Misra pairs it with one marketable product per engineer per week.

**Quality, features, deadline: choose two** (Dylan Field) — Usually keep the deadline and a minimum quality bar, cut features, then iterate on quality. Fails for physical products or users who will not give a second chance. Related: minimal lovable product (Jiaona Zhang), be embarrassed by the first iteration (Laura Schaffer), tech spike up front (Jiaona Zhang).

**Understand work** (Bangaly Kaba) — Put de-risking and learning on the roadmap with owners across functions, run in parallel with execution; build a sprint portfolio mixing low-effort high-impact and medium-effort high-impact executions so understanding never stalls shipping. Anti-pattern: identify, justify, execute.

**Commit dates only for controllable phases** (Annie Pearl) — Discovery gets a committed end date, then solutioning, then build with estimates; put discovery on the quarterly roadmap as a committed item.

**Customer love sprint** (Noah Weiss; Jessica Fain) — Two-week hackathon-like sprint burning down low-effort, high-impact fixes; ship everything. At Slack engineers picked what to ship and delivered 65 improvements. Run quarterly for user-facing teams.

**Design the hardest part first** (Caitlin Kalinowski) — Start at the pinch points where the product is likeliest to fail; do known to-dos right now because surprises will eat slack.

## 5. Focus and capacity

**Back to a functional startup org; cut 80% of projects** (Brian Chesky) — Write down everything in one sheet, cut to what you can do, put three teams on one thing instead of one team on three, remove layers, replace divisions with functions, hire fewer more senior people. Related wartime focus: 40 priorities to three (Brandon Chu); make the proven bet the number-one priority above all (Kayvon Beykpour); priorities must show up in resourcing (Tomer Cohen).

**Barrels and ammunition** (Keith Rabois; also Nick Turley) — Few people can take an initiative from inception to success; the barrel-to-ammunition ratio caps parallel initiatives. Count barrels, add them before ammunition, match ammunition to each project.

**Deliberately understaff; capacity calculator; dehydrated hiring** (Matt MacInnis; Timothy Davis; Varun Mohan) — Bias toward understaffing since overstaffing breeds politics. Hire only when a capacity calculator is red for multiple quarters and cutting meetings does not cure it. Hire only when the team is underwater, like adding water to a dehydrated company. Stewart Butterfield and Matt Mochary add that managers want reports and every added person adds geometric overhead; Molly Graham warns that growth above 100% a year is harmful.

**Single-threaded leader and single-threaded small team** (Bill Carr; Geoff Charles; Keith Coleman) — Replace project orientation with a persistent program owned by one leader with dedicated cross-functional resources and controllable metrics; requires service-based architecture and documented APIs, fails on monoliths. Charles's recipe: small team (3 engineers, designer, PM), one goal, tight timeline, shielded and not announced. Keith Coleman's Thermal team adds one driver, one senior decision-maker, 100% dedication and repeated funding decisions.

**Beneficial silos and innovation by isolation** (Heidi Helfand; Noam Lovinsky; Matt Mochary) — Put a new product team off to the side with process freedom, a real decision-maker and a leader telling others not to disturb it. Fails without executive sponsorship, or if others must maintain what it builds; avoid organ rejection by framing it as core to the mission.

**Known valuable work and coordination cost** (Stewart Butterfield; Alex Komoroske) — As companies grow, supply of known valuable work shrinks and people fill the gap with work-like activity; coordination cost grows with the square of people; a big rig must pivot less and add program management and planning slack.

## 6. Org design for velocity

**Product operating model** (Melissa Perri; Marty Cagan) — Four parts: strategy, org design, product operations, culture and incentives; a development operating model (agile) alone does not cover go-to-market or product management. Cagan's version is about 20 principles across strategy, discovery and delivery. Scale with leaders, not process (Cagan); Perri counters that process is not the enemy at scale.

**Product operations** (Melissa Perri, Denise Tilles, Christine Itwaru) — Three pillars: business and data insights, customer and market insights, process and practices. Start with one person on the highest-leverage pillar; high-growth companies start with data, enterprises in transformation start with process and governance. Report to the CPO; PMs keep decisions; a one-to-one ratio is wrong. Casey Winters views ops roles as a hack that should work to eliminate their own need; Itwaru and Brian Tolkin disagree (ops is a sign of growth).

**Baseline, train, practice, level-set** (Melissa Perri) — For large PM transformations: baseline everyone, train, practice, let some opt out into ops, data or research, level-set and add experienced hires where teams are weak. C-suite must set direction; middle managers stall transformations. Product owner should be a product manager, SAFe splits discovery from backlog and creates order-takers.

**Conway's law restructure** (Dhanji R. Prasanna) — You ship your org structure; Block moved from independent business-unit teams to a single engineering and design org to unlock AI and platform investment. Counterpoints: Drew Houston says functional orgs lose accountability past one product; Kayvon Beykpour says functional orgs need a tiebreaker.

**Alpha and beta of process** (Matt MacInnis; Eeke de Milliano) — Process lowers variance but suppresses upside; apply rigid process where reliability matters (payroll), a touch where creativity matters. Use minimum viable process: templates state the bar, not the ceiling; break the org for high performers.

**Pods with product staff; functions and missions** (Adam Mosseri; Alex Hardiman; Tomer Cohen) — Instagram pods of four to six generalist engineers plus a product staff lead; functions own craft, missions own work; pods reassembled each quarter.

**Feature team vs empowered team** (Marty Cagan) — Feature teams get a prioritized roadmap; empowered teams get problems and are measured on outcomes. Empowered teams need a problem, a real PM, strategic context and discovery skills. Gokul Rajaram: present the target behavior change, not the feature, to avoid a feature factory. Ryan Singer: a shipping feature factory is healthy, fix the input.

**Context, not control** (Elizabeth Stone; Claire Hughes Johnson) — Share leadership notes org-wide; show live dashboards in metrics reviews rather than slides; house of founding documents, supporting structures and operating cadence.

**Reteaming** (Heidi Helfand) — Five patterns: one by one, grow and split, merging, isolation, switching. Signals a team should split: meetings take longer, decisions get harder (five people versus thirteen), work diverges. Whiteboard reteaming makes reorgs transparent.

## 7. Quality, rewrites and tech debt

**Rewrites are a trap** (Camille Fournier; Maggie Crowley; Katie Dill) — Engineers underestimate migration time and what the old system does. Crowley's side-by-side rewrite estimated at six months took two and a half years. Stage the uplift of contained pieces, inventory undocumented business rules. Counter: Dhanji R. Prasanna suggests that with AI, rebuild from scratch each release if the spec captures accumulated fixes; Melanie Perkins' two-year frontend rewrite was essential for scale.

**No bug backlog; red-metric feature freeze** (Geoff Charles) — Production engineers fix bugs as surfaced; if customer-confusion tickets rise or a metric is red, freeze new features. Yuhki Yamashita adds: let bottom-up engineer fixes happen, they are estimated at about half the time of PM-requested work.

**Tech debt as a product problem** (Ebi Atawodi; Melissa Perri; Gaurav Misra) — The PM owns it. Perri: if the backlog is thin, let developers choose tech debt. Misra: deliberately take on debt and pay it down in a planned quarter.

**Proof of existence; research preview** (Jeff Weinstein; Jenny Wen) — Break red tape with one working end-to-end instance. Ship early under a research preview label and keep visibly iterating; trust is lost only when nothing follows.

**Dogfooding and staged rollout** (Nickey Skarstad; Mihika Kapoor; David Singleton) — Use the product constantly, put it on staging early, roll out to a small percentage then ramp, and unship developer-only visibility tools before launch (Roman Ugarte).

## 8. AI-era velocity

**Slowest part of the system** (Brian Balfour) — Map the whole system including permission, budget, IT, legal and procurement; attack the slowest part. Dan Shipper: adding capacity in one stage (non-engineers filing pull requests) breaks the next (review and integration).

**Automate the path to production** (Sherwin Wu) — Agent patches lint errors and restarts CI; measure PRs merged per engineer.

**Idea-to-users in a week** (Cat Wu) — Anthropic's feature timelines fell from six months to one month and sometimes a week or day; build a corner of the product where an idea reaches users by end of week and de-emphasize multi-quarter alignment, keeping PRDs for heavy infrastructure. Cost: product inconsistency, so invest in education.

**Port with a reference** (Alexander Embiricos) — Have the agent read the existing implementation, produce plans, and implement while viewing both sides; Sora Android shipped to employees in 18 days and GA in 28 days with two to three engineers.

**Fast demo, slow deployment; proof of usage** (Aparna Chennapragada; Simon Willison) — Time to first demo shrinks but the bar for scale rises; tests, docs and polish no longer signal quality, so label unused work as alpha. Dan Shipper's vibe-coded launch needed human senior engineers to stabilize.

**Fast and slow groups** (Howie Liu) — A fast AI platform group ships capabilities near weekly; a slow group builds infrastructure so adoption seeds grow into deployments. Ask how an AI-native company would execute and whether you are as fast.

**Automate before you hire** (Claire Vo; Jeff Weinstein) — Spend a week trying to automate the role before opening the JD.
