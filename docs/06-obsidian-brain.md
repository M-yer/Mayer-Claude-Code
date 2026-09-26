# Obsidian second brain

An Obsidian vault Claude reads at session start and writes to as it works.

## Wiring

1. Install the **Local REST API** plugin in Obsidian (default `http://127.0.0.1:27123`).
2. Add the `mcp-obsidian` server to `.mcp.json` with the API key in an env var (see [04](04-settings-plugins-mcp.md)).
3. In `CLAUDE.md`, gate the behaviour: "only when `mcp__obsidian__*` tools are confirmed available." This stops Claude trying and failing when Obsidian is closed.

## Vault structure

```
My Brain/
  inbox/            quick captures, mid-session ideas and blockers (timestamped)
  Discoveries/      new tools / better approaches worth keeping
  knowledge/
    coding/         patterns, decisions, lessons
    projects/<n>/   per-project context: stack, decisions, status
  projects/sessions/<n>/YYYY-MM-DD    change log per session
  docs/             references and templates
  graphify/<n>/     canvas mirrors of knowledge graphs (view only)
```

Template rules block: [`templates/brain/brain-rules.md`](../templates/brain/brain-rules.md)

## The loop

- **Session start:** read `knowledge/projects/<name>` and the latest `projects/sessions/<name>/` before asking questions.
- **During:** update the project note when something meaningful is decided (stack, architecture, a solved problem). Do not wait for the end.
- **After a task:** append a dated entry of *what changed and why*. No transcripts.
- **Never overwrite** existing notes. Append or add a dated file.
- **Do not log** typo fixes or routine edits.

Note conventions (from the vault's own `CLAUDE.md`): prose-as-title (`async-await-beats-callbacks.md`), wiki-links inside sentences, frontmatter with `source`, `date`, `type`, `status`, and a duplicate check on `source:` before ingesting anything.

Success test: the next session needs zero re-explaining.
