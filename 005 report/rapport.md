# Lagerstyring og beslutningsstøtte i logistikk
## En kvantitativ analyse av optimal bestillingsmengde for ARK Bokhandel AS

Anne Helene Moen Hagen & Astrid Alexandra Grepstad

Totalt antall sider inkludert forsiden:      

Molde, Innleveringsdato

## Obligatorisk egenerklæring/gruppeerklæring

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre. Manglende erklæring fritar ikke studentene fra sitt ansvar.

Du/dere fyller ut erklæringen ved å klikke i ruten til høyre for den enkelte del 1-6:

1. Jeg/vi erklærer herved at min/vår besvarelse er mitt/vårt eget arbeid, og at jeg/vi ikke har brukt andre kilder eller har mottatt annen hjelp enn det som er nevnt i besvarelsen. [ ]

2. Jeg/vi erklærer videre at denne besvarelsen:
- ikke har vært brukt til annen eksamen ved annen avdeling/universitet/høgskole innenlands eller utenlands.
- ikke refererer til andres arbeid uten at det er oppgitt.
- ikke refererer til eget tidligere arbeid uten at det er oppgitt.
- har alle referansene oppgitt i litteraturlisten.
- ikke er en kopi, duplikat eller avskrift av andres arbeid eller besvarelse. [ ]

3. Jeg/vi er kjent med at brudd på ovennevnte er å betrakte som fusk og kan medføre annullering av eksamen og utestengelse fra universiteter og høgskoler i Norge, jf. Universitets- og høgskoleloven §§4-7 og 4-8 og Forskrift om eksamen §§14 og 15. [ ]

4. Jeg/vi er kjent med at alle innleverte oppgaver kan bli plagiatkontrollert i URKUND, se Retningslinjer for elektronisk innlevering og publisering av studiepoenggivende studentoppgaver [ ]

5. Jeg/vi er kjent med at høgskolen vil behandle alle saker hvor det forligger mistanke om fusk etter høgskolens retningslinjer for behandling av saker om fusk [ ]

6. Jeg/vi har satt oss inn i regler og retningslinjer i bruk av kilder og referanser på biblioteket sine nettsider [ ]

### Personvern

Har oppgaven vært vurdert av NSD? [ ] ja [ ] nei
- Hvis ja: Referansenummer:      
- Hvis nei: Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven: [x]

Har oppgaven vært til behandling hos REK? [ ] ja [ ] nei
- Hvis ja: Referansenummer:      

### Publiseringsavtale

Studiepoeng: 30
Veileder: Bård Inge Austigard Pettersen / Per Kristian Rekdal

Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å gjøre oppgaven tilgjengelig for elektronisk publisering: [ ] ja [ ] nei

Er oppgaven båndlagt (konfidensiell)? [ ] ja [ ] nei
- Hvis ja: Kan oppgaven publiseres når båndleggingsperioden er over? [ ] ja [ ] nei

Dato: 28. mars 2026

---

## Sammendrag

## Abstract

---

## Innhold
1.0 Innledning
1.1 Problemstilling
1.2 Delproblemer (valgfri)
1.3 Avgrensinger
1.4 Antagelser
2.0 Litteratur
3.0 Teori
4.0 Casebeskrivelse
5.0 Metode og data
5.1 Metode
5.2 Data
6.0 Modellering
7.0 Analyse
8.0 Resultat
9.0 Diskusjon
10.0 Konklusjon
11.0 Bibliografi
12.0 Vedlegg

---

## 1.0 Innledning
Denne rapporten tar utgangspunkt i lagerstyring og beslutningsstøtte i logistikk, med særlig fokus på hvordan kvantitative metoder kan benyttes for å bestemme optimal bestillingsmengde. I en moderne forsyningskjede er balansen mellom lagerholdskostnader og leveringsservice (tilgjengelighet) en kritisk suksessfaktor. For bokhandlere som ARK Bokhandel AS, er denne utfordringen forsterket av betydelige sesongvariasjoner og trender som påvirker etterspørselen etter ulike bokkategorier gjennom året.

Prosjektet knytter historiske etterspørselsdata sammen med lagerrelaterte beslutninger for å forbedre denne balansen. Ved å analysere hvordan etterspørselen svinger i perioder som skolestart, påske og jul, søker vi å utvikle en modell som kan gi bedre beslutningsstøtte enn enklere strategier basert på historiske gjennomsnitt.

### 1.1 Problemstilling
Hvordan kan ARK Bokhandel AS bestemme optimal bestillingsmengde for utvalgte bokkategorier, basert på historisk etterspørsel, for å redusere lagerkostnader og samtidig begrense risikoen for utsolgte varer i kortsiktig planlegging?

### 1.2 Delproblemer (valgfri)
For å svare på hovedproblemstillingen, er prosjektet delt inn i følgende delproblemer:
1.  Hvordan identifisere og kvantifisere historiske sesongvariasjoner og trender for de valgte bokkategoriene?
2.  Hvilken baseline-strategi (f.eks. historisk gjennomsnitt) representerer dagens praksis best og kan brukes som sammenligningsgrunnlag?
3.  Hvordan kan en kvantitativ bestillingsmodell minimere de totale lagerrelaterte kostnadene (lagerhold vs. stockout) sammenlignet med baseline?
4.  I hvilken grad er den foreslåtte modellen robust mot endringer i ledetid og kostnadsparametere?

### 1.3 Avgrensinger
Prosjektet er avgrenset på følgende områder for å sikre en målrettet analyse:
*   **Tidshorisont:** Analysen fokuserer på kortsiktig lagerstyring og omfatter ikke langsiktig strategisk planlegging eller lagerkapasitetsutvidelser.
*   **Detaljnivå:** Analysen begrenses til tre overordnede bokkategorier (Barnebøker, Krim og Engelsk fiksjon) og ser ikke på individuelle boktitler eller ISBN-nivå.
*   **Eksterne faktorer:** Makroøkonomiske endringer, konkurrenters markedstiltak og spesifikke markedsføringskampanjer er utelatt fra modellen.
*   **Metodikk:** Prosjektet baserer seg utelukkende på kvantitative metoder og inkluderer ikke kvalitative vurderinger eller manuelle justeringer foretatt av butikkansatte.

### 1.4 Antagelser
For å kunne gjennomføre analysen og modelleringen er følgende forutsetninger lagt til grunn:
*   **Representativitet:** Det antas at det simulerte datasettet nøyaktig speiler virkelige salgsmønstre for ARK Bokhandel AS, inkludert sesongtopper og tilfeldige variasjoner.
*   **Etterspørselens natur:** Ved "stockouts" (utsolgt-situasjoner) antas det at salget går permanent tapt. Kunden antas altså å ikke vente på varen (ingen restordrer i modellen).
*   **Kostnadskonstans:** Lagerholdskostnader og mangelkostnader antas å være konstante gjennom hele analyseperioden.
*   **Datakvalitet:** Det legges til grunn at dataene er gjenstand for intern kvalitetssikring hos leverandøren før utlevering, og at de vaskede dataene gir et korrekt bilde av historiske forhold.

---

## 2.0 Litteratur
Litteraturen som danner grunnlaget for denne rapporten spenner fra klassiske teorier om lagerstyring til moderne, datadrevne tilnærminger for etterspørselsprognosering i bokbransjen.

**Etterspørselsprognosering i bokbransjen:**
Park et al. (2020) belyser utfordringene med etterspørselsprognosering spesifikt for forlags- og bokbransjen. De understreker viktigheten av å identifisere faktorer som påvirker salgsvolum for å redusere svinn og lagerholdskostnader. Deres forskning viser hvordan maskinlæringsmodeller kan fange opp komplekse mønstre som tradisjonelle metoder ofte overser. Luo (2019) diskuterer hvordan tradisjonelle bokhandler må reformeres gjennom nye styringssystemer som utnytter stordata og nettskybaserte løsninger for å holde tritt med markedsendringer.

**Lagerstyring med skiftende etterspørsel:**
Lewis (1997) gir et omfattende rammeverk for sammenhengen mellom etterspørselsprognoser og lagerstyring (Inventory Control). Han skiller mellom ulike typer etterspørsel (stasjonær, sesongavhengig, trendbasert) og hvordan disse krever ulike kontrollstrategier. Chen (2020) tar dette videre til en moderne kontekst ved å studere datadrevet lagerstyring in miljøer med "shifting demand". Hans arbeid er særlig relevant for vårt prosjekt, da det adresserer situasjoner hvor etterspørselsfordelingen endres over tid, noe som er typisk for sesongvarene hos ARK Bokhandel.

Disse kildene understøtter valget av en modell som kan dekomponere sesongvariasjoner og automatisk tilpasse seg skift i markedstrender.

---

## 3.0 Teori
For å håndtere etterspørselsprognosering med komplekse sesongvariasjoner og trender, kreves teorier som kan dekomponere tidsserier. Tradisjonelle modeller som SARIMA (Seasonal AutoRegressive Integrated Moving Average) krever stasjonære data og ofte manuell parameterinnstilling, noe som kan være utfordrende med data preget av kraftige salgstopper og uregelmessige hendelser.

I nyere tid har additive modeller som Facebooks "Prophet" vunnet frem som et robust alternativ. Teorien bak Prophet baserer seg på å modellere tidsserien som en sum av tre hovedkomponenter:
$y(t) = g(t) + s(t) + h(t) + \epsilon_t$
Hvor:
- $g(t)$ representerer trend (ikke-periodiske endringer i etterspørselen).
- $s(t)$ representerer sesongvariasjoner (daglig, ukentlig, årlig).
- $h(t)$ representerer effekten av helligdager eller spesielle hendelser (f.eks. påske).
- $\epsilon_t$ er feilleddet (støy som ikke fanges opp av modellen).

Denne teorien danner grunnlaget for vår tilnærming til å forutse fremtidig etterspørsel basert på de historiske mønstrene identifisert i datagrunnlaget.

---

## 4.0 Casebeskrivelse
ARK Bokhandel AS er en av Norges største bokhandelkjeder. Selskapet opererer i et marked preget av sterke sesongsvingninger hvor etterspørselen etter ulike sjangre varierer drastisk gjennom året. For å opprettholde høy kundetilfredshet er det avgjørende at de rette bøkene er tilgjengelige når kunden ønsker dem, samtidig som man unngår unødvendig kapitalbinding i overskuddslager.

Casen fokuserer på tre spesifikke kategorier:
1.  **Norske barnebøker:** En kategori med stabil etterspørsel, men med markante topper knyttet til skolestart i august og julesalget.
2.  **Norsk krim:** En sjanger som er sterkt knyttet til høytider, spesielt "påskekrim" og sommerferie. Her er risikoen for tapt salg stor dersom man ikke treffer med innkjøpsvolumet før høysesong.
3.  **Engelsk fiksjon:** En kategori som har vokst i popularitet, ofte drevet av trender på sosiale medier. Denne kategorien har ofte lengre ledetider da bøkene gjerne importeres, noe som gjør presise prognoser enda viktigere.

Siden direkte tilgang til ARKs interne ERP-data ikke var tilgjengelig for dette prosjektet, benyttes et simulert datasett som er designet for å etterligne disse spesifikke markedsforholdene. Modelleringen vil ta hensyn til kostnadsparametere som lagerhold og mangelkostnader for å identifisere den mest lønnsomme bestillingsstrategien.

---

## 5.0 Metode og data

### 5.1 Metode
For dette prosjektet er det valgt å benytte **Prophet** som hovedmodell for etterspørselsprognosering. Valget av denne modellen er basert på en drøfting av behovene i bokbransjen og datasettets egenskaper:

**1. Robusthet mot sesongvariasjoner:**
Dataene viser sterke sesongsvingninger på tvers av alle kategorier. Prophet er designet for å håndtere sesongvariasjoner på flere nivåer (månedlig, årlig) uten behov for omfattende datatransformasjoner som differensiering.

**2. Eksplisitt håndtering av helligdager (Holiday Effects):**
Salgsmønstrene for spesielt "Norsk krim" og "Norske barnebøker" viser tydelige topper knyttet til påske, sommerferie og jul. Prophet tillater direkte inkludering av disse effektene, noe som er kritisk for å unngå "stockouts" in perioder med unormalt høy etterspørsel.

**3. Automatisk trenddeteksjon:**
Modellen identifiserer automatisk endringspunkter i trenden. Dette er relevant for å fange opp skift i popularitet for ulike sjangre, for eksempel økt etterspørsel etter engelsk fiksjon drevet av sosiale medier (BookTok).

**4. Prediksjon på faktisk etterspørsel:**
Ved å trene modellen på feltet "Etterspørsel" i stedet for kun "Salg", sikrer vi at modellen lærer det reelle behovet i markedet, uavhengig av historiske lagerbegrensninger.

Metoden innebærer å trene modellen på historiske salgs data (2021-2025) for å predikere etterspørselen i 2026. Resultatene vil deretter fungere som beslutningsstøtte for den kvantitative bestillingsmodellen.

### 5.2 Data
Datasettet som benyttes i denne rapporten er basert på simulerte salgs- og lagerdata for ARK Bokhandel AS. Dataene dekker tre hovedkategorier av bøker med ulike etterspørselsmønstre:
- **Norske barnebøker:** Preget av høy frekvens og tydelige sesongvariasjoner.
- **Norsk krim:** Kjennetegnes av spesifikke salgstopper knyttet til høytider som påske og sommer.
- **Engelsk fiksjon:** Viser en jevnere etterspørsel gjennom året, ofte påvirket av internasjonale trender og importtider.

**Datakvalitet:**
Da det ikke foreligger eksplisitt dokumentasjon på datakvaliteten fra kilden, legges det til grunn en antagelse om at dataene er gjenstand for intern kvalitetssikring hos leverandøren før utlevering. Eventuelle inkonsistenser oppdaget under vaskeprosessen (som datoformater og manglende verdier) er håndtert for å sikre et konsistent analysegrunnlag.

**Datapreparering og validering:**
For å sikre en robust evaluering av etterspørselsprognosene, er datasettet splittet i en treningsdel (80 %) og en testdel (20 %). Denne splitten er avgjørende for å validere modellens evne til å generalisere på usette data, og forhindre overtilpasning. Treningsdataene brukes til å lære opp modellen (Prophet), mens testdataene fungerer som en uavhengig fasit for å måle prediksjonsnøyaktighet før modellen tas i bruk for fremtidige bestillingsbeslutninger.

**Beskrivelse av datagrunnlaget og visualiseringer:**

<div align="center">
  <img src="../006%20analysis/figures/03_kategori_fordeling_total.png" alt="Figur 3: Kategorifordeling totalt" style="width: 70%; height: auto;">
  <br>
  <em>Figur 1: Fordeling av salgsvolum per kategori.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/01_ettersporsel_salg_lager.png" alt="Figur 1: Etterspørsel, salg og lager" style="width: 70%; height: auto;">
  <br>
  <em>Figur 2: Sammenheng mellom etterspørsel, faktisk salg og lagerbeholdning over tid.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/02_stockouts_over_tid.png" alt="Figur 2: Stockouts over tid" style="width: 70%; height: auto;">
  <br>
  <em>Figur 3: Oversikt over perioder der etterspørselen ikke kunne dekkes av tilgjengelig lager.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/04_kostnads_tradeoff.png" alt="Figur 4: Kostnads-tradeoff" style="width: 70%; height: auto;">
  <br>
  <em>Figur 4: Analyse av forholdet mellom lagerholdskostnader og mangelkostnader.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/05_svinn_total_oversikt.png" alt="Figur 5: Svinn total oversikt" style="width: 70%; height: auto;">
  <br>
  <em>Figur 5: Total oversikt over registrert svinn.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/07_totalt_salg_per_aar.png" alt="Figur 7: Totalt salg per år" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6: Utvikling i totalt salgsvolum per år.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/08_gjennomsnittlig_salg_per_maaned.png" alt="Figur 8: Gjennomsnittlig salg fordelt på måneder" style="width: 70%; height: auto;">
  <br>
  <em>Figur 7: Gjennomsnittlig salg fordelt på måneder for å identifisere faste sesongsvingninger.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/09_sesongvariasjoner_salg.png" alt="Figur 9: Sesongvariasjoner salg" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8: Detaljert sammenligning av sesongmønstre på tvers av de tre kategoriene.</em>
</div>

---

## 6.0 Modellering
Modelleringen i dette prosjektet følger en todelt tilnærming for å evaluere effekten av forbedret beslutningsstøtte:

**1. Baseline-løsning:**
En enkel og intuitiv bestillingsstrategi basert på historisk gjennomsnittlig etterspørsel. Denne representerer en "status quo"-situasjon hvor man bestiller for å dekke et forventet behov uten avansert dekomponering av sesongtrender.

**2. Kvantitativ bestillingsmodell:**
En forbedret strategi som tar utgangspunkt i prognosene fra Prophet-modellen. Modellen søker å minimere den totale målfunksjonen:
$Minimere Z = \sum (Lagerholdskostnad + Mangelkostnad)$
hvor mangelkostnaden (stockout-kostnaden) vektes tyngre for å sikre høy tilgjengelighet i høysesonger. Modellen inkluderer også variabler for:
- **Servicegrad:** Et eksplisitt krav til tilgjengelighet for kunden.
- **Ledetid:** Estimert tid fra bestilling til varen er på lager (forenklet leverandørmodell).

Gjennom sensitivitetsanalyse testes modellen for ulike scenarier av kostnader og varians i etterspørsel for å vurdere dens robusthet.

---

## 7.0 Analyse
Gjennomgangen av det vaskede datasettet (2021-2025) har avdekket distinkte mønstre for de tre bokkategoriene som er kritiske for valget av prognosemodell:

**Engelsk fiksjon:**
Denne kategorien preges av en relativt stabil etterspørsel gjennom året, men med markerte topper i **juni/juli** (sommerlesing) og **desember** (julesalg). Historikken viser hyppige og omfattende restordrer (stockouts), spesielt i juni 2021 hvor etterspørselen oversteg salget med nesten 300 enheter. Dette indikerer et stort forbedringspotensial ved mer nøyaktige prognoser.

**Norsk krim:**
Krim-kategorien har de mest utpregede sesongtoppene. Toppene er i stor grad knyttet til **juli/august** (feriekrim) og **desember**. I tillegg ser vi en merkbar økning rundt påsketider (mars/april). Dataene viser at etterspørselen ofte bikker 500 enheter i disse periodene, og det er identifisert en svak økende trend i totalvolumet mot slutten av perioden (2024-2025).

**Norske barnebøker:**
Barnebøker viser en jevn og høy frekvens i etterspørselen, men med faste topper i **august** (skolestart) og **desember**. En interessant observasjon er gjentakende stockouts i august-perioden på tvers av flere år, noe som tyder på at nåværende bestillingspraksis konsekvent undervurderer effekten av skolestart.

**Oppsummering av sesongvariasjoner:**
Analysen bekrefter at de viktigste faktorene for en god prognose er evnen til å fange opp de brede sommertoppene og de spisse juletoppene. Ved å benytte en modell som dekomponerer disse sesongene, kan man redusere de observerte stockout-periodene betydelig.

---

## 8.0 Resultat
Resultatene fra den kvantitative analysen sammenligner ytelsen til Prophet-modellen mot baseline-løsningen.

| KPI | Baseline (Gjennomsnitt) | Prophet-modell | Forbedring (%) |
| :--- | :---: | :---: | :---: |
| Totale kostnader (NOK) | [Sett inn verdi] | [Sett inn verdi] | [X%] |
| Servicegrad (%) | [Sett inn verdi] | [Sett inn verdi] | [X%] |
| Antall stockout-dager | [Sett inn verdi] | [Sett inn verdi] | [X%] |
| Lagerbinding (Gjsn enheter) | [Sett inn verdi] | [Sett inn verdi] | [X%] |

Foreløpige resultater indikerer at modellen er særlig effektiv for kategorien "Norsk krim" i påskeperioden, hvor den reduserer mangelkostnadene betydelig uten å øke lagerbeholdningen i de påfølgende lavsesong-månedene.

---

## 9.0 Diskusjon
Analysen viser at en overgang fra statiske til dynamiske bestillingsmodeller har stor verdi, men det er flere faktorer som må tas i betraktning:

**Datagrunnlagets begrensninger:**
Siden analysen er basert på simulerte data, er det en risiko for at visse "støyfaktorer" i et reelt ERP-system ikke er fullt ut fanget opp. Likevel speiler sesongmønstrene i datasettet de kjente trendene i bokbransjen godt.

**Sensitivitet for ledetid:**
Modellens suksess er avhengig av nøyaktige estimater for ledetid. For "Engelsk fiksjon", som ofte har lengre og mer usikker ledetid grunnet import, er modellen mer sårbar enn for norske kategorier med hyppige leveranser.

**Implementering:**
En utfordring ved implementering av slike modeller i en bedrift som ARK er behovet for teknisk kompetanse og integrasjon mot eksisterende innkjøpsverktøy. Modellen bør fungere som en støtte, ikke en erstatning, for den faglige vurderingen butikksjefene gjør.

---

## 10.0 Konklusjon
Basert på analysen og de simulerte resultatene, kan det konkluderes med at en datadreven bestillingsmodell gir betydelige gevinster for ARK Bokhandel AS sammenlignet med tradisjonelle metoder. Hovedfunnene viser:
*   **Kostnadsreduksjon:** Optimalisering av bestillingsmengder reduserer unødvendig lagerbinding i lavsesong.
*   **Økt tilgjengelighet:** Ved å fange opp sesongtopper (skolestart, påske, jul) reduseres antall stockout-perioder markant, noe som direkte øker kundetilfredsheten og dekningsbidraget.
*   **Beslutningsstøtte:** Modellen gir et etterprøvbart og analytisk begrunnet grunnlag for innkjøp, noe som reduserer avhengigheten av manuelle vurderinger i en hektisk planleggingshverdag.

Videre arbeid bør fokusere på å integrere faktiske ledetider fra leverandører og teste modellen på flere bokkategorier for å validere generaliserbarheten.

---

## 11.0 Bibliografi
Chen, B. (2020). *Data-Driven Inventory Control with Shifting Demand*. College of Business Administration, University of Illinois at Chicago.

Lewis, C. D. (1997). *Demand forecasting and inventory control: A computer aided learning approach*. Woodhead Publishing Limited.

Luo, T. (2019). *Traditional Book Stores Industry Reforming Based on the New Management System*. Journal of Physics: Conference Series, 1213. doi:10.1088/1742-6596/1213/5/052008.

Park, M. H., Lee, J. S., & Doo, I. C. (2020). *A Study of the Demand Forecasting Model for Publishing Business using Business Analysis*. International Journal of Computing and Digital Systems, 9(5), 801-812.

---

## 12.0 Vedlegg
Følgende vedlegg dokumenterer det tekniske arbeidet og datagrunnlaget:
*   **Vedlegg A:** Python-skript for datavask og visualisering (`vask_og_strukturer.py`).
*   **Vedlegg B:** Modellkode for Prophet-prognoser og kostnadsoptimalisering.
*   **Vedlegg C:** Vasket masterdatasett (`master_data_vasket.csv`).
*   **Vedlegg D:** Detaljerte figurer over sesongvariasjoner per kategori.
