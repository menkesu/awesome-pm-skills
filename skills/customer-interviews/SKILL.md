---
name: customer-interviews
description: Designs customer interviews and turns the transcripts into decisions. Produces an interview guide plus a synthesis (forces of progress, jobs, pathways, opportunities) you can paste into a doc. Use for 'customer interviews', 'discovery calls', 'JTBD', 'switch interview', 'who should I talk to', 'how many interviews', 'synthesize these transcripts', or 'why do customers churn/buy'. Draws on 140 Lenny's Podcast guests incl. Teresa Torres, Bob Moesta and Judd Antin.
---

# Customer Interviews

![customer-interviews: lead guest team](assets/card.png)

Go from 'we should talk to customers' to a guide, a recruiting plan and a synthesis that changes a decision. Built from 312 insights from 140 Lenny's Podcast guests. **Lead team:** Teresa Torres, Bob Moesta, Judd Antin.

## When to use
- You are about to run discovery and want the guide, the recruiting plan and the sample size.
- You have transcripts, call notes or a survey export and need forces, jobs and opportunities out of them.
- Churn, conversion or adoption is off and the dashboard cannot say why.
- A PM asked a researcher for 'a quick study to validate' something (grade the request first).
- You are pre-product and need to learn the job before building (B2B or consumer).
- You need to stop 'research theater': lots of calls, no changed decisions.
- You want weekly discovery to survive past the first month.

## Step 1 — Diagnose (ask before answering)
If the user attached a guide, transcripts, a survey or a research request, read it first and skip questions it answers. Ask at most these four:
1. **What decision will this change, and by when?** Routes the research altitude (Judd Antin's macro / middle-range / micro). No decision means do not run it.
2. **Did customers recently switch, buy or cancel, or is the product habitual with no real choice?** Routes switch interview (Bob Moesta) vs observation.
3. **Pre-product, live product, or a metric you cannot explain? B2B (how many accounts) or consumer at scale?** Routes sample size, recruiting channel and whether to ship-and-measure instead (Casey Winters, Keith Rabois).
4. **Who can you reach this week, and do you already have recordings?** Routes recruiting automation vs synthesis-only.

## Step 2 — Pick the play
| If… (situation) | Use | From | Why |
|---|---|---|---|
| Existing product; why do people buy, switch, churn | Switch interview + forces of progress | Bob Moesta | Reconstructs the buying story; clusters into pathways, not segments |
| Ongoing discovery, want opportunities for the roadmap | Story-based interview + weekly automated recruiting | Teresa Torres | One prompt, past behavior, sustainable cadence |
| Pre-product, B2B, idea stage | Call 10 customers yourself, watch the workflow, then test dollars | Jag Duggal, Gustaf Alstromer, Todd Jackson | Raw exposure; pain intensity seen, not asked; extreme value then ability then willingness to pay |
| Zero-to-one, no customers yet | Interview switchers of the alternatives (eBay/Etsy sellers style) | Bob Moesta | Only people who already tried to make the progress can tell the story |
| Metric moved or an experiment failed, cause unknown | Anomaly to session replay, then call the users; interview funnel failures and non-users | Laura Schaffer, Jessica Lachs, Uri Levine, Mihika Kapoor | Data says where, people say why |
| Habitual or no-choice product | Observation, use-occasion questions, do the user's job | Moesta, Gustaf Alstromer, Adriel Frederick | Switch stories do not exist; behavior must be watched |
| Large inbound signal volume (NPS, tickets, G2, calls) | Customer listening / feedback river with LLM clustering | Oji Udezue, Shaun Clowes | Triage what already arrives before scheduling more calls |
| Research request arrives late ('validate our plan') | Reframe to falsify; classify macro / middle / micro | Judd Antin | Late validation is user-centered performance |

## Step 3 — Run it

### A. Frame and recruit (before any call)
1. Write the **decision** and a **crisp hypothesis** with the reaction that would count as real excitement (Jag Duggal). Be the judge, not the lawyer, of your hypothesis.
2. Write predictions of what you expect to hear. Compare after; this kills the 'we knew that already' reaction (Judd Antin on hindsight bias).
3. **Who to recruit:** people who recently bought, switched or cancelled; best customers who signed up 3 to 6 months ago so they still remember life before (Georgiana Laudi). Add non-users, churners and funnel drop-offs (Mihika Kapoor, Chris Miller, Uri Levine). In B2B include the economic buyer, not only end users (Geoffrey Moore). For lighthouse learning pick customers living in the future (Mike Maples Jr.).
4. **Skip:** friends and family (Grant Lee, Jeff Weinstein discounts friend feedback to zero), and anyone paying nothing if you want signal about value (Daniel Lereya).
5. **Sample size by purpose:** 10 to 12 per round, two rounds beat one of 24 (Moesta); 7 to 14 for a single segment (Shaun Clowes); 25 to 50 to find an idea (Gustaf Alstromer); 20 to 30 key accounts driving 80 to 90 percent of revenue for willingness to pay (Madhavan Ramanujam). **Stop when you can predict 70 to 80 percent of the next answer** (Todd Jackson, Nick Turley).
6. **Automate recruiting** so the interview is already on the calendar: in-product intercept ('Do you have 20 minutes to talk to us?') plus scheduling link (Torres); Gong keyword alert to Slack to Zapier to Calendly (Kevin Yien); booking prompt inside the activation flow because churned users will not come to you (Oji Udezue); three template emails a week to hypothesis-selected users (Zoelle Egner). Floor: one interview a week (Torres); founder target: 20 to 30 percent of time on customer calls (Dalton Caldwell).

### B. The interview guide (short, story-first)
Torres and Moesta both reject the long protocol. Moesta's version: no discussion guide, the four forces as the frame. Use a one-page skeleton, not a script:
1. **Open on the story.** *Tell me about the last time you [bought / switched / tried to do X].* (Torres). Never *what are your top three problems* (Gokul Rajaram).
2. **Set the scene.** *Where were you, who were you with, what else was going on?* Context is what makes behavior rational (Moesta).
3. **Find the trigger (push).** *What happened that made today the day?* For adoption: *Why do you use it? Where were you?* (Robby Stein).
4. **Walk the timeline.** *What happened next?* repeated, instead of why-why-why (Torres). Move forward, summarize, return to the moment you want more of.
5. **Probe the four forces.** Push (what was wrong with the old way), pull (what the new one promised), anxiety (what worried you, what did you give up), habit (what kept you where you were). Add: *how did you convince someone else?* and *what were deal breakers?* (Moesta, Laudi).
6. **Reconstruct hire and fire criteria.** *What did you try, who influenced you, what did you compare it to?*
7. **Close.** *What can you do now that you could not before?* (Laudi) and *What questions should I have asked you?* (Christina Wodtke).

**Rules in the room**
- Past behavior only. No *would you*, no hypotheticals, no *what keeps you up at night* or *magic wand* (Jen Abel). Behavior is the measure (Torres).
- Do not pitch or demo first; sit in silence (Jeff Weinstein). Sellers talk well under half the time (Jeanne Grosser).
- Say 'tell me more about that' or 'give me an example' rather than repeated whys; avoid why when it sounds scolding (Moesta, Carole Robin). For cancellations ask *what made you cancel* rather than why (Jason Cohen).
- **Layers of language** (Moesta): first answer is pablum ('it was good'), then fantasy or nightmare exaggeration, then what actually happened. Ask one more question and pull back to dates and events.
- At the edge of language, bracket ('more this or more that') or play the story back slightly wrong so they correct you (Moesta).
- Feel the emotional consequence: keep asking until you reach the moment they felt bad (Nan Yu).
- Treat 'interesting' as a no; real interest is a wow reaction or a request for the deck or another meeting (Todd Jackson). Check the face: eyes lighting up is data (Wes Kao).
- Ask for the reference or the review to expose hesitation (Christian Idiodi).
- PM and designer attend, or cancel the call (Marty Cagan). Engineers behind the glass (Judd Antin, Christine Itwaru); a live Slack thread captures reactions (Noah Weiss).
- Do not summarize with AI instead of attending (Peter Deng). Real humans for usability, not simulated users (Simon Willison).

### C. Synthesize (within 24 hours of each call, then across calls)
1. **Story card per interview** (template below): trigger, timeline, four forces, hire and fire criteria, alternatives, who influenced, quote.
2. **Cluster stories into pathways**, not themes or demographic segments (Moesta). A pathway is a set of reasons that go together.
3. **Name conflicting jobs** inside pathways and decide which one to serve. People have jobs; products and organizations do not (Moesta).
4. **Write the job statement:** *When I am in [situation], help me [motivation], so I can [outcome]* (Laudi). Capture functional, emotional and social energy (Moesta); do not skip the emotional job (Robby Stein, Adam Fishman).
5. **Convert to opportunities** (Torres): customer needs, pains and desires framed specifically, not solutions; pull one shared structure (an experience map) out of unique stories.
6. **Check for say-do gaps:** compare stated wishes to trade-offs actually made (Moesta's Energy Star example: 93 percent said they wanted it, nobody paid). Discount stated unwillingness that contradicts behavior (Merci Grace on invites).
7. **Weigh, don't obey:** segment feedback by whether the person values your core benefit; deliberately ignore the rest (Rahul Vohra). Expect about 20 percent of design-partner feedback to be new (Jen Abel).
8. **Triangulate:** counts from tickets, NPS verbatims, session replay (Oji Udezue, Laura Schaffer). When surveys and instrumentation disagree, investigate the survey first (Nicole Forsgren). An LLM can cluster across transcripts after you have read the stories (Dan Shipper, Shaun Clowes).
9. **Report what, so what, then what** and propose experiments, not a build order (Judd Antin).

## Where the experts disagree
**1. Open stories vs hypothesis and prototype.** *Open, no pitch:* Teresa Torres, Bob Moesta, Jeff Weinstein. *Bring a hypothesis and prototype:* Jake Knapp, Jag Duggal, Mihika Kapoor (go in with an A- idea). → Open when you do not know the job or problem; prototype when you have a candidate solution and need reasons they will not use it (Marty Cagan). **Default:** story interviews first, concept test in a separate session so the pitch never anchors the story.

**2. Talk to customers vs ship and measure.** *Talk:* Torres, Duggal, Kevin Yien (raw material, not reports), Cagan. *Do not, outside enterprise:* Keith Rabois. *Research is scarce:* Casey Winters, Ebi Atawodi. → Talk for enterprise, high uncertainty, or a stalled metric; ship and measure for consumer-scale, well-trodden problems. **Default:** do the one-a-week floor, reserve deep rounds for big and poorly understood problems.

**3. JTBD as the frame vs JTBD as dogma.** *Use it simply:* Moesta, Georgiana Laudi, Paul Adams, Robby Stein. *It breaks:* Sriram Krishnan and Aarthi Ramamurthy (trade-offs between users in networks and marketplaces), Kayvon Beykpour (religious rollout at Twitter). → Single buyer with a purchase decision: switch interview. Multi-sided products: use it for the V1 hypothesis and add explicit trade-offs. **Default:** forces and job statement as a lens, never the governing rule.

**4. Sample size.** Moesta 10 to 12, Clowes 7 to 14, Alstromer 25 to 50, Ramanujam 20 to 30 key accounts. → Causal mechanisms: small rounds; idea finding or willingness to pay: wider. **Default:** rounds of 10 to 12 and stop on predictability.

## Deliverable
Produce both, fenced, ready to paste.

```markdown
# Interview Plan: <topic>
**Decision this changes:** <decision, owner, date>     **Altitude:** macro / middle-range (framed to a metric) / micro
**Hypothesis + what real excitement sounds like:** <...>     **Predictions (write before calls):** <...>
**Who:** <recent switchers / best customers 3-6 mo / non-users / economic buyer>   **Not:** <friends, free users>
**Sample:** <N per round, stop rule>   **Recruiting:** <channel + automation + weekly cadence>
**Guide (one page):** 1 story open | 2 scene | 3 trigger | 4 timeline | 5 four forces | 6 hire/fire | 7 close
**In the room:** <PM, designer, engineer attending; Slack thread>

# Synthesis: <topic>
## Story cards
| # | Who / context | Trigger (push) | Pull | Anxiety | Habit | Hire / fire criteria | Alternatives | Key quote |
## Pathways (clusters of stories)
| Pathway | Stories | Reasons that go together | Job statement: When I..., help me..., so I can... |
## Conflicting jobs and which we serve: <...>
## Opportunities (needs, not solutions)
| Opportunity | Evidence (stories) | Say-do check | Next experiment |
## Predictions vs actual: <what surprised us>
## What, so what, then what: <3 bullets>
## Next 3 actions
1. <...>  2. <...>  3. <...>
```

## Grade existing work
Score a guide, a research request or a synthesis. 1 = weak, 3 = partial, 5 = strong.
| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Decision link (Antin) | No decision named; validate-our-idea | Decision named, late in process | Decision, owner, date; framed to funnel or OKR; asks how we might be wrong |
| Past behavior (Torres) | Opinions, hypotheticals, top-3 problems | Mixed | Last-time stories with a timeline |
| Right people (Moesta, Laudi) | Friends, any user | Customers but not recent | Recent switchers, best customers 3-6 months, non-users, economic buyer |
| Leading and pitching (Weinstein, Todd Jackson) | Pitch first, happy ears | Some leading questions | Non-leading, silence, interest read by behavior |
| Depth (Moesta, Nan Yu) | Stops at pablum | Some follow-up | Layers peeled; forces and emotional consequence found |
| Synthesis (Moesta, Torres) | Themes and a quote deck | Themes plus forces | Pathways, job statements, opportunities not solutions |
| Sampling and stop rule | One call or 50 with no rule | Fixed N | Rounds of 10 to 12, predictability stop |
| Cadence and team (Torres, Cagan) | One-off, researcher-only | Quarterly goal | Weekly, automated recruiting, PM and designer attend |

Output: score per criterion, total out of 40, and the **top 3 fixes** each tied to the guest and framework behind it.

## Red flags
- **User-centered performance:** research that signals customer obsession, not a decision (Judd Antin). Executive listening sessions are mostly performance too.
- **Research theater:** talking to the people you always talk to and learning nothing new (Shaun Clowes).
- **Happy ears and polite interest:** founders hear only what supports them (Todd Jackson, Raaz Herzberg).
- **Fifty-question protocols and what would you do questions** (Torres).
- **Building what they ask for:** requests hide the real problem; ask why and build one scalable fix (Annie Pearl, Yuhki Yamashita, Janna Bastow). Say-do gap (Kristen Berman).
- **Multiple-choice cancellation lists:** randomized order produced equal picks, pure noise (Jason Cohen).
- **Delegated or filtered research:** reports are bent glass (Kevin Yien, Dmitry Zlokazov).
- **Anecdote lock-in:** 'I talked to eight customers' sticks in everyone's head (Keith Rabois). Present patterns, not stories.
- **Friends, family and dogfooding as customer proxies** (Grant Lee, Paige Costello, Alexander Embiricos).
- **Tenured-PM complacency:** customers' lives keep changing (Kevin Yien).
- **Reacting to every raw note** (Vijay Iyengar): keep a small escalation channel (Yuhki Yamashita's Concerning Tweets).

## Receipts
- "if F1 and F2 are not greater than F3 and F4, they're not going to move, they're not going to do anything." — Bob Moesta, Lenny's Podcast (00:12:34)
- "The real measure is tell me about your behavior. What did you actually do?" — Teresa Torres, Lenny's Podcast (39:57)
- "it starts to repeat around seven or eight. And I usually do 10, no more than 12. And I would rather do two rounds of 12 interviews than do 24 interviews." — Bob Moesta, Lenny's Podcast (00:27:07)
- "It's work we do to signal to each other how customer obsessed we are, not because we want to make a different decision." — Judd Antin, Lenny's Podcast (00:24:11)
- "Can I make it so that when you wake up on Monday morning, there's an interview on your calendar and you literally did nothing to get it there?" — Teresa Torres, Lenny's Podcast (26:35)
- "The word interesting is a polite way of saying no, right? And so I'm either looking for wow statements or I'm looking for demonstrated behavior that shows interest." — Todd Jackson, Lenny's Podcast (01:18:06)

## Go deeper
- `references/frameworks.md` — every framework in this skill, how to run it
- `references/quotes.md` — verified quotes with timestamps
- Related skills:
  - `validate-idea` — when interviews surface a candidate bet and you need the cheapest test.
  - `prioritize` — to turn the opportunity list into a confidence-scored roadmap.
  - `position` — to turn pathways and the job statement into positioning and messaging.
  - `price` — when the open question is willingness to pay.
