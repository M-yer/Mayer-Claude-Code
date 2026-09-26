# Skills and slash commands

## Skill layout

```
~/.claude/skills/
  my-skill/
    SKILL.md            required
    references/*.md     optional: long material loaded only when needed
    scripts/*           optional: helpers the skill calls
```

`SKILL.md` = YAML frontmatter + markdown body.

```markdown
---
name: my-skill
description: Use when <situation>. Not for <non-situation>.
version: 1.0.0
---

# Title
Body: the playbook Claude follows once the skill loads.
```

Template: [`templates/skills/my-skill/SKILL.md`](../templates/skills/my-skill/SKILL.md).

### The `description` is the whole trigger

Claude sees only `name` + `description` in its skill list and decides from that whether to load the body. So write it as *when to use*, not *what it is*:

- Good: "Use when designing or auditing any website when the goal is to look intentionally designed rather than templated."
- Weak: "A design skill."

Include the phrases you would actually say ("caveman mode", "less tokens", "match my taste") and say what it is **not** for.

### How my skills are grouped

| Group | Examples | Notes |
|---|---|---|
| Design taste | `mayer-taste`, `taste-skill`, `brutalist-skill`, `minimalist-skill`, `soft-skill`, `redesign-skill`, `frontend-design` | Different aesthetic playbooks; `mayer-taste` is my own philosophy skill |
| Communication | `caveman`, `caveman-commit`, `caveman-review`, `caveman-compress` | Token-cutting output modes |
| Knowledge | `graphify`, `brain`, `ingest`, `obsidian-*` | Build/query graphs and the vault |
| Workflow | `grill-me`, `write-a-prd`, `prd-to-issues`, `tdd` | Process prompts |
| Plugins | `superpowers:*`, `ecc:*`, `vercel:*`, `claude-seo:*`, `marketing-skills:*` | Installed via plugins, not hand-written |

## Writing a good custom skill (what `mayer-taste` does)

See [`examples/skills/mayer-taste.SKILL.md`](../examples/skills/mayer-taste.SKILL.md).

1. State the **core law** first (one sentence the rest serves).
2. Force **named decisions before work** (it makes Claude name a register, a scene, and a signature move before designing).
3. Give **transferable principles**, not locked values (no hex codes, so it works on any project).
4. End with a **checklist/audit** the skill can run against finished work.
5. Keep it under ~100 lines. Push detail into `references/`.

## Slash commands

A command is a single markdown file: `~/.claude/commands/<name>.md`, invoked as `/name`. Same frontmatter idea, body is the prompt. Good for prompts you paste often.

Example: [`examples/skills/grill-me.command.md`](../examples/skills/grill-me.command.md), where the whole command is "interview me one question at a time until we agree". Template: [`templates/commands/example.md`](../templates/commands/example.md).

Skills vs commands: skills are discovered and auto-loaded by description; commands only run when you type them.

## Managing the pile

- Overlap is real (I have several design-taste skills). Prefer fewer, sharper skills.
- Turn skills off without deleting: `"skillOverrides": {"name": "off"}` in `settings.json`.
- `skills/synced/` and `skills/learned/` are managed by Claude itself. Do not hand-edit.
