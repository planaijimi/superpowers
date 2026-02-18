---
name: skill-prompt-versioning
description: Use when creating or updating AgentSkills and you want a lightweight convention for an optional but strongly recommended PROMPT.md that stores the current prompt snapshot with integer versioning while git keeps full history.
---

# Skill Prompt Versioning

## Overview
Use this convention to keep the original skill intent visible and easy to iterate.

`PROMPT.md` is **optional but highly recommended** for every skill.

## Rules
1. Place `PROMPT.md` in the skill root (`<skill>/PROMPT.md`).
2. Use frontmatter:
   - `purpose: dev-only`
   - `version: <integer>`
3. Keep only the **current active prompt** in this file.
4. Keep content concise, list-based, and human-readable.
5. Use git history for full evolution and previous prompt versions.
6. Increment `version` when prompt intent changes materially.
7. Never store secrets in `PROMPT.md`.

## Recommended Template
```md
---
purpose: dev-only
version: 1
---

# Active Prompt (Current)

- Goal: <one short line>
- Scope: <one short line>
- Constraints: <short bullets>
- Success criteria: <short bullets>
```

## Update Workflow
1. Edit concise bullets to match current intent.
2. Increase integer version if change is material.
3. Commit with a clear message (git is the audit trail).

## Done Checklist
- [ ] `PROMPT.md` exists (recommended)
- [ ] Frontmatter is valid
- [ ] Prompt is short and list-based
- [ ] Version is integer and current
- [ ] Changes committed to git
