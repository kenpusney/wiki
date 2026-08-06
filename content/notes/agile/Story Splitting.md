
Large user stories that are too big for a single sprint need to be split into smaller, more manageable pieces. Story splitting is a critical skill for agile teams.

## When to Split Stories

- **Too large for a sprint** — Won't fit in the iteration
- **Too complex to estimate** — Too many unknowns
- **Too risky** — Too many dependencies or unknowns
- **Multiple user personas** — Serves different user types differently
- **Multiple workflows** — Contains several distinct paths

## Splitting Techniques

### By Workflow Steps
Split a story along the natural workflow:

**Original**: "As a user, I want to book a hotel room"

Split into:
- Search for hotels by location and dates
- View hotel details and photos
- Select room type and options
- Enter guest information
- Process payment
- Receive confirmation

### By CRUD Operations
Split Create, Read, Update, Delete:

**Original**: "As an admin, I want to manage user accounts"

Split into:
- Create new user accounts
- View user account details
- Update user account information
- Deactivate user accounts

### By Business Rules
Split along different business rules:

**Original**: "As a shopper, I want to apply discount codes"

Split into:
- Apply percentage discount codes
- Apply fixed amount discount codes
- Apply free shipping codes
- Apply buy-one-get-one codes

### By Data Type or Platform
Split by different data or platforms:

**Original**: "As a user, I want to export reports"

Split into:
- Export reports as PDF
- Export reports as CSV
- Export reports as Excel
- Export reports as JSON

### By Operations (Simple/Complex)
Split the simple path from complex:

**Original**: "As a user, I want to reset my password"

Split into:
- Reset password via email (simple)
- Reset password via SMS (additional)
- Reset password via security questions (additional)
- Account recovery for locked accounts (complex)

### By Interface
Split by different user interfaces:

**Original**: "As a user, I want to view my order history"

Split into:
- View order history on web
- View order history on mobile app
- View order history via email
- View order history via API

### By Test Cases
Split based on test scenarios:

**Original**: "As a user, I want to search for products"

Split into:
- Search returns exact matches
- Search returns partial matches
- Search handles no results
- Search handles special characters
- Search handles long queries

## INVEST Criteria

Good user stories follow the **INVEST** criteria:

| Letter | Meaning | Description |
|--------|---------|-------------|
| **I** | Independent | Story doesn't depend on other stories |
| **N** | Negotiable | Story is a placeholder for conversation |
| **V** | Valuable | Story delivers value to the customer |
| **E** | Estimable | Team can estimate the effort |
| **S** | Small | Story fits in a single sprint |
| **T** | Testable | Story has clear acceptance criteria |

If a story violates INVEST, it probably needs splitting.

## Splitting Anti-Patterns

### ❌ Splitting by technical layer
- "Frontend story" / "Backend story" / "Database story"
- These don't deliver value independently
- Split by user value instead

### ❌ Splitting by tasks
- "Write code" / "Write tests" / "Write documentation"
- Tasks aren't deliverable increments
- Split by user-facing functionality

### ❌ Splitting too thin
- Stories that are too small waste time on overhead
- Aim for stories that take 1-3 days
- Don't split just to split

### ❌ Splitting by sub-tasks
- "Create database table" / "Create API endpoint" / "Create UI"
- These are tasks, not stories
- Each split should deliver user value

## Story Splitting and Agile Practices

- **[[User Stories]]** — Splitting is essential for effective user stories
- **[[Sprint Planning]]** — Smaller stories are easier to plan
- **[[User Story Points|Story Points]]** — Smaller stories are easier to estimate
- **[[Backlog Refinement]]** — Splitting happens during refinement
- **[[User Story Mapping]]** — Maps help identify natural splitting points
- **[[Sprint Backlog]]** — Small stories fit better in sprints
