# Heigl ZT Repository Analyse (Snapshot)

- Datum: 2026-02-18 04:54
- Repo: `/home/seb/code/www.heigl-zt.at`
- Branch: `main`
- Commit: `4dbdbf0`

## 1) Technischer Überblick

- Framework: Astro 5 + Tailwind CSS 4
- Content: Astro + MDX (`src/components/content/leistungen/*.mdx`)
- SEO: `astro-seo`, Sitemap Integration aktiv
- Karten: Leaflet (Standorte Graz/Wien)
- Sprache: Default Locale `de`
- URL-Format: `trailingSlash=always`
- Sitemap filtert `/partner-projekte` aktiv aus

### Dependencies (Produktion)
- @astrojs/mdx
- @astrojs/sitemap
- @tailwindcss/typography
- @tailwindcss/vite
- astro
- astro-seo
- blurhash
- leaflet
- sharp
- tailwindcss

### Dependencies (Dev)
- @eslint/eslintrc
- @eslint/js
- @types/leaflet
- @typescript-eslint/eslint-plugin
- @typescript-eslint/parser
- astro-compress
- astro-eslint-parser
- eslint
- eslint-plugin-astro
- eslint-plugin-jsx-a11y
- globals
- prettier
- prettier-plugin-astro
- prettier-plugin-css-order
- prettier-plugin-tailwindcss
- svg-to-ico
- terser

## 2) Seiten / Routen

| Route | Datei | SEO-Title | SEO-Description |
|---|---|---|---|
| `/404` | `404.astro` | 404 - Seite nicht gefunden \| Heigl Ziviltechnik | Die angeforderte Seite wurde nicht gefunden. |
| `/agb-und-datenschutz/` | `agb-und-datenschutz.astro` | HEIGL ZT: AGB & Datenschutz | Unsere Allgemeinen Geschäftsbedingungen und Datenschutzbestimmungen. |
| `/` | `index.astro` | HEIGL ZT: Ziviltechniker für Maschinenbau in Graz und Wien | HEIGL ZT: Ziviltechniker für Maschinenbau in Graz und Wien, für ganz Österreich. Persönliche Beratung durch Dipl.-Ing. Alexander Heigl, BSc. |
| `/kontakt/` | `kontakt.astro` | Kontakt HEIGL ZT: Ziviltechniker für Maschinenbau | HEIGL ZT: Ihr staatlich befugter und beeideter Zivilingenieur für Maschinenbau in Graz. Wir beraten Sie gerne in allen Fragen rund um Ziviltechnik in Österreich. Persönliche Beratung durch Dipl.-Ing. Alexander Heigl, BSc. |
| `/leistungen/arbeitnehmerinnenschutz-und-sicherheit-am-arbeitsplatz/` | `leistungen/arbeitnehmerinnenschutz-und-sicherheit-am-arbeitsplatz.astro` | ArbeitnehmerInnenschutz & Sicherheit am Arbeitsplatz | Evaluierung, Sicherheits- & Gesundheitsschutzdokument (DOK-VO), Unterweisungen & sicherheitstechnische Betreuung. ArbeitnehmerInnenschutz nach ASchG. |
| `/leistungen/begutachtung-von-kraftfahrzeugen/` | `leistungen/begutachtung-von-kraftfahrzeugen.astro` | Unabhängige Kfz-Gutachten & Kfz-Typisierung \| Heigl ZT | Unabhängige Kfz‑Sachverständigen‑Gutachten durch staatlich befugten und beeideten Zivilingenieur – Wertgutachten, Einzelgenehmigung, Umtypisierung, ... |
| `/leistungen/gutachtenerstellung-im-maschinenbau-und-anlagenbau/` | `leistungen/gutachtenerstellung-im-maschinenbau-und-anlagenbau.astro` | Gutachtenerstellung im Maschinen- & Anlagenbau \| Heigl ZT | Ziviltechniker-Gutachten im Maschinen- & Anlagenbau: Schadensgutachten, Lärm-/Schwingungsmessungen & Wertgutachten. Belastbar, normkonform, österreichweit. |
| `/leistungen/kommerzielle-bewertung-von-fahrnissen/` | `leistungen/kommerzielle-bewertung-von-fahrnissen.astro` | Kommerzielle Bewertung von Fahrnissen \| Heigl ZT | Unabhängige Ziviltechniker‑Gutachten für Fahrnisse (Maschinen, Anlagen, Fahrzeuge, ...) in Österreich. Belastbar, nachvollziehbar und gerichtstauglich. |
| `/leistungen/maschinensicherheit-und-ce-kennzeichnung/` | `leistungen/maschinensicherheit-und-ce-kennzeichnung.astro` | CE‐Kennzeichnung & Maschinensicherheit \| Heigl ZT | CE‑Kennzeichnung & Maschinensicherheit mit Heigl ZT: Strategie, Risikobeurteilung, Dokumentation, EU‑Erklärung... Heigl ZT Graz & Wien für ganz Österreich. |
| `/leistungen/oldtimerbegutachtung-begutachtung-von-historischen-fahrzeugen/` | `leistungen/oldtimerbegutachtung-begutachtung-von-historischen-fahrzeugen.astro` | Unabhängige Oldtimer-Gutachten in Österreich \| Heigl ZT | Oldtimer‑ & Youngtimer-Gutachten, auch für Typisierung & Einzelgenehmigungen in Österreich durch Kfz-Sachverständigen. Unabhängige Ziviltechniker‑Qualität. |
| `/leistungen/projekte-im-maschinenbau-anlagenbau-und-industrieanlagenbau/` | `leistungen/projekte-im-maschinenbau-anlagenbau-und-industrieanlagenbau.astro` | Projekte im Maschinenbau, Anlagenbau und Industrieanlagenbau | HEIGL ZT: Wir beraten Sie gerne in allen Fragen rund um Projekte im Maschinenbau, Anlagenbau und Industrieanlagenbau in Österreich. |
| `/leistungen/ueberpruefungen-nach-arbeitsmittelverordnung/` | `leistungen/ueberpruefungen-nach-arbeitsmittelverordnung.astro` | AM‑VO‑Prüfungen: sicher & rechtskonform \| HEIGL ZT | AM‑VO‑Prüfungen nach §7/§8/§9/§10 – prüfstellengerechte Befunde, Maßnahmen & Fristenmanagement. Ziviltechniker‑Qualität. |
| `/leistungen/ueberpruefungen-nach-gewerbeordnung/` | `leistungen/ueberpruefungen-nach-gewerbeordnung.astro` | GewO § 82b: Überprüfung von Betriebsanlagen \| Heigl ZT | Fachgerechte § 82b GewO‑Überprüfung: Abgleich Bescheid & Auflagen, Sicherheits‑/Umweltschutz, Maßnahmenplan mit Fristen & auditfester Bericht. |
| `/leistungen/umstrukturierungen-von-maschinenparks-und-verlagerung-von-produktionsstaetten/` | `leistungen/umstrukturierungen-von-maschinenparks-und-verlagerung-von-produktionsstaetten.astro` | Maschinenpark-Umstrukturierung & Verlagerung \| Heigl ZT | Ihr Ziviltechniker‑Partner für sichere, termintreue und wirtschaftliche Umstrukturierung und Verlagerung von Maschinen, Linien & Anlagen in Österreich. |
| `/leistungen/` | `leistungen.astro` | Leistungen von HEIGL ZT: Ziviltechniker für Maschinenbau | Dienstleistungen und Tätigkeitsfelder von HEIGL ZT: Ziviltechniker für Maschinenbau in Graz und Wien. Beratung, Begutachtung, Bewertung & Entwicklung für ganz Österreich. |
| `/partner-projekte/` | `partner-projekte.astro` |  |  |
| `/standorte-graz-wien/` | `standorte-graz-wien.astro` | HEIGL ZT Standorte: Graz & Wien \| Ziviltechniker für Maschinenbau | HEIGL ZT: Standorte Graz und Wien. Ihr staatlich befugter und beeideter Zivilingenieur für Maschinenbau in Graz und Wien. |
| `/ziviltechnikerkanzlei/` | `ziviltechnikerkanzlei.astro` | Ziviltechnikerkanzlei Dipl.‑Ing. Alexander Heigl | Staatlich befugter und beeideter Zivilingenieur für Wirtschaftsingenieurwesen-Maschinenbau. Persönliche Beratung durch Dipl.-Ing. Alexander Heigl, BSc. |

## 3) Leistungen (Detailseiten)

| Route | Wrapper | SEO-Title | H1 in MDX | MDX-Quelle |
|---|---|---|---|---|
| `/leistungen/arbeitnehmerinnenschutz-und-sicherheit-am-arbeitsplatz/` | `arbeitnehmerinnenschutz-und-sicherheit-am-arbeitsplatz.astro` | ArbeitnehmerInnenschutz & Sicherheit am Arbeitsplatz | ArbeitnehmerInnenschutz und Sicherheit am Arbeitsplatz in&nbsp;Österreich | `src/components/content/leistungen/arbeitnehmerinnenschutz-und-sicherheit-am-arbeitsplatz.mdx` |
| `/leistungen/begutachtung-von-kraftfahrzeugen/` | `begutachtung-von-kraftfahrzeugen.astro` | Unabhängige Kfz-Gutachten & Kfz-Typisierung \| Heigl ZT | Kfz‑Gutachten & Typisierung in&nbsp;Österreich | `src/components/content/leistungen/begutachtung-von-kraftfahrzeugen.mdx` |
| `/leistungen/gutachtenerstellung-im-maschinenbau-und-anlagenbau/` | `gutachtenerstellung-im-maschinenbau-und-anlagenbau.astro` | Gutachtenerstellung im Maschinen- & Anlagenbau \| Heigl ZT | Gutachtenerstellung im Maschinenbau und Anlagenbau in&nbsp;Österreich | `src/components/content/leistungen/gutachtenerstellung-im-maschinenbau-und-anlagenbau.mdx` |
| `/leistungen/kommerzielle-bewertung-von-fahrnissen/` | `kommerzielle-bewertung-von-fahrnissen.astro` | Kommerzielle Bewertung von Fahrnissen \| Heigl ZT | Kommerzielle Bewertung von Fahrnissen in&nbsp;Österreich | `src/components/content/leistungen/kommerzielle-bewertung-von-fahrnissen.mdx` |
| `/leistungen/maschinensicherheit-und-ce-kennzeichnung/` | `maschinensicherheit-und-ce-kennzeichnung.astro` | CE‐Kennzeichnung & Maschinensicherheit \| Heigl ZT | CE&#8209;Kennzeichnung und Maschinensicherheit in&nbsp;Österreich | `src/components/content/leistungen/maschinensicherheit-und-ce-kennzeichnung.mdx` |
| `/leistungen/oldtimerbegutachtung-begutachtung-von-historischen-fahrzeugen/` | `oldtimerbegutachtung-begutachtung-von-historischen-fahrzeugen.astro` | Unabhängige Oldtimer-Gutachten in Österreich \| Heigl ZT | Oldtimerbegutachtung: Gutachten für historische Fahrzeuge in&nbsp;Österreich | `src/components/content/leistungen/oldtimerbegutachtung-begutachtung-von-historischen-fahrzeugen.mdx` |
| `/leistungen/projekte-im-maschinenbau-anlagenbau-und-industrieanlagenbau/` | `projekte-im-maschinenbau-anlagenbau-und-industrieanlagenbau.astro` | Projekte im Maschinenbau, Anlagenbau und Industrieanlagenbau | Projekte im Maschinenbau, Anlagenbau und Industrieanlagenbau in&nbsp;Österreich | `src/components/content/leistungen/projekte-im-maschinenbau-anlagenbau-und-industrieanlagenbau.mdx` |
| `/leistungen/ueberpruefungen-nach-arbeitsmittelverordnung/` | `ueberpruefungen-nach-arbeitsmittelverordnung.astro` | AM‑VO‑Prüfungen: sicher & rechtskonform \| HEIGL ZT | Überprüfungen nach Arbeitsmittelverordnung in Österreich mit Heigl ZT | `src/components/content/leistungen/ueberpruefungen-nach-arbeitsmittelverordnung.mdx` |
| `/leistungen/ueberpruefungen-nach-gewerbeordnung/` | `ueberpruefungen-nach-gewerbeordnung.astro` | GewO § 82b: Überprüfung von Betriebsanlagen \| Heigl ZT | GewO § 82b – Wiederkehrende Überprüfung von Betriebsanlagen in&nbsp;Österreich | `src/components/content/leistungen/ueberpruefungen-nach-gewerbeordnung.mdx` |
| `/leistungen/umstrukturierungen-von-maschinenparks-und-verlagerung-von-produktionsstaetten/` | `umstrukturierungen-von-maschinenparks-und-verlagerung-von-produktionsstaetten.astro` | Maschinenpark-Umstrukturierung & Verlagerung \| Heigl ZT | Umstrukturierungen von Maschinenparks und Verlagerung von Produktionsstätten | `src/components/content/leistungen/umstrukturierungen-von-maschinenparks-und-verlagerung-von-produktionsstaetten.mdx` |

## 4) Referenzen & Social Proof

### 4.1 Projekte & Referenzen (Logo-Wall) — 25 Einträge
1. Fresenius Kabi Austria GmbH
2. Holding Graz
3. KTM AG
4. Pierer Mobility AG
5. Biocraftlab 3D Print GmbH
6. TÜV Rheinland AG
7. ABB AG
8. Österreichische Post AG
9. Logistikkomponenten GmbH
10. Deltaforce Engineering GmbH
11. Weyland GmbH
12. Cura-San Bandagist GmbH
13. PALFINGER AG
14. Wiener Städtische Versicherung AG
15. Spannbeton Ltd.
16. FAB Verein
17. MHT e.U.
18. VMG Niederdruckguss GmbH
19. Kobleder GmbH
20. TLL The Longevity Labs GmbH
21. Die Autowaschbären e.U.
22. KLEDO Reisemobile GmbH
23. KHU Sondermaschinen GmbH
24. Faenger Systems GmbH
25. Musik Meisinger e.K.

### 4.2 Kundenstimmen — 5 Einträge (derzeit auf Startseite auskommentiert)
1. **Tobias Elmer** — „Hervorragende Termintreue, erstklassige Umsetzung und hochwertige Dokumentation, selbst unter Zeitdruck.“
2. **Franco Pichler** — „Rasche und professionelle Erstellung eines Gutachtens! Gerne wieder, klare Weiterempfehlung!“
3. **Arne Schlachter** — „Sehr seriös mit herausragender Expertise“
4. **Nico Teuschler** — „Was mich besonders beeindruckt hat, war die Effizienz und Genauigkeit, mit der Herr Heigl seine Arbeit erledigt.“
5. **Robert Sorgmann** — „Verlässlichkeit, Fachwissen und Engagement auf höchstem Niveau – absolut empfehlenswert für jeden der einen Ziviltechniker sucht!“

Hinweis: In `src/pages/index.astro` ist `<Testimonials />` aktuell auskommentiert.

## 5) Kontakt-, Standort- und Firmendaten (aus Quellcode)

- Telefon: `+43 699 15 91 64 13`
- E-Mail: `office@heigl-zt.at`
- Website: `https://www.heigl-zt.at`
- Kanzlei Graz: Muchargasse 30, 8010 Graz
- Zweigniederlassung Wien: Zukunftsweg 26, 1210 Wien
- UID: `ATU78333135`
- IBAN: `AT43 4300 0421 9880 5006`
- BIC: `VBOEATWWXXX`
- Kontoinhaber: Alexander Heigl
- Bank: Volksbank Wien
- Gerichtstand: Graz

## 6) Navigation / Informationsarchitektur

- Die Kanzlei → `/ziviltechnikerkanzlei/`
- Leistungen → `/leistungen/`
- Standorte → `/standorte-graz-wien/`
- Kontakt → `/kontakt/`
- Startseite → `/`

## 7) Dateibestand (grob)

- Gesamtdateien im Repo: **546**
- Häufigste Dateitypen:
  - `.jpg`: 130
  - `.webp`: 104
  - `.avif`: 100
  - `.png`: 47
  - `.svg`: 37
  - `.astro`: 32
  - `.json`: 18
  - `.html`: 18
  - `(none)`: 15
  - `.sample`: 14
  - `.mdx`: 11
  - `.js`: 4
  - `.yaml`: 2
  - `.mjs`: 2
  - `.txt`: 2

## 8) Relevante Beobachtungen für Content/Marketing

- Starker fachlicher Fokus auf Maschinenbau-/Anlagenbau-nahe B2B-Leistungen und Compliance-Themen in Österreich.
- Referenzbereich ist breit (Industrie, Mobilität, Medizin/Pharma, Versicherungen, Logistik).
- Social Proof vorhanden (Testimonials), aber aktuell nicht live auf der Startseite eingebunden.
- Technische Basis ist SEO-geeignet (saubere Seitenstruktur, Sitemap, individuelle Meta-Descriptions je Kernseite).

## 9) Speicherorte der aufbereiteten Inhalte

- Volltext-Korpus: `/home/seb/code/superpowers/skills/heigl-zt-content/references/heigl-zt-corpus.md`
- Analyse-Snapshot: `/home/seb/code/superpowers/skills/heigl-zt-content/references/heigl-zt-repo-analysis.md`