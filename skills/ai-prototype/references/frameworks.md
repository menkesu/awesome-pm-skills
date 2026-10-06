# Frameworks: AI Prototype

Every distinct method from the 44 guests in this skill, grouped by theme. Each entry: what it is for, when it applies or fails, steps, benchmark.

## A. Starting and planning

### Parallel multi-fidelity starts (Lazar Jovanovic, episode: Lazar Jovanovic)
Start several projects at increasing clarity instead of staring at a blank page. **Applies:** any new project with only a vague idea; tools have free tiers so cost is low. **Steps:** (1) brain-dump the vague idea by voice and send it without waiting; (2) open a second project with a clearer feature/page list plus a reference screenshot from Mobbin or Dribbble; (3) open a third with code snippets from a library like 21st.dev; (4) compare the 3 to 5 concepts and continue with the clear winner. **Why:** restarting from a clearer concept costs a little up front but saves hundreds of credits and days versus patching a weak first direction. Mark Pincus and Dhanji R. Prasanna endorse the same parallel instinct.

### 80/20 plan-to-execute split (Lazar Jovanovic)
With AI builders the bottleneck is clarity, not coding. **Steps:** use chat/plan mode first; execute only once the plan is explicit; optimize for the kind of speed that is clarity. **Applies:** Lovable, Cursor, Claude Code, anything where output is far faster than your thinking. Zevi Arnovitz agrees for complex work. **Fails/contrast:** Amjad Masad and Anton Osika often start minimal (see Minimalist vs PRD-style prompt).

### Lovable PRD generator GPT (Lazar Jovanovic)
A custom GPT that interviews you after a brain dump and outputs four planning files. **Steps:** open ChatGPT and find the generator; brain-dump; answer its clarifying questions; upload the four files into your builder. **Applies:** starting a new AI-built project when you do not want to hand-write planning docs.

### Sketch first, then vibe code (Jake Knapp, episode: Jake Knapp + John Zeratsky 2.0)
Treat detailed pencil sketches as your prompt engineering. **Steps:** sketch screens and flow on paper with intentional detail on what the customer needs to know and see; use the sketches as the plan for vibe coding; combine vibe coding, real code and a product video so the whole thing need not work freeform. **Applies:** technical or AI-centric products where depth matters. **Contrast:** co-designing with the LLM through chat yields a more generic result. Bob Baxley's primal mark argues similarly.

### Prototype fidelity map: outsource prototyping, not thinking (John Zeratsky)
Prototypes are simulations that answer a key question. **Steps:** do the Foundation Sprint thinking first (copy, how the product is described, how it differs); identify the key question; mark each part real, vibe coded, or static mockup/video; use AI to build the simulation quickly. **Fails:** vibe coding at the very start produces believable but generic results, because LLMs are trained on existing products.

### Fork from community (Guillermo Rauch, episode: Guillermo Rauch)
Beat writer's block by forking a close community project and prompting modifications. **Steps:** browse the gallery; fork the closest match; prompt changes to make it yours. **Applies:** new users of AI builders.

### Minimalist vs PRD-style prompt (Amjad Masad; Anton Osika)
Two valid styles. Minimalist: a vague idea or even two words (an Airbnb clone), review the output, iterate with specific follow-ups. PRD-style: describe the app type and audience, list core features (submission, voting, status columns, admin controls), optionally specify the stack. **Applies:** first-version prototypes and internal tools. **Fails:** large later iterations (database migrations) can hit unrecoverable errors.

### Prompt like a ticket (Eric Simons, episode: Eric Simons)
Write the prompt as you would a Linear or JIRA ticket. **Steps:** specify what matters; leave creative latitude elsewhere (for example make it prettier); take time to craft the first ask. **Applies:** PMs using Bolt and similar tools.

### Describe the end-user experience, not the implementation (Guillermo Rauch)
State the experience and goals; stay open to the tool knowing more than you. Rauch's fitness function of trying wild ideas daily (a flight tracker with a canvas overlay in under two hours on a $20 plan) shows the payoff.

### Context is all you need (Logan Kilpatrick) and Genie with three wishes (Lazar Jovanovic)
Two limits: the model has a finite token window and no context about you. **Steps:** say who you are, what you do and your goal; paste the documents or links instead of relying on training data; be specific, since AI does not understand 'you know what I mean'; provide the references. Lazar adds that the ceiling on output is what the model sees before it acts.

### Brain-dump then refine (Dr. Becky Kennedy; Lazar Jovanovic)
Dump all thoughts into the AI without organizing, turn them into something visual (a UX flow, a full email flow), then refine, and do not be attached to the artifact. If you lack vocabulary, switch to chat mode and ask the tool to help you prompt it better. **Fails:** teams may prefer hearing the idea before seeing a finished version.

### Few-shot examples and role framing in prompts (Kevin Weil)
Poor man's fine-tuning: write several example inputs with ideal answers into the prompt, then give the real problem. Role framing: open with a persona such as the world's greatest brand marketer. **Fails:** will not match a real fine-tune; limited by context size. Logan Kilpatrick notes tiny prompt tweaks only add roughly 1 to 2 percent, so do not over-invest.

## B. Building

### Experience first, then make it real (Guillermo Rauch; Anton Osika)
Work front end first, then add performance and backend without prescribing tech. **Steps:** UI from a short prompt; iterate design; connect a backend as a service; prompt login; let users upload and edit data; deploy; describe performance problems rather than the fix.

### Screenshots and precise inline prompts (Guillermo Rauch)
Paste screenshots of your own boards, Figma or Slack posts to generate or restyle UIs. **Steps:** paste screenshot or attach Figma; refine with inline prompts such as center this; apply a second screenshot as a style reference; ask for added functionality. **Fails:** not for cloning other people's sites.

### Code snippets as the reference (Lazar Jovanovic)
These tools interpret code better than English. **Steps:** find a library that exports code (21st.dev); attach the snippet; ask for exactly that design or functionality. **Applies:** design-heavy UI.

### Style prompts (Andrew Wilkinson)
Give a big business-details document, ask for a web app or site, then steer design and copy with style lines (Stripe design, a named writer's tone). He finds Replit the most functional; Lovable and Bolt may need fiddlier deployment.

### Visual editing for small tweaks (Anton Osika)
Select the element in the preview and edit text or color directly; reserve prompts for larger changes.

### Fictional-persona test data (Alex Komoroske)
Write a short backstory of a fictional user; have the LLM generate schema-fitting data consistent with their world. **Applies:** demos and prototypes needing realistic data.

### Scope down for large codebases (Guillermo Rauch)
LLMs struggle to reason over very long context. **Steps:** break work into components and files; give a smaller task on a specific file. Eric Simons adds that models get unreliable beyond roughly a thousand files: use text-to-app tools for greenfield and for admin or marketing surfaces, and Cursor with a developer for large codebases.

### Prototype by chatting (Asha Sharma)
Plain-language chatting with a prototyping tool can give a more expressive prototype than hand-coding. **Applies:** early concept prototypes.

### Round trip between prompt and hand-tweaking (Dylan Field)
AI output is a starting point. **Steps:** prompt for a first pass; bring screens into a design tool to tweak by hand; bring that context back into the AI tool; expose via MCP so the tool is not the only destination.

## C. Debugging and getting unstuck

### Four by four debugging (Lazar Jovanovic)
When stuck, escalate through four different approaches, each tried only once. **Steps:** (1) the agent's try-to-fix button; (2) awareness layer; (3) external diagnostic tool; (4) revert a few steps, rethink the prompt, take a break; afterwards ask the tool how to prompt better and record the lesson in rules.md. **Applies:** non-engineers on Lovable, Cursor, Claude Code. **Fails:** when the thing is not yet technically possible.

### Awareness layer (Lazar Jovanovic)
Agents fix what they are aware of. **Steps:** run the broken function in preview; read the browser console; ask the agent to add console logs along each step; rerun; paste the full log into chat. Lazar says this is enough 99 percent of the time. **Applies:** third-party integrations where the agent cannot see the failure.

### External diagnostic consultant (Lazar Jovanovic)
**Steps:** export to GitHub and import into Codex, or compress with Repomix and upload to Claude or ChatGPT; describe what you are building, the problem and the logs; take the diagnosis back to the original tool. Never let the unfamiliar tool edit code.

### Escape hatch to another AI (Guillermo Rauch)
After many iterations, copy the generated code into another strong reasoning model; use Git to make it a hybrid prompt-plus-code project; keep code visible so you can drop to traditional engineering.

### Revert and re-prompt (Lazar Jovanovic)
When the bug is your own bad prompt, go back a few steps in version history and retry with a clearer prompt; small stumbles often vanish.

### Just try something else (Guillermo Rauch)
Treat the tool like an agency or engineer you coach. Say try something else when output is stuck and describe the experience rather than prescribing.

### Chat mode to understand and unstick (Anton Osika; Lazar Jovanovic)
Ask how things work, what you may be missing, what to do. It unblocks you and teaches you how software is built.

### State expected vs actual (Anton Osika)
Say exactly what you expect, which parts work and which do not. This matters even more with AI than with human teammates.

### Know the cliffs (Amjad Masad; Eric Simons; Michael Truell)
Builders shine at v1 and early users but can break on large iterations such as database migrations (Masad, 2024-era capability); reliability drops beyond roughly 1000 files (Simons, early 2025); and vibe coding without understanding the details leaves you with something too big to change (Truell). Fallbacks: ChatGPT or Claude debugging, a human coder, or an engineer.

## D. Tool choice and builder growth

### Graduated ladder into coding tools (Zevi Arnovitz, episode: Zevi Arnovitz)
Treat code as exposure therapy. **Steps:** chatbot project; Bolt or Lovable; Cursor in light mode; terminal tools like Claude Code; graduate when you outgrow each (for example when adding payments).

### Harness tradeoff (Zevi Arnovitz)
Bolt, Lovable, Replit, Base44 and v0 use the same models as Claude Code but add a harness that removes decisions (database, auth). You gain ease and lose control; move to Cursor or Claude Code when you want those decisions or cutting-edge model ability. Code is just files, so you can carry a project between tools.

### AI CTO project (Zevi Arnovitz)
A chat project whose custom prompt makes the AI the technical owner: you own the problem and how users should feel, it owns how it is built, and it must challenge you. Use for architecture decisions before coding; voice mode helps ideation. **Fails:** default chat sycophancy outside such a project.

### Learning-opportunity command (Zevi Arnovitz)
A slash command that tells the agent you are a technical PM in the making and asks for an 80/20 explanation of what you are working on.

### Read the agent output, not the code (Lazar Jovanovic)
Learn what is possible and the vocabulary by reading what the agent says it did after each action; use chat mode for feasibility. Treat the tool as technical co-founder and educator.

### Positively delusional beginner's mind (Lazar Jovanovic)
Assume everything is possible until proven wrong, then ask the agent in chat mode whether it really is. Nikhyl Singhal agrees you need to be opinionated, not an engineer.

### Models as people (Zevi Arnovitz)
Treat each model as a persona (Claude the communicative opinionated lead, Codex the silent elite coder, Gemini the erratic design scientist) and assign roles. Cross-model review lets non-engineers check AI code.

### Stress-test the tool (Guillermo Rauch; Alexander Embiricos)
Rauch tries something wild daily to find what the tool cannot build. Embiricos: evaluate a coding agent on your hardest scoped task, align on the codebase and a plan first, then execute bit by bit.

## E. Prototype strategy and rigor

### Failure machine (Mark Pincus)
Use AI to test a hundred ideas a day. **Steps:** assume the current version is the wrong product; build it wrong in a day or a week, just good enough for signal; test pieces separately, such as ads or messaging; iterate across many ideas.

### Parallel overnight experiments (Dhanji R. Prasanna)
Describe several experiments in detail, let agents build them overnight, throw most away in the morning. **Benchmark:** about 60 percent success on well-described features; the other 40 percent needed intervention.

### SoloWare (Dharmesh Shah, episode: Dharmesh Shah)
Software for exactly one user, you. No UI polish, minimal testing, shut it off at will; productize only if useful enough to be worth the calories. Chip Huyen's micro tools are the same idea: build small tools that remove personal friction.

### Vibe coding vs agentic engineering (Simon Willison)
Ask who gets hurt if the code has bugs. Only you: vibe code freely. Other people: apply review, tests and security thinking. Knowing what is responsible is itself an expert skill, for example a scraper that hammers someone's site. Edwin Chen is skeptical that vibe coding stays maintainable.

### Prototype first, spec second (Elena Verna, episode: Elena Verna 4.0)
Keep the written spec but attach a Lovable prototype others can click and edit; screenshot an existing page, recreate it with changes, hand it to engineering. Building reveals what is important and kills weak ideas early. Eric Simons, Kevin Weil (vibe-coded demo in about 30 minutes instead of Figma), Aparna Chennapragada (demos before memos), Dylan Field (prototypes beat static mocks, mocks beat words) endorse.

### PM-built v0/v1 then hand to engineering (Amjad Masad; Mike Krieger)
PM or designer builds a functional demo, tests with users, then engineers structure the real change. Prototyping moving earlier is the biggest role shift (Krieger); structuring backend and frontend remains engineering skill.

### Foundational AI prototypes of core screens (Albert Cheng)
Build AI prototypes of onboarding, home and core experience so anyone can layer ideas on top. **Fails:** interoperability between PM, design and engineering AI tools is weak, so handoffs remain.

### Prototype to build informed gut (Tony Fadell)
Make many prototypes to sharpen direction, then architect it explicitly and have AI work on limited-scope pieces. **Fails:** treating the prototype as the production foundation (Sam Lessin: vibe coding does not scale on its own).

### No AI for the MVP (Marily Nika)
Fake the AI with a Figma prototype to show users and get buy-in; invest in a model only with your own or adjacent-product data.

### Prototype on the real model for AI products (Jenny Wen; Karina Nguyen)
Non-deterministic output means you cannot mock all states or build a faithful clickable prototype. Use the real model, watch real users, design around discovered use cases. Nguyen: a prompted demo of 100K-context file upload convinced people to ship it. **Fails:** deterministic products.

### The primal mark (Bob Baxley)
Wait as long as possible to draw: the first realistic artifact becomes the baseline everyone anchors on. **Steps:** stay conceptual; when something looks promising, table it and ask what else; reach a second, third and fourth idea in one meeting; then draw. AI prototype tools are a production tool once the idea is formed.

### Get it into users' hands (Gaurav Misra)
Designs that look good in perfect conditions are not always useful in use; prototypes in users' hands beat design review.

### Economics benchmarks (Eric Simons; Jonathan Becker)
A greenfield CRM with AI and Stripe took three weeks and about $300 versus a $30K, six-month agency quote (not zero-shot; expect days to weeks of iteration). Rough creative mockups can take about 1 percent of the former time. Tomer Cohen: invest hours up front learning the tools before velocity improves.
