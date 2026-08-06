
Velocity is a metric that measures the amount of work a team completes during a sprint. It's calculated by summing the [[User Story Points|story points]] of all completed backlog items at the end of a sprint.

## What is velocity?

Velocity measures how much work a team gets done per sprint. It's typically measured in story points, though some teams use task counts or ideal days.

Velocity is not a measure of individual productivity — it's a **team-level metric** that reflects the team's collective capacity to deliver work.

## How to calculate velocity

Velocity = Total story points of completed items in a sprint

**Example:**

| Sprint | Completed Items | Story Points |
|--------|----------------|-------------|
| Sprint 1 | A(5) + B(3) + C(2) | 10 |
| Sprint 2 | D(8) + E(3) + F(2) | 13 |
| Sprint 3 | G(5) + H(5) + I(3) | 13 |
| Sprint 4 | J(8) + K(5) | 13 |

**Average velocity** = (10 + 13 + 13 + 13) / 4 = **12.25 points per sprint**

It typically takes 3-5 sprints for a team to establish a stable velocity baseline.

## Using velocity for planning

### Sprint planning
With a known velocity, the team can select backlog items that match their capacity:

- Average velocity: 13 points
- Select items totaling approximately 13 points
- Leave a small buffer (10-20%) for unexpected work

### Release planning
Velocity helps predict when features will be delivered:

- 50 story points remaining
- Team velocity: 13 points/sprint
- Estimated completion: ~4 sprints

### Predictability
Compare planned vs. completed story points to measure team predictability:

```
Commitment reliability = Completed points / Planned points × 100%
```

Aim for 80-100% reliability. Consistently below 80% suggests over-commitment.

## Factors that affect velocity

- **Team changes** — Adding or removing members changes dynamics
- **Technical debt** — Accumulated debt slows delivery
- **Tool/process changes** — New tools require learning curves
- **Sprint interruptions** — Unplanned work reduces capacity
- **Team maturity** — New teams take time to stabilize
- **Scope changes** — Mid-sprint changes affect completion

## Common velocity mistakes

1. **Comparing velocity across teams** — Velocity is team-specific. A team with 13 points is not "slower" than a team with 20 points.
2. **Using velocity as a productivity metric** — Velocity measures capacity, not individual output. Using it to evaluate people undermines trust.
3. **Chasing higher velocity** — The goal is consistent, sustainable delivery — not ever-increasing numbers.
4. **Ignoring incomplete work** — Only count fully completed items. Partially done work counts for zero velocity.
5. **Changing the DoD** — If the [[Definition of Done]] changes, previous velocity numbers become incomparable.

## Velocity vs throughput

| Metric | What it measures | Unit |
|--------|-----------------|------|
| **Velocity** | Effort completed per sprint | Story points |
| **Throughput** | Number of items completed per time period | Count of items |

Both are useful. Throughput is particularly valuable for Kanban teams that don't use story points.
