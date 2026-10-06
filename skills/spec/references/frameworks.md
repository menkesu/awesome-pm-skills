# Spec: Frameworks

Grouped by theme. Each entry: originator and episode, what it is for, when it applies or fails, steps, benchmarks.

## A. Shaping (Ryan Singer, Shape Up)

**1. Framing / setting the boundaries** (Ryan Singer, Ryan Singer episode). Narrow a request that arrives as a noun (calendar, dashboard, newsletter builder) into a specific problem worth spending time on. Applies whenever a generic request lands. Fails if the problem stays fuzzy: shaping becomes endless. Steps: refuse to build the generic thing; find the specific pain behind repeated requests (e.g. seeing empty spaces); agree the narrowed problem is worth the appetite; hand the frame to the shaping session.

**2. Shaping session** (Singer). A live whiteboard session: a senior engineer who knows the system, a product person with the backstory, and a designer, working until a version emerges that they believe fits the time box. Fails if product and design shape alone and show engineering later. Steps: bring the engineer who knows what is easy and hard; bring the product person who knows why this is an opportunity; add a designer; whiteboard together.

**3. Breadboarding and fat marker sketching** (Singer). Communicate the solution at the level of buttons, flows and calculations. Must genuinely communicate the idea, not be a blurry Figma. Fails when it is a generic wireframe (dashboard here, four reports). Steps: sketch the flow (hit this button, go here, this calculation runs, then a choice); keep detail where the team moves fast but sees something real; check the sketch tells a builder what to build.

**4. Fewer than ten moving pieces** (Singer). Benchmark of concreteness: a well-shaped solution is describable in fewer than about ten moving pieces (the calendar example: a two-month dot grid, an agenda view beneath, navigation, a create button). Steps: list the pieces; if more than ten it is not shaped; check against the narrowed problem and time box.

**5. Shaped output test** (Singer). Show the sketch to a technical person and ask if they know exactly what to build. User stories and generic wireframes fail it. If no, keep shaping.

**6. Detail dial** (Singer). The right amount of detail depends on who builds. Juniors get more implementation guidance, trusted seniors less, and engineers who want input on fundamentals join the shaping. Dial back over successive projects. Fails: over-specifying for seniors feels like being told what to build.

**7. Try to break the idea** (Singer). Draw an idea; the technical person looks for why it will not work; product plays through the customer scenario; step back and draw a very different idea B; note the 'what abouts' (e.g. multi-day events) and spike them. Do not polish one idea for hours.

**8. Shaping session cadence** (Singer). About three hours per session; a clear problem on existing technology can usually be shaped in about three sessions, with breaks to sketch and spike. Fails for inventing new technology or AI models.

**9. Diagnose overruns: is an engineer in the picture?** (Singer). When a team says Shape Up did not work, ask to see their shaping work. If it is a PRD or Figma files with no engineer involved, bring the best-suited engineer into product for shaping.

**10. High-fidelity artifacts hide the wall** (Singer; contrarian). Long PRDs and polished Figma files made without engineering hide what is under the UI, causing a reality check later. Figma is fine once the underlying shape is settled. Singer also argues the dominant real-world failure is not enough detail, not too much.

## B. Working backwards and PR/FAQ

**11. PR/FAQ** (Bill Carr, Bill Carr episode; originator at Amazon). A short internal press release: first paragraph the product, second the customer problem, third the solution, backed by data not hyperbole, plus a data-rich FAQ. Steps: headline that says what it is; hypothetical launch date (signals simplicity or complexity); the specific customer; the specific, ideally quantified problem; the solution; FAQ. Used to decide what to build and choose between competing ideas. It is not a real press release; do not use that language.

**12. Document the big idea before debating it** (Carr). Unwritten big ideas get debated as concepts, so decisions default to politics or top-down will. Steps: document the idea; assign an owner to investigate; build only if it survives. Applies to orgs stuck in the thinking-to-doing gap.

**13. Amazon mock press release** (Jag Duggal). Before any engineer is assigned, write two paragraphs to the intended customer on why they should care. If you cannot do it crisply, the idea is not ready.

**14. Write the press release first** (Carilu Dietrich). At ideation, product and marketing agree on a coherent theme instead of marketing receiving a bag of doorknobs. Steps: write the release before building; negotiate whether it resonates and is the wanted outcome; build to it.

**15. Working backwards from the machinery on launch day** (Anuj Rathi). Working backwards also defines the GTM machinery and date. Steps: one-page release with date, value proposition and quotes; take the date to engineering to test if too aggressive; use the customer quote to ask marketing and pricing whether they can deliver what customers will say; use the business-owner quote to confirm targets (e.g. three-month goals); if someone disagrees, adjust date and goals together.

**16. FAQ as process checklist** (Anuj Rathi). Hard-wire company-specific checks into the FAQ: mandatory compliance and legal sign-off at a fintech; for marketplaces, implications for each side (restaurants, each delivery-partner segment).

**17. GACCS marketing brief** (Emily Kramer). Before big marketing projects: Goals, Audience, Creative (what makes it stand out), Channels, Stakeholders (DRI, approvers, contributors). Share with product up front for early buy-in.

## C. Document design and review mechanics

**18. Two-way writeups** (Lane Shackleton, Lane Shackleton episode; originator). Feedback, discussion and sentiment are part of the content. Beats one-way six-pagers with comment margins. Steps: done-reading button at the end; question table people upvote; sentiment table where each person rates the proposal; run the discussion off top-voted questions and the sentiment spread. Applies to cross-functional proposals in collaborative-doc companies.

**19. Dory (question table)** (Shackleton). Put reader questions in a table that people upvote so the facilitator addresses the most important one instead of scanning comments in the last 20 minutes.

**20. Done-reading button** (Shackleton). Tells you who has read it, replacing the habit of watching for an SVP's avatar in the doc.

**21. Crisp doc, messy meeting** (John Mark Nickels). Write a crisp narrative (Amazon-style), then use the meeting to pick it apart and debate rather than present.

**22. Write, then cut almost all of it** (Ami Vora). Write everything you need to think it through, then cut to the minimum for a clean recommendation. Format: looked at the data, three analyses suggest X, one suggests Y and we think it is inaccurate or worth the risk; close with any objections, any new context? Forces opinion over hiding behind analyses.

**23. Qualified problem statement** (Christopher Miller). Label the problem business, customer or efficiency; for a business problem ask why it has not solved itself to find the customer problem; list assumptions and predicted downstream effects; why-why-why to justify direction, what-what-what to size blast radius. For growth specs and experiment docs.

**24. Specific problem statement before launch** (Tomer Cohen). In product jams spend real time on a nuanced problem definition (not 'launch a video product' but what kind of video, which audience, what unique criteria) so the team sees the whole path up the mountain; solution follows first-principles opinions.

**25. Why-now one-pager** (Maggie Crowley). Open with background and context: the problem, why it matters, why it matters now. Keep a running dated list of decisions, descopes and links to research. Bring it to the team early and ask smart people to attack it.

**26. First principles section** (Nickey Skarstad). Add a second-order impact line to spec templates; write first principles (what we care about, why, what matters less); run a brainstorm on how changes cascade. Aligns teams before design. Best for marketplaces and complex systems.

**27. Success metric and growth lever in every ticket** (Hila Qu). PMs write the success metric and the growth lever (acquisition, activation, retention, monetization) up front; the exercise often kills low-value work.

**28. Product review template** (Brian Tolkin, Opendoor). Context, problem statement and jobs to be done, potential solution, risks and pre-mortem, measurement of success; bucket reviews by stage from ideation to pre-ship. Fails if you expect the template alone to improve thinking.

**29. ChatPRD default template** (Claire Vo). Objectives and user goals, user stories, out of scope, UX walkthrough, a narrative on how to pitch the product (a part PMs often miss), sequencing and milestones, measurement and goals. Customize per company. Usage benchmark: about 60% of ChatPRD users put in an idea and get a PRD, about 30% improve an existing doc.

**30. Pod strategy doc** (Geoff Charles). Sits between roadmap and vision: goals, hypothesis, why we are uniquely positioned, metrics, initiatives, risks, long-term outcomes. Each pod writes one and the leader reconciles with product and financial strategy. (Chandra Janakiraman argues the roadmap stays out of the strategy doc.)

**31. Roadmap doc linking to live systems** (Jiaona Zhang). Written doc over decks for remote teams; link to Jira instead of static spreadsheets that go stale. Steps: what you are trying to achieve; big areas and themes; projects per theme; link to the real system; edit themes only on major learning.

**32. Short memos at each level** (Melissa Perri). Two-page memos per level rather than 20-page requirements documents.

**33. Chaos to clarity** (Melanie Perkins). Move an idea from chaos to clarity in increments: write it down, pitch deck, designs, prototype, sharing at each step. First step feels embarrassing; do it anyway.

**34. Feelings kickoff** (Josh Miller). Instead of a PRD listing emotions, get the small team in a room: the user problem, where it fits their day, the feeling to create (for Peek: light, airy, fast, agile); reference the feelings in design decisions. Fails at scale without shared context.

## D. Choosing the medium: doc, prototype, demo or nothing

**35. Pick the medium for the point** (Andrew Ambrosino). Document for clarity on a vague area; prototype to stress-test an interaction. Label the stage of the artifact. Failure modes: engineers over-produce documents, non-engineers over-jump to prototypes.

**36. Prompt sets are the new PRDs** (Aparna Chennapragada). New features come with working prototypes and prompt sets; show a live demo before a memo. Skip for deep changes inside mature products.

**37. Light PRD plus live prototype** (Eric Simons). Only key outcomes, a link to a working prototype, detail added only for sophisticated features.

**38. Prototypes over decks and PRDs for AI** (Howie Liu). Build an open-ended prototype; try messy, non-golden-path prompts; judge speed and whether to expose reasoning steps or a progress bar.

**39. Live PRD in v0** (Guillermo Rauch). Prototype the feature in an AI builder, include error, success and loading or slow-stream states, share it as the spec.

**40. Demos not memos** (Max Schoening). Bring a demo to reviews; if writing a PRD, write the changelog or blog post a user would read; produce alternatives fast when people react.

**41. Working demos instead of decks** (Keith Rabois). Shopify disallows PowerPoint or keynote for product for two years; every product presentation is a working demo.

**42. Scale documentation to project size** (Amol Avasare). About 60-80% of Anthropic growth work ships with no PRD. Small: Slack with a product-minded engineer. Large: 30-minute cross-functional kickoff. Critical 20-30%: thorough doc. Use a Claude skill plus prior PRDs to draft fast. Fails for high-stakes projects needing a careful doc.

**43. One-pager for ambiguous work only** (Cat Wu). Goals, delightful use cases, current failure modes. Skip for small, quick features.

**44. When PRDs still earn their keep** (Dianne Penn). Aligning a very large group (engineering, legal, safety) on one source of truth; exploring ambiguous capabilities in a vision section. Use evals when the problem is defined and the audience is researchers.

**45. Design-first discovery** (Gaurav Misra; contrarian). Designers explore many concepts without a defined why, then review with PMs and spec the interesting ones. For consumer apps seeking novel ideas.

**46. Chatter-driven development** (Alexander Embiricos; contrarian). Spec-driven development may not win; agents consuming team chatter and signals could fix small bugs without a spec.

## E. Specs for AI features and agents

**47. Tool-spec design** (Karina Nguyen). A spec for an AI feature is a prompted prototype of desired behavior plus a tool spec: what the model must extract (e.g. the time for a reminder), the JSON schema, and how the task fires and notifies.

**48. Expected input/output dataset** (Aishwarya Naresh Reganti). PMs and subject matter experts gather example inputs and ideal outputs before building; disagreements show the team is not aligned on behavior.

**49. PRD updated from error analysis** (Shreya Shankar). Judge prompts and evals encode requirements, but failure modes are unknown up front. Write an initial PRD, do error analysis, feed discovered expectations back.

**50. Exploration phase** (Zevi Arnovitz). Before planning, the agent fetches the ticket, reads the relevant code and asks clarifying questions on scope, data model, UX, validation, grading and prompt changes; you answer. For serious apps, not quick prototypes.

**51. Markdown plan file with status trackers** (Zevi Arnovitz). From the exploration exchange, the agent writes a plan: TLDR, critical decisions, clear minimal tasks with status trackers it updates; kept in the repo so multiple models and future agents see prior work.

## F. Anti-patterns to name out loud

**52. Google Docs syndrome** (Nabeel S. Qureshi, contrarian). Writing requirement documents and managing in a sane, rational way instead of driving outcomes; a failure mode Palantir feared in traditional PMs.
