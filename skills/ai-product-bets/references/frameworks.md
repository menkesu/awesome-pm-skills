# Frameworks: ai-product-bets

Each entry: what it is for, when it applies or fails, how to run it. Originators are named; others who endorse it are noted. Episodes are Lenny's Podcast.

## A. Forward-compatibility tests (will it get better as models improve?)

### 1. The Claude 8 test (Dianne Penn, Dianne Penn episode)
For: testing whether a product is forward compatible. Applies to any AI product on a fast capability curve.
Steps: imagine a model several generations ahead; ask what users would do differently; check whether today's build survives that experience. Output: list of features that disappear (crutches) and features that get better.

### 2. The 2X test (Nick Turley, Nick Turley episode)
For: deciding if a feature is worth shipping. If it does not get twice as good when the model gets twice as smart, it probably should not ship.
Fails for: compliance and enterprise requirements (SOC 2, permissions). Do them, but do not count them as AI bets.
Steps: for each feature ask if model improvement flows through; deprioritize those that do not.

### 3. Model maximalism (Kevin Weil, Kevin Weil episode)
For: AI products where capability, not distribution, is the constraint. Build at the edge of what barely works; skip heavy scaffolding around non-critical failures; keep scaffolding only for errors you truly cannot tolerate; re-evaluate on the next release.
Fails: high-stakes domains with unacceptable errors; products that must work reliably today.

### 4. Worst model you will ever use (Kevin Weil; echoed by Dhanji R. Prasanna)
For: planning on the trajectory, not today's limit. Steps: list capabilities your product needs that models almost have; design for the model arriving in a couple of months; re-test hardest use cases at each release. Benchmark: new reasoning models every 3-4 months, cost for a capability down about 10x per year (Weil); Benjamin Mann cites 10x cost drop per intelligence level.

### 5. Build for the model N months out (Boris Cherny, Amjad Masad, Benjamin Mann, Jeetu Patel, Sherwin Wu, Tara Seshan, Cat Wu)
For: AI products in fast model cycles. N is contested: 6 months (Cherny, Masad, Mann, Patel), a capability that is 80% working today (Sherwin Wu), 2-3 months (Tara Seshan), one month on a golden path that elicits maximum capability from the current model (Cat Wu).
Fails: companies that cannot survive months of weak PMF; if model progress stalls. Steps: identify what the model almost does; build the product around it; ship and switch on as the model lands.

### 6. Prototype all, retest on each model leap (Andrew Ambrosino; Eric Simons, Dharmesh Shah, Cat Wu)
For: products where model capability is the main constraint. Steps: list every feature of interest for 1-2 years; prototype all; ship the ready ones; let the others bake; retry with each new model. Feature viability depends on model smartness, not shape. Eric Simons shipped Bolt after a model crossed a reliability threshold a year after a failed attempt; Dharmesh Shah's GrowthBot failed six years before ChatSpot. Keep a list of ideas that failed due to technology limits.

### 7. Failing in market does not mean the shape is wrong (Andrew Ambrosino)
For: AI products on capability curves. Operator, Atlas agent and Codex are the same idea re-released as intelligence improved. Steps: keep failed-feature artifacts as test fixtures; re-release or retest as models improve. Fails: product teams cannot assume unlimited models; the form factor must fit current ability.

### 8. Too AGI-pilled for the moment (Andrew Ambrosino)
Counterweight to #5. The original Codex web delegated full tasks and was not good enough; Claude Code's local, ask-questions shape fit what models could do. Research ambition can lead; product shape must match current ability.

### 9. Pull the future forward, then delete (Roman Ugarte)
For: products on top of foundation models. Steps: predict what the next generation will solve in 3-6 months; build it now with extra engineering; delete the scaffold when it becomes baseline; repeat. Side effect: accumulate distribution and data advantage.

### 10. Update your priors (Aparna Chennapragada)
For: any team adopting AI. Past failures create scar tissue. Retest tasks that failed a few months ago, set high expectations, and ask how to use AI whenever starting something manual.

### 11. Product overhang (Dianne Penn)
For: products where capability outpaces UX. Current models have capabilities users and products have not found; part of the PM job is discovering and surfacing them. Related: Jeetu Patel on the capabilities overhang.

### 12. Form factor follows model capability (Howie Liu; Scott Wu, Michael Truell)
For: re-inventing UX at each capability step (autocomplete, agentic, full app generation). Map today's one-shot ability to the form factor it supports; re-evaluate each release. Scott Wu expects many generations of agent product.

## B. Scaffolding and model strategy

### 13. Harness features as crutches (Cat Wu, Claude Code)
For: products with a harness around a rapidly improving model. The to-do list existed so Claude would finish all 20 call sites of a refactor; later models did it naturally. Steps: at each launch read the entire system prompt; ask per section if the model still needs it; remove; de-emphasize crutch features.

### 14. The bitter lesson (Boris Cherny; Sherwin Wu, Tamar Yehoshua)
For: teams that can swap in newer general models. Scaffolding gains of 10-20% usually get wiped by the next model; wait rather than build; avoid fine-tuning unless there is a clear reason. Sherwin Wu: models absorb agent frameworks, vector-store pipelines and file-based context. Tamar Yehoshua: a differentiator that compensates for LLM weakness goes away.
Fails: hard cost, latency or privacy constraints that force small or fine-tuned models.

### 15. Latent demand applied to the model (Boris Cherny)
Look at what the model is trying to do and make it easier. Steps: observe what it does unprompted; give a minimal set of tools; let it choose and sequence; make the product the model with minimal scaffolding. Fails: workflows needing strict determinism.

### 16. Custom models complement foundation models (Michael Truell)
For: high-frequency, latency-sensitive or specialized tasks. Steps: custom fast model where foundation models cannot serve on cost or speed (autocomplete under 300 ms); custom retrieval on the input side; frontier model for high-level thinking in few tokens; small specialist to turn sketches into diffs; start from the best open pre-trained model. Fails: where foundation models are already excellent.

### 17. Adapt a model and model system (Asha Sharma)
Adapt an existing model with your own, purchased or synthetic data (post-training, RL) instead of using off-the-shelf as is or training your own. Use a model system: pick models per task by latency and thinking-time need. Also: bet on a swappable platform layer for the slope of change, not any single tool. Chip Huyen: post-training is where labs differ most.

### 18. Pareto-efficient vs frontier by upside (Anish Acharya; Max Schoening)
Use frontier models where upside is unbounded (drug discovery, sales, research, engineering); cheaper open-weight or RL-tuned models where bounded (closing books, legal, finance). Max Schoening: intelligence saturates like retina pixels, then cost, speed and modality matter. Fails: support, where one odd bug report can seed a company-changing insight; cancer research-style domains.

### 19. Model sommelier habit (Anish Acharya; Simon Willison)
Ship something with every new model, note each model's personality, and route work accordingly. Simon Willison: labs leapfrog every few weeks; stickiness is taste fit. Edwin Chen: models will differentiate by the values and objective functions of their labs.

### 20. Three pillars of AI at Canva (Cameron Adams)
Build own models where you have a data advantage, partner for commodity capability (LLMs, video), open an app ecosystem for third-party AI. Do not build an LLM; it is a commodity.

## C. Choosing what to build

### 21. Work backwards from the problem (Inbal Shani, Marily Nika, Melanie Perkins, Tomer Cohen, Anton Osika)
Start from the workflow and the manual or configuration-heavy pain; choose AI only where it shortens time or reduces friction. Marily Nika: user, pain point and high-level solution first, then data scientists. Melanie Perkins: integrate AI inside the workflow where users already work, not front and center for investors. Anton Osika: design the end-to-end experience first, then add AI.

### 22. Map your product against what AI can do (Paul Adams)
Write what the product does and why people use it; list what AI can do today (write, summarize, find facts, scan images, take actions); mark each job AI can do, partially, or not yet; decide replace vs augment; decide what the company does about it.

### 23. Baseline accuracy fit (Jason Droege)
AI wins where the human process is 10-20% accurate or liked; reaching 50-80% is big. Where human accuracy is ~98%, AI will not close the last 2%. Related: Chip Huyen on outcome-clear use cases (conversion, booking, support) getting adopted more easily than internal productivity tools.

### 24. Feature or category reinvention (Marc Andreessen)
Is AI an added ingredient to the existing formula, or does it make the workflow unnecessary? Answer decides retrofit vs rebuild. Companion: AI native, not AI appended (Jag Duggal): ask what you would design if the tools existed from day one. Marc Andreessen's three layers: product, jobs and team size, the idea of a company.

### 25. Hard generative product test (Gustav Söderström)
A true generative product could not have existed without generative AI (Spotify's AI DJ). Separate iterative AI improvements from products impossible before; budget accordingly. Also his rule: do as little as possible and get out of the way, because people came for the music.

### 26. Task versus job (Benedict Evans)
Before assuming AI replaces a role, ask whether the hard part is the automated task or the judgement around it. If the task is the whole job, expect automation; if not, expect more demand. Companions: Jevons paradox as price elasticity; scoring professions as X% exposed is an expert-systems mistake.

### 27. Domains with automated feedback loops (Scott Wu; Eric Simons)
Code was the natural agent domain because running it gives verifiable feedback for RL. Verticals with deterministic, checkable outputs improve fastest; subjective domains such as law lag. Fails: domains without cheap verification.

### 28. Desirable, viable, feasible (Marily Nika; Marty Cagan)
AI product sits at the intersection of user desire, business viability and research feasibility. Marty Cagan: with probabilistic software, viability (legal, ethical, mission-critical) becomes the harder question and lands on the PM.

### 29. Business-process automation vs open-ended knowledge work (Sherwin Wu)
Software engineering is open-ended; most economic work is SOP-driven, repeatable and needs determinism and business-data integration. Look at support lines and utilities. Related: Bret Taylor, agents accomplish a job, so gains are self-evident and measurable.

## D. Reliability, interface and trust

### 30. Fault-tolerant UI (Gustav Söderström)
Design the UI around the hit rate. Steps: measure model performance; show roughly 1/hit-rate candidates; provide a very easy no-you-are-wrong path; revisit as quality improves. Midjourney's four-image grid. Varun Mohan: a 30% acceptance rate is fine because users learn which 70% to ignore.

### 31. Every nine is an order of magnitude (Jason Droege; Edwin Chen, Aishwarya Naresh Reganti)
POCs reach 60-70% fast; each extra nine costs about 10x more. Robust automation of an important process takes 6-12 months including legal, policy and change management (Droege); 4-6 months to real ROI (Aishwarya). About 74-75% of enterprises cite reliability as their biggest problem. Edwin Chen: 80% to 99% is a different problem. The 95% pilot-failure headline overstates it because most pilots are throwaway.

### 32. Squishy computer (Alex Komoroske)
LLMs roughly do what you meant. A product that fails badly 1% of the time is not viable if the failure is catastrophic; design the failure mode, not only the failure rate. Treat LLMs as duct tape, not autonomous oracles.

### 33. Jagged-frontier questions (Benedict Evans)
Can the user tell where it will work? Is it intuitive? Can they tell after it worked? Can they work out what to do with it? The product must answer for them. Tamar Yehoshua adds guardrails for chat: autocomplete, refinements, suggested prompts, education on non-determinism.

### 34. UI promise matches data quality (Noah Weiss; Guillermo Rauch)
LLMs sound confident when wrong. Match UI confidence to data confidence, show sources, design loops that create training data as a byproduct. Guillermo Rauch: show the AI's thinking so users can steer and bug reports get richer.

### 35. Algorithm vs human responsibility split (Adriel Frederick)
List the product's decisions, assign each to the algorithm or a person, define the framework people use. ML optimizes a given objective but not constraints or strategy; operational control is a first-order requirement; give operators information plus safe tools. Fails: pure consumer products that run unattended. Lyft's pricing algorithm had to be rebuilt for ignoring operational flexibility.

### 36. Chat, generated UI and the interface debate (Kevin Weil, Nick Turley, Alexander Embiricos, Amjad Masad, Jenny Wen, Michael Truell)
Chat is the catch-all for the unknown (Weil, Embiricos); natural language yes, turn-by-turn chat no, AI should render its own UI (Turley, Jenny Wen); chat lacks precision where users must point at things (Truell); agent vs assistant modes let users choose control (Masad); Aparna Chennapragada: the interface lags intelligence. Design for review, not authoring, when AI writes most output (Varun Mohan).

### 37. Autonomy ladder and proactivity (Alexander Embiricos; Dan Shipper, Kiriti Badam, Roman Ugarte)
Pair interactively, capture permissions and context, delegate longer tasks, then proactive work initiated by the agent, surfaced as mixed-initiative contextual actions where wrong suggestions are cheap to dismiss. Dan Shipper's measure: how long a leash you can give it. Autonomy moved from 15-30 seconds to 10-30 minutes unattended in about a year (Boris Cherny); Sherwin Wu expects day-long tasks in 12-18 months via the METR trend.

### 38. User control for agents (Nick Turley)
Give a visible view of what the agent is doing and confirmation on consequential steps; accept friction for trust (Waymo screen analogy). Sander Schulhoff notes human-in-the-loop is good now but unlikely to be the long-term answer.

### 39. Model is the product; ship to learn; listen after launch (Nick Turley)
Iterate on the model like a product: ship open-ended, observe real use, improve the model on those jobs. You cannot reason a priori about capability or demand; stop and listen after launch. Rahul Vohra and Chris Miller: ship speculative AI features and measure real usage, because predicted winners often underperform.

## E. Moat, market position and economics

### 40. Three segments of the AI market (Bret Taylor)
Frontier models (hyperscaler capex; Ben Horowitz's rule of thumb is $2B raisable before product progress), tooling (viable, ask why customers will not use the infra provider's feature), applied AI and agents (the startup opportunity).

### 41. Shovels, mine or middle (Matt MacInnis)
Make money selling the model or owning proprietary data. Apps that rent both need a durable insight. Related: Michael Truell, pick one area of knowledge work and build technology and product together; Ben Horowitz on the thin-wrapper fallacy.

### 42. AI and the seven powers (Hamilton Helmer)
No eighth power. Fixed model cost is scale economies; cross-user learning is network economies; a model that learns a user raises switching costs. Three technology plays: provider, enabled-new, incumbent user; AI's biggest impact is likely the third. Brian Balfour: moat is context and memory.

### 43. Where labs will and will not go (Logan Kilpatrick)
Labs build general assistants and agents, not verticalized products. Startups compete in domain verticals with fine-tuning and custom UI. Guillermo Rauch and Marc Andreessen back expert vertical tools; Mark Pincus warns AI chat is not yet a platform with third-party distribution.

### 44. Three-part utility of AI products (Mike Krieger)
Utility is model intelligence plus context and memory plus application and UI; all three must converge. AI is a data-management problem: about 90% of the effort is getting fresh, structured data to the model (Shaun Clowes); context engineering is at least half the performance (Dan Shipper).

### 45. Monetize from day one and the cost curve (Madhavan Ramanujam; David Singleton, Benedict Evans, Mark Pincus)
Inference costs and value capture force early monetization; otherwise you train customers to expect more for less. Agentic products tap labor budgets about 10x software budgets. Benedict Evans: marginal cost blocks the free-to-50-million playbook. Mark Pincus: design consumer services assuming tokens become nearly free.

## F. Security

### 46. Lethal trifecta (Simon Willison)
Agent with private data, exposure to malicious instructions and a way to exfiltrate is vulnerable. Steps: check each leg; if all three, cut one, usually exfiltration. Probabilistic filters and detection scores are a failing grade; assume anyone who can talk to the agent can make it do anything it is permitted to do. Normalization of deviance: each unsafe success breeds overconfidence.

### 47. Three-tier AI security decision (Sander Schulhoff)
Pure chatbot on the user's own data: no AI-specific defenses. Verify it really is only a chatbot by locking permissions the classical way. Agentic on untrusted data: architectural permission restriction (CaMeL-style) or do not deploy. Guardrails create false confidence; also run AI inventory and governance (find the 16 chatbots you did not know about).

## G. Organizing to run the bets

### 48. Diverge then converge (Tomer Cohen, LinkedIn)
Let teams explore broadly for a few weeks, accepting duplicate effort; write the playbook as you learn; then converge top-down on 4-5 bets reviewed weekly. Companion: let go of the roadmap, return to objectives, ask how the new technology achieves them better. Product leaders own the objective function, data and fine-tuning investment.

### 49. Dedicated prototyping team, then hand off (Paige Costello; Noah Weiss, Paul Adams)
Staff a small team outside normal process (skip the Double Diamond), then hand the starter hypothesis and prototype to the team with the deepest customer-problem expertise. Noah Weiss: central ML infrastructure plus parallel prototyping teams, later AI in every roadmap. Paul Adams: do not bolt AI on; teach everyone.

### 50. Embed product with research (Mike Krieger, Peter Deng, Tara Seshan)
At model companies, highest-leverage PM work is partnership with post-training and research; tie product bets to the research roadmap. Fails: teams using models off the shelf.

### 51. Three stages of enterprise AI adoption (Asha Sharma)
Make everyone AI fluent; apply AI to one existing process end to end and measure; then use proven approaches to inflect growth. Failure mode: many parallel projects with no blueprint, stack plan, measurement, observability or evals. Chip Huyen: AI strategy is use cases plus talent, top-down and bottom-up together.

### 52. Strategy clarity as AI speeds mistakes (Jessica Fain)
Faster building compounds mistakes faster; maintain a living shared strategy on problems, compute and dollars. Nikhyl Singhal: judgment about which changes to accept becomes the core skill as volume of proposed changes grows 10-100x.
