# Frameworks: agent-workflow

Every distinct framework or method behind the agent-workflow skill, grouped by theme. Each entry: what it is for, when it applies or fails, steps, benchmarks. Names are credited to the originator; other endorsers are noted.

## 1. Structuring agents and lanes

**One agent per lane of work** (Claire Vo, Claire Vo OpenClaw; endorsed by Roman Ugarte, Tomer Cohen) - Split work across narrowly scoped agents the way teams use separate Slack channels, so context stays small and tool access stays clear. *Applies when* one agent starts forgetting or losing tool access. *Steps:* list distinct lanes (work admin, family, sales, podcast, course); create one agent per lane with its own identity; let lanes intersect only when needed. Roman Ugarte adds: make agents long-lived and role-based with persistent memory, not a new chat per task, so you stop copy-pasting between chats. *Fails when* you cannot maintain many personal agents; see super-agent-first below.

**Super agent first, specialize downward** (Dan Shipper, Dan Shipper 2.0) - Roll out async agents top-down: one company-wide agent (for example data requests in Slack) owned by a forward-deployed engineer or equivalent, then specialized team agents, personal agents later as models need less hand-holding. *Applies:* companies of any size (Shopify and Ramp have company agents). *Fails:* personal agents that users will not maintain.

**Every agent needs a human who cares** (Dan Shipper) - Assign a named human owner to every agent; they review behavior, keep context current, treat maintenance as ongoing work. Related: **Automation is a lie** (Dan Shipper): every automation needs a human on top to keep it working. *Fails:* may relax as models get less fiddly.

**Specialized agents first, orchestrator later** (Tomer Cohen, Tomer Cohen 2.0) - Build narrow single-purpose agents so each can be rated and graded; add an orchestration layer so they collaborate (not just sequentially); hide the mesh behind one front door. Head-of-craft-built agents: each craft lead builds an agent encoding their expertise (a trust agent that reviews specs for harm vectors found everything the team had caught on an old spec plus holes missed). Growth agent: fund past loops, funnels and tests into an agent that critiques new ideas.

**Supervisor plus subagents** (Kiriti Badam, Aishwarya Naresh Reganti + Kiriti Badam) - Multi-agent systems split by function and communicating peer-to-peer are misunderstood and hard to control; a supervisor agent that delegates to subagents works. Also: *Society of models* (Amjad Masad) - different models per role (generation, manager/editor, critique, embedding); heavy engineering, only where it pays.

**Soul, heartbeat, schedule, memory** (Claire Vo) - An agent feels proactive because of four plain pieces: identity/soul file, cron-scheduled tasks, a heartbeat that checks its to-do every 30-60 minutes, and a memory file. Companion files: `tools.md` listing each tool and how you want it used; interview-style onboarding where the agent writes its own IDENTITY and SOUL files; voice-note onboarding (the Yapper API, Claire Vo).

**Shared machine vs partitioned machine** (Claire Vo) - Agents can share one computer if cross-access is harmless; sensitive lanes (family, personal email) get a physically separate device and accounts. A physical device is the hardest boundary. Roman Ugarte's own-computer agents: give every bot its own computer, especially for tools with weak APIs.

**Coding agent as administrator** (Claire Vo) - Install Claude Code or Codex on the agent's host, point it at the agent's config and docs, and ask it to fix errors or split memory between agents.

**API first, browser second** (Claire Vo) - Look for an API; if none, test browsing; if that fails, walk away and solve the problem behind the problem instead.

## 2. Working loop for coding with agents

**Plan mode** (Boris Cherny, Boris Cherny) - Start about 80% of tasks in plan mode, which only tells the model not to write code yet; iterate on the plan; then auto-accept edits and the model usually one-shots it. *Applies:* non-trivial coding with Opus-class models. Extended by **Plan.md before long agent tasks** (Alexander Embiricos): collaborate on a markdown plan with verifiable steps; verifiable plans make agents run much longer. Nicole Forsgren's variant: state architecture, stack and workflow, have the model design the plan, assign an agent to each piece in parallel with interoperability instructions, then evaluate.

**Ask the agent why it can't verify its work** (Alexander Embiricos) - Prompt repeatedly: why can't you verify your work, fix it. Loop until the agent can build, run tests and see results; then add integration harnesses. Max Schoening's **Human intervention is a bug**: treat every manual code edit as a flaw in the verification loop and fix the loop.

**Multi-Claude-ing** (Boris Cherny) - Run many sessions in parallel across terminal, desktop and mobile; check in only when one needs you. *Fails* on sequentially dependent tasks. Variants: Scott Wu's **Start your day by assigning five tasks to five agents** (Cognition engineers run up to five Devins at once); Sherwin Wu's **Engineer as tech lead of agent fleets** (10-20 parallel threads, steer them, never walk away); Lazar Jovanovic's multi-tab parallel building (only works if docs carry the context).

**Chop work into small spec-generate-review loops** (Michael Truell) - Specify a little, let the AI write a little, review, repeat; same total specifying time, far better results than one giant spec. Companion: **Background vs foreground agents** - send easily specified tasks with easy correctness (bug fixes) to background agents and pull them back to the foreground to refine.

**Give agents tasks, not problems** (Scott Wu) - Best on well-defined work that is fast to verify (front-end tweaks, bug fixes, tests, docs). Also **Treat the agent like a new junior engineer**: set up the repo, start with one-pointers, ensure it can run tests, lint and CI in its own environment, then scale. **Agent confidence levels and interactive planning**: the agent posts its plan, files and confidence before executing; humans answer async.

**Ask for the ambitious change, retry from scratch** (Benjamin Mann) - Outputs are stochastic; restart from the same prompt (optionally naming what failed) rather than patching a failed attempt.

**Use the most capable model; unlimited tokens first** (Boris Cherny) - The best model at max effort is often cheaper per finished task because it needs fewer tokens and less correction; do not cost-cut before an idea works and scales (then move to Sonnet or Haiku). Pair with **Do not box the model in**: give tools and a goal, drop scaffolding earlier models needed. *Fails:* high-volume simple tasks.

**Model per strength** (Zevi Arnovitz; Andrew Wilkinson's model per task) - Fast model for simple execution, Gemini for frontend, Claude as dev lead, Codex for the worst bugs; Gemini for huge documents. Strengths shift over time.

**Planner plus retrieval plus fast-edit model** (Varun Mohan) and **Model + API + harness stack** (Alexander Embiricos) - For teams building agent products: capabilities like compaction need changes across model, API and harness. Kevin Weil's **Ensemble of specialized models**: decompose into narrow tasks, pick a model and prompt per task.

**Slash-command PM build workflow** (Zevi Arnovitz) - Encode the build process as saved commands: create-issue (capture to Linear via MCP), exploration (agent reads codebase and asks questions), create-plan (TLDR, decisions, status-tracked tasks), execute-plan, review and peer-review (cross-model), update-docs. *Fails:* not ready-to-build tickets at large companies. Companion: **Claude.md as workflow system prompt** (write how you work, add 'challenge my thinking' for exploration) and **Update docs after each feature**.

**PRD doc stack** (Lazar Jovanovic) - Masterplan, implementation plan, design guidelines (include CSS specifics), user journeys, then tasks.md as execution source of truth; agents rules file says read all docs, take the next task, report what was done and how to test; prompt afterward with a short proceed. Companion: **Post-fix prompt retro** (ask how you should have prompted to fix it in one go; put the answer in the rules file). *Fails:* pure exploration, where vibing is fine.

**Thin starting template** (Simon Willison) - Agents copy patterns already in the repo; start projects from a thin template with your layout and one trivial test instead of long instruction files. Also **Combine existing code examples**: point the agent at the source of two past tools and ask for a new one combining them.

**Compounding engineering** (Dan Shipper) - For every unit of work, make the next easier: write the prompt for the platonic ideal of an artifact (a PRD from rambling), save it as a slash command in a shared repo, keep refining. Companion: **Don't repeat yourself goal** - codify repeated feedback into prompts so people get a simulation of you before they reach you.

## 3. Autonomy, trust and calibration

**Agency-control trade-off** (Aishwarya Naresh Reganti) - Each increment of decision-making autonomy given up is control relinquished, so autonomy must be earned through demonstrated reliability. Decide what the AI may decide, start with high control and low agency, increase only as it proves reliable.

**Start with high control, low agency, then ladder up** (Kiriti Badam; Aishwarya Naresh Reganti) - V1 AI suggests and humans decide; V2 answers shown directly; V3 actions such as refunds. Maps to coding assistants (inline completion, larger blocks, autonomous PRs) and marketing (draft, run campaign, auto-optimize).

**Customer support agent agency ladder** (Aishwarya Naresh Reganti) - V1 routing (reveals messy taxonomies), V2 copilot drafts (logging human edits is free error analysis), V3 end-to-end resolution when drafts are used mostly as-is. Kevin Weil's **Human-in-the-loop support flywheel** shows the endpoint: auto-answer when confident, suggest to a human when not, feed human answers back as fine-tuning data.

**Continuous Calibration, Continuous Development (CCCD)** (Aishwarya Naresh Reganti) - Development loop (scope capability, curate data, set up, design eval metrics, deploy) plus calibration loop (analyze behavior, spot recurring error patterns, fix, add metrics only for recurring patterns), repeated at the next higher-agency version. A new data distribution can appear even at V3. Related **Behavior calibration**: you cannot predict how the system will behave, so keep the experience safe, constrain autonomy by action count, topic or risk, and log what humans do.

**Constrain autonomy by risk** (Aishwarya Naresh Reganti; Anish Acharya's risk gate) - Classify cases by risk; AI auto-handles low-risk (pre-authorizing routine tests), humans handle high-risk (invasive surgery). Anish Acharya's **Business loops**: map the recurring workflow (input, decision, action, measurement), turn it into an agent loop with a risk gate, stack loops across functions.

**Progressive trust ladder** (Claire Vo) - Calendar only, then read email, then draft, then send, then attend meetings. **Onboard the agent like an employee**: own email, calendar and local account, delegated access, secrets through a password manager. **Human-in-the-loop carve-outs**: the agent owns routine segments end to end, escalates high-value ones, and rules are tuned by telling it.

**Agent calls a human, human coaches, traces become training** (Anish Acharya; Jason Droege on training agents to escalate at low confidence; Eric Simons's human expert escape hatch) - Let the agent escalate when stuck, capture the coaching, ask what do you know that the model does not.

**Legibility test for agent candidates** (Jeanne DeWitt Grosser) - Start with workflows you can write down, that are replicable and mostly deterministic (inbound lead qualification), then low-end outbound; use agents for research only in complex enterprise accounts. Vercel result: 10 inbound SDRs became one agent QA reviewer with conversion flat. Build workflow-specific agents in-house; buy generalizable ones.

**Do not default to an agent / Jobs-to-be-done map for agents** (Aishwarya Naresh Reganti; Evan Spiegel) - Map the workflow, mark steps ripe for AI vs human, choose ML, code or LLM per step; list the jobs to be done and build cross-functional teams around the jobs agents can do.

## 4. Context, memory and documentation

**Agent failures are context failures** (Sherwin Wu; Bret Taylor; Claire Vo's agent failures are structural) - Missing or underspecified context is the usual cause; encode tribal knowledge as docs, comments, structure, .md files and skills; root-cause every bad output and fix the context, not the single output. Sherwin Wu's **Remove the escape hatch experiment**: a bounded team with a 100% agent-written codebase surfaces the real blockers.

**Constant postmortems on AI mistakes** (Zevi Arnovitz) - Ask the agent what in its prompt or tooling caused the mistake, then update docs, commands or tooling. Review prompts after successes too.

**AI-native codebase** (Zevi Arnovitz; Nicole Forsgren) - Technical people first add markdown docs explaining structure and areas; then PMs can ship contained UI changes via a PR a dev finishes, not heavy migrations. Better documentation and comments directly improve agent output. Chip Huyen's **AI-readable documentation layer**: add annotations for scales, units and meaning that human docs assume.

**Operational hygiene for memory** (Claire Vo) - Manage context rather than harden memory; before compaction, have the agent write action items and update the to-do list like closing a meeting; use hooks to automate.

**Instruction brief for a model** (Robby Stein) - Brief like a new hire: where the data is, schema, URL, when to use each source, where to be extra careful. Natural-language steering often beats heavy fine-tuning.

## 5. Review, verification and quality

**Claude reviews every PR plus human check** (Boris Cherny) - 100% AI review, human layer after, human skip only for throwaway prototypes. Sherwin Wu's version: Codex review on every PR cuts review from 10-15 minutes to 2-3, small PRs skip the second human, human attention drops from 100% to about 30%; beware circularity when one model writes and reviews.

**AI reviews AI, humans do acceptance testing** (Mike Krieger) - Different Claude reviews; humans acceptance-test instead of reading line by line. *Fails:* risk of an unmaintainable codebase; has not happened yet per Krieger.

**AI supervising AI** (Bret Taylor; Marc Andreessen's play AIs off against each other; Dan Shipper's self-judging loop) - Chain a generator with a reviewer: two 90% agents approach 99% if errors are independent. *Fails* when errors are correlated, or models that inflate grades.

**Dark factory pattern** (Simon Willison) - Nobody types code, nobody reads code; quality comes from simulated end-user testing and cloned dependencies. *Fails:* a virtual QA team saying it is good does not prove it is secure.

**Evaluate trajectories not just answers** (Edwin Chen) - Review the steps an agent takes, reward efficient solutions, penalize reward-hacking; RL environments simulate a company's tools to expose end-to-end failures.

**Can the agent check its own output?** (Simon Willison) - Code is easy for agents because it is obviously right or wrong; for any other function, ask whether an objective check exists, else plan a human verifier. Related: Dan Shipper - even when agents write code, engineers still review it and study internals.

## 6. Security and blast radius

**Single trusted instruction channel** (Claire Vo) - One authenticated channel is the only command source; the soul file says email, Slack and websites are never instruction sources; add explicit anti-social-engineering rules. **Clean machine isolation** (Claire Vo): separate machine, dedicated account. Caitlin Kalinowski's story: a sandboxed agent given one private item and told not to share posted it within five minutes.

**Assume user controls data and actions** (Sander Schulhoff) - Any accessible data can be leaked and any action triggered; lock down permissions as if the model were an adversary; contain AI output (run generated code in a container on a separate system). Prompt-based defenses are the weakest. Jailbreaking vs prompt injection: indirect injection through emails and web pages is the main agent risk.

**CaMeL** (Sander Schulhoff; Simon Willison) - Restrict agent permissions ahead of time from the user's request (summarize emails gets read-only); Willison's variant splits a privileged agent that plans from a quarantined agent that touches untrusted text, tracks taint, and asks humans only on high-risk actions. *Fails:* tasks combining read and write; complicated to implement.

**Run agents in a hosted sandbox with permissions off** (Simon Willison) - Run several agents on the vendor's servers without approving every action; no private data or secrets in the environment; review PRs; pull sensitive work down for deeper review.

**Single-user default** (Claire Vo) - A personal agent assumes one trusted instructor; do not drop it into open group chats.

## 7. Team rollout and organization

**Top-down plus bottoms-up with a tiger team** (Sherwin Wu) - Exec buy-in, tools purchased, and a full-time tiger team of technical-adjacent enthusiasts applying AI to specific workflows, running hackathons and sharing. Top-down mandates alone likely produce negative ROI. Last-mile work intricacies can only be solved by the people doing the work.

**Head of AI Operations** (Dan Shipper) - One curious, process-oriented person turns repeated work into prompts, workflows and small apps; weekly meeting logs repetitive tasks; adoption needs a behavior change, not just a tool. Dan Shipper's **AI adoption rollout playbook**: AI-first memo (say it was written with ChatGPT), weekly prompt-sharing, usage stats emails naming contributors; **10/80/10 adoption split** and role-specific training (about 4 weeks, one hour a week).

**Platform, tools and agents, culture** (Tomer Cohen) - Three investments for AI-native building at scale: re-architect platforms so AI can reason over them, build or customize agents per craft, invest in culture and change management. Pilot with early-adopter pods who must give feedback; announce the mountain, report progress; do not run a small team on the side while the org wonders. Third-party tools never worked off the shelf on the LinkedIn stack.

**Executive dogfooding and CEO usage** (Dhanji R. Prasanna; Dan Shipper; Howie Liu) - CEO and exec daily use is the best adoption predictor; Howie Liu watches hourly use or inference spend. Brian Balfour's **Hard constraints** (cap function size, prove AI cannot do the work before headcount, no PRD without three prototypes) and warning that execs are disconnected from real adoption.

**Mini-PM two-week rule** (Amol Avasare) - Projects of two engineering weeks or less: engineer owns PM duties and PM advises; above two weeks PM stays accountable; one-week controversial projects stay PM-driven. Companion: **PM leverage at scale** - improve the why and what by even 5% rather than shipping the 21st feature.

**Conditions for fluid roles** (Elizabeth Stone) - Role fluidity needs source-of-truth data, production guardrails, clear trust boundaries, humans accountable for output. *Prototype yes, ship to production no.* Max Schoening: PMs and designers code to master the material, steer them to terminal agents, and keep **playground prototyping** in a small agent-friendly codebase. Julie Zhuo: builders not roles (60th-70th percentile in adjacent skills, specialist review). Tomer Cohen's **Full Stack Builder** model and five human traits (vision, empathy, communication, creativity, judgment).

**New bottlenecks when AI writes the code** (Mike Krieger) - Upstream decision-making and alignment; downstream merge queues and review. Provide a minimum viable strategy; re-architect the merge queue. Varun Mohan's **Amdahl's Law for AI productivity**: if writing is 30 of 100 time units, speeding it up gives about 27%; Windsurf sees 30-40%. Always-on agents (Dhanji R. Prasanna): push session length from minutes to hours; a wishlist of ten well-described features succeeds on roughly 60%.

## 8. PM and personal productivity with agents

**Three steps to start with Cowork** (Boris Cherny) - Use a tool, connect tools, run many tasks in parallel. Cat Wu: connect calendar, Slack, email and Drive first; spend about 30% of PM time pushing tool limits; keep setups simple.

**Scheduled PM agents** (Amol Avasare; Andrew Ambrosino; Fiona Fung; Tamar Yehoshua) - Weekly misalignment scan over Slack; morning review of 20-25 dashboards (track false positives); daily brief from Slack with plain-language coaching; overnight feedback-to-PR routine; feature launch status prompt giving a date, open issues and a confidence level. Boris Cherny's Cowork project management: a status sheet and a Monday agent that pings those who have not filled it in.

**Automate the product operating system and obsolete yourself** (Nikhyl Singhal) - Automate product reviews, standups and status reports from ground-truth sources; build tooling that keeps you on top of many engineers rather than shipping as the 51st engineer; ask of every repeated task whether an agent can do it.

**Infovore chief-of-staff ladder** (Roman Ugarte) - V1 daily roundup from Slack and email with your role and rules; add firehoses; connect a QA bot; allow paging only when false positives are near zero. **Email triage agent chain** (Andrew Wilkinson): skip, flag for 24 hours, multiple-choice replies, send.

**AI as thought partner, human first** (Marty Cagan, Dianne Penn, Wes Kao, Mike Krieger, Adam Mosseri) - Think first, then have the model challenge; give your point of view and ideal outcome; ask it to be brutal; choose models that push back; enumerate inputs when asking for strategy. **Human sandwich** (Molly Graham): human sets direction, AI does the middle, human reviews. Molly Graham's **Legos you should not give to AI**: judgment, trust, relationships, vision, anything where you cannot define good. Claire Vo: for each task, delegate at 80% quality or give a skilled person a toolkit for 3-10x.

**Learning with agents** (Sam Schillace; Dharmesh Shah; Michael Truell; Simon Willison; Fiona Fung; Nikhyl Singhal) - Pick a concrete, even arbitrary, goal; fall on your face in a safe side project; keep a backlog of tasks AI could not do and retest on each model; find your first moment of joy with a small personal tool. Hilary Gridley's 30 days of GPT is a habit tool, not education.

**Demo, don't memo** (Lazar Jovanovic; Howie Liu; Amjad Masad; Andrew Ambrosino) - Build a prototype in about 30 minutes and hand it to engineers as the spec; share artifacts instead of docs; the shared language is working prototypes. Andrew Ambrosino's **Inverted product process**: implementation is cheap, taste and curation of many attempts is the scarce work. Max Schoening: the first 10% is free, the last 10% is still 90% of the work.
