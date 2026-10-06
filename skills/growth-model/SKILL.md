---
name: growth-model
description: Diagnose where your growth is actually leaking (acquisition, activation, retention, or loops) and produce a growth plan with a named loop, an activation definition, a 90-day experiment portfolio and channel guardrails. Use it when someone says growth stalled, signups don't activate, retention is flat, how do we build a growth loop, should we go PLG, onboarding redesign, churn, referral program, or which channel should we bet on. Draws on 672 insights from 143 Lenny's Podcast guests, led by Elena Verna, Casey Winters and Lauryn Isford.
---

# Growth Model

![growth-model: lead guest team](assets/card.png)

Turn 'we need more growth' into a diagnosed leak, one named loop, an activation metric and a 90-day plan. Built from 672 insights from 143 Lenny's Podcast guests. **Lead team:** Elena Verna, Casey Winters, Lauryn Isford.

## When to use
- Signups or traffic are fine but users do not reach value (activation / onboarding problem).
- Retention curves keep dwindling and nobody knows which lever to pull.
- Acquisition is concentrated in one channel (paid, SEO) or CAC keeps climbing.
- You are asked to design a growth loop, a referral program, a community, or a PLG motion.
- A sales-led B2B company wants a self-serve or product-led-sales layer.
- Leadership wants a growth team, a first growth hire, or a growth roadmap and asks where to start.
- You have a funnel export, cohort table, onboarding flow, or growth deck that needs grading.

## Step 1 — Diagnose (ask before answering)
If the user attached a funnel export, cohort CSV, onboarding screens, or a growth deck, read it first and ask only what is still missing. Max 4 questions:
1. **Does a signup cohort's retention curve flatten, and at what level?** Routes everything: if no flattening, stop and fix the product or run `pmf-check` (Verna, Ellis, Winters all say growth amplifies PMF, it cannot create it). Pre-PMF with fewer than a few hundred users routes to manual work, not a growth team (Alströmer, Caldwell).
2. **Who is the product for and how does it get used: B2B or B2C, single-player or multiplayer, time to first value in minutes, days or weeks?** Routes loops vs PLG vs sales (Hila Qu, Carilu Dietrich, Yuriy Timen).
3. **What share of new users comes from paid, SEO, and organic or referral, and where is the largest drop-off in signup to first value?** Routes channel work vs activation work (Gokul Rajaram, Grant Lee, Sean Ellis).
4. **Is this an AI-native product in a fast-moving category, and who owns growth today (team size, engineering access)?** Routes big swings vs optimization (Verna 4.0, Avasare) and staffing (Chris Miller).

State your inferred answers back in one line before proceeding.

## Step 2 — Pick the play
| If… (situation) | Use | From | Why |
|---|---|---|---|
| You cannot say which of acquisition, activation or retention is the biggest lever | **Growth accounting + instrumented funnel** (Play 1) | Naomi Gleit, Jason Cohen | Facebook found churn and resurrection lines dwarfed new users; Cohen's churn ceiling shows why growth stalls mechanically |
| Signups are healthy, few users reach value | **Derive activation metric, then rebuild first run** (Play 2) | Hila Qu, Sean Ellis, Lauryn Isford, Ben Williams | Onboarding is the choke point upstream of conversion; early-stage gains of 2-4x are common |
| Cohorts decay, churn is the story | **Early-lifecycle + tactical retention** (Play 3) | Sarah Tavel, Dan Hockenmaier, Patrick Campbell, Jackson Shuttleworth | Most cancellation is early; tactical fixes are cheap and neglected |
| Retention is decent but acquisition is paid, flat or concentrated | **Name and instrument a growth loop** (Play 4) | Elena Verna, Shishir Mehrotra, Casey Winters, Julian Shapiro | Funnels end at acquisition; loops compound and are owned |
| B2B product with individual entry and enterprise upside | **PLG fit test + product-led sales** (Play 5) | Hila Qu, Elena Verna, Carilu Dietrich | PLG volume plus a human layer for large accounts |
| Brand-new AI category with many fast competitors | **Reinvention over optimization, wow moment, giveaways as marketing** (Play 6) | Elena Verna (4.0), Amol Avasare | Perishable opportunity; activation lives in the agent |
| Pre-PMF, handful of users | **Kindle strategies and concierge onboarding** (see references) | Casey Winters, Rahul Vohra, Gustaf Alströmer | Do unscalable work; only build loops that unlock a fire strategy |
| Considering a hot new channel or influencer program | **Channel guardrails and three-ingredient test** (Play 4, step 7) | Adam Grenier, Yuriy Timen, Grant Lee | Define pass/fail before spending |

## Step 3 — Run it

### Play 1 — Baseline and leak (Gleit, Cohen)
1. Instrument every registration and onboarding step before experimenting. Naomi Gleit's team paused roadmap work for a period to do this; Bangaly Kaba's first quarter at Instagram was step-level logging. Break drop-off down by country and device (Kayvon Beykpour found an SMS verification bug this way).
2. Growth accounting, per day or week: **net growth = new users − stale users + resurrected users** (stale = no login in 30 days). Compare the size of each line; push effort to the biggest one, which is often retention.
3. Churn ceiling (Jason Cohen): **max customers = new customers per month ÷ monthly logo churn.** 100 new per month at 5% churn caps at 2,000. Cancellations scale with the base, marketing does not.
4. Plot weekly signup cohorts. You want a plateau (Tavel) or a smile curve (Balfour). Judge cohort over cohort, not absolute (Josh Miller). A dwindling curve is a leaky bucket and top-of-funnel size is irrelevant (Kaba).
5. Done when you can write: 'The biggest line is ___ (number), the leakiest step is ___ (number), the cohort curve plateaus at ___ or does not plateau.'

### Play 2 — Activation (Hila Qu, Sean Ellis, Lauryn Isford, Ben Williams)
1. **Qualitative first (Ellis):** when has a user had enough of an experience to know the product? List 2-3 candidate behaviors (first merged PR, first shared report, 5 searches plus one list).
2. **Correlate each candidate against both conversion and retention** versus the average user. If none stands out, combine actions (Hila Qu). Then run an experiment pushing users to the action to prove causation, because correlation alone gives false aha moments.
3. **Set threshold plus window, reachable in the first session or week.** Reference points: Facebook 7 friends in 10 days; Slack 3 real people and 50 real messages; Instacart 3 orders in the first month; GitLab 2 users and 2 features in 14 days; Ramp 4 events in 30 days. For team products measure at team level (Snyk: fixing vulnerabilities within 30 days of team creation).
4. **Prefer a precise, low-rate definition.** Isford: 5-15% of users is better than a loose metric because it tracks long-term retention and leaves headroom. Oji Udezue tracks three increasing thresholds and the drop-off between them.
5. **Rebuild the first run around one egg (Grant Lee).** Rules that survive across guests:
   - Ask 3-4 profile questions at sign-up and use every answer (Verna; Archie Abrams; Laura Schaffer saw +5% conversion from four dropdowns with no personalization). Route invited teammates differently from builders (Isford).
   - Start with one generic flow that serves 90%+ of users, then personalize; segment by learning and building style, not job title (Isford).
   - Mandatory setup of three screens or fewer, everything else optional and random-access (Oji Udezue).
   - Give a warm start with sample data or a template (Hila Qu); Miro takes a use-case question then drops you into a template, about five minutes end to end.
   - Do not name features in onboarding, and do not map onboarding to your pricing tiers (Isford). Do not lead with the scary step (Schaffer's pill in the hot dog).
   - Wizards: Isford's wizard was her biggest single win for a high-cognitive-load product; Oji Udezue and Shopify skip them. Use a wizard only when starting is the hard part.
6. **Expected lift:** 2-4x at early stage, 20-30% at Series B and later (Yuriy Timen); Airtable's wizard plus personalization plus education gave +20% activation over 6-8 months (Isford); curves shift 10-20 points outward (Adam Fishman).
7. **Name one owner.** Activation falls between product and marketing (Ellis, Gia Laudi).
8. Done when: one definition with threshold and window, correlation evidence, a named owner, three experiments queued.

### Play 3 — Retention (Tavel, Hockenmaier, Campbell, Shuttleworth, Cohen)
1. **Classify usage:** daily-habit, install-and-forget, or in-between. Campbell: daily workflow products and no-login-needed products churn least, the middle is death. Albert Cheng: in daily products existing-user retention becomes the bigger lever as you mature; in install-and-forget products activation is the lever.
2. **Chart cancellations by customer age.** Almost all cancellation happens in the first day, 30 or 90 days (Cohen). Fix variability in the first week or month: find customers having a bad but unrepresentative start and pull them up to average (Hockenmaier: Uber and Lyft guaranteed first-week earnings).
3. **Make the product get better with use and cost more to leave** (Tavel level 2): personalization from the core action, stored value, non-transferable reputation or audience (Shapiro's building state). Then add re-engagement loops where one user's action pulls a dormant user back (level 3).
4. **Habit mechanics only if the core loop is already wanted** (Shuttleworth). Duolingo specifics: define the streak on the true unit of use; retention rises daily through day 7 then loss aversion kicks in, so aim experiments at a 7-day streak; two free freezes early beat one, three were no better; Earn Back beat paid repair; send the reminder 23.5 hours after last practice; an 8-word plain explainer of the streak was a top-three retention win.
5. **Tactical retention (Campbell):** failed-payment recovery, cancellation flow and offboarding are about 25-40% of churn and take about two months. Cancellation flow: two multiple-choice questions, why are you leaving and what did you like. Add pause as a temporary option (Crystal Widjaja).
6. **Diagnose real churn reasons.** *Too expensive* and *project ended* are proximate, never the real reason (Cohen). Interview churned users about what changed in their context (Bob Moesta). Contact at-risk customers before they cancel (Cohen). Stop churn by acquiring customers who do not leave (Madhavan Ramanujam).
7. **Benchmarks:** D1 retention 30-40% is solid for a consumer app (Cheng); consumer subscriptions need annual retention north of 60-70% (Winters); high-frequency products show 30-50% three-month retention at PMF (Uri Levine); freemium-converted customers retain 10-20% better than trial-converted (Campbell).
8. **Sequence:** do not start with resurrection; churned users already decided against you (Hockenmaier). Do not copy what your best users do (Hockenmaier). Mature products with large dormant pools need a dedicated returning-user experience (Cheng).
9. Done when: a retention lever list ranked by size, the first-week variability fix identified, and the churn reason list rewritten without 'too expensive'.

### Play 4 — Loops and channels (Verna, Mehrotra, Winters, Shapiro, Timen)
1. **Draw your loop:** an action produces a reaction that produces another action, self-contained (Verna). Find it in how you pitched your last few candidates (Shishir Mehrotra). Name each loop; Coda draws a Black Loop (create, share, teammates create) and a Blue Loop (create, publish, strangers discover).
2. **Check it is real:** does utility rise with more users in your segment? Network effects are either inherent or absent (Timen). One-to-many relationships (Slack, Miro) make product-led acquisition possible; single-user tools like Snowflake do not (Verna). Referral is an accelerant for a product people already talk about, not a fix (Ellis).
3. **Instrument entry points separately.** Teammate share activates best, published content second, cold top of funnel worst (about one in five reach activation) (Mehrotra).
4. **Work both ends:** optimize the sender experience and the recipient experience (Dropbox: over 50% of acquisition via sharing, run by a dedicated pod). Billboard the product with signatures and shareable links (Shapiro).
5. **Bridge into the account:** present teammates from an existing company domain with an option to join that account (Verna); give users a reason to show output to a manager (B2B report sharing).
6. **Plan the second loop now.** New loops take 6-18 months to produce visible revenue, most spin out in 5-7 years, so introduce something new roughly every 18 months (Verna). Casey Winters: scalable acquisition via a loop is a requirement for PMF, so design it in before PMF.
7. **Channel guardrails.** Before spending, set minimum impressions, 2-3 creative angles and a target CTR range; abandon or continue on those numbers (Timen). Before a hot new channel, score the medium's strengths against customer need, the channel's own trajectory and monetization, and your risk appetite and current Google/Facebook volume (Grenier; new channels pay off about 5% of the time).
8. **Mix thresholds:** 40-50% of new customers organic is healthy (Rajaram); paid above 50% means the core engine is broken (Grant Lee); never start paid before you can compute LTV (Gina Gotthilf); optimize on incrementality, not attribution (Abrams); one channel above 80% is fine while volume is small, but past about $50M ARR with 90% in one channel, carve out resources to diversify (Timen).
9. Done when: one loop drawn with named edges and a metric per edge, entry-point activation measured separately, one channel test with pass/fail numbers written down.

### Play 5 — PLG fit and product-led sales (Hila Qu, Verna, Dietrich)
1. **Why do you want to be product led?** Name the outcome: top-of-funnel demand, constrained CS or implementation capacity, or revenue efficiency; map it to a journey stage (Chris Miller).
2. **Fit test (Hila Qu):** low complexity, short time to value (days, not weeks), a large pool of end users who can try without boss approval. Add Merci Grace's day-zero value test: if the pitch is that you'll be glad in six months, reconsider PLG.
3. **Readiness checklist:** a free vehicle (free tier, trial, open source or realistic demo, not only a Book demo button), fast time to value, self-checkout, a data foundation, simple pricing. Start with activation, then checkout conversion, then PQL/PQA, then product-led acquisition only if there is a collaboration workflow.
4. **Two conversion paths:** low-priced usage buys by card; high-usage accounts that match ICP get a sales or CS touch (Hila Qu). Engage sales only after a threshold such as 20-40 engaged users paying by card (Dietrich).
5. **PQA window (Verna):** hit the account across every channel when it enters the window, sunset outreach if you do not connect, wait for the next window.
6. **Escalator (Verna):** write the individual job, team value and enterprise value; sales exists because products communicate enterprise value badly, so push the product up the escalator over time.
7. **Staff it:** a dedicated team with engineering, design and data; assigning PLG to one person is the classic failure (Hila Qu, Chris Miller). Do not slice up the enterprise product; start from self-serve users' own problems (Schaffer).
8. Done when: fit test scored, hybrid motion drawn, threshold for sales engagement written down.

### Play 6 — AI-native category (Verna 4.0, Avasare, Turley)
1. Shift mix toward larger swings (Avasare: 50-70% big swings if an improving model underlies core value; Verna: about 95% innovation at Lovable).
2. Target a wow moment, not an aha: first generation, first preview (Verna). Activation lives in the agent team, so improving intent understanding lifts every session.
3. Treat free usage and LLM cost of giveaways as marketing spend, but still build a retention strategy (Verna).
4. Close capability overhang: models improve faster than users find what they can do; build on-ramps to newly unlocked uses (Avasare).
5. Retention gains split roughly into thirds: model quality, product-research capabilities (search, memory), classic product work (Nick Turley).

## Where the experts disagree
1. **Optimize the funnel vs reinvent.** *Camp A* (Sean Ellis, Deb Liu, Adam Fishman, Mayur Kamat): compound many small tests, fix activation first. *Camp B* (Elena Verna 4.0, Amol Avasare, Brian Chesky): big swings and new loops. *Use A when* the business is scaled and stable; *B when* the category is new and perishable. Default: 70/30 small to large, flip it if a model underpins your value.
2. **Remove friction vs add the right friction.** *Camp A* (Scott Belsky, Nikita Bier, Sam Schillace): users are lazy, show value in seconds. *Camp B* (Elena Verna, Laura Schaffer, Kristen Berman, Nickey Skarstad, Adam Fishman): questions and filtering raise activation and retention. *Use A for* simple, high-intent products; *B for* complex or B2B products. Default: cut every step that does not help comprehension, add 3-4 profile questions, and watch conversion and retention together.
3. **Engineer virality vs earn word of mouth.** *Camp A* (Elena Verna, Drew Houston, Shishir Mehrotra, Julian Shapiro): design loops into the product. *Camp B* (Rahul Vohra, Oji Udezue, Yuriy Timen, Chris Miller): virality cannot be manufactured; B2B rarely has tight loops. *Use A when* use of the product inherently exposes it to non-users; *B otherwise*, with a macro flywheel of value before extraction. Default: loop only on inherent multiplayer edges.
4. **Pure PLG vs hybrid.** *Camp A* (Elena Verna on product owning monetization, Atlassian's low-sales model per Carilu Dietrich): product sells. *Camp B* (Pete Kazanjy, Jeanne DeWitt Grosser, Geoffrey Moore): self-serve has a ceiling and cannot cross the chasm alone. *Use A for* developer and SMB entry; *B before* self-serve revenue hits its ceiling. Default: hybrid with usage-threshold handoff.

## Deliverable
```markdown
# Growth Plan: <product>, <date>

## 1. Diagnosis
- Stage / motion: <pre-PMF | post-PMF | scaling>, <B2B|B2C>, <single|multi-player>
- Retention curve: <plateaus at X% | no plateau>   (if no plateau: stop, fix product)
- Growth accounting (per week): new <n> − stale <n> + resurrected <n> = <net>
- Churn ceiling: <new/month> ÷ <churn> = <max customers>
- Biggest lever: <acquisition | activation | retention | expansion> because <number>

## 2. Activation
- Definition: <behavior, threshold, window>   Evidence: <correlation with conversion and retention>
- Current rate: <x%>   Target: <y%>   Owner: <name>
- First-run changes: <3 bullets from Play 2>

## 3. Loop
- Primary loop (named): <action → reaction → action>   Metric per edge: <...>
- Entry-point activation: teammate <x%> | publish <x%> | cold <x%>
- Second loop to start by <date>: <...>

## 4. Channels
| Channel | Share of new users | Test guardrails (impressions / angles / CTR) | Decision date |
- Organic share target: <40-50%>   Paid cap: <50%>   Payback guardrail: <months>

## 5. 90-day experiment portfolio
| # | Hypothesis | Lever | Size (big swing / small) | Metric | Kill criteria |
(aim for about 10 per sprint batch; keep a backlog of 100 hypotheses)

## 6. Org and ownership
- Growth team staffing, DRI for activation, marketing-to-product handoff owner

## Next 3 actions
1. <this week: instrument or pull cohort data>
2. <this sprint: ship the first activation experiment>
3. <this quarter: stand up the loop and review at day 90>
```

## Grade existing work
Score each 1-5 (1 / 3 / 5 anchors), total /40.
| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Retention precedes acquisition (Verna, Ellis) | Spending on traffic with no cohort plateau | Plateau known, not acted on | Cohorts plateau and improve cohort over cohort (J. Miller) |
| Leak diagnosis (Gleit) | Anecdote or vanity totals | Funnel with step drop-offs | Growth accounting plus per-screen, per-country drop-off |
| Activation definition (Qu, Isford, Ellis) | Signed up or logged in | Behavior chosen by gut | Threshold plus window, correlated with retention, tested causally |
| Onboarding design (Isford, Udezue, Belsky) | Feature tour, names features | Some personalization | One-egg first run, profile questions used, route by role |
| Loop specificity (Verna, Mehrotra) | Funnel only | Loop described, not measured | Named loop, edge metrics, entry points split |
| Channel discipline (Timen, Rajaram, Lee) | One channel, no guardrails | Several channels, vague tests | Pass/fail guardrails, organic 40-50%, paid under 50% |
| Retention levers (Tavel, Campbell, Hockenmaier) | Email nudges | Cohort charts, generic fixes | Early-lifecycle fix, tactical churn recovery, habit loop |
| Ownership and portfolio (Qu, Miller, Deb Liu) | One person, no resources | Team exists, no batch plan | Dedicated team, DRI per surface, big and small bets |
Output: score per criterion, total, then **top 3 fixes**, each naming the guest and framework behind it.

## Red flags
- A roadmap line item that says simplify onboarding: it is a solution, not a problem (Verna).
- Hiring a head of growth with no engineering, design or data and a big number (Chris Miller).
- Adding Google or Facebook sign-in as a growth tactic: it is customer experience, not incrementality (Verna).
- Naming features in onboarding, or onboarding to premium tiers (Isford).
- Making everyone copy what best users do, or launching resurrection before the new-user experience is fixed (Hockenmaier).
- Referral incentives layered on a product nobody talks about (Ellis, Julian Shapiro).
- One channel above 80-90% of new users at scale; SEO as a live-by-the-sword channel (Noam Lovinsky, Timen).
- Paid acquisition before LTV is known, or optimizing lowest cost per lead (Gotthilf, Becker).
- Assigning PLG to one person or treating a free trial as the whole motion (Hila Qu).
- Growth hacking, A/B tests and analytics for a startup with no customers (Dalton Caldwell).
- Accepting too expensive as the churn reason (Cohen).
- Streak or gamification on a core loop users do not already want (Shuttleworth).

## Receipts
- "scalable acquisition or what we call an acquisition loop is a requirement for product market fit." — Casey Winters, Lenny's Podcast (00:49:12)
- "never start with product led acquisition. You first always have to start with product led retention, activation, and engagement." — Elena Verna, Lenny's Podcast (00:34:00)
- "if you ever have a line item on your roadmap that says simplified onboarding, please cross it out." — Elena Verna, Lenny's Podcast (01:12:48)
- "I would much prefer to pick a more specific, more precise metric that maybe only 5% of users reach, but know that those 5% of users will be with us for the long haul" — Lauryn Isford, Lenny's Podcast (00:26:38)
- "customer acquisition is so hard that if you're not really efficient at converting and retaining and monetizing people, you're going to really struggle on the customer acquisition side." — Sean Ellis, Lenny's Podcast (00:27:00)
- "cancellations automatically grow as you grow, even if you're doing everything right, but marketing doesn't." — Jason Cohen, Lenny's Podcast (00:14:58)

## Go deeper
- `references/frameworks.md` — every framework in this skill, how to run it
- `references/quotes.md` — verified quotes with timestamps
- Related skills:
  - `pmf-check` — hand off first when the retention curve does not plateau.
  - `experiment` — hand off to design and read out the tests this plan queues.
  - `metrics` — hand off for the north star and metric tree once the activation definition is set.
  - `price` — hand off when the free/paid fence or expansion packaging is the bottleneck.
  - `position` — hand off when users do not understand who the product is for at the front door.
