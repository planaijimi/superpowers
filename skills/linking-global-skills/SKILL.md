---
name: linking-global-skills
description: Use when setting up or synchronizing AI tool skills across multiple tools, or when a new tool needs access to shared skills (Linux/macOS only)
---

# Linking Global Skills

**One master repository → all tools sharing the same skills.**

## Supported Tools

Each tool lists its detection command, skill directory, and official superpowers clone location (if applicable):

| Tool | Detection | Skills Directory | Manual Superpowers Clone |
|------|-----------|------------------|--------------------------|
| Antigravity | `~/.gemini/antigravity` | `~/.gemini/antigravity/skills/` | `~/.gemini/antigravity/superpowers` |
| Claude Code | `~/.claude` | `~/.claude/skills/` | `~/.claude/superpowers` |
| Cursor | `~/.cursor` | `~/.cursor/skills/` | `~/.cursor/superpowers` |
| OpenCode | `~/.config/opencode` | `~/.config/opencode/skills/` | `~/.config/opencode/superpowers` |
| Codex | `~/.agents` | `~/.agents/skills/` | `~/.codex/superpowers` |
| Custom tools | See "Tool Integration Files" below |

## Workflow

1. Ask user for master repository path
2. Validate master repository
3. Identify tools to skip (master repo is at official superpowers location)
4. Scan and process each remaining tool directory
5. Process tool integration files (for non-symlink tools)
6. Cleanup orphaned symlinks

## Quick Reference

**Scan tool status:**
```bash
# Check if tool is installed (Detection column) and skills directory state
for tool in "antigravity:~/.gemini/antigravity:~/.gemini/antigravity/skills" \
            "claude:~/.claude:~/.claude/skills" \
            "cursor:~/.cursor:~/.cursor/skills" \
            "opencode:~/.config/opencode:~/.config/opencode/skills" \
            "codex:~/.agents:~/.agents/skills"; do
  name="${tool%%:*}"
  detect="${tool#*:}"; detect="${detect%%:*}"
  skills="${tool##*:}"
  detect="${detect/#\~/$HOME}"
  skills="${skills/#\~/$HOME}"
  echo -n "$name: "
  if [[ ! -d "$detect" ]]; then
    echo "not installed"
  elif [[ -L "$skills" ]]; then
    echo "→ $(readlink "$skills")"
  elif [[ -d "$skills" ]]; then
    echo "dir ($(ls "$skills" 2>/dev/null | wc -l) skills)"
  else
    echo "installed, no skills dir"
  fi
done
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

### Step 3: Identify Tools to Skip

If the master repository is located at a manual superpowers clone location, skip that tool—it's already configured correctly via the standard installation method.

**Detection logic:**
```bash
MASTER_REPO="/path/to/user/provided/repo"
MASTER_REPO_REAL=$(cd "$MASTER_REPO" && pwd)

# Map each tool's manual clone location to the tool to skip
case "$MASTER_REPO_REAL" in
  */.gemini/antigravity/superpowers) SKIP_ANTIGRAVITY=true ;;
  */.claude/superpowers) SKIP_CLAUDE=true ;;
  */.cursor/superpowers) SKIP_CURSOR=true ;;
  */.config/opencode/superpowers) SKIP_OPENCODE=true ;;
  */.codex/superpowers) SKIP_CODEX=true ;;
esac
```

Report to user which tools will be skipped and why:
```
Skipping OpenCode: master repo is at manual clone location (~/.config/opencode/superpowers)
```

### Step 4: Process Tool Directories

For each tool (excluding skipped tools), first check if it's installed using its **Detection** path (from the table above). If not installed, skip it entirely.

**Note:** The skills directory may not exist yet—this is normal for newly installed tools. The tool is still considered "installed" if its main directory exists.

If installed, handle the skills directory based on its current state:

- **Symlink pointing to correct master**: Skip (already configured)
- **Symlink pointing elsewhere**: Ask user whether to replace
- **Empty directory**: Replace with symlink to master
- **Non-empty directory**: Ask user: Merge, Replace, or Skip
- **Does not exist**: Create symlink to master

### Step 5: Handle Merge

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

### Step 6: Process Integration Files

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

### Step 7: Cleanup Orphaned Symlinks

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

- **Skills directory doesn't exist**: Normal for new installations—create symlink to master repo
- **Master repo at manual clone location**: Tool is skipped automatically—already configured via standard install
- **Symlink already exists**: Skip if correct, ask if different
- **Permission denied**: Check directory ownership
- **Master repo not found**: Ask user for correct path
- **All skills are conflicts**: Suggest Replace or Skip
- **Tool not installed**: Skip entirely, offer to remove orphaned symlinks
