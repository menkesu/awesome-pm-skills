# Craft Review: Frameworks

Every framework below is credited to the guest who described it on Lenny's Podcast. Where several guests endorse the same method, they are listed.

## A. Reviewing a journey

### 1. Walk the store / critical user journeys (Katie Dill, Stripe)
**For:** orgs where many teams own pieces of one journey. **Steps:** pick about 15 critical user journeys; assign an engineering, product and design leader trio to each; on a regular cadence walk the journey end to end as a user (search, website, docs, dashboard); friction log with screenshots and tags; file bugs with owning teams; score on a rubric; calibrate scores together. **Fails when:** treated as a replacement for user research or data.

### 2. Product Quality Review (Katie Dill, Stripe)
**For:** debating and prioritizing what the walks found. **Steps:** team does the walkthrough together (engineer, PM, designer at minimum); fills the friction log and a rubric score; presents to a small multidisciplinary room incl. product marketing; room debates score and adjusts urgency. **Fails when:** the room is large.

### 3. Color-based quality rubric (Katie Dill)
**For:** subjective quality calls without arguing 6 vs 7. **Steps:** tag moments (nice touch, fix, P0); summarize with a color (e.g. yellow, yellow-green) across usability, utility, desirability and surprisingly great. It is judgment, not an objective score.

### 4. Quality score calibration (Katie Dill)
Each owner team scores its journey; leaders meet and test whether they interpret the bar consistently, as managers calibrate performance reviews; urgency follows the calibrated score.

### 5. Friction logging (David Singleton, Stripe)
**For:** any team, incl. internal tools. **Template:** state what you want to do, name the user you are modeling, then write a continuous stream-of-consciousness log; tag who must act; praise what is good. **Steps:** pick a specific user, do the real flow (dashboard, docs, writing code), flag friction that persona would hit, invest the most where friction appears. Also: treat errors as a product surface and link each API error to the doc that fixes it; be meticulous at high-stakes moments, not everywhere.

### 6. Group UX review (David Singleton)
Pre-ship review: product team, support and exec partners imagine a specific user while the PM walks the flow and everyone types issues into a shared log; decide on each issue at the end. Regular holistic friction logging keeps experiences cohesive when thousands of engineers diverge.

### 7. Stripe Study Groups (Jeff Weinstein)
**For:** mature, multi-team products with entropy. **Steps:** 4-8 volunteers from any function; invent a company, CEO and goal; Rule 1 you do not work at Stripe and use no internal knowledge; Rule 2 no solutioning, critiquing or bug filing in the session; use the product slowly for 60-90 minutes; funnel findings into existing bug/SLA processes. Escalation ladder: be your own customer, sit next to a customer, pantomime a customer. Failure mode: you stop looking.

### 8. Craft bug SLAs (Jeff Weinstein)
Add craft tags to the existing bug system; P0 craft bugs must be acknowledged within seven days; teams may relabel severity so they keep ownership. No new process required.

### 9. Complaint storms (Noah Weiss)
**For:** teams of power users building for newer customers, or a team at a dead end. **Steps:** gather the team (and a founder); start with an adjacent product, then your own; project the landing-to-first-value journey; everyone logs every confusing or stopping moment as if they did not work on it; use the output for calibration on pace and quality.

### 10. Person, not persona wall (Anuj Rathi)
Define one specific person (age, income, last month's behavior, needs, fears), pick a moment (what triggered the app open at 11:00), and design each screen, word and pixel for it; on marketplaces plot the other side's timeline too. Keep a current-version wall and a new-version wall. Heavy, so use on key journeys.

### 11. Design with real, messy data (Bret Taylor)
Require design reviews to use real production-like data so designs work as systems across the distribution of inputs, not the best case. Applies to UGC and AI-generated output. Karri Saarinen adds: before release a sponsor tests the real build with varied states and message lengths, which exposes janky animation and scrolling.

### 12. Use it end to end for a real use case (Bangaly Kaba)
Teams build the pieces of a flow without the experience that delivers the output. Pick a real use case, complete it in the app, check the output is actually delivered.

## B. Comprehension, friction and complexity

### 13. Comprehension over friction (Stewart Butterfield)
Removing friction helps only when intent and comprehension are already high. For novel products and first visits ask: does the user know what this is and what to do next? Explain what happens after a click before asking for commitment. Right for registration, auth and checkout to cut friction; wrong default elsewhere.

### 14. Intent and specificity of intent (Butterfield)
Estimate strength and specificity of the visitor's intent. High both (concert tickets): friction barely matters. Partial (T-shirts about 70%): minimize checkout friction. Low specificity (a new category such as Slack): invest in comprehension.

### 15. Pretend you're a regular person / owner's delusion (Butterfield)
Stop, breathe, pretend to be an actual human with a messy day, then look at the page and check it makes sense in a fraction of a second; have others review. Owners wrongly assume visitors care as much as they do.

### 16. Don't Make Me Think (Butterfield, Noah Weiss, Tobi Lutke)
Every decision you force costs effort and, if not understood, makes the user feel stupid. Slack's principles add: be a great host (save steps) and more clicks can be okay when they build confidence in non-transactional software.

### 17. Uber Where to / Other pattern (Butterfield)
Find the 1-3 things people most want to do, surface only those, put everything else behind a single Other entry; group menu items with dividers. Eight easy taps beat two fraught ones. Fails for products where rapid tapping is the experience (Snapchat).

### 18. Shouty rooster (Butterfield)
For tragedy-of-the-commons features, add a friendly confirmation that states real cost (how many people, how many time zones) to deter and to teach.

### 19. Golden gut (Scott Belsky)
Reduce cognitive load by asking what if I remove this altogether; replace steps with presumptuous defaults users can change; accept that 10% may be confused if 90% get through far faster. Counterpoint: Jackson Shuttleworth found preselecting a goal sped users up but lost engagement, so do not remove productive friction.

### 20. Every tap is a miracle (Nikita Bier)
On consumer mobile, users bounce quickly. Watch a real person switch apps, audit each tap in the core flow, remove or merge any step that does not deliver value.

### 21. Irreducible complexity and keep simple things simple (Dylan Field)
Features have non-linear costs; one plus one sometimes equals one and a half. Watch the system, not local decisions, and revisit it when good decisions add up to something too complex. Everyone is responsible for simplicity: keep simple things simple, make complex things possible.

### 22. Remove unused features (Uri Levine) and Lower complexity (Tobi Lutke)
After adding features to find the ones people use, remove the rest. Absorb first-time-user complexity (taxes, payments, fraud) into the product; measure businesses that survive.

### 23. Hacks to avoid simple-to-complex cycle (Casey Winters)
Un-bundle (Messenger, Uber Eats), progressive disclosure (Pinterest), proactive training or training-wheels UI, segmented experiences by user type. Fails with heterogeneous, shifting users (Eventbrite).

### 24. Clarity over cleverness (Robby Stein)
Lean on standards users already understand; use the global icon (it's a camera); name features plainly; reinvent selectively. Do not contort an entrenched core surface for a new behavior; build a separate format.

### 25. System architecture design initiative (Vijay Iyengar)
Protect a three-month design-led block to define the few core building blocks and how users discover and relate them; hold related engineering until done. Consistent architecture multiplies the reach of every enhancement; design at the end of projects blows up scope.

## C. Deciding how much quality

### 26. Levels of quality (Katie Dill)
Level 1: delivers core value. Level 2: error-free and well-rounded. Levels 3-5: exceeds expectations and surprises. Levels are set by user expectation; users rarely ask for quality, but support cases reveal the gaps. Matters most once competition exists; the early first car needed less.

### 27. Value, ease of use, joy (Julie Zhuo)
Triage feedback in order: is it valuable for the target user and job, then ease of use (confusion, slowness), then joy. Disregard polish feedback until value is confirmed. State the stage at the start of a critique so rough prototypes do not draw comments on shades of blue.

### 28. Quality means meeting spec (Seth Godin)
Quality is not luxury; define the spec as delighting the target buyer, ship when it is met, and improve the spec if it is not good enough. Perfectionism is hiding. Karri Saarinen echoes: a perfection mindset makes it hard to ship.

### 29. Ship early to ourselves, polish at general release (Karri Saarinen)
Put the feature in the app in about the first week, internal only; recruit 1-10 opt-in customers; accept a janky state and say so; give full craft attention before GA.

### 30. Ship is one point on the journey (Nick Turley)
In AI you cannot know what to polish before shipping. Polish model output and critical basics first, ship, learn usage, then clean up. Fails if it becomes an excuse to never reach great.

### 31. Mission-critical means dial it up (Rahul Vohra)
Marketplaces with network effects need speed; mission-critical products like email cannot launch half-baked because a duplicate-send bug costs trust. Rahul also argues for game design, not gamification: fun toys combined into games, not points and badges.

### 32. Craft versus MVP (Eric Ries)
Perfection only means something for a specific customer; craft in engineering primitives speeds you up; craft as an excuse to avoid feedback is the failure mode. If craft is a core value you will not test, say so and test everything else more.

### 33. Obsess versus ship-fast triage (Ian Silber) and obsess over which details (Peter Deng)
Deep craft (try a hundred things, ship one) for durable, core interactions; ship in hours for fast-changing areas. Peter Deng: know which details do not matter; Uber Reserve crafted only the peace of mind that the car will come. Caitlin Kalinowski: iterate most on what the customer touches most.

### 34. Better means 10 out of 10 (Mark Pincus)
A real Better is one every existing user would endorse; what the team thinks is better is New and a likely failure. Craigslist added photos over two years to avoid angering habituated users.

### 35. Quality quarter (Amol Avasare) and pixie dust (Jiaona Zhang)
Avasare: Mercury's growth team spent a quarter ignoring metrics to fix onboarding quality. Zhang: ship table stakes, then scatter extra delight in a few chosen areas (keyboard shortcuts for power users, pre-populated templates) without pushing out launch.

### 36. Five reasons beauty matters in B2B (Katie Dill)
Trust (visible care signals care about invisible details), usability and better outcomes, beauty begets beauty, pride, talent attraction. Also: utility plus usability plus desirability; beauty alone is Blu-ray. Dmitry Zlokazov's Revolut and Karri Saarinen echo design as a differentiator in crowded categories.

### 37. Five ingredients of organizational quality (Katie Dill)
Shared care (not one star hire or QA), a unifying vision, an editor who can narrow and remove, courage to say almost but no, and a user-journey lens. Related: Evan Spiegel's design as intentional bottleneck and Dmitry Zlokazov's founder review of every screen (Revolut), which trade speed for cohesion and can bottleneck at scale.

## D. Building a taste bar and taste

### 38. Taste loop (Dylan Field)
Experience something, ask whether you like it and why, build repertoire and learn the canon, decide where you agree philosophically, look for cross-correlations, articulate your framework and revisit old views, and practice matching others' taste for brand work. Many can match a framework; few can create one.

### 39. Intuition as hypothesis generator (Dylan Field)
Generate hypotheses constantly, state them explicitly, find data that supports or negates, winnow to a working hypothesis. Julie Zhuo: data and design are complements; you still choose which numbers to look at.

### 40. Binary monthly quality triage (Varun Parmar)
Design leaders classify everything shipped that month as high quality or not, record why, and share the examples. Taste is easier shown than described. Needs democratizing to scale.

### 41. Design tenets vs principles (Bob Baxley)
Replace platitudes with 3-4 opinionated tenets that settle recurring debates; cap at 3-4; reference in every design debate. Example set: documentation is a failure state; start simple, opt into complexity; the product looks like it came from one mind. Operates at strategy level, not for single features.

### 42. Distill founder taste into principles (Noah Weiss)
Turn a founder's repeated feedback into explicit principles that become review language; teams explore within them and avoid Goldilocks reviews. Hilary Gridley: treat the high-bar CEO's repeated feedback as a principle and find high-impact, low-cost touches.

### 43. Taste as virtual machine in your head (Max Schoening)
Taste is simulating how a chosen in-group will react; build it with reps and feedback, own side projects end to end, surround yourself with great objects.

### 44. Exposure hours and exposure time (Guillermo Rauch, Lazar Jovanovic)
Quantify hours watching people use your product and others'; hand the product to someone and watch silently. Jovanovic: set aside more time for learning than building; study styles and the prompts that produce them. Others: Kayvon Beykpour (voracious user of many products), Howie Liu (study the chairs, then build your own; taste the soup by touching the model), Julie Zhuo's product-sense ladder (observe yourself, discuss, read teardowns, ask about A/B learnings), Jessica Hische's font feelings exercise and Song Exploder your intuition (ask why you felt that way).

### 45. Taste as distance from the LLM default (Alex Komoroske)
Compare your output to what an LLM would write from the same prompt; lean into where you differ and keep what resonates. Related: Lazar Jovanovic on the widened gap between good enough and world-class; fonts and copy carry outsized weight; Ian Silber and Jenny Wen debate whether taste remains a human moat.

### 46. Few taste makers at the heart (Aparna Chennapragada) and small group holds the bar (Archie Abrams)
As roles blur, keep one or a few editors or taste makers; Abrams: core teams judged on shipping the right thing, held by a small group reviewing releases in depth. Without a defined bar it becomes unaccountable.

### 47. Shipping Frankensteins guard (Elizabeth Stone)
When non-designers build, have senior designers encode templates and brand expression so everyone ships coherent work. Dylan Field: start AI prototypes inside the design system so ideas are judged on merit.

## E. Reviewing the artifact at the right stage

### 48. State the stage (Julie Zhuo) and polished-prototype anchoring (Andrew Ambrosino)
Open critique with where the work is and what feedback is wanted; separate visual polish from readiness of the underlying user and business model; treat a polished prototype as something to test against.

### 49. Many reviews, different audiences (Julie Zhuo)
Design peers, the team, outsiders, target customers; synthesize against target user and problem; do not decide by consensus.

### 50. Block brain diagrams and drawing badly (Bob Baxley, Christina Wodtke)
Ultra low-fi chunky blocks so reviewers discuss concept, not looks; sketch badly on a whiteboard with engineers so others fix it. Ryan Singer: Figma is for picking the tile once the kitchen layout is settled.

### 51. Prototype to feel it and extreme versions (Tamar Yehoshua, Nan Yu)
A mock-up does not tell you what it will feel like. Nan Yu: ask for the most outrageous version along a trait, build it, then find the balance (Linear draft-saving: fastest, then safest, then a hybrid).

### 52. Design velocity (Evan Spiegel)
A weekly design review with no gate on what can be shown; hundreds of ideas a week; critique where learning happens. Spiegel also: art versus design, where design needs empathy and range.

## F. AI and agent surfaces

### 53. Wait-time UX by duration and reasoning like a human (Kevin Weil)
Long async tasks: design for leaving and returning. 10-25 second waits: summarized progress. At 400M users OpenAI settled on one-or-two-sentence reasoning summaries rather than raw chain of thought.

### 54. Show the work, calibrated; NLX is the new UX; design follow-ups (Aparna Chennapragada)
Prompts, editable plans, progress display and follow-ups are components. Tune verbosity, personalize over time, suggest next steps but cap volume. Contrast: Roman Ugarte hides internals and shows only an active dot and progressive updates.

### 55. Wrap the chatbot in use cases / under-merchandised capabilities / blank box (Benedict Evans, Howie Liu, Ian Silber)
Open prompt boxes leave users lost; wrap AI in use cases and let it disappear into the feature; show capabilities with visual metaphors; adaptive interface for novices and power users; tappable follow-ups; editable output blocks; no modes.

### 56. Now can vs now has (Roman Ugarte) and maximally accelerate the human (Alexander Embiricos)
Frame launches as capabilities rather than added pixels; natural-language automations replaced trigger-action builders. Order what users see by trust (preview before diff) and ship features that make the reviewing role feel empowered.

### 57. Trust through naturalness and visibility (Shweta Shrivastava)
For autonomous products, trust comes from many small designed signals: smooth predictable behavior, visibility into what the system sees, a reachable human; match human expectations even when the machine could go faster.

### 58. Make the user feel like a winner (Claire Vo)
Agents should make the end user look and feel good (proactive meeting prep with context) rather than upsell.

## G. Dogfooding and instincts

### 59. Be your own customer / dogfood by getting creative (Kayvon Beykpour, Yuhki Yamashita)
Use the product daily and note pain points; move internal workflows into it (Figma moved memos to decks built in Figma). Does not help for features aimed at customers unlike you.

### 60. Don't habituate to friction (Robby Stein)
Notice annoyances you currently tolerate and ask why they exist; treat each as an opportunity.

### 61. Complaint to underlying pain (Evan Spiegel, Nan Yu)
Spiegel: users asked for a send-all button but complained about pressure; Stories answered the pain (no public metrics, 24-hour expiry, chronological). Nan Yu: elicit the specific incident behind a complaint, then remove the feeling (flexible target-date granularity).
