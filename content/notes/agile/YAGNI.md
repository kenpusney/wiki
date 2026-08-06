
YAGNI (You Aren't Gonna Need It) is an [[Extreme Programming|XP]] practice that says: **don't build something until you actually need it.**

## What is YAGNI?

YAGNI is the principle that you should not add functionality until it is necessary. It's about resisting the temptation to build for hypothetical future needs.

### The YAGNI mindset

- "We might need this later" → Don't build it now
- "It would be nice to have" → Don't build it now
- "What if we need to..." → Don't build it now
- "This is a good opportunity to add..." → Don't build it now

## Why YAGNI Matters

### Reduces waste
- Code you don't write doesn't need to be tested
- Code you don't write doesn't need to be maintained
- Code you don't write doesn't need to be documented

### Faster delivery
- Less code to write = faster completion
- Fewer features = simpler design
- Focus on what matters today

### Better design
- You understand the problem better later
- Future requirements may be different than you expect
- Simple design beats speculative design

### Less technical debt
- Unused code rots
- Unused code confuses future developers
- Unused code increases the surface area for bugs

## YAGNI in Practice

### Before writing code, ask:
1. **Do we need this right now?** — Not "will we ever need this"
2. **Is there a simpler way?** — Can we solve the problem with less code?
3. **What's the cost of adding this?** — Not just writing, but testing, maintaining, documenting

### When to add functionality:
- When a user story requires it
- When a test fails because it's missing
- When the customer explicitly asks for it
- When it's the simplest thing that could possibly work

## YAGNI vs The Future

| Approach | YAGNI | Speculative |
|----------|-------|-------------|
| **When to build** | When needed | When imagined |
| **Risk** | Low (you know the need) | High (you might be wrong) |
| **Cost** | Only when necessary | Upfront investment |
| **Flexibility** | High (can change direction) | Low (committed to design) |

## Common YAGNI Violations

1. **"Let's add a hook for future extensibility"** — Add it when you need to extend
2. **"We should support multiple languages"** — Add i18n when you have a second language
3. **"Let's make this configurable"** — Add configuration when you have different configurations
4. **"We might need to scale this"** — Optimize when you have a scaling problem

## YAGNI and XP Practices

- **[[Simple Design]]** — YAGNI is a key input to simple design
- **[[Refactoring]]** — It's easy to add later because you can refactor
- **[[Test-Driven Development]]** — Tests document what you actually built
- **[[Small Releases]]** — Frequent releases let you learn what you actually need
- **[[Sustainable Pace]]** — Less code = less maintenance = sustainable pace
