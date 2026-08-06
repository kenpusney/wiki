
SAFe (Scaled Agile Framework) is a framework for scaling agile practices across large organizations with multiple teams. It provides guidance at the portfolio, program, and team levels.

## What is SAFe?

SAFe is designed for organizations that need to coordinate agile work across many teams. It extends Scrum and XP practices to work at scale, introducing new roles, events, and artifacts.

## SAFe Levels

| Level | Focus | Key Concept |
|-------|-------|-------------|
| **Team** | Individual team execution | [[Scrum Framework|Scrum]], [[Kanban]], [[Extreme Programming|XP]] |
| **Program** | Cross-team coordination | Agile Release Train (ART), [[PI Planning]] |
| **Large Solution** | Complex, multi-team solutions | Solution Train, Solution Management |
| **Portfolio** | Strategic alignment | Lean Portfolio Management, Value Streams |

## Core SAFe Concepts

### Agile Release Train (ART)

An ART is a long-lived team of agile teams (typically 5-12 teams, 50-125 people) that aligns to a shared mission and roadmap.

- Teams work in synchronized [[Sprint|Sprints]] or iterations
- [[PI Planning]] aligns the entire ART every 8-12 weeks
- A [[Scrum Master]] or Release Train Engineer (RTE) facilitates coordination

### [[PI Planning]]

[[PI Planning]] is the cornerstone event in SAFe. Every 8-12 weeks, all teams on the ART come together to:
- Share vision and context
- Identify dependencies
- Create a shared plan
- Commit to PI Objectives

### Program Increment (PI)

A PI is a timebox (typically 8-12 weeks, or 4-6 Sprints) during which an ART delivers value. It's like a super-Sprint at the program level.

### Lean Portfolio Management

Aligns strategy and execution by:
- Defining strategic themes
- Managing portfolio backlog
- Governing with lightweight controls

## SAFe Principles

1. **Take an economic view** — Deliver early and often, minimize waste
2. **Apply systems thinking** — Optimize the whole, not just parts
3. **Assume variability; preserve options** — Build in contingency
4. **Build incrementally with fast, integrated learning cycles** — Short iterations with fast feedback
5. **Base milestones on objective evaluation of working systems** — Working software is the measure of progress
6. **Make value flow visible** — Visualize work, limit WIP, manage queue sizes
7. **Apply cadence, synchronize with cross-domain planning** — Regular rhythm for coordination
8. **Unlock the intrinsic motivation of knowledge workers** — Autonomy, mastery, purpose
9. **Decentralize decision-making** — Empower teams
10. **Organize around value** — Structure teams around value streams

## SAFe vs Scrum

| Aspect | Scrum | SAFe |
|--------|-------|------|
| **Scope** | Single team | Multiple teams |
| **Iterations** | 1-4 weeks | 8-12 week PIs (with 2-4 week Sprints inside) |
| **Planning** | Sprint Planning | [[PI Planning]] (plus Sprint Planning) |
| **Roles** | PO, SM, Dev Team | Added: RTE, Product Management, Business Owners |
| **Artifacts** | Product/Sprint Backlog | Added: Program Backlog, PI Objectives |

## SAFe and Other Practices

- **[[Kanban]]** — Used at multiple levels in SAFe for flow management
- **[[Extreme Programming|XP]]** — Engineering practices are encouraged at the team level
- **[[User Stories]]** — Work items at the team level
- **[[Feature]]** — Work items at the program level
- **[[Epic]]** — Work items at the portfolio level
- **[[Retrospectives|Inspect and Adapt]]** — SAFe's version of retrospectives at the PI level

## When to Use SAFe

SAFe works well when:
- You have 5+ agile teams that need to coordinate
- There are significant cross-team dependencies
- The organization needs visibility into progress at scale
- Regulatory or compliance requirements exist

SAFe may be overkill when:
- You have fewer than 5 teams
- Teams are largely independent
- The organization is already agile at scale
