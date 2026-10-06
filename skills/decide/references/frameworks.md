# Decide: frameworks

Every framework below comes from Lenny's Podcast guests. Each entry: originator and episode, what it is for, when it applies or fails, steps, and benchmarks.

## 1. Framing the question

**Eigenquestions** (Shishir Mehrotra, Shishir Mehrotra and EOY Review) — Find the question that, once answered, answers the most other questions. Applies: strategy offsites, a team split on many hard calls. Fails: hard to find under pressure; takes practice.
Steps: list all open questions; for each, count how many others it would resolve; rank by that, not importance or recency; debate the top one explicitly; derive the rest. Follow-up test: what decision will answering it let me make? Example: YouTube's Modern Family debate became *will online video value consistency or comprehensiveness?*, which settled linking out, embedding other players and taking back the iPhone app. Practice on low-stakes cases (why three gas stations on one corner?).

**Missing diagnosis and Think again** (Richard Rumelt) — A statement of desire is not a diagnosis. Ask *because...* until a cause is named; resolve internal disagreement about the cause before choosing actions. Then write down why you reached the diagnosis and deliberately look for a bigger piece of wood: another way to see the situation.

**Problem, cause, solution** (Patrick Campbell) — State the problem, list causes, rank by magnitude, align solutions to the biggest causes. Works from strategy down to a support ticket.

**PPS: problem, people, system** (Austin Hay) — For a tooling or ops request, define the problem, then who is involved (approvers, trainees, confounders), then the system. Resist requests like give me admin access to the tool.

**MECE decomposition** (Sri Batchu) — Split a problem into mutually exclusive, collectively exhaustive branches (revenue per customer vs number of customers, then recurse) to avoid missing causes.

**First-principles event questions** (Eoghan McCabe) — Who is it for, what is the goal, what mechanism makes it work, what other mechanisms reach the same goal, how do we define success, how does the user define value. Aarthi Ramamurthy's version: if the product did not exist, would you build it the same way for these customers? Endorsed by Farhan Thawar (rebuild from first principles) and Geoff Charles (do not pattern-match from past companies).

**Do we even need this? / Question base assumptions** (Dhanji R. Prasanna) — Before buy versus build, ask whether the process needs to exist. Camille Fournier's rewrite test: could I leave this untouched for a long time without harming the business? Chip Huyen's technology triage: how much better is the optimal choice, and how hard is it to switch later? If small, stop debating.

**Systems thinking for product decisions** (Sriram Krishnan; Nickey Skarstad, Hari Srinivasan, Kunal Shah on second-order effects) — List every actor, their incentives and how they interact; then ask what happens next, and after that. Linchpins in a marketplace are costly to change. Skarstad recommends Thinking in Systems. Will Larson's stocks and flows: find the biggest drop-off, stop modeling at close enough, because reality is always right. Fails: over-modeling.

**Should/can divide** (John Cutler) — Some teams only ask can we given constraints. Ask: if the constraints were gone, what should we do? Then decouple current tactics from optimal ones. John Cutler also offers Cynefin: classify the situation as clear, complicated, complex or chaotic before picking a decision approach.

## 2. Setting the rigor budget

**Decision triage** (Brandon Chu) — Rate how important a decision is first. Check reversibility and breadth of user impact; spend your time on the few critical ones, decide the rest by gut or delegate. Fails: he admits he may dismiss too much.

**Calories proportional to consequences** (Dharmesh Shah) — Effort scales with the cost of being wrong; a continuous version of one-way and two-way doors.

**One-way vs two-way doors** (Amazon; Nickey Skarstad, Gibson Biddle, Mayur Kamat, Claire Hughes Johnson, Eeke de Milliano) — Spend time and seek buy-in only on hard-to-reverse decisions. Gibson Biddle: check magnitude and reversibility; a two-way door can cost real money and still be fast. Skarstad: standards all supply must follow (Airbnb Experiences, Etsy handmade) were one-way. Eeke de Milliano: test rigorously whether a trapdoor really is one; pricing can be grandfathered, titles cannot. Mayur Kamat: reserve deliberate analysis for what could kill users or the company.

**Two-way door misuse and the two-minute/two-day/two-week pause** (Shreyas Doshi, Shreyas Doshi Live) — Below CEO level, most apparent two-way doors are one-way: you are committed, busy, and the QBR will ask you to defend the feature. Before committing, think through customer motivation, differentiation and distribution, and pause two minutes, two days or two weeks. Fails: genuinely cheap, reversible experiments. Also: strip a catchy framework to plain words (fail quickly, reversible decision) and see if it still convinces you.

**30 to 70 percent data rule** (Shaun Clowes, citing Colin Powell) — Under 30% of the data is a big mistake; waiting for 70% or more is far too long. Companion: diminishing returns on information (Evan LaPointe), and Anneka Gupta's decide at roughly 70% because committing yields better learning than waiting; do not use for irreversible high-stakes bets.

**False precision** (Alex Komoroske) — Pinning down uncertain numbers at great expense is a comfort blanket; check only the order of magnitude when the upside is large. Fails when the margin between options is small (Sri Batchu: marginal decisions are marginal for a reason).

**Will anyone remember in six months?** (Will Larson) — If not, pick something reasonable and move on. Related: Mental time travel (Annie Duke): how will I feel in 10 minutes, 10 months, 10 years? Fails: some things matter in 20 years.

**Pick the side to err on** (Matt MacInnis) — When the answer is unknowable, make a best guess and decide whether over-steering or under-steering relative to your midpoint is cheaper.

**Slicing decisions** (Alex Komoroske) — Smaller steps remove most risk while keeping exposure to upside. Companion: Ryan Singer's budget-driven trade-offs: fix the time budget and vary scope.

## 3. Collecting input and deciding

**Discover, discuss, decide** (Annie Duke) — Only discussion belongs in the meeting. Steps: decide which opinions you need; ask each person independently and asynchronously for a forced ranking with a three to five sentence rationale; for repeated decisions, use a form only you can see; circulate the compiled view; discuss the disagreements; decide outside the room via one decider or a private vote. Applies: roadmap planning, forecasting, budgeting. Anti-pattern: loudest-voice estimation, where cross influence hands the decision to the most confident or senior person.

**Nominal group forecast** (Annie Duke) — Everyone independently submits point estimate, lower bound and upper bound for a timeline with a rationale; the facilitator reflects back without an opinion.

**Alignment is stupid** (Annie Duke) — Do not ask are we aligned. Explain why you believe something; leader states the decision and acknowledges disagreement. Contrast with Naomi Gleit's extreme clarity: everyone shares the same facts, options and trade-offs even if they disagree.

**Work alone together, note and vote** (Jake Knapp, Jake Knapp and John Zeratsky) — Silently write several answers, vote, designated decider locks it, move on. Works for 2-7+ people and solo founders. Jake Knapp's lenses: plot options on several lenses (including founder conviction); if nothing wins every lens, pick the priority lens.

**Role-grouped Pulse and sentiment table** (Shishir Mehrotra, from Coinbase RAPID; Lane Shackleton) — Add a role column (responsible, approver, participating, informed, decider), pre-fill what you need from each person, let informed people comment but not block. A sentiment rating per reader exposes quiet dissent (a lead designer's one smiley) before the meeting. Mehrotra's warning: consensus building to a fault leaves a decider with 30 inputs and no idea whether consensus is needed.

**Decision involvement table** (Lane Shackleton) — List upcoming decisions; stakeholders mark heavily involved, opinions but keep going, or notify me after. Default most decisions to keep going and notify.

**Decide who decides** (Dharmesh Shah; Claire Hughes Johnson, Hari Srinivasan, Keith Yandell, Kevin Aluwi) — Naming the decider is nearly the first decision. Claire Hughes Johnson: pick a model (SPADE, RACI, RADAR), state that a decision is being made, name the decider, criteria and informed; if unsure, it is probably you. Hari Srinivasan's RAPID: recommend, agree, input, decide; one name on the decision line. Heidi Helfand's RIDE for org changes: request, input, decide, execute. Kevin Aluwi: accountable equals decider. Keith Yandell: name the tiebreaker and a deadline; first make each side steelman the other with three best reasons.

**Disagree and commit / champion / unite** (Bill Carr; Sanchan Saxena; Dharmesh Shah) — Disagreement supplies new information; once heard, commit by understanding, not grudging compliance. Sanchan: disagree and champion, with a DRI who gathers written input from functions. Dharmesh: debate, decide, unite. Dylan Field: if not fatal, say go with it and share your skepticism.

**Go around the circle and state what we decided** (Deb Liu; Alisa Cohn) — Ask every leader what they would do, functions included; at the end ask each attendee to state the decision to expose six different answers. Fails: a written summary may silence quiet dissenters.

**Three options and a recommendation, live-edited visual** (Naomi Gleit) — Three options, a recommendation, and a slide edited live to record the choice and numbered next steps.

**Traffic-light option table** (Naomi Gleit) — Options as rows, criteria or functional perspectives as columns, red/yellow/green with rationale; rule out the reddest; each function owns its cells. Replaces flat pros and cons.

**Power of three PR/FAQs and recommend one** (Anuj Rathi) — Write three divergent, fully thought-through PR/FAQs; present side by side; explain why rejected options were rejected; the PM still recommends one. Ebi Atawodi: do not bring an A-versus-B doc; align on a side and bring the risks you need help with. At Netflix, write the argument but one decider decides.

**Single Decisive Reason** (Rahul Vohra) — For important decisions find one reason that alone supports it; ask if only one of these were true, would you still do it? Weak reasons rarely add up and hide opportunity cost. Fits consensus-driven or risk-averse groups.

**Decision factors spreadsheet and weighted criteria** (Dharmesh Shah; Nicole Forsgren) — Listing the factors is 80% of the value; stack-rank without exact weights. Forsgren: define the objective, list options and criteria, weights summing to 100%, score, multiply, then sanity-check against your gut (data informed, not data driven). Fails: over-quantifying small decisions.

**Stress-test questions** — What do we do if it is green? if red? (Tom Verrilli); if you could build only one of five, which? (Ebi Atawodi); is it better for the customer too? (Jason Cohen); how does this make users love the product more? (Shreyas Doshi, from Jack Dorsey); how do you know? chained down to the label source (Tom Verrilli); what would a human teammate do? (Roman Ugarte, for AI products); put a number on it (Amol Avasare); what are you optimizing for, today, this quarter, this year? (Nikita Miller).

**Convert trade-offs to ratios and project principles** (Caitlin Kalinowski; Jake Knapp) — Put a numeric exchange rate between goals (value of a gram vs dollars). Turn each differentiator into a one-line principle that settles later trade-offs.

**Separate facts from hypotheses** (Megan Cook) — Present what you know as facts and the rest as hypotheses with a test plan; exposing your thinking builds credibility. Maya Prohovnik: gut is a valid data type but must be explained objectively.

**Conviction levels** (Brian Tolkin) — Rate low, medium or high; for consequential decisions at low or medium, talk to more customers or compare intuition with another person, then set a feedback loop after shipping.

**Data vs opinion on a 1.0** (Tony Fadell; Jason Fried, Sanchan Saxena) — In a new category with few analogs, a very small set of informed taste-makers make opinion-based calls, articulate the why, ship and correct. Fails: mature products with good analog data, or deciders without informed gut. Counterweights: Itamar Gilad (supercharge opinion with evidence), Mayur Kamat (Rosenberg rule: bring data, not ideas), Ronny Kohavi (hierarchy of evidence; do not ship on flat), Judd Antin (check gut with slow thinking and a diverse crowd).

## 4. Risk and conviction

**Pre-mortem and tigers, paper tigers, elephants** (Shreyas Doshi) — Imagine the launch failed miserably six months from now; work backwards; silent writing; share; each person picks the scariest tiger raised by someone else; leader prioritizes and owns the action plan. Cheap, low downside, high upside. Many launch backlashes were obvious to someone who lacked safety and vocabulary.

**Pre-mortem with kill criteria** (Annie Duke) — A pre-mortem alone rarely changes plans (her research with Schweitzer and Gandhi). Turn each early signal into a kill criterion with a pre-committed action: kill, pursue, probe. Related: quarter-long go/no-go milestones (Jiaona Zhang); Bing's 100 person-years (Ronny Kohavi); six-pager stage gates read silently for 15 minutes (Tanguy Crusson).

**Murder board** (Nabeel S. Qureshi) — Two-page plan (vision, goals, three-month tactics, principles) torn apart by three or four smart outsiders. Related: red teaming your own idea (Jessica Fain); open the code before green-lighting (Ryan Singer's grumpy plumber).

**Make the bet's assumptions explicit** (Tom Conrad) — List what the model needs from day one, benchmark each against comparable products, and tell the founder the probability. Distinguish structurally impossible from highly improbable.

**Check with someone not in fear** (Matt Mochary; Jonathan Lowenhar, Jonny Miller) — Fear gives bad advice; separate intuition (quiet, pattern recognition) from reaction (a fear response). Mochary: ask someone not in fear, predict outcomes of both options. Jason Droege: when highly convicted, run your list of known biases. Joe Hudson and Jonny Miller argue emotions are inputs to name rather than suppress.

**Same decision, same result** (Qasar Younis) — Strip ownership and emotion: would several people in the company reach the same decision? Bret Taylor: confidence is not correlated with opinion quality; single-issue voter bias at 30%.

**Negative visualization and fear setting** (Jason Fried; Paul Millerd) — Role-play the worst case and be at peace with it, only for bets you can afford to lose. Millerd: write fears, mitigations and the cost of inaction.

## 5. Quit, pivot or persist

**Quitting too late** (Annie Duke) — By the time you think about quitting you are past due. Ask whether you would start this today, count only future costs, set kill criteria in advance.

**Conviction test** (Scott Belsky) — More or less conviction than at the start? More: messy middle. Less: quit or pivot. Not on a bad day. Companions: Uri Levine's would I do this if I started today with a 90-day clock; Graham Weaver's quit when you can no longer see or believe the vision; Noam Lovinsky's stamina kills projects.

**Out-of-growth-ideas pivot test** (Dalton Caldwell) — List untried credible growth ideas; half a dozen or more means keep trying; vague hopes mean pivot.

**Fixed-period pivot reset** (Eric Ries) — If you suspect you should pivot you already know. Time-box a weekend to six weeks; one person or team on one thing; everyone says what they wish they were doing; give excited ideas a month each; if exhausted, consider returning money.

**Kill hope, B+ test** (Mark Pincus) — Belief is grounded in behavior and data; hope is confidence without basis. If you are asking whether it is an A, it is not.

**Pivot when the assumption breaks** (Varun Mohan) — Write the assumption the business depends on; when it breaks, pivot fully, not side by side. Regret: not being wrong faster. Todd Jackson and Tom Conrad: winding down early and returning cash is legitimate.

**Crisis triage** (Uri Levine; Ben Horowitz; Brian Halligan) — What is impacted, how long will it last, how much runway; decide today; target a runway (12 months) because waiting shrinks it. Horowitz: when both options are bad, pick the less-bad one explicitly and fast. Halligan: do the bad news once, not in rounds.

**No sunk cost and re-derive the tree** (Brandon Chu, Tobi Lütke) — Shopify throws away roadmaps three to six months in if the world changes. Lütke: re-run the decision over the updated state; if a root assumption flipped, accept the new landing zone. Ethan Evans: gambling consciously is forgivable.

## 6. Learning from decisions

**Resulting** (Annie Duke) — Judging quality by outcome; luck and temperament confound it. Applies to post-mortems and performance reviews.

**There is no such thing as a long feedback loop** (Annie Duke) — Pick necessary and correlated intermediate outcomes, forecast them at the decision, and track them back. Applies: venture, long product bets.

**Make the implicit explicit and the decision rubric** (Annie Duke, First Round) — Break the decision into components rated 1-7 with shared definitions (mediating judgments), add forecasts, record, compare to outcomes, refine. Needs many resolved decisions (hundreds over five years). Even expert partners found factors that predicted for others but not for themselves.

**Decision log** (Kevin Yien; Eric Ries's whiteboard memory) — Record decision and rationale, set a reminder, review. A big text file with a #decision tag; start with one weekly bet. Not a replacement for building. Eric Ries: memory is buggy; written hypotheses reveal how your views actually changed.

**Be the historian and ask why not what** (Anneka Gupta; Bret Taylor, Howie Liu) — Reconstruct how and why past decisions were made. When taking advice, ask for the chain of thought, ask three advisors, build your own model.

**Curiosity Loop** (Ada Chen Rekhi) — A structured ask to a curated set of people before a big decision; read the pattern of answers for surprises; reserve for roughly quarterly or truly indecisive moments. Not a substitute for deciding.

**Values exercise and run the movie forward** (Ada Chen Rekhi) — Pick values from a word list, group, stack-rank into three to five sentences, score your current path and any new option; revisit as life changes. Companions: Deb Liu's career measuring stick; Bob Moesta's name your trade-offs; Joe Hudson's five personal principles tested five days each; Chip Conley's anticipated regret; Molly Graham's financial vs capability fear.
