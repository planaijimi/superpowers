# Skill Prompt Versioning Design

**Date:** 2026-02-18
**Owner:** Jimmy

## Context
Seb wants an extension to the skill-creation workflow without modifying OpenClaw core skills. The extension should preserve the initial creation prompt for skills in a dedicated `PROMPT.md` file.

## Requirements
- Add a **new standalone skill** in the superpowers repository.
- `PROMPT.md` should be **optional but highly recommended**.
- `PROMPT.md` must include frontmatter:
  - `purpose: dev-only`
  - `version: <integer>`
- Prompt history is tracked in **git**; `PROMPT.md` should contain only the **current active prompt version**.
- Prompt content should be **very concise, list-based, and human-readable**.

## Chosen Approach
Create a new skill: `skill-prompt-versioning`.

The skill documents:
1. When to add `PROMPT.md`
2. The exact frontmatter contract
3. A concise template
4. Update rules (increment integer version on material intent change)
5. Practical guardrails (no secrets, keep lists short)

## Why this approach
- No changes to OpenClaw’s upstream `skill-creator`.
- Low maintenance and immediate usability.
- Compatible with existing git-based workflows.

## Out of Scope
- Hard enforcement via packaging validator.
- Automation scripts for generating `PROMPT.md`.
- Retrofitting all existing skills automatically.
