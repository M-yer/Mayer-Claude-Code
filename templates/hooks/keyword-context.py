#!/usr/bin/env python3
"""UserPromptSubmit hook: when the prompt mentions KEYWORD, inject extra context for this turn."""
import json
import re
import sys

KEYWORD = r"myclient"                       # regex, case-insensitive
KB = "/path/to/knowledge-base"              # folder Claude should load

try:
    prompt = json.load(sys.stdin).get("prompt", "")
except Exception:
    sys.exit(0)

if not re.search(KEYWORD, prompt, re.I):
    sys.exit(0)

context = (
    f"KNOWLEDGE BASE RULE. 1) If not yet read this session, read {KB}/00-INDEX.md first. "
    f"2) Before ending the turn, append (never overwrite) any new decision or fact, dated, to the matching note in {KB}. "
    f"3) Never write secrets into notes; paths only. 4) If nothing new, write nothing."
)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": context}}))
