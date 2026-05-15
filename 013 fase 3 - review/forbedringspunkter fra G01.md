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

- [x] **Løft frem det viktigste funnet eksplisitt.** ~~Start 9.1 (eller lag et kort innledende avsnitt) med én tydelig setning om hva som er hovedfunnet.~~ Gjort: 9.1 åpner nå med en fet hovedfunn-setning som forener de tre nøkkelfunnene i én linje — 20,26 % kostnadsreduksjon, CSL fra 84,7 % til 87,2 %, og det avgjørende forbeholdet om at hele gevinsten kommer fra de to volatile kategoriene mens baseline slår Prophet for *Norske barnebøker*. Etterfølgende setning presiserer at modellens merverdi er betinget av etterspørselsstrukturen, ikke en universell egenskap. Det opprinnelige fire-nivå-avsnittet er beholdt, men koblet til den nye åpningen via "Resultatene i kapittel 8 bekrefter dermed …".
- [x] **Reduser parallelle refleksjoner.** ~~Slå sammen overlappende resonnementer i 9.1–9.4 slik at hver underseksjon har et tydelig poeng.~~ Gjort: Kartla resonnement-overlapp på tvers av 9.1–9.4. Den klareste parallellen var **trippel-referansen til Goltsos et al. (2022)** om at prognose- og lagerstyring må behandles som én integrert prosess — den dukket opp tre ganger: (1) 9.1 bullet 3 (Bias-korreksjonen), (2) 9.1 bullet 4 (Parametervalget), og (3) 9.3 paragraf 1. Konsolidert ved å la **9.3 være kanonisk hjem** (litteraturkapittelet er det naturlige stedet for den teoretiske rammen) og fjerne restatementene i 9.1:

  **Endring 1 (9.1 bullet 3):** Avsluttende setning "Dette understreker Goltsos et al. (2022) sin observasjon om at prognose- og lagerbeslutninger må behandles som én integrert tilbakekoblingssløyfe — uten backtestingen ville biasen forplantet seg uhindret inn i bestillingspunktene." → "...særlig for *Norsk krim* der modellen ellers ville underbestilt systematisk i høysesong **og spist opp store deler av den realiserte gevinsten**." Goltsos-namechecken er flyttet (implisitt) til 9.3.

  **Endring 2 (9.1 bullet 4):** Avsluttende setning "...parametervalget er like viktig som metoden – en observasjon som også støtter Goltsos et al. (2022) sitt argument om integrert behandling av prognose- og lagerstyringsbeslutninger." → "...parametervalget er like viktig som metoden." (full stopp). Hovedpoenget i bulleten — at samme rammeverk kalibreres ulikt mellom kategorier — står like sterkt uten Goltsos-restatementen.

  **Andre vurderte overlapp som ble *beholdt* (med begrunnelse):**
  - 9.1 bullet 2 og 9.4 paragraf 1 nevner begge $\sigma_d$, men fra ulike vinkler (bedre prognose → lavere $\sigma_d$ vs. metning der $\sigma_d$ blir bindende skranke) — komplementære, ikke parallelle.
  - 9.2 paragraf 1 gjentar barnebok-funnet fra 9.1-åpningen, men dette er bevisst seksjonsåpning som setter konteksten for utdypingen i 9.2 (lesere som hopper rett til 9.2 trenger orienteringen).
  - To Kirmizi (2024)-referanser (9.1 bullet 2 om $\sigma_d$ og 9.2 om hybridtilnærminger) siterer ulike poenger fra samme kilde — ikke parallelle.

  **Resultat:** Goltsos-integrasjonsargumentet står nå én gang, i 9.3 hvor det hører hjemme. 9.1 bullet 3 og 4 har fått skarpere "tydelig poeng" uten å miste substans.

## I. Kapittel 10 – Konklusjon

- [x] **Balanser konklusjonen.** ~~Konklusjonen er for ensidig positiv – legg inn en kort vurdering av begrensninger og hva som ikke ble løst, før de praktiske implikasjonene.~~ Gjort: kapittel 10 omskrevet fra ensidig positiv tre-bullet-versjon til balansert konklusjon med fem ledd i logisk rekkefølge:

  **1. Hovedfunn (paragraf 1):** Åpner med problemstillingen, deretter headline-tallene — 20,26 % kostnadsreduksjon (198 636 → 158 395 NOK) og CSL fra 84,7 % til 87,2 % i testperioden 2025.

  **2. Betinget gevinst (paragraf 2):** Eksplisitt at funnet *ikke* er uniformt — *Norsk krim* (−38,1 %) og *Engelsk fiksjon* (−19,6 %) gir besparelse, mens *Norske barnebøker* er unntaket (+7,9 % med Prophet). Konkluderer at hovedfunnet er *betinget* av etterspørselsstrukturen, ikke universelt.

  **3. Begrensninger (paragraf 3, NY):** Kort, men eksplisitt vurdering av (a) simulert datagrunnlag som ikke fanger reelle ERP-støykilder, (b) deterministisk ledetid som overvurderer gevinst for *Engelsk fiksjon*, (c) Z-score-basert kampanjeidentifisering med få observasjoner, (d) bias-korreksjon som potensielt overfit på testperioden, og (e) manglende empirisk SARIMA-sammenligning. Avslutter med eksplisitt forbehold om at tallene er "estimat på potensialet", ikke presist drifts-anslag.

  **4. Praktiske implikasjoner (paragraf 4):** Tre konkrete anbefalinger til ARK — (i) differensiert modellvalg etter etterspørselsstruktur, (ii) rullerende bias-korreksjon, (iii) kategorivis kalibrering av $k$.

  **5. Videre forskning (paragraf 5):** Fire konkrete neste skritt — reell ERP-validering, SARIMAX-sammenligning, makrovariabler (Haque et al. 2023), bredere kategoritest. Avslutter med refleksjonssetning som forener gevinst og forbehold: "metodevalg må forankres i etterspørselsstrukturen til den enkelte varegruppen — og gevinstestimatene må prøves mot reelle driftsforhold før de kan tas i bruk".

  **Rekkefølgen følger G01s eksplisitte anbefaling:** begrensninger plassert *før* praktiske implikasjoner. Konklusjonen er nå balansert uten å miste den positive substansen — modellen *virker*, men under spesifiserte betingelser og med kjente forbehold.

## J. Skriveflyt og formelle aspekter (gjennomgang av hele rapporten)

- [x] **Kvalitetssikre APA-formatering.** ~~Gå gjennom alle inntekstreferanser og bibliografien (kapittel 11) for konsistent APA-stil.~~ Gjort: Auditert alle 40+ inntekstreferanser og alle 12 bibliografi-oppføringer mot APA 7.

  **Allerede konsistent (ikke endret):**
  - Narrativ/parentetisk konjunktor: "og" i narrativ form ("Taylor og Letham (2018)", "Adeyemi og Onanuga (2014)"), "&" i parentetisk form ("(Taylor & Letham, 2018)", "(Adeyemi & Onanuga, 2014)"). Brukt konsistent i alle 6+6 forekomster.
  - "et al."-bruk for 3+ forfattere (Park, Ensafi, Haque, Goltsos, Kirmizi, Douaioui): korrekt narrativt og parentetisk.
  - Multipel-sitering med semikolon: "(Lewis, 1997; Adeyemi & Onanuga, 2014)" — APA-korrekt.
  - Alfabetisk rekkefølge i bibliografien.
  - Italik på journaltitler og volumnummer, ikke på utgavenummer eller sidetall.
  - Forfatterinitialer med punktum og mellomrom ("A. A.", "S. H.").
  - DOI-format "https://doi.org/..." brukt konsistent.

  **Inkonsistenser rettet:**

  **1. Possessiv-konstruksjon "Forfatter (Årstall) sitt …" (5 instanser i kapittel 9):** Resten av rapporten bruker ikke-possessiv narrativ form ("X (Y) påpeker/argumenterer/studerer ..."), men kapittel 9 hadde 5 lokale instanser med possessiv "sitt". Standardisert alle til ikke-possessiv:
    - Linje 928: "Kirmizi et al. (2024) sitt poeng om at ..." → "Kirmizi et al. (2024), som påpeker at ..."
    - Linje 940: "Chen (2021) sitt arbeid om datadrevet lagerstyring ... hviler implisitt ..." → "Chen (2021) studerer datadrevet lagerstyring ... — en kontekst som implisitt forutsetter ..."
    - Linje 942: "Kirmizi et al. (2024) sitt argument om at hybridtilnærminger overgår ..." → "Kirmizi et al. (2024), som argumenterer for at hybridtilnærminger overgår ..."
    - Linje 946: "Goltsos et al. (2022) sitt hovedpoeng ..." → "Hovedpoenget hos Goltsos et al. (2022) ..."
    - Linje 948: "Taylor og Letham (2018) sitt \"analyst-in-the-loop\"-paradigme ..." → "\"Analyst-in-the-loop\"-paradigmet beskrevet av Taylor og Letham (2018) ..."

  **2. Haque et al. (2023) arXiv-oppføring i bibliografien:** Den gamle formen "*arXiv preprint arXiv:2308.11939*" hadde feil italikbruk (italik skal på paper-tittel, ikke på "arXiv preprint"-stempel) og blandet to APA-stiler. Rettet til moderne APA 7-form for preprints: "*Retail demand forecasting: A comparative study for multivariate time series* (arXiv:2308.11939). arXiv. https://arxiv.org/abs/2308.11939" — paper-tittel i italik, arXiv som archive-navn uten italik, arXiv-ID i parentes etter tittel.

  **Beholdt med forbehold (kunne ikke verifiseres uten kildesjekk):**
  - *Adeyemi & Onanuga (2014):* Mangler sidetall i bibliografien (kun "*5*(22)"). Research Journal of Finance and Accounting bruker artikkelnummer-stil i noen utgaver, men uten verifisering legges ikke sidetall til.
  - *Park et al. (2020):* Mangler DOI. International Journal of Computing and Digital Systems tildeler DOI-er, men uten verifisert lookup legges det ikke til.
  - Em-dash (—) i tittelundertekst på enkelte oppføringer (Adeyemi & Onanuga; Kirmizi et al.) er beholdt slik originaltitlene foreligger; APA krever ikke konvertering til kolon hvis em-dash er originalformatet.
- [x] **Vær konsistent på språk.** ~~Velg norsk eller engelsk for fagbegreper og bruk valget konsekvent (unngå å blande "forecasting"/"prognosering" om hverandre).~~ Gjort: Auditert rapporten for blandet bruk av norske/engelske fagbegreper.

  **Allerede konsistent (ikke endret):**
  - **"prognose"/"prognosering"** brukes konsekvent norsk gjennom hele rapporten (40+ forekomster); ingen "forecasting" i brødtekst.
  - **"stockout"** brukes som lånt engelsk fagbegrep konsekvent (logistikk-jargon i Norge); kun definert med norsk forklaring i 1.4 ("Ved 'stockouts' (utsolgt-situasjoner) antas det at salget går permanent tapt").
  - **"backtesting"** brukes som lånt engelsk fagbegrep konsekvent (også vanlig i norsk finans/logistikk).
  - **"feature engineering"**, **"lost-sales"**, **"shifting demand"**, **"analyst-in-the-loop"** brukes som engelske termer i sitater eller direkte referanse til kilder — konsekvent.
  - **Norsk komma som desimalskilletegn** brukes i de aller fleste tall (20,26 %; 84,7 %; 1,8; −11,78; osv.).
  - **Kategorinavn** ("Norsk krim", "Engelsk fiksjon", "Norske barnebøker") er stor forbokstav på alle ord — konsistent som "merkenavn" for kategoriene.
  - **$C_h$ "(holding cost)" og $C_s$ "(stockout cost)"** i kapittel 6 er parentetisk engelsk glossing av norsk hovedtekst — symmetrisk og konsistent.

  **Inkonsistenser rettet (5 instanser):**

  **1. "restordrer (stockouts)" på linje 708:** Dette var både en terminologi-inkonsistens OG en teknisk feil — modellantagelsen (1.4, 5.2) er lost-sales, ikke restordre-baserte, så ordet "restordrer" motsier modellrammeverket. Rettet til "stockouts" alene: "Historikken viser hyppige og omfattende stockouts, spesielt i juni 2021 ...".

  **2. "(Safety Margin Factor)" på linje 782:** Engelsk parentetisk merkelapp etter "sikkerhetsmarginfaktoren". Denne dukket opp i et tidligere stadium da figurlabels var engelske; etter figurnorskifiseringen (jf. seksjon G/forbedringspunkt 3) er den overflødig og bare introduserer engelsk-norsk-blanding. Fjernet — teksten leser nå "...en økning i sikkerhetsmarginfaktoren til 1,5...".

  **3. Engelsk desimalpunktum (tre instanser):** Lokalt blandet med engelsk decimal-konvensjon mens resten av rapporten bruker norsk komma:
    - Linje 782: "1.5" → "1,5"
    - Linje 798: "0.8" → "0,8"
    - Linje 814: "1.2" → "1,2"

  **4. "engelsk fiksjon" liten forbokstav (to instanser):** I 46 forekomster brukes stor forbokstav som proper-noun-stil ("Engelsk fiksjon"), men to instanser hadde liten forbokstav:
    - Linje 372: "...økt etterspørsel etter engelsk fiksjon..." → "Engelsk fiksjon"
    - Linje 782: "For engelsk fiksjon observeres..." → "For Engelsk fiksjon observeres..."

  **Beholdt med forbehold:**
  - "forecast vs. actual" på linje 723 er beholdt fordi det refererer eksplisitt til en analysepakke-filsti og PNG-filnavn (`10_forecast_vs_actual_*.png`), ikke bruk av engelsk i selvstendig brødtekst.
  - "shifting demand" er beholdt i sitater fordi det refererer til Chen (2021) som bruker dette som teknisk term i originaltittelen.
- [x] **Forklar alle forkortelser ved første forekomst.** ~~Gå gjennom rapporten og legg til full betegnelse første gang en forkortelse brukes (EOQ, MAPE, ADF osv.).~~ Gjort: Auditert alle forkortelser i `rapport.md`. ADF (linje 229), CSL (linje 287), KI (linje 42) og KPI (linje 183) var allerede forklart ved første forekomst. Lagt til full betegnelse ved første forekomst for:

  - **NSD** → "Norsk senter for forskningsdata" (linje 33, front matter)
  - **REK** → "Regionale komiteer for medisinsk og helsefaglig forskningsetikk" (linje 38, front matter)
  - **SARIMA** → "Seasonal AutoRegressive Integrated Moving Average" (linje 181, kap. 2 — første forekomst). Dupliserte ekspansjoner i 3.0 (linje 215) og 6.1.5 (linje 540) fjernet.
  - **LSTM** → "Long Short-Term Memory" (linje 181)
  - **CNN** → "Convolutional Neural Network" (linje 181)
  - **ROP** → "Reorder Point" (linje 189, første forekomst i kap. 2 — flyttet definisjonen frem fra 3.3.1)
  - **EOQ** → "Economic Order Quantity" (linje 191)
  - **SARIMAX** → "SARIMA utvidet med eksogene regressorer" (linje 197). Erstattet redundant "med eksterne regressorer".
  - **ML** → "maskinlæring" / **DL** → "dyplæring" (linje 209)
  - **ERP** → "Enterprise Resource Planning" (linje 353, første forekomst i kap. 4)
  - **MAE** → "Mean Absolute Error", **RMSE** → "Root Mean Squared Error", **MAPE** → "Mean Absolute Percentage Error" (linje 411, første forekomst i kap. 5.2)
  - **AR** → "autoregressive" / **MA** → "moving average" (linje 544, 6.1.5 — eksplisitt parentetisk ekspansjon ved første standalone bruk)
  - **ARIMA** → "AutoRegressive Integrated Moving Average" (linje 656, 6.4.1)
  - **KPSS** → "Kwiatkowski-Phillips-Schmidt-Shin" (linje 658, 6.4.1)

  **Ikke forklart (vurdert som ikke nødvendig):** BookTok (egennavn på sosialt medie-fenomen, ikke akronym); $C_h$/$C_s$ (matematiske symboler definert med engelsk parentes "holding cost"/"stockout cost" der de introduseres i 6.3, ikke akronymer); ISBN (linje 153, etablert internasjonalt standardakronym i bokbransjen — ikke forklart).
- [x] **Vurder/fjern interne filhenvisninger.** ~~Henvisninger til interne filer virker lite akademiske – erstatt dem med referanser til vedlegg eller fjern dem.~~ Gjort: Identifiserte fem inntekst-henvisninger til milestone-dokumenter og Python-skript i kap. 6–8 (linje 568, 572, 612, 723, 778). Alle er nå enten erstattet med vedleggsreferanse eller fjernet:

  **Endringer:**

  1. **Linje 568 (slutt av 6.1):** Sletning av "Full dokumentasjon … finnes i `006 analysis/milestones/M5 …/3.5_Kvantitativ_Modell.md`. Implementasjonen ligger i `004 data/python_skript/prophet_analysis.py`." → "Komponentfigurene for alle tre kategorier er presentert i Figur 6.1–6.4. Implementasjonen av basisversjonen av Prophet-modellen er dokumentert i vedlegg B."

  2. **Linje 572 (6.2):** Erstattet "fra treningsdatasettet (`train_data.csv`)" → "fra treningsdatasettet (jf. seksjon 5.2 og vedlegg D)".

  3. **Linje 612 (slutt av 6.2):** Erstattet "Implementasjonen ligger i `004 data/python_skript/baseline_vs_optimization.py`, som kjører simuleringen og genererer Figur 6.5a–6.5c …" → "Implementasjonen som genererer Figur 6.5a–6.5c for alle tre kategorier, er dokumentert i vedlegg B."

  4. **Linje 723 (åpning av kap. 8):** Erstattet "…dokumentert i `006 analysis/milestones/M5 …/3.6_Analysepakke.md`, og figurene er generert av `004 data/python_skript/generate_m6_visualisations.py`." → "…presenteres i seksjon 8.1.1–8.1.3 nedenfor; det tilhørende analyseskriptet er gjengitt i vedlegg C."

  5. **Linje 778 (åpning av 8.2):** Fjernet både milestone-stien og de interne milestone-seksjonsreferansene "(3.5, 3.6, 3.10 og 3.12)" som ikke matchet rapportens egne kapittelnumre. Erstattet med ren rapport-intern krysshenvisning: "Metodikk og kategorivise nøkkelfunn presenteres i seksjon 8.2.1–8.2.3 nedenfor, med tilhørende figurer i Figur 8.5–8.10."

  **Beholdt med begrunnelse:** Vedleggslisten i kap. 12 (linje 1044–1047) nevner spesifikke filnavn (`vask_og_strukturer.py`, `final_simulation.py`, `generate_m6_visualisations.py`, `master_data_vasket.csv`) i parentes. Disse er beholdt som de er, fordi de utgjør den kanoniske vedleggsmerkingen — det er nettopp her interne filer hører hjemme i en akademisk rapport, ikke i brødteksten.

  **Verifisering:** Grep etter `\.py`, `\.csv`, `\.md\`` og mappestier (`004 data/`, `006 analysis/`, `python_skript/`) i `rapport.md` returnerer nå kun de fire vedleggsoppføringene på linje 1044–1047.
- [x] **Standardiser figurer og tabeller.** ~~Lik formatering, fontstørrelse, fargepalett og figurtekst på tvers av rapporten (jf. malen i CLAUDE.md: midtstilt, `width: 70%`, kursiv figurtekst).~~ Gjort: Auditert alle 32 figurblokker og 11 tabeller i rapporten mot malen i CLAUDE.md (`<div align="center">` + `width: 70%; height: auto;` + `<br>` + `<em>` figurtekst).

  **Status før audit:**
  - **Bredde/midtstilling/kursiv:** Allerede konsistent på tvers av alle 32 figurer (en tidligere standardisering må ha fanget dette).
  - **Fontstørrelse og fargepalett:** Allerede håndtert i seksjon F-3 ("Forstørre figurer med liten tekst") og G-3 ("Forbedre lesbarheten på Figur 16–23") — DPI hevet til 150–160, tittel 14 pt fet, aksetitler 12 pt, tick-labels 11 pt, rutenett `alpha=0.3`, norsk legende-tekst. Ingen ytterligere skript-kjøring nødvendig.

  **Inkonsistenser identifisert og rettet:**

  **1. `alt`-attributt på `<img>`:** 8 av 32 figurer (Figur 4.1–5.4 i kap. 4 og 5) hadde `alt="Figur X.Y: ..."`-attributt; de resterende 24 (Figur 6.1–8.16 i kap. 6 og 8) hadde det ikke. CLAUDE.md-malen inkluderer ikke `alt`. For å matche malen eksakt og oppnå full konsistens, fjernet `alt` fra de 8 figurene i kap. 4 og 5. Alle 32 figurer har nå identisk `<img>`-format: `<img src="..." style="width: 70%; height: auto;">`. **Trade-off:** Mister litt tilgjengelighetsmetadata, men malen i CLAUDE.md er det reviewer eksplisitt peker på, og figurnummer + figurtekst i `<em>` under bildet ivaretar samme informasjon.

  **2. Periode på slutten av figurtekst:** 3 av 32 figurtekster manglet avsluttende periode:
  - Figur 8.14: "Scenario-sammenligning for Engelsk fiksjon i 2026" → "...i 2026."
  - Figur 8.15: "Scenario-sammenligning for Norsk krim i 2026" → "...i 2026."
  - Figur 8.16: "Scenario-sammenligning for Norske barnebøker i 2026" → "...i 2026."

  De resterende 29 figurtekstene hadde allerede konsekvent avsluttende periode. Alle 32 har nå periode.

  **3. Bold-formatering på kategorinavn i tabell (linje 846–850 før, 848–852 nå):** Tabellen "Justert etterspørsel, sikkerhetslager og bestillingspunkt per kategori" hadde rene tekstnavn (`Engelsk fiksjon`), mens alle åtte andre kategoritabeller (Trend-endring, Baseline-parametre, Stasjonaritet, MAE/RMSE/MAPE, Kostnadsbesparelse, Etterspørselsjustering, Scenario) brukte fet skrift (`**Engelsk fiksjon**`). Endret til bold for konsistens. Også justert kolonnebredder i header-raden så de matcher de andre kategoritabellene visuelt.

  **Beholdt uten endring:**
  - **Tabellnummerering:** Rapporten har ikke "Tabell 6.1: ..."-numre eller tabellbildetekster — alle tabeller introduseres i brødtekst rett over. CLAUDE.md-malen spesifiserer kun figurtekst, ikke tabelltekst. Akademisk konvensjon foretrekker eksplisitt tabellnummerering, men dette er en rapport-omfattende restrukturering som ligger utenfor "standardiser eksisterende"-mandatet. Markert som mulig fremtidig forbedring.
  - **Datatabellenes alignment:** Mest brukte mønster er `:---` for kategori-kolonne og `:---:` for tallkolonner — allerede konsistent på tvers av tabellene.
  - **Datatabellenes type-bredde:** Variasjon i kolonnebredde (whitespace-padding i markdown-kildene) er kosmetisk og påvirker ikke renderet utseende.

  **Verifisering:** `grep -c '<img '` → 32, `grep -c 'alt="'` → 0. `grep '<em>Figur' | grep -vE '\.</em>'` → ingen treff (alle figurtekster ender med periode).
- [ ] **Bryt opp teksttunge avsnitt.** Identifiser særlig tunge passasjer (kap. 3 og 6) og del dem opp med lister, figurer eller mellomtitler.
