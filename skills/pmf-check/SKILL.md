---
name: pmf-check
description: Diagnoses product-market fit from survey, usage and pipeline data and returns a scored verdict with the next moves. Use when you ask 'do we have product-market fit', 'is our PMF survey good enough', 'what does 35% very disappointed mean', 'should we scale yet', 'why is growth stalling', or need a Sean Ellis survey, retention check, or PMF level read. Draws on 137 insights from 66 Lenny's Podcast guests incl. Sean Ellis, Todd Jackson and Rahul Vohra.
---

# PMF Check

![pmf-check: lead guest team](assets/card.png)

Turn a survey CSV, retention data, or a pile of customer signals into a PMF verdict, a diagnosis of what is missing, and a half-and-half roadmap. Built from 137 insights from 66 Lenny's Podcast guests. **Lead team:** Sean Ellis, Todd Jackson, Rahul Vohra.

## When to use
- You have (or can run) a 'how would you feel if you could no longer use this' survey and need to interpret it.
- Someone asks 'should we start spending on growth?' or 'are we ready to hire a growth lead / demand gen?'
- A sales-led B2B startup wants to know which PMF level it is at and what to fix before the next one.
- Growth stalled after a launch spike, a market shift, or a model release.
- You have a score of 15-39% and need a plan to move it, not a pep talk.
- The team is split between 'years away' and 'what are we waiting for'.
- A feature or new product inside a larger company needs a go/no-go signal.

## Step 1 - Diagnose (ask before answering)
If the user attached a survey export, cohort table, CRM export, deck or repo, read it first and only ask what is still missing. Max 4 questions:
1. **Who pays and how do they buy?** Sales-led B2B, self-serve/PLG, consumer, two-sided marketplace, or an AI product. *Routes between Todd Jackson's levels (sales-led B2B), the Ellis/Vohra survey (recurring-use products), retention gates (consumer), and the two-PMF split (marketplaces).*
2. **How many people have used it 2+ times in the last 1-2 weeks, and how many customers/ARR?** *Under 30 usable respondents means qualitative signals instead of a score (Sean Ellis's 30-response floor, Claire Butler).*
3. **What data exists today?** Survey responses, retention cohorts, win/loss and sales cycle, churn reasons, organic share of signups. *Decides which evidence streams you can triangulate.*
4. **What decision hangs on this?** Scale spend, hire growth, raise, pivot, kill a feature. *Sets the bar: a launch gate needs the threshold (Jag Duggal); a stall needs the Cohen order.*

## Step 2 - Pick the play
| If... (situation) | Use | From | Why |
|---|---|---|---|
| 30+ real users, product used repeatedly (B2B or B2C) | Sean Ellis PMF test + sampling rules + segment cross-tab | Sean Ellis, Rahul Vohra | Day-one leading indicator; 40% is the shared target |
| Score is 10-39% and a core benefit is visible | Superhuman PMF Engine (half love, half objections) | Rahul Vohra | Moves on-the-fence users who share the core benefit |
| Sales-led B2B, under ~100 customers or $25M ARR | Four levels of PMF with benchmarks and stuck signs | Todd Jackson | Staged, includes efficiency; tells you what to optimize now |
| Under 30 users or pre-revenue | Pull signals + reference-customer count + milestones ladder | Raaz Herzberg, Christian Idiodi, Claire Butler, Jen Abel | Numbers are meaningless at this size |
| Consumer, free, or a launch spike that flattened | Retention flatten bar + J-curve gates + word-of-mouth share | Crystal Widjaja, Robby Stein, Uri Levine, Grant Lee | Spikes lie; retention and organic share do not |
| Marketplace | Two separate PMF surveys + minimum viable happiness | Benjamin Lauzier, Sarah Tavel | Each side has its own fit |
| Passing score but growth is stalling, or the market or model changed | Cohen five-question order; PMF decay and treadmill checks | Jason Cohen, Casey Winters, Elena Verna, Adam Grenier | Fit is not permanent; fix churn before channels |
| Better than the alternative but not winning | Delta 4 test + willingness-to-pay check | Kunal Shah, Madhavan Ramanujam | Reversible adoption and no-pay answers explain flat pull |

## Step 3 - Run it

### Play A: Run and read the Sean Ellis survey (Sean Ellis)
1. **Sample.** Random users who used the product 2+ times, ideally in the last 1-2 weeks. Exclude signups who never activated and demo viewers. Testing a new onboarding? Survey only people who went through it.
2. **Ask** (wording of the extra questions is ours; the first is Ellis's):
   - *How would you feel if you could no longer use [product]?* Very disappointed / Somewhat disappointed / Not disappointed / N/A, I no longer use it.
   - *What is the main benefit you get from [product]?*
   - *What would you use instead if it were no longer available?* (Ellis: must-haves are valuable and unique.)
   - *What is the one thing holding you back from loving it?* (Vohra's objection question.)
   - A use-case multiple choice, so you can bucket and cross-tab.
3. **Size check.** Under 30 responses: report as directional only. 4 of 10 is a signal, not a go-to-market sample.
4. **Compute** % very disappointed (state your denominator and keep it fixed; changing method resets the baseline, per Vohra). Then cross-tab by use case, persona, plan, signup channel, and key behavior. Report each segment's score next to its size.
5. **Read it:**
   - Under 40%: do not scale; run Play B. Over 40%: start aggressive growth work, keep surveying and watching cohorts.
   - Calibrate the bar to the culture you survey (Nubank: 50% in Brazil; Ellis: ~30% may do in a more pessimistic market). Agree the number *before* seeing results.
   - A very high score in a product with heavy user investment (site builders, event setup) is inflated by switching costs. Read the reasons.
   - Find the bullseye cohort (Jag Duggal: 40% overall, 70% for users with 4+ commitments on 2+ rails) and ask what behavior defines it.
6. **Done when** you can state: the score, n, the highest-scoring segment and its size, the main benefit in the users' words, and the top objection.

### Play B: Superhuman PMF Engine (Rahul Vohra)
1. From the very disappointed, extract the **main benefit** (their words, 3-5 recurring phrases).
2. Take the somewhat disappointed. **Keep** those whose answers center on that same benefit; politely disregard the rest.
3. From the kept group, list what holds them back. Cluster into 3-6 objections.
4. Build the roadmap: **half the cycle doubles down on what the very disappointed love, half removes the kept group's objections.** Do not over-act on the very disappointed's feature requests; they already love it.
5. Re-run with the same method on the next cohort. Expect the score to climb quarter over quarter. Ellis's other lever: PMF is usually an onboarding problem; set the right expectations in acquisition messaging, then get new users to the value moment fast (Lookout: 7% to 40% in two weeks by repositioning on antivirus and putting it first in onboarding).

### Play C: Place yourself on Todd Jackson's levels (sales-led B2B)
1. Count: satisfied customers, team size, ARR, months at this level. Place on the ladder:
   - **L1** 3-5 customers, <10 people, $0-500K ARR. Optimize satisfaction. Demand comes from your network (~20 warm intros per customer; 50+ conversations to reach 3-5).
   - **L2** 5-25 customers, ~20 people, $500K-5M. Add demand: you need a repeatable source beyond grit (cold outreach, content, events).
   - **L3** 25-100+ customers, 30-100 people, $5-25M. Add efficiency.
   - **L4** 100+ customers, $25M+. Hold all three, expand TAM.
2. Score the three legs: **satisfaction** (survey, regretted churn), **demand** (inbound share, first-call-to-close ~10% cold at L2), **efficiency** (magic number 0.5-0.75 at L2; burn multiple not worse than 5x at L2, 1-3 at L3; gross margin 50%+ at L2, 60%+ at L3).
3. Run the **marginal customer test**: is the next customer getting easier to acquire and easier to serve well?
4. Check the stuck signs for your level:
   - L1 after 6-12 months: customers would not be disappointed if you vanished; each wants a different key feature (consulting, not product); next customer is hard to find; usage stalls.
   - L2 for 12-18 months: regretted churn over 20%, long cycles plus low ACV, late-funnel losses, 'no budget / next year' answers (those mean no).
   - L3: NRR under 90%, regretted churn over 10%, first channel saturating, growth spend pushing burn multiple above 3.
5. Name the one leg to fix next. Do not optimize all three at once; they trade off (marketing lifts demand and cuts efficiency).

### Play D: Under 30 users, so no score yet (Herzberg, Abel, Idiodi, Butler)
Count these, in order of strength:
1. **Pull behaviors:** buyers ask about price, ask when a proof of value can start, name who on their team to bring in, invite a boss to the next call. Polite praise counts as zero.
2. **Interest rate:** a low reply rate to identical outreach usually means the problem is not widely felt (Jen Abel saw 2% versus 12% from insight alone).
3. **Reference-ready customers:** 6-8 for B2B, 15-25 for B2C (Christian Idiodi).
4. **Milestone ladder:** one company using it, still using it, a second company, someone paying (Claire Butler).
5. **Ease of sale:** is there a segment that is surprisingly easy to sell into? Double down there; drop segments where the marginal customer is very hard (Brendan Foody, Karri Saarinen).
6. **Emotive language:** sheer joy, not just 4 out of 5 ratings (Cameron Adams).
7. **Willingness to pay:** ask for money. A free-beta answer is R&D, not fit (Naomi Ionita, Madhavan Ramanujam).

### Play E: Consumer or free product, spike then flat (Widjaja, Stein, Levine, Lee)
1. Plot week-one cohort retention at the product's natural frequency. Free product should flatten near 60% within 2-3 periods; paid 20-30%; friends and family near 80%.
2. Check the J-curve at day 7, 30, 90: does it flatten, or drip to zero?
3. Check organic share: Gamma got over 50% of leads from word of mouth. If low, ask why people are not telling colleagues.
4. Check you did not pull forward everyone who could convert (Netflix, Spotify, credit-card-poor markets) and that new-market surges are not masking poor retention (Periscope).
5. Do not buy more top-of-funnel to compensate (Grant Lee, Luc Levesque).

### Play F: Passing score but stuck (Jason Cohen's order)
1. Logo churn too high? Fix first. 2. Pricing and positioning right? 3. Existing customers growing (NRR over 100%)? 4. Channels saturated? 5. Do you need to grow at all? An unfixed earlier question makes later fixes pointless.
Also: did the market, a competitor, or a model release change what 'must-have' means? If so, assume you must re-earn fit (Adam Grenier, Casey Winters, Elena Verna).

## Where the experts disagree
**1. Binary or a level?** *Binary:* Nikita Bier, Matt MacInnis, Eric Ries (you will know; if you are asking, you do not have it). *Staged/spectrum:* Todd Jackson (levels with benchmarks), Karri Saarinen (per segment), Noah Weiss (stacking S-curves). -> *Use the binary read for consumer products with viral dynamics (people fight to get in, systems break); use levels for B2B where signals are ambiguous.* Default: levels for any B2B, binary sanity-check for consumer.

**2. What to do with the somewhat disappointed.** *Ignore them:* Sean Ellis (nice-to-have, as good as gone). *Selectively convert them:* Rahul Vohra (keep those who share the main benefit and remove their objections). -> *Ignore when your must-have segment is already identifiable and small; filter-and-convert when you are stuck at 10-30% and the core benefit is clear.* Default: Vohra's filter, with Ellis's discipline of not tuning for people who do not share the benefit.

**3. Pull or economics?** *Pull first:* Nikhyl Singhal (how hard is it to acquire users, ignore payback math early). *Economics are part of the definition:* Todd Jackson (the $100 vending machine, efficiency as a leg). -> *Early (L1, pre-revenue), read pull; once you have 25+ customers or are subsidizing growth, efficiency becomes mandatory.* Default: pull until ~$500K ARR, then add magic number and burn multiple.

**4. Growth before fit?** *Not before:* Luc Levesque (damages users who will not retry), Timothy Davis (ads into a product that cannot convert), Grant Lee. *Build loops early:* Casey Winters (scalable acquisition loops are a requirement for PMF). -> *Do not spend on paid or hire growth until retention flattens and the score clears your bar; do design the loop and the onboarding path in parallel.* Default: no paid acquisition pre-fit, yes to loop design.

## Deliverable
Produce this, filled in:

```markdown
# PMF Diagnosis: <product> - <date>

## Verdict
<No fit yet | Fit in one pocket | Fit, not scalable yet | Fit and ready to scale>
Confidence: <low/med/high>, because <n, sampling quality, agreeing evidence streams>

## Scorecard
| Evidence | Reading | Bar | Pass? | Source of bar |
|---|---|---|---|---|
| % very disappointed (n=__) | __% | 40% (calibrated: __) | | Ellis / Vohra |
| Best segment score and size | __% of __% of users | | | Ellis |
| Retention flattens at | __% by period __ | free 60 / paid 20-30 | | Widjaja |
| Organic / referral share | __% | rising; Gamma over 50% | | Lee |
| Level (sales-led B2B) | L__ | | | Jackson |
| Marginal customer easier? | yes/no | | | Jackson |
| Efficiency (magic no., burn mult.) | __ / __ | per level | | Jackson |
| Will they pay? | __ | | | Ramanujam / Ionita |

## Who loves it, and why
Main benefit (their words): __ | Who they are: __ | What they would use instead: __

## What is holding the others back
Top 3 objections from the kept somewhat-disappointed: 1. __ 2. __ 3. __

## Roadmap split (Vohra)
Double down (50%): __ | Remove objections (50%): __

## Stuck signs triggered
<list from Plays C-F, or none>

## Next 3 actions
1. <action, owner, date, metric that moves>
2.
3.
```

## Grade existing work
Give the user's PMF survey, analysis, or board slide a 1-5 per criterion, a total out of 40, and the top 3 fixes with the guest behind each.
| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Sample quality (Ellis) | Everyone who signed up | Active users, not filtered by recency | Random, 2+ uses, last 1-2 weeks, onboarding cohort isolated |
| Sample size (Ellis) | Under 15 | 15-29, caveated | 30+ and per-segment sizes shown |
| Question integrity (Vohra) | Reworded, mixed with NPS | Right question, inconsistent over time | Exact question, fixed denominator, comparable baseline |
| Threshold set in advance (Ellis, Duggal) | None | 40% quoted from memory | Team-agreed, calibrated to culture, tied to a scale decision |
| Segmentation (Ellis, Duggal) | One blended number | By persona only | By use case and behavior, bullseye cohort found |
| Action loop (Vohra) | Report only | Some objections listed | Main benefit extracted, half/half roadmap |
| Triangulation (Ellis, Widjaja, Lee) | Survey alone | Survey plus one metric | Survey, retention flatten, organic share, and willingness to pay |
| Stage fit (Jackson) | Ignores efficiency and level | Level named, no benchmarks | Level, stuck signs and the single leg to optimize |
Output: score per criterion, total, then fixes ranked by gap size times decision impact.

## Red flags
- **Survey of signups, not users.** Ellis: sample people who really used it, 2+ times.
- **Declaring victory on 4 of 10.** Under 30 responses is directional (Ellis).
- **Tuning for the somewhat disappointed.** Dilutes the product for must-have users (Ellis); only the ones who share the core benefit are worth converting (Vohra).
- **Launch spike mistaken for fit.** Netflix and Spotify pulled forward all who could subscribe (Widjaja); Periscope's surges hid weak retention (Kayvon Beykpour).
- **Investor, YC or press validation counted as PMF** (Gustaf Alstromer). Assume you lack it until customers prove it.
- **Happy customers, bad economics.** WeWork and Casper gave $2 for $1 (Todd Jackson).
- **Polite 'no budget / try next year'.** That is a no (Jackson); likewise 'super cool, keep me posted' (Raaz Herzberg).
- **Buying top of funnel to cover weak organic pull** (Grant Lee, Luc Levesque, Timothy Davis).
- **TAM and PMF defined differently** (Adam Grenier): early adopters may be nothing like the broad market.
- **Treating PMF as permanent.** Expectations and competition rise (Casey Winters); in AI, recapture every ~3 months (Elena Verna).
- **Each customer wants a different key feature.** That is a consulting business (Todd Jackson).

## Receipts
"you want more people to be very disappointed without your product. The trick here is not to act too much on the feedback that the very disappointed people are giving you, because they already love your product."
— Rahul Vohra, Lenny's Podcast (00:56:03)

"just ignore the people who say they'd be somewhat disappointed. They're telling you it's a nice to have. They're as good as gone, so just ignore those guys."
— Sean Ellis, Lenny's Podcast (00:40:43)

"They're basically with their products, giving away $2 for $1 and it gets them pretty far. But that's not real product-market fit."
— Todd Jackson, Lenny's Podcast (00:18:59)

"you can kind of tell by how hard it is to acquire your users. When companies are putting very little in marketing and there're people coming into the door or there's such an easy sale, you've got it."
— Nikhyl Singhal, Lenny's Podcast (00:20:36)

"product market fit in general have only one metric, only one metric, retention. Look, it's really simple, if you create value, they will come back, that's it."
— Uri Levine, Lenny's Podcast (00:11:43)

"product market fit is a sort of thing where you absolutely know it when you see it, and therefore if you don't absolutely know it, you don't have it."
— Matt MacInnis, Lenny's Podcast (00:42:59)

## Go deeper
- `references/frameworks.md` - every framework in this skill, how to run it
- `references/quotes.md` - verified quotes with timestamps
- Related skills:
  - `validate-idea` - before there are users to survey: riskiest assumptions and cheapest tests
  - `growth-model` - once the score clears the bar: loops, activation and retention work
  - `price` - when the diagnosis says willingness to pay is the missing leg
  - `position` - when somewhat-disappointed users name easy alternatives or prospects ask about competitors
  - `metrics` - to turn the scorecard into a standing north star and review cadence
