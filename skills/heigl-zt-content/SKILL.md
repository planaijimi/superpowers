---
name: heigl-zt-content
description: Use when creating, refining, or repurposing German LinkedIn and website content for Heigl ZT with transparent sourcing, zero-copy rewriting, and a practical B2B focus.
---

# Heigl ZT Content

## Ziel
Erstelle hochwertigen, umsetzbaren Content für Heigl ZT mit Fokus auf:
- Sicherheitsbeauftragte in großen Unternehmen (DACH)
- fachliche Autorität statt Marketing-Floskeln
- klare Wirkung (Reichweite, Vertrauen, Anfragen)

## Pflichtquellen (in dieser Reihenfolge)
1. `PROMPT.md` (aktiver Arbeitsrahmen)
2. `references/heigl-zt-repo-analysis.md`
3. `references/heigl-zt-corpus.md`
4. `references/regulatory-watch.md` (vorrecherchierte Primärquellen + Content-Winkel)
5. `references/source-transparency-template.md` (Standard für saubere Quellen-/Zitatzeilen)
6. `references/hook-angle-library.md` (schnelle, fachlich belastbare Hook-Starts ohne Clickbait)
7. `references/cta-pattern-library.md` (schnelle, fachlich saubere CTA-Auswahl je Thema)
8. `references/comment-response-playbook.md` (schnelle, fachlich saubere Antwortmuster für LinkedIn-Kommentare)
9. `references/risk-safe-phrasing-library.md` (rechtlich konservative, klare Formulierungen ohne Überversprechen)
10. `references/rapid-review-checklist.md` (90-Sekunden-Freigabecheck vor Versand)
11. `references/group-post-log.jsonl` (strukturierte Historie für spätere Website-Optimierung)
12. Nur bei Bedarf: aktuelle externe Quellen (News/Normen/Regulatorik)

## Verbindliche Regeln
- Keine erfundenen Fakten.
- Kein Copy-Paste aus Quellen/Konkurrenz.
- Immer eigenständig formulieren.
- Zitate nur kurz und klar gekennzeichnet.
- Bei Quellenbezug transparent: Link + kurzer Kontext.
- Bei Unsicherheit konservativ formulieren.

## Priorisierte Leistungen (Content-Gewichtung)
1. AM-VO Überprüfungen
2. Maschinensicherheit & CE-Kennzeichnung
3. Gutachtenerstellung Maschinen-/Anlagenbau
4. GewO §82b Überprüfungen

## Tagesbetrieb (Telegram `heigl-zt-news`)
- Frequenz: Montag bis Samstag
- Zeiten (Europe/Vienna): 06:00, 10:00, 12:00
- Pro Slot: 1 klarer Vorschlag
- Pro Tag: 3 gemischte Vorschläge (privat/firma flexibel nach Relevanz)
- Inhalte müssen auch für Alexander persönlich interessant sein

## Output-Format (Standard)
Nutze genau diese Struktur (ohne Einleitung/Meta-Text):

1. **Titelzeile** (kurz, knackig, LinkedIn-tauglich, ohne Prefix)
2. **Leerzeile**
3. **Hook** (1–2 Zeilen)
4. **Einordnung** (kurz)
5. **3–5 konkrete Punkte** (praxisnah)
6. **Nächster Schritt / Empfehlung**
7. **CTA**
8. **Optional: 3–5 Hashtags**
9. **Transparenzblock**
   - `Quelle(n): ...`
   - `Zitat: keine` _oder_ `Zitat: "..." (Quelle)`

## Qualitätscheck vor Ausgabe
- Ist der Nutzen für Sicherheitsbeauftragte sofort erkennbar?
- Ist der Text klar, präzise, ohne Blabla?
- Ist ein starker Hook enthalten?
- Ist der Text vollständig eigenständig formuliert?
- Sind Quellen/Zitate transparent ausgewiesen?

## Dokumentationspflicht (für spätere Website-Optimierung)
Nach jedem Gruppen-Post in `heigl-zt-news` einen JSONL-Eintrag ergänzen in:
- `references/group-post-log.jsonl`

Pflichtfelder je Eintrag:
- `ts`, `channel`, `group`, `topic`, `servicePriority`, `title`, `hook`, `postText`, `cta`, `hashtags`, `sources`, `quote`, `notesForWebsite`

`notesForWebsite` muss enthalten:
- Kernproblem der Zielgruppe
- Nutzenversprechen
- konkrete Website-Content-Chance (z. B. FAQ, Abschnitt, Landingpage-Idee)

## Schneller Workflow
1. Thema wählen (nach Prioritäten + Relevanz)
2. Quellenlage prüfen (intern zuerst)
3. Entwurf schreiben (Hook → Punkte → CTA)
4. Humanizer-Pass anwenden mit Skill `heigl-linkedin-humanizer` (Pflicht)
5. Transparenzblock ergänzen
6. Qualitätscheck durchgehen
7. Final ausgeben (copy-paste-fähig)

## Ressourcen
- Repo-Extrakt neu erzeugen:

```bash
python3 scripts/extract_heigl_repo_text.py \
  --repo /home/seb/code/www.heigl-zt.at \
  --output references/heigl-zt-corpus.md \
  --include-dir src/pages \
  --include-dir src/components \
  --include-dir src/layouts
```

- Interne Wissensbasis:
  - `references/heigl-zt-corpus.md`
  - `references/heigl-zt-repo-analysis.md`
