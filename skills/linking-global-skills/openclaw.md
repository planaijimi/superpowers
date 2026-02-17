# OpenClaw Integration

## Detection

```bash
[[ -d ~/.openclaw ]] && echo "installed" || echo "not installed"
```

## Instructions

OpenClaw uses `skills.load.extraDirs` in `~/.openclaw/openclaw.json` instead of symlinks.

### Step 1: Check for jq

```bash
which jq >/dev/null 2>&1 && echo "installed" || echo "not installed"
```

If jq is not installed, ask the user:

- Install jq (provide command for their system, e.g., `sudo apt install jq` or `brew install jq`)
- Manually edit the config file (skip to Step 4 for manual instructions)

### Step 2: Read Current Config

```bash
cat ~/.openclaw/openclaw.json 2>/dev/null || echo "{}"
```

### Step 3: Check Current extraDirs

Show the user what's currently configured:

```bash
jq '.skills.load.extraDirs // []' ~/.openclaw/openclaw.json
```

If the master repo path is already in the array, report "OpenClaw already configured" and skip to Step 6.

### Step 4: Add Master Repo to extraDirs

The jq command uses `unique` so it's safe to run multiple times—no duplicates will be created.

```bash
jq --arg path "$MASTER_REPO" \
  '.skills.load.extraDirs += [$path] | .skills.load.extraDirs |= unique' \
  ~/.openclaw/openclaw.json > /tmp/oc.json && mv /tmp/oc.json ~/.openclaw/openclaw.json
```

### Step 5: Verify

```bash
jq '.skills.load.extraDirs' ~/.openclaw/openclaw.json
```

### Step 6: Manual Edit (if jq not available)

If the user chose manual edit, show them the config file location and the required structure:

1. Open `~/.openclaw/openclaw.json`
2. Find or create the `skills.load.extraDirs` array
3. Add the master repo path to the array
4. Save the file

### Step 7: Report

"OpenClaw configured to use master repo at [path]"

## Documentation

Latest: https://docs.openclaw.ai/tools/skills

Config file: `~/.openclaw/openclaw.json`

Skill precedence: workspace > managed > extraDirs > bundled

Format: SKILL.md with YAML frontmatter

**Example config:**
```json
{
  "skills": {
    "load": {
      "extraDirs": ["/path/to/master/skills"]
    }
  }
}
```
