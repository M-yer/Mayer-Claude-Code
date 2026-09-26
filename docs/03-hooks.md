# Hooks

Hooks are commands the **harness** runs on events. Claude does not decide to run them, so they are reliable in a way instructions are not.

Use a hook when you would otherwise write "always do X after Y" in `CLAUDE.md`.

## Mine: keyword-triggered context injection

Event: `UserPromptSubmit`. The script reads the prompt from stdin; if it mentions a keyword, it prints JSON that adds context for that turn. Otherwise it exits silently.

Register in `~/.claude/settings.json`:

```json
"hooks": {
  "UserPromptSubmit": [
    { "hooks": [
      { "type": "command",
        "command": "python3 \"$HOME/.claude/hooks/keyword-context.py\" 2>/dev/null || true",
        "timeout": 10 }
    ] }
  ]
}
```

Script: [`templates/hooks/keyword-context.py`](../templates/hooks/keyword-context.py).

What it buys: mention a client name and Claude is told to read that client's knowledge base first and to append new decisions to it before ending the turn. No need to remember to ask.

## Rules of thumb

- End the command with `|| true` so a broken hook never blocks you.
- Set a `timeout`.
- Output nothing (exit 0) when the hook does not apply.
- Common events: `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`.
- Debug by running the script by hand: `echo '{"prompt":"myclient test"}' | python3 hook.py`.
- Hooks from plugins (I have several) run alongside yours. If one is noisy, disable it with env vars in `settings.local.json`.
