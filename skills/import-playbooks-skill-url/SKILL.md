---
name: import-playbooks-skill-url
description: Use when a user provides a Playbooks/OpenClaw skill URL and wants that skill imported into the local master skill repository with normalized SKILL.md, SOURCE.md, and LICENSE.
---

# import-playbooks-skill-url

Import a skill from a Playbooks URL into `~/code/superpowers/skills/<slug>`.

## Workflow
1. Validate incoming URL (`https://playbooks.com/skills/...`) and extract `<slug>`.
2. Check whether the page links to `https://github.com/openclaw/skills`.
3. If yes, use local clone:
   - `cd ~/code/skills`
   - `git pull`
   - search for the skill folder (expected: `skills/<owner>/<slug>`)
4. Copy the entire upstream folder into master repo:
   - source: `~/code/skills/skills/<owner>/<slug>`
   - target: `~/code/superpowers/skills/<slug>`
5. Normalize/adapt local package:
   - ensure `SKILL.md` frontmatter uses only `name` + `description`
   - add/update `SOURCE.md` with Playbooks URL + upstream path
   - ensure `LICENSE` exists (from upstream repo)
6. Verify target folder and key files exist; report result.

## Fallback
If the page does not point to `openclaw/skills`, stop and ask the user before importing from another source.

## Rules
- Prefer local clone (`~/code/skills`) when upstream is `openclaw/skills`.
- Use `pnpm dlx` (not `npx`) if Playbooks CLI is ever needed.
- Keep attribution explicit in `SOURCE.md`.
- Keep imported skill concise and runnable in this environment.

## Output checklist
- [ ] Playbooks URL validated
- [ ] `openclaw/skills` link confirmed
- [ ] `~/code/skills` pulled
- [ ] source folder found
- [ ] folder copied to `~/code/superpowers/skills/<slug>`
- [ ] SKILL.md normalized
- [ ] SOURCE.md + LICENSE present
- [ ] final paths reported
