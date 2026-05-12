# Forbedringspunkter fra G01s review – konkret og i rekkefølge

**Kilde:** `G01 vurderer G02s oppgave.md`
**Dato:** 7. mai 2026
**Sortering:** Følger rapportens struktur fra topp til bunn

---

## A. Forsiden / Front matter (helt øverst i rapporten)

- [x] **Lag innholdsfortegnelse med sidetall.** ~~Dagens innholdsfortegnelse (linje 62 i `rapport.md`) mangler sidetall – legg til sidetall for hvert kapittel og delkapittel.~~ Gjort: alle hovedkapitler og underkapitler er nå klikkbare lenker. Sidetall står som `s. _` placeholder – fyll inn faktiske sidetall ved PDF-eksport.
- [x] **Legg til en eksplisitt KI-erklæring.** ~~Rapporten mangler beskrivelse av bruk av KI – legg inn et eget avsnitt (f.eks. under egenerklæringen) som beskriver hvilke KI-verktøy som er brukt og til hva.~~ Gjort: ny seksjon `### Bruk av kunstig intelligens (KI)` lagt inn mellom Personvern og Publiseringsavtale i `rapport.md`. Dekker verktøy, bruksområder og kvalitetssikring – tilpass detaljene hvis bruken har vært annerledes.
- [x] **Vurder å skrive "vi" konsekvent i egenerklæringen (egen notat, ikke fra G01).** ~~I dag står det "Jeg/vi" gjennom hele egenerklæringen (linje 16–31 i `rapport.md`). Siden dette er en gruppeoppgave kan det være ryddigere å bytte ut alle "Jeg/vi"/"min/vår" med bare "vi"/"vår".~~ Gjort: alle "Jeg/vi" → "Vi", "min/vår" → "vår" og "mitt/vårt" → "vårt" i punktene 1–6 i egenerklæringen i `rapport.md`. "Jeg/vi" i Personvern-seksjonen (linje 37) er ikke endret, da neste punkt vurderer å fjerne hele seksjonen.
- [x] **Vurder å fjerne Personvern-seksjonen (egen notat, ikke fra G01).** ~~Vi har krysset av at oppgaven ikke omfattes av Personopplysningsloven, og vi bruker simulerte data. Vurder om hele underseksjonen "Personvern" (linje 33–40) kan fjernes – eller om den må stå fordi den er en del av den obligatoriske malen fra HiM.~~ Vurdering gjort: seksjonen beholdes fordi NSD/REK-blokken er en del av HiMs obligatoriske front-matter-mal (samme nivå som egenerklæringspunktene 1–6 og publiseringsavtalen), og den dokumenterer eksplisitt konklusjonen om at oppgaven ikke omfattes av Personopplysningsloven — nyttig informasjon for sensor gitt at vi bruker simulerte data. Som oppfølging er "Jeg/vi" → "Vi" rettet på linje 37 for konsistens med egenerklæringen (punkt 3).

## A2. Overordnede grep som går på tvers av rapporten

Disse er hentet fra "Hovedfunn" i G01s helhetsinntrykk og påvirker flere kapitler samtidig.

- [x] **Tydeliggjør skillet mellom simulerte data og antagelser.** ~~Antagelsene står i 1.4, mens datasettet beskrives i 5.2 – sørg for at det er krystallklart hva som er rene modellforutsetninger (antagelser) og hva som er simulert datagrunnlag. Vurder å krysshenvise mellom 1.4 og 5.2, eller å lage en oppsummeringstabell.~~ Gjort: (1) 1.4 omstrukturert med to underkategorier (datagrunnlag vs. modell/domene). (2) 5.2 utvidet med eksplisitt "simulert", variabelliste, krysshenvisninger til 1.4 og 5.1, og en oppsummeringstabell som mapper hvert element til type og rapportseksjon. (3) Feilaktig referanse på linje 236 (sikkerhetslager) korrigert fra 1.4 til 6.4.
- [x] **Sammenlign modeller eksplisitt og vis mer kritisk refleksjon.** ~~Reviewen påpeker generelt for lite modellsammenligning og kritisk refleksjon. Konkretisering ligger i punktene under kap. 2/3 (vurder styrker/svakheter ved modeller) og kap. 6 (forklar manglende SARIMA-sammenligning) – men tenk gjennom om det også bør utvides i diskusjonen (kap. 9).~~ Gjort: (1) Ny seksjon i kap. 2 ("Sammenliknende styrker og svakheter ved modellene") som dekker SARIMA, Prophet, ML/hybrid og klassiske lagerstyringsmodeller. (2) Nytt avsnitt på slutten av 3.2 om Prophets teoretiske svakheter ift. SARIMA. (3) Nytt avsnitt på slutten av 6.1.5 som eksplisitt forklarer hvorfor empirisk SARIMA-sammenligning ikke ble gjort. Diskusjonen i 9.4–9.5 hadde allerede god kritisk refleksjon (særlig 9.5 #4 om SARIMA og bias-overfit), så den er ikke endret. **NB:** dette dekker også senere punkter i seksjon C (kritikk i kap. 2/3) og F (SARIMA-forklaring i 6) – kryss av/slett dem også.

## B. Kapittel 1 – Innledning

- [x] **Spiss åpningen mot ARK / bokbransjen.** ~~Erstatt det generiske om "forsyningskjede" med et mer konkret innledningsavsnitt som tar utgangspunkt i ARK Bokhandel og bokbransjens særtrekk.~~ Gjort: ny åpning av 1.0 starter med bokbransjens særtrekk (skolestart-topp for barnebøker, påske for krim, jul, BookTok-trender, importerte engelske bøker), forankrer ARKs konkrete situasjon (flere utsalgssteder, lost-sales-mekanikk med konkurrent/e-bok), og navngir de tre kategoriene eksplisitt i andre avsnitt.
- [x] **Snevre inn bruken av "forsyningskjede".** ~~Begrepet er for bredt – bytt det ut eller presiser at fokuset er på lager- og bestillingsbeslutninger i detaljhandelen.~~ Dekket av punktet over: ordet er fjernet fra innledningen. Det forekommer fortsatt på linje 170 i kap. 2, men der refererer det til Boruckas (2023) studie og er kontekstuelt riktig.

## C. Kapittel 2 & 3 – Litteratur og teori

- [x] **Oppdater eldre kilder.** ~~Gå gjennom referanselisten og bytt ut/utfyll kilder som er eldre enn 5 år der nyere alternativer finnes.~~ Gjort: Kartla alle 10 referansene i bibliografien — 6 var eldre enn 5-årsgrensen (2021-05-12). Endringer gjort:

  **Erstattet/oppdatert:**
  - **Chen (2020) → Chen (2021):** Working paper-versjonen er erstattet med peer-reviewed publikasjon i *Production and Operations Management*, 30(5), 1365–1385, DOI 10.1111/poms.13326 (samme paper, men nå referert til den publiserte versjonen).

  **Lagt til som supplement der nyere alternativ finnes:**
  - **Ensafi et al. (2022):** Lagt inn i kap. 2 (Prophet-avsnittet) som nyere empirisk støtte — komparativ analyse av SARIMA, eksponensiell utjevning, Prophet, LSTM og CNN på sesongbasert detaljsalg. Prophet ble anbefalt som mest kostnadseffektive. *International Journal of Information Management Data Insights*, 2(1), 100058, DOI 10.1016/j.jjimei.2022.100058.
  - **Douaioui et al. (2024):** Lagt inn i kap. 2.4 (oppsummering/kunnskapsgap) som nyere systematisk gjennomgang av 119 ML/DL-baserte prognosestudier i forsyningskjeden. *Applied System Innovation*, 7(5), 93, DOI 10.3390/asi7050093.

  **Beholdt med begrunnelse (jf. G01s formulering "der nyere alternativer finnes"):**
  - *Taylor & Letham (2018)* — foundational Prophet-paper; siteres for å introdusere modellen og kan ikke erstattes.
  - *Adeyemi & Onanuga (2014)* — klassisk gjennomgang av EOQ/sikkerhetslager-teori. Nyere reviews fokuserer på ML-tilnærminger (jf. Bergsma et al. 2025 vurdert), ikke klassiske analytiske modeller, så er ikke et substitutt for denne rollen.
  - *Lewis (1997)* — klassisk lærebok-anker for grunnleggende lagerstyringsteori (ROP, kostnadsdekomponering). Ingen ny lærebok i feltet de siste 5 årene gir nyere kanonisk referanse for de samme grunnbegrepene; Goltsos et al. (2022) supplerer allerede den moderne vinklingen.
  - *Luo (2019)* — eneste industri-spesifikke kilde om reform av tradisjonelle bokhandler. Søk etter post-2021 peer-reviewed alternativer for samme tematikk (bokhandel + digital transformasjon) ga ikke treff; det generelle omnichannel-detaljhandel-feltet har bevegd seg videre, men det dekker ikke bokhandel-spesifikke styringsutfordringer.
  - *Park et al. (2020)* — eneste industri-spesifikke kilde om etterspørselsprognosering i forlagsbransjen. Søk etter post-2021 publishing-spesifikk forecasting-litteratur ga ikke treff; nyere arbeid omhandler generell detaljhandel (dekkes nå av Ensafi et al. 2022 og Douaioui et al. 2024).

  **Status:** 3 nye referanser lagt til i bibliografien (alfabetisert rekkefølge bevart), 1 oppgradert, 5 beholdt med eksplisitt begrunnelse. Litteraturkapittelet bygger nå tyngre på post-2021 kilder, særlig for Prophet-valget og ML-trenden i feltet.
- [x] **Legg til kritisk vurdering av modellene.** ~~I både litteratur- og teorikapittelet: skriv inn korte avsnitt om styrker og svakheter ved Prophet, SARIMA, EOQ osv. – ikke bare beskriv dem.~~ Dekket av A2-punkt 2: ny seksjon "Sammenliknende styrker og svakheter ved modellene" i kap. 2 + tilsvarende avsnitt på slutten av 3.2.
- [x] **Gjør teorikapittelet mer lesbart.** ~~Reduser tettheten av matematiske notasjoner, eller suppler hver formel med en setning som forklarer hva den betyr i praksis (slik at lesere uten LaTeX-kjennskap henger med).~~ Gjort: lagt til en kort, plain-norsk "i praksis"-setning etter de mest kryptiske formlene i kap. 3: differensiering (3.1), ADF-regresjonen (3.1.1), Prophet-dekomponeringen (3.2), bestillingspunktet og sikkerhetslageret (3.3.1) og totalkostnadsformelen (3.3.3). CSL-formelen (3.3.2) hadde allerede en plain-språk-forklaring rett etterpå og er ikke endret.

## D. Kapittel 4 – Casebeskrivelse

- [x] **Tydeliggjør at hovedfiguren viser aggregerte tall.** ~~Skriv eksplisitt i figurteksten at etterspørsel, salg og lagerbeholdning er aggregert på tvers av de tre kategoriene.~~ Gjort: figurteksten til Figur 4.1 presiserer nå "aggregert på tvers av de tre kategoriene (Norske barnebøker, Norsk krim og Engelsk fiksjon)". Tilsvarende presisering lagt til i Figur 4.2 (stockouts).
- [x] **Innfør figurnummerering.** ~~Gå gjennom hele rapporten og nummerer figurer per kapittel (Figur 4.1, 4.2, …, Figur 6.1, 6.2 osv.) – og bruk disse referansene i brødteksten.~~ Gjort: alle figurer er nummerert per kapittel — kap. 4: Figur 4.1–4.4, kap. 5: 5.1–5.4, kap. 6: 6.1–6.4 + 6.5a–6.5c, kap. 8: 8.1–8.16. Alle inntekstreferanser i kap. 4, 6, 8 og 9 er oppdatert til ny nummerering, og alt-tekster er oppdatert der de var satt.

## E. Kapittel 5 – Metode og data

- [x] **Konkretiser variabelbeskrivelsen i 5.2.** ~~Lag en tabell eller punktliste som viser hvilke variabler datasettet inneholder (dato, kategori, salg, etterspørsel, lagerbeholdning osv.) og hvordan de er bygget opp.~~ Gjort: bullet-listen i 5.2 er erstattet av en tabell med kolonnene Variabel / Type-enhet / Beskrivelse for `Dato`, `Kategori`, `Etterspørsel`, `Salg`, `Lagerbeholdning` og `Svinn`. Lagt til en presisering om at differansen `Etterspørsel − Salg` utgjør tapt salg (lost-sales), med krysshenvisning til antagelse i 1.4.
- [x] **Klargjør hva modellen trenes på.** ~~Skriv eksplisitt om Prophet trenes på salg, etterspørsel eller begge – og hvorfor.~~ Gjort: ny underseksjon "Hva Prophet-modellen trenes på" i 5.2 sier eksplisitt at modellen trenes utelukkende på `Etterspørsel` — ikke `Salg`, ikke begge — og begrunner det med lost-sales-mekanikken (stockout-perioder ville undervurdert reelt behov). Krysshenvisning til 5.1 punkt 4 for teoretisk drøfting.
- [x] **Samle valideringsforklaringen.** ~~Slå sammen forklaringen av 80/20-splitten og backtesting til ett samlet avsnitt som viser hvordan de henger sammen.~~ Gjort: avsnittet "Datapreparering og validering" i 5.2 forklarer nå valideringen som ett sammenhengende toleddet løp — først kronologisk 80/20-splitt (trening ca. 2021–2024, test 2025), deretter backtesting på testsettet med både treffsikkerhet (MAE/RMSE/MAPE) og bias-justering. Krysshenvisning til 6.5 for resultatene.
- [x] **Reflekter over begrensninger ved simulert data.** ~~Legg til et kort avsnitt om at simulert datagrunnlag gir kontroll, men begrenser overførbarheten til ARKs faktiske drift.~~ Gjort: avsnittet "Datakvalitet og begrensninger ved simulert datagrunnlag" i 5.2 er utvidet til å eksplisitt presentere både styrken (kjent "fasit" — vanskelig på reelle ERP-data) og begrensningen (fanger ikke leverandørforsinkelser, kampanjestøy, makroskift, BookTok-sjokk). Krysshenvisning til kapittel 9.

## F. Kapittel 6 – Modellering

- [x] **Lag en flytmodell/figur i 6.3.** ~~Kapitlet er tett pakket med variabler og formler – legg inn en enkel figur som viser hvordan prognoseoutputen mates inn i optimaliseringsmodellen.~~ Gjort: ny Figur 6.6 lagt inn rett etter introduksjonsavsnittet i 6.3 (før målfunksjonen), slik at leseren får visuell oversikt før formlene. Figuren viser dataflyten Historisk data → Prophet ($\hat{y}(t)$) → Bias-justering ($D_t$) → Optimaliseringsmodell ← Parametere ($C_h$, $C_s$, $L$, $SL_{mål}$) → Beslutningsvariabler ($Q_t$, $s_t$, sikkerhetslager). Generert av nytt skript `004 data/python_skript/generate_flytmodell_6_3.py` (matplotlib), output: `006 analysis/figures/16_flytmodell_prognose_optimalisering.png`. Nummeret 6.6 valgt for å unngå renummerering av eksisterende 6.1–6.5c.
- [x] **Forklar hvorfor SARIMA ikke ble sammenlignet direkte.** ~~Avsnitt 6.1.5 begrunner valget av Prophet teoretisk – legg til en setning eller to om hvorfor en direkte empirisk sammenligning mot SARIMA ikke ble gjennomført.~~ Dekket av A2-punkt 2: nytt avsnitt på slutten av 6.1.5 ("Hvorfor en empirisk sammenligning mot SARIMA ikke ble gjennomført") som peker videre til 9.5 og 9.7.
- [x] **Forstørre figurer med liten tekst.** ~~Gå gjennom figurene i kapittel 6 og øk skriftstørrelse / akseteksting der det er for smått.~~ Gjort: Vurdering av alle figurer i kap. 6 viste at Figur 6.5a–6.5c (baseline-sykler) og Figur 6.6 (flytmodell) allerede hadde god lesbarhet, mens **Figur 6.1–6.4** (Prophet `plot_components()`-output) hadde for små fonter OG engelske default-etiketter ("trend", "ds", "holidays", "yearly"). Modifisert `004 data/python_skript/enhanced_modeling_3_8.py` (Figur 6.1–6.3) og `004 data/python_skript/prophet_analysis.py` (Figur 6.4): figurstørrelsen er økt til 13×12 tommer, tick-fonter til 12 pt, aksetitler til 13 pt, suptitle til 15 pt fet, DPI til 160, og engelske aksetitler er oversatt ("Trend (enheter)", "Dato", "Helligdager / kampanjer (enheter)", "Årlig sesong (enheter)", "Dag i året"). Skriptene er kjørt på nytt — alle fire PNG-filer er regenerert. Modellparametere og output-tabeller (`forbedret_modell_resultater.csv`, `M5_Analyse_Oppsummering.md`) er ikke endret. **NB:** Tick-etikettene i sesongkomponenten ("January 1", "March 1" …) er fortsatt engelske fordi Prophet hardkoder disse i `plot_yearly()`; å oversette krever monkey-patching av Prophet — bedømt som ikke verdt innsatsen siden månedsnavn er internasjonalt lesbare.

## G. Kapittel 7 & 8 – Analyse og resultat

- [x] **Flytt forklaringen av Norske barnebøker tidligere.** ~~Kategorien skiller seg ut – nevn det allerede tidlig i 8.1 i stedet for først i 8.1.3, slik at leseren vet hva som kommer.~~ Gjort: innledningsavsnittet i 8.1 er utvidet med en foregripende setning som signaliserer hovedfunnet før kategorigjennomgangen — Norsk krim (+38,1 %) og Engelsk fiksjon (+19,6 %) gir gevinst, mens Norske barnebøker er unntaket (−7,9 %). Krysshenviser til 8.1.3 (detaljer), 8.2 (sensitivitetsanalyse) og 9.3/9.5 (drøfting), slik at leseren vet hvor full forklaring kommer.
- [x] **Kort ned repetitive figurforklaringer.** ~~Gå gjennom 8.1.1–8.1.3 og 8.2.1–8.2.3 og fjern gjentakelser; én tydelig forklaring per figur er nok.~~ Gjort: gjennomgikk hele 8.1.1–8.1.3 og 8.2.1–8.2.3. Identifiserte to konkrete gjentakelser i 8.1.1 (Norsk krim) og fjernet dem; resten av kapitlet hadde allerede stramme figurtekster.

  **Endringer (begge i 8.1.1):**
  1. *Figur 8.1*: figurteksten "Legg merke til hvordan prediksjonen fanger opp de kraftige svingningene i testdataene" gjentok body-teksten ("Prophet-modellen treffer svært godt på de ekstreme sesongtoppene"). Figurteksten kortet ned til kun "Forecast vs. Actual for Norsk krim."
  2. *Figur 8.3*: body-teksten "Figur 8.3 viser fordelingen mellom lagerholdskostnader ($C_h$) og stockout-kostnader ($C_s$) for baseline og Prophet-modellen" gjentok figurteksten "Kostnadsfordeling for Norsk krim (Baseline vs. Prophet)". Body-teksten endret til å fokusere på funnet i stedet: "Netto reduksjon i totalkostnad er på over 26 000 NOK, hovedsakelig drevet av lavere $C_s$ (Figur 8.3)."

  **Beholdt uten endring:** 8.1.2, 8.1.3, og alle 8.2-underseksjoner — figurtekstene der er allerede minimalistiske labels, og body-teksten bærer analysen uten overlapp.
- [x] **Forbedre lesbarheten på Figur 16–23.** ~~Større skrift, tydeligere akseforklaringer, og rydd opp i figurer som har for mye informasjon.~~ Gjort: G01 brukte gammel nummerering — etter renummereringen tilsvarer dette figurene i §8.1–§8.2 (Figur 8.1–8.10). Sjekket også Figur 8.11–8.16. Identifiserte tre konkrete kvalitetsproblemer og rettet alle:

  **1. Utdaterte figurnumre i bilde-titlene (gjaldt Figur 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 8.10):** Skriptene `generate_m6_visualisations.py` og `sensitivity_analysis.py` hardkodet titler som "Figur 10:", "Figur 11:", "Figur 12:", "Figur 13:", "Figur 14:" — som ikke matchet den nye nummereringen. Løsning: fjernet figurnummerprefiksene fra bilde-titlene helt (markdown-figurteksten håndterer nummereringen), så titlene viser nå bare beskrivelse + kategori, f.eks. "Forecast vs. Actual – Norsk krim".

  **2. Engelsk legendetekst i sensitivitetsfigurene (Figur 8.5, 8.6, 8.7, 8.8, 8.9, 8.10):** `test_configs`-listen i `sensitivity_analysis.py` brukte "Stockout Cost", "Holding Cost", "Safety Margin Factor" som ble vist direkte som legendetekst via seaborn `hue`-parameter. Endret til norske termer: "Stockout-kostnad", "Lagerholdskostnad", "Sikkerhetsmargin-faktor". Tilsvarende oppdatering i `scenario_analysis_3_12.py` ("−20 % Safety Stock" → "−20 % sikkerhetslager").

  **3. Ch ikke synlig i kostnadsfordeling (Figur 8.3, 8.4):** Stablede søyler ble dominert av $C_s$ (60-80k NOK) slik at $C_h$ (100-1500 NOK) ble nesten usynlig. Endret til **grupperte søyler side-ved-side** med verdiannoteringer over hver søyle, slik at både $C_h$ og $C_s$ er sammenlignbare og leselige uavhengig av størrelsesforhold.

  **Andre lesbarhetsforbedringer på samme skript-kjøring:**
  - X-aksetitler lagt til der de manglet (Figur 8.1: "Måned (testperiode 2025)"; Figur 8.5–8.10: "Multiplikator på basisverdi").
  - Font-størrelser eksplisitt satt: tittel 14 pt fet, aksetitler 12 pt, tick-labels 11 pt, legend 11 pt.
  - DPI hevet til 150 ved lagring (var default 100) for skarpere PDF-eksport.
  - Rutenett aktivert med `alpha=0.3` for alle figurer som manglet det.

  **Skript modifisert og kjørt på nytt:** `generate_m6_visualisations.py` (8.1–8.4), `sensitivity_analysis.py` (8.5–8.10), `scenario_analysis_3_12.py` (8.14–8.16). Modellparametere og output-CSV-er er ikke endret. Figur 8.11–8.13 (prognose 2026) hadde allerede god lesbarhet og er ikke endret.

## H. Kapittel 9 – Diskusjon

- [ ] **Løft frem det viktigste funnet eksplisitt.** Start 9.1 (eller lag et kort innledende avsnitt) med én tydelig setning om hva som er hovedfunnet.
- [ ] **Reduser parallelle refleksjoner.** Slå sammen overlappende resonnementer i 9.1–9.4 slik at hver underseksjon har et tydelig poeng.

## I. Kapittel 10 – Konklusjon

- [ ] **Balanser konklusjonen.** Konklusjonen er for ensidig positiv – legg inn en kort vurdering av begrensninger og hva som ikke ble løst, før de praktiske implikasjonene.

## J. Skriveflyt og formelle aspekter (gjennomgang av hele rapporten)

- [ ] **Kvalitetssikre APA-formatering.** Gå gjennom alle inntekstreferanser og bibliografien (kapittel 11) for konsistent APA-stil.
- [ ] **Vær konsistent på språk.** Velg norsk eller engelsk for fagbegreper og bruk valget konsekvent (unngå å blande "forecasting"/"prognosering" om hverandre).
- [ ] **Forklar alle forkortelser ved første forekomst.** Gå gjennom rapporten og legg til full betegnelse første gang en forkortelse brukes (EOQ, MAPE, ADF osv.).
- [ ] **Vurder/fjern interne filhenvisninger.** Henvisninger til interne filer virker lite akademiske – erstatt dem med referanser til vedlegg eller fjern dem.
- [ ] **Standardiser figurer og tabeller.** Lik formatering, fontstørrelse, fargepalett og figurtekst på tvers av rapporten (jf. malen i CLAUDE.md: midtstilt, `width: 70%`, kursiv figurtekst).
- [ ] **Bryt opp teksttunge avsnitt.** Identifiser særlig tunge passasjer (kap. 3 og 6) og del dem opp med lister, figurer eller mellomtitler.
