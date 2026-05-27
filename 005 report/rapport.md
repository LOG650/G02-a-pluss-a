# Lagerstyring og beslutningsstøtte i logistikk

## En kvantitativ analyse av optimal bestillingsmengde for ARK Bokhandel AS

Anne Helene Moen Hagen & Astrid Alexandra Grepstad

Totalt antall sider inkludert forsiden:      

Molde, Innleveringsdato

## Obligatorisk egenerklæring/gruppeerklæring

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre. Manglende erklæring fritar ikke studentene fra sitt ansvar.

Du/dere fyller ut erklæringen ved å klikke i ruten til høyre for den enkelte del 1-6:

1. Vi erklærer herved at vår besvarelse er vårt eget arbeid, og at vi ikke har brukt andre kilder eller har mottatt annen hjelp enn det som er nevnt i besvarelsen. [x]
2. Vi erklærer videre at denne besvarelsen:

- ikke har vært brukt til annen eksamen ved annen avdeling/universitet/høgskole innenlands eller utenlands. [x]
- ikke refererer til andres arbeid uten at det er oppgitt. [x]
- ikke refererer til eget tidligere arbeid uten at det er oppgitt. [x]
- har alle referansene oppgitt i litteraturlisten. [x]
- ikke er en kopi, duplikat eller avskrift av andres arbeid eller besvarelse. [x]

3. Vi er kjent med at brudd på ovennevnte er å betrakte som fusk og kan medføre annullering av eksamen og utestengelse fra universiteter og høgskoler i Norge, jf. Universitets- og høgskoleloven §§4-7 og 4-8 og Forskrift om eksamen §§14 og 15. [x]
4. Vi er kjent med at alle innlevere oppgaver kan bli plagiatkontrollert i URKUND, se Retningslinjer for elektronisk innlevering og publisering av studiepoenggivende studentoppgaver [x]
5. Vi er kjent med at høgskolen vil behandle alle saker hvor det forligger mistanke om fusk etter høgskolens retningslinjer for behandling av saker om fusk [x]
6. Vi har satt oss inn i regler og retningslinjer i bruk av kilder og referanser på biblioteket sine nettsider [x]

### Personvern

Har oppgaven vært vurdert av NSD (Norsk senter for forskningsdata)? [ ] ja [x] nei

- Hvis ja: Referansenummer:      
- Hvis nei: Vi erklærer at oppgaven ikke omfattes av Personopplysningsloven: [x]

Har oppgaven vært til behandling hos REK (Regionale komiteer for medisinsk og helsefaglig forskningsetikk)? [ ] ja [x] nei

- Hvis ja: Referansenummer:      

### Bruk av kunstig intelligens (KI)

I tråd med Høgskolen i Moldes retningslinjer for ansvarlig bruk av KI-verktøy, erklærer vi følgende om bruken av kunstig intelligens i arbeidet med denne oppgaven:

**KI-verktøy benyttet:** Claude (Anthropic), primært via Claude Code.

**Bruksområder:**

- Strukturering, språklig bearbeiding og korrekturlesing av rapporttekst.
- Hjelp til implementering og feilsøking av Python-kode (bl.a. Prophet-modellen, baseline-løsning, sensitivitets- og scenarioanalyse).
- Generering og forbedring av visualiseringer og figurer.
- Diskusjonspartner for faglige problemstillinger, metodevalg og tolkning av resultater.

**Kvalitetssikring og begrensninger:**

- KI er ikke benyttet til å generere kilder eller referanser uten egen verifikasjon.
- Alle modellresultater, analyser og konklusjoner er kontrollert og validert av forfatterne.
- Problemstilling, metodevalg, faglige vurderinger og endelig fortolkning av resultatene er forfatternes egne.
- Rapporten er gjennomlest og kvalitetssikret av begge forfattere før innlevering.

### Publiseringsavtale

Studiepoeng: 30
Veileder: Bård Inge Austigard Pettersen / Per Kristian Rekdal

Vi gir herved Høgskolen i Molde en vederlagsfri rett til å gjøre oppgaven tilgjengelig for elektronisk publisering: [ ] ja [x] nei

Er oppgaven båndlagt (konfidensiell)? [ ] ja [x] nei

- Hvis ja: Kan oppgaven publiseres når båndleggingsperioden er over? [ ] ja [ ] nei

Dato: 28. mars 2026

---

## Sammendrag

ARK Bokhandel AS opererer i et marked preget av sterke sesongsvingninger, der både underbestilling og overbestilling gir betydelige kostnader. Denne rapporten undersøker hvordan en prognosedrevet, kvantitativ bestillingsmodell kan redusere lagerkostnader og samtidig opprettholde høy servicegrad, gjennom en analyse av tre bokkategorier med ulik etterspørselsdynamikk: Norsk krim, Engelsk fiksjon og Norske barnebøker.

Metoden kombinerer Prophet-modellen for etterspørselsprognosering med en kvantitativ bestillingsregel basert på dynamisk sikkerhetslager, bias-korreksjon og kategorivis sikkerhetsfaktor. Modellen er trent på et simulert datasett som dekker perioden 2021–2025, og evaluert mot en baseline basert på historisk gjennomsnitt.

Resultatene viser at den prognosedrevne modellen reduserer total lagerkostnad med 20,26 % (fra 198 636 NOK til 158 395 NOK) og hever gjennomsnittlig servicegrad fra 84,7 % til 87,2 % i testperioden 2025. Gevinsten er imidlertid ikke jevnt fordelt: For Norsk krim og Engelsk fiksjon gir modellen betydelige besparelser (henholdsvis 38,1 % og 19,6 %), mens for Norske barnebøker — der etterspørselen er stabil og sesongmønsteret forutsigbart — er en enkel baseline overlegen (−7,9 %).

Hovedkonklusjonen er at en prognosedrevet modell skaper merverdi når etterspørselen har en struktur modellen er designet for å utnytte, men ikke som et universalmiddel. Studien anbefaler et tolags driftsregime der Prophet brukes for volatile eller trenddrevne kategorier, og enklere regelbaserte rutiner beholdes for stabile kategorier. Resultatene er basert på simulert data og bør valideres mot reelle ERP-data før operativ implementering.

## Abstract

ARK Bokhandel AS operates in a market characterised by strong seasonal fluctuations, where both under- and over-ordering incur substantial costs. This report investigates how a forecast-driven, quantitative ordering model can reduce inventory costs while maintaining a high service level, through an analysis of three book categories with distinct demand dynamics: Norwegian crime fiction, English fiction, and Norwegian children's books.

The method combines the Prophet model for demand forecasting with a quantitative ordering rule based on dynamic safety stock, bias correction, and category-specific safety factors. The model is trained on a simulated dataset spanning 2021–2025, and evaluated against a baseline derived from historical averages.

The results show that the forecast-driven model reduces total inventory costs by 20.26 % (from NOK 198,636 to NOK 158,395) and raises the average service level from 84.7 % to 87.2 % over the 2025 test period. The gains are, however, not evenly distributed: For Norwegian crime fiction and English fiction the model delivers substantial savings (38.1 % and 19.6 %, respectively), whereas for Norwegian children's books — where demand is stable and the seasonal pattern predictable — a simple baseline outperforms the model (−7.9 %).

The main conclusion is that a forecast-driven model creates value when demand has a structure the model is designed to exploit, but not as a universal solution. The study recommends a two-tier operating regime in which Prophet is used for volatile or trend-driven categories, while simpler rule-based procedures are retained for stable categories. The results are based on simulated data and should be validated against real ERP data prior to operational deployment.

---

## Innhold

- [**1.0 Innledning**](#10-innledning) — s. 1
  - [1.1 Problemstilling](#11-problemstilling) — s. 2
  - [1.2 Delproblemer (valgfri)](#12-delproblemer-valgfri) — s. 2
  - [1.3 Avgrensinger](#13-avgrensinger) — s. 2
  - [1.4 Antagelser](#14-antagelser) — s. 2
- [**2.0 Litteratur**](#20-litteratur) — s. 3
  - [Etterspørselsprognosering i detaljhandel og bokbransjen](#etterspørselsprognosering-i-detaljhandel-og-bokbransjen) — s. 3
  - [Lagerstyring og kostnadsoptimalisering](#lagerstyring-og-kostnadsoptimalisering) — s. 4
  - [Oppsummering og kunnskapsgap](#oppsummering-og-kunnskapsgap) — s. 5
- [**3.0 Teori**](#30-teori) — s. 5
  - [3.1 Stasjonaritet og differensiering](#31-stasjonaritet-og-differensiering) — s. 5
  - [3.2 Additive modeller og Prophet](#32-additive-modeller-og-prophet) — s. 6
  - [3.3 Lagerstyringsteori](#33-lagerstyringsteori) — s. 7
- [**4.0 Casebeskrivelse**](#40-casebeskrivelse) — s. 8
- [**5.0 Metode og data**](#50-metode-og-data) — s. 10
  - [5.1 Metode](#51-metode) — s. 10
  - [5.2 Data](#52-data) — s. 11
- [**6.0 Modellering**](#60-modellering) — s. 14
  - [6.1 Prophet-modellen for etterspørselsprognosering](#61-prophet-modellen-for-etterspørselsprognosering) — s. 14
  - [6.2 Baseline-løsning](#62-baseline-løsning) — s. 19
  - [6.3 Kvantitativ bestillingsmodell (Optimaliseringsmodell)](#63-kvantitativ-bestillingsmodell-optimaliseringsmodell) — s. 21
  - [6.4 Modellforutsetninger og antagelser](#64-modellforutsetninger-og-antagelser) — s. 23
  - [6.5 Modellvalidering og Bias-justering (Backtesting)](#65-modellvalidering-og-bias-justering-backtesting) — s. 24
- [**7.0 Analyse**](#70-analyse) — s. 24
- [**8.0 Resultat**](#80-resultat) — s. 25
  - [8.1 Detaljert analyse per kategori](#81-detaljert-analyse-per-kategori) — s. 25
  - [8.2 Sensitivitetsanalyse og robusthet](#82-sensitivitetsanalyse-og-robusthet) — s. 27
  - [8.3 Optimalisering av styringsparametere](#83-optimalisering-av-styringsparametere) — s. 30
  - [8.4 Prognoser for 2026 (Operasjonell Planlegging)](#84-prognoser-for-2026-operasjonell-planlegging) — s. 31
  - [8.5 Scenario-analyse (Robusthetstesting)](#85-scenario-analyse-robusthetstesting) — s. 32
- [**9.0 Diskusjon**](#90-diskusjon) — s. 34
  - [9.1 Tolkning av hovedfunnene](#91-tolkning-av-hovedfunnene) — s. 34
  - [9.2 Når fungerer ikke den avanserte modellen? Tilfellet Norske barnebøker](#92-når-fungerer-ikke-den-avanserte-modellen-tilfellet-norske-barnebøker) — s. 35
  - [9.3 Sammenheng med eksisterende litteratur](#93-sammenheng-med-eksisterende-litteratur) — s. 35
  - [9.4 Robusthet og modellens grenser](#94-robusthet-og-modellens-grenser) — s. 36
  - [9.5 Begrensninger ved datagrunnlag og metode](#95-begrensninger-ved-datagrunnlag-og-metode) — s. 36
  - [9.6 Implikasjoner for næringslivet og ARKs driftspraksis](#96-implikasjoner-for-næringslivet-og-arks-driftspraksis) — s. 37
  - [9.7 Generaliserbarhet og videre arbeid](#97-generaliserbarhet-og-videre-arbeid) — s. 38
- [**10.0 Konklusjon**](#100-konklusjon) — s. 38
- [**11.0 Bibliografi**](#110-bibliografi) — s. 39
- [**12.0 Vedlegg**](#120-vedlegg) — s. 40

---

<div style="page-break-after: always;"></div>

## 1.0 Innledning

Bokbransjen er preget av kraftige sesongsvingninger som få andre detaljhandelssegmenter: skolestart løfter etterspørselen etter barnebøker i august, påsken utløser en konsentrert topp for krimlitteratur, og julehandelen står for en betydelig andel av årsomsetningen i desember. Samtidig påvirkes enkeltkategorier av mer uforutsigbare trender — sosiale medier som BookTok kan på kort tid drive opp etterspørselen etter spesifikke titler, og importerte engelskspråklige bøker er eksponert for valuta- og leveringssvingninger. For en stor aktør som ARK Bokhandel AS, med flere utsalgssteder og et bredt produktspekter, gjør dette lagerstyring til et særlig krevende problem: bestiller man for lite, går salget gjerne permanent tapt fordi kunden velger en konkurrent eller en e-bok i stedet; bestiller man for mye, bindes kapital opp og marginene spises av lagerholdskostnader.

Denne rapporten undersøker hvordan kvantitative metoder kan brukes til å bestemme optimal bestillingsmengde for tre utvalgte bokkategorier hos ARK — Norsk krim, Engelsk fiksjon og Norske barnebøker — som hver representerer en distinkt etterspørselsdynamikk. Prosjektet knytter historiske salgs- og lagerdata til konkrete bestillingsbeslutninger gjennom en integrert modell, der etterspørselsprognoser fra Prophet-modellen mater inn i en kvantitativ bestillingsregel med dynamisk sikkerhetslager. Målet er å vise om en slik datadreven tilnærming gir bedre beslutningsstøtte enn enklere strategier basert på historiske gjennomsnitt.

### 1.1 Problemstilling

Hvordan kan ARK Bokhandel AS bestemme optimal bestillingsmengde for utvalgte bokkategorier, basert på historisk etterspørsel, for å redusere lagerkostnader og samtidig begrense risikoen for utsolgte varer i kortsiktig planlegging?

### 1.2 Delproblemer

For å svare på hovedproblemstillingen, er prosjektet delt inn i følgende delproblemer:

1. Hvordan identifisere og kvantifisere historiske sesongvariasjoner og trender for de valgte bokkategoriene?
2. Hvilken baseline-strategi (f.eks. historisk gjennomsnitt) representerer dagens praksis best og kan brukes som sammenligningsgrunnlag?
3. Hvordan kan en kvantitativ bestillingsmodell minimere de totale lagerrelaterte kostnadene (lagerhold vs. stockout) sammenlignet med baseline?
4. I hvilken grad er den foreslåtte modellen robust mot endringer i ledetid og kostnadsparametere?

### 1.3 Avgrensinger

Prosjektet er avgrenset på følgende områder for å sikre en målrettet analyse:

* **Tidshorisont:** Analysen fokuserer på kortsiktig lagerstyring og omfatter ikke langsiktig strategisk planlegging eller lagerkapasitetsutvidelser.
* **Detaljnivå:** Analysen begrenses til tre overordnede bokkategorier (Barnebøker, Krim og Engelsk fiksjon) og ser ikke på individuelle boktitler eller ISBN-nivå.
* **Eksterne faktorer:** Makroøkonomiske endringer, konkurrenters markedstiltak og spesifikke markedsføringskampanjer er utelatt fra modellen.
* **Metodikk:** Prosjektet baserer seg utelukkende på kvantitative metoder og inkluderer ikke kvalitative vurderinger eller manuelle justeringer foretatt av butikkansatte.

### 1.4 Antagelser

For å kunne gjennomføre analysen og modelleringen er følgende forutsetninger lagt til grunn. For å skille tydelig mellom hva som er forutsetninger om selve datagrunnlaget og hva som er forutsetninger om modellen, er antagelsene gruppert i to kategorier. Det simulerte datasettet er beskrevet i seksjon 5.2.

**Antagelser om datagrunnlaget:**

* **Representativitet:** Det antas at det simulerte datasettet speiler virkelige salgsmønstre for ARK Bokhandel AS, inkludert sesongtopper og tilfeldige variasjoner. Implikasjonen er at funn i analysen kan tolkes som indikative for ARKs faktiske drift, men med de forbeholdene som drøftes i kapittel 9.
* **Datakvalitet:** Det legges til grunn at det simulerte og vaskede datagrunnlaget er internt konsistent og gir et korrekt bilde av de historiske forholdene det skal representere (jf. seksjon 5.2).

**Antagelser om modellen og lagerstyringsdomenet:**

* **Etterspørselens natur:** Ved "stockouts" (utsolgt-situasjoner) antas det at salget går permanent tapt. Kunden antas altså å ikke vente på varen (ingen restordrer i modellen).
* **Kostnadskonstans:** Lagerholdskostnader og mangelkostnader antas å være konstante gjennom hele analyseperioden.

---

## 2.0 Litteratur

Litteraturen som danner grunnlaget for denne rapporten spenner fra klassiske teorier om lagerstyring til moderne, datadrevne tilnærminger for etterspørselsprognosering i detaljhandelen og bokbransjen. Gjennomgangen er strukturert langs prosjektets to hovedakser: (1) etterspørselsprognosering og (2) lagerstyring og kostnadsoptimalisering.

### Etterspørselsprognosering i detaljhandel og bokbransjen

Park et al. (2020) belyser utfordringene med etterspørselsprognosering spesifikt for forlags- og bokbransjen. De understreker viktigheten av å identifisere faktorer som påvirker salgsvolum for å redusere svinn og lagerholdskostnader, og viser hvordan maskinlæringsmodeller kan fange opp komplekse mønstre som tradisjonelle metoder ofte overser. Luo (2019) diskuterer i forlengelsen av dette hvordan tradisjonelle bokhandler må reformeres gjennom nye styringssystemer som utnytter stordata og nettskybaserte løsninger for å holde tritt med markedsendringer.

Taylor og Letham (2018) introduserer Prophet-modellen, en modulær additiv tidsseriemodell designet for prognosering «i stor skala». Modellen dekomponerer tidsserien i trend, sesongvariasjon og helligdagseffekter, og er utviklet for å gi intuitive parametere som analytikere uten spesialisert statistisk bakgrunn kan justere. Modellens evne til å håndtere manglende data, uteliggere og trendskift automatisk gjør den særlig egnet for detaljhandelsdata med uregelmessige sesongmønstre — som er tilfellet for ARK Bokhandel. Ensafi et al. (2022) gir nyere empirisk støtte til dette valget: i en komparativ analyse av SARIMA (Seasonal AutoRegressive Integrated Moving Average), eksponensiell utjevning, Prophet, LSTM (Long Short-Term Memory) og CNN (Convolutional Neural Network) på sesongbasert detaljsalg viste Prophet og LSTM høyest treffsikkerhet, og Prophet ble anbefalt som den mest kostnadseffektive løsningen for operativ bruk.

Haque et al. (2023) gjennomfører en komparativ studie av ulike prognosemodeller for etterspørsel i detaljhandelen, inkludert regresjonsmodeller og maskinlæringsmetoder. Et sentralt bidrag er inkluderingen av makroøkonomiske variabler — som konsumprisindeks (KPI), forbrukertillitsindeks og arbeidsledighetsrate — som forklaringsvariabler i tillegg til historiske salgsdata. Deres funn viser at modeller som kombinerer tidsseriedata med eksterne faktorer gir bedre prognosenøyaktighet, noe som støtter tilnærmingen i dette prosjektet der sesong- og helligdagseffekter inkluderes eksplisitt i Prophet-modellen. Borucka (2023) sammenligner matematiske metoder for kortsiktig etterspørselsprognosering for produkter med sterke sesongvariasjoner og utviklingstrender. Studien viser at valg av prognosemetode har direkte konsekvenser for forsyningskjeden, og at sesongbaserte metoder gir et vesentlig bedre beslutningsgrunnlag enn enkle gjennomsnitt. Denne innsikten er direkte overførbar til ARK Bokhandels situasjon, der sesongsvingningene er en av de største utfordringene for lagerstyring.

### Lagerstyring og kostnadsoptimalisering

Lewis (1997) gir et klassisk rammeverk for sammenhengen mellom etterspørselsprognoser og lagerstyring. Han skiller mellom ulike typer etterspørsel (stasjonær, sesongavhengig, trendbasert) og hvordan disse krever ulike kontrollstrategier. Chen (2021) bygger videre på dette i en moderne kontekst ved å studere datadrevet lagerstyring i miljøer med «shifting demand». Hans arbeid er særlig relevant for dette prosjektet, da det adresserer situasjoner hvor etterspørselsfordelingen endres over tid — noe som er typisk for sesongvarene hos ARK Bokhandel.

Goltsos et al. (2022) gjennomfører en omfattende litteraturstudie av samspillet mellom etterspørselsprognoser og lagerstyring, og påpeker at de to forskningsfeltene i stor grad har utviklet seg fragmentert. Prognosestudier ignorerer ofte de nedstrøms konsekvensene for lagerbeslutninger, mens lagermodeller gjerne forutsetter at etterspørselen er kjent. Forfatterne foreslår et integrasjonsrammeverk som binder de to disiplinene sammen. Denne innsikten er bærende for strukturen i vårt prosjekt, som eksplisitt kobler Prophet-prognoser til bestillingsparametere som bestillingspunkt (Reorder Point, ROP), sikkerhetslager og servicegrad.

Kirmizi et al. (2024) undersøker sikkerhetslagerstrategier gjennom en casestudie og demonstrerer at etterspørselsvariabilitet er den mest kritiske faktoren for dimensjonering av sikkerhetslager. Deres funn om at hybridtilnærminger overgår enkeltmetoder i å redusere totale lagerkostnader, forsterker argumentet for å bruke nøyaktige prognoser som input til lagermodellen — slik det gjøres i dette prosjektet. Adeyemi og Onanuga (2014) gir i tillegg en teoretisk gjennomgang av EOQ-modeller (Economic Order Quantity) og sikkerhetslagerberegninger under både deterministisk og stokastisk etterspørsel, og danner dermed et supplerende grunnlag for kostnadsvurderingene i denne rapporten.

### Sammenliknende styrker og svakheter ved modellene

For å plassere prosjektets metodevalg i et kritisk perspektiv vurderes her styrker og svakheter ved de sentrale modellgruppene som litteraturen omtaler.

**Klassiske statistiske tidsseriemodeller (SARIMA, eksponensiell utjevning):** Sterk teoretisk forankring, tolkbare parametere og god prognosenøyaktighet når serien er tilnærmet stasjonær og residualene viser tydelig autokorrelasjonsstruktur. Svakhetene er kravet til omfattende pre-prosessering (differensiering, log-transformering), sårbarhet for uteliggere, og at additive sjokk som kampanjer og bevegelige helligdager må håndteres via SARIMAX (SARIMA utvidet med eksogene regressorer) (Taylor & Letham, 2018).

**Additive modeller (Prophet):** Eksplisitt dekomponering i trend, sesong og helligdager, robusthet mot manglende observasjoner og et intuitivt parameterapparat som muliggjør "analyst-in-the-loop"-justering. Svakhetene er at modellen ikke modellerer korttidsavhengigheter (autokorrelasjon) eksplisitt, kan overtilpasse flate kategorier med stabile mønstre (jf. drøftingen av *Norske barnebøker* i kapittel 9), og krever ekstra arbeid for å integrere eksogene kovariater.

**Maskinlærings- og hybride tilnærminger (Haque et al., 2023):** Fanger komplekse, ikke-lineære sammenhenger og kan inkorporere makroøkonomiske kovariater. Svakhetene er krav om større datavolum, lavere tolkbarhet og høyere driftskompleksitet — noe som er en reell barriere i en operativ logistikkontekst.

**Klassiske lagerstyringsmodeller (EOQ, (s, Q), ROP):** Analytisk tolkbare bestillingsregler og lavt datakrav. Svakhetene er forutsetninger om deterministisk eller normalfordelt etterspørsel og konstante kostnader (Adeyemi & Onanuga, 2014); i kontekster med skiftende etterspørsel (Chen, 2021) blir disse antagelsene strenge, noe som motiverer hybride tilnærminger der fleksible prognoser mater inn i den klassiske lagerstyringsformelen — slik dette prosjektet gjør.

Avveiningen i dette prosjektet er gjort ut fra ARKs operative kontekst: tolkbarhet for innkjøpere og naturlig håndtering av helligdager er prioritert over den marginale prognosenøyaktigheten en fullt tunet maskinlæringsmodell potensielt kunne bidra med.

### Oppsummering og kunnskapsgap

Samlet sett viser litteraturen en bevegelse fra klassiske analytiske modeller (Lewis, 1997; Adeyemi & Onanuga, 2014) mot datadrevne og maskinlæringsbaserte tilnærminger (Taylor & Letham, 2018; Ensafi et al., 2022; Haque et al., 2023; Borucka, 2023). En nyere systematisk gjennomgang av 119 maskinlærings- (ML) og dyplærings- (DL) baserte prognosestudier i forsyningskjeden (Douaioui et al., 2024) bekrefter at feltet de siste fem årene domineres av modeller som integrerer eksogene variabler og eksplisitte sesongkomponenter — i tråd med tilnærmingen i dette prosjektet. Samtidig avdekkes det et vedvarende gap mellom prognoseforskning og lagerstyringsforskning (Goltsos et al., 2022). Dette prosjektet søker å adressere dette gapet ved å integrere en moderne prognosemodell (Prophet) direkte med kvantitative bestillingsbeslutninger for ARK Bokhandel AS, og dermed binde prognosekvalitet til konkrete lagerstyringsbeslutninger i en kontekst preget av sterke sesongvariasjoner.

---

## 3.0 Teori

For å håndtere etterspørselsprognosering med komplekse sesongvariasjoner og trender, kreves teorier som kan dekomponere tidsserier. Tradisjonelle modeller som SARIMA krever stasjonære data og ofte manuell parameterinnstilling, noe som kan være utfordrende med data preget av kraftige salgstopper og uregelmessige hendelser.

### 3.1 Stasjonaritet og differensiering

Et sentralt begrep i tidsserieanalyse er **stasjonaritet**. En tidsserie $\{y_t\}$ sies å være strengt stasjonær dersom dens statistiske egenskaper ikke endrer seg over tid. I praksis fokuserer man ofte på svak stasjonaritet (eller "covariance stationarity"), som krever:

1. Konstant forventningsverdi: $E[y_t] = \mu$ for alle $t$.
2. Konstant varians: $Var(y_t) = \sigma^2$ for alle $t$.
3. Autokovarians som kun avhenger av tidsforskyvningen (lag) $k$, ikke selve tidspunktet $t$.

Dersom en tidsserie har en tydelig trend eller sesongvariasjon, vil den være **ikke-stasjonær**. For å kunne anvende klassiske statistiske modeller, må dataene transformeres til en stasjonær form, vanligvis gjennom **differensiering**:
$\Delta y_t = y_t - y_{t-1}$
Hvor $\Delta y_t$ er den første-ordens differensierte serien. Med andre ord ser man på endringen fra én periode til neste i stedet for selve nivåene — en jevnt stigende trend blir da omformet til en flatere serie rundt null, som er enklere å modellere statistisk. Dersom serien fortsatt ikke er stasjonær, kan man utføre differensiering av høyere orden eller sesong-differensiering.

#### 3.1.1 Augmented Dickey-Fuller (ADF) test

For å teste om en tidsserie er stasjonær på en statistisk signifikant måte, benyttes ofte **Augmented Dickey-Fuller-testen**. Testen undersøker nullhypotesen ($H_0$) om at serien har en enhetsrot (unit root), noe som innebærer at den er ikke-stasjonær.

Testens regresjonsmodell kan uttrykkes som:
$\Delta y_t = \alpha + \beta t + \gamma y_{t-1} + \sum_{i=1}^p \delta_i \Delta y_{t-i} + \epsilon_t$
Intuisjonen bak modellen er at hvis koeffisienten $\gamma$ er negativ og signifikant, "trekkes" serien tilbake mot et stabilt nivå hver gang den vandrer bort fra det — da er den stasjonær. Er $\gamma$ derimot lik null, vandrer serien fritt uten å vende tilbake til et middelnivå. Vi tester altså om $\gamma = 0$ ($H_0$). Dersom test-statistikken er lavere enn den kritiske verdien (eller p-verdien er under signifikansnivået på 0,05), forkastes nullhypotesen til fordel for alternativhypotesen om at serien er stasjonær.

#### 3.1.2 Log-transformering

For tidsserier preget av økende varians over tid (heteroskedastisitet), benyttes ofte en logaritmisk transformasjon, $y'_t = \ln(y_t)$, for å stabilisere variansen og transformere multiplikative sesongeffekter til en additiv form. Dette kan gjøre det lettere for enkelte modeller å fange opp prosentvise endringer. I dette prosjektet benyttes de opprinnelige etterspørselsverdiene for å sikre direkte tolkbarhet i bestillingsantall (stykktall) i logistikkoperasjonene, men transformasjonen er vurdert som et verktøy for å håndtere de kraftige sesongamplitudene identifisert i analysen.

### 3.2 Additive modeller og Prophet

I nyere tid har additive modeller som Facebooks «Prophet» (Taylor & Letham, 2018) vunnet frem som et robust alternativ til modeller som krever manuell differensiering. Teorien bak Prophet baserer seg på å modellere tidsserien som en sum av tre hovedkomponenter:
$y(t) = g(t) + s(t) + h(t) + \epsilon_t$

Hvor:

- $g(t)$ er trendfunksjonen som modellerer ikke-periodiske, langsiktige endringer i tidsserienes nivå.
- $s(t)$ representerer periodiske endringer (sesongvariasjoner), modellert gjennom Fourier-rekker.
- $h(t)$ fanger opp effekten av helligdager og spesielle hendelser med kortvarig, men signifikant innvirkning.
- $\epsilon_t$ er feilleddet som representerer idiosynkratiske endringer som ikke fanges opp av modellen.

I praksis betyr dette at salgsverdien på et gitt tidspunkt splittes i fire tolkbare biter: en langsiktig trend, et gjentakende sesongmønster, helligdagseffekter og tilfeldig støy.

Til forskjell fra SARIMA-modeller, som krever at dataene er stasjonære (jf. seksjon 3.1), opererer Prophet direkte på de opprinnelige verdiene uten behov for differensiering. Modellen er designet som et «analyst-in-the-loop»-verktøy (Taylor & Letham, 2018), der intuitive parametere — som styrken på sesongkomponenten og plasseringen av trendskift — kan justeres av analytikere uten spesialisert statistikkbakgrunn. Denne egenskapen gjør Prophet egnet for praktisk beslutningsstøtte i logistikkoperasjoner, som er det overordnede målet for dette prosjektet. De matematiske detaljene for hver komponent presenteres i seksjon 6.1.

**Teoretiske avveininger mellom Prophet og SARIMA:**

De to modellene har komplementære styrker og svakheter:

- **Prophet:** Strukturelt enklere å spesifisere og krever ikke at dataene transformeres til stasjonær form. Svakheten er at modellen ikke fanger korttidsavhengigheter (autokorrelasjon) eksplisitt, og kan derfor underprestere på serier der residualene viser tydelige autokorrelerte mønstre.
- **SARIMA:** Kan gi marginalt bedre prognosenøyaktighet for serier som er nær stasjonære og uten kraftige helligdagseffekter, fordi modellen utnytter autokorrelasjonsstrukturen direkte (Lewis, 1997). Svakheten er kravet til stasjonaritet og at additive sjokk som helligdager må håndteres manuelt via eksogene regressorer.

For dette prosjektet — der både trendskift og helligdager er sentrale — vurderes Prophets fleksibilitet som mer verdifull enn SARIMAs autokorrelasjonsmodellering. Begrunnelsen for valget i operativ kontekst, samt en drøfting av hvorfor de to modellene ikke er sammenlignet empirisk på datasettet, er gitt i seksjon 6.1.5 og 9.5.

### 3.3 Lagerstyringsteori

Mens seksjon 3.1–3.2 dekker det teoretiske grunnlaget for etterspørselsprognosering, omhandler denne seksjonen teorien som knytter prognosene til konkrete lagerbeslutninger. Goltsos et al. (2022) påpeker at disse to disiplinene ofte behandles isolert i litteraturen — dette prosjektet søker å integrere dem.

#### 3.3.1 Bestillingspunkt og sikkerhetslager

I et lagerstyringssystem med kontinuerlig overvåking utløses en ny bestilling når lagerbeholdningen synker til et definert **bestillingspunkt** (Reorder Point, ROP). Bestillingspunktet må dekke forventet etterspørsel i ledetiden pluss et sikkerhetslager som beskytter mot usikkerhet (Lewis, 1997):

$ROP = \hat{D}_L + SS$

Hvor:

- $\hat{D}_L = \hat{d} \cdot L$ er forventet etterspørsel i ledetiden, med $\hat{d}$ som gjennomsnittlig etterspørsel per periode og $L$ som ledetid.
- $SS$ er sikkerhetslageret.

Praktisk talt utløses en ny bestilling så snart det er akkurat nok på lager til å dekke ventet salg under ledetiden, pluss en sikkerhetsmargin.

Sikkerhetslageret dimensjoneres ut fra ønsket beskyttelse mot etterspørselssvingninger og beregnes som:

$SS = z_\alpha \cdot \sigma_L$

Hvor:

- $z_\alpha$: Normalfordelingens fraktil (z-verdi) som svarer til ønsket servicenivå $\alpha$.
- $\sigma_L = \sigma_d \cdot \sqrt{L}$: Standardavviket for etterspørselen i ledetiden, der $\sigma_d$ er standardavviket for etterspørselen per periode.

I praksis vokser sikkerhetslageret både med ønsket servicegrad (høyere $z_\alpha$) og med hvor uforutsigbar etterspørselen er ($\sigma_L$) — strenge tilgjengelighetskrav og volatil etterspørsel krever altså begge en større buffer. Denne formuleringen forutsetter at etterspørselen er tilnærmet normalfordelt og at ledetiden er deterministisk — antagelser som er spesifisert i seksjon 6.4.

Kirmizi et al. (2024) demonstrerer at etterspørselsvariabilitet ($\sigma_d$) er den mest kritiske faktoren for dimensjonering av sikkerhetslageret. Dette understreker viktigheten av nøyaktige prognoser: jo bedre prognosene fanger opp sesongvariasjoner og trender, desto lavere blir residualvariansen, og desto mindre sikkerhetslager kreves for å oppnå samme servicenivå.

#### 3.3.2 Servicegrad

Servicegraden uttrykker sannsynligheten for at etterspørselen kan dekkes direkte fra lager i en gitt periode. I dette prosjektet benyttes **Cycle Service Level (CSL)**, definert som:

$CSL = P(\text{Etterspørsel i ledetiden} \leq ROP)$

En CSL på 95 % innebærer at etterspørselen dekkes av tilgjengelig lager i 95 av 100 bestillingssykluser. Valget av servicenivå representerer en avveining mellom lagerholdskostnader og risikoen for tapt salg — en avveining som er sentral i dette prosjektet (Adeyemi & Onanuga, 2014).

#### 3.3.3 Kostnadsstruktur i lagerstyring

Den totale relevante lagerkostnaden kan dekomponeres i to hovedkomponenter (Lewis, 1997; Adeyemi & Onanuga, 2014):

$TC = C_h \cdot \bar{I} + C_s \cdot \bar{S}$

Hvor:

- $C_h$ er lagerholdskostnaden per enhet per periode, som reflekterer kapitalbinding, lagerplass og svinn.
- $C_s$ er mangelkostnaden per enhet, som reflekterer tapt dekningsbidrag og goodwill-tap ved stockouts.
- $\bar{I}$ er gjennomsnittlig lagerbeholdning og $\bar{S}$ er gjennomsnittlig antall enheter i mangel.

Med andre ord er total lagerkostnad summen av det det koster å ligge med varer på lager og det det koster å gå tom for varer — to hensyn som trekker i hver sin retning og må balanseres.

Forholdet mellom $C_h$ og $C_s$ er avgjørende for det optimale servicenivået. Når mangelkostnaden er vesentlig høyere enn lagerholdskostnaden — som er tilfellet i bokbransjen der tapte salg er permanente (jf. seksjon 1.4) — forskyves det optimale servicenivået oppover, noe som krever større sikkerhetslager.

#### 3.3.4 Kobling mellom prognose og lagerstyring

I dette prosjektet kobles de to teoriblokkene sammen ved at Prophet-prognosene ($\hat{y}(t)$) erstatter $\hat{d}$ i beregningen av bestillingspunktet, og residualene fra modellen ($\epsilon_t$) brukes til å estimere $\sigma_d$. Denne integrasjonen er i tråd med rammeverket foreslått av Goltsos et al. (2022), der prognosekvalitet direkte påvirker lagerbeslutningens kvalitet. Den fullstendige implementeringen av denne koblingen presenteres i seksjon 6.3.

---

## 4.0 Casebeskrivelse

ARK Bokhandel AS er en av Norges største bokhandelkjeder. Selskapet opererer i et marked preget av sterke sesongsvingninger hvor etterspørselen etter ulike sjangre varierer drastisk gjennom året. For å opprettholde høy kundetilfredshet er det avgjørende at de rette bøkene er tilgjengelige når kunden ønsker dem, samtidig som man unngår unødvendig kapitalbinding i overskuddslager.

Casen fokuserer på tre spesifikke kategorier:

1. **Norske barnebøker:** En kategori med stabil etterspørsel, men med markante topper knyttet til skolestart i august og julesalget.
2. **Norsk krim:** En sjanger som er sterkt knyttet til høytider, spesielt "påskekrim" og sommerferie. Her er risikoen for tapt salg stor dersom man ikke treffer med innkjøpsvolumet før høysesong.
3. **Engelsk fiksjon:** En kategori som har vokst i popularitet, ofte drevet av trender på sosiale medier. Denne kategorien har ofte lengre ledetider da bøkene gjerne importeres, noe som gjør presise prognoser enda viktigere.

Utfordringene knyttet til disse sesongvariasjonene er tydelige når vi analyserer det historiske forholdet mellom etterspørsel og faktisk tilgjengelighet for ARK:

<div align="center">
  <img src="../006%20analysis/figures/01_ettersporsel_salg_lager.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 4.1: Sammenheng mellom etterspørsel, faktisk salg og lagerbeholdning over tid, aggregert på tvers av de tre kategoriene (Norske barnebøker, Norsk krim og Engelsk fiksjon). Legg merke til gapet mellom etterspørsel og salg i toppene.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/02_stockouts_over_tid.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 4.2: Oversikt over perioder der etterspørselen ikke kunne dekkes av tilgjengelig lager (stockouts), aggregert på tvers av de tre kategoriene.</em>
</div>

Som vist i Figur 4.1 og 4.2, oppstår de mest kritiske situasjonene i de faste salgstoppene gjennom året. Dette mønsteret gjentas på tvers av kategoriene, men med ulik timing og intensitet, noe som krever en modell som kan fange opp disse mønstrene:

<div align="center">
  <img src="../006%20analysis/figures/08_gjennomsnittlig_salg_per_maaned.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 4.3: Gjennomsnittlig salg fordelt på måneder for å identifisere faste sesongsvingninger i casen.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/09_sesongvariasjoner_salg.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 4.4: Detaljert sammenligning av sesongmønstre på tvers av de tre kategoriene som utgjør kjernen i denne analysen.</em>
</div>

Siden direkte tilgang til ARKs interne ERP-data (Enterprise Resource Planning) ikke var tilgjengelig for dette prosjektet, benyttes et simulert datasett som er designet for å etterligne disse spesifikke markedsforholdene. Modelleringen vil ta hensyn til kostnadsparametere som lagerhold og mangelkostnader for å identifisere den mest lønnsomme bestillingsstrategien.

---

## 5.0 Metode og data

### 5.1 Metode

Prosjektet følger et kvantitativt forskningsparadigme, der all analyse er basert på numeriske data og statistiske modeller. Forskningsdesignet er en simuleringsbasert case-studie med en todelt tilnærming: først etterspørselsprognosering, deretter kvantitativ bestillingsoptimalisering.

For dette prosjektet er det valgt å benytte **Prophet** som hovedmodell for etterspørselsprognosering. Valget av denne modellen er basert på en drøfting av behovene i bokbransjen og datasettets egenskaper:

**1. Robusthet mot sesongvariasjoner:**
Dataene viser sterke sesongsvingninger på tvers av alle kategorier. Prophet er designet for å håndtere sesongvariasjoner på flere nivåer (månedlig, årlig) uten behov for omfattende datatransformasjoner som differensiering.

**2. Eksplisitt håndtering av helligdager (Holiday Effects):**
Salgsmønstrene for spesielt "Norsk krim" og "Norske barnebøker" viser tydelige topper knyttet til påske, sommerferie og jul. Prophet tillater direkte inkludering av disse effektene, noe som er kritisk for å unngå "stockouts" i perioder med unormalt høy etterspørsel.

**3. Automatisk trenddeteksjon:**
Modellen identifiserer automatisk endringspunkter i trenden. Dette er relevant for å fange opp skift i popularitet for ulike sjangre, for eksempel økt etterspørsel etter Engelsk fiksjon drevet av sosiale medier (BookTok).

**4. Prediksjon på faktisk etterspørsel:**
Ved å trene modellen på feltet "Etterspørsel" i stedet for kun "Salg", sikrer vi at modellen lærer det reelle behovet i markedet, uavhengig av historiske lagerbegrensninger.

Metoden innebærer å trene modellen på historiske salgsdata (2021-2025) for å predikere etterspørselen i 2026. Resultatene vil deretter fungere som beslutningsstøtte for den kvantitative bestillingsmodellen.

### 5.2 Data

Datasettet som benyttes i denne rapporten er **simulert** salgs- og lagerdata for ARK Bokhandel AS. Reelle ERP-data fra ARK var ikke tilgjengelige, og datasettet er derfor konstruert syntetisk slik at det etterligner ARKs salgsmønstre på tvers av tre bokkategorier. Antagelsene som ligger til grunn for å bruke et simulert datagrunnlag — særlig at det er representativt for virkelige salgsmønstre og av tilstrekkelig kvalitet — er formulert eksplisitt i seksjon 1.4 ("Antagelser om datagrunnlaget").

**Innhold og struktur:**
Datasettet dekker perioden 2021–2025 og inneholder daglige observasjoner per kategori. Tabellen under viser hvordan datasettet er bygget opp:

| Variabel            | Type / enhet             | Beskrivelse                                                                              |
| ------------------- | ------------------------ | ---------------------------------------------------------------------------------------- |
| `Dato`            | Tidsstempel (YYYY-MM-DD) | Daglig observasjonstidspunkt fra 2021-01-01 til 2025-12-31.                              |
| `Kategori`        | Kategorisk (3 nivåer)   | "Norske barnebøker", "Norsk krim" eller "Engelsk fiksjon".                              |
| `Etterspørsel`   | Heltall (enheter/dag)    | Det reelle, simulerte behovet i markedet — uavhengig av lagerstatus.                    |
| `Salg`            | Heltall (enheter/dag)    | Faktisk solgt mengde, oppad begrenset av tilgjengelig lager (`Salg ≤ Etterspørsel`). |
| `Lagerbeholdning` | Heltall (enheter)        | Beholdning ved slutten av dagen, etter dagens salg og eventuelle leveranser.             |
| `Svinn`           | Heltall (enheter/dag)    | Registrert svinn på dagen (skade, retur, etc.).                                         |

Differansen mellom `Etterspørsel` og `Salg` på en gitt dag utgjør tapt salg ved stockout (lost-sales-mekanikk, jf. antagelse i 1.4).

**Hva Prophet-modellen trenes på:**
Prophet-modellen trenes **utelukkende på variabelen `Etterspørsel`** — ikke på `Salg`, og ikke på begge samtidig. Grunnen er at `Salg` er begrenset oppad av tilgjengelig lager, slik at historiske stockout-perioder ville systematisk undervurdert det reelle markedsbehovet og forplantet denne skjevheten inn i prognosen for 2026. Ved å trene på `Etterspørsel` lærer modellen det underliggende behovet i markedet, som så fungerer som input til bestillingsmodellen i kapittel 6. Den teoretiske begrunnelsen er gitt i 5.1 (punkt 4).

**Tre distinkte etterspørselsmønstre:**
De tre bokkategoriene er valgt fordi de representerer ulike markedsdynamikker, noe som gjør det mulig å teste modellens robusthet på tvers av flere typer etterspørsel:

- **Norske barnebøker:** Preget av høy frekvens og tydelige sesongvariasjoner, men med høy grad av forutsigbarhet og regelmessighet.
- **Norsk krim:** Kjennetegnes av spesifikke salgstopper knyttet til høytider som påske og sommer.
- **Engelsk fiksjon:** Viser en jevnere etterspørsel gjennom året, ofte påvirket av internasjonale trender og importtider.

**Datakvalitet og begrensninger ved simulert datagrunnlag:**
Bruken av et simulert datagrunnlag er en bevisst metodisk avveining. Styrken er at vi kjenner det sanne underliggende signalet (sesong, trend, støy) og dermed kan måle hvor godt modellen rekonstruerer det — et eksperiment som er vanskelig å gjennomføre på reelle ERP-data hvor det ikke finnes en kjent "fasit". Samtidig er kontrollen også en begrensning: simulerte data fanger ikke opp den uregelmessige støyen i reelle driftsdata, som leverandørforsinkelser, kampanjeeffekter utenfor vår parameterisering, makroøkonomiske skift, registreringsfeil eller plutselige BookTok-drevne etterspørselssjokk. Inkonsistenser oppdaget under datavasking (datoformater, manglende verdier) er håndtert for å sikre et konsistent analysegrunnlag. Implikasjonen er at modellen testes under kontrollerte betingelser, og overførbarheten av resultatene til ARKs faktiske drift må derfor vurderes med forsiktighet. Denne begrensningen diskuteres mer inngående i kapittel 9.

**Datapreparering og validering:**
Valideringsstrategien har to ledd som henger sammen. Først splittes datasettet kronologisk i en treningsdel (80 %, ca. 2021–2024) og en testdel (20 %, ca. 2025), slik at modellen kan evalueres på data den ikke har sett under trening. Treningssettet brukes til å estimere Prophet-modellens parametere, mens testsettet brukes til *backtesting* — en empirisk sammenligning av predikert mot faktisk etterspørsel i 2025. Backtestingen tjener to formål: (1) den kvantifiserer modellens treffsikkerhet (Mean Absolute Error (MAE), Root Mean Squared Error (RMSE) og Mean Absolute Percentage Error (MAPE)), og (2) den identifiserer eventuell systematisk skjevhet (bias) per kategori, som korrigeres før prognosene mates inn i bestillingsmodellen for 2026. Selve resultatene av backtestingen og den påfølgende bias-justeringen presenteres i 6.5.

**Oppsummering — datagrunnlag vs. antagelser:**

For å gjøre skillet mellom det simulerte datagrunnlaget og antagelsene som ligger til grunn for analysen tydelig, gir tabellen under en samlet oversikt over hvilke elementer som er hva, og hvor i rapporten de er beskrevet.

| Element                                           | Type                  | Beskrevet i |
| ------------------------------------------------- | --------------------- | ----------- |
| Daglige tidsserier (etterspørsel, salg, lager)   | Simulert datagrunnlag | 5.2         |
| Sesongmønstre, helligdagstopper, tilfeldig støy | Simulert datagrunnlag | 5.2         |
| Representativitet for ARKs virkelige drift        | Antagelse om data     | 1.4         |
| Datakvalitet og indre konsistens                  | Antagelse om data     | 1.4 og 5.2  |
| Lost-sales ved stockout                           | Modellantagelse       | 1.4         |
| Konstante lager- og mangelkostnader               | Modellantagelse       | 1.4         |
| Normalfordelt prognosefeil                        | Modellantagelse       | 6.4.3       |

**Beskrivelse av datagrunnlaget og tekniske visualiseringer:**

<div align="center">
  <img src="../006%20analysis/figures/03_kategori_fordeling_total.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 5.1: Fordeling av salgsvolum per kategori i det benyttede datasettet.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/04_kostnads_tradeoff.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 5.2: Teknisk analyse av forholdet mellom lagerholdskostnader og mangelkostnader.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/05_svinn_total_oversikt.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 5.3: Total oversikt over registrert svinn i datagrunnlaget.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/07_totalt_salg_per_aar.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 5.4: Utvikling i totalt salgsvolum per år i treningsdataene.</em>
</div>

---

## 6.0 Modellering

Modelleringen i dette prosjektet følger en todelt tilnærming. Først benyttes en avansert tidsseriemodell (Prophet) for å generere nøyaktige etterspørselsprognoser. Deretter benyttes disse prognosene som input i en kvantitativ bestillingsmodell for å optimere lagerbeholdningen.

### 6.1 Prophet-modellen for etterspørselsprognosering

Prophet er en additiv regresjonsmodell utviklet av Facebook, designet for å håndtere tidsserier med sterke sesongvariasjoner og flere sesonger (f.eks. ukentlig og årlig). Modellen dekomponerer tidsserien i fire hovedkomponenter:

$y(t) = g(t) + s(t) + h(t) + \epsilon_t$

Hvor:

- $y(t)$ er den observerte verdien (etterspørselen) ved tidspunkt $t$.
- $g(t)$ er trendfunksjonen som modellerer ikke-periodiske endringer.
- $s(t)$ representerer periodiske endringer (sesongvariasjoner).
- $h(t)$ representerer effekten av helligdager eller spesielle hendelser.
- $\epsilon_t$ er feilleddet som representerer idiosynkratiske endringer som ikke fanges opp av modellen. Det antas at $\epsilon_t \sim N(0, \sigma^2)$.

#### 6.1.1 Trendkomponenten $g(t)$

For dette prosjektet benyttes en stykkevis lineær trendmodell ("piecewise linear growth"). Denne fanger opp endringer i vekstrate over tid ved hjelp av definerte endringspunkter (changepoints). Matematisk formuleres dette som:

$g(t) = (k + a(t)^T \delta)t + (m + a(t)^T \gamma)$

Her defineres størrelsene som følger:

- $k$: Den initielle vekstraten.
- $\delta$: Una vektor av ratejusteringer, hvor $\delta_j$ er endringen i vekstrate som oppstår ved endringspunkt $j$.
- $m$: Et offset-parameter (skjæringspunkt med y-aksen).
- $a(t)$: Una binær vektor av indikatorfunksjoner slik at $a_j(t) = 1$ dersom $t \ge s_j$, og $0$ ellers, hvor $s_j$ er tidspunktet for endringspunkt $j$.
- $\gamma$: Una vektor av justeringsparametre definert som $\gamma_j = -s_j \delta_j$ for å sikre at trendfunksjonen er kontinuerlig.

#### 6.1.2 Sesongkomponenten $s(t)$

For å modellere periodiske effekter benytter Prophet en Fourier-rekke. Dette gir modellen fleksibilitet til å tilpasse seg komplekse sesongmønstre. Sesongfunksjonen er gitt ved:

$s(t) = \sum_{n=1}^N \left( a_n \cos\left(\frac{2\pi nt}{P}\right) + b_n \sin\left(\frac{2\pi nt}{P}\right) \right)$

Hvor:

- $P$: Perioden for sesongen (f.eks. $P = 365,25$ for årlig sesongvariasjon).
- $N$: Rekkens orden, som bestemmer hvor raskt sesongen kan endre seg (høyere $N$ fanger opp mer detaljerte svingninger).
- $a_n, b_n$: Fourier-koeffisienter som estimeres under modelltilpasningen. For årlig sesongvariasjon benyttes ofte $N=10$, noe som gir 20 parametere som skal estimeres.

#### 6.1.3 Helligdagskomponenten $h(t)$

Helligdager og kampanjeperioder har ofte en signifikant, men kortvarig effekt på salget. Prophet modellerer dette ved å summere effektene av hver spesifiserte hendelse $i$:

$h(t) = \sum_{i=1}^L \kappa_i \cdot \mathbb{1}(t \in D_i)$

Hvor:

- $L$: Antall unike helligdager/hendelser (f.eks. påske, jul, skolestart).
- $\kappa_i$: Effekten av helligdag $i$ på etterspørselen (parameter som estimeres).
- $D_i$: Mengden av datoer som faller inn under helligdag $i$.
- $\mathbb{1}(\cdot)$: Una indikatorfunksjon som er $1$ dersom tidspunkt $t$ er en del av hendelsen $D_i$.

#### 6.1.4 Utvidet Feature Engineering og identifisering av kampanjer

En kritisk utfordring i etterspørselsprognosering er å skille mellom regelmessig sesongvariasjon og diskrete sjokk forårsaket av markedsføringstiltak (kampanjer). Dersom kampanjer ikke identifiseres og isoleres, vil modellen feilaktig inkludere disse toppene i den årlige sesongkomponenten, noe som fører til systematiske overestimeringer i fremtidige perioder uten tilsvarende kampanjer.

I fravær av eksplisitte kampanjemarkører i rådataene, er det benyttet en metodikk basert på **Z-score residualanalyse** for å retrospektivt identifisere sannsynlige kampanjeperioder. Observasjoner med et avvik større enn 1,5 standardavvik fra det månedlige snittet er klassifisert som kampanjehendelser. Disse hendelsene er deretter inkludert som unike binære variabler i helligdagskomponenten $h(t)$.

Resultatet av denne dekomponeringen er visualisert i Figur 6.1, 6.2 og 6.3:

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.8%20utvidet%20feature%20engineering/komponenter_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.1: Komponentanalyse for Engelsk fiksjon. Legg merke til de betydelige utslagene i helligdagskomponenten (nederst) som fanger opp seks identifiserte kampanjer og faste høytider.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.8%20utvidet%20feature%20engineering/komponenter_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.2: Komponentanalyse for Norsk krim. Kategorien viser en svært stabil sesongprofil med kun én identifisert kampanje (mai 2025).</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.8%20utvidet%20feature%20engineering/komponenter_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.3: Komponentanalyse for Norske barnebøker. Modellen fanger opp de faste toppene ved skolestart og jul, supplert med to identifiserte kampanjeperioder.</em>
</div>

#### 6.1.5 Valg av Prophet fremfor SARIMA

Valget av Prophet som primær prognosemodell er basert på en metodisk vurdering opp mot den tradisjonelle SARIMA-modellen. Selv om begge modellene er stokastiske og kan håndtere sesongvariasjoner, anses Prophet som et mer naturlig valg for denne typen logistikkprosjekt av følgende årsaker:

1. **Håndtering av flere sesongmønstre og helligdager:** Bokbransjen preges av komplekse kalendereffekter, som "bevegelige" helligdager (påske) og faste salgstopper (jul, skolestart). Prophet inkluderer en dedikert komponent for helligdager ($h(t)$) som enkelt fanger opp disse additive sjokkene. I en SARIMA-modell ville dette krevd omfattende bruk av eksterne variabler (SARIMAX) og manuell koding av datoer.
2. **Robusthet mot ikke-stasjonaritet:** SARIMA krever streng stasjonaritet, noe som ofte fordrer flere runder med differensiering og statistisk testing for å transformere dataene. Prophet er en additiv modell som håndterer trender og sesongvariasjoner internt uten behov for omfattende pre-prosessering, noe som reduserer risikoen for feil ved modellspesifisering.
3. **Praktisk tolkbarhet:** Prophet dekomponerer tidsserien i visuelle komponenter (trend, årstid, helligdager). Dette gir et langt mer intuitivt beslutningsgrunnlag for en logistikkansvarlig enn de mer abstrakte matematiske parameterne i en SARIMA-modell (AR- (autoregressive) og MA- (moving average) ordener).
4. **Håndtering av uregelmessige data:** Prophet er robust mot manglende observasjoner og store uteliggere, noe som ofte forekommer i reelle salgsdata fra ERP-systemer.

Samlet sett gir Prophet en bedre balanse mellom statistisk presisjon og praktisk anvendelighet for ARK Bokhandel, da modellen er skreddersydd for tidsserier med sterke menneskeskapte mønstre.

**Hvorfor en empirisk sammenligning mot SARIMA ikke ble gjennomført:**

Prosjektets primære forskningsspørsmål handler om å integrere prognose med lagerstyring (jf. Goltsos et al., 2022), ikke om å rangere prognosemodeller mot hverandre. En direkte komparativ evaluering av Prophet mot SARIMAX ville krevd et separat eksperimentelt oppsett med konsistent feature engineering, hyperparametertuning og kryssvalidering for begge modeller — noe som ligger utenfor prosjektets ramme.

Vurderingen i listen over er derfor metodisk og kvalitativ, ikke empirisk. Dette er en reell begrensning for hvor sterkt valget av Prophet kan rettferdiggjøres på prognosenøyaktighet alene. En komparativ benchmarking mot SARIMAX og utvalgte maskinlæringsmodeller er løftet frem som et naturlig neste steg i seksjon 9.5 og 9.7.

For å illustrere hvordan Prophet dekomponerer etterspørselen, viser Figur 6.4 komponentene for kategorien "Norsk krim" før utvidet feature engineering:

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.5%20kvantitativ%20modell/prophet_components_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.4: Opprinnelig dekomponering av etterspørsel for Norsk krim i trend, helligdager og årlig sesongvariasjon (før inkludering av kampanjeanalyse).</em>
</div>

Modellens estimerte nøkkelparametre for de tre kategoriene er oppsummert i tabellen nedenfor:

| Kategori                     | Estimert Trend-endring (%) | Sesong-amplitude (enheter) |
| :--------------------------- | :------------------------: | :------------------------: |
| **Engelsk fiksjon**    |          -4,84 %          |       204,8 enheter       |
| **Norske barnebøker** |          -0,10 %          |       105,3 enheter       |
| **Norsk krim**         |          +12,70 %          |       114,8 enheter       |

Komponentfigurene for alle tre kategorier er presentert i Figur 6.1–6.4.

### 6.2 Baseline-løsning

Baseline-strategien fungerer som et sammenligningsgrunnlag for å vurdere merverdien av Prophet-modellen, og er implementert som en enkel **(s, Q)-politikk** basert på historiske gjennomsnittstall fra treningsdatasettet (jf. seksjon 5.2 og vedlegg A). Parameterne beregnes kategorivis som:

- **Forventet etterspørsel:** $\hat{D} = \frac{1}{n} \sum_{i=1}^{n} D_i$ (historisk månedssnitt).
- **Bestillingspunkt:** $s = \hat{D} \cdot \bar{L} \cdot 1{,}10$, hvor $\bar{L}$ er gjennomsnittlig ledetid omregnet til måneder og 10 % er en fast sikkerhetsmargin.
- **Bestillingsmengde:** $Q = \hat{D}$ (snittbehov per måned).

Strategien representerer en «status quo»-situasjon hvor innkjøper bestiller for å dekke et forventet gjennomsnittsbehov uten å dekomponere sesongtrender eller ta høyde for spesifikke kalenderhendelser. De kategorispesifikke baseline-parameterne er oppsummert i tabellen under:

| Kategori                     | Gj.sn. etterspørsel | Gj.sn. ledetid | Bestillingspunkt ($s$) | Bestillingsmengde ($Q$) |
| :--------------------------- | :------------------: | :------------: | :----------------------: | :-----------------------: |
| **Engelsk fiksjon**    |     338 enheter     |    7 dager    |        88 enheter        |        338 enheter        |
| **Norske barnebøker** |     286 enheter     |    3 dager    |        31 enheter        |        286 enheter        |
| **Norsk krim**         |     365 enheter     |    3 dager    |        40 enheter        |        365 enheter        |

Figur 6.5a–6.5c illustrerer den karakteristiske (s, Q)-sykelen for hver av de tre kategoriene over testperioden (2025). I hver figur er blå linje lagerbeholdning etter salg, rød stiplet linje markerer bestillingspunktet $s$, oransje søyler viser faktisk etterspørsel, og grønne trekanter markerer månedene hvor en bestilling på $Q$ enheter legges.

For **Engelsk fiksjon** (Figur 6.5a) ser vi den klassiske sagtannprofilen: lageret tappes ned, en bestilling på $Q = 338$ utløses når beholdningen krysser $s = 88$, og den ankommer i påfølgende periode. Modellen bygger likevel ikke opp ekstra buffer før sesongtoppene i juli/august og desember, og flere måneder har lager på null.

<div align="center">
  <img src="../006%20analysis/figures/15_baseline_sq_sykel_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.5a: Baseline (s, Q)-sykel for Engelsk fiksjon.</em>
</div>

For **Norske barnebøker** (Figur 6.5b) er det lave bestillingspunktet ($s = 31$) og det relativt lave $Q = 286$ utilstrekkelig for de faste toppene rundt skolestart (august) og jul. Lageret tappes til null allerede tidlig i året og forblir der gjennom høysesongen. Det understreker at selv om kategorien har regelmessige sesongmønstre, krever den et betydelig sikkerhetslager som den enkle baselinen ikke dimensjonerer for.

<div align="center">
  <img src="../006%20analysis/figures/15_baseline_sq_sykel_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.5b: Baseline (s, Q)-sykel for Norske barnebøker.</em>
</div>

For **Norsk krim** (Figur 6.5c) er ubalansen mest ekstrem: $Q = 365$ ligger under det månedlige gjennomsnittet i testperioden, og kombinert med den positive trenden (+12,7 %) og sterke sesongtopper faller lageret til null allerede i februar. Dette illustrerer at baselinen, basert på historiske snitt, ikke fanger trendutviklingen og systematisk underdimensjonerer volumet.

<div align="center">
  <img src="../006%20analysis/figures/15_baseline_sq_sykel_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.5c: Baseline (s, Q)-sykel for Norsk krim.</em>
</div>

Ved å holde denne baselinen konstant gjennom hele testperioden fanger den verken trendendringer eller sesongeffekter, og forventes derfor å generere stockouts i høysesong – særlig for Norsk krim og Engelsk fiksjon. Dette gjør den til et strengt, men rettferdig sammenligningsgrunnlag for den kvantitative optimaliseringsmodellen i kapittel 6.3. 

### 6.3 Kvantitativ bestillingsmodell (Optimaliseringsmodell)

Den kvantitative bestillingsmodellen tar utgangspunkt i etterspørselsprognosene fra Prophet. Målet er å bestemme den optimale bestillingsmengden $Q_t$ for hver periode $t$ som minimerer de totale logistikkostnadene.

Figur 6.6 gir en samlet oversikt over dataflyten i modellen — fra historisk etterspørsel, gjennom Prophet-prognosen og bias-justeringen, til den kvantitative optimaliseringsmodellen som leverer bestillingsbeslutningene. Den viser hvordan prognoseoutputen $\hat{y}(t)$ konverteres til prognostisert etterspørsel $D_t$ som mates inn i målfunksjonen sammen med de eksterne parametrene ($C_h$, $C_s$, $L$, $SL_{mål}$).

<div align="center">
  <img src="../006%20analysis/figures/16_flytmodell_prognose_optimalisering.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6.6: Dataflyt fra historisk etterspørsel til bestillingsbeslutning. Prophet-modellen produserer prognosen $\hat{y}(t)$, som bias-justeres på bakgrunn av backtesting (kap. 6.5) og mates inn som $D_t$ i optimaliseringsmodellen sammen med parametrene $C_h$, $C_s$, $L$ og $SL_{mål}$. Modellen returnerer beslutningsvariablene $Q_t$ (bestillingsmengde), $s_t$ (bestillingspunkt) og sikkerhetslager.</em>
</div>

**Målfunksjon:**
$Minimere Z = \sum_{t=1}^T (C_h \cdot I_t + C_s \cdot S_t)$

Under forutsetning av:

- $I_t = I_{t-1} + Q_{t-L} - D_t + S_t$ (Lagerbalanse-ligning)
- $I_t \ge 0, Q_t \ge 0$

Hvor variablene og parameterne er definert som:

- $Z$: Totale relevante kostnader over planleggingsperioden $T$.
- $C_h$: Lagerholdskostnad per enhet per tidsperiode (holding cost).
- $C_s$: Mangelkostnad per enhet (stockout cost), som inkluderer tapt dekningsbidrag og goodwill-tap.
- $I_t$: Lagerbeholdning ved slutten av periode $t$.
- $S_t$: Antall enheter i restordre (stockout) i periode $t$.
- $Q_{t-L}$: Leveranse mottatt i periode $t$, som ble bestilt i periode $t-L$.
- $L$: Ledetid fra bestilling til varemottak.
- $D_t$: Faktisk etterspørsel i periode $t$ (estimert ved $\hat{y}(t)$ fra Prophet).

Modellen inkluderer også et krav til **Servicegrad (SL)**, som definerer sannsynligheten for å kunne dekke etterspørselen direkte fra lager:
$P(I_t > 0) \ge SL_{mål}$

Gjennom sensitivitetsanalyse testes modellen for ulike scenarier av kostnader og varians i etterspørsel for å vurdere dens robusthet i møte med usikkerhet.

### 6.4 Modellforutsetninger og antagelser

For å sikre modellens validitet og tolkbarhet er følgende forutsetninger lagt til grunn for den kvantitative analysen:

#### 6.4.1 Stasjonaritet og trendhåndtering

I motsetning til tradisjonelle tidsseriemodeller (som ARIMA — AutoRegressive Integrated Moving Average), forutsetter ikke Prophet at dataene er stasjonære. Modellen håndterer ikke-stasjonaritet ved å modellere trenden som en stykkevis lineær funksjon.

For å dokumentere serienes egenskaper er det gjennomført både en **Augmented Dickey-Fuller (ADF) test** og en **Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test** på etterspørselsdataene for de tre kategoriene. Resultatene er gjengitt i tabellen under:

| Kategori                     | ADF p-verdi | KPSS p-verdi | ADF Konklusjon | KPSS Konklusjon | Samlet Vurdering      |
| :--------------------------- | :---------: | :----------: | :------------- | :-------------- | :-------------------- |
| **Engelsk fiksjon**    |    0,000    |    0,100    | Stasjonær     | Stasjonær      | Konsistent stasjonær |
| **Norske barnebøker** |    0,001    |    0,100    | Stasjonær     | Stasjonær      | Konsistent stasjonær |
| **Norsk krim**         |    0,000    |    0,100    | Stasjonær     | Stasjonær      | Konsistent stasjonær |

Ved å kombinere disse to testene, hvor ADF tester for enhetsrot ($H_0$: ikke-stasjonær) og KPSS tester for stasjonaritet ($H_0$: stasjonær), oppnår vi en sterkere statistisk bekreftelse. At testene er samstemte for alle tre kategorier, underbygger at dataene svinger stabilt rundt en trend, noe som gjør Prophet-modellens dekomponering svært egnet for denne typen beslutningsstøtte.

Selv om testene indikerer stasjonaritet (p < 0,05 for ADF og p > 0,05 for KPSS), viser de visuelle analysene i Figur 4.1 og 6.1 kraftige, periodiske sesongsvingninger. Valget av Prophet-modellen er derfor begrunnet i dens evne til å modellere disse svingningene og helligdagseffekter eksplisitt, noe som gir bedre beslutningsstøtte enn modeller som utelukkende fokuserer på stasjonaritet gjennom differensiering.

* **Analysefunn:** Trendanalysen viser stor variasjon mellom kategoriene. Mens *Norsk krim* har en tydelig positiv trend (+12,7 %), viser *Engelsk fiksjon* en svak negativ utvikling (-4,8 %). *Norske barnebøker* skiller seg ut med en svært stabil trend (-0,1 %), noe som indikerer en moden kategori med forutsigbart volum over tid. Ved å dekomponere disse trendene for alle tre kategorier, unngår vi at langsiktige endringer forveksles med sesongsvingninger.

#### 6.4.2 Sesongkomponenter og helligdagseffekter

Det antas at de historiske sesongmønstrene er representative for fremtidig etterspørsel.

* **Amplitude:** Analysen viser kraftige sesongeffekter for alle kategorier, men med ulik intensitet. *Engelsk fiksjon* har den høyeste amplituden (ca. 205 enheter), etterfulgt av *Norsk krim* (114,8 enheter) og *Norske barnebøker* (105,3 enheter).
* **Helligdager:** Effekten av påske, jul og skolestart er modellert som additive sjokk. Det antas at disse hendelsene påvirker etterspørselen i et fast tidsvindu hvert år (f.eks. 15 dager før julaften).

#### 6.4.3 Feilledd og normalfordeling

Det antas at feilleddet $\epsilon_t$ er normalfordelt med forventningsverdi null. Dette er avgjørende for beregning av sikkerhetslager og servicegrad, da vi benytter normalfordelingens fraktiler ($z$-verdier) for å bestemme bestillingspunktet $s_t$.

#### 6.4.4 Lagerstyringsantagelser

* **Ledetid:** Det antas at ledetiden $L$ er deterministisk eller følger en kjent fordeling basert på historiske leverandørdata.
* **Mangelkostnad:** Mangelkostnaden $C_s$ er satt betydelig høyere enn lagerholdskostnaden $C_h$ (f.eks. 120 NOK vs 10 NOK for Engelsk fiksjon) for å reflektere den strategiske viktigheten av tilgjengelighet i bokbransjen.
* **Restordrer:** Som spesifisert i kapittel 1.4, antas det at tapt salg ved stockout er permanent og ikke genererer restordrer ("lost sales"-modell).

### 6.5 Modellvalidering og Bias-justering (Backtesting)

Før modellen tas i bruk for fremtidige prognoser (2026), er den validert gjennom "backtesting" mot historiske data for 2025. Dette steget er kritisk for å identifisere systematiske skjevheter (bias) i modellen.

| Kategori                     |  MAE  | RMSE | MAPE (%) |  Bias  |
| :--------------------------- | :---: | :---: | :------: | :----: |
| **Engelsk fiksjon**    | 49,62 | 60,89 | 17,43 % | +15,96 |
| **Norsk krim**         | 23,89 | 30,63 |  5,93 %  | -11,78 |
| **Norske barnebøker** | 25,47 | 32,10 |  8,68 %  | +0,69 |

Analysen viser at modellen for *Engelsk fiksjon* har en positiv bias (overestimering), mens *Norsk krim* har en negativ bias (underestimering). For å sikre optimale bestillinger i 2026, er det i seksjon 8.3 implementert automatiske bias-korreksjoner som nøytraliserer disse systematiske feilene før bestillingsmengden beregnes.

---

## 7.0 Analyse

Gjennomgangen av det vaskede datasettet (2021-2025) har avdekket distinkte mønstre for de tre bokkategoriene som er kritiske for valget av prognosemodell:

**Engelsk fiksjon:**
Denne kategorien preges av en relativt stabil etterspørsel gjennom året, men med markerte topper i **juni/juli** (sommerlesing) og **desember** (julesalg). Historikken viser hyppige og omfattende stockouts, spesielt i juni 2021 hvor etterspørselen oversteg salget med nesten 300 enheter. Dette indikerer et stort forbedringspotensial ved mer nøyaktige prognoser.

**Norsk krim:**
Krim-kategorien har de mest utpregede sesongtoppene. Toppene er i stor grad knyttet til **juli/august** (feriekrim) og **desember**. I tillegg ser vi en merkbar økning rundt påsketider (mars/april). Dataene viser at etterspørselen ofte bikker 500 enheter i disse periodene, og det er identifisert en svak økende trend i totalvolumet mot slutten av perioden (2024-2025).

**Norske barnebøker:**
Barnebøker viser en jevn og høy frekvens i etterspørselen, men med faste topper i **august** (skolestart) og **desember**. En interessant observasjon er gjentakende stockouts i august-perioden på tvers av flere år, noe som tyder på at nåværende bestillingspraksis konsekvent undervurderer effekten av skolestart.

**Oppsummering av sesongvariasjoner:**
Analysen bekrefter at de viktigste faktorene for en god prognose er evnen til å fange opp de brede sommertoppene og de spisse juletoppene. Ved å benytte en modell som dekomponerer disse sesongene, kan man redusere de observerte stockout-periodene betydelig.

---

## 8.0 Resultat

Resultatene fra den kvantitative analysen sammenligner ytelsen til den Prophet-baserte modellen mot baseline-løsningen over testperioden. Den samlede analysepakken (forecast vs. actual, residualer og kostnadsfordeling for alle tre kategorier) presenteres i seksjon 8.1.1–8.1.3 nedenfor.

| Kategori                     |   Kostnad Baseline   |    Kostnad Prophet    |  Besparelse (%)  |   SL Baseline   |    SL Prophet    |
| :--------------------------- | :-------------------: | :-------------------: | :---------------: | :--------------: | :--------------: |
| **Engelsk fiksjon**    |      89 267 NOK      |      71 802 NOK      |      19,57 %      |      83,1 %      |      86,3 %      |
| **Norske barnebøker** |      41 115 NOK      |      44 346 NOK      |      -7,86 %      |      85,4 %      |      83,8 %      |
| **Norsk krim**         |      68 254 NOK      |      42 247 NOK      |      38,10 %      |      85,8 %      |      91,5 %      |
| **TOTALT**             | **198 636 NOK** | **158 395 NOK** | **20,26 %** | **84,7 %** | **87,2 %** |

### 8.1 Detaljert analyse per kategori

For å forstå de underliggende driverne for besparelsene, dekomponeres resultatene i prognosekvalitet og kostnadsfordeling for hver kategori. Hovedfunnet er ikke ensartet: *Norsk krim* (38,1 % besparelse) og *Engelsk fiksjon* (19,6 % besparelse) viser tydelig gevinst med Prophet-modellen, mens **Norske barnebøker skiller seg ut som unntaket** — her gir modellen et marginalt negativt resultat (−7,9 %). Denne asymmetrien har en sammenheng med kategorienes underliggende variansstruktur og diskuteres i 8.1.3, sensitivitetsanalysen i 8.2, og i drøftingen i 9.3 og 9.5.

#### 8.1.1 Norsk krim (Høy volatilitet og sterk trend)

Dette er kategorien med størst økonomisk gevinst (38,1 %). Figur 8.1 viser at Prophet-modellen treffer svært godt på de ekstreme sesongtoppene i testperioden, noe som er kritisk for å unngå utsolgt-situasjoner i høysesong.

<div align="center">
  <img src="../006%20analysis/figures/10_forecast_vs_actual_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.1: Forecast vs. Actual for Norsk krim.</em>
</div>

Ved å analysere residualene (prognosefeilen) i Figur 8.2, ser vi en tilnærmet normalfordeling med en svak negativ bias. Dette underbygger bruken av sikkerhetslager basert på normalfordelingens fraktiler for å sikre ønsket servicegrad.

<div align="center">
  <img src="../006%20analysis/figures/11_residualer_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.2: Distribusjon av residualer for Norsk krim. Den røde linjen indikerer nullavvik.</em>
</div>

Netto reduksjon i totalkostnad er på over 26 000 NOK, hovedsakelig drevet av lavere $C_s$ (Figur 8.3).

<div align="center">
  <img src="../006%20analysis/figures/12_cost_breakdown_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.3: Kostnadsfordeling for Norsk krim (Baseline vs. Prophet).</em>
</div>

#### 8.1.2 Engelsk fiksjon (Uforutsigbarhet og import)

For Engelsk fiksjon oppnår Prophet-modellen en besparelse på 19,57 %, hvor reduksjonen i $C_s$ utgjør over 15 000 NOK. Kategorien har den høyeste prognoseusikkerheten av de tre (MAPE 17,43 %, jf. 6.5).

<div align="center">
  <img src="../006%20analysis/figures/12_cost_breakdown_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.4: Kostnadsfordeling for Engelsk fiksjon.</em>
</div>

#### 8.1.3 Norske barnebøker (Forutsigbare sesongmønstre)

For Norske barnebøker gir Prophet-modellen et negativt resultat (−7,86 %), tilsvarende en merkostnad på 3 231 NOK sammenlignet med baseline. Servicegraden faller marginalt fra 85,4 % til 83,8 %.

### 8.2 Sensitivitetsanalyse og robusthet

For å vurdere modellens pålitelighet er det gjennomført en sensitivitetsanalyse hvor sentrale parametere (stockout-kostnad $C_s$, lagerholdskostnad $C_h$ og sikkerhetsmarginfaktor) varieres én om gangen rundt basisverdien. Metodikk og kategorivise nøkkelfunn presenteres i seksjon 8.2.1–8.2.3 nedenfor, med tilhørende figurer i Figur 8.5–8.10. Dette er avgjørende for å forstå hvordan modellen håndterer usikkerhet i kostnadsestimater og operasjonelle marginer.

#### 8.2.1 Engelsk fiksjon

For Engelsk fiksjon observeres en lineær sammenheng mellom stockout-kostnad og totalkostnad, mens servicenivået forblir stabilt. Dette indikerer en robust modell, men som vist i Figur 8.6, gir en økning i sikkerhetsmarginfaktoren til 1,5 en dramatisk forbedring i både kostnad og service.

<div align="center">
  <img src="../006%20analysis/figures/13_sensitivitet_kost_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.5: Kostnadssensitivitet (Engelsk fiksjon).</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/14_sensitivitet_service_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.6: Servicenivå-sensitivitet (Engelsk fiksjon).</em>
</div>

#### 8.2.2 Norske barnebøker

Barnebøker viser høyere sensitivitet for lagerholdskostnad. En reduksjon i denne kostnaden (faktor 0,8) muliggjør et betydelig hopp i servicenivået, da modellen velger å holde mer bufferlager strategisk før sesongtopper.

<div align="center">
  <img src="../006%20analysis/figures/13_sensitivitet_kost_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.7: Kostnadssensitivitet (Norske barnebøker).</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/14_sensitivitet_service_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.8: Servicenivå-sensitivitet (Norske barnebøker).</em>
</div>

#### 8.2.3 Norsk krim

Norsk krim fremstår som den mest stabile kategorien. Som vist i Figur 8.10, oppnår modellen et "metningspunkt" ved en sikkerhetsmarginfaktor på 1,2, hvor ytterligere lagerbeholdning ikke gir gevinst i servicenivå. Dette tyder på at de resterende manglene skyldes uforutsigbare sjokk som faller utenfor modellens rekkevidde gitt ledetiden.

<div align="center">
  <img src="../006%20analysis/figures/13_sensitivitet_kost_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.9: Kostnadssensitivitet (Norsk krim).</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/14_sensitivitet_service_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.10: Servicenivå-sensitivitet (Norsk krim).</em>
</div>

### 8.3 Optimalisering av styringsparametere

Som et resultat av backtestingen og sensitivitetsanalysen er de endelige styringsparameterne for 2026-sesongen fastsatt. Tabellen under viser bias-justering, sikkerhetsfaktor (k) og estimert kampanjeløft per kategori:

| Kategori                     | Bias-justering | Sikkerhetsfaktor (k) | Est. Kampanjeløft |
| :--------------------------- | :------------: | :------------------: | :----------------: |
| **Engelsk fiksjon**    |     -15,96     |         1,4         |   135,6 enheter   |
| **Norsk krim**         |     +11,78     |         1,8         |    56,6 enheter    |
| **Norske barnebøker** |     -0,69     |         1,5         |    39,7 enheter    |

Sikkerhetsfaktoren er satt kategorivis ut fra bias-størrelse og observert volatilitet, mens kampanjeløftet er estimert fra historiske kampanjeobservasjoner i datasettet (seks for *Engelsk fiksjon*, to for *Norske barnebøker* og én for *Norsk krim*). Disse reglene danner grunnlaget for den endelige prognosegenereringen og scenario-analysen.

### 8.4 Prognoser for 2026 (Operasjonell Planlegging)

Som det siste steget i den kvantitative analysen er det generert endelige etterspørselsprognoser for hele 2026. Disse prognosene integrerer alle funn fra tidligere steg, inkludert bias-justering fra backtestingen (6.5) og dynamisk beregning av sikkerhetslager basert på de optimaliserte k-faktorene (8.3).

Tabellen nedenfor viser de forventede gjennomsnittlige verdiene per måned for 2026, som danner grunnlaget for ARKs taktiske lagerplanlegging:

| Kategori                     | Justert etterspørsel (snitt) | Sikkerhetslager (snitt) | Bestillingspunkt (snitt) |
| :--------------------------- | :---------------------------: | :---------------------: | :----------------------: |
| **Engelsk fiksjon**    |            283,82            |          75,60          |          359,42          |
| **Norsk krim**         |            418,90            |          35,10          |          454,00          |
| **Norske barnebøker** |            290,59            |          30,26          |          320,85          |

Sikkerhetslageret er beregnet ved å estimere prognosens standardavvik fra Prophets 90 %-usikkerhetsintervall ($\sigma \approx (\hat{y}_{upper} - \hat{y})/1{,}645$) og deretter multiplisere med den kategoritilpassede k-faktoren fra 8.3, slik at $SS = k \cdot \sigma$.

De månedlige svingningene i forventet etterspørsel og det tilhørende behovet for sikkerhetslager er visualisert i Figur 8.11, 8.12 og 8.13. Disse visualiseringene viser hvordan modellen proaktivt øker lagerbeholdningen i forkant av de identifiserte sesongtoppene for å opprettholde målsetningen om leveringsservice.

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.11%20prognoser/prognose_2026_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.11: Prognose og sikkerhetslager for Engelsk fiksjon i 2026.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.11%20prognoser/prognose_2026_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.12: Prognose og sikkerhetslager for Norsk krim i 2026.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.11%20prognoser/prognose_2026_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.13: Prognose og sikkerhetslager for Norske barnebøker i 2026.</em>
</div>

### 8.5 Scenario-analyse (Robusthetstesting)

For å sikre at den foreslåtte bestillingsmodellen er robust mot uforutsette endringer i markedsforholdene, er det gjennomført en scenario-analyse for 2026. To ulike ytterpunkter er testet mot baseline-prognosen:

1. **Scenario A (Kampanje-sjokk):** Simulerer en situasjon der kampanjene i mai og desember gir 50 % høyere løft enn historisk snitt, kombinert med en 20 % økning i sikkerhetslageret for å håndtere økt volatilitet.
2. **Scenario B (Kostnads-sjokk):** Simulerer en kraftig økning i lagerholdskostnader (f.eks. strøm og husleie), som tvinger frem en 20 % reduksjon i sikkerhetslageret for å minimere kapitalbinding.

**Antagelser og datakvalitet:**
Analysen antar at sesongmønsteret fra de siste 4 årene vedvarer i 2026. Kampanjeløftet i scenario A er basert på historisk effekt pluss et estimert sjokk (50% økning av gjennomsnittlig løft). Modellen tar høyde for normal volatilitet, men ekstreme "Sorte svaner" er ikke inkludert i simuleringen.

Tabellen nedenfor oppsummerer hvordan det gjennomsnittlige lagernivået (Order-up-to level) må justeres i de ulike scenariene:

| Kategori                     | Baseline (Units) | Scenario A: Kampanje-sjokk | Scenario B: Kostnads-sjokk |
| :--------------------------- | :--------------: | :------------------------: | :------------------------: |
| **Engelsk fiksjon**    |      360,3      |           +7,4 %           |           -4,2 %           |
| **Norsk krim**         |      453,8      |           +2,6 %           |           -1,5 %           |
| **Norske barnebøker** |      320,1      |           +2,9 %           |           -1,8 %           |

Baseline tilsvarer det gjennomsnittlige bestillingspunktet fra 8.4 (små avvik skyldes Prophets stokastiske trekning). *Engelsk fiksjon* krever den største justeringen under kampanje-sjokket (+7,4 %), mens *Norsk krim* og *Norske barnebøker* holder seg under 3 % endring i begge scenarier.

De visuelle forskjellene i lagernivå for de ulike scenariene er presentert i Figur 8.14, 8.15 og 8.16:

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.12%20scenario-analyse/scenario_plot_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.14: Scenario-sammenligning for Engelsk fiksjon i 2026.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.12%20scenario-analyse/scenario_plot_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.15: Scenario-sammenligning for Norsk krim i 2026.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.12%20scenario-analyse/scenario_plot_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8.16: Scenario-sammenligning for Norske barnebøker i 2026.</em>
</div>

---

## 9.0 Diskusjon

Den kvantitative analysen viser at en overgang fra statiske, gjennomsnittsbaserte bestillingsregler til en prognosedrevet og dynamisk modell gir en samlet kostnadsbesparelse på 20,26 % (fra 198 636 NOK til 158 395 NOK) og løfter den gjennomsnittlige servicegraden fra 84,7 % til 87,2 % i testperioden. Samtidig avdekker resultatene at gevinsten ikke er jevnt fordelt mellom kategoriene, og at modellens merverdi avhenger sterkt av etterspørselsstrukturen i den enkelte varegruppen. Diskusjonen under tolker funnene i lys av problemstillingen, litteraturen og metodens iboende begrensninger, og peker på hva resultatene faktisk betyr for ARK Bokhandels drift.

### 9.1 Tolkning av hovedfunnene

**Hovedfunnet er at den prognosedrevne modellen reduserer totalkostnaden med 20,26 % og hever servicegraden fra 84,7 % til 87,2 %, men at hele gevinsten kommer fra de to kategoriene med volatil eller trendpreget etterspørsel — for *Norske barnebøker*, der etterspørselen er stabil og sesongmønsteret forutsigbart, er en enkel baseline overlegen.** Modellens merverdi er altså betinget av etterspørselsstrukturen, ikke en universell egenskap ved metoden.

Resultatene i kapittel 8 bekrefter dermed at modellen leverer på problemstillingens to kjernekrav — å redusere lagerkostnader og samtidig begrense risikoen for utsolgte varer — men bare når etterspørselen har en struktur modellen er designet for å utnytte. Det er fire nivåer i tolkningen som bør løftes frem.

**Gevinstens drivere er konsistent med kostnadsasymmetrien.** For *Norsk krim* (−38,10 %) og *Engelsk fiksjon* (−19,57 %) kommer besparelsen hovedsakelig fra en kraftig reduksjon i mangelkostnaden $C_s$, delvis på bekostning av en moderat økning i lagerholdskostnaden $C_h$ (jf. Figur 8.3 og 8.4). Dette er i tråd med den teoretiske forventningen i seksjon 3.3.3: når mangelkostnaden er vesentlig høyere enn lagerholdskostnaden — som er tilfellet i bokbransjen med permanent tapt salg (seksjon 1.4) — forskyves det optimale servicenivået oppover, og en dynamisk allokering av lager mot sesongtoppene blir lønnsom. Omfordelingen mellom $C_h$ og $C_s$ er altså ikke en bivirkning av modellen, men en rasjonell respons på asymmetrien mellom de to kostnadstypene.

**Servicegraden øker samtidig som kostnadene faller.** At CSL for *Norsk krim* stiger fra 85,8 % til 91,5 % viser at gevinsten ikke hentes ut ved å akseptere flere stockouts, men ved at modellen bestiller mer presist når behovet faktisk oppstår. Dette er konsistent med Kirmizi et al. (2024), som påpeker at bedre prognoser reduserer residualvariansen $\sigma_d$ og dermed kravet til sikkerhetslager for et gitt servicenivå.

**Bias-korreksjonen er en undervurdert gevinstdriver.** Backtestingen i 6.5 avdekket systematisk skjevhet i to av tre kategorier: +15,96 for *Engelsk fiksjon* og −11,78 for *Norsk krim*. Korreksjonen anvendt i 8.3 var trolig et av de enkeltstående viktigste bidragene til besparelsen, særlig for *Norsk krim* der modellen ellers ville underbestilt systematisk i høysesong og spist opp store deler av den realiserte gevinsten.

**Parametervalget reflekterer kategoriens risikoprofil.** Sikkerhetsfaktoren k (8.3) er satt kategorivis ut fra en kvalitativ avveining mellom $C_h$ og $C_s$: en høyere k binder mer kapital, men reduserer eksponeringen for stockouts. *Norsk krim* tildeles k = 1,8 fordi modellen systematisk underestimerer etterspørselen (bias −11,78), og sensitivitetsanalysen (8.2.3) viser at servicegevinsten klart overstiger den marginale økningen i $C_h$. *Engelsk fiksjon* holdes på 1,4 – bias-korreksjonen reduserer allerede sikkerhetsbehovet, og en høyere k kombinert med volatiliteten ville gitt for høy kapitalbinding. *Norske barnebøker* ligger på 1,5 som et nøytralt midtpunkt, siden modellen der er tilnærmet forventningsrett (bias −0,69). At samme modellrammeverk kalibreres så ulikt mellom varegruppene, illustrerer et sentralt prinsipp: parametervalget er like viktig som metoden.

### 9.2 Når fungerer ikke den avanserte modellen? Tilfellet Norske barnebøker

Det mest overraskende funnet er at Prophet-modellen gir et *dårligere* resultat enn baseline for *Norske barnebøker* (+7,86 % i kostnad). Dette fortjener en egen drøfting, fordi det har direkte konsekvenser for hvordan ARK bør velge mellom ulike prognoseverktøy i drift.

Barnebokkategorien kjennetegnes av svært regelmessige og forutsigbare sesongtopper (skolestart i august, jul i desember) og en marginalt negativ trend (−0,10 %) som i praksis kan betraktes som flat. I en slik kategori har en statisk baseline med fast sikkerhetsmargin en innebygget fordel: den "betaler" lite for å overdimensjonere lageret, og mønstrene som skal fanges opp er få og lett identifiserbare. Prophet-modellens dynamiske tilnærming, som søker å minimere lageret i lavsesong for deretter å bygge det opp før topper, blir mer sårbar for små timing-feil og usikkerhetsestimering rundt de korte, intensive toppene.

Funnet plasserer seg godt i litteraturen: Borucka (2023) påpeker at valget av prognosemetode må tilpasses etterspørselsstrukturen, mens Chen (2021) studerer datadrevet lagerstyring under "shifting demand" — en kontekst som implisitt forutsetter at etterspørselen *faktisk* skifter. Når etterspørselen i stedet er tilnærmet stasjonær med stabil sesongstruktur — slik den er for *Norske barnebøker* — er det lite rom for en modell som er designet for å fange nettopp skift.

Den praktiske implikasjonen er viktig: en "én-modell-passer-alle"-strategi ville her gitt 3 231 NOK i merkostnad for barnebøker som delvis nøytraliserer gevinsten i de to andre kategoriene. Et mer realistisk driftsregime er å la Prophet håndtere volatile eller trendbasert kategorier og beholde en enklere regelbasert (s, Q)-politikk for stabile kategorier. Dette er i tråd med Kirmizi et al. (2024), som argumenterer for at hybridtilnærminger overgår enkeltmetoder.

### 9.3 Sammenheng med eksisterende litteratur

Resultatene plasserer seg tydelig i det forskningslandskapet som ble kartlagt i kapittel 2. Hovedpoenget hos Goltsos et al. (2022) — at prognose- og lagerstyringsforskning har utviklet seg fragmentert — materialiserer seg konkret i dette prosjektet ved at *integrasjonen* (Prophet-prognose → bias-korreksjon → sikkerhetslager → bestillingspunkt) er der mesteparten av gevinsten skapes. En god prognose alene er ikke tilstrekkelig; den må konverteres til handlingsrettede bestillingsparametere for å gi verdi i drift.

"Analyst-in-the-loop"-paradigmet beskrevet av Taylor og Letham (2018) manifesterer seg i den utvidede feature engineering-prosessen (6.1.4), der Z-score-basert kampanjeidentifisering ble brukt til å skille ordinær sesongvariasjon fra diskrete markedsføringssjokk. Uten dette skillet ville kampanjeeffektene blitt feilaktig absorbert i den årlige sesongkomponenten $s(t)$ og forplantet seg som systematiske overestimeringer i 2026-prognosen. Det er et konkret eksempel på at Prophets fleksibilitet er dobbeltkantet — den må temmes med domenekunnskap for å unngå overfitting til tilfeldige hendelser.

Haque et al. (2023) argumenterer for å inkludere eksterne makroøkonomiske variabler (KPI, forbrukertillit, arbeidsledighet) i prognosemodeller. Dette prosjektet har ikke inkludert slike variabler, men den eksplisitte modelleringen av helligdager og kampanjer ivaretar mye av den samme rollen — å gi modellen informasjon om eksogene sjokk som ikke følger av interne salgsmønstre. En naturlig videreutvikling er å teste om makrovariabler kan gi ytterligere forklaringskraft, særlig for *Engelsk fiksjon* der MAPE på 17,43 % indikerer at en vesentlig del av variansen fortsatt er uforklart.

### 9.4 Robusthet og modellens grenser

Sensitivitetsanalysen (8.2) viser at modellen reagerer forutsigbart på kostnadsparameterne: en høyere $C_s$ gir lineært høyere totalkostnad uten at servicenivået endres nevneverdig, mens en økt sikkerhetsmarginfaktor gir servicegevinst inntil et metningspunkt. Det er særlig funnet for *Norsk krim* som er interessant. Ved en sikkerhetsmarginfaktor på 1,2 oppnås metning, og ytterligere lagerøkning gir *ingen* servicegevinst. Dette er konsistent med teorien i seksjon 3.3.1: ved et gitt sikkerhetsnivå blir den uforklarte residualvariansen $\sigma_d$ den bindende skranken, og den kan ikke reduseres ved å holde mer lager. De resterende stockout-hendelsene i *Norsk krim* skyldes altså trolig uforutsigbare sjokk som faller utenfor det modellen kan fange innenfor ledetiden — et praktisk viktig poeng, fordi det betyr at det finnes en kostnadsgrense for hvor høy servicegrad som rasjonelt kan etterstrebes.

Scenario-analysen (8.5) bekrefter at modellen er robust mot moderate markedssjokk: for to av tre kategorier kreves under 3 % justering av lagernivået selv under et 50 %-kampanjesjokk (scenario A) eller en 20 %-reduksjon i sikkerhetslageret (scenario B). At *Engelsk fiksjon* krever 7,4 % økning under kampanje-sjokket er en naturlig konsekvens av at kategorien har den høyeste sesongamplituden (ca. 205 enheter) og seks identifiserte kampanjer — den er rett og slett mer eksponert for kampanjevariasjon enn de to andre. For ARK gir dette konkret informasjon om hvor mye ekstra bufferkapital som bør være tilgjengelig dersom markedsforholdene forverres, og hvilken kategori det først vil merkes i.

### 9.5 Begrensninger ved datagrunnlag og metode

Analysen har fem hovedbegrensninger som bør påvirke hvor sterkt resultatene kan tolkes.

**1. Simulert datagrunnlag:** Datasettet er konstruert for å etterligne ARK Bokhandels sesongmønstre, men fanger neppe alle støykilder i et reelt ERP-system (feilregistreringer, manuelle lagerjusteringer, returer, svinn utover det som er modellert). De absolutte kostnadsbesparelsene på 20,26 % bør derfor tolkes som et *estimat på potensialet* snarere enn et presist anslag for hva som vil realiseres i produksjon.

**2. Kampanjeidentifisering basert på Z-score:** Metoden i 6.1.4 identifiserer kampanjer retrospektivt ved avvik > 1,5 standardavvik fra månedssnittet. Det er en pragmatisk tilnærming i fravær av eksplisitte kampanjemarkører, men den risikerer å klassifisere ekte etterspørselssjokk (for eksempel en viral BookTok-anbefaling) som kampanjer — eller omvendt. For *Norsk krim* identifiserer metoden kun én kampanje (mai 2025), og kampanjeløftet på 56,6 enheter hviler dermed på én observasjon. Scenario A (8.5) kompenserer delvis ved å teste et +50 %-sjokk, men den underliggende estimeringsusikkerheten forblir reell.

**3. Deterministisk ledetid:** Modellen forutsetter at ledetiden $L$ er kjent og konstant. I virkeligheten vil særlig importerte bøker (*Engelsk fiksjon*) være eksponert for leverandørforsinkelser, tollklarering og fraktkapasitet. En stokastisk ledetid ville kreve at sikkerhetslageret dimensjoneres ut fra $\sigma_L = \sqrt{L \cdot \sigma_d^2 + \hat{d}^2 \cdot \sigma_L^2}$ (jf. Adeyemi & Onanuga, 2014), noe som ville gitt et betydelig høyere sikkerhetslager for *Engelsk fiksjon* og trolig redusert den realiserte gevinsten for denne kategorien.

**4. Tilsynelatende motsetning mellom stasjonaritetstester og visuell sesongstruktur:** ADF- og KPSS-testene i 6.4.1 indikerer at alle tre serier er stasjonære, mens komponentanalysene i Figur 6.1–6.3 viser tydelige periodiske svingninger. Dette er ikke en selvmotsigelse — testene måler om serien svinger rundt et stabilt gjennomsnitt, ikke om den er fri for sesongstruktur — men det innebærer at tradisjonelle modeller som SARIMA i prinsippet kunne vært anvendt. Valget av Prophet er begrunnet praktisk i 6.1.5, men en komparativ evaluering mot SARIMAX er et naturlig neste steg for å kvantifisere hvor mye Prophet faktisk tilfører.

**5. Bias-korreksjon som potensielt overfit:** Bias-justeringen i 8.3 er estimert på 2025-testdataene og applisert på 2026-prognosen. Dersom bias ikke er konstant over tid — noe som er sannsynlig i en kategori med skiftende trend som *Norsk krim* — vil korreksjonen delvis være en overtilpasning til testperioden. En mer robust tilnærming er rullerende backtesting som kan fange endringer i bias over tid, og som bør vurderes ved operativ implementering.

### 9.6 Implikasjoner for næringslivet og ARKs driftspraksis

Funnene gir flere konkrete anbefalinger til ARK Bokhandel.

**Differensier modellvalget mellom kategorier.** Resultatene for *Norske barnebøker* viser at det ikke finnes én universelt optimal modell. En enkel regelbasert (s, Q)-politikk kan være både billigere å drifte og mer treffsikker for kategorier med stabile, forutsigbare mønstre. Anbefalingen er et tolags regime: Prophet-basert optimalisering for volatile eller trenddrevne kategorier (*Norsk krim*, *Engelsk fiksjon*, trolig også ny-introduserte sjangre), og regelbaserte rutiner for modne, stabile kategorier (etablerte bestselgende barnebokserier).

**Behold modellen som beslutningsstøtte, ikke erstatning.** Selv for volatile kategorier er det viktig at innkjøpere og butikksjefer beholder muligheten til å justere modellens anbefalinger basert på markedsinnsikt som ikke er kvantifisert i dataene (nye TV-adaptasjoner, forfatterbesøk, lokale arrangementer, BookTok-trender). Prophets "analyst-in-the-loop"-filosofi (Taylor & Letham, 2018) støtter denne arbeidsformen ved å gjøre parameterne og komponentene tolkbare.

**Etabler bias-oppfølging som fast prosess.** De systematiske skjevhetene avdekket i backtestingen (+15,96 for *Engelsk fiksjon*, −11,78 for *Norsk krim*) tilsier at det bør etableres en kvartalsvis rutine for re-backtesting og biasjustering. Uten dette vil prognosene gradvis drifte etter hvert som markedsforholdene endrer seg.

**Prioriter systemintegrasjon.** Den kvantitative gevinsten realiseres kun dersom modellen faktisk brukes i bestillingsprosessen. Det krever integrasjon mot eksisterende ERP- og innkjøpsverktøy, samt opplæring av innkjøpere i hvordan modellens output skal tolkes. Luo (2019) påpeker at tradisjonelle bokhandlere må reformere styringssystemer for å utnytte datadrevet beslutningsstøtte, og dette prosjektet illustrerer konkret hvordan en slik reform kan utformes i praksis.

### 9.7 Generaliserbarhet og videre arbeid

Prosjektet bygger på tre kategorier hos én bokhandelkjede, og den direkte overførbarheten til andre kontekster er derfor begrenset. Samtidig er kategoriene valgt nettopp for å dekke ulike etterspørselsarketyper (stabil sesong, skarpe høytidstopper, trenddrevet vekst), og funnene har dermed en viss metodisk generaliseringskraft: *mønsteret* om at modellvalg må tilpasses kategoristrukturen er trolig overførbart til andre detaljhandelsbransjer med sterke sesongmønstre (leketøy, klær, sesongbaserte matvarer).

For videre arbeid peker analysen på fem retninger:

1. **Utvidelse til ISBN-nivå:** Aggregering på kategorinivå skjuler sannsynligvis store forskjeller mellom enkelttitler. En bestselgende serie og en nisjetittel kan ha svært ulike prognosekrav.
2. **Validering mot reelle ERP-data:** Den viktigste valideringen er å kjøre modellen mot faktiske ARK-data og måle realisert gevinst mot prognostisert gevinst.
3. **Stokastisk ledetid:** Inkorporere leverandørvariabilitet, særlig for importerte bøker, i sikkerhetslagerberegningen.
4. **Komparativ modellevaluering:** Benchmarke Prophet mot SARIMAX og utvalgte maskinlæringsmetoder for å kvantifisere hvor mye mer komplekse metoder tilfører.
5. **Makroøkonomiske kovariater:** Teste om variabler som konsumprisindeks og forbrukertillit (Haque et al., 2023) gir ytterligere forklaringskraft, særlig for *Engelsk fiksjon* der residualvariansen er størst.

---

## 10.0 Konklusjon

Problemstillingen som har styrt arbeidet er: *Hvordan kan ARK Bokhandel redusere lagerkostnader og samtidig opprettholde høy servicegrad gjennom en prognosedrevet bestillingsmodell?* Den kvantitative analysen på et simulert, men realistisk datagrunnlag viser at en overgang fra statiske bestillingsregler til en Prophet-basert dynamisk modell — koblet med bias-korreksjon og kategorivis sikkerhetsfaktor — reduserer total lagerkostnad med 20,26 % (fra 198 636 NOK til 158 395 NOK) og hever den gjennomsnittlige servicegraden fra 84,7 % til 87,2 % i testperioden 2025.

Gevinsten er imidlertid ikke uniform. For *Norsk krim* og *Engelsk fiksjon* gir modellen betydelige besparelser (henholdsvis −38,1 % og −19,6 % i kostnad), mens for *Norske barnebøker* — der etterspørselen er stabil og sesongmønsteret forutsigbart — er en enkel baseline overlegen (+7,9 % i kostnad med Prophet). Hovedkonklusjonen er derfor *betinget*: en prognosedrevet modell skaper merverdi når etterspørselen har en struktur modellen er designet for å utnytte, men ikke som et universalmiddel.

**Begrensninger ved studien.** Analysen er gjennomført på simulert data og fanger derfor ikke alle støykilder i et reelt ERP-system (returer, manuelle lagerjusteringer, feilregistreringer). Ledetiden er modellert som deterministisk, noe som trolig overvurderer gevinsten for *Engelsk fiksjon* der leverandørforsinkelser og importrisiko er reelle. Kampanjeidentifiseringen hviler på Z-score-deteksjon med få observasjoner per kategori, og bias-korreksjonen er estimert på 2025-testdataene og kan delvis representere overtilpasning til testperioden. En direkte empirisk sammenligning mot SARIMA er heller ikke gjennomført, slik at den relative merverdien av Prophet over enklere tidsseriemetoder er teoretisk begrunnet, men ikke empirisk verifisert. Disse forholdene innebærer at de absolutte tallene bør tolkes som et *estimat på potensialet*, ikke et presist anslag for hva som vil realiseres i drift.

**Praktiske implikasjoner.** For ARK gir resultatene tre konkrete anbefalinger: (1) prognosedrevet bestilling bør implementeres differensiert — Prophet eller tilsvarende dynamiske modeller for kategorier med volatil eller trendpreget etterspørsel, og enklere regelbasert (s, Q)-politikk for kategorier med stabil sesongstruktur; (2) bias-korreksjon basert på rullerende backtesting bør være en integrert del av bestillingsprosessen, ikke en engangsjustering; og (3) sikkerhetsfaktoren $k$ bør kalibreres kategorivis ut fra kostnadsasymmetri og residualvarians, ikke settes uniformt. Modellen gir samtidig et etterprøvbart beslutningsgrunnlag som reduserer avhengigheten av manuelle vurderinger i en hektisk planleggingshverdag.

**Videre forskning.** Naturlige neste skritt er å (i) validere modellen på reelle ERP-data fra ARK med faktiske leverandørledetider; (ii) gjennomføre en komparativ evaluering mot SARIMAX og enklere benchmarkmetoder for å kvantifisere Prophets faktiske merverdi; (iii) inkludere eksogene makrovariabler (jf. Haque et al., 2023) for kategorier med høy uforklart varians, særlig *Engelsk fiksjon*; og (iv) teste rammeverket på flere kategorier og kanaler for å vurdere generaliserbarhet ut over de tre kategoriene som inngår her. Studien viser at integrert prognose- og lagerstyring kan gi betydelig verdi, men understreker også at metodevalg må forankres i etterspørselsstrukturen til den enkelte varegruppen — og at gevinstestimatene må prøves mot reelle driftsforhold før de kan tas i bruk.

---

## 11.0 Bibliografi

Adeyemi, A. A., & Onanuga, A. T. (2014). Dynamics of inventory cost optimization — A review of theory and evidence. *Research Journal of Finance and Accounting*, *5*(22).

Borucka, A. (2023). Seasonal methods of demand forecasting in the supply chain as support for the company's sustainable growth. *Sustainability*, *15*(9), 7399. https://doi.org/10.3390/su15097399

Chen, B. (2021). Data-driven inventory control with shifting demand. *Production and Operations Management*, *30*(5), 1365–1385. https://doi.org/10.1111/poms.13326

Douaioui, K., Oucheikh, R., Benmoussa, O., & Mabrouki, C. (2024). Machine learning and deep learning models for demand forecasting in supply chain management: A critical review. *Applied System Innovation*, *7*(5), 93. https://doi.org/10.3390/asi7050093

Ensafi, Y., Amin, S. H., Zhang, G., & Shah, B. (2022). Time-series forecasting of seasonal items sales using machine learning – A comparative analysis. *International Journal of Information Management Data Insights*, *2*(1), 100058. https://doi.org/10.1016/j.jjimei.2022.100058

Goltsos, T. E., Syntetos, A. A., Glock, C. H., & Ioannou, G. (2022). Inventory–forecasting: Mind the gap. *European Journal of Operational Research*, *299*(2), 397–419. https://doi.org/10.1016/j.ejor.2021.07.040

Haque, M. S., Amin, M. S., & Miah, J. (2023). *Retail demand forecasting: A comparative study for multivariate time series* (arXiv:2308.11939). arXiv. https://arxiv.org/abs/2308.11939

Kirmizi, S. D., Ceylan, Z., & Bulkan, S. (2024). Enhancing inventory management through safety-stock strategies — A case study. *Systems*, *12*(7), 260. https://doi.org/10.3390/systems12070260

Lewis, C. D. (1997). *Demand forecasting and inventory control: A computer aided learning approach*. Woodhead Publishing Limited.

Luo, T. (2019). Traditional book stores industry reforming based on the new management system. *Journal of Physics: Conference Series*, *1213*, 052008. https://doi.org/10.1088/1742-6596/1213/5/052008

Park, M. H., Lee, J. S., & Doo, I. C. (2020). A study of the demand forecasting model for publishing business using business analysis. *International Journal of Computing and Digital Systems*, *9*(5), 801–812.

Taylor, S. J., & Letham, B. (2018). Forecasting at scale. *The American Statistician*, *72*(1), 37–45. https://doi.org/10.1080/00031305.2017.1380080

---

## 12.0 Vedlegg

Følgende vedlegg dokumenterer det tekniske arbeidet og datagrunnlaget:

* **Vedlegg A:** Vasket masterdatasett kan fremvises ved behov.

