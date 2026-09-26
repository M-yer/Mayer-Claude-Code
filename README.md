# Mayer-Claude-Code

How my [Claude Code](https://claude.com/claude-code) environment is set up, written so you can copy it and adapt it to your own workflow.

Nothing here is a product. It is a documented setup: one global `CLAUDE.md`, a handful of skills, one hook, file-based memory, an Obsidian "second brain", and per-project knowledge graphs.

## The layers

| Layer | Lives in | What it does | Doc |
|---|---|---|---|
| Instructions | `~/.claude/CLAUDE.md` + per-project `CLAUDE.md` | Rules Claude follows every session | [docs/01-claude-md.md](docs/01-claude-md.md) |
| Skills | `~/.claude/skills/<name>/SKILL.md` | Loadable playbooks (design taste, compression, graph queries) | [docs/02-skills.md](docs/02-skills.md) |
| Slash commands | `~/.claude/commands/*.md` | One-file prompts you trigger with `/name` | [docs/02-skills.md](docs/02-skills.md) |
| Hooks | `~/.claude/settings.json` → `hooks` | Scripts the harness runs (not Claude), e.g. inject context on keyword | [docs/03-hooks.md](docs/03-hooks.md) |
| Settings, plugins, MCP | `settings.json`, `.mcp.json` | Model, permissions, plugin list, tool servers | [docs/04-settings-plugins-mcp.md](docs/04-settings-plugins-mcp.md) |
| Memory | `~/.claude/projects/<proj>/memory/` | Small typed notes that persist across sessions | [docs/05-memory.md](docs/05-memory.md) |
| Second brain | Obsidian vault + REST API MCP | Project notes and session logs Claude reads at start | [docs/06-obsidian-brain.md](docs/06-obsidian-brain.md) |
| Knowledge graphs | `<project>/graphify-out/graph.json` | Query a project instead of reading its files (saves tokens) | [docs/07-graphify.md](docs/07-graphify.md) |

## Quick start

```bash
git clone https://github.com/<you>/Mayer-Claude-Code && cd Mayer-Claude-Code
# 1. Global instructions: copy, then edit every [BRACKET]
cp templates/CLAUDE.md ~/.claude/CLAUDE.md
# 2. Skills / commands / hooks: copy what you want
cp -r templates/skills/my-skill ~/.claude/skills/
cp templates/commands/example.md ~/.claude/commands/
cp templates/hooks/keyword-context.py ~/.claude/hooks/
# 3. Settings: merge by hand into your existing file, do not overwrite
#    templates/settings.example.json  ->  ~/.claude/settings.json
```

Read [docs/00-philosophy.md](docs/00-philosophy.md) first if you want to know *why* it is shaped this way.

## Secrets

Real config files contain tokens (MCP `Authorization` headers, Obsidian API keys). Everything in this repo is redacted. Keep yours that way: put secrets in env vars or a git-ignored file, never in a file you might publish.

## Layout

```
docs/        explanations, numbered in reading order
templates/   copy-and-edit starting points (generic, no personal data)
examples/    real files from my setup, lightly sanitized, for reference
```
