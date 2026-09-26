# Global CLAUDE.md: [YOUR NAME]
> Keep under 250 lines. Trim before adding.

## Agent Behavior (read this first)

### Think before coding
- If a request is ambiguous, state your interpretation before writing code. Don't silently pick one.
- If multiple approaches have real tradeoffs, name them briefly and ask.
- If something contradicts earlier context, say so. Don't comply silently.
- Stop and ask rather than guess if the answer changes what gets built.

### Simplicity first
- Minimum code that solves the problem. Nothing speculative.
- No abstraction layers unless reuse is certain and immediate.
- No error handling for scenarios that cannot happen.

### Surgical changes only
- Modify only what the task requires. No drive-by refactors or reformatting.
- Don't remove comments or code you don't understand.
- One task = one focused diff.

### Goal-driven execution
- Define "done" before starting. If unclear, ask.
- After finishing, verify the original goal is met, not just that it runs.
- If blocked, say so instead of shipping partial output.

### Context continuity
- At session start, read `[NOTES PATH]/projects/[project]` before asking questions.
- Update the project note when something meaningful is decided, not at the end.
- Goal: next session needs zero re-explaining.

### No scope creep
- New idea mid-task? Say: "We're currently doing [X]. This would expand scope. Finish first, or pivot?" and wait.
- If my approach is flawed, say: "Your approach has a problem: [issue]. Why: [reason]. Suggested fix: [alt]. How do you want to proceed?"
- Be direct. I prefer correction to wasted time.

---

## Environment
- **OS:** [Linux/macOS/Windows]
- **Shell:** [bash/zsh/PowerShell]
- **Projects live in:** `[PATH]`
- **Available globally:** [node, python, ...]

### Cross-OS warning (delete if single-OS)
Before writing a hardcoded path or OS-specific command, warn once: "This is OS-specific. Confirm target OS or use a cross-platform approach."

---

## Stack Selection
No default framework. Before choosing, ask: who uses it, where does it run, what scope, is there an existing codebase (match it).

| Use case | Default thinking |
|---|---|
| Internal tool | Simplest thing: script, plain HTML + JS |
| Client-facing web app | Match complexity: static = Astro/HTML; dynamic = Next.js/SvelteKit |
| Backend/API | Match existing stack first |
| Desktop / Mobile | [your picks] |

State stack + reasoning before scaffolding.

## Code Style
- Comments only when the WHY is non-obvious.
- No dead code, no commented-out blocks.
- Follow the project's existing conventions.

## UI/UX Rules (client-facing only)
- Mobile layout first.
- Real content, no lorem ipsum.
- Animations subtle on desktop, smooth on mobile.

## Git
- Commit after each meaningful unit with a clear message.
- Push only when asked or when a task is complete.
- Identity: `[Name] <[email]>`. Add attribution rules here (e.g. "no Co-Authored-By lines").

## Browser Automation
- Use [Playwright / other] for navigation, forms, scraping.
- DevTools-style tools: inspection/debugging only.

---

## Second brain (optional; only if Obsidian MCP tools exist)
- Vault: `[PATH]`
- Start: read `knowledge/projects/[project]` and `projects/sessions/[project]/`.
- During: quick ideas/blockers go to `inbox/`.
- After a task: append `projects/sessions/[project]/YYYY-MM-DD` (changes only).
- Never overwrite notes. Don't log routine edits.

## Graphify (optional)
Query the graph before reading files: `graphify query "<q>" --graph "<project>/graphify-out/graph.json"`

| Project | Folder |
|---|---|
| [name] | `[folder]` |

## Project-specific auto-loads (optional)
- When [CLIENT] comes up: read `[KB PATH]/00-INDEX.md` first. Backed by a UserPromptSubmit hook.
