---
name: learning-cycle
description: Process new content from 00.inbox/ through the Discover → Explore → Organize → Learn → Produce loop. Use when the user adds content to 00.inbox/ and requests organization, classification, routing, or downstream planning.
---

# Learning Cycle

User-driven closed loop for new content. Analyze and recommend; execute only after user confirmation.

## Trigger

- New files exist in `00.inbox/`
- User invokes this skill or requests inbox processing

## Approach

1. Read every file in `00.inbox/`.
2. For each file, run the five phases and produce a recommendation object.
3. Present the consolidated recommendation.
4. Execute only after the user confirms each action.

## Phases

### Discover
- Identify type: article / note / collection / project / publication / plan / draft / other
- Identify topic, scope, audience, and maturity
- Flag whether it is ready-to-publish or in-progress

### Explore
- Map connections to existing `content/` structure
- Identify duplicate or related content
- Identify knowledge gaps or opportunities

### Organize
- Propose target directory and filename
- Propose Wikilink updates to index pages
- Propose any new index pages needed

### Learn
- Design note structure if applicable
- Identify extraction points (key concepts, quotes, references)
- Propose templates or recurring patterns

### Produce
- Propose downstream artifacts
- Map to potential articles, projects, or publications
- Suggest timing and dependencies

## Output Format

For each inbox item:

**File**: `<filename>`

**Discover**
- Type: ...
- Topic: ...
- Maturity: ...

**Explore**
- Connections: ...
- Gaps: ...

**Organize**
- Target: ...
- Rename: ...
- Index updates: ...

**Learn**
- Structure: ...
- Templates: ...

**Produce**
- Artifacts: ...
- Roadmap: ...

**Questions for you**
- ...

## References

- `references/project-structure.md` — Standard project scaffold for learning projects
- `references/routing.md` — Inbox item routing table

## Rules

- Do not move, rename, or edit any file without explicit user confirmation.
- Do not modify build config outside `content/`.
- Preserve Obsidian compatibility.
- Keep recommendations specific to this repo's structure.
