---
name: openclaw-config-backup-explainer
description: Use when someone asks how OpenClaw config backups to GitHub work (hooks/path+timer), whether tokens are consumed, what is local vs cloud, and how to verify/troubleshoot.
---

# OpenClaw Config Backup Explainer

## Ziel
Erkläre klar und knapp, wie der OpenClaw-Config-Backup-Mechanismus funktioniert:
- trigger-basiert (Dateiänderung)
- periodischer Safety-Net-Lauf
- Push in privates GitHub-Repo
- **ohne LLM-Tokenverbrauch** im normalen Betrieb

## Pflichtquelle
1. `PROMPT.md` (aktueller Erklärrahmen)

## Kernbotschaft (immer enthalten)
- Backups laufen lokal über `systemd` + Shell-Script + `git`/`ssh`.
- Dafür werden **keine OpenAI/OpenClaw-LLM-Tokens** verbraucht.
- Es fallen nur normale Infrastrukturkosten an (CPU/IO/Bandbreite/GitHub API/Git-Verkehr).

## Erklärstruktur (Standard)
1. **Kurzantwort** (Ja/Nein auf Token-Frage)
2. **Warum** (welche Komponenten laufen lokal)
3. **Was trotzdem verbraucht wird** (Systemressourcen)
4. **Wann doch Tokens verbraucht würden** (nur bei Agent-/Modellaufrufen)
5. **Optional:** kurzer Verify-Block (wie prüfen)

## Verify-Block (optional, wenn gefragt)
- `systemctl --user status openclaw-config-backup.path`
- `systemctl --user status openclaw-config-backup.timer`
- `journalctl --user -u openclaw-config-backup.service -n 50 --no-pager`
- letztes Repo-Commit im Backup-Repo prüfen

## Guardrails
- Keine Geheimnisse/Tokens im Klartext posten.
- Nicht behaupten, dass *nie* Tokens genutzt werden: präzise sagen, dass der **Backup-Mechanismus selbst** keine LLM-Tokens braucht.
- Keine unnötigen technischen Romane; klar, direkt, verständlich.
