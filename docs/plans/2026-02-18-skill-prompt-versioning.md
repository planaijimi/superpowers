# Skill Prompt Versioning Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a standalone skill that standardizes optional-but-recommended `PROMPT.md` usage for skill development with concise current-prompt snapshots and integer versioning.

**Architecture:** Introduce one new skill directory under `skills/` with a focused `SKILL.md` and a dogfooded `PROMPT.md` example. Keep rules process-oriented only (no scripts, no validators), with Git as source of full historical diffs.

**Tech Stack:** Markdown, YAML frontmatter, existing superpowers skill conventions.

---

### Task 1: Create new skill directory skeleton

**Files:**
- Create: `skills/skill-prompt-versioning/SKILL.md`
- Create: `skills/skill-prompt-versioning/PROMPT.md`

**Step 1: Verify target directory does not already exist**

Run: `test -d /home/seb/code/superpowers/skills/skill-prompt-versioning && echo EXISTS || echo MISSING`
Expected: `MISSING`

**Step 2: Create directory**

Run: `mkdir -p /home/seb/code/superpowers/skills/skill-prompt-versioning`
Expected: Directory created successfully.

**Step 3: Commit**

```bash
git -C /home/seb/code/superpowers add skills/skill-prompt-versioning
# commit deferred until content is added
```

### Task 2: Author SKILL.md with concise convention guidance

**Files:**
- Modify: `skills/skill-prompt-versioning/SKILL.md`

**Step 1: Write content with required frontmatter (`name`, `description`)**

Include:
- Trigger conditions for skill creation/update contexts
- Rule that `PROMPT.md` is optional but highly recommended
- Required frontmatter keys for `PROMPT.md`: `purpose: dev-only`, `version: <integer>`
- Guidance that git stores full history; `PROMPT.md` stores current active prompt only
- Short list-based template

**Step 2: Validate readability and brevity**

Run: `wc -w /home/seb/code/superpowers/skills/skill-prompt-versioning/SKILL.md`
Expected: Concise doc that remains easy to scan.

**Step 3: Commit**

```bash
git -C /home/seb/code/superpowers add skills/skill-prompt-versioning/SKILL.md
git -C /home/seb/code/superpowers commit -m "feat(skills): add prompt versioning convention skill"
```

### Task 3: Add PROMPT.md example for the new skill itself

**Files:**
- Modify: `skills/skill-prompt-versioning/PROMPT.md`

**Step 1: Add frontmatter and concise list-based active prompt**

Template:

```md
---
purpose: dev-only
version: 1
---

# Active Prompt (Current)

- ...
- ...
- ...
```

**Step 2: Verify frontmatter and format**

Run: `sed -n '1,40p' /home/seb/code/superpowers/skills/skill-prompt-versioning/PROMPT.md`
Expected: Valid frontmatter and concise bullet list.

**Step 3: Commit**

```bash
git -C /home/seb/code/superpowers add skills/skill-prompt-versioning/PROMPT.md
git -C /home/seb/code/superpowers commit -m "docs(skills): add prompt snapshot for skill-prompt-versioning"
```

### Task 4: Final verification

**Files:**
- Verify: `skills/skill-prompt-versioning/SKILL.md`
- Verify: `skills/skill-prompt-versioning/PROMPT.md`

**Step 1: Display both files for final check**

Run:

```bash
sed -n '1,220p' /home/seb/code/superpowers/skills/skill-prompt-versioning/SKILL.md
sed -n '1,120p' /home/seb/code/superpowers/skills/skill-prompt-versioning/PROMPT.md
```

Expected: Conforms to requested convention and remains short.

**Step 2: Commit (if not already done)**

```bash
git -C /home/seb/code/superpowers status --short
```

Expected: New skill files staged/committed per team preference.
