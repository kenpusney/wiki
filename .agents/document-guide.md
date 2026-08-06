
# Agent Facing Document Guide

## What's Agent Facing Documents

Agent Facing Document means any document that's named `AGENTS.md` or under `.agents/`.

## Principles

- **Agent first**: Write agent facing documents for agents, not humans. Prefer direct, accurate instructions over rationale. For skills, put detail in `references/`, do not inline it.
- **Agent neutral**: Do not depend on a specific agent, runtime, or harness. Use standard `agentskills.io` structure: YAML frontmatter, Markdown body, optional `references/`.
- **Focused**: Each skill owns one capability with a clear trigger and output. Prefer small skills. Do not let a skill expand past its workflow boundary.
- **Size controlled**: Documents must stay within total 100 lines. For skills, draft fully if needed, then extract bulk detail into `references/`. Keep references as long as necessary, but avoid duplication.
- **User-centric**: Start from real user scenarios. Do not add ceremony without evidence that it helps.
- **Experience-driven**: Distill from concrete execution, failures, friction, and feedback, not theoretical completeness.

## Language rules

- **English**: Write agent facing documents in English unless project convention says otherwise.
- **Output language**: Agent-facing artifacts stay in English. Human-facing output must match the user's prompt language.
