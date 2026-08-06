
Technical debt is the implied cost of additional rework caused by choosing an easy solution now instead of using a better approach that would take longer. Like financial debt, technical debt accumulates interest — the longer you wait to address it, the more it costs.

## What is Technical Debt?

Coined by Ward Cunningham in 1992, technical debt describes the trade-off between:
- **Speed** — Getting something working quickly
- **Quality** — Building it the right way

Sometimes taking a shortcut is the right decision. The problem is when that shortcut becomes permanent.

## Types of Technical Debt

### Deliberate debt
"We know this isn't ideal, but we need to ship now."
- Choosing a simpler approach to meet a deadline
- Skipping tests to deliver faster
- Using a quick hack to prove a concept

### Accidental debt
"We didn't realize this would be so complex."
- Underestimating complexity
- Poor initial design that becomes problematic
- Lack of knowledge about best practices

### Bitrot
"The code was fine when we wrote it."
- Dependencies become outdated
- Requirements change
- Technology evolves
- Code that was once good becomes problematic

## The Technical Debt Quadrant

Martin Fowler's Technical Debt Quadrant categorizes debt by intention and reason:

|  | **Deliberate** | **Inadvertent** |
|--|---------------|----------------|
| **Reckless** | "We don't have time for design" | "What's layering?" |
| **Prudent** | "Ship now, refactor later" | "Now we know how we should have done it" |

## Signs of Technical Debt

### Code smells
- Duplicated code
- Long methods or classes
- Complex conditionals
- Poor naming
- Dead code

### Process indicators
- Slow build times
- Frequent bugs
- Difficulty adding features
- Fear of changing code
- Long onboarding for new developers

### Team indicators
- "We'll fix it later" mentality
- Avoiding certain parts of the codebase
- High turnover
- Low morale
- Decreasing velocity

## Managing Technical Debt

### 1. Make it visible
Track technical debt like any other work:
- Add it to the backlog
- Estimate it
- Prioritize it
- Track it over time

### 2. Pay it down incrementally
- Use the **Boy Scout Rule** — Leave code cleaner than you found it
- Allocate 10-20% of each sprint to debt reduction
- Refactor when you touch code

### 3. Prevent new debt
- Use [[Test-Driven Development]] to catch issues early
- Practice [[Pair Programming]] for real-time review
- Enforce [[Coding Standards]]
- Run [[Continuous Integration]]

### 4. Make trade-offs explicit
When taking on debt, document:
- What you're doing
- Why you're doing it
- When you plan to pay it off
- What the interest cost will be

## Technical Debt vs [[Refactoring]]

| Technical Debt | [[Refactoring]] |
|---------------|----------------|
| Shortcut that adds complexity | Improvement that reduces complexity |
| Increases future cost | Decreases future cost |
| Often unconscious | Always intentional |
| Should be paid off | Should be done continuously |

## Technical Debt and Agile Practices

- **[[Test-Driven Development]]** — Tests prevent debt from accumulating
- **[[Pair Programming]]** — Real-time review catches shortcuts
- **[[Refactoring]]** — Continuous improvement reduces debt
- **[[Continuous Integration]]** — Catches integration issues early
- **[[Sprint Planning]]** — Allocate time for debt reduction
- **[[Retrospectives]]** — Discuss and address debt regularly
