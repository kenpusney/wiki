
Extreme Programming (XP) is an agile software development framework that aims to produce higher quality software and higher quality of life for the development team. XP is the most specific of the agile frameworks regarding appropriate engineering practices for software development.

## XP Values

XP defines five values that guide all its practices:

### 1. Communication
Problems are typically caused by lack of communication or misunderstanding. XP emphasizes:
- Face-to-face conversations over documents
- Pair programming as a knowledge-sharing tool
- Shared code ownership
- On-site customer availability

### 2. Simplicity
"Do the simplest thing that could possibly work" — XP's golden rule:
- Write code for today's needs, not tomorrow's speculations
- Avoid over-engineering
- Small, incremental changes
- Refactor constantly to keep design simple

### 3. Feedback
Fast feedback loops at every level:
- Unit tests give immediate feedback on code quality
- Continuous integration tells you if changes broke something
- Pair programming provides real-time code review
- Short iterations deliver working software frequently
- Customer demos ensure the team builds the right thing

### 4. Courage
XP requires the courage to:
- Refactor code without fear (protected by tests)
- Say "no" to unmanageable scope
- Accept and act on feedback
- Throw away code that doesn't work
- Try new approaches and learn from failures

### 5. Respect
Every team member's contribution matters:
- Everyone contributes code
- No blame culture
- Support team members who are struggling
- Value different perspectives and skills
- Commit to the team's success

## The Four XP Activities

XP defines four basic activities that occur throughout development:

### Coding
The heart of software development. Without working code, nothing else matters. XP emphasizes:
- Write code every day
- Code should be visible to everyone (shared repository)
- Refactor continuously to maintain quality

### Listening
Understanding what the customer really needs:
- Listen to the customer's stories
- Understand the business domain
- Pair with the customer on stories

### Designing
Making the system work simply and elegantly:
- Use the simplest design that works
- Refactor to remove duplication
- Use patterns where appropriate
- Keep the system's architecture flexible

### Testing
Ensuring the code works and keeps working:
- Write tests before code (TDD)
- Test continuously
- Test at all levels (unit, integration, system)
- Automate everything possible

## XP Core Practices

XP defines 12 core practices (later expanded to more):

### Programming Practices

#### [[Pair Programming]]
Two programmers work together at one workstation. The **driver** writes code while the **navigator** reviews each line of code as it's typed. They switch roles frequently.

**Benefits:**
- Real-time code review catches bugs immediately
- Knowledge sharing across the team
- Better design through collaborative thinking
- Increased bus factor
- Higher code quality

#### [[Test-Driven Development]]
Write tests *before* writing the production code. The cycle is: **Red → Green → Refactor**.

1. **Red**: Write a failing test that defines desired behavior
2. **Green**: Write the minimum code to make the test pass
3. **Refactor**: Clean up the code while keeping tests green

**Benefits:**
- Forces you to think about the design before coding
- Creates a comprehensive test suite automatically
- Enables fearless refactoring
- Documents the code's intended behavior

#### [[Collective Code Ownership]]
Anyone can change any code in the system. No one "owns" a module or component.

**Why it matters:**
- Eliminates knowledge silos
- Enables faster bug fixes (whoever finds it can fix it)
- Promotes better code design (no need to understand one person's style)
- Increases team resilience

#### [[Simple Design]]
Always run with the simplest design that works. XP uses four rules of Simple Design (in priority order):

1. **Passes the tests** — All tests pass
2. **Reveals intention** — Code clearly expresses what it does
3. **No duplication** — Each piece of knowledge appears once
4. **Fewest classes/methods** — Minimum elements needed

#### [[Refactoring]]
Improving the internal structure of code without changing its external behavior. Refactoring is made safe by having a comprehensive test suite.

**Common refactoring techniques:**
- Extract Method/Function
- Rename Variable/Method
- Move Method/Field
- Replace Temp with Query
- Introduce Parameter Object

#### [[Coding Standards]]
The team agrees on and follows common coding conventions:
- Naming conventions
- Code formatting
- Comment standards
- Error handling patterns
- File organization

### Planning Practices

#### [[Planning Game]]
A collaborative planning session involving developers and customers:

- **User Stories** define requirements from the customer's perspective
- **Story Points** estimate relative effort
- **Iterations** are short (1-2 weeks)
- **Velocity** guides how much work to take on

#### [[Small Releases]]
Deliver working software frequently in small increments:
- Release the simplest version first
- Get feedback early
- Build on what you learn
- Reduce risk through frequent delivery

#### [[Whole Team]]
Everyone involved in the project works together in the same space:
- Customer on-site (or highly available)
- Developers, testers, designers all together
- Shared responsibility for success
- No "us vs. them" mentality

### Engineering Practices

#### Continuous Integration
Integrate and test code changes multiple times per day:
- Commit to the mainline at least daily
- Automated build and test on every commit
- Fix broken builds immediately (within 10 minutes)
- Never go home with a broken build

#### Sustainable Pace
The team should be able to maintain their pace indefinitely:
- No overtime (or very rare and voluntary)
- 40-hour work weeks (approximately)
- Rest and recharge
- Long-term productivity over short-term heroics

#### [[System Metaphor]]
A simple shared story that explains how the system works:
- Guides design decisions
- Helps new team members understand the system
- Provides a common vocabulary
- Example: "The system is like a library where books (data) are organized by topic and can be checked out (accessed) by patrons (users)"

#### Coding Standards
A shared set of rules for how code should be written:
- Consistent formatting
- Naming conventions
- Comment guidelines
- Error handling patterns
- The whole team follows these standards

## XP vs Scrum

| Aspect | XP | Scrum |
|--------|-----|-------|
| **Focus** | Engineering practices | Project management |
| **Iterations** | 1-2 weeks (shorter preferred) | 2-4 weeks |
| **Practices** | Prescriptive engineering practices | Framework, team chooses practices |
| **Planning** | Story points, velocity | Story points, velocity |
| **Roles** | No specific roles (whole team) | PO, SM, Dev Team |
| **Technical practices** | TDD, pair programming, CI required | Not prescribed |

Many teams combine Scrum (for project management) with XP (for engineering practices) — this is sometimes called **Scrum/XP**.

## Benefits of XP

1. **Higher code quality** — Through pair programming, TDD, and continuous refactoring
2. **Faster feedback** — Short iterations and continuous integration
3. **Reduced risk** — Small releases and frequent integration
4. **Better knowledge sharing** — Collective code ownership and pair programming
5. **Customer satisfaction** — Frequent delivery of working software
6. **Sustainable development** — No burnout, consistent pace
7. **Adaptability** — Simple design and refactoring enable change

## When to use XP

XP works best when:
- Requirements change frequently
- The team is co-located (or has excellent remote collaboration tools)
- The customer can be highly available
- The team is committed to engineering excellence
- The project is complex and risky

XP may be challenging when:
- The team is distributed and can't pair program easily
- The customer cannot be involved
- The organization doesn't support the required cultural changes
- Legacy code makes TDD difficult (though it can be adopted incrementally)


## YAGNI: You Aren't Gonna Need It

A related XP principle: don't build something until you actually need it. See [[YAGNI]].
