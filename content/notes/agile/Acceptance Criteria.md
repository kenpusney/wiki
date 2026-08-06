
Acceptance criteria are the conditions that a user story must meet to be accepted by the Product Owner or stakeholder. They define the boundaries of a user story and provide the details needed for the development team to know when the story is complete.

## What are acceptance criteria?

Acceptance criteria (AC) are the "conditions of satisfaction" for a user story. They:

- Clarify what the team should build before they start work
- Ensure a common understanding of the problem or needs of the customer
- Help team members know when the story is complete
- Provide a basis for [[Definition of Done|acceptance testing]] and automated tests

## Acceptance criteria vs Definition of Done

| Aspect | Acceptance Criteria | [[Definition of Done]] |
|--------|-------------------|------------------------|
| **Scope** | Specific to individual user stories | Applies to ALL work items |
| **Content** | What the feature must do | Quality standards for all work |
| **When defined** | Per user story | Once, for the entire project |
| **Who defines** | Product Owner with team input | The whole Scrum team |

## How to write acceptance criteria

### The Given-When-Then format

This format, also known as the Gherkin syntax, is widely used because it's clear and testable:

```gherkin
Given [some context]
When [some action is taken]
Then [some outcome is expected]
```

**Example:**

> **As a** registered user, **I want to** log in with my email and password, **so that** I can access my account.

Acceptance Criteria:
- Given I am on the login page, when I enter a valid email and password, then I should be redirected to my dashboard
- Given I am on the login page, when I enter an invalid email, then I should see an error message "Please enter a valid email"
- Given I am on the login page, when I enter an incorrect password, then I should see an error message "Invalid credentials"
- Given I have entered my credentials incorrectly 5 times, when I try again, then my account should be temporarily locked

### The checklist format

A simpler approach that works well for less complex stories:

- [ ] User can search by keyword
- [ ] Search results are ranked by relevance
- [ ] No results found shows a helpful message
- [ ] Search works on mobile devices

## What acceptance criteria should include

- **Functional behavior** — What the system should do
- **Error scenarios** — What happens when things go wrong
- **Non-functional requirements** — Performance, security, accessibility
- **UX considerations** — Visual design and interaction requirements
- **Edge cases** — Boundary conditions and unusual scenarios

## What acceptance criteria should NOT include

- Code review was done
- Non-blocker or major issues
- Performance testing performed
- Acceptance and functional testing done

These items are already part of the [[Definition of Done]]. Including them in acceptance criteria creates redundancy.

## Examples by story type

### Login story
**As a** user, **I want to** log in with biometrics, **so that** I can access my account quickly.

AC:
- Given the device supports fingerprint, when I tap the fingerprint icon, then I can authenticate using my fingerprint
- Given the device supports Face ID, when I tap the Face ID icon, then I can authenticate using face recognition
- Given biometric authentication fails, when I see the error, then I can fall back to password login
- Given I'm not registered, when I try biometric login, then I'm prompted to create an account

### Search story
**As a** shopper, **I want to** filter search results by price, **so that** I can find products within my budget.

AC:
- Given I'm on the search results page, when I select a price range, then only products within that range are displayed
- Given I've applied a price filter, when I clear it, then all products are shown again
- Given no products match the filter, when I see the results, then I see a "No products found" message with suggestions
- Given I'm on mobile, when I tap the filter, then a modal opens with price range options

## Tips for effective acceptance criteria

1. **Keep them simple and clear** — Avoid technical jargon; write in business language
2. **Make them testable** — Each criterion should be verifiable as pass or fail
3. **Focus on the "what," not the "how"** — Describe the desired behavior, not the implementation
4. **Collaborate** — Write AC together with the Product Owner, developers, and testers
5. **Review before sprint planning** — Ensure AC are clear before the team commits to the story
