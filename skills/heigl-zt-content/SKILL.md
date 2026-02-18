---
name: heigl-zt-content
description: Use when creating, reviewing, improving, or repurposing German content for Heigl ZT across website, LinkedIn, and social media, including competitor benchmarking and adapting research into brand-consistent drafts.
---

# Heigl ZT Content

## Überblick
Nutze diesen Skill für alle Content-Aufgaben rund um Heigl ZT: Analyse, Optimierung, Neuentwicklung und kanalgerechte Adaption.

Ziel: Inhalte mit messbarer Marketingwirkung erstellen, in klarer Corporate Language, ohne Floskeln.

## Pflichtergebnis
1. **Substanz vor Stil:** Nutzen, Klarheit, Relevanz für die Zielgruppe.
2. **Corporate Language:** Direkt, professionell, verständlich, kompetent.
3. **Kanalfit:** Format, Länge und CTA passend zum Kanal.
4. **Umsetzbarkeit:** Vorschläge so konkret, dass sie sofort nutzbar sind.

## Workflow
1. **Ziel klären**
   - Zielgruppe
   - Kanal (Website, LinkedIn, Social)
   - Ziel (Awareness, Vertrauen, Leads)
2. **Quellen sammeln**
   - Heigl-ZT-Basisinhalte aus Repo-Extrakt (siehe Ressourcen)
   - Relevante Konkurrenzbeispiele
   - Aktuelle Recherchequellen
3. **Analyse liefern**
   - Stärken/Schwächen
   - 3–7 konkrete Verbesserungen mit kurzer Begründung
4. **Content erzeugen**
   - 1 finale Version + optional 1–2 Varianten
   - klare Struktur (Hook, Kernbotschaft, CTA)
5. **Qualitätscheck**
   - markenkonsistent
   - keine unbelegten Behauptungen
   - sprachlich präzise, keine Füllsätze

## Standard-Ausgabeformat
- **Ziel**
- **Zielgruppe**
- **Kanal/Format**
- **Finaler Text**
- **CTA**
- **Kurzbegründung** (2–4 Bulletpoints)
- **Optional: Varianten**

## Ressourcen
- Repo-Text-Extrakt erzeugen/aktualisieren:

```bash
python3 scripts/extract_heigl_repo_text.py \
  --repo /home/seb/code/www.heigl-zt.at \
  --output references/heigl-zt-corpus.md \
  --include-dir src/pages \
  --include-dir src/components \
  --include-dir src/layouts
```

- Extrahierter Korpus:
  - `references/heigl-zt-corpus.md`

## Guardrails
- Keine erfundenen Fakten.
- Keine rechtlich riskanten Aussagen ohne Grundlage.
- Keine 1:1-Übernahme von Konkurrenztexten.
- Bei fehlendem Kontext max. 3 präzise Rückfragen stellen.
