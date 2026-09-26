# Memory

File-based, one fact per file, plus an index. Lives at `~/.claude/projects/<project-path-slug>/memory/`.

```
memory/
  MEMORY.md                      index, loaded every session: one line per memory
  feedback_git_identity.md
  project_myapp_state.md
  reference_credentials_location.md
```

## Memory file

```markdown
---
name: feedback-git-identity
description: One line used to decide relevance later
metadata:
  type: feedback        # user | feedback | project | reference
---

The fact. For feedback/project, add:
**Why:** the reason or incident behind it.
**How to apply:** when this kicks in.
```

Templates: [`templates/memory/`](../templates/memory/)

## The four types

| Type | Holds | Example |
|---|---|---|
| `user` | Who you are, expertise, preferences | "Designs UI-first, backend second" |
| `feedback` | Corrections **and** confirmed approaches, with the why | "Never add a Co-Authored-By line to commits" |
| `project` | Ongoing goals/constraints not visible in code | "Feature freeze until 3 Oct; deploy via git push" |
| `reference` | Where to find things outside the repo | "Vault path", "credentials live in a git-ignored env file" |

## `MEMORY.md` index

One line per memory, no frontmatter, no content:

```markdown
- [Git Identity](feedback_git_identity.md): always commit as <name>/<email>
```

It is loaded into context every session, so keep it short. Detail goes in the topic files.

## Rules I follow

- Update an existing memory rather than adding a duplicate.
- Do not store what the repo already records (structure, git history, `CLAUDE.md`).
- Convert relative dates ("Thursday") to absolute.
- Delete memories that turn out wrong.
- Never store secrets; store *where* they live.
- Link related memories with `[[name]]`.

## Memory vs `CLAUDE.md`

`CLAUDE.md` = standing rules you wrote. Memory = things Claude learned along the way, often from your corrections. If a memory proves to be a permanent rule, promote it to `CLAUDE.md`.
