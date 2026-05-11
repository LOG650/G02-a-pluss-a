# Forbedringspunkter fra G01s review – konkret og i rekkefølge

**Kilde:** `G01 vurderer G02s oppgave.md`
**Dato:** 7. mai 2026
**Sortering:** Følger rapportens struktur fra topp til bunn

---

## A. Forsiden / Front matter (helt øverst i rapporten)

- [x] **Lag innholdsfortegnelse med sidetall.** ~~Dagens innholdsfortegnelse (linje 62 i `rapport.md`) mangler sidetall – legg til sidetall for hvert kapittel og delkapittel.~~ Gjort: alle hovedkapitler og underkapitler er nå klikkbare lenker. Sidetall står som `s. _` placeholder – fyll inn faktiske sidetall ved PDF-eksport.
- [x] **Legg til en eksplisitt KI-erklæring.** ~~Rapporten mangler beskrivelse av bruk av KI – legg inn et eget avsnitt (f.eks. under egenerklæringen) som beskriver hvilke KI-verktøy som er brukt og til hva.~~ Gjort: ny seksjon `### Bruk av kunstig intelligens (KI)` lagt inn mellom Personvern og Publiseringsavtale i `rapport.md`. Dekker verktøy, bruksområder og kvalitetssikring – tilpass detaljene hvis bruken har vært annerledes.
- [x] **Vurder å skrive "vi" konsekvent i egenerklæringen (egen notat, ikke fra G01).** ~~I dag står det "Jeg/vi" gjennom hele egenerklæringen (linje 16–31 i `rapport.md`). Siden dette er en gruppeoppgave kan det være ryddigere å bytte ut alle "Jeg/vi"/"min/vår" med bare "vi"/"vår".~~ Gjort: alle "Jeg/vi" → "Vi", "min/vår" → "vår" og "mitt/vårt" → "vårt" i punktene 1–6 i egenerklæringen i `rapport.md`. "Jeg/vi" i Personvern-seksjonen (linje 37) er ikke endret, da neste punkt vurderer å fjerne hele seksjonen.
- [ ] **Vurder å fjerne Personvern-seksjonen (egen notat, ikke fra G01).** Vi har krysset av at oppgaven ikke omfattes av Personopplysningsloven, og vi bruker simulerte data. Vurder om hele underseksjonen "Personvern" (linje 33–40) kan fjernes – eller om den må stå fordi den er en del av den obligatoriske malen fra HiM.

## A2. Overordnede grep som går på tvers av rapporten

Disse er hentet fra "Hovedfunn" i G01s helhetsinntrykk og påvirker flere kapitler samtidig.

- [x] **Tydeliggjør skillet mellom simulerte data og antagelser.** ~~Antagelsene står i 1.4, mens datasettet beskrives i 5.2 – sørg for at det er krystallklart hva som er rene modellforutsetninger (antagelser) og hva som er simulert datagrunnlag. Vurder å krysshenvise mellom 1.4 og 5.2, eller å lage en oppsummeringstabell.~~ Gjort: (1) 1.4 omstrukturert med to underkategorier (datagrunnlag vs. modell/domene). (2) 5.2 utvidet med eksplisitt "simulert", variabelliste, krysshenvisninger til 1.4 og 5.1, og en oppsummeringstabell som mapper hvert element til type og rapportseksjon. (3) Feilaktig referanse på linje 236 (sikkerhetslager) korrigert fra 1.4 til 6.4.
- [x] **Sammenlign modeller eksplisitt og vis mer kritisk refleksjon.** ~~Reviewen påpeker generelt for lite modellsammenligning og kritisk refleksjon. Konkretisering ligger i punktene under kap. 2/3 (vurder styrker/svakheter ved modeller) og kap. 6 (forklar manglende SARIMA-sammenligning) – men tenk gjennom om det også bør utvides i diskusjonen (kap. 9).~~ Gjort: (1) Ny seksjon i kap. 2 ("Sammenliknende styrker og svakheter ved modellene") som dekker SARIMA, Prophet, ML/hybrid og klassiske lagerstyringsmodeller. (2) Nytt avsnitt på slutten av 3.2 om Prophets teoretiske svakheter ift. SARIMA. (3) Nytt avsnitt på slutten av 6.1.5 som eksplisitt forklarer hvorfor empirisk SARIMA-sammenligning ikke ble gjort. Diskusjonen i 9.4–9.5 hadde allerede god kritisk refleksjon (særlig 9.5 #4 om SARIMA og bias-overfit), så den er ikke endret. **NB:** dette dekker også senere punkter i seksjon C (kritikk i kap. 2/3) og F (SARIMA-forklaring i 6) – kryss av/slett dem også.

## B. Kapittel 1 – Innledning

- [x] **Spiss åpningen mot ARK / bokbransjen.** ~~Erstatt det generiske om "forsyningskjede" med et mer konkret innledningsavsnitt som tar utgangspunkt i ARK Bokhandel og bokbransjens særtrekk.~~ Gjort: ny åpning av 1.0 starter med bokbransjens særtrekk (skolestart-topp for barnebøker, påske for krim, jul, BookTok-trender, importerte engelske bøker), forankrer ARKs konkrete situasjon (flere utsalgssteder, lost-sales-mekanikk med konkurrent/e-bok), og navngir de tre kategoriene eksplisitt i andre avsnitt.
- [x] **Snevre inn bruken av "forsyningskjede".** ~~Begrepet er for bredt – bytt det ut eller presiser at fokuset er på lager- og bestillingsbeslutninger i detaljhandelen.~~ Dekket av punktet over: ordet er fjernet fra innledningen. Det forekommer fortsatt på linje 170 i kap. 2, men der refererer det til Boruckas (2023) studie og er kontekstuelt riktig.

## C. Kapittel 2 & 3 – Litteratur og teori

- [ ] **Oppdater eldre kilder.** Gå gjennom referanselisten og bytt ut/utfyll kilder som er eldre enn 5 år der nyere alternativer finnes.
- [x] **Legg til kritisk vurdering av modellene.** ~~I både litteratur- og teorikapittelet: skriv inn korte avsnitt om styrker og svakheter ved Prophet, SARIMA, EOQ osv. – ikke bare beskriv dem.~~ Dekket av A2-punkt 2: ny seksjon "Sammenliknende styrker og svakheter ved modellene" i kap. 2 + tilsvarende avsnitt på slutten av 3.2.
- [x] **Gjør teorikapittelet mer lesbart.** ~~Reduser tettheten av matematiske notasjoner, eller suppler hver formel med en setning som forklarer hva den betyr i praksis (slik at lesere uten LaTeX-kjennskap henger med).~~ Gjort: lagt til en kort, plain-norsk "i praksis"-setning etter de mest kryptiske formlene i kap. 3: differensiering (3.1), ADF-regresjonen (3.1.1), Prophet-dekomponeringen (3.2), bestillingspunktet og sikkerhetslageret (3.3.1) og totalkostnadsformelen (3.3.3). CSL-formelen (3.3.2) hadde allerede en plain-språk-forklaring rett etterpå og er ikke endret.

## D. Kapittel 4 – Casebeskrivelse

- [ ] **Tydeliggjør at hovedfiguren viser aggregerte tall.** Skriv eksplisitt i figurteksten at etterspørsel, salg og lagerbeholdning er aggregert på tvers av de tre kategoriene.
- [ ] **Innfør figurnummerering.** Gå gjennom hele rapporten og nummerer figurer per kapittel (Figur 4.1, 4.2, …, Figur 6.1, 6.2 osv.) – og bruk disse referansene i brødteksten.

## E. Kapittel 5 – Metode og data

- [ ] **Konkretiser variabelbeskrivelsen i 5.2.** Lag en tabell eller punktliste som viser hvilke variabler datasettet inneholder (dato, kategori, salg, etterspørsel, lagerbeholdning osv.) og hvordan de er bygget opp.
- [ ] **Klargjør hva modellen trenes på.** Skriv eksplisitt om Prophet trenes på salg, etterspørsel eller begge – og hvorfor.
- [ ] **Samle valideringsforklaringen.** Slå sammen forklaringen av 80/20-splitten og backtesting til ett samlet avsnitt som viser hvordan de henger sammen.
- [ ] **Reflekter over begrensninger ved simulert data.** Legg til et kort avsnitt om at simulert datagrunnlag gir kontroll, men begrenser overførbarheten til ARKs faktiske drift.

## F. Kapittel 6 – Modellering

- [ ] **Lag en flytmodell/figur i 6.3.** Kapitlet er tett pakket med variabler og formler – legg inn en enkel figur som viser hvordan prognoseoutputen mates inn i optimaliseringsmodellen.
- [x] **Forklar hvorfor SARIMA ikke ble sammenlignet direkte.** ~~Avsnitt 6.1.5 begrunner valget av Prophet teoretisk – legg til en setning eller to om hvorfor en direkte empirisk sammenligning mot SARIMA ikke ble gjennomført.~~ Dekket av A2-punkt 2: nytt avsnitt på slutten av 6.1.5 ("Hvorfor en empirisk sammenligning mot SARIMA ikke ble gjennomført") som peker videre til 9.5 og 9.7.
- [ ] **Forstørre figurer med liten tekst.** Gå gjennom figurene i kapittel 6 og øk skriftstørrelse / akseteksting der det er for smått.

## G. Kapittel 7 & 8 – Analyse og resultat

- [ ] **Flytt forklaringen av Norske barnebøker tidligere.** Kategorien skiller seg ut – nevn det allerede tidlig i 8.1 i stedet for først i 8.1.3, slik at leseren vet hva som kommer.
- [ ] **Kort ned repetitive figurforklaringer.** Gå gjennom 8.1.1–8.1.3 og 8.2.1–8.2.3 og fjern gjentakelser; én tydelig forklaring per figur er nok.
- [ ] **Forbedre lesbarheten på Figur 16–23.** Større skrift, tydeligere akseforklaringer, og rydd opp i figurer som har for mye informasjon.

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
