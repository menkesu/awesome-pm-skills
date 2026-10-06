# Eval Plan - Verified Quotes

## Start from data, not tests
> "You should start with some kind of data analysis to ground what you should even test, and that's a little bit different than software engineering where you have a lot more expectations of how the system is going to work." — Hamel Husain, Lenny's Podcast (00:10:06)

> "They have a suite of generic tools, cosine similarity, hallucination score, whatever, and that doesn't work." — Hamel Husain, Lenny's Podcast (01:22:06)

> "The goal is not to do evals perfectly, it's to actionably improve your product." — Shreya Shankar, Lenny's Podcast (01:26:37)

## Error analysis
> "The answer is, just write down the first thing that you see that's wrong, the most upstream error. Don't worry about all the errors, just capture the first thing that you see that's wrong, and stop, and move on." — Hamel Husain, Lenny's Podcast (00:22:38)

> "So basic counting is the most powerful analytical technique in data science because it's so simple and it's kind of undervalued in many cases, and so it's very approachable for people." — Hamel Husain, Lenny's Podcast (00:32:06)

> "It's when you are theoretically saturating or you're not uncovering any new types of notes, new types of concepts, or nothing that will materially change the next part of your process." — Shreya Shankar, Lenny's Podcast (00:30:31)

> "People's opinions of good and bad change as they review more outputs, they think of failure modes only after seeing 10 outputs they would never have dreamed of in the first place," — Shreya Shankar, Lenny's Podcast (01:03:35)

## Triage and judges
> "Because you're asking the judge to do one thing, evaluate one failure mode, so the scope of the problem is very small and the output of this LLM judge is pass or fail." — Shreya Shankar, Lenny's Podcast (00:49:49)

> "That's just in most cases, that's a weasel way of not making a decision." — Hamel Husain, Lenny's Podcast (00:52:16)

> "before you release your LLM as a judge, you want to make sure it's aligned to the human." — Hamel Husain, Lenny's Podcast (00:56:28)

> "if you only have the error 10% of the time, then you can easily have 90% agreement by just having a judge say it passes all the time." — Hamel Husain, Lenny's Podcast (00:57:55)

> "They don't have this matrix and they haven't iterated to make sure that these two types of errors have gone down to zero, then it's a bad smell. Go and ask them to go fix that." — Shreya Shankar, Lenny's Podcast (00:59:56)

> "You shouldn't do an eval like this for everything, just the pesky ones that you've described your ideal behavior in your agent prompt, but it's still failing." — Shreya Shankar, Lenny's Podcast (01:05:23)

> "So it doesn't have the same kind of gut. It's thinking about what you probably want hear too much." — Dan Shipper, Lenny's Podcast (00:38:07)

## Production and iteration
> "I can sample 1000 traces every day, run my LLM judge, real production traces, and see what the failure rate is there." — Shreya Shankar, Lenny's Podcast (00:51:28)

> "I think the products that are doing this, they have a very sharp sense of how well their application is performing, and people don't talk about it, because this is their moat." — Shreya Shankar, Lenny's Podcast (01:07:48)

> "So I feel evals are important, production monitoring is important, but this notion of only one of them is going to solve things for you that is completely dismissible in my opinion." — Kiriti Badam, Lenny's Podcast (00:33:47)

> "Whenever we put these models in contact with reality and we learn about a problem, we actually go back and make sure we have good metrics for this stuff." — Nick Turley, Lenny's Podcast (00:57:25)

## Evals as the product spec
> "Here's a question you want to be able to ask. Here's an amazing answer for that question. And then turning those into evals and then hill climbing on those evals." — Kevin Weil, Lenny's Podcast (00:21:57)

> "If the model gets it right 60% of the time, you build a very different product than if the model gets it right 95% of the time versus if the model gets it right 99.5% of the time." — Kevin Weil, Lenny's Podcast (00:18:16)

> "we actually have a saying on the team of evals are the new PRDs." — Dianne Penn, Lenny's Podcast (00:41:00)

> "this might be the lingua franca of how to communicate what the product should be doing to people who do AI research." — Nick Turley, Lenny's Podcast (01:14:41)

## Debates: when to skip or delay evals
> "I think for a completely novel product experience or form factor, you should actually not start with evals and you should start with vibes, right?" — Howie Liu, Lenny's Podcast (01:03:50)

> "coding agents are fundamentally very different than other AI products, because the developer is the domain expert, so you can short circuit a lot of things," — Hamel Husain, Lenny's Podcast (01:14:31)

> "You're not doing evals. That's not evals. Those are model evals." — Aishwarya Naresh Reganti, Lenny's Podcast (00:41:03)

> "The easiest way to climb LLM Arena, it's adding crazy boating. It's doubling the number of emojis. It's tripling the length of your model responses, even if your model starts hallucinating and getting the answer completely wrong." — Edwin Chen, Lenny's Podcast (00:23:53)

## Security and adversarial testing
> "humans break everything. A hundred percent of the defenses in maybe like 10 to 30 attempts." — Sander Schulhoff, Lenny's Podcast (00:33:25)

> "you can patch a bug, but you can't patch a brain." — Sander Schulhoff, Lenny's Podcast (00:40:49)

> "the number of possible attacks against another LLM is equivalent to the number of possible prompts. Each possible prompt could be an attack." — Sander Schulhoff, Lenny's Podcast (00:31:04)

> "if the smartest AI researchers in the world can't solve this problem, why do you think some random enterprise who doesn't really even employ AI researchers can?" — Sander Schulhoff, Lenny's Podcast (00:37:02)
