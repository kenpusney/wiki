
A **spike** is a time-boxed research investigation used to reduce risk or uncertainty about a technical approach, design decision, or unknown requirement. Spikes are common in [[Extreme Programming|XP]] and [[Agile 101|agile]] development.

## What is a Spike?

A spike is not a user story or a feature — it's a **research activity** that produces knowledge, not working software. The goal is to answer questions, explore options, and reduce uncertainty before committing to implementation.

### Types of Spikes

#### Technical Spike
Explores a technical question or approach:
- "Can we integrate with this API?"
- "How do we handle this performance requirement?"
- "What's the best way to implement this algorithm?"

#### Functional Spike
Explores a business requirement or user need:
- "What does the customer really want here?"
- "How should this feature work?"
- "What are the edge cases?"

#### Design Spike
Explores architectural or design options:
- "Should we use microservices or monolith?"
- "How should we structure the database?"
- "What's the best way to handle this integration?"

## When to Use Spikes

### Before committing to a story
If you don't understand how to implement something, spike before estimating:
- Reduces estimation uncertainty
- Uncovers hidden complexity
- Identifies risks early

### When facing technical uncertainty
If you're unsure about a technical approach:
- Evaluate multiple solutions
- Prototype risky components
- Prove feasibility before building

### When exploring new technologies
If you need to learn a new tool, framework, or API:
- Build a proof of concept
- Understand limitations and capabilities
- Make informed adoption decisions

## How to Run a Spike

### 1. Define the question
Write a clear, specific question the spike should answer:
- ❌ "Research databases" (too broad)
- ✅ "Can PostgreSQL handle 10,000 concurrent connections with sub-100ms response times?" (specific)

### 2. Time-box it
Spikes should be short and focused:
- **1-2 days** is typical
- **Never more than a week**
- If you need more time, break it into smaller spikes

### 3. Document findings
Record what you learned:
- What options did you evaluate?
- What did you choose and why?
- What are the trade-offs?
- What are the remaining unknowns?

### 4. Present to the team
Share your findings with the team:
- Demo any prototypes
- Explain your recommendation
- Answer questions
- Decide next steps together

## Spike Output

A spike doesn't produce working code — it produces **knowledge**. Typical outputs include:

- **Recommendation** — Which approach to take
- **Prototype** — Proof of concept code (may be discarded)
- **Document** — Technical analysis or comparison
- **Updated estimates** — Better understanding of effort
- **Risk assessment** — Identified risks and mitigations

## Spike Best Practices

1. **Keep them short** — Spikes should be time-boxed, not open-ended
2. **Focus on the question** — Don't get sidetracked building things
3. **Time-box ruthlessly** — If you can't answer in the time-box, break it down
4. **Document everything** — Future you will thank present you
5. **Share with the team** — Knowledge should be distributed
6. **Don't spike forever** — At some point, you need to decide and build

## Spike Anti-Patterns

1. **Spike that never ends** — If you're still researching after a week, you're avoiding commitment
2. **Spike that produces production code** — Spikes produce knowledge, not features
3. **Spike without a clear question** — Know what you're trying to learn
4. **Spike without time-box** — Research expands to fill available time
5. **Spike that isn't shared** — Knowledge hoarding defeats the purpose

## Spike vs Spike Story

Some teams track spikes as stories in the backlog:
- **Spike story** — A backlog item for research, estimated and planned like other stories
- **Technical spike** — Research activity within a story, not tracked separately
- **Architecture spike** — Larger research effort, may span multiple sprints

## Spikes and Estimation

Spikes improve estimation by reducing uncertainty:
- Before spike: "This could take 2-10 days, we don't know"
- After spike: "We now know it will take about 5 days"

This makes sprint planning more reliable and reduces the risk of over-commitment.
