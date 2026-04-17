# Review: Aktivitet 3.4 - Baseline-løsning
**Dato:** 18. april 2026
**Status:** Godkjent
**Reviewer:** Claude (AI-assistent)

### 1. Sammendrag
Vurderer leveransene for aktivitet 3.4 (Baseline-løsning, WBS 3.4) under Milepæl M5. Kildefilene er `006 analysis/milestones/M5 - Kvantitativ analyse/3.4 baseline løsning/Baseline_Resultater.md`, kopien i `006 analysis/results/Baseline_Resultater.md`, implementasjonen i `004 data/python_skript/baseline_vs_optimization.py`, samt koblingen til kapittel 6.2 i `005 report/rapport.md`. Formålet er å sikre at baselinen er tydelig definert, reproduserbar og riktig beskrevet i rapporten, slik at den fungerer som et etterprøvbart sammenligningsgrunnlag for Prophet-modellen.

### 2. Styrker
*   **Tydelig (s, Q)-metodikk:** `Baseline_Resultater.md` definerer bestillingspunkt og bestillingsmengde eksplisitt, med formler og begrunnelse for 10 % sikkerhetsmargin.
*   **Konkrete kategoriparametere:** Tabellen med $s$, $Q$, gjennomsnittlig etterspørsel og ledetid per kategori gir full sporbarhet fra treningsdata til simulering.
*   **Låste kostnadsparametere:** Lagerholds-, stockout- og bestillingskostnader er dokumentert som konstante input, noe som oppfyller krav R3 (sammenligning mot baseline) i `requirements.json`.
*   **Konsistens med M5-resultater:** Baseline-kostnadene i `M5_Sluttresultater_Simulering.md` (198 636 NOK totalt) samsvarer med tallene i rapportens resultattabell (kapittel 8.0).
*   **Reproduserbar implementasjon over alle kategorier:** `baseline_vs_optimization.py` parametriserer nå (s, Q)-simuleringen i en løkke over alle tre kategorier, med kostnadsparametere samlet i `KATEGORI_INFO`.
*   **Visualisering av (s, Q)-sykelen:** Skriptet genererer nå tre figurer (`15_baseline_sq_sykel_*.png`) som binder tallene i tabellen til faktisk lagerutvikling og bestillingstidspunkter i testperioden.

### 3. Svakheter og forbedringspotensial
Alle kritiske avvik er adressert. Gjenstående observasjoner:
*   **Duplisert dokumentasjon (med hensikt):** `Baseline_Resultater.md` er beholdt i både `006 analysis/milestones/M5 .../3.4 baseline løsning/` og `006 analysis/results/` for oversiktens skyld. Begge filer er synkronisert, med tilpassede relative figurstier.
*   **Figur-nummerering i rapporten:** `rapport.md` har enkelte duplikater i figurnummerering fra før (f.eks. «Figur 10» i både 6.1.4 og 8.1.1). De nye baseline-figurene bruker sub-labels «Figur 15a/15b/15c» for å unngå å legge til flere nye duplikater, men kolliderer fortsatt i tallet 15. En samlet renummerering av figurene bør gjøres før M8.

### 4. Konklusjon
Aktivitet 3.4 er **godkjent**. Baselinen er nå riktig beskrevet i rapporten, parametriseringen dekker alle tre kategorier, og (s, Q)-sykelen er visualisert. Dokumentasjonen oppfyller krav R3, og figurformateringen følger `AGENTS.md`.

**Endringer i denne runden:**
1. Skrev om `rapport.md` kapittel 6.2 slik at beskrivelsen speiler den faktiske (s, Q)-baselinen med formler for $\hat{D}$, $s$ og $Q$, i stedet for å fremstille den som en ren glidende-gjennomsnitt-prognose.
2. La inn tabell med kategorispesifikke baseline-parametere ($s$, $Q$, gjennomsnittlig etterspørsel og ledetid) i kapittel 6.2 for full sporbarhet mot `Baseline_Resultater.md`.
3. La til eksplisitte referanser fra rapporten til `006 analysis/results/Baseline_Resultater.md` og `004 data/python_skript/baseline_vs_optimization.py`.
4. Ryddet gjenværende språkfeil i rapport.md (kapittel 6.4, 7.0, 8.1) — flere forekomster av «we», «year», «with» og «in» som stammer fra tidligere LLM-oversettelser, ble erstattet med riktig norsk.
5. Parametriserte `baseline_vs_optimization.py` slik at skriptet nå kjører alle tre kategorier i en løkke, med kostnadsparametere definert i `KATEGORI_INFO`, og rapporterer en samlet oppsummering.
6. La til figurgenerering i skriptet – (s, Q)-sykel plottes for hver kategori og lagres som `15_baseline_sq_sykel_<kategori>.png` under `006 analysis/figures/`.
7. Inkluderte alle tre (s, Q)-figurene (Figur 15a, 15b, 15c – Engelsk fiksjon, Norske barnebøker, Norsk krim) i `rapport.md` kapittel 6.2, med kategorispesifikk tolkning for hver figur slik at rapporten står selvstendig uten å kreve vedlegg.
8. La til alle tre (s, Q)-figurene i `Baseline_Resultater.md` (begge kopier) med tilhørende observasjonstekst som binder resultatene til M5-sluttresultatene.
