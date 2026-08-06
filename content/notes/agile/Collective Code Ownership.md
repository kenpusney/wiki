
Collective code ownership is an [[Extreme Programming|XP]] practice where **any team member can change any code** in the system. No one "owns" a module, file, or component. The entire team owns the entire codebase.

## Why Collective Ownership?

### Eliminates knowledge silos
- No single point of failure when someone leaves
- Everyone understands the whole system
- Knowledge is shared naturally through pair programming

### Enables faster response
- Whoever finds a bug can fix it
- No waiting for "the expert" to become available
- Faster on-call response

### Improves code quality
- Multiple perspectives on every piece of code
- No "sacred" code that's never touched
- Continuous improvement from diverse viewpoints

### Increases team resilience
- Team members can help each other
- Work can be redistributed easily
- Reduced bottlenecks

## How to Implement Collective Ownership

### 1. Shared coding standards
The team agrees on and follows common coding conventions:
- Formatting rules
- Naming conventions
- Design patterns
- Architecture guidelines

### 2. Comprehensive test suite
Tests give confidence to change code:
- Write tests with [[Test-Driven Development]]
- High test coverage for critical paths
- [[Continuous Integration]] runs tests on every commit

### 3. [[Pair Programming]]
Pairing spreads knowledge naturally:
- Rotate pairs regularly
- Pair across different areas of the codebase
- Use pairing to mentor junior developers

### 4. Code reviews
Review changes before they're merged:
- Everyone reviews everyone's code
- Focus on knowledge sharing, not gatekeeping
- Use automated tools to catch simple issues

### 5. Small, frequent commits
Small changes are easier to understand and review:
- Commit at least daily
- Keep commits focused on one thing
- Write clear commit messages

## Common Concerns

### "But nobody knows my module as well as I do"
- That's a problem, not a feature
- Share your knowledge through pairing and documentation
- The goal is for everyone to know every module

### "People will break my code"
- That's what tests are for
- If tests catch it, the system works as designed
- If tests don't catch it, write better tests

### "It's inefficient — people will make mistakes"
- Short-term: yes, some mistakes
- Long-term: much faster because knowledge is shared
- The cost of knowledge silos is much higher

## Collective Ownership vs Code Ownership

| Aspect | Code Ownership | Collective Ownership |
|--------|---------------|---------------------|
| **Who can change code** | Only the "owner" | Anyone |
| **Knowledge** | Concentrated | Distributed |
| **Bus factor** | Low (1 person) | High (whole team) |
| **Flexibility** | Low | High |
| **Code quality** | Varies by owner | Consistent |

## Collective Ownership and XP Practices

- **[[Pair Programming]]** — Spreads knowledge through pairing
- **[[Test-Driven Development]]** — Tests provide safety to change code
- **[[Continuous Integration]]** — Frequent integration prevents divergence
- **[[Coding Standards]]** — Common conventions make code consistent
- **[[Refactoring]]** — Anyone can improve any code
