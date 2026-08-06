
The [[Definition of Done]] is a shared understanding among the Scrum Team of what it means for work to be complete. It is used to assess when work is done on the product increment.

## What is the Definition of Done?

The Definition of Done (DoD) is a formal description of the state of the [[Sprint Backlog|increment]] when it meets the quality standards required of the product. When a Product Backlog item or an increment is described as "Done," everyone must understand what "Done" means.

A DoD creates transparency by providing a shared understanding of what work must be completed before an increment can be released.

## Why does the Definition of Done matter?

1. **Creates shared understanding** — Everyone on the team (and stakeholders) knows exactly what "complete" means
2. **Enables quality** — Work that doesn't meet the DoD isn't considered done, preventing technical debt from accumulating
3. **Supports estimation** — When the team knows what "done" includes, they can estimate more accurately with [[User Story Points|story points]]
4. **Prevents scope creep** — Clear boundaries prevent the definition of "done" from expanding mid-sprint
5. **Enables transparency** — Stakeholders know exactly what they're getting when work is marked complete

## What should a Definition of Done include?

A DoD typically covers multiple dimensions of quality. Here's an example:

### Code quality
- [ ] Code reviewed by at least one other developer
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] No critical or high-severity bugs remain

### Testing
- [ ] Acceptance criteria verified
- [ ] Cross-browser testing completed
- [ ] Mobile responsiveness checked
- [ ] Performance benchmarks met

### Documentation
- [ ] API documentation updated
- [ ] User-facing documentation updated (if applicable)
- [ ] Internal technical notes added

### Deployment
- [ ] Feature deployed to staging environment
- [ ] Smoke tests pass in staging
- [ ] Ready for release to production

## Definition of Done vs Acceptance Criteria

| Aspect | Definition of Done | [[Acceptance Criteria]] |
|--------|-------------------|------------------------|
| **Scope** | Applies to ALL work items | Specific to individual user stories |
| **Purpose** | Ensures consistent quality standards | Defines what the specific feature must do |
| **When defined** | Once, for the entire project | Per user story |
| **Who defines** | The whole Scrum team | Product Owner with team input |

## How to create a Definition of Done

1. **Gather the whole team** — The DoD is a team commitment, not a top-down mandate
2. **Start with a basic template** — Use a standard DoD as a starting point
3. **Add team-specific items** — Customize based on your project's quality needs
4. **Make it realistic** — An unachievable DoD will be ignored
5. **Review and evolve** — As the team matures, the DoD should become more rigorous

## Definition of Ready

The [[Definition of Ready]] (DoR) is the complement to the Definition of Done. While the DoD describes when work is *complete*, the DoR describes when a backlog item is *ready to be worked on*.

A DoR might include:
- User story follows the standard format ([[User Stories|As a... I want... So that...]])
- Acceptance criteria are defined
- Dependencies identified
- Story is estimated with [[User Story Points|story points]]
- UX designs are available (if applicable)
