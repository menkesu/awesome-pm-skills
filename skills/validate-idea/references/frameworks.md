# Frameworks: validate-idea

Grouped by theme. Each entry: originator and episode, what it's for, when it applies or fails, steps, benchmark.

## 1. Frame the hypothesis and pick the riskiest assumption

**1. Foundation Sprint** (Jake Knapp, Jake Knapp + John Zeratsky) — Make the key early decisions and write one founding hypothesis before building. *Applies:* new product, startup or large project at inception, especially pre-seed. *Fails:* if you already have strong product-market-fit evidence and conviction. *Steps:* clear the core team's calendar for about 10 hours in two 4-6 hour blocks → Phase 1 basics (customer, problem, competition, advantages) → Phase 2 differentiation (score against competitors, pick two differentiators, set principles) → Phase 3 approach (list implementation paths, compare with magic lenses, pick a first choice and a backup) → write the founding hypothesis as one sentence → follow with 2-3 weeks of design sprints. *Benchmark:* founders report compressing 3-4 months of work into 3-4 weeks (subjective).

**2. Design Sprint** (Jake Knapp; Miro's Varun Parmar runs it for zero-to-one) — Five days from zero to a prototype and a customer test, replacing the perfect PRD. *Applies:* teams stuck on an idea; high behavioral risk (AI, health, education, trust). *Fails:* a slightly cheaper or faster version of something that already exists. *Steps:* map the customer path and key moment → sketch individually → decide → prototype on day four, not before (John Zeratsky) → test on day five. Parmar's add-on: at the end, ask who you got insight from, and let that insight choose the architecture.

**3. Design-sprint loop with founding-hypothesis scorecard** (Jake Knapp) — Weekly sprints that each start from the hypothesis and the biggest current risk. *Steps:* start from the hypothesis → ask which risk is biggest → pick the key moment → prototype (for example three head-to-head with fake brands) and test with new customers → per-interview scorecard: right customer? has the problem? right approach? chose it over real competitors? differentiation valuable and motivating? → write conclusions, edit the hypothesis, sprint again. *Benchmark:* Latchet's first scorecard was mostly red after four interviews and green by sprint three; expect red. *Caveat:* interviews are a simulation of the real world.

**4. Leap-of-faith assumptions to MVP chain** (Eric Ries) — If you can't scope an MVP, the problem is upstream: you're unclear on what you want to learn. *Steps:* brainstorm and categorize leap-of-faith assumptions → select the riskiest → for each, brainstorm metrics and pick the learning metric → brainstorm MVPs and score them → build the cheapest test. *Applies:* teams stuck on scoping, especially in corporations.

**5. MVP is a hypothesis test, not a stripped-down product** (Eric Ries) — State the hypothesis, learn the customer's quality bar in your market, and if it's high build only the one critical feature at that quality; ship to about 10 customers and have them tell you what is awful. *Fails:* when craft itself is the thesis.

**6. Cut the feature list in half, twice** (Eric Ries) — People misjudge what's necessary by one or two orders of magnitude; the MVP curve is U-shaped so near-optimal is enough.

**7. Sequential validation: if this is true, what must be true next** (Nikita Bier) — List about four must-be-true statements, execute the stage you're validating at 100% (core flow, spread within a peer group, hop between groups, monetization) and half-ass the rest. *Fails:* products where every layer must exist to function at all.

**8. Four-box framework: words, then data** (Nicole Forsgren) — Top row: cause and effect in words, aligned with stakeholders; bottom row: data proxies for each. Failures trace to bad data or a bad hypothesis rather than blame. Don't use the outcome as its own proxy.

**9. Match discovery depth to risk** (Teresa Torres) — Robust discovery on core experience and differentiators; skip heavy discovery on commodity flows; instrument releases to learn where the risk really is. *Fails:* companies that assume no risk and do none.

**10. Compare and contrast multiple solutions** (Teresa Torres; Simon Willison does it with AI) — Work several solutions for the same opportunity, as you would compare apartments. Willison: prototype three versions of every feature because prototypes are nearly free; ask AI for 20 ideas, then 20 more, and mine the tail.

## 2. Problem validation: is it real and sharp?

**11. Validate with strangers** (Uri Levine) — Talk to about 20 people you don't know (aim up to 100). I know someone with this problem means it isn't real; someone correcting your problem description with theirs is the signal to follow. In B2B, speak with many businesses.

**12. Fall in love with the problem, not the solution** (Uri Levine; echoed by Dharmesh Shah, Jiaona Zhang) — Validate the problem, then think of the solution; describe the product via the problem. Passion is built by validation, not required up front (Levine, Shah; opposed by Andrew Wilkinson's follow-your-passion-into-the-niche).

**13. Reference customer discovery** (Christian Idiodi) — Work with target customers until they will put their reputation behind you. *Benchmark:* 6-8 references for B2B, 15-25 for B2C; all must want the same thing; if you can't recruit them, stop. *Fails:* charismatic asks yield polite promises, hence the large numbers and a focus on hesitation. Strive and Rippling reportedly work similarly.

**14. Bitchin' ain't switchin'** (Bob Moesta) — Complaints and stated intent aren't evidence; only trust people who actually tried to change, and ask what made them try. Research is small-sample hypothesis-building (7-12 interviews), not statistical testing.

**15. Sharp problem** (Oji Udezue) — Pick a problem that steals time, energy, money or focus from many people, or from a few who will pay thousands. On a sharp problem mistakes are survivable.

**16. Workflow compression test** (Oji Udezue) — Draw the current workflow and the post-product workflow; look for 2-3x shorter. After launch, interview enthusiastic users and measure workflow change. Whites-of-the-eyes reactions are an early but less reliable signal.

**17. Workflow quadrant: frequency x breadth** (Oji Udezue) — High-frequency niche workflows are where B2B SaaS thrives; high-frequency everyone workflows are most profitable but Microsoft and Google territory. Not static; plan a route to a higher quadrant.

**18. Behavioral diagnosis before building** (Kristen Berman) — Map every step the target behavior needs, compare say with do, and be skeptical of anything that adds user work. Budgeting, the top-requested feature, produced zero change in a 10,000-person experiment.

**19. Problem journal and niche-community immersion** (Ryan Hoover) — Log annoyances without solving them; immerse in niche long-tail communities for recurring problem statements.

**20. Use the incumbent yourself** (Gustaf Alströmer) — Run the existing experience end to end and record where it fails. Plan outreach at roughly 10 contacts per early-adopter call (the 90/10 ratio).

**21. High-volume buyer calls** (Raaz Herzberg, Wiz) — 10 to 15 customer calls a day with the real buyer in the idea phase; the PM sits on every call; listen to the type of response, not politeness.

**22. Urgency of the buyer** (Jason Droege) — Value isn't enough; the product must address what the buyer thinks about daily, not an annual saving. Wide aperture: keep many ideas alive until signals coalesce (Uber Eats came after about 15 delivery variants).

**23. Pain plus new technology** (Tony Fadell) — Start from real, often habituated pain; ask what new technology solves it fundamentally differently; redesign the whole system. Nan Yu's variant: an outsider maps the rhythm of feelings across the week to find the dreaded moments.

**24. Latent demand** (Nikita Bier; Mark Pincus) — Find places where people go through a distorted, painful process to get a value, or love an activity they skip because it costs too much effort or money. Build the mechanic that delivers the value without the distortion. Pincus: services that were uneconomic before agents.

**25. Value denial** (Richard Rumelt) — List what you should be able to buy but can't; imagine how it ought to work; check whether regulation or materials block it.

**26. Hated incumbent search** (Dalton Caldwell) — List large public or PE-owned companies their customers hate, in a knowable large market with horrible software. Caveat: tailored to Zip's founders.

## 3. Money and demand tests

**27. Price before product** (Madhavan Ramanujam) — You only control when the pricing conversation happens. Pitch the whole value six months before launch and ask would you pay, then why. Match method to stage: idea means the conversation; mid-stage purchase probability; late-stage most/least and trade-offs.

**28. Ready to pay is not paying** (Jeff Weinstein) — Ask for a refundable wire on big promises; have first-time founders send a $1 invoice early; watch who flinches.

**29. Pre-sell before you build** (Dalton Caldwell; Todd Jackson's sell-before-you-build) — Customer validation before code, decks or fundraising; line up customers as the green light. Todd Jackson notes build-first founders can also succeed.

**30. Ask for lots of money fast** (Nabeel Qureshi) — Take it to a customer and ask for a lot; if they won't pay, change problem rather than wait three weeks. Hard to tell failing from quitting too soon.

**31. Brochure test** (Eric Ries) — Replace a costly build with a high-quality brochure and pre-orders to test the real leap-of-faith (a team nearly spent $18M and three years before customers laughed at the efficiency pitch).

**32. Waitlist before code** (Tanguy Crusson) — Advertise in an existing channel your audience reads and collect signups (3,000 in two weeks) to test demand and reach.

**33. Test marketing on the live product** (Mark Pincus) — Put art and message variants of the upcoming feature on the live board, measure clicks, and offer early-access keys; Zynga sold $19M of keys. Needs a large engaged base.

**34. Gross margin short-circuit and business-model filter** (Jason Droege) — Ask why the pitch doesn't work at a much higher margin to expose the real alternative; filter ideas for recurring revenue, stickiness, network effects, lock-in and value at scale; then pick by passion. A coarse litmus test, not an instrument.

**35. Triangulating unit economics** (Jason Droege) — When incumbents won't share economics, build a bottom-up model (order the food, price ingredients from a supplier catalog) and triangulate against what operators and reps say.

## 4. Solution and fidelity tests

**36. Validation spectrum** (Itamar Gilad) — Assessment, fact finding, tests (fake door, smoke, Wizard of Oz, concierge, usability), early-adopter programs, experiments, release. Start left and escalate only ideas with positive evidence. A competitor having a feature is not validation.

**37. Facade test** (Itamar Gilad, Gmail tabs) — HTML facade, researchers hand-sort the user's top 50 messages with permission, reveal after distraction questions; no code written.

**38. Match demo fidelity to product** (Todd Jackson) — Mockups for Lattice, real-data demos for Looker, doing the work manually for Vanta and Pilot. Vanta: delivering SOC 2 manually to three design partners; inefficient at level one is fine if satisfaction is incredible.

**39. Prototype with 20 zero-skin users in a day** (Grant Lee) — Build a functional prototype, recruit about 20 on-persona people with no stake via panels, have them think aloud, review the same evening; chunk ideas small so most die cheaply.

**40. Pretend the product exists** (Chris Hutchins) — Run clickable-prototype interviews as if it's live, reveal at the end it isn't out; read the reaction. Stated interest in automation can overstate adoption.

**41. Fake-door believability** (Mihika Kapoor) — Decide where to take the quality hit and where to push to make it feel real; prototype before the green light.

**42. Test with operations before product** (Keith Yandell) — A promo code handed out in forums, or one hotel with hacky operations, beats a heavy integration that franchisees ignore.

**43. Prove it at every stage** (Keith Coleman) — Mockups, then an ordinary-participant pilot, then about 1,000 public users, then wider rollout; expand only on data. Jay Baxter: pilot data showed polarization, not manipulation, was the real problem.

**44. Trusted tester group** (Robby Stein) — A few hundred testers with a direct channel to report breakage; iterate until feedback turns positive. Daniel Lereya: if first feedback is amazing, you waited too long.

**45. Isolated-market exposure** (Luc Levesque) — Contain marketing to a small off-the-grid English-speaking market for dozens to hundreds of users per day of real signal. Noam Lovinsky: experiments of tens to hundreds.

**46. Graduation trigger from R&D to product** (Ryan Salva) — Informal market tests once a representative set of customers has a genuine problem and there is at least medium-confidence signal that the solution works in a novel way.

**47. Two independent teams** (Matt Mochary) — One custom-code team, one manual/off-the-shelf; see which progresses faster.

**48. Solve the problem to learn the problem** (Christian Idiodi) — Trying to solve it hands-on beats fake-door tests or opportunity trees at exposing say-versus-do gaps.

## 5. Why now, consensus and idea selection

**49. Inflections, Insights, Founder-Future Fit** (Mike Maples Jr.) — External inflection, non-consensus insight, founder matched to that future. *Applies:* pre-seed/seed, zero-to-one. Inflections can be technological, regulatory or belief shifts; Moore's-law-style curves are not inflections.

**50. Inflection stress test and is-this-from-the-future** (Mike Maples Jr.) — Name the specific new thing, how it empowers specific people, and under what conditions it holds; ask what part of the future the founder has lived in.

**51. Two of three inflection points** (Aparna Chennapragada) — Technology step function, consumer behavior shift, business-model shift; proceed on at least two. Ryan Hoover's why-now: what changed, what insight do you have, why doesn't it exist yet.

**52. Savor surprises; Scott Cook's three surprises** (Mike Maples Jr.) — Design experiments that can surprise you; ask a team for its three biggest surprises, and if none, they're seeking validation.

**53. Love-it-or-hate-it polarization test** (Sam Schillace; Maples) — Look at the distribution of reactions, not the average. Bimodal means impact; a bell curve means incremental. Toy criticism can signal real threat but is a signal, not proof. Also what-if versus why-not questions.

**54. Tarpit ideas** (Dalton Caldwell) — Many founders have it, it seems unsolved, positive validation is easy, and it has failed for years. Find the structural reason first. Related: same information diet produces the same ideas.

**55. Base-rate asymmetry** (Richard Rumelt) — State the base rate and the specific skill, information or resource that tilts the odds; if you can't name one, don't.

**56. Potential, probability, passion/proximity, prowess** (Dharmesh Shah) — Score 0-10, starting with potential before probability; none is decisive; passion can be built.

**57. Bezos's three tests and working backwards** (Ian McAllister) — Is it a big idea, should we be doing it, is there a legitimate plan to succeed. Problem paragraph first; if you can't write one, maybe there is no problem. Pantry-ingredients smell test. The press release is a mechanism, not the point.

**58. Proven, Better, New** (Mark Pincus) — Copy what's proven for this exact platform and audience, add a Better that 10 of 10 users would endorse, add one New and expect it to fail; keep four more New ideas ready. Opposes blank-whiteboard innovation. Abused when proven is claimed from another platform.

**59. Pick the hot space if incumbents are unambitious** (Michael Truell) — A sleepy domain the team didn't know failed; the crowded one with under-ambitious incumbents worked.

**60. Idea lag and Uber test** (Benedict Evans) — The bottleneck is often realizing which industry problem a technology solves; you can't predict which industries will be transformed.

**61. Marketplace white space** (Sarah Tavel) — Low-NPS segment of a horizontal marketplace, an ignored niche, or a changed atomic unit of supply; LLMs may unlock long-tail onboarding.

**62. Fish where the fish are; boring is good** (Andrew Wilkinson) — Unglamorous niches with little competition; follow a passion into the profitable adjacent vendor niche.

**63. Pivot to the customer who can pay** (Andrew Wilkinson) — Same skill, segment where a small improvement is worth a lot (realtors earn $20-50K per house); charge 5x for less work.

**64. Crazy Ideas doc; New bets framework** (Eeke de Milliano; Dmitry Zlokazov) — Company-level intake: a January blank doc (90% nonsense, 10% 10x-100x; Retool ships three to eight a year) and Revolut's proposal of market, business case and right-to-win, then a lean first version to a small base, scaled only on retention.
