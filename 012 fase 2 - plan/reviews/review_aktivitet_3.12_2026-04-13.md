# Review: Aktivitet 3.12 Scenario-analyse 2026
**Dato:** 13. april 2026 (oppdatert 20. april 2026)
**Status:** Godkjent

### 1. Sammendrag
Gjennomgangen dekker scenario-analysen for 2026, som simulerer effekten av kampanje-sjokk og kostnads-sjokk på lagerbehovet for tre bokkategorier. Relevante filer befinner seg i mappen `006 analysis/milestones/M5 - Kvantitativ analyse/3.12 scenario-analyse/`, med kildeskript `004 data/python_skript/scenario_analysis_3_12.py` og presentasjon i `005 report/rapport.md` seksjon 8.5.

### 2. Styrker
*   **Overholdelse av AGENTS.md:** Rapporten følger de spesifikke formateringskravene for figurer (midtstilt `div`, `width: 70%`, og kursiv figurtekst).
*   **Automatiserte resultater:** Bruken av Python-skript for å generere både data, figurer og selve Markdown-rapporten sikrer konsistens mellom analyse og dokumentasjon.
*   **Tydelig metodikk:** Scenariene er godt definert med klare parametere (f.eks. +50% kampanjeløft, +/- 20% sikkerhetslager).
*   **God visualisering:** Plottene viser tydelig avviket fra baseline for begge scenarier, noe som gjør det lett å tolke risiko og behov.
*   **Konsistent baseline med 3.11:** Prophet-konfigurasjonen og sigma-estimeringen (yhat_upper − yhat) / 1.645 er identisk med prognoseskriptet i 3.11, slik at baseline-Order_Up_To er sammenlignbar på tvers av aktivitetene.

### 3. Utbedringer utført (13.04.2026)
Følgende punkter fra den opprinnelige reviewen er utbedret:
*   **Dokumentasjon av datakvalitet:** Lagt til et avsnitt i rapporten som beskriver antagelser knyttet til 2026-prognosen.
*   **Standardisert terminologi:** Endret fra "Kostnads-kutt" til "Scenario B: Kostnads-sjokk" i alle tabeller og titler.
*   **Figurnummerering:** Lagt til inkrementelle figurnummer i figurteksten (Figur 1, 2, 3).
*   **Konsistens i hovedrapport:** Oppdatert seksjon 8.5 i `005 report/rapport.md` med de nyeste tallene og riktig formatering.

### 4. Utbedringer utført (20.04.2026)
*   **Plot-legenden harmonisert:** Skriptet brukte fortsatt "Scenario B: Kostnads-kutt" i `plt.plot(...)`, mens tekst og tabeller bruker "Kostnads-sjokk". Endret til "Scenario B: Kostnads-sjokk" i `scenario_analysis_3_12.py` og regenererte alle tre PNG-filer.
*   **Tabell i rapport.md oppdatert:** Etter regenerering var Prophet-trekningen marginalt forskjellig (Engelsk fiksjon 359,7 → 360,3; Norsk krim −1,6 % → −1,5 %; Norske barnebøker 320,7 → 320,1, −1,9 % → −1,8 %). Tabellen i 8.5 er oppdatert tilsvarende slik at rapport, oppsummering og CSV samsvarer.

### 5. Konklusjon
Aktivitet 3.12 er fullstendig og ferdigstilt i henhold til prosjektets standarder. Leveransen er klar for inkludering i den endelige rapporten, og status i `schedule.json` er bekreftet som "Fullført".
