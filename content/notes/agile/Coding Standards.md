
Coding standards are agreed-upon rules for how the team writes code. They ensure consistency, readability, and maintainability across the entire codebase.

## Why Coding Standards Matter

### Readability
- Code is read far more often than it's written
- Consistent style reduces cognitive load
- Developers can focus on logic, not formatting

### Collaboration
- Everyone can read everyone's code
- No "style wars" or debates
- Easier [[Pair Programming]]
- Easier [[Collective Code Ownership]]

### Quality
- Consistent patterns are easier to review
- Automated tools can enforce standards
- Reduced likelihood of style-related bugs

### Onboarding
- New developers learn one style
- Less time spent on style debates
- Faster integration into the team

## What Coding Standards Should Cover

### Formatting
- Indentation (spaces vs tabs, how many)
- Line length limits
- Blank line usage
- Brace style
- Trailing commas

### Naming
- Variables: `camelCase` or `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Functions: descriptive verbs
- Files: consistent naming convention

### Comments
- When to comment (and when not to)
- Documentation style (JSDoc, docstrings, etc.)
- TODO format
- Comment language (English is standard)

### Code Structure
- File organization
- Import ordering
- Class/method length limits
- Function complexity limits

### Error Handling
- Consistent error patterns
- Logging standards
- Exception types
- Error messages

## Establishing Standards

### 1. Discuss as a team
Don't impose standards — agree on them:
- What do we value most?
- What tools can enforce standards automatically?
- What are our pain points with current code?

### 2. Start with existing code
- Use the existing codebase as a starting point
- Don't rewrite everything at once
- Gradually improve over time

### 3. Automate enforcement
Use tools to enforce standards automatically:
- **Linters** — ESLint, Pylint, RuboCop
- **Formatters** — Prettier, Black, gofmt
- **Pre-commit hooks** — Prevent non-compliant code
- **CI checks** — Fail builds on style violations

### 4. Document the standards
Create a style guide that covers:
- All formatting rules
- Naming conventions
- Examples of good and bad code
- Links to tool configurations

### 5. Review and evolve
Standards should evolve with the team:
- Revisit periodically
- Add new rules as needed
- Remove rules that don't help
- Keep the guide concise

## Common Coding Standard Tools

### JavaScript/TypeScript
- **ESLint** — Linting
- **Prettier** — Formatting
- **Husky** — Git hooks
- **lint-staged** — Pre-commit checks

### Python
- **Flake8** — Linting
- **Black** — Formatting
- **isort** — Import sorting
- **mypy** — Type checking

### Java/Kotlin
- **Checkstyle** — Linting
- **Spotless** — Formatting
- **ktlint** — Kotlin formatting

### Go
- **gofmt** — Formatting (built-in)
- **golangci-lint** — Linting

### Rust
- **rustfmt** — Formatting (built-in)
- **clippy** — Linting (built-in)

## Coding Standards and XP Practices

- **[[Pair Programming]]** — Standards make pairing smoother
- **[[Collective Code Ownership]]** — Everyone can read everyone's code
- **[[Refactoring]]** — Standards make refactoring safer
- **[[Continuous Integration]]** — Standards enable automated checks
- **[[Test-Driven Development]]** — Standards apply to test code too
