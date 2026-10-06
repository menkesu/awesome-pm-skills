---
name: price
description: Builds a pricing model, packaging/tier structure and willingness-to-pay research plan, then grades your existing pricing page or plan. Use when you ask 'how much should we charge', 'what should our pricing model be', 'seat vs usage vs outcome pricing', 'good-better-best tiers', 'what goes in the free plan', 'should we raise prices', 'freemium vs free trial', or 'how do we price our AI product'. Draws on 199 insights from 79 Lenny's Podcast guests including Madhavan Ramanujam, Naomi Ionita and Patrick Campbell.
---

# Price

![price: lead guest team](assets/card.png)

Turn a vague "what should we charge?" into a pricing model, a tier structure and a willingness-to-pay test you can run this week. Built from 199 insights from 79 Lenny's Podcast guests. **Lead team:** Madhavan Ramanujam, Naomi Ionita, Patrick Campbell.

## When to use
- You are about to launch and the price is a guess (or copied from a competitor).
- You have one plan, or one clump of customers on the entry tier, and suspect money is left on the table.
- You are choosing seat vs usage vs hybrid vs outcome pricing, especially for an AI product.
- You are designing the free tier, trial or reverse trial, or the free-to-paid paywall.
- You want to raise prices and need evidence, a test, or political cover.
- Enterprise deals are discounted to close, or win rate looks too good.
- You have a pricing page, deck or spreadsheet and want it graded.

## Step 1 — Diagnose (ask before answering)
If the user attached a pricing page, plan matrix, price list, survey CSV, deck or repo, read it first and infer as much as you can. Ask only what is still missing (max 4):

1. **How do customers buy: self-serve card, sales-led, marketplace, or consumer app?** Routes to freemium/checkout plays (self-serve), deal-size plays (sales-led) or take-rate plays (marketplace). Self-serve card monetization caps around $10,000 a transaction (Elena Verna), so above that you need a sales motion.
2. **Is the price a guess, or do you have live data (conversion, plan mix, win rate, churn)?** Guess means run willingness-to-pay research. Data means diagnose the symptom (entry-tier clump, win rate above 35%, guilt-driven upgrades).
3. **Is it an AI product? If so, does it do work autonomously, can you prove impact on the customer's KPI, and what is the marginal inference cost?** Routes to the Attribution x Autonomy 2x2 and decides whether a flat low price is survivable.
4. **What is the goal: revenue, growth/share, or enterprise land?** Growth-first categories (Lovable-style) and venture-scale enterprise want different answers, and the experts split here.

## Step 2 — Pick the play
| If… (situation) | Use | From | Why |
|---|---|---|---|
| Pre-launch or price was guessed | Van Westendorp 4 questions plus range test (Play 1) | Rahul Vohra, Naomi Ionita, Nick Turley, Mike Maples Jr. | Cheap, runs in days, and reveals the cliff before you commit |
| AI product, choosing the model | Attribution x Autonomy 2x2 (Play 2) | Madhavan Ramanujam | Matches the model to how provable and autonomous the work is |
| SaaS or PLG, price does not scale with customer value | Value metric first, then hybrid quota (Play 3) | Patrick Campbell, Naomi Ionita | Highest-leverage pricing decision; lowers churn and lifts expansion |
| One plan, or 60-70% on the cheapest tier | Leaders, fillers, killers plus decoy tier (Play 4) | Madhavan Ramanujam | Packaging fixes need no product change and can lift ARPU 30%+ |
| Freemium or trial design, weak free-to-paid | What to make free, three pillars, reverse trial (Play 5) | Naomi Ionita, Elena Verna, Lauryn Isford | Most free users do not know what the paid plan sells |
| Want to raise prices on a live product | Raise-until-signups-move, plus earn-the-increase check (Play 6) | Jason Cohen, Patrick Campbell, Jason Lemkin | Most prices are guesses that were never revisited |
| Sales-led enterprise pricing | 75-150K land, co-author with the champion (Play 7) | Jen Abel, Naomi Ionita | Small lands anchor the account and wreck expansion |
| Downturn, buyers will not commit | De-featured alternative, value trades, model switch | Madhavan Ramanujam, Sahil Mansuri | A discount becomes the new price |
| Marketplace take rate | Price off incrementality and cost-to-serve | Jason Droege, Nilan Peiris, Ramesh Johari | Take rate has no simple demand curve; flat cuts invite disintermediation |

## Step 3 — Run it

### Play 1 — Find the price (willingness-to-pay research)
1. **Position first.** Decide the category and who you are best for (Rahul Vohra: positioning before pricing). Best-in-class for the high end means price near the expensive point; marketplaces and land-grabs orient on the bargain point.
2. **Interview dozens of customers** with product and product marketing. They will not name a price outright, so anchor on relative value against a related spend (Julia Schottenstein: dbt versus warehouse cost; customers valued it at 20-35% of that spend).
3. **Ask the four questions after pitching value as you would post-launch** (~100 early users is enough; Superhuman did this, Nick Turley did it with a Google Form on Discord for ChatGPT's $20):
   - *At what price is it so expensive you would not consider it?*
   - *At what price is it so cheap you would doubt the quality?*
   - *At what price does it start to feel expensive?*
   - *At what price is it a bargain?*
   Quick variant (Madhavan Ramanujam, Todd Jackson): ask acceptable, expensive, prohibitively expensive. Todd Jackson treats the expensive answer as the realistic price, because the fair answer is deal-seeking.
4. **Plot the curves and find the cliff.** At scale, demand drops at psychological thresholds (e.g. 99 to 101 shows 20-30% more calling it expensive; common $29-30 a month, 9.99). Price just under the cliff; retest when you add add-ons or usage components.
5. **Test a range, not one number.** Fake-door page that 404s at checkout, show prices well above your hypothesis (Chegg tested up to $75 against a $35 guess).
6. **Gut-check market size.** Target ARR for your valuation divided by price equals subscribers needed (Superhuman: 300K subscribers at $30 a month toward $1B).
7. **Stretch exercise:** ask what the $1,000 or $10,000 a month version would be (Anish Acharya's Birkin bag) and what it would need to do.
8. **Done when:** you can state a price, the cliff above it, and the one-line value story (a dollar a day for four hours back a week, or Nest's $249 that saves $800-1,200 a year).

### Play 2 — Choose the model for an AI product (Attribution x Autonomy)
1. Score **attribution** (can you prove impact on the buyer's KPI?) and **autonomy** (is a human in the loop?).
2. Read the quadrant: low/low is seat or subscription; high attribution, low autonomy (copilot like Cursor) is hybrid seats plus credits; high autonomy, low attribution is usage-based; high/high is outcome-based (Intercom Fin, 99 cents per AI-resolved ticket, charged only when no human intervenes).
3. **Derive outcome price from value, not cost.** Research what customers pay per outcome today ($20-30 per human-resolved ticket for SaaS, about $5 consumer), test points, and treat cost as your problem (Eoghan McCabe; Bret Taylor agrees: tokens are not outcomes).
4. **Do not rush.** Outcome pricing without provable attribution fails; build KPI dashboards and value audits first, then agentic workflows (Madhavan Ramanujam's roadmap). Outcome-based AI firms capture 25-50% of value versus 10-20% typical for SaaS.
5. **If inference is expensive, a flat low price breaks.** Bolt's flat $9 plan was burned in 48 hours and users begged to pay more; tiered usage shipped in under a week (Eric Simons).
6. **Done when:** you have named your quadrant, the single KPI you will attribute to, and what must change before you move quadrants.

### Play 3 — Pick the value metric
1. List candidate units customers associate with value (users, projects, messages, monthly tracked users, resolutions).
2. Keep the metric that (a) scales with customer size and value, (b) you can track and customers agree on (usage pricing without trackable metrics is a bad idea, Madhavan Ramanujam), (c) lets accounts upgrade automatically so you replace manual upsell pitches (Patrick Campbell: churn about 20-25% lower, expansion roughly doubled).
3. **Prefer hybrid:** a fixed good/better/best subscription with a quota on the value metric, quota-hit as the upgrade trigger (Naomi Ionita; only about 5% of SaaS is pure usage because CFOs want predictability).
4. Choose subscription when bills must be predictable or value is ongoing; usage when commitment must be low, value is intermittent, or costs scale with use.
5. For two-sided growth, use a value matrix: per-user price falls as both seats and departments rise.
6. **Done when:** a customer could predict their bill and your best accounts naturally pay more as they succeed.

### Play 4 — Package and tier
1. Run a most/least (MaxDiff) feature ranking, or a 100-point allocation across features (Naomi Ionita).
2. Classify: **leaders** (must-have), **fillers** (nice to have, bundle for marginal price), **killers** (not needed by most, sell as add-ons). Thresholds: 10-20% want it badly means add-on; more than 50% means leader.
3. **Map to the journey.** Day-one value in the starter plan; features whose value depends on accumulated data or advanced use in pro, sold as an upsell (Invoice2go doubled starter-to-pro upgrades while raising pro price about 30%).
4. **Check the plan mix.** If 60-70% pick the cheapest tier you gave away too much; reserve something for the middle tier. Move the middle tier to the inelastic threshold and add an expensive decoy (one SaaS went 79 to 99, 149 to 199, added 299, for 30%+ MRR with no product change).
5. **SKU audit by who buys.** Vercel found half its Enterprise SKU buyers were startups, so it unbundled those features for self-serve.
6. **Name limits as benefits**, not feature lists (Shopify inventory locations; SmugMug's benefit rewrite gave a double-digit revenue lift). Keep it simple: the test is whether a prospect can explain your pricing back as if selling it for you.
7. **Productize to segments:** different needs get different products, not different messaging (Eventbrite: one ticket type, unlimited, enterprise).

### Play 5 — Free tier, trial and the paywall
1. **Free what earns growth:** anything that gets users to the aha moment and habit, drives virality or network effects, or is commodity for every user (Naomi Ionita, Elena Verna). Never put a paywall on the edge that spreads the product (Shishir Mehrotra: charge makers, not sharers; Figma limits files, not collaborators); gate anything else that creates friction for the growth model.
2. **Survey converters.** If guilt is a top reason they upgrade, the free tier is too good and one premium tier leaves money on the table (Evernote at $45 a year). Create plans by persona.
3. **Work the three pillars in order** (Elena Verna): monetization awareness first (feature walls, usage walls, trials; about 75% of free users do not know what you sell), then checkout and pricing-page conversion, then model changes last. Make every paid trigger look the same and ensure each user sees at least three.
4. **Consider a reverse trial:** full premium for 7-30 days, then fall back to free (Lauryn Isford); strongest for B2B with lock-in (Albert Cheng). Test trial length; longer trials convert more because buying timing follows the buyer's calendar (Merci Grace).
5. **Benchmark:** free-to-paid under 5% will not sustain a company; aim above 7% (Yuriy Timen).
6. **Self-serve checkout:** make it as easy as top e-commerce, segment success by country and add local payment methods (Hila Qu). A pricing page that forces a quote request breaks self-serve.
7. **Done when:** you can write why each feature is free or paid in one sentence tied to the growth model.

### Play 6 — Raise prices on a live product
1. **Check headroom:** is NPS above 20 and support decent? Then raise at least once a year (Patrick Campbell). Most prices were guessed and never revisited (Jason Cohen).
2. **Raise substantially, watch signups per month.** If nothing changes, raise again (50% to 2x) before spending the extra margin. Price selects the market: serious buyers read $2 or $100 a month as immature.
3. **Earn it.** Ask whether you added commensurate value (Jason Lemkin: an 8% increase should come with roughly 30% more value) and tell a value-exchange story.
4. **Cadence:** one pricing change every quarter, however small, owned by a pricing committee with revenue per customer as the one KPI (Patrick Campbell); review the model yearly (twice as often in AI), price points every 6-12 months (Madhavan Ramanujam).
5. **Beware:** grandfathering and legacy migration is painful at scale if the value metric was never chosen (Melissa Tan). In marketplaces, price hikes that cause liquidity issues are a local maximum (Noam Lovinsky).

### Play 7 — Price an enterprise deal
1. Open at a 75K-150K initial contract with contained scope, and show years two and three so the buyer can defend it (Jen Abel). Price should follow sales cycle: about $100K at 90 days, $250-300K at nine months.
2. Hold the number until after the demo, discuss it one-on-one with the champion, give a ballpark if pushed, then co-author: *how would you defend this, where would you cut, how do I build the ROI slide?*
3. Never discount to close. If asked, make them defend it or trade for something real (design partnership, multi-year, reference).
4. Sanity check: a win rate above 25-35% from qualified opportunities means you are priced too low. Keep asking for more until you hit resistance and accept losing 20-30% of deals on price (Naomi Ionita, Envoy's 10x story, with incremental pushes to keep data).
5. Slow sales cycle plus low ACV is the quadrant of death (Todd Jackson).

## Where the experts disagree
**1. How to price AI.** *Outcome-based* (Madhavan Ramanujam, Eoghan McCabe, Bret Taylor) vs *hybrid or no playbook* (Naomi Ionita, Krithika Shankarraman, Brian Balfour warns outcome margins get competed away without a moat). → *Use outcome when work is autonomous and attributable (support resolutions); hybrid seats plus credits for copilots.* **Default:** start hybrid, build attribution, move to outcome only when you can prove the KPI.

**2. Charge early vs grow free.** *Monetize from day one* (Madhavan Ramanujam 2.0, Naomi Ionita, Ryan Hoover's 10% of focus) vs *treat AI cost as marketing and give it away* (Elena Verna, Lovable). → *Free wins in hypergrowth categories where share and engagement retention is the north star; charging early wins when you need a real PMF signal or inference cost is high.* **Default:** keep a visible paywall plan from day one even if you delay switching it on.

**3. Freemium vs no free.** *Freemium and sampling paid features* (Albert Cheng, Sean Ellis, Lauryn Isford's reverse trial) vs *no freemium or discount pre-chasm* (Geoffrey Moore, Jeanne DeWitt Grosser, who killed Stripe Billing's free tier). → *Freemium when word of mouth and user volume matter and marginal cost is low; skip it when integration effort already creates stickiness or buyers bear risk.* **Default:** reverse trial for B2B with lock-in.

**4. Land small vs land big.** *Land at 75-150K* (Jen Abel) vs *free individuals, expand wall-to-wall* (Naomi Ionita on Figma, Claire Butler). → *Sales-led and venture-scale: land big. Collaborative PLG with a multiplayer bridge: trade long-tail revenue for growth, but price enterprise inbound as enterprise from the start.*

**5. Annual commitments for SMB.** *Push annual* (common VC advice) vs *let customers choose, longest customer-centric trial* (Jason Lemkin). → *Annual helps enterprise procurement; for SMB show evidence before forcing it.*

## Deliverable
Produce this and offer to save it:
```markdown
# Pricing & Packaging Plan: <product>

## Situation
Buyer/motion: <self-serve | sales-led | marketplace | consumer> | Stage: <...> | AI? <y/n> | Goal: <revenue | share | enterprise land>

## Willingness to pay
Method: <Van Westendorp | acceptable/expensive/prohibitive | conjoint | range test> | n = <...>
Cliff/threshold found: <$...> | Chosen price point: <$...> | Value story: <one line>

## Model
Quadrant (attribution x autonomy, if AI): <...> | Value metric: <unit> | Model: <subscription | usage | hybrid | outcome>
Why not the other models: <1 line each>

## Packaging
| Tier | Price | Who it is for | Leaders included | Fillers | Upgrade trigger |
|---|---|---|---|---|---|
Add-ons (killers): <...> | Decoy tier: <...> | Free/trial: <what is free and why>

## Risks and test plan
Hypothesis -> test -> metric -> kill criterion (one row per pricing change)
Cadence: pricing committee <members>, quarterly change calendar, yearly model review

## Next 3 actions
1. <this week: run the 4-question survey with N users>
2. <this month: ship the one packaging/price change>
3. <this quarter: put the recurring pricing review on the calendar>
```

## Grade existing work
Score the user's pricing page, plan matrix or pricing doc 1-5 on each, then total (max 40) and return the top 3 fixes with the guest behind each.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Price grounded in WTP data | Guessed or copied from competitors (Jason Cohen) | Some interviews, no curve | Van Westendorp or conjoint, cliff identified (Rahul Vohra, Madhavan Ramanujam) |
| Value metric | Flat price or seats unrelated to value | Metric exists but customers cannot predict bill | Scales with value, trackable, auto-upgrades (Patrick Campbell) |
| Model fits product | Copied from fashion | Defensible but untested | Matches attribution/autonomy or value pattern (Madhavan Ramanujam) |
| Tier design | One plan, or 60-70% on the cheapest | Good/better/best with fuzzy edges | Leaders, fillers, killers sorted; decoy; benefit-named limits |
| Free tier / trial logic | Free tier is crippled or too generous | Aha moment free, triggers inconsistent | Growth-loop edge free; three consistent triggers; conversion above 5-7% |
| Simplicity | Needs a quote or laundry-list matrix | Understandable after reading | A prospect can explain it back as a seller |
| Price integrity | Discounts to close, win rate above 35% | Ad-hoc discount rules | Trades value, never discounts alone (Jen Abel, Madhavan Ramanujam) |
| Review cadence | Set and forget | Annual at best | Pricing committee, quarterly change, yearly model review (Patrick Campbell, Naomi Ionita) |

## Red flags
- **Low-price anchor:** a $20 product to grab share trains customers to expect cheap (Madhavan Ramanujam).
- **Free MVP of the easy 20%:** the 20% that drives 80% of willingness to pay given away free (Madhavan Ramanujam).
- **Price paralysis:** reluctance to raise is internal and emotional, not external (Madhavan Ramanujam).
- **Guilt-driven conversion** and one plan for all segments (Naomi Ionita).
- **Waiting too long to monetize,** then facing backlash (Naomi Ionita); not choosing a value metric early (Melissa Tan).
- **Pricing complexity creep:** seats, messages, leads, tiers; simplifying cost Intercom about $50M ARR but customers stayed longer (Eoghan McCabe, Paul Adams).
- **Discounting as a closer:** negotiating with yourself (Jen Abel); discount becomes the new price (Madhavan Ramanujam).
- **Charging at the share moment** kills the viral loop (Shishir Mehrotra).
- **Price per token** is measuring engineers by lines of code (Bret Taylor).
- **Penetration pricing without the cost structure** for it (Madhavan Ramanujam).
- **Enterprise priced at small-business rates:** documented price history makes the later step-up near impossible (Jen Abel).

## Receipts
- "So there are two axes here. One is attribution, and the other one is autonomy. And when you have high attribution and high autonomy, that is when you have high pricing power" — Madhavan Ramanujam, Lenny's Podcast (00:39:39)
- "We usually say how you charge is way more important than how much you charge." — Madhavan Ramanujam, Lenny's Podcast (01:00:04)
- "if guilt is one of the main reasons why people are paying you, then your free version is too good, and you are leaving money on the table." — Naomi Ionita, Lenny's Podcast (15:53)
- "find one thing you're going to do every three months, put a calendar invite, let it renew every three months." — Patrick Campbell, Lenny's Podcast (00:19:42)
- "So what often happens is you raise prices and signups don't change." — Jason Cohen, Lenny's Podcast (00:37:16)
- "If your win rate is higher than that, your price is too low." — Jen Abel, Lenny's Podcast (01:08:41)

## Go deeper
- `references/frameworks.md` — every framework in this skill, how to run it
- `references/quotes.md` — verified quotes with timestamps
- Related skills:
  - `position` — hand off when the price question is really a category/positioning question (Rahul Vohra: positioning before pricing).
  - `pmf-check` — hand off when low conversion may mean no product-market fit rather than bad pricing.
  - `growth-model` — hand off for free-tier loops, activation and retention work behind the paywall.
  - `b2b-sales` — hand off for ICP, pitch and pipeline once the enterprise price band is set.
  - `experiment` — hand off to design and read out a pricing A/B or holdout.
