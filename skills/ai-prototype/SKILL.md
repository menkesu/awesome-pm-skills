---
name: ai-prototype
description: Turns an idea into a working, user-testable prototype with AI builders (Lovable, v0, Bolt, Replit, Cursor, Claude Code) and gets you unstuck when the tool breaks. Produces a Prototype Brief with a build-prompt pack, a debugging log and a user-test plan. Use for 'vibe coding', 'build a prototype', 'prototype this feature', 'Lovable prompt', 'my AI builder is stuck', 'prototype instead of a PRD', or 'demo for users'. Draws on 44 Lenny's Podcast guests incl. Lazar Jovanovic, Zevi Arnovitz and Guillermo Rauch.
---

# AI Prototype

![ai-prototype: lead guest team](assets/card.png)

Go from a vague idea to a clickable, testable prototype in a day, and keep moving when the AI builder gets stuck. Built from 96 insights from 44 Lenny's Podcast guests. **Lead team:** Lazar Jovanovic, Zevi Arnovitz, Guillermo Rauch.

## When to use
- You have an idea or feature and want something users can click before anyone writes a spec.
- You are about to write a PRD and want a prototype to attach to it.
- You are non-technical (or semi-technical) and want to start building with AI tools.
- Your AI builder is looping, breaking things, or burning credits on the same bug.
- You need a demo for execs, a customer test, or a sprint prototype this week.
- You are deciding which tool to use (Lovable, v0, Bolt, Replit, Cursor, Claude Code).
- You want to build an AI feature prototype and are unsure whether to use a real model or fake it.

## Step 1 — Diagnose (ask before answering)
If the user attached a PRD, sketch, repo, screenshot or half-built project, read it first and skip questions it answers. Ask at most 4:
1. **What single question must this prototype answer, and who will see it** (just you / team / customers / execs)? *Routes fidelity: SoloWare vs sprint simulation vs exec demo.*
2. **Have you built with AI tools before, and which ones?** *Routes the tool ladder and how much to teach (Zevi Arnovitz).*
3. **Greenfield, or inside an existing codebase (roughly how many files)? Is the core of the product itself AI-generated behavior?** *Routes to scope-down, Cursor vs builder, and real-model vs faked-AI.*
4. **How clear is the idea: a vague hunch, a sketch, or references and screenshots?** *Routes to parallel starts vs sketch-first.*

## Step 2 — Pick the play
| If… (situation) | Use | From | Why |
|---|---|---|---|
| Vague idea, blank page | Parallel multi-fidelity starts (3 to 5 projects, pick the winner) | Lazar Jovanovic | Cheap concepts to compare beat patching one weak direction |
| Clear idea, differentiation matters, or AI-centric product | Sketch first, then vibe code; decide what is real vs static | Jake Knapp, John Zeratsky | AI-built prototypes trend generic unless you supply the thinking |
| First time building, non-technical | Graduated tool ladder + AI CTO project + read agent output | Zevi Arnovitz, Lazar Jovanovic | Ease in; build technical judgment while shipping |
| Need to know if an idea is worth it, fast | Failure machine: build it wrong in a day, test pieces separately | Mark Pincus | Lowest-cost version that gives signal |
| Prototype for yourself only | SoloWare, with a harm check | Dharmesh Shah, Simon Willison | No polish, no tests, shut it off at will |
| AI feature with non-deterministic output | Prototype on the real model and watch real users | Jenny Wen, Karina Nguyen | You cannot mock every state |
| Startup MVP where AI is the pitch | Fake the AI with a prototype; do not train a model | Marily Nika | Prove demand before investing in a model |
| Existing large codebase | Scope to one component/file; use Cursor, not a text-to-app tool | Guillermo Rauch, Eric Simons | LLMs degrade on long context and 1000+ files |
| Tool is stuck | Four by four debugging | Lazar Jovanovic | Escalate through different approaches, once each |

## Step 3 — Run it

### Play 1: Plan, then build (every project)
1. **Spend the first block on clarity, not output** (Lazar Jovanovic's 80/20). Use chat/plan mode only. Brain-dump by voice (Zevi Arnovitz uses dictation), and let the tool or a PRD-generator GPT interview you. Do not tidy first (Dr. Becky Kennedy).
2. **Write the first prompt like a ticket** (Eric Simons): who the user is, named features and pages (e.g. submission, voting, status board, admin controls, per Amjad Masad), what matters, and where the tool has creative latitude.
3. **Describe the end-user experience, not the implementation** (Guillermo Rauch). Say what the user sees and feels; leave tech choices to the tool unless you have a reason.
4. **Attach references, not adjectives.** Screenshot of your own board/Figma/Slack post (Rauch); a design screenshot from Mobbin or Dribbble; code snippets from a component library such as 21st.dev for pixel-level fidelity (Lazar Jovanovic). Add a style line like *in the style of Stripe* (Andrew Wilkinson).
5. **Build experience first, then make it real** (Rauch, Anton Osika): UI mockup, then connect a backend, then login, then editable data, then deploy. Do each as its own prompt.
6. **Give it realistic data**: write a short backstory for a fictional user and have the model generate data that fits their world (Alex Komoroske).
7. **Tiny edits go in the visual editor** (Osika), not in new prompts. Reserve prompts for larger changes.
8. **For payments or database changes, plan with the agent before any code** (Zevi Arnovitz).
9. **Done when:** a stranger can complete the core journey without you narrating, and you know which parts are real vs faked.

### Play 2: Parallel multi-fidelity starts (vague ideas)
1. Project A: raw voice brain-dump, send without polishing.
2. Project B: refined prompt with feature/page list plus a reference screenshot.
3. Project C: prompt plus code snippets from a component library.
4. Compare the 3 to 5 concepts, pick one, and continue only there. Restarting from a clearer concept costs a little up front but saves hundreds of credits (Lazar Jovanovic).

### Play 3: Debug loop (Lazar Jovanovic's four by four, plus Rauch's escape hatches)
Before attempt 1, state what you expect and what you are not getting; never just say it does not work (Anton Osika). Then, one attempt per approach:
1. **Let the agent try to fix it** (the built-in fix button), or say *try something else* (Rauch).
2. **Awareness layer:** open the preview, run the broken function, ask the agent to add console logs along each step, rerun, paste the full log back into chat. Fixes most bugs on third-party integrations.
3. **External consultant:** export to GitHub (or compress with Repomix), give a different tool (Codex, Claude, ChatGPT) the goal, the problem and the logs. Diagnosis only; take the answer back to the original tool. Rauch's version: paste the generated code into another strong reasoning model.
4. **Revert and rethink:** go back a few versions, rewrite the prompt, take a break. If you do not know the vocabulary, switch to chat mode and ask the tool to draft a better prompt.
5. **Afterwards:** ask the tool how you should have prompted, and write the lesson into a rules file the agent reads.
6. **Stop rule:** ask chat mode whether the capability is feasible before brute-forcing. Lazar lost a week on something that was not yet technically possible.
7. **Know the cliffs:** large iterations and database migrations (Amjad Masad), 1000+ files (Eric Simons), and apps big enough that you can no longer change them (Michael Truell). At the cliff, hand the working prototype to an engineer rather than fighting on.

### Play 4: Make the prototype answer a question (testing)
1. Write the key question. For each screen decide: **real**, **vibe coded**, or **static mockup/video** (John Zeratsky). Only the parts that bear on the question must be real.
2. For AI behavior: put the real model behind it and watch real use; do not hand-mock outputs (Jenny Wen). For an MVP pitch with no data, fake the AI instead (Marily Nika).
3. Put it in front of users, not in a design review (Gaurav Misra). Watch what they do before you ask what they think.
4. Hand engineering the validated prototype plus the evidence, not a spec alone (Amjad Masad, Mike Krieger, Elena Verna). Treat the code as a throwaway: architect the real system explicitly (Tony Fadell).

### Play 5: Tool choice and growth path (non-technical builders)
1. Start in a chatbot project, move to Bolt or Lovable, then Cursor, then terminal tools, graduating when you outgrow each (Zevi Arnovitz).
2. Pick by harness: the models are the same; builders remove decisions (database, auth), editors give control back.
3. Create an AI CTO project that owns the how and is told to challenge you (Zevi Arnovitz). Use a learning-opportunity command to get 80/20 explanations of what you just built.
4. Do not invest in tool workarounds or stack debates; tools absorb them in months (Lazar Jovanovic).

## Where the experts disagree
1. **Prototype first** (Aparna Chennapragada, Kevin Weil, Dylan Field, Eric Simons) vs **think first** (Bob Baxley, Jake Knapp, John Zeratsky). → *Prototype first when the problem is understood and you are exploring options; think first when the concept is fragile or differentiation is unknown, because the first realistic artifact becomes everyone's anchor.* → **Default:** a short conversation and a paper sketch, then parallel starts.
2. **Non-technical is an advantage** (Lazar Jovanovic, Nikhyl Singhal) vs **you must understand what is under the hood** (Michael Truell, Simon Willison, Edwin Chen). → *Prototypes and personal tools: stay beginner-minded and read the agent output. Anything touching other people's data, money or systems: add review.* → **Default:** Zevi Arnovitz's cross-model review and a learning habit; escalate to an engineer before real users are exposed.
3. **Fake the AI** (Marily Nika) vs **use the real model** (Jenny Wen, Karina Nguyen). → *Fake when you are proving demand with no data; real when the question is how good or surprising the behavior is.* → **Default:** scripted AI for desirability tests, a real prompt for behavior tests, never a trained model for a prototype.
4. **Plan-heavy** (Lazar Jovanovic, Zevi Arnovitz) vs **minimalist prompt** (Amjad Masad, Anton Osika). → *Minimal when the target is a known category and the first output is just a baseline; plan-heavy for custom flows, payments, data models.* → **Default:** short first prompt for a known pattern, plan mode for anything novel.

## Deliverable
```markdown
# Prototype Brief: [name]
**Key question this prototype answers:** [one sentence]
**Audience:** [self / team / customers / execs]   **Time box:** [hours/days]
**Tool and why:** [builder or editor; harness tradeoff]

## Fidelity map
| Screen / behavior | Real | Vibe coded | Static or faked |
|---|---|---|---|

## Concept starts (parallel)
| Start | Input (voice dump / refined prompt / reference + code snippet) | Verdict |
|---|---|---|

## Build prompt #1 (ticket style)
- User and situation:
- Experience the user should have:
- Named features/pages:
- Must be specific:
- Open for creativity:
- References attached: [screenshots, snippets, style line]
- Test-data persona: [short backstory]

## Phases
1. Experience  2. Backend  3. Auth  4. Editable data  5. Deploy  (plan mode first for payments/DB)

## Debug log
| Symptom | Expected vs actual | Attempt (fix / logs / external / revert) | Result |
|---|---|---|---|

## rules.md lines learned
-

## User test plan
- Participants and task:
- What we watch for (the key question):
- Success / kill signal:

## Handoff
- Evidence, prototype link, what is throwaway, where the cliff was hit

## Next 3 actions
1.
2.
3.
```

## Grade existing work
Score each 1 to 5, total /40. Return the score table and the top 3 fixes, each with the guest behind it.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Key question | None; built because it was fun | Implied | Stated, and every screen serves it (Zeratsky) |
| Planning before building | Straight into code | Prompt written, no plan | Clarity phase done; plan mode used for payments/DB (Lazar, Zevi) |
| Prompt quality | One vague line, 'make it nice' | Features listed | Ticket-style, user experience described, latitude marked (Simons, Rauch) |
| References | None | Adjectives | Screenshots and code snippets attached (Lazar, Rauch) |
| Concept exploration | One direction, patched forever | Two options | 3 to 5 compared, winner chosen (Lazar) |
| Realism of data and AI | Lorem ipsum, hand-mocked AI | Some real data | Persona-based data; real model for behavior tests (Komoroske, Wen) |
| Debug discipline | Repeats the same fix | Pastes errors | Logs gathered, external diagnosis, revert, rules recorded (Lazar) |
| User contact and handoff | Never shown to users | Shown internally | Tested with users; handoff says what is throwaway (Masad, Fadell) |

## Red flags
- Coding instantly on payments or database changes with no plan (Zevi Arnovitz).
- Reporting only that it does not work, with no expected vs actual (Anton Osika).
- Patching a weak first direction for days instead of restarting clearer (Lazar Jovanovic).
- Brute-forcing a capability that is not yet technically possible (Lazar Jovanovic).
- Letting the external diagnostic tool edit your code (Lazar Jovanovic).
- A believable but generic prototype that does not show how the product differs (John Zeratsky).
- Training a model for an MVP when a faked prototype would prove the market (Marily Nika).
- Loading a huge legacy codebase into a text-to-app tool (Eric Simons).
- Treating the prototype as the production foundation (Tony Fadell, Sam Lessin, Bret Taylor).
- Vibe coding scrapers or tools that touch other people's systems without knowing the risk (Simon Willison).
- Hi-res output too early, which pulls feedback to colors and shapes instead of value (Bob Baxley).

## Receipts
> "I can say I spent 80% of my time in planning and chatting and only 20% in executing the plan actually." — Lazar Jovanovic, Lenny's Podcast (00:12:36)

> "You copy that, you paste it inside your chat. 99% of the time, that's enough, that's already enough." — Lazar Jovanovic, Lenny's Podcast (01:07:58)

> "Take screenshots of your own things. Take screenshots of your art boards, take screenshots of things that people post in Slack, and also don't hesitate add functionality." — Guillermo Rauch, Lenny's Podcast (00:59:12)

> "the main difference between all these tools is basically the harness. So the models are all the same models." — Zevi Arnovitz, Lenny's Podcast (00:32:11)

> "while you're outsourcing that prototyping work, you don't outsource the thinking." — John Zeratsky, Lenny's Podcast (01:33:12)

> "if you're vibe coding something for yourself where the only person who gets hurt if it has bugs is you, go wild." — Simon Willison, Lenny's Podcast (00:08:50)

## Go deeper
- `references/frameworks.md` — every framework in this skill, how to run it
- `references/quotes.md` — verified quotes with timestamps
- Related skills:
  - `validate-idea` — when the riskiest assumption is demand, not usability; test it before building.
  - `spec` — when the prototype is validated and needs a shaped spec or PR-FAQ for engineering.
  - `craft-review` — when the prototype works and you need a friction log and taste bar.
  - `eval-plan` — when the prototype contains an AI feature that must graduate to production quality.
