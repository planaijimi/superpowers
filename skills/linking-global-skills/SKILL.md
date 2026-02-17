---
name: linking-global-skills
description: Use when setting up or synchronizing AI tool skills across multiple tools, or when a new tool needs access to shared skills (Linux/macOS only)
---

# Linking Global Skills

**One master repository → all tools sharing the same skills.**

## Supported Tools

Each tool lists its detection command and skill directory:

- **Antigravity**: detected by `[[ -d ~/.gemini/antigravity ]]`
  Skills: `~/.gemini/antigravity/skills/`

- **Claude Code**: detected by `[[ -d ~/.claude ]]`
  Skills: `~/.claude/skills/`

- **Cursor**: detected by `[[ -d ~/.cursor ]]`
  Skills: `~/.cursor/skills/`

- **OpenCode**: detected by `[[ -d ~/.config/opencode ]]`
  Skills: `~/.config/opencode/skills/`

- **Codex/OpenAI/Agents**: detected by `[[ -d ~/.agents ]]`
  Skills: `~/.agents/skills/`

- **Custom tools**: See "Tool Integration Files" below

## Workflow

1. Ask user for master repository path
2. Validate master repository
3. Scan and process each tool directory
4. Process tool integration files (for non-symlink tools)
5. Cleanup orphaned symlinks

## Quick Reference

**Scan tool status:**
```bash
for dir in ~/.gemini/antigravity/skills ~/.claude/skills ~/.cursor/skills ~/.config/opencode/skills ~/.agents/skills; do echo -n "$dir: "; if [[ -L "$dir" ]]; then echo "→ $(readlink "$dir")"; elif [[ -d "$dir" ]]; then echo "dir ($(ls "$dir" 2>/dev/null | wc -l) skills)"; else echo "not found"; fi; done
```

**List skills:**
```bash
ls -1 /path/to/skills/
```

**Create symlink:**
```bash
ln -s /master/repo ~/.config/opencode/skills
```

**Find new skills:**
```bash
comm -23 <(ls tool/skills/ | sort) <(ls master/ | sort)
```

**Find conflicts:**
```bash
comm -12 <(ls tool/skills/ | sort) <(ls master/ | sort)
```

## Execution

### Step 1: Master Repository

Ask user for the master skill repository path using the Question tool.

### Step 2: Validate

```bash
ls /path/to/master/repo/
```

Confirm it contains skill directories (folders with SKILL.md files).

### Step 3: Process Tool Directories

For each tool, first check if it's installed using its detection command. If not installed, skip it entirely.

If installed, handle the skills directory based on its current state:

- **Symlink pointing to correct master**: Skip (already configured)
- **Symlink pointing elsewhere**: Ask user whether to replace
- **Empty directory**: Replace with symlink to master
- **Non-empty directory**: Ask user: Merge, Replace, or Skip
- **Does not exist**: Create symlink to master

### Step 4: Handle Merge

**CRITICAL: Never overwrite existing skills in the master repository.**

When user chooses Merge:

1. Identify conflicts:
   ```bash
   NEW=$(comm -23 <(ls tool/skills/ | sort) <(ls master/ | sort))
   CONFLICTS=$(comm -12 <(ls tool/skills/ | sort) <(ls master/ | sort))
   ```

2. Report to user:
   ```
   New skills to copy: [list]
   Conflicts (will skip): [list]
   Proceed? [Y/n]
   ```

3. Execute:
   ```bash
   for skill in $NEW; do cp -r "tool/skills/$skill" master/; done
   rm -rf tool/skills && ln -s master tool/skills
   ```

### Step 5: Process Integration Files

Some tools require special configuration (not symlinks). These are defined in separate files.

**Discovery:**
```bash
ls linking-global-skills/*.md | grep -v SKILL.md
```

**For each file:**
1. Read file content
2. Run detection command from `## Detection` section
3. If "installed" → follow `## Instructions`
4. Report result to user

### Step 6: Cleanup Orphaned Symlinks

After processing all tools, check for symlinks pointing to the master repo in directories of uninstalled tools.

Ask user if they want to remove these orphaned symlinks.

## Tool Integration Files

Non-symlink tools are configured via integration files in this directory.

### Adding a New Tool

Create `toolname.md` with this structure:

```markdown
# Tool Name Integration

## Detection

```bash
[[ -d ~/.toolname ]] && echo "installed" || echo "not installed"
```

## Instructions

Steps to configure the tool.

## Documentation

(Optional) Link to docs.
```

The skill automatically discovers and processes these files—no changes to SKILL.md needed.

### Current Integrations

- `openclaw.md` - OpenClaw (uses extraDirs config)

## Common Issues

- **Symlink already exists**: Skip if correct, ask if different
- **Permission denied**: Check directory ownership
- **Master repo not found**: Ask user for correct path
- **All skills are conflicts**: Suggest Replace or Skip
- **Tool not installed**: Skip entirely, offer to remove orphaned symlinks
