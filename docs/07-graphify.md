# Graphify: query instead of read

Graphify builds a knowledge graph of a project (code, docs, images) into `<project>/graphify-out/graph.json`. Claude queries it instead of opening files, which saves a lot of context.

## Rules in my `CLAUDE.md`

1. Keep a table of *project → graph path* in the global file.
2. At session start, if the project is in the table, query it:
   `graphify query "<question>" --graph "<project>/graphify-out/graph.json"`
3. Read source files only if the answer is insufficient or the file needs editing.
4. Never read a file just to learn structure.
5. After adding or heavily changing files: `graphify update <project-root>`.
6. New project: run `/graphify <path>` once after scaffolding, then add it to the table.

## Two locations, do not confuse them

| Path | Purpose |
|---|---|
| `<project>/graphify-out/graph.json` | The queryable graph the CLI uses |
| `<vault>/graphify/<project>/` | Obsidian canvas mirror, for viewing only |

Always query the first one. Export the mirror with the `--obsidian` flag.

## Known-graphs table format

```markdown
**Known graphs**: base: `/path/to/projects/`

| Project | Folder |
|---|---|
| my-site | `my-site` |
```
