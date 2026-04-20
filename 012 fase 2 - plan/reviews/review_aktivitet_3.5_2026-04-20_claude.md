# Review: Aktivitet 3.5 - Kvantitativ modell
**Dato:** 20. april 2026
**Status:** Godkjent
**Reviewer:** Claude (AI-assistent)

### 1. Sammendrag
Vurderer leveransene for aktivitet 3.5 (Kvantitativ modell, WBS 3.5) under Milepæl M5. Kildefilene er `006 analysis/milestones/M5 - Kvantitativ analyse/3.5 kvantitativ modell/` (tre `prophet_components_*.png` og nytt `3.5_Kvantitativ_Modell.md`), implementasjonen i `004 data/python_skript/prophet_analysis.py`, det overordnede M5-sammendraget i `M5_Analyse_Oppsummering.md`, samt koblingen til kapittel 6.1 i `005 report/rapport.md`. Formålet er å sikre at den opprinnelige Prophet-modellen er riktig dokumentert, reproduserbar og at den kobles tydelig til baseline (3.4) og de påfølgende videreutviklingene (3.7–3.10).

### 2. Styrker
*   **Reproduserbar implementasjon:** `prophet_analysis.py` parametriserer modellen over alle tre kategorier med eksplisitte helligdagsvinduer (jul, påske, skolestart) og genererer både komponentfigurer og en strukturert resultat-DataFrame.
*   **Kategorispesifikk nøkkeltallsoversikt:** Trend-endring og sesongamplitude er rapportert per kategori, noe som direkte forklarer hvorfor baseline-løsningen (3.4) underpresterer for *Norsk krim* (positiv trend) og *Engelsk fiksjon* (høy amplitude).
*   **Teoretisk forankring i rapporten:** Kapittel 6.1 i `rapport.md` gir en grundig matematisk beskrivelse av Prophet-dekomponeringen ($g(t)$, $s(t)$, $h(t)$, $\epsilon_t$) med formler for hver komponent, og begrunner valget fremfor SARIMA i kapittel 6.1.5.
*   **AGENTS.md-formatering:** Alle figurer i det nye `3.5_Kvantitativ_Modell.md` bruker `<div align="center">`, `width: 70%; height: auto`, `<br>` og kursiv figurtekst, i tråd med prosjektets standard.
*   **Eksplisitt kobling til 3.4 og 3.8:** Den nye resultatfilen refererer til både baseline-løsningen og utvidelsen med kampanjedeteksjon, noe som gir sporbarhet gjennom M5.

### 3. Svakheter og forbedringspotensial
Alle kritiske avvik er adressert. Gjenstående observasjoner:
*   **Figurnummer-konflikter i rapporten:** `rapport.md` har flere duplikater i figurnummerering (bl.a. Figur 10, 11, 12, 13 og 15). Dette er allerede flagget i review-en for 3.4 og bør håndteres samlet før M8 – det berører 3.5 indirekte ved at «Figur 12: Opprinnelig dekomponering» konkurrerer med «Figur 12: Kostnadsfordeling for Norsk krim» i kapittel 8.
    *   *Anbefaling:* Samlet renummerering av alle figurer i `rapport.md` gjennomføres som et eget «rydde»-pass før M7.
*   **Valgfritt – reproduserbarhet på tallene:** Tabellen med trend-endring i `rapport.md` (-4,84 %, -0,10 %, +12,70 %) kommer fra `M5_Analyse_Oppsummering.md`. Det kunne vært nevnt eksplisitt at resultatene er generert ved å kjøre `prophet_analysis.py` mot `train_data.csv`.
    *   *Anbefaling:* Den nye `3.5_Kvantitativ_Modell.md` angir nå skript og datasett; ingen handling nødvendig utover dette.

### 4. Konklusjon
Aktivitet 3.5 er **godkjent**. Den opprinnelige Prophet-modellen er nå dokumentert på aktivitetsnivå med et dedikert resultatsdokument, komponentfigurene er tilgjengelige for alle tre kategorier, og koblingen til både baseline (3.4) og videreutviklingene (3.7–3.10) er sporbar. Leveransen oppfyller krav R1 (kvantitativ metode) og R2 (etterprøvbarhet) i `requirements.json`.

**Endringer i denne runden:**
1. Opprettet `006 analysis/milestones/M5 - Kvantitativ analyse/3.5 kvantitativ modell/3.5_Kvantitativ_Modell.md` med dedikert dokumentasjon av basisversjonen av Prophet-modellen: metodikk, nøkkeltallstabell, alle tre komponentfigurer, antagelser og eksplisitte koblinger til øvrige M5-aktiviteter.
2. Rettet ødelagte bildestier i `M5_Analyse_Oppsummering.md` – `prophet_components_*.png` pekte på bare filnavn, men filene ligger i undermappen `3.5 kvantitativ modell/`. Stiene er nå URL-enkodede (`3.5%20kvantitativ%20modell/...`) slik at figurene renderes korrekt fra milepælsrotmappen.
3. Ryddet mindre typografiske feil i `M5_Analyse_Oppsummering.md` (manglende avslutning på *Notat*-linje og en løs asterisk på slutten av sensitivitetsseksjonen).
4. Utvidet `rapport.md` kapittel 6.1 med en henvisning til `3.5_Kvantitativ_Modell.md` og `prophet_analysis.py`, slik at leseren enkelt finner det fullstendige aktivitetsdokumentet og kildekoden.
