
Pair programming is a core [[Extreme Programming|XP]] practice where two developers work together at one workstation. The **driver** writes code while the **navigator** reviews each line of code as it is typed. The roles switch frequently, typically every 15-30 minutes.

## How it works

### Roles

- **Driver**: Writes the code. Focuses on the implementation details and syntax.
- **Navigator**: Reviews the code as it's written. Thinks about the bigger picture, potential issues, and alternative approaches.

### The flow

1. The driver starts coding the current task
2. The navigator reviews each line, catches errors, suggests improvements
3. They discuss approaches and trade-offs in real-time
4. They switch roles regularly (every 15-30 minutes)
5. Both commit to the code they produce together

## Benefits

### Code quality
- **Real-time code review** catches bugs immediately
- **Two perspectives** on every design decision
- **Reduced defects** through continuous review
- **Better variable names** and clearer code

### Knowledge sharing
- **Eliminates knowledge silos** — everyone knows the codebase
- **Cross-training** happens naturally
- **Bus factor** increases — no single point of failure
- **Faster onboarding** for new team members

### Design quality
- **Better design decisions** through discussion
- **Simpler code** — two people naturally resist over-engineering
- **Continuous refactoring** encouraged by having a safety net

### Focus and productivity
- **Stay on task** — harder to procrastinate with a partner
- **Faster problem-solving** — two minds are better than one
- **Reduced interruptions** — pair programming eliminates many context switches

## Types of pair programming

### Driver-Navigator
The most common style:
- One person drives (types), the other navigates (reviews)
- Switch roles at regular intervals
- Good for most situations

### Ping-Pong Pairing
Great for TDD:
1. Person A writes a failing test
2. Person B writes the code to make it pass
3. Person B writes the next failing test
4. Person A writes the code to make it pass
5. Repeat

### Strong-Style Pairing
"For an idea to go from your head into the computer, it MUST go through the other person's hands."
- The navigator dictates, the driver types
- Forces more thinking before coding
- Good for complex problems

### Remote Pair Programming
With modern tools, pair programming works remotely:
- Screen sharing (VS Code Live Share, Tuple, Zoom)
- Shared IDE environments
- Communication via video call
- Asynchronous pairing for different time zones

## Common concerns

### "It's too expensive — two people doing one person's job"

Research shows pair programming:
- **Reduces bugs by 15-60%** (various studies)
- **Reduces debugging time** significantly
- **Improves design quality**, reducing future rework
- **Knowledge sharing** reduces onboarding costs
- **Overall cost is often lower** than solo programming with code reviews

### "I need alone time to focus"

- Pairing is intense — schedule regular breaks
- Mix pairing with solo work (e.g., pair in the morning, solo in the afternoon)
- Not everything needs pairing — research, simple tasks, etc.
- Pair on complex or high-risk code; work solo on straightforward tasks

### "My partner is too slow/fast"

- Discuss pace openly
- Switch pairs regularly to learn different styles
- Use pairing as a learning opportunity
- The navigator should be actively engaged, not just watching

## Best practices

1. **Switch roles frequently** — every 15-30 minutes
2. **Take breaks** — pair programming is mentally exhausting
3. **Use version control** — commit frequently so progress isn't lost
4. **Keep pairs fresh** — rotate pairs to share knowledge
5. **Pair on hard stuff** — complex algorithms, new technologies, critical bugs
6. **Don't pair all day** — mix with solo work for balance
7. **Communicate actively** — talk through your thinking
8. **Be patient** — it takes time to get good at pairing

## When to pair

**Great for:**
- Complex or unfamiliar code
- Critical bugs or features
- Onboarding new team members
- Learning new technologies
- Design decisions
- High-risk changes

**Less necessary for:**
- Simple, well-understood tasks
- Research and exploration
- Writing documentation
- Administrative tasks
- Tasks requiring deep, uninterrupted focus

## Pair programming tools

- **VS Code Live Share** — Real-time collaborative editing
- **Tuple** — Purpose-built for pair programming
- **JetBrains Code With Me** — IntelliJ-based pairing
- **CodeSandbox** — Browser-based collaborative coding
- **Screen sharing** — Zoom, Teams, Slack Huddle
