---
name: one-step-better-ai-pm
description: Get one actionable improvement for your AI product based on the latest GenAI PM briefs. Fetch the last 5 days of curated AI PM insights from genaipm.com, analyze the current repo/project, find synergy between trending topics and the user's work, then research the source material and apply a concrete improvement. Use when the user wants to improve their AI product, get coaching on AI PM best practices, apply the latest industry insights to their codebase, or run "/one-step-better-ai-pm". Requires a GenAI PM subscriber email (set GENAIPM_EMAIL env var or provide when prompted).
---

# One Step Better AI PM

Get 1% better at AI product management every day. Pull the latest curated insights from GenAI PM, find what applies to the current project, and apply one concrete improvement.

## Prerequisites

- GenAI PM subscription (free at https://genaipm.com)
- Subscriber email via `GENAIPM_EMAIL` env var or provided when prompted

## Workflow

### Phase 1: Fetch the Latest Briefs

1. Get subscriber email: check `GENAIPM_EMAIL` env var first, then ask the user
2. Fetch briefs:
   ```
   WebFetch https://genaipm.com/api/feed/latest?email=<email>
   ```
3. Parse the JSON response — `data` array contains up to 5 entries, each with `date`, `title`, and `content` (full HTML)
4. Extract key insights across all briefs:
   - New AI capabilities, model releases, API changes
   - Developer tools, frameworks, libraries
   - Real-world implementation patterns and case studies
   - Claude Code, Cursor, and AI coding assistant tips
   - Product management frameworks, methodologies, processes
   - Infrastructure, deployment, and DevOps patterns

If the API returns a 401, tell the user to subscribe at https://genaipm.com and set their email.

### Phase 2: Build a Repo Profile

Create a structured summary of the project across 4 dimensions. This profile drives relevancy matching in Phase 3.

**Step 1: Read universal discovery files** (check each, skip if missing):

- `README.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules` — project description and conventions
- `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod` — dependencies and stack
- `docs/` directory listing — look for product briefs, architecture docs, or design docs and read them
- `.claude/settings.json`, `.claude/hooks.json`, `.claude/skills/` — AI assistant setup

**Step 2: Scan the codebase structure:**

- List top-level directories to understand project layout
- Grep for AI/LLM SDK imports (openai, anthropic, langchain, langgraph, google.generativeai, xai, cohere, replicate, huggingface, etc.)
- Grep for API keys/env vars referencing AI services
- Identify the main entry points and core business logic files

**Step 3: Summarize into 4 dimensions:**

1. **Product/Business** — What does this product do? Who is it for? What problem does it solve? What is the core user-facing value?
2. **AI/ML Usage** — Which AI models, APIs, and providers are used? What does the AI do in this product? (generation, curation, classification, chat, agents, embeddings, etc.) What's the AI pipeline?
3. **Technology Stack** — Languages, frameworks, databases, hosting, key libraries. Frontend vs backend vs infra.
4. **Dev Tooling** — CI/CD, testing, linting, AI coding tools (Claude Code, Cursor, Copilot), hooks, skills, MCP servers.

Write this summary internally before proceeding — it's the lens for matching briefs.

**Step 4:** Read `.one-step-better/history.json` if it exists — skip previously applied improvements.

### Phase 3: Match, Rank, and Present (Approval Gate)

**Do NOT proceed to Phase 4 without explicit user approval.**

**Step 1: Score each brief item against the repo profile.**

For every distinct insight in the briefs, score it on these criteria (highest priority first):

1. **Core product relevance** — Does this directly relate to what the product does? (e.g., a new model for a product that uses LLMs, a curation technique for a product that curates content, a payment integration for an e-commerce product)
2. **AI/ML pipeline relevance** — Does this improve, extend, or optimize the AI/ML capabilities the project already uses? (e.g., a new model from a provider already in use, a better prompting technique, an evaluation framework)
3. **Technology stack relevance** — Does this relate to the specific frameworks, languages, or infrastructure in use? (e.g., a Next.js performance improvement for a Next.js app, a Python library for a Python project)
4. **Dev tooling relevance** — Does this improve the development workflow? (e.g., CI/CD, testing, AI coding tools)

Items matching criteria 1-2 should always rank above items matching only 3-4. A new model option for your AI pipeline beats a dev tooling tip every time.

**Step 2: Present the top matches.**

1. **"Your repo profile:"** — Show the 4-dimension summary from Phase 2 (2-3 sentences total) so the user can verify understanding
2. **"From the latest GenAI PM briefs:"** — List 2-3 highest-scoring items. For each:
   - What the brief covered (1-2 sentences)
   - Why it's relevant to this project specifically (reference the repo profile)
3. **"Recommended improvement:"** — For the #1 match:
   - What to do (specific and concrete)
   - Which files would be affected
   - Expected benefit
   - Estimated time to apply
4. **Ask:** "Want me to research this and apply it?"

Wait for the user to approve, pick a different item, or decline.

### Phase 4: Deep Research & Apply

Once approved:

1. **Research the source** — Extract URLs from the brief item's HTML. Use WebFetch to read the original article, blog post, docs, or repo. If the brief mentions a tool or technique, search the web for official documentation.
2. **Apply the improvement** — Make the concrete change based on deep research and understanding of the repo. Examples:
   - Add or update Claude Code hooks, skills, or MCP configuration
   - Refactor code to use a new pattern or API from the brief
   - Add a new capability based on a tool or framework mentioned
   - Improve prompts, CLAUDE.md, or AI assistant setup
   - Update dependencies to leverage new features
3. **Explain what changed** — Summarize: files modified, why (linked to the brief insight), and how it helps this project

### Phase 5: Track Progress

1. Create `.one-step-better/history.json` if it doesn't exist
2. Append an entry:
   ```json
   {
     "date": "<today>",
     "briefDate": "<brief date>",
     "briefTitle": "<brief title>",
     "improvement": "<short description>",
     "filesChanged": ["<path1>", "<path2>"]
   }
   ```
3. Report: "You've applied N improvements from GenAI PM briefs."
4. Suggest adding `.one-step-better/` to `.gitignore` if not already there

## Guidelines

- Always wait for approval in Phase 3 before making changes
- Skip improvements already in `.one-step-better/history.json`
- Prioritize improvements to the core product over dev tooling — a new model option for the AI pipeline is more valuable than a linting hook
- If no briefs are relevant to the project, say so honestly and suggest checking back tomorrow
- The repo profile is the key to relevancy — spend the time to build an accurate one
