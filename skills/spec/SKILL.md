---
name: spec
description: Writes (or rewrites) a spec, PRD, PR-FAQ or shaped pitch and grades it against what the best product teams actually do. Use when you ask 'write a PRD', 'how do I spec this', 'PR/FAQ', 'working backwards doc', 'shape this project', 'do we even need a PRD', or 'engineering says the spec isn't detailed enough'. Draws on 56 insights from 38 Lenny's Podcast guests incl. Ryan Singer, Bill Carr and Lane Shackleton.
---

# Spec: Shaped Spec / PR-FAQ, Graded

![spec: lead guest team](assets/card.png)

Turn a vague request into a spec an engineer can build from, or a PR/FAQ that decides whether to build at all, then grade it and return the top 3 fixes. Built from 56 insights from 38 Lenny's Podcast guests. **Lead team:** Ryan Singer, Bill Carr, Lane Shackleton.

## When to use
- A stakeholder hands you a noun (*calendar*, *dashboard*, *newsletter builder*) and you need to turn it into something buildable.
- You need to decide between competing ideas, or whether an idea deserves engineers at all.
- Engineering keeps saying the spec lacks detail, or projects keep overrunning.
- You are launching cross-functionally and need dates, goals and owners agreed in writing.
- You are specifying an AI feature and the behavior is hard to put in prose.
- You are asking whether to write a doc, build a prototype, or just post in Slack.
- You have an existing PRD, PR/FAQ, pitch or ticket and want it scored and tightened.

## Step 1: Diagnose (ask before answering)
If the user attached a PRD, ticket, deck, transcript or repo, read it first and infer answers from it. Ask only what remains, max 4:
1. **What is the doc's job?** Decide whether to build / hand a defined problem to engineers / align a big group / launch plan. *Routes to PR/FAQ vs shaping vs PRD vs launch PR-FAQ.*
2. **Can a senior engineer join a live session, and how senior is the build team?** *Routes to the shaping session and sets the detail dial.*
3. **Is this an AI feature or can you prototype it in a day?** *Routes to prototype-first and tool-spec plays.*
4. **How big is the blast radius?** Small change, multi-month infra, regulated, multi-sided marketplace, or many approvers (legal, safety, marketing). *Decides doc weight and mandatory FAQ items.*

## Step 2: Pick the play
| If... (situation) | Use | From | Why |
|---|---|---|---|
| Request arrives as a vague noun or a stakeholder wish | **Framing**: narrow it to a specific problem first | Ryan Singer | Without a narrow frame, shaping never ends |
| Problem is clear, you must hand engineering something with a time box | **Shaping session + shaped output test** | Ryan Singer | Engineer in the room exposes what is easy and hard before commitment |
| Choosing what to build, or among competing ideas; pre-staffing | **PR/FAQ** (or the 2-paragraph mock press release) | Bill Carr, Jag Duggal | Writing it down kills weak ideas before build time is spent |
| Cross-functional launch with dates and approvers | **PR as a negotiation tool + FAQ as checklist** | Anuj Rathi | Customer and business-owner quotes become commitments marketing, pricing and eng must test |
| Many readers, async buy-in, politics | **Two-way writeup** (done-reading, question table, sentiment table) | Lane Shackleton | Feedback becomes part of the doc, not comments nobody triages |
| New feature, cheap prototyping, or AI with open-ended inputs | **Light PRD + live prototype** (include error, slow, success states) | Eric Simons, Howie Liu, Guillermo Rauch | Words are not proof; messy prompts and latency only show in a prototype |
| AI feature | **Prompted prototype + tool spec + expected input/output set** | Karina Nguyen, Aishwarya Naresh Reganti | Surfaces team disagreement on behavior before building |
| An agent will implement it | **Exploration phase + markdown plan file** | Zevi Arnovitz | Answered questions yield far better plans than vibing |
| Small, quick change with a strong engineer | **No PRD: Slack, or one-pager only if ambiguous** | Amol Avasare, Cat Wu | Most Anthropic growth work ships without a PRD |

## Step 3: Run it

### Play A: Frame, then shape (Ryan Singer)
1. **Frame.** Refuse to build the generic thing. Find the specific customer pain behind repeated requests (for calendar: seeing empty spaces). Write one sentence naming the pain and the time you are willing to spend.
2. **Label the problem** (Christopher Miller): business, customer, or efficiency. If business, ask why it has not solved itself; the answer is the customer problem. Then ask why, why, why to justify direction and what, what, what to size blast radius.
3. **Convene 3 people:** the engineer who truly knows the system, the product person with the backstory, a designer. Run about 3 hours at a whiteboard.
4. **Sketch at the level of buttons, flows and calculations** (breadboard / fat marker): *hit this button, go here, this calculation runs, then a choice.* A generic wireframe (*dashboard here, four reports*) does not count.
5. **Try to break each idea.** Engineer hunts for why it will not work; product plays the customer scenario to check value. Then draw a very different idea B. Log the 'what abouts' (e.g. multi-day events) and spike them between sessions.
6. **Stop when it passes two tests:** you can describe it in fewer than about 10 moving pieces, and you can hand it to a technical person who says they know what to build. If not, keep shaping. Expect about 3 sessions for work on existing tech; new algorithms or models take longer.
7. **Turn the detail dial.** Juniors get more implementation guidance, trusted seniors less; dial back over successive projects. Pull in any engineer who wants a say in fundamentals.
8. **Only now** hand to design for high fidelity. Figma before the shape is settled hides what is in the wall.

### Play B: PR/FAQ (Bill Carr)
1. Headline that plainly says what the thing is. Set a hypothetical launch date (it signals simplicity or complexity).
2. Para 1: the product. Para 2: the specific customer and a quantified problem. Para 3: the solution. Data, not hyperbole; it is an internal document, not real marketing copy.
3. Add a customer quote and a business-owner quote (Anuj Rathi). Take the date to engineering, the customer quote to marketing and pricing (*can we ship something customers would say this about?*), the business quote to the owner (e.g. three-month targets). If anyone disagrees, adjust date and goals together.
4. FAQ: data-rich, and hard-wire your company's checks as mandatory items: compliance sign-off at a fintech, implications for every side of a marketplace and each partner segment (Anuj Rathi).
5. Minimum version before any engineer is staffed (Jag Duggal): two paragraphs to the intended customer on why they should care. If you cannot do it crisply, the idea is not ready.
6. Assign an owner to investigate and build only if the writing survives scrutiny (Bill Carr).

### Play C: Make the doc two-way (Lane Shackleton)
1. End the doc with a **done-reading button** (three for a long doc). Stop watching for the SVP's avatar.
2. Replace comment-margin triage with a **question table** (Dory) readers upvote; run the meeting from the top-voted questions.
3. Add a **sentiment table**: each reader rates the proposal. Discuss the spread, not the average.
4. Keep the doc itself crisp and the meeting messy (John Mark Nickels). Write, then cut almost all of it, down to the minimum that supports a clean recommendation (Ami Vora): *three analyses say X, one says Y and we think it is wrong or worth the risk; any objections or new context?*

### Play D: Prototype-first and AI specs
1. Pick the medium for the point (Andrew Ambrosino): a document for clarity on a vague area, a prototype to stress-test an interaction. Label the artifact's stage so an exploration is not mistaken for production-ready.
2. Prototype with realistic messy inputs, not golden-path ones; judge latency and whether to expose reasoning (Howie Liu). Show error, success and slow states (Guillermo Rauch).
3. Keep the PRD to key outcomes plus the prototype link (Eric Simons). At GitHub the PRD, if written, was the changelog or blog post a user would read (Max Schoening).
4. For AI: write the prompted prototype of desired behavior, list what the model must extract, define the JSON schema, design how the task fires and notifies (Karina Nguyen). Gather PM and SME example inputs and ideal outputs first; disagreements there are the real spec (Aishwarya Naresh Reganti). Then update the PRD from error analysis, because you do not know what you want until you see outputs (Shreya Shankar).
5. For agent builds: have the agent read the code and ask questions on scope, data model, UX, validation and prompt changes; answer them; then have it write a markdown plan with TLDR, critical decisions and minimal tasks with status trackers (Zevi Arnovitz).

### Play E: Right-size the document
- Under a day of work with a product-minded engineer: Slack, no doc.
- Larger: a 30-minute cross-functional kickoff where legal, safeguards and others say what they care about (Amol Avasare).
- Ambiguous or multi-month infra: a one-pager with goals, delightful use cases, current failure modes (Cat Wu).
- Squad-level: open with background, problem, why it matters, why now; keep a dated log of decisions and cuts (Maggie Crowley).
- Every ticket: success metric and growth lever (acquisition, activation, retention, monetization); this often kills low-value work (Hila Qu).

## Where the experts disagree
1. **Are PRDs dead?** **Camp A:** Aparna Chennapragada, Guillermo Rauch, Keith Rabois, Howie Liu, Amol Avasare say prototypes, prompt sets and live demos replace them. **Camp B:** Andrew Ambrosino, Dianne Penn, Eric Simons, Ryan Singer say they stay useful if minimal and paired with a demo. *Use A for new, interactive or AI features where building is cheap; B for large-group alignment (legal, safety, engineering) and ambiguous opportunities.* **Default:** a half-page doc plus a prototype link, nothing longer.
2. **How much detail?** **Camp A:** Ryan Singer says the dominant failure is not enough detail. **Camp B:** Melissa Perri (two-page memos), Ami Vora (cut almost everything), Eric Simons (minimal context). *Use A when engineers keep asking product for more; B for readers who skim.* **Default:** cut prose, but add concreteness (moving pieces, flows, calculations). Detail is not length.
3. **One-way or two-way docs?** **Camp A:** Bill Carr and John Mark Nickels (crisp narrative, messy meeting). **Camp B:** Lane Shackleton (two-way writeups outperform six-pagers with comments). *Use A when a few senior readers decide live; B when async cross-functional input is the point.* **Default:** crisp narrative plus a question table and done-reading button.
4. **Spec before or after talking to engineering?** **Camp A:** Ryan Singer (engineer in the room, no PRD-first or Figma-first handoffs). **Camp B:** Gaurav Misra (let designers explore many ideas with no defined why, then review with PMs). *Use B only for novel consumer-app idea generation; A to commit to a project.* **Default:** B to find ideas, A to spec them.

## Deliverable
Produce this, filled in from the user's context:

```markdown
# <Project name>  | Stage: ideation / shaping / ready-to-build | Owner: <name> | Date: <date>

## Background and why now
<What is the problem, why it matters, why it matters now. 3-5 lines.>

## Problem (qualified)
Type: business / customer / efficiency. <One specific, quantified problem for one named customer.>
Why it has not solved itself: <...>   Assumptions and predicted downstream effects: <...>

## Customer press release (optional if PR/FAQ was chosen)
Headline: <what it is>   Launch date: <hypothetical>
Para 1 product / Para 2 customer + problem / Para 3 solution
Customer quote: <what we want customers to say>   Business-owner quote: <target>

## Appetite and shape
Time box: <...>   Build team and detail dial: <junior / mixed / senior>
Moving pieces (fewer than 10):
1. ...
Sketch / breadboard / prototype link: <...>   Includes error, slow and success states: yes/no
Shaped output test: engineer <name> confirmed on <date> they know what to build: yes/no

## What-abouts and risks
- <edge case> -> spiked? <result>      - Pre-mortem: <how this fails>
## Not doing
- ...
## Success
Metric: <...>   Growth lever: acquisition / activation / retention / monetization
## FAQ
Q: Compliance / legal sign-off? Q: Implications for each side or segment? Q: What would make us kill it?
## Decision log (dated)
- <date>: decided / descoped <...>
## Review
Done-reading: <who>   Top questions (upvoted): <...>   Sentiment spread: <...>

### Next 3 actions
1. <who / what / by when>
2. ...
3. ...
```

## Grade existing work
Score each 1-5 (1 / 3 / 5 shown). Total out of 40.
| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Problem specificity (Singer, Miller, Cohen) | Noun or goal (*build a calendar*) | Customer named, problem vague | Typed, quantified, one customer, explains why it is unsolved |
| Customer clarity (Carr, Duggal) | No customer voice | Customer described | Press release or two paragraphs a customer would care about, with quotes to test |
| Shaped concreteness (Singer) | Prose and user stories | Wireframes, generic | Under 10 moving pieces; builder says they know what to build |
| Engineering involvement (Singer) | Engineers see it after | Engineer reviewed | Engineer co-shaped, hunted for breakage |
| Detail fits builder (Singer) | Under- or over-specified for team | Some tuning | Dial set to team seniority; fundamentals open for senior input |
| Success and lever (Hila Qu) | None | Metric only | Metric plus growth lever; work still justified |
| Risks and what-abouts (Singer, Tolkin) | None | Listed | Spiked, with pre-mortem and mandatory FAQ checks |
| Format and discussion design (Ambrosino, Shackleton, Nickels) | Wrong medium, comments only | Right medium | Right medium, done-reading, question and sentiment tables, stage labeled |

Output: score per criterion, total, then the **top 3 fixes**, each naming the guest and framework behind it.

## Red flags
- **The shaping artifact is a PRD or Figma with no engineer in the room.** The usual reason Shape Up projects overrun (Ryan Singer).
- **A generic wireframe or user stories counted as shaped** (Ryan Singer).
- **A big idea debated as a concept, never written down**, so politics wins (Bill Carr).
- **A press release full of hyperbole or real marketing language** (Bill Carr).
- **Handing marketing a bag of doorknobs** instead of a coherent theme (Carilu Dietrich).
- **Engineers writing documents not worth reading; non-engineers jumping to prototypes** (Andrew Ambrosino).
- **A bare problem statement** with no type and no why (Christopher Miller).
- **Golden-path-only prototypes of AI features** (Howie Liu).
- **Google Docs syndrome:** managing by sane, rational requirement docs instead of driving outcomes (Nabeel S. Qureshi).
- **Treating a template as thinking:** templates alone do not improve thinking (Brian Tolkin).
- **Unlabeled stage:** an exploration mistaken for a production-ready plan (Andrew Ambrosino).

## Receipts
- "the dominant failure case that I see in the real world is always, again and again, not enough detail." — Ryan Singer, Lenny's Podcast (00:47:26)
- "If it's shaped well, you can usually describe it in less than 10 moving pieces." — Ryan Singer, Lenny's Podcast (00:42:21)
- "So one problem is that companies get stuck, I think, where they never actually go do that documentation. And so it's a debate and discussion about concepts that aren't really well fleshed out." — Bill Carr, Lenny's Podcast (00:52:46)
- "we're in the midst of a new phase, which is essentially two-way writeups and that's where it's more conversational and feedback and discussion is actually part of the content itself." — Lane Shackleton, Lenny's Podcast (01:14:35)
- "If implementation is abundant, then it's really important to pick the right format for the point you're trying to make." — Andrew Ambrosino, Lenny's Podcast (00:07:45)
- "if you haven't checked if there's electricity in that wall there or not, it's going to drastically change the cost and the time and everything" — Ryan Singer, Lenny's Podcast (00:40:16)

## Go deeper
- `references/frameworks.md`: every framework in this skill, how to run it
- `references/quotes.md`: verified quotes with timestamps
- Related skills: **validate-idea** (hand off when the riskiest assumption is untested before you write a spec); **prioritize** (when the question is which spec to write first); **launch** (when the PR/FAQ becomes a launch plan); **eval-plan** (when an AI spec needs judges and error analysis).
