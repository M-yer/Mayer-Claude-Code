# Settings, plugins, MCP

Full redacted file: [`templates/settings.example.json`](../templates/settings.example.json)

## Files

| File | Scope | Commit? |
|---|---|---|
| `~/.claude/settings.json` | you, all projects | no |
| `~/.claude/settings.local.json` | you, machine-specific: permissions, env | no |
| `<project>/.claude/settings.json` | project, shared | yes |
| `~/.claude/.mcp.json` or project `.mcp.json` | MCP servers | **never with tokens** |

## Notable keys in mine

| Key | Value | Why |
|---|---|---|
| `model` | `sonnet` | Default model; switch per task |
| `effortLevel` | `high` | More reasoning by default |
| `autoCompactEnabled` | `true` | Long sessions summarise instead of failing |
| `autoContinueAtUsageLimit` | `true` | Resume after a limit resets |
| `enabledPlugins` | map | The plugin list, toggled per plugin |
| `extraKnownMarketplaces` | map | GitHub repos plugins are pulled from |
| `skillOverrides` | map | Turn individual skills off |
| `hooks` | map | See [03-hooks.md](03-hooks.md) |

`settings.local.json` holds `permissions.allow` (pre-approved commands such as `Bash(gh repo *)`) and `env`. Approve only what you trust.

## Plugins I run

Superpowers (process skills), Everything Claude Code (agents/commands), Vercel, marketing-skills, claude-seo, claude-mem, Ruflo (swarm/coordination), Codex (second-opinion runner). Add a marketplace under `extraKnownMarketplaces`, then enable the plugin under `enabledPlugins`.

Fewer plugins is better: each adds skills to the list Claude must scan, and overlapping ones (I have three code-review skills) blur triggers.

## MCP servers

Connected: Supabase, Obsidian (REST API), HeroUI docs, Playwright, plus hosted connectors (Vercel, Gmail, Meta Ads, PostHog…).

Two config shapes:

```json
// remote HTTP server
"supabase": { "type": "http", "url": "https://mcp.supabase.com/mcp",
              "headers": { "Authorization": "Bearer ${SUPABASE_TOKEN}" } }

// local stdio server
"obsidian": { "type": "stdio", "command": "npx", "args": ["-y", "mcp-obsidian"],
              "env": { "OBSIDIAN_API_KEY": "${OBSIDIAN_API_KEY}", "OBSIDIAN_HOST": "http://127.0.0.1:27123" } }
```

Prefer `${ENV_VAR}` expansion over pasting tokens into the file.

Note: my own config has tokens written literally into `settings.json` and `.mcp.json`. That is exactly what not to do if you will ever share or back up the file. This repo replaces them with placeholders.
