---
name: continuous-discovery
description: Implements Teresa Torres' continuous discovery habits for weekly customer contact, opportunity solution trees, and assumption testing. Use when building discovery processes, conducting user research, validating assumptions, or establishing product trio workflows.
---

# Continuous Discovery Habits

## When This Skill Activates

Claude uses this skill when:
- Setting up discovery processes
- Planning weekly user research
- Creating opportunity solution trees
- Testing assumptions
- Building product trio workflows
- Prioritizing discovery activities

## Core Frameworks

### 1. Continuous Discovery Habits (Source: Teresa Torres)

**The Core Principle:**
> "At a minimum, weekly touchpoints with customers by the team building the product, where they conduct small research activities in pursuit of a desired outcome."

**The Three Pillars:**
1. **Weekly customer contact** by the product trio (PM, designer, engineer)
2. **Opportunity solution trees** to visualize discovery
3. **Assumption testing** before building

**Use when:** Establishing discovery processes or improving product decisions

---

### 2. The Product Trio

**The Team:**
- **Product Manager:** Ensures business viability
- **Designer:** Ensures usability and desirability
- **Engineer:** Ensures feasibility

**Why Together:**
> "When a designer, engineer, and PM collaborate on discovery, you get better decisions faster. Each brings a unique lens."

**How:**
- All three participate in customer interviews
- All three analyze research together
- All three generate solutions together
- All three test assumptions together

---

### 3. Opportunity Solution Trees

**The Structure:**
```
Outcome (top)
    ↓
Opportunities (customer needs/pain points)
    ↓
Solutions (possible ways to address)
    ↓
Assumptions (what needs to be true)
    ↓
Experiments (how to test)
```

**Use when:** Need to visualize the path from outcome to solution

**Example:**
```
Outcome: Increase retention to 80%
    ↓
Opportunity: Users forget to use the product
    ↓
Solution: Daily email reminder
    ↓
Assumption: Users check email daily
    ↓
Experiment: Survey 20 users about email habits
```

---

### 4. Interview Snapshot

**The One-Pager:**
After each interview, create a snapshot capturing:
- **Date & Participant:** Who and when
- **Key Insights:** 3-5 main takeaways
- **Opportunities:** Customer needs/pain points discovered
- **Quotes:** Verbatim customer language
- **Next Steps:** What to test or explore next

**Why:** Keeps learning accessible to the whole team

---

### 5. Assumption Testing

**The Progression:**
```
Story → Assumptions → Tests → Evidence
```

**Question to Ask:**
> "What needs to be true for this solution to work?"

**Test Types (by risk/cost):**
1. **One-question surveys** (lowest risk)
2. **Customer interviews** 
3. **Prototypes/mockups**
4. **Concierge tests** (manual behind-the-scenes)
5. **Wizard of Oz** (fake the feature)
6. **Live data tests** (build and measure)

**Rule:** Test highest-risk assumptions first with lowest-cost method

---

## Decision Trees

### Should I Build This Feature?

```
Do we have a clear outcome?
├─ No → Define outcome first
└─ Yes → Have we interviewed 6+ customers?
    ├─ No → Do discovery first
    └─ Yes → Have we identified opportunities?
        ├─ No → Map opportunities
        └─ Yes → Have we tested key assumptions?
            ├─ No → Test assumptions first
            └─ Yes → Build it!
```

### How Should I Test This Assumption?

```
What's the risk if we're wrong?
├─ Low risk → Build and ship (reversible)
└─ High risk → How much does testing cost?
    ├─ Low cost → Interview 5 users
    ├─ Medium cost → Prototype test
    └─ High cost → Still cheaper than building wrong thing
```

---

## Action Templates

### Template: Weekly Discovery Plan

```markdown
# Weekly Discovery Plan - Week of [Date]

## Outcome We're Pursuing
[e.g., Increase activation rate to 50%]

## This Week's Focus
**Opportunity:** [Which pain point are we exploring?]
**Solution:** [Which solution are we considering?]
**Key Assumption:** [What needs to be true?]

## Discovery Activities (Minimum 1 per week)

### Monday-Wednesday: Research
- [ ] Interview 1: [Participant profile] - [PM/Designer/Engineer attending]
- [ ] Interview 2: [Participant profile] - [PM/Designer/Engineer attending]
- [ ] Interview 3: [Participant profile] - [PM/Designer/Engineer attending]

### Thursday: Synthesis
- [ ] Product trio synthesis session (30 min)
- [ ] Create/update interview snapshots
- [ ] Update opportunity solution tree
- [ ] Identify new assumptions to test

### Friday: Planning
- [ ] Review evidence collected
- [ ] Decide: build, test more, or pivot?
- [ ] Plan next week's discovery activities

## Interview Snapshots
[Link to snapshots folder]

## Opportunity Solution Tree
[Link to latest tree]
```

---

### Template: Interview Snapshot

```markdown
# Interview Snapshot - [Date]

## Participant
- **Name/ID:** [Anonymized if needed]
- **Role:** [Job title/persona]
- **Context:** [Relevant background]

## Interview Focus
[What we were trying to learn]

## Key Insights
1. [First major insight]
2. [Second major insight]
3. [Third major insight]

## Opportunities Discovered
- 📍 [Pain point or unmet need #1]
- 📍 [Pain point or unmet need #2]
- 📍 [Pain point or unmet need #3]

## Memorable Quotes
> "[Exact customer words that capture key point]"

> "[Another powerful quote]"

## Updated Assumptions
- ✅ Validated: [What we confirmed]
- ❌ Invalidated: [What we disproved]
- ❓ New: [New assumptions to test]

## Next Steps
- [ ] [Specific action based on learning]
- [ ] [Another action]

## Attending
- [PM name]
- [Designer name]
- [Engineer name]
```

---

### Template: Opportunity Solution Tree

```markdown
# Opportunity Solution Tree - [Product/Feature Name]

## Outcome
🎯 **[Business outcome we're driving]**
[Specific, measurable, time-bound]

---

## Opportunities (Customer Needs/Pain Points)

### Opportunity 1: [Customer problem]
**Evidence:** [3-5 customer interviews, usage data, etc.]
**Impact:** [How big is this problem?]

#### Solutions Being Considered:
1. **[Solution A]**
   - Assumptions:
     - [ ] Assumption 1
     - [ ] Assumption 2
   - Tests: [How we'll validate]
   - Status: [Testing/Building/Shipped]

2. **[Solution B]**
   - Assumptions:
     - [ ] Assumption 1
     - [ ] Assumption 2
   - Tests: [How we'll validate]
   - Status: [Testing/Building/Shipped]

### Opportunity 2: [Another customer problem]
**Evidence:** [3-5 customer interviews, usage data, etc.]
**Impact:** [How big is this problem?]

[Continue for each opportunity...]

---

## Decision Log
- **[Date]:** Chose Solution A for Opportunity 1 because [evidence]
- **[Date]:** Decided to test Assumption X before building
- **[Date]:** Pivoted from Solution B to Solution C based on [learning]
```

---

### Template: Assumption Test Plan

```markdown
# Assumption Test Plan - [Feature/Solution Name]

## Solution Statement
[Brief description of what we're considering building]

## Key Assumptions

### Assumption 1: [High Risk]
**Statement:** [What needs to be true]
**If wrong:** [What's the impact?]
**Confidence:** [Low/Medium/High]

**Test Method:** [Interview/Survey/Prototype/etc.]
**Success Criteria:** [What would validate this?]
**Timeline:** [When we'll test]
**Owner:** [Who's running the test]

---

### Assumption 2: [Medium Risk]
**Statement:** [What needs to be true]
**If wrong:** [What's the impact?]
**Confidence:** [Low/Medium/High]

**Test Method:** [Interview/Survey/Prototype/etc.]
**Success Criteria:** [What would validate this?]
**Timeline:** [When we'll test]
**Owner:** [Who's running the test]

---

## Test Results

### Assumption 1 Results
**Date Tested:** [Date]
**Method Used:** [What we did]
**Sample Size:** [How many participants]

**Findings:**
- [Key finding 1]
- [Key finding 2]
- [Key finding 3]

**Decision:** ✅ Validated / ❌ Invalidated / ❓ Needs more testing
**Next Steps:** [What we'll do based on results]

---

### Assumption 2 Results
[Same structure as above]
```

---

## Quick Reference

### 📅 Weekly Discovery Cadence

**Every Week Minimum:**
- [ ] 3-5 customer touchpoints (interviews, observation, etc.)
- [ ] Product trio participates together
- [ ] Create interview snapshots
- [ ] Update opportunity solution tree
- [ ] Test at least 1 assumption

**Every Month:**
- [ ] Review all evidence collected
- [ ] Update outcomes if needed
- [ ] Celebrate learning (not just building)

---

### 🎯 Discovery vs Delivery Balance

**Good Discovery Practice:**
- ✅ Discovery happens weekly (not just quarterly)
- ✅ Product trio does discovery together
- ✅ Small tests before big builds
- ✅ Evidence-based decisions
- ✅ Comfortable saying "we learned that won't work"

**Signs of Insufficient Discovery:**
- ❌ Only talking to customers after shipping
- ❌ PM does all research alone
- ❌ Building first, validating later
- ❌ Opinion-based decisions
- ❌ Fear of "wasting time" on research

---

### 🌳 Opportunity Solution Tree Checklist

**Before Creating:**
- [ ] Clear outcome defined
- [ ] Conducted 6+ customer interviews
- [ ] Identified multiple opportunities

**When Building Tree:**
- [ ] Start with ONE outcome (top)
- [ ] Map opportunities (not solutions)
- [ ] Generate multiple solutions per opportunity
- [ ] List assumptions for each solution
- [ ] Plan tests for assumptions

**Using the Tree:**
- [ ] Update weekly with new learning
- [ ] Share with stakeholders
- [ ] Use to explain why you're building what
- [ ] Reference when prioritizing work

---

### 🧪 Assumption Testing Hierarchy

**Test in This Order:**
1. **Desirability** - Do customers want this?
2. **Usability** - Can they use it?
3. **Feasibility** - Can we build it?
4. **Viability** - Should we build it?

**Use Cheapest Test First:**
```
Interview < Survey < Prototype < Concierge < Build
```

---

## Real-World Examples

### Example: Spotify's Discovery Process

**Outcome:** Increase music discovery engagement

**Opportunity:** Users don't know what to listen to
- Evidence: Interviews showed decision fatigue
- Solution considered: Algorithmic playlists
- Assumption: Users trust algorithmic recommendations
- Test: Created Discover Weekly, measured engagement
- Result: Massive success, became core feature

**Key Learning:** They tested the algorithm assumption before building fancy UX

---

### Example: Netflix's Continue Watching

**Outcome:** Reduce time to content consumption

**Opportunity:** Users forget what they were watching
- Evidence: Drop-off analysis + customer interviews
- Solution: "Continue Watching" row
- Assumption: Users want to resume (not restart)
- Test: A/B test with 5% of users
- Result: Validated, rolled to 100%

**Key Learning:** Small test before full build saved months of work

---

## Common Pitfalls

### ❌ Discovery Theater
**Problem:** Doing research but not changing decisions
**Solution:** Explicitly decide what you'll do if assumptions are wrong

### ❌ Outsourcing Discovery
**Problem:** PM does research, then "throws it over the wall"
**Solution:** Product trio interviews together

### ❌ Building Multiple Solutions at Once
**Problem:** Spreading resources too thin
**Solution:** Test assumptions first, build one at a time

### ❌ Skipping Discovery "To Move Fast"
**Problem:** Building wrong thing is slowest path
**Solution:** Small tests are faster than big rebuilds

### ❌ Only Talking to Happy Customers
**Problem:** Missing problems and churn reasons
**Solution:** Interview across the spectrum (new, power, churned users)

---

## Key Quotes

**Teresa Torres on Weekly Contact:**
> "If you're not talking to customers every week, you're not doing continuous discovery."

**On Product Trios:**
> "The best product decisions come from diverse perspectives. A PM, designer, and engineer will see different things in the same customer interview."

**On Opportunity Solution Trees:**
> "The tree makes your thinking visible. It shows how you got from an outcome to a solution, which builds stakeholder trust."

**On Assumption Testing:**
> "Don't ask customers what to build. Test assumptions about what will work."

**On Discovery vs Delivery:**
> "Discovery and delivery should happen continuously. Discovery doesn't end when you start building."

---

## Related Skills

**Use together with:**
- **user-feedback-system** - For ongoing feedback collection
- **jtbd-building** - For understanding customer motivations
- **exp-driven-dev** - For testing assumptions with data
- **metrics-frameworks** - For defining outcomes
- **strategic-build** - For deciding what's worth discovering

**Comes before:**
- **zero-to-launch** - Discover before building
- **design-first-dev** - Design based on discovery

**Comes after:**
- **strategy-frameworks** - Define strategy, then discover how

---

## Quick Start Guide

### Week 1: Set Up Discovery Process
1. Form product trio (PM, designer, engineer)
2. Define one clear outcome to pursue
3. Schedule first 3 customer interviews
4. Create interview snapshot template

### Week 2: Start Discovery Habit
1. Conduct 3 interviews together
2. Create interview snapshots
3. Begin opportunity solution tree
4. Identify opportunities from interviews

### Week 3: Map Solutions
1. Generate 3+ solutions per opportunity
2. List assumptions for each solution
3. Prioritize which assumptions to test
4. Plan assumption tests

### Week 4: Test Assumptions
1. Run first assumption tests
2. Update opportunity solution tree
3. Decide: build, test more, or pivot
4. Make discovery routine sustainable

---

**Remember:** Continuous discovery isn't a phase. It's a habit. The product trio that talks to customers weekly makes better product decisions.

---

**Guest:** Teresa Torres  
**Book:** Continuous Discovery Habits (2021)  
**Website:** [producttalk.org](https://www.producttalk.org/)  
**Known for:** Opportunity Solution Trees, Product Trios, Weekly Touchpoints

