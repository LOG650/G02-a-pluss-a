# Statusrapport - LOG650 Gruppe A + A

**Sist oppdatert:** 2026-04-22
**Prosjekt:** Lagerstyring og beslutningsstøtte i logistikk (ARK Bokhandel AS)
**Rapportør:** Prosjektledelsen (Astrid Alexandra Grepstad & Anne Helene Moen Haugen)

---

## 1. Kort status

**Hvor er vi nå?** Prosjektet er i Fase 4 - Resultater og rapport. Milepæl M5 (Kvantitativ analyse gjennomført) er nådd, og alle tekniske analyseaktiviteter i Fase 3 (3.1-3.12) er ferdigstilt og godkjent via interne reviews.

**Hva er gjort nylig?**
- Aktivitet 3.12 (scenario-analyse) er ferdigstilt, inkludert harmonisering av plot-legende og tabell i rapport.md (20.04.2026).
- Oppfølgings-reviews gjennomført for 3.3, 3.4, 3.5, 3.6 og 3.7 - alle godkjent med mindre merknader.
- Rapport.md er utvidet med seksjonene 8.1-8.5 (resultater, sensitivitet, optimalisering, 2026-prognoser, scenario-analyse).

**Neste steg:**
- Skrive ferdig sammendrag og abstract (kapittel 0) i rapport.md.
- Utdype diskusjonen (kapittel 9) med kobling til litteratur (Goltsos et al., Borucka, Kirmizi et al.).
- Gjennomføre samlet renummerering av figurer i rapport.md (flagget i reviews for 3.4, 3.5, 3.6, 3.7).
- Nå milepæl M6 (Tolkning og diskusjon) innen 2026-05-07.

---

## 2. Faktisk fremdrift per aktivitet

| ID | Aktivitet | Planlagt periode | Status |
| :--- | :--- | :--- | :---: |
| 1.1 | Prosjektavklaring | 2026-01-12 - 2026-02-09 | Ferdig |
| 1.2 | Godkjent proposal (M1) | 2026-02-09 - 2026-02-23 | Ferdig |
| 1.3 | Prosjektstyringsplan | 2026-02-09 - 2026-02-18 | Ferdig |
| 2.1 | Litteraturgrunnlag | 2026-02-09 - 2026-03-02 | Ferdig |
| 2.2 | Teoriramme | 2026-02-16 - 2026-03-09 | Ferdig |
| 2.3 | Metode/forskningsdesign (M3) | 2026-02-23 - 2026-03-09 | Ferdig |
| 3.1 | Dataspesifikasjon | 2026-03-09 - 2026-03-16 | Ferdig |
| 3.2 | Datagrunnlag ferdigstilt (M4) | 2026-03-09 - 2026-04-07 | Ferdig |
| 3.3 | Datadokumentasjon | 2026-03-23 - 2026-04-07 | Ferdig |
| 3.4 | Baseline-løsning | 2026-03-23 - 2026-04-02 | Ferdig |
| 3.5 | Kvantitativ modell | 2026-03-30 - 2026-04-13 | Ferdig |
| 3.6 | Analysepakke (M5) | 2026-04-06 - 2026-04-20 | Ferdig |
| 3.7 | Sensitivitetsanalyse | 2026-04-01 - 2026-04-20 | Ferdig |
| 3.8 | Utvidet Feature Engineering | 2026-04-02 - 2026-04-20 | Ferdig |
| 3.9 | Modellvalidering (Backtesting) | 2026-04-02 - 2026-04-12 | Ferdig |
| 3.10 | Optimalisering av Bestillingsregler | 2026-04-02 - 2026-04-12 | Ferdig |
| 3.11 | Prognosegenerering 2026 | 2026-04-12 - 2026-04-12 | Ferdig |
| 3.12 | Scenario-analyse | 2026-04-12 - 2026-04-20 | Ferdig |
| 4.1 | Resultatpresentasjon | 2026-04-12 - 2026-04-27 | Pågår |
| 4.2 | Diskusjon og anbefaling (M6) | 2026-04-20 - 2026-05-07 | Pågår |
| 4.3 | Fullstendig oppgaveutkast (M7) | 2026-05-07 - 2026-05-21 | Ikke startet |
| 4.4 | Reproduserbarhet/vedlegg | 2026-05-07 - 2026-05-21 | Pågår |
| 4.5 | Kvalitetssikret sluttrapport | 2026-05-21 - 2026-05-28 | Ikke startet |
| 4.6 | Endelig innlevering (M8) | 2026-05-28 - 2026-05-31 | Ikke startet |

---

## 3. Detaljert avhukingsliste - delaktiviteter

### Fase 1 - Prosjektledelse og planlegging

**1.1 Prosjektavklaring**
- [x] Identifisert tema (lagerstyring og beslutningsstøtte i bokbransjen).
- [x] Valgt fiktiv case-bedrift (ARK Bokhandel AS).
- [x] Definert sponsor, kunde og forretningscase (Alternativ B - kvantitativ modell).
- [x] Avklart behov: kombinere historiske data med kvantitative metoder.

**1.2 Godkjent proposal (M1)**
- [x] Skrevet og levert proposal til emneansvarlig.
- [x] Mottatt godkjenning 2026-02-23.

**1.3 Prosjektstyringsplan**
- [x] Utarbeidet `projectplan.md` med 12 seksjoner (sammendrag, omfang, fremdrift, risiko, saker, interessenter, ressurser, kommunikasjon, kvalitet, anskaffelser, endringskontroll, vedlegg).
- [x] Satt opp WBS med fire faser (`data/wbs.json`).
- [x] Etablert risikoregister og sakliste.
- [x] Produsert MS Project-plan (`semesteroppgave LOG650.mpp`) og PDF/DOCX-versjon av styringsplanen.

### Fase 2 - Teori og metode

**2.1 Litteraturgrunnlag**
- [x] Gjennomgått relevant litteratur fra siste 5 år (Goltsos et al. 2022, Borucka 2023, Haque et al. 2023, Kirmizi et al. 2024, m.fl.).
- [x] Identifisert kunnskapsgap: manglende kobling mellom prognosering og lagerstyring.
- [x] Skrevet kapittel 2.0 i rapport.md (Litteratur).

**2.2 Teoriramme**
- [x] Beskrevet stasjonaritet og differensiering (3.1).
- [x] Beskrevet additive modeller og Prophet (3.2).
- [x] Beskrevet lagerstyringsteori - EOQ, ROP, sikkerhetslager (3.3).
- [x] Plassert egen problemstilling i lys av teorien.

**2.3 Metode og forskningsdesign (M3)**
- [x] Etablert kvantitativt forskningsparadigme med todelt design (Prophet-prognose + EOQ/ROP-optimalisering).
- [x] Definert 80/20 trenings-/testsplitt og backtesting-metodikk.
- [x] Begrunnet valg av Prophet med fire konkrete egenskaper koblet til datasettets behov.
- [x] Spesifisert kampanjeidentifisering via Z-score residualanalyse.
- [x] Dokumentert i `forskningsdesign.md` og rapport.md kapittel 5.0.
- [x] Rettet språkfeil i rapportkapittel 5.1 og lagt til paradigme-beskrivelse (etter review 14.04.2026).

### Fase 3 - Data og analyse

**3.1 Dataspesifikasjon**
- [x] Definert nødvendige variabler: dato, kategori, salg, etterspørsel, lagerbeholdning, kostnader, ledetid.
- [x] Valgt tre bokkategorier: Engelsk fiksjon, Norsk krim, Norske barnebøker (ulike etterspørselsmønstre).
- [x] Fastsatt tidsrekkeperiode (2021-2025) for historiske data.

**3.2 Datagrunnlag ferdigstilt (M4)**
- [x] Utviklet datagenerator for simulerte ERP-data.
- [x] Kalibrert sesongmønstre mot kjente trender i bokbransjen.
- [x] Produsert masterdatasett `master_data_vasket.csv` med alle nøkkelkolonner.
- [x] Milepæl M4 nådd 2026-04-07.

**3.3 Datadokumentasjon**
- [x] Skrevet `Data_Beskrivelse.md` med variabeloversikt og antagelser.
- [x] Generert 9 figurer (sesongvariasjoner, stockouts, kategorifordeling, svinn).
- [x] Lagt til kvantitative *Funn*-linjer under hver figur.
- [x] AGENTS.md-formatering (midtstilt, `width: 70%`, kursiv figurtekst).
- [x] Dokumentert antagelser med eksplisitte *Konsekvens*-linjer.
- [x] Inkludert som Vedlegg D i sluttrapporten.

**3.4 Baseline-løsning**
- [x] Implementert (s, Q)-baseline i `baseline_vs_optimization.py` med løkke over alle tre kategorier.
- [x] Dokumentert bestillingspunkt (s), bestillingsmengde (Q), sikkerhetsmargin (10%) per kategori.
- [x] Låst kostnadsparametere (Ch, Cs, bestillingskostnad) som konstante input.
- [x] Generert visualiseringer av (s, Q)-sykelen (Figur 15a/b/c).
- [x] Skrevet kapittel 6.2 i rapport.md med formler og kategorispesifikke tabeller.
- [x] Baseline-totalkostnad verifisert: 198 636 NOK (konsistent med M5-resultater).

**3.5 Kvantitativ modell**
- [x] Implementert Prophet-modellen i `prophet_analysis.py` med helligdagsvinduer (jul, påske, skolestart).
- [x] Generert komponentfigurer per kategori (trend, sesong, helligdag).
- [x] Rapportert trend-endring og sesongamplitude per kategori.
- [x] Skrevet kapittel 6.1 i rapport.md med matematisk beskrivelse av g(t), s(t), h(t), ε_t.
- [x] Begrunnet valg av Prophet fremfor SARIMA (kapittel 6.1.5).
- [x] Opprettet dedikert `3.5_Kvantitativ_Modell.md` med kobling til 3.4 og 3.8.

**3.6 Analysepakke (M5)**
- [x] Generert forecast-vs-actual plott (Figur 10a/b/c) for alle tre kategorier.
- [x] Generert residual-distribusjonsplott (Figur 11a/b/c).
- [x] Generert kostnadsfordelingsplott Baseline vs. Prophet (Figur 12a/b/c).
- [x] Skrevet `3.6_Analysepakke.md` med MAE-tabell og diagnostikk.
- [x] Skrevet `M5_Sluttresultater_Simulering.md` med total besparelse 20,26%.
- [x] Dokumentert kategorispesifikke funn: Norsk krim +38,1%, Engelsk fiksjon +19,6%, Norske barnebøker -7,86%.
- [x] Skrevet kapittel 8.0 og 8.1 i rapport.md.

**3.7 Sensitivitetsanalyse**
- [x] Implementert OAT-design i `sensitivity_analysis.py` med faktorintervall {0,5 ... 2,0}.
- [x] Reestimert Q_opt etter hver kostnadsendring.
- [x] Generert kostnadssensitivitetsfigurer (Figur 13a/b/c) og servicenivåfigurer (Figur 14a/b/c).
- [x] Skrevet kvalitativ fortolkning per kategori (lineær Cs-respons, SL-metning, Ch-buffer-effekt).
- [x] Identifisert knekkpunkt: Safety Margin Factor = 1,5 for Engelsk fiksjon.
- [x] Skrevet kapittel 8.2 i rapport.md.
- [x] Ryddet opp i skriptet (korrekt OUTPUT_DIR, ikke-destruktiv oppdatering).

**3.8 Utvidet Feature Engineering**
- [x] Identifisert kampanjer via Z-score (>1,5 std. avvik) utover normal sesong.
- [x] Inkludert kampanjer og helligdager som Prophet-features.
- [x] Implementert dynamisk helligdagskalender via `holidays.Norway(years=[2021…2026])`.
- [x] Målt forbedring: MAE redusert 27-33% og RMSE 27-33% på tvers av kategorier.
- [x] Skrevet `3.8_konklusjon.md` med komponentplott og sammenligningstabell (før/etter).

**3.9 Modellvalidering (Backtesting)**
- [x] Satt opp treningsperiode (2021-2024) og testperiode (2025).
- [x] Beregnet MAE, RMSE, MAPE og Bias per kategori.
- [x] Generert residualplott for validering.
- [x] Skrevet `3.9_validering_resultater.md` med utvidet analyse av Engelsk fiksjon.
- [x] Bias-verdier brukt som input til 3.10 (bias-justering).

**3.10 Optimalisering av Bestillingsregler**
- [x] Beregnet eksakte bias-verdier fra 3.9 og implementert bias-justering.
- [x] Fastsatt kategori-spesifikke sikkerhetsfaktorer (k): Norsk krim k=1,8, lavere for stabile kategorier.
- [x] Estimert kampanjeløft basert på funn fra 3.7 og 3.8.
- [x] Produsert `3.10_optimalisering_oppsummering.md` som kobler k til Ch/Cs-balansen.
- [x] Skrevet kapittel 8.3 i rapport.md.

**3.11 Prognosegenerering 2026**
- [x] Generert etterspørselsprognoser for hele 2026 for alle tre kategorier.
- [x] Integrert bias-justering (fra 3.9) og dynamisk sikkerhetslager (fra 3.10).
- [x] Produsert operasjonell CSV `prognoser_2026_alle_kategorier.csv` (kolonner: `yhat_adj`, `Safety_Stock`, `Order_Up_To`).
- [x] Generert visualiseringer av sikkerhetslagersoner med sesongvariasjon og usikkerhetsbånd.
- [x] Skrevet kapittel 8.4 i rapport.md.

**3.12 Scenario-analyse**
- [x] Definert Scenario A (kampanje-sjokk +50% løft) og Scenario B (kostnads-sjokk, +/- 20% sikkerhetslager).
- [x] Harmonisert Prophet-konfigurasjon og sigma-estimering med 3.11 for sammenlignbar baseline.
- [x] Automatisert generering av data, figurer og Markdown-rapport via `scenario_analysis_3_12.py`.
- [x] Lagt til inkrementell figurnummerering (Figur 1, 2, 3) og standardisert terminologi.
- [x] Regenerert plot med korrekt legende ("Kostnads-sjokk") og oppdatert tabell i rapport.md (20.04.2026).
- [x] Skrevet kapittel 8.5 i rapport.md.

### Fase 4 - Resultater og rapport

**4.1 Resultatpresentasjon**
- [x] Hovedtabell med Baseline vs. Prophet per kategori (kapittel 8.0).
- [x] Detaljert analyse per kategori (kapittel 8.1).
- [x] Sensitivitetsanalyse-resultater (kapittel 8.2).
- [x] Optimalisering av styringsparametere (kapittel 8.3).
- [x] 2026-prognoser (kapittel 8.4).
- [x] Scenario-analyse (kapittel 8.5).
- [ ] Samlet renummerering av figurer (flagget i reviews for 3.4-3.7).

**4.2 Diskusjon og anbefaling (M6)**
- [x] Utkast til kapittel 9 (datagrunnlagets begrensninger, ledetidssensitivitet, implementering).
- [ ] Utvide diskusjon med eksplisitt kobling til litteraturen (Goltsos et al., Borucka, Kirmizi et al.).
- [ ] Diskutere generaliserbarhet og ærlig vurdering av svakheter.
- [ ] Anbefalinger til ARK Bokhandel AS.
- [ ] Konkluderende kapittel 10 utvidet med hovedfunn og videre forskning.

**4.3 Fullstendig oppgaveutkast (M7)**
- [ ] Skrive sammendrag og abstract (kapittel 0).
- [ ] Fylle ut egenerklæring (krysse av ruter 1-6).
- [ ] Fylle ut publiseringsavtale og personvern.
- [ ] Generere komplett innholdsfortegnelse med sidetall.
- [ ] Oppgi totalt antall sider på forsiden.

**4.4 Reproduserbarhet/vedlegg**
- [x] Vedlegg A-E listet i kapittel 12.
- [x] Python-skript organisert i `004 data/python_skript/`.
- [x] Masterdatasett tilgjengelig som Vedlegg D.
- [ ] Verifisere at alle skript kjører end-to-end på ren installasjon.
- [ ] Sjekke at alle figurreferanser peker til eksisterende filer.

**4.5 Kvalitetssikret sluttrapport**
- [ ] Korrekturlesing for språk, tegnsetting og typografi.
- [ ] Sjekke alle referanser i bibliografi mot siterte verk.
- [ ] Konsistenssjekk på tall og prosenter mellom seksjoner.
- [ ] Verifisere AGENTS.md-formatering på alle figurer.
- [ ] Endelig figur-renummerering på tvers av alle kapitler.

**4.6 Endelig innlevering (M8)**
- [ ] Eksportere til PDF i henhold til HiM-mal.
- [ ] Plagiatkontroll via URKUND.
- [ ] Innlevering innen 2026-05-31.

---

## 4. Rapportstatus

| Kapittel | Innhold | Status |
| :--- | :--- | :---: |
| Forside | Tittel, forfattere, dato, sidetall | Pågår |
| Egenerklæring | Avkrysningsruter 1-6 | Påbegynt |
| Personvern | NSD-/REK-erklæring | Påbegynt |
| Publiseringsavtale | Signaturfelt, dato | Påbegynt |
| Sammendrag | Norsk sammendrag | Ikke startet |
| Abstract | Engelsk sammendrag | Ikke startet |
| Innhold | Innholdsfortegnelse | Pågår |
| 1.0 Innledning (1.1-1.4) | Problemstilling, delproblemer, avgrensinger, antagelser | Ferdig |
| 2.0 Litteratur | Etterspørselsprognosering, lagerstyring, kunnskapsgap | Ferdig |
| 3.0 Teori (3.1-3.3) | Stasjonaritet, Prophet, lagerstyringsteori | Ferdig |
| 4.0 Casebeskrivelse | ARK Bokhandel AS, produktmiks, ledetider | Ferdig |
| 5.0 Metode og data (5.1-5.2) | Metodevalg og datagrunnlag | Ferdig |
| 6.0 Modellering (6.1-6.5) | Prophet, baseline, optimalisering, antagelser, backtesting | Ferdig |
| 7.0 Analyse | Kategorispesifikke mønstre | Ferdig |
| 8.0 Resultat (8.0-8.5) | Hovedtabell, kategorianalyse, sensitivitet, optimalisering, 2026-prognoser, scenarier | Ferdig |
| 9.0 Diskusjon | Datagrunnlag, ledetid, implementering | Påbegynt |
| 10.0 Konklusjon | Hovedfunn og videre forskning | Påbegynt |
| 11.0 Bibliografi | Referanseliste (10 kilder) | Ferdig |
| 12.0 Vedlegg (A-E) | Python-skript, datasett, figurer | Ferdig |

---

## 5. Milepæler

| ID | Milepæl | Planlagt frist | Status |
| :--- | :--- | :---: | :---: |
| M1 | Problemstilling og proposal godkjent | 2026-02-23 | Oppnådd |
| M2 | Litteraturgrunnlag og teoriramme etablert | 2026-03-09 | Oppnådd |
| M3 | Forskningsdesign og metode fastsatt | 2026-03-09 | Oppnådd |
| M4 | Datagrunnlag (simulerte data) ferdigstilt | 2026-04-07 | Oppnådd |
| M5 | Kvantitativ analyse gjennomført | 2026-04-27 | Oppnådd (2026-04-20) |
| M6 | Resultater tolket og diskutert | 2026-05-07 | Planlagt |
| M7 | Fullstendig oppgaveutkast ferdigstilt | 2026-05-21 | Planlagt |
| M8 | Endelig innlevering | 2026-05-31 | Planlagt |

---

*Neste statusmøte: Mandag 2026-04-27 kl. 12:00 på Teams.*
