# Review: Aktivitet 3.7 - Sensitivitetsanalyse
**Dato:** 01. april 2026
**Status:** Gjennomgått - Trenger utbedring

### 1. Sammendrag
Aktivitet 3.7 omfatter gjennomføring av en sensitivitetsanalyse for å vurdere hvordan endringer i kostnadsparametere (Lagerholdskostnad, Stockout-kostnad) og sikkerhetsmargin (Safety Margin Factor) påvirker totalkostnader og servicenivå for de tre produktkategoriene. Gjennomgangen er basert på skriptet `004 data/python_skript/sensitivity_analysis.py` og resultatfilen `006 analysis/milestones/M5 - Kvantitativ analyse/3.5 kvantitativ modell/Sensitivitetsanalyse_Resultater.md`.

### 2. Styrker
*   **Grundig simulering:** Skriptet bruker en realistisk lagersimulering som tar hensyn til ledetid og variabel etterspørsel basert på Prophet-prognoser.
*   **Systematisk tilnærming:** Analysen dekker alle tre hovedkategorier og varierer parametere over et bredt spekter (faktorer fra 0.5 til 2.0).
*   **Strukturert data:** Resultatene er oversiktlig presentert i tabellform, noe som gir et godt grunnlag for videre analyse.

### 3. Svakheter og forbedringspotensial
*   **Mangel på visualiseringer:** 
    *   Det mangler grafer som viser sensitiviteten visuelt (f.eks. linjediagrammer som viser kostnadsutvikling vs. servicenivå). Dette gjør det vanskelig å identifisere optimale "knekkpunkter" raskt.
    *   *Anbefaling:* Utvid `sensitivity_analysis.py` til å generere grafer (f.eks. Figur 13 og 14) og lagre disse i `006 analysis/figures/`.
*   **Manglende diskusjon og tolkning:** 
    *   Markdown-filen inneholder kun rådata i tabeller. For eksempel observeres det at for "Engelsk fiksjon" er servicenivået uendret til tross for endringer i Stockout-kostnad, noe som krever en forklaring (sannsynligvis styrt av Prophet-intervallet heller enn kostnadsmosetning).
    *   *Anbefaling:* Legg til et avsnitt "Tolkning av funn" for hver kategori i markdown-filen for å forklare de observerte trendene.
*   **Overholdelse av AGENTS.md:** 
    *   Dersom figurer legges til, må de følge prosjektets formateringskrav (midtstilling, 70% bredde, kursiv figurtekst).
    *   *Anbefaling:* Ved implementering av visualiseringer, bruk HTML-tagger som spesifisert i AGENTS.md.

### 4. Konklusjon
Aktiviteten er teknisk godt gjennomført, men leveransen er ufullstendig uten visualisering og analyse av resultatene. Kvaliteten på rådataene er høy, men for at dette skal ha verdi for sluttrapporten må funnene tolkes og presenteres grafisk. Det anbefales å oppdatere dokumentasjonen før aktiviteten godkjennes som ferdigstilt.
