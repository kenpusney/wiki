
Simple Design is an [[Extreme Programming|XP]] practice that says: **always run with the simplest design that could possibly work.**

## The Four Rules of Simple Design

Kent Beck defined four rules for evaluating design, **in priority order**:

1. **Passes the tests** — All tests pass
2. **Reveals intention** — Code clearly expresses what it does
3. **No duplication** — Each piece of knowledge appears once
4. **Fewest classes/methods** — Minimum elements needed

If you have to sacrifice one rule, sacrifice the lower-priority one. For example, slightly more code (violating rule 4) is acceptable if it removes duplication (satisfying rule 3).

## What Simple Design is NOT

- **Big Design Up Front (BDUF)** — Designing everything before coding
- **No design** — Writing code without any thought
- **Premature abstraction** — Creating abstractions before you need them
- **Over-engineering** — Building for hypothetical future needs

## Why Simple Design Matters

### Reduces complexity
- Less code to understand and maintain
- Fewer places for bugs to hide
- Easier onboarding for new developers

### Enables change
- Simple code is easier to refactor
- Less effort to modify or extend
- Lower risk of breaking things

### Saves time
- Less time writing code
- Less time debugging
- Less time explaining to others

## How to Achieve Simple Design

1. **Write the simplest code that passes the tests** — Don't add anything you don't need right now
2. **Refactor constantly** — Remove duplication, improve naming, clarify intent
3. **Delay decisions** — Wait until you have more information before committing to a design
4. **Trust your tests** — If tests pass, the design is working

## Simple Design and XP Practices

- **[[Test-Driven Development]]** — Tests give you the confidence to keep the design simple
- **[[Refactoring]]** — Continuously improve design without changing behavior
- **[[Pair Programming]]** — Two perspectives prevent over-engineering
- **[[Collective Code Ownership]]** — Simple code is easier for everyone to work with
- **[[YAGNI]]** — You Aren't Gonna Need It — don't build for the future
