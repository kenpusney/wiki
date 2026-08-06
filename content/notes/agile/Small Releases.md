
Small Releases is an [[Extreme Programming|XP]] practice of delivering working software in small, frequent increments. The goal is to get feedback early and reduce risk.

## Why Small Releases?

### Faster feedback
- Learn from users quickly
- Validate assumptions early
- Adjust direction before investing too much

### Reduced risk
- Smaller changes are easier to understand and debug
- If something goes wrong, the blast radius is small
- Easier to roll back

### Continuous delivery
- Always releasable codebase
- No "big bang" releases
- Predictable delivery cadence

### Better planning
- Short feedback loops improve estimation
- Actual usage informs future priorities
- Technical debt is addressed incrementally

## How to Practice Small Releases

### Release early, release often
- Release as soon as a story is complete and passes [[Definition of Done|Definition of Done]]
- Don't wait for "the perfect moment"
- A working feature today is worth more than a perfect feature next month

### Keep releases small
- Each release should contain a small number of changes
- Easier to understand what caused issues
- Faster to test and deploy

### Automate the release process
- [[Continuous Delivery]] makes small releases practical
- [[Continuous Integration]] ensures code is always releasable
- Automated testing catches issues before they reach users

### Use feature flags
- Deploy code without exposing it to users
- Gradually roll out features
- Quick rollback if something goes wrong

## Small Releases vs Big Releases

| Aspect | Small Releases | Big Releases |
|--------|---------------|-------------|
| **Frequency** | Daily/weekly | Monthly/quarterly |
| **Risk** | Low | High |
| **Feedback** | Fast | Slow |
| **Rollback** | Easy | Difficult |
| **Planning** | Adaptive | Predictive |
| **Stress** | Low | High |

## Common Challenges

### "We need to release everything together"
- Use feature flags to decouple deployment from release
- Release partially, iterate based on feedback

### "Our release process is too slow"
- Invest in [[Continuous Delivery]]
- Automate testing and deployment
- Start with one component, expand gradually

### "Stakeholders want a fixed release date"
- Release on a cadence (weekly, bi-weekly)
- Negotiate scope, not dates
- Show the benefits of early feedback

## Small Releases and XP Practices

- **[[Continuous Integration]]** — Keeps code always releasable
- **[[Continuous Delivery]]** — Automates the release process
- **[[Test-Driven Development]]** — Ensures quality at every release
- **[[Sustainable Pace]]** — Frequent releases are sustainable; big releases are stressful
- **[[Planning Game]]** — Velocity guides what to release when
