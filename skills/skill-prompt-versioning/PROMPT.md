---
purpose: dev-only
version: 1
---

# Active Prompt (Current)

- Goal: Add a standalone skill that introduces `PROMPT.md` as optional but highly recommended for skill development.
- Format: Require concise, list-based content for humans plus frontmatter with `purpose: dev-only` and integer `version`.
- History model: Keep only the current prompt snapshot in `PROMPT.md`; use git commits as full version history.
- Scope: Process guidance only (no scripts, no packaging enforcement).
- Success: Agents creating/updating skills can apply one clear, reusable convention.
