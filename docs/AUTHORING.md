# Authoring an Awesome PM Skill (v2)

You are writing one skill for **awesome-pm-skills v2**: the most actionable PM skill library built from all 340 Lenny's Podcast episodes. Each skill is used inside Claude Code / Cursor / Codex by product managers who want work *done*, not advice *read*.

Work from the repository root.

## Inputs
- `digests/<skill>.md` (optional local research input, excluded from Git) — every insight for this skill's PM jobs, extracted from the transcripts: guest, episode, framework, claim, steps, when it applies / fails, originator and contrarian flags, and a **verbatim, pre-verified quote with timestamp**. Lead guests come first. Read the WHOLE digest (page through it with offset/limit if Read truncates). Your skill must synthesize across ALL guests, not just the leads.
- The catalog below (for the skill's promise, lead team, and related skills).

## Outputs (write exactly these files)
```
skills/<skill>/SKILL.md
skills/<skill>/references/frameworks.md
skills/<skill>/references/quotes.md
```

## What makes these skills different (non-negotiable)
1. **Do, don't lecture.** The skill runs a workflow and ends with a concrete deliverable the PM can paste into a doc. If the user provides a file (PRD, survey CSV, deck, transcript, repo), read it and work on it.
2. **Context routes the framework.** Guests disagree and frameworks fit different situations. Diagnose first (stage, B2B/B2C, AI or not, team size, what's at stake), then pick the play from a routing table. Never dump every framework.
3. **Show the debates.** Where guests genuinely disagree, name both camps (with guest names), say when each one wins, and recommend for this user's context.
4. **Grade existing work.** Every skill can score the user's existing artifact with a rubric and return the top 3 fixes.
5. **Receipts.** Every recommendation is traceable to a named guest. Quotes are verbatim only.
6. **Specific beats generic.** Prefer numbers, benchmarks, exact questions to ask, templates, thresholds, named anti-patterns. Cut anything a smart PM already knows.

## Quote rules (a script checks this; the skill fails if violated)
- Use **double quotes ONLY for verbatim guest quotes copied exactly from the digest's QUOTE field**, character for character. Never write, merge, trim mid-sentence, or "clean up" a quote. Never invent quotes.
- For example phrasings, sample questions you wrote, or template text, use *italics* or single quotes — never double quotes.
- Attribute every quote: `— Guest Name, Lenny's Podcast (HH:MM:SS)` using the digest's timestamp.
- Keep quotes short (they already are, ≤45 words). Max ~6 quotes in SKILL.md, 15–30 in quotes.md.
- Never role-play a guest ("As Shreyas, I think…"). Write "Shreyas Doshi's pre-mortem asks…".

## SKILL.md template (150–300 lines; tight, scannable, imperative voice)
```markdown
---
name: <skill>
description: <2–3 sentences, trigger-rich: what it does + the deliverable + when to use it, with the words a PM would actually type (e.g. "pricing", "how much should we charge", "packaging", "tiers"). Mention it draws on N Lenny's Podcast guests incl. the 3 leads.>
---

# <Title>

<One-line promise.> Built from <N> insights from <M> Lenny's Podcast guests. **Lead team:** <Lead 1>, <Lead 2>, <Lead 3>.

## When to use
- bullets of concrete triggers/situations (5–7)

## Step 1 — Diagnose (ask before answering)
Ask only what you can't infer from files/context, max 4 questions. List them with *why each matters* (which play it routes to). If the user attached an artifact, read it first.

## Step 2 — Pick the play
| If… (situation) | Use | From | Why |
|---|---|---|---|
4–8 rows. Plays are named frameworks from the digest, credited to their originator.

## Step 3 — Run it
For each play (or the 2–4 most important ones): numbered, concrete steps; exact questions/prompts to use; thresholds/benchmarks; how to know you're done. This is the heart of the skill.

## Where the experts disagree
2–4 debates: **Camp A** (guests) vs **Camp B** (guests) → *Use A when…, B when…* → our default.

## Deliverable
The fill-in template the skill produces (fenced markdown), ending with a short "Next 3 actions" section.

## Grade existing work
Rubric table: 5–8 criteria, each with what a 1 / 3 / 5 looks like (derived from guest advice). Output: score per criterion, total, top 3 fixes with the guest/framework behind each.

## Red flags
6–10 anti-patterns guests warn about (credit them).

## Receipts
3–6 verbatim quotes (see quote rules).

## Go deeper
- `references/frameworks.md` — every framework in this skill, how to run it
- `references/quotes.md` — verified quotes with timestamps
- Related skills: 2–4 from the catalog, each with one line on when to hand off
```

## references/frameworks.md
Every distinct, useful framework/method in the digest for this skill (typically 12–40), grouped by theme. For each: **Name** (originator, episode) — what it's for; when it applies / fails; steps; any benchmark. Merge duplicates across guests and note who else endorses it. Skip trivia.

## references/quotes.md
15–30 of the strongest verbatim quotes, grouped by theme, each with `— Guest, Lenny's Podcast (timestamp)`. Copy exactly from the digest.

## Finish
1. Run `python3 check_quotes.py skills/<skill> --transcripts /path/to/transcripts` and fix every NOT MATCHED line (copy the exact digest quote, or convert your own wording to italics). Re-run until OK.
2. Reply with one line: `<skill>: SKILL.md <lines> lines, <F> frameworks, <Q> quotes verified`.

## Catalog (all 25 skills)
| skill | promise / deliverable | lead team |
|---|---|---|
| eval-plan | Eval suite for an AI feature: error analysis → criteria → LLM judges → CI | Hamel Husain, Shreya Shankar, Sander Schulhoff |
| agent-workflow | Set up how you and your team build with AI agents: lanes, plan mode, autonomy ladder | Claire Vo, Boris Cherny, Aishwarya Naresh Reganti |
| ai-prototype | Idea → working prototype with AI builders: build prompts, debugging loop, user test | Lazar Jovanovic, Zevi Arnovitz, Guillermo Rauch |
| ai-product-bets | Decide which AI features to build and whether they improve as models improve | Nick Turley, Kevin Weil, Dianne Penn |
| strategy | Product strategy + moat stress test → strategy one-pager | Roger Martin, Richard Rumelt, Hamilton Helmer |
| prioritize | Confidence-scored roadmap + goals/OKRs | Itamar Gilad, Christina Wodtke, Janna Bastow |
| decide | Decision memo: eigenquestion, pre-mortem, reversibility, decision hygiene | Annie Duke, Shreyas Doshi, Shishir Mehrotra |
| spec | Shaped spec / PR-FAQ, graded | Ryan Singer, Bill Carr, Lane Shackleton |
| customer-interviews | Interview guide → synthesis (forces, jobs, opportunities) | Teresa Torres, Bob Moesta, Judd Antin |
| validate-idea | Riskiest assumptions + cheapest tests before building | Mike Maples Jr., Eric Ries, Jake Knapp |
| pmf-check | Product-market-fit diagnosis from survey/usage data + next moves | Sean Ellis, Todd Jackson, Rahul Vohra |
| price | Pricing model, packaging/tiers and willingness-to-pay plan | Madhavan Ramanujam, Naomi Ionita, Patrick Campbell |
| position | Positioning canvas + strategic narrative | April Dunford, Andy Raskin, Arielle Jackson |
| growth-model | Growth loops, activation and retention diagnosis → growth plan | Elena Verna, Casey Winters, Lauryn Isford |
| experiment | Experiment design + trustworthiness checks + readout | Ronny Kohavi, Ramesh Johari, Archie Abrams |
| metrics | North star + metric tree + review cadence | Sarah Tavel, Crystal Widjaja, Jessica Lachs |
| launch | Launch plan + story + press/distribution | Emilie Gerber, Lulu Cheng Meservey, Jason Feifer |
| b2b-sales | Founder-led sales motion: ICP, pitch, pipeline, first sales hire | Jen Abel, Geoffrey Moore, Pete Kazanjy |
| exec-comms | Exec update / memo / talk, rewritten for impact | Wes Kao, Nancy Duarte, Matt Abrahams |
| hard-conversations | Feedback / hard-conversation script | Kim Scott, Carole Robin, Alisa Cohn |
| influence | Stakeholder map + influence plan | Jessica Fain, Jeffrey Pfeffer, Hilary Gridley |
| hire | Role scorecard + interview loop + reference checks | Adam Ward, Keith Rabois, Lauren Ipsen |
| career | Career plan / promotion case / job-move decision | Phyl Terry, Nikhyl Singhal, Deb Liu |
| craft-review | Product quality review: friction log, critical journeys, taste bar | Katie Dill, Dylan Field, Stewart Butterfield |
| ship-faster | Diagnose what slows delivery → velocity plan | Farhan Thawar, Nicole Forsgren, Melissa Perri |
