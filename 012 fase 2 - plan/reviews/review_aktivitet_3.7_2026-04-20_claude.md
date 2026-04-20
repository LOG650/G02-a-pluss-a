# Review: Aktivitet 3.7 - Sensitivitetsanalyse
**Dato:** 20. april 2026
**Status:** Godkjent
**Reviewer:** Claude (AI-assistent)

### 1. Sammendrag
Oppfølgings-review av aktivitet 3.7 (Sensitivitetsanalyse, WBS 3.7) etter forrige gjennomgang 1. april 2026. Kildefilene er skriptet `004 data/python_skript/sensitivity_analysis.py`, figurene 13a–c og 14a–c i `006 analysis/figures/`, det nye aktivitetsdokumentet `006 analysis/milestones/M5 - Kvantitativ analyse/3.7 sensitivitetsanalyse/3.7_Sensitivitetsanalyse.md`, M5-oppsummeringen i `M5_Analyse_Oppsummering.md`, samt kapittel 8.2 i `005 report/rapport.md`. Formålet er å verifisere at de tre kritikkpunktene fra forrige review (manglende visualiseringer, manglende tolkning, AGENTS.md-formatering) er lukket, og at aktiviteten er sporbar mot 3.5/3.6/3.10/3.12 og rapporten.

### 2. Styrker
*   **Komplett visualiseringsdekning:** Seks sensitivitetsfigurer (13a/b/c og 14a/b/c) dekker kostnad og servicenivå for alle tre kategorier og gjør knekkpunktene (særlig Safety Margin Factor = 1,5 for Engelsk fiksjon) lett avlesbare.
*   **Kvalitativ fortolkning per kategori:** Hver kategori har et eget "Tolkning av funn"-avsnitt som forklarer mekanismen bak tallene (lineær Cs-respons, SL-metning for Norsk krim, Ch-drevet buffer-effekt for barnebøker), og en oppsummeringstabell (seksjon 2) løfter hovedknekkpunktene til leseren før detaljene.
*   **Metodisk transparens:** Aktivitetsdokumentet beskriver OAT-designet eksplisitt, faktorintervallene $\{0{,}5 \dots 2{,}0\}$, at $Q_{\text{opt}}$ reestimeres etter hver kostnadsendring, og den faste 1,5-multiplikatoren for *Norsk krim* – noe som adresserer reproduserbarhetskravet R2 i `requirements.json`.
*   **Reproduserbarhet og atskilt dokumentasjon:** Skriptet skriver rådata til `sensitivity_results.csv` men overskriver ikke lenger den kuraterte aktivitetsfilen, slik at kvalitative funn er trygge ved rerun. Figurgenereringen er uendret, og kjørebanen er nå riktig (`3.7 sensitivitetsanalyse` i stedet for `3.5 kvantitativ modell`).
*   **AGENTS.md-formatering:** Alle seks figurer i `3.7_Sensitivitetsanalyse.md` bruker `<div align="center">`, `width: 70%; height: auto`, `<br>` og kursiv figurtekst. Sub-labels (a/b/c) benyttes på aktivitetsnivå for å holde kategoriene adskilt.
*   **Sporbar kobling mot rapport og øvrige aktiviteter:** Kapittel 8.2 i `rapport.md` peker nå eksplisitt til aktivitetsdokumentet og skriptet, og dokumentet selv har en seksjon "Kobling mot øvrige aktiviteter" som knytter funnene til 3.5 (basis-Prophet), 3.6 (kostnadsfordeling), 3.10 (k-faktor-optimalisering) og 3.12 (scenario-analyse).

### 3. Svakheter og forbedringspotensial
Alle kritiske avvik fra 01.04-reviewen er adressert. Gjenstående observasjoner:
*   **Figurnummer-konflikter i rapporten:** `rapport.md` benytter Figur 18–23 for sensitivitetsfigurene i kapittel 8.2, mens aktivitetsdokumentet bruker 13a–c og 14a–c (samme filnavn som i `006 analysis/figures/`). Dette er en kjent konsekvens av at rapporten renummererer figurer per kapittel og er flagget i reviewene for 3.4, 3.5 og 3.6.
    *   *Anbefaling:* Håndteres samlet i renummereringsrunden før M7. Ingen handling nødvendig for aktivitet 3.7 isolert.
*   **OAT-begrensning:** Analysen varierer parametere én om gangen, noe som ikke fanger samvariasjon mellom $C_h$ og $C_s$. Dette er eksplisitt dokumentert som antagelse 3 i seksjon 6, og scenario-analysen i 3.12 dekker kombinerte parameterendringer, så begrensningen er kontrollert og kommunisert.
    *   *Anbefaling:* Ingen handling. Sammenhengen mellom 3.7 (OAT) og 3.12 (kombinert) bør forbli synlig i kapittel 8.

### 4. Konklusjon
Aktivitet 3.7 er **godkjent**. De tre anbefalingene fra forrige review er nå adressert: (1) sensitivitetsfigurer er generert, formatert og bundet til hver kategori, (2) kvalitativ fortolkning er skrevet per kategori og supplert med en hovedfunnstabell, og (3) AGENTS.md-kravene er oppfylt. I tillegg er skriptet ryddet opp (riktig utdatamappe, ikke-destruktiv oppdatering) og aktiviteten er sporbart koblet mot rapport og nabo-aktiviteter. Leveransen oppfyller krav R1 (kvantitativ metode), R2 (etterprøvbarhet) og R3 (sammenligning mot baseline) i `requirements.json`.

**Endringer i denne runden:**
1. Opprettet `006 analysis/milestones/M5 - Kvantitativ analyse/3.7 sensitivitetsanalyse/3.7_Sensitivitetsanalyse.md` som dedikert aktivitetsdokument med metodikk, hovedfunnstabell, alle seks figurer (13a/b/c, 14a/b/c), bevarte tolkningsavsnitt, antagelser og eksplisitte koblinger til 3.5, 3.6, 3.10 og 3.12.
2. Ryddet opp i `004 data/python_skript/sensitivity_analysis.py`: korrigerte `OUTPUT_DIR` til `3.7 sensitivitetsanalyse`, fjernet den destruktive markdown-skrivingen (som ville overskrive kvalitative funn ved rerun) og beholdt figurgenereringen + rådata-CSV (`sensitivity_results.csv`).
3. Slettet den utgåtte `Sensitivitetsanalyse_Resultater.md` (erstattet av det kuraterte aktivitetsdokumentet).
4. Oppdaterte `M5_Analyse_Oppsummering.md` med en lenke til det nye aktivitetsdokumentet og referanse til skriptet.
5. Utvidet `rapport.md` kapittel 8.2 med en henvisning til `3.7_Sensitivitetsanalyse.md` og `sensitivity_analysis.py`, og presiserte at analysen er en One-At-a-Time-studie rundt basisverdiene.
