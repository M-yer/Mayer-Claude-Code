# Philosophy

Four ideas shape everything else.

1. **Claude should push back.** The global `CLAUDE.md` opens with behavior rules: state your interpretation, name tradeoffs, flag scope creep, say when the approach is wrong. I would rather be corrected than waste an hour.
2. **Small diffs.** "Surgical changes only" and "simplicity first" exist because the default failure mode is helpful over-building.
3. **Zero re-explaining.** Every session should start already knowing the project. That is what memory, the Obsidian brain and knowledge graphs are for. If I have to re-explain something, the notes were not good enough.
4. **Instructions belong in the layer that enforces them.** A preference goes in `CLAUDE.md` or memory. An *automatic behavior* ("whenever X happens, do Y") goes in a hook, because the harness runs hooks and Claude may forget instructions.

## Which layer for what

| I want… | Use |
|---|---|
| A rule Claude always follows | `CLAUDE.md` |
| A rule for one project only | that project's `CLAUDE.md` |
| A reusable playbook loaded on demand | Skill |
| A prompt I trigger by name | Slash command |
| Something to happen automatically | Hook |
| A fact/preference to survive sessions | Memory file |
| Long-form project knowledge | Obsidian brain / project notes |
| To avoid re-reading a codebase | Knowledge graph |
