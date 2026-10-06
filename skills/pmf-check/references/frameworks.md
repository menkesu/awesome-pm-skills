# Frameworks: pmf-check

Every distinct method in the digest, grouped by theme. Originators are credited; other endorsers are noted. Numbers are the guests' own and are representative, not strict.

---

## A. The survey: measuring must-have

### 1. Sean Ellis PMF test (Sean Ellis)
**For:** a day-one, no-analytics read on whether a product is a must-have. Endorsed by Rahul Vohra, Jag Duggal (Nubank), Sarah Tavel.
**Question:** *How would you feel if you could no longer use this product?* Answers: very disappointed / somewhat disappointed / not disappointed / N/A, I no longer use it.
**Steps:**
1. Sample random users who have really used the product.
2. Ask the question with the four answer choices.
3. Treat about 40% 'very disappointed' as the bar to start aggressively growing.
4. Dig into the 'very disappointed' segment: who are they, and why.
**Applies:** any stage once there is an MVP; recurring-use products, B2B and B2C. **Fails:** one-off products (a movie, a workshop) where 'no longer use' makes no sense.
**Why not NPS:** Sarah Tavel prefers this question to NPS; Rahul Vohra found it more predictive. Ellis originally flipped from satisfaction to this wording at Xobni because demanding senior-management users were never 'satisfied'.

### 2. Sampling rules (Sean Ellis)
Random sample of people who have used the product 2+ times, ideally in the last 1-2 weeks (before they churn). Not signups, not demo viewers. If you are testing a new onboarding, survey only people who went through it. Minimum 30 responses before you rely on the number; 4 of 10 is directional, not a go-to-market sample.

### 3. The threshold is a shared target, not magic (Sean Ellis)
The value of 40% is that the team agrees on a number: we do not grow aggressively until we hit it. That ends the 'years away' versus 'what are we waiting for' argument. Agree the number before you see the result. If you change the survey method, the new method sets a new baseline (Vohra).

### 4. Calibrate to culture (Sean Ellis, Jag Duggal)
Response bias varies. Nubank requires 50% in Brazil because Brazilians are polite and optimistic; Ellis suggests ~30% may be enough in a more pessimistic market such as Hungary. Pick a target for your market and hold it constant across surveys.

### 5. Switching-cost inflation (Sean Ellis)
Scores run high when users have invested time or face switching costs: webs.com scored about 90% and Eventbrite was near the top. Read the score together with the reasons given. The score is a function of both switching costs and utility.

### 6. Segment by use case (Sean Ellis)
Force users into use-case buckets (multiple choice) and cross-tab. Example: one use case scores 60% but is small, another scores 35% and is far larger. That turns PMF into an explicit strategic choice: intense niche versus broad almost-there group.

### 7. Find the bullseye cohort (Jag Duggal, Nubank)
Cross-tab the score by behavior. Payments Assistant scored 40% overall but 70% for users with 4+ commitments on 2+ payment rails. Then make dozens of product iterations that push more users into that behavior. MAU went from hundreds of thousands to 10M+ in about 15 months.

### 8. Superhuman Product-Market Fit Engine (Rahul Vohra)
**For:** products stuck at 10-30%. Ellis endorses it as a refinement.
**Steps:**
1. Run the survey; track % very disappointed (benchmark 40%).
2. Ask the very disappointed why they love it; extract the main benefit.
3. Among somewhat-disappointed users, keep those for whom that main benefit resonates; politely disregard the rest.
4. Ask that kept group what holds them back.
5. Each planning cycle: half the roadmap doubles down on what people love, half removes the objections.
**Key trap:** do not over-act on the very disappointed users' feedback; they already love it.

### 9. Ignore the somewhat disappointed (Sean Ellis)
Their feedback dilutes the product until it is good for everyone and great for no one. Ellis's rule is the simple version; Vohra's filter (step 3 above) is the refined version. See debate in SKILL.md.

### 10. What would you use instead? (Sean Ellis)
Add the question to the survey. Somewhat-disappointed users usually name an easy commodity alternative. A must-have has to be both valuable and unique. Feeds positioning work.

### 11. Feature-level PMF test (Sean Ellis, Nubank)
Ask how users would feel if they could no longer use a given feature or new product; gate launch at a threshold (Nubank: 50%). If a feature is not a must-have, maybe it should not exist. Needs enough users to sample without over-surveying.

### 12. Gate scaling on the score (Jag Duggal)
Nubank rarely scales a launched product until its Sean Ellis score clears a threshold, enforced culturally by making 'what is the score?' a standard post-launch review question. Ultravioleta premium card: loved only by customers who spend enough to waive the fee; scaling was held two to two and a half years while iterating on that segment.

### 13. Leading survey, lagging retention (Sean Ellis)
The survey works on day one; retention cohorts are the more accurate but lagging confirmation, and give no qualitative why. Keep surveying during growth. If you are churning out the users who said very disappointed, stop scaling and reassess.

### 14. Marketplaces have two PMFs (Benjamin Lauzier)
Run the very-disappointed survey on demand and on supply separately. Check that the value proposition (for example margins) is compelling for suppliers, not just buyers.

---

## B. Levels, efficiency and benchmarks (sales-led B2B)

### 15. Four levels of product-market fit (Todd Jackson, First Round)
PMF arrives in sequenced levels over roughly four to six years. You optimize satisfaction first, then demand, then efficiency.
| Level | Customers | Team | ARR | Optimize |
|---|---|---|---|---|
| 1 nascent | 3-5 satisfied | <10 | $0-500K | satisfaction |
| 2 developing | 5-25 | up to ~20 | $500K-5M | + demand |
| 3 strong | 25-100+ | 30-100 | $5-25M | + efficiency |
| 4 extreme | 100+ | 100+ | $25M+ | all three, expand TAM |
**Fails for:** consumer and bottom-up products (the authors say these involve more alchemy). PMF is a level, not a binary: 25 happy customers and $5M ARR can still be level 2.

### 16. Extreme PMF: demand, satisfaction, efficiency (Todd Jackson)
Widespread demand for a product that satisfies a critical need and can be delivered repeatably and efficiently. Most people omit the efficiency leg. The three trade off: marketing spend lifts demand but cuts efficiency; automation lifts efficiency but can hurt satisfaction.

### 17. Level 1 benchmarks and stuck signs (Todd Jackson)
About 20 warm intros to land one customer; at least 50 conversations to reach 3-5 customers; demand comes from your network. After 6-12 months, yellow flags: customers would not be disappointed if you vanished; each customer wants a different key feature (consulting, not product); the next customer is hard to find; usage is low or stalls.

### 18. Level 2 playbook and benchmarks (Todd Jackson)
Going from 5 to 25 customers cannot be done by grit; build a repeatable demand source (tuned cold outreach, content, community events) so the product does heavy lifting. Benchmarks: first call to close without a warm intro ~10%; magic number 0.5-0.75; regretted churn 10-20%; NRR 100%+; gross margin not worse than 50%; burn multiple not worse than 5x.
**Stuck at level 2:** 12-18 months without opening demand; regretted churn over 20%; long cycles with low ACV (the quadrant of death); late-funnel losses; struggling to hit price; polite 'no budget / try next year' answers, which mean no. Long cycles are normal for six-figure and government deals.

### 19. Level 3 benchmarks and stuck signs (Todd Jackson)
$5-25M ARR, ~75K ACV, approaching 100 customers, 10%+ of leads from referrals or organic, gross margin above 60% (hopefully 70%), burn multiple 1-3, regretted churn under 10%, NRR above 110%. Stuck: NRR under 90%, regretted churn over 10%, growth slowing (3x two years running, struggling to hit 2x), first channel saturating, growth spend pushing burn multiple back above 3.

### 20. Efficiency metric definitions (Todd Jackson)
Magic number = new ARR in a period / CAC spent in that period. Burn multiple = net burn / new ARR (burn $5M to add $1M ARR is 5x).

### 21. Marginal customer test (Todd Jackson)
If PMF is strengthening, the next customer is easier to acquire and easier to serve well. Flat or worsening difficulty means fit is not strengthening.

### 22. The $100 vending machine (Todd Jackson)
Demand and satisfaction without efficiency is not PMF: WeWork and Casper gave away $2 for $1. Check unit economics before declaring victory.

### 23. Odds of getting past level 2 (Todd Jackson)
Roughly 60-70% of startups get stuck at level 1 or 2. Qasar Younis adds that good companies tend to show traction early and sustain it for a decade or more.

---

## C. Retention and behavioral data

### 24. Retention benchmarks (Crystal Widjaja)
Week-one cohort retention should flatten at about 60% for a free product, 20-30% for a paid product, and near 80% for friends and family. Choose a frequency period that matches natural usage and judge within 2-3 periods. If friends and family are not near 80%, it likely will not work for strangers.

### 25. Retention J-curve gates (Robby Stein; Uri Levine)
Plot the percentage still using the product on day 7, 30 and 90; does it flatten, or do people drip out? Then check whether usage is good enough to spread by word of mouth, and whether the product can get big enough. A curve that goes to zero means the product is toast. Uri Levine goes further: PMF has one metric, retention.

### 26. Good-cohort conviction (Dan Hockenmaier)
Even with few customers, strong retaining cohorts (especially a smiling curve, where engagement rises later in life) justify investing more than lots of low-quality volume.

### 27. Week-four multi-user activation (Lauryn Isford, Airtable)
Let analytics find the behavior most correlated with long-term retention, and set a relatively high bar. Airtable: more than one person on a team active in a workflow in week four. For seat-based collaboration products.

### 28. Minimum viable happiness (Sarah Tavel)
Do unscalable work until a threshold percentage of people retain after a transaction; only then work scaling levers. For early marketplaces.

### 29. Launch-spike traps (Crystal Widjaja, Kayvon Beykpour, Grant Lee)
A spike can pull forward every user who could subscribe (Netflix, Spotify in markets without credit cards). Periscope's surges in new markets masked poor retention. Do not buy top-of-funnel to compensate for weak organic pull; that brute-forces a fleeting destination.

### 30. Waze iteration loop (Uri Levine)
Interview users who churned, ask what did not work, build the next version, repeat even when sure it will work, and roll out market by market once good enough. Waze took about four years; Microsoft five, Netflix ten.

---

## D. Pull and qualitative signal

### 31. Signals of real pull (Raaz Herzberg, Jen Abel)
Buyers push to the next step: asking about price, asking when a proof of value can start, naming who to connect you to, inviting colleagues or their boss. Discount generic praise. Jen Abel's discovery gate: is the problem growing and currently measured or managed? If nobody measures it, it is probably not a priority. A low outreach response rate is usually a signal the problem is not widely felt (2% versus 12% from the same outreach, differing only in insight).

### 32. Pull as the simplest early signal (Nikhyl Singhal; Brendan Foody; Naomi Gleit)
How hard is it to acquire a user? Little marketing and an easy sale means pull. Look for the customer that is surprisingly easy to sell into (Foody). Naomi Gleit's Facebook signals: obsessive usage plus a waitlist of adjacent audiences. Caveat: pull alone does not prove a business model.

### 33. Word-of-mouth machine and two checkpoints (Grant Lee, Gamma)
Checkpoint 1: organic growth (Gamma: over 50% of leads via word of mouth or direct). Checkpoint 2: willingness to pay. Do not mistake a Product Hunt spike for PMF. Julia Schottenstein: users who cannot stop talking about it and share it with teammates are the spark.

### 34. Reference-customer threshold (Christian Idiodi)
B2B: 6-8 customers willing to be references. B2C: 15-25 (he will not launch an app until 25 five-star reviews are waiting). Work with 25+ people in one target market until enough will vouch.

### 35. Early PMF milestones ladder (Claire Butler)
One company uses it (learn what they want) -> keep them using it -> second company -> someone pays. At the earliest stage you cannot optimize your way to PMF; small numbers make metrics meaningless.

### 36. Lighthouse Users Program (Tanguy Crusson)
For bets inside a larger company: work with 10, then 100, then 1,000 hand-picked customers with a playbook per stage. Spend stage one explaining why they are a proxy for later customers. Report with customer video snippets, not aggregates.

### 37. Emotive language and first ICP (Cameron Adams)
Run continuous user tests; the standout segment shows incredibly emotive language (sheer joy), not just positive ratings. Canva found social media managers this way in its last six months of testing. MVP must spark joy: users ask how to sign up or pay and want to tell others.

### 38. Complaints, silence and outages (Claire Vo; Gaurav Misra; Jeff Weinstein)
Complaints that it is broken or not good enough (rather than not useful) indicate fit the product has not caught up to. If nobody complains after a minimal release, that is a red flag. Jeff Weinstein's startup had a 20-minute outage and customers only murmured; the lack of outrage was the signal there was no PMF.

### 39. Reach test and internal banger (Dan Shipper)
Do you reach for the product organically when you wake up? Does the team adopt it spontaneously without being told? Works when the team resembles the early-adopter audience.

### 40. Click (Jake Knapp)
In head-to-head prototype interviews against real alternatives, a product that clicks with customer after customer is a strong pre-launch signal. Interviews are a simulation, only a helpful signal.

### 41. Delta 4 (Kunal Shah)
Have users score the incumbent way of doing the job out of 10, then score yours. A gap under 4 means adoption is reversible. A Delta 4 product is irreversible, users tolerate occasional failure, and they brag unprompted (low or zero CAC). Replaces the unmeasurable 10x-better heuristic; scores are subjective.

---

## E. Willingness to pay

### 42. Product-market-pricing fit (Madhavan Ramanujam; Naomi Ionita)
Validating PMF without a price attached tells you what you want to hear. 72% of innovations fail commercially because the monetization check came too late. Treat free-beta feedback as R&D cost; people opening wallets is the true signal (Ionita).
**Purchase probability scale:** on a 1-5 intent scale a 5 means only 30-50% real probability, a 4 means 10-20%, 3 or below means they will not buy. Vary price and see if ratings move.

---

## F. Diagnosing why you are not there

### 43. Why they are not desperate (Mike Maples Jr.)
Either the insight is wrong, the implementation is wrong, or you are talking to the wrong (not future-living) customer. Okta kept its insight but changed implementation from cloud management to identity management. Core question: what can we uniquely offer that people are desperate for?

### 44. Five-question stalled-growth diagnostic (Jason Cohen)
Strict order, because an unfixed earlier problem makes later fixes pointless: (1) is logo churn too high, (2) is pricing and positioning right, (3) are existing customers growing (NRR over 100%), (4) are channels saturated, (5) do you actually need to grow? B2B SaaS focus.

### 45. Funnel diagnostic before hiring demand gen (Krithika Shankarraman)
How many leads enter, and how likely are they to close once in a sales conversation? High conversion: scale top of funnel. If prospects ask about competitors and price: hire a product marketer for differentiation, positioning and enablement. April Dunford: the leading indicator of a better pitch is more deals converting from first substantive call to opportunity.

### 46. Reset when the market is not narrowing your path (Qasar Younis)
At about year two, if market feedback is not pointing to a more specific path, question the foundation (co-founders, market, phase of life, effort) and consider a hard reset. Mike Krieger's version: ten units of input for one unit of output means consider shutting down.

### 47. Receptors and drugs (Matt MacInnis)
Demand is already decided like receptors binding a drug; marketing cannot create it. Treat a launch as an experiment, and if it fails, change the product rather than marketing harder. Also: if you do not absolutely know you have PMF, you do not.

### 48. Early adopters differ from the broad market (Adam Grenier)
Define which evidence from early adopters predicts PMF in the broader market. If your TAM definition and your PMF definition describe different customers, that is a red flag.

### 49. Vocal 20% versus the 80% (Maya Prohovnik; Tamar Yehoshua)
If the target is everyone, vocal feature-requesters can pull you deeper into a niche. Balance metrics with intuition and do not over-index on the vocal unhappy minority. Fails for niche products with a specific vocal audience.

---

## G. Durability: PMF after PMF

### 50. PMF decays (Casey Winters)
Expectations and competition rise continuously; teams that do not keep improving UX, value and latency can drift out of PMF over a year or five.

### 51. PMF treadmill in AI (Elena Verna)
Capability and expectations change roughly every three months; alternate short scaling blitzes with reinvention, and build ahead of model releases. Expected to slow when models stabilize. Her adjacent-user worry: constantly recapturing pioneers while the latent majority is left behind.

### 52. Re-earn PMF after a market shift (Adam Grenier)
After a macro shift, assume you no longer have PMF and re-validate, rather than assuming a new channel will fix it.

### 53. Stacking S-curves (Noah Weiss) and PMF by segment (Karri Saarinen)
PMF is a series of S-curves: one audience, a ceiling, then the next audience (non-developers, enterprises, other countries). Saarinen: measure fit per segment as a spectrum; become the default for the strongest segment, then push into larger ones. Double down where you see pull (Zoom with universities) until you have captured it.

### 54. Product-market-story fit (Paul Adams)
Market = people with the same problem who care a lot; product = the solution; story = a simple, clear narrative. A great product in a great market can still fail on a convoluted story (Rdio versus Spotify).

### 55. Lochhead's contrarian frame (Christopher Lochhead)
PMF fits the product into an existing market; design a market category for your product instead (Threads hit PMF fastest ever and still cratered). Fits winner-take-most ambitions; incremental businesses can rely on existing demand.

### 56. PMF is not growth readiness (Sean Ellis; Naomi Gleit)
Companies can fail despite a passing score, then it is an execution challenge; scores can hide risk when the core reason (BlackBerry's keyboard) is disrupted. Gleit: growth teams may get credit that strong PMF earned, so check whether demand already outruns supply before crediting growth work.
