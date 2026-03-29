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

Utfordringene knyttet til disse sesongvariasjonene er tydelige når vi analyserer det historiske forholdet mellom etterspørsel og faktisk tilgjengelighet for ARK:

<div align="center">
  <img src="../006%20analysis/figures/01_ettersporsel_salg_lager.png" alt="Figur 1: Etterspørsel, salg og lager" style="width: 70%; height: auto;">
  <br>
  <em>Figur 1: Sammenheng mellom etterspørsel, faktisk salg og lagerbeholdning over tid. Legg merke til gapet mellom etterspørsel og salg i toppene.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/02_stockouts_over_tid.png" alt="Figur 2: Stockouts over tid" style="width: 70%; height: auto;">
  <br>
  <em>Figur 2: Oversikt over perioder der etterspørselen ikke kunne dekkes av tilgjengelig lager (stockouts).</em>
</div>

Som vist i figur 1 og 2, oppstår de mest kritiske situasjonene i de faste salgstoppene gjennom året. Dette mønsteret gjentas på tvers av kategoriene, men med ulik timing og intensitet, noe som krever en modell som kan fange opp disse mønstrene:

<div align="center">
  <img src="../006%20analysis/figures/08_gjennomsnittlig_salg_per_maaned.png" alt="Figur 3: Gjennomsnittlig salg fordelt på måneder" style="width: 70%; height: auto;">
  <br>
  <em>Figur 3: Gjennomsnittlig salg fordelt på måneder for å identifisere faste sesongsvingninger i casen.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/09_sesongvariasjoner_salg.png" alt="Figur 4: Sesongvariasjoner salg" style="width: 70%; height: auto;">
  <br>
  <em>Figur 4: Detaljert sammenligning av sesongmønstre på tvers av de tre kategoriene som utgjør kjernen i denne analysen.</em>
</div>

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
For å sikre en robust evaluering av etterspørselsprognosene, er datasettet splittet i en treningsdel (80 %) og en testdel (20 %). Denne splitten er avgjørende for å validere modellens evne til å generalisere på usette data.

**Beskrivelse av datagrunnlaget og tekniske visualiseringer:**

<div align="center">
  <img src="../006%20analysis/figures/03_kategori_fordeling_total.png" alt="Figur 5: Kategorifordeling totalt" style="width: 70%; height: auto;">
  <br>
  <em>Figur 5: Fordeling av salgsvolum per kategori i det benyttede datasettet.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/04_kostnads_tradeoff.png" alt="Figur 6: Kostnads-tradeoff" style="width: 70%; height: auto;">
  <br>
  <em>Figur 6: Teknisk analyse av forholdet mellom lagerholdskostnader og mangelkostnader.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/05_svinn_total_oversikt.png" alt="Figur 7: Svinn total oversikt" style="width: 70%; height: auto;">
  <br>
  <em>Figur 7: Total oversikt over registrert svinn i datagrunnlaget.</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/07_totalt_salg_per_aar.png" alt="Figur 8: Totalt salg per år" style="width: 70%; height: auto;">
  <br>
  <em>Figur 8: Utvikling i totalt salgsvolum per år i treningsdataene.</em>
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
- $\delta$: En vektor av ratejusteringer, hvor $\delta_j$ er endringen i vekstrate som oppstår ved endringspunkt $j$.
- $m$: Et offset-parameter (skjæringspunkt med y-aksen).
- $a(t)$: En binær vektor av indikatorfunksjoner slik at $a_j(t) = 1$ dersom $t \ge s_j$, og $0$ ellers, hvor $s_j$ er tidspunktet for endringspunkt $j$.
- $\gamma$: En vektor av justeringsparametre definert som $\gamma_j = -s_j \delta_j$ for å sikre at trendfunksjonen er kontinuerlig.

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
- $\mathbb{1}(\cdot)$: En indikatorfunksjon som er $1$ dersom tidspunkt $t$ er en del av hendelsen $D_i$.

### 6.2 Baseline-løsning
Baseline-strategien fungerer som et sammenligningsgrunnlag for å vurdere merverdien av den avanserte modelleringen. Denne baserer seg på et historisk glidende gjennomsnitt:

$\hat{D}_{t+1} = \frac{1}{n} \sum_{i=t-n+1}^t D_i$

Hvor $\hat{D}_{t+1}$ er prognosen for neste periode, og $n$ er antall historiske observasjoner som inkluderes i gjennomsnittet. Denne strategien representerer en "status quo"-situasjon hvor man bestiller for å dekke et forventet behov uten å dekomponere sesongtrender eller ta høyde for spesifikke kalenderhendelser.

### 6.3 Kvantitativ bestillingsmodell (Optimaliseringsmodell)
Den kvantitative bestillingsmodellen tar utgangspunkt i etterspørselsprognosene fra Prophet. Målet er å bestemme den optimale bestillingsmengden $Q_t$ for hver periode $t$ som minimerer de totale logistikkostnadene.

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
I motsetning til tradisjonelle tidsseriemodeller (som ARIMA), forutsetter ikke Prophet at dataene er stasjonære. Modellen håndterer ikke-stasjonaritet ved å modellere trenden som en stykkevis lineær funksjon. 
*   **Analysefunn:** For *Norsk krim* er det identifisert en positiv trend på ca. 12,7 % over analyseperioden, mens *Engelsk fiksjon* viser en svak negativ trend (-4,8 %). Ved å dekomponere disse trendene unngår vi at langsiktige endringer i popularitet forveksles med sesongvariasjoner.

#### 6.4.2 Sesongkomponenter og helligdagseffekter
Det antas at de historiske sesongmønstrene er representative for fremtidig etterspørsel. 
*   **Amplitude:** Analysen viser kraftige sesongeffekter, spesielt for *Engelsk fiksjon* med en amplitude på ca. 205 enheter rundt de faste sesongtoppene. 
*   **Helligdager:** Effekten av påske, jul og skolestart er modellert som additive sjokk. Det antas at disse hendelsene påvirker etterspørselen i et fast tidsvindu hvert år (f.eks. 15 dager før julaften).

#### 6.4.3 Feilledd og normalfordeling
Det antas at feilleddet $\epsilon_t$ er normalfordelt med forventningsverdi null. Dette er avgjørende for beregning av sikkerhetslager og servicegrad, da vi benytter normalfordelingens fraktiler ($z$-verdier) for å bestemme bestillingspunktet $s_t$.

#### 6.4.4 Lagerstyringsantagelser
*   **Ledetid:** Det antas at ledetiden $L$ er deterministisk eller følger en kjent fordeling basert på historiske leverandørdata.
*   **Mangelkostnad:** Mangelkostnaden $C_s$ er satt betydelig høyere enn lagerholdskostnaden $C_h$ (f.eks. 120 NOK vs 10 NOK for Engelsk fiksjon) for å reflektere den strategiske viktigheten av tilgjengelighet i bokbransjen.
*   **Restordrer:** Som spesifisert i kapittel 1.4, antas det at tapt salg ved stockout er permanent og ikke genererer restordrer ("lost sales"-modell).

---

## 7.0 Analyse
Gjennomgangen av det vaskede datasettet (2021-2025) har avdekket distinkte mønstre for de tre bokkategoriene som er kritiske for valget av prognosemodell:

**Engelsk fiksjon:**
Denne kategorien preges av en relativt stabil etterspørsel gjennom året, men med markerte topper i **juni/juli** (sommerlesing) og **desember** (julesalg). Historikken viser hyppige og omfattende restordrer (stockouts), spesielt i juni 2021 hvor etterspørselen oversteg salget med nesten 300 enheter. Dette indikerer et stort forbedringspotensial ved mer nøyaktige prognoser.

**Norsk krim:**
Krim-kategorien har de mest utpregede sesongtoppene. Toppene er i stor grad knyttet til **juli/august** (feriekrim) og **desember**. I tillegg ser vi en merkbar økning rundt påsketider (mars/april). Dataene viser at etterspørselen ofte bikker 500 enheter i disse periodene, og det er identifisert en svak økende trend i totalvolumet mot slutten av perioden (2024-2025).

**Norske barnebøker:**
Barnebøker viser en jevn og høy frekvens i etterspørselen, men med faste topper i **august** (skolestart) og **desember**. En interessant observasjon er gjentakende stockouts i august-perioden på tvers av flere year, noe som tyder på at nåværende bestillingspraksis konsekvent undervurderer effekten av skolestart.

**Oppsummering av sesongvariasjoner:**
Analysen bekrefter at de viktigste faktorene for en god prognose er evnen til å fange opp de brede sommertoppene og de spisse juletoppene. Ved å benytte en modell som dekomponerer disse sesongene, kan man redusere de observerte stockout-periodene betydelig.

---

## 8.0 Resultat
Resultatene fra den kvantitative analysen sammenligner ytelsen til den Prophet-baserte modellen mot baseline-løsningen over testperioden.

| Kategori | Kostnad Baseline | Kostnad Prophet | Besparelse (%) | SL Baseline | SL Prophet |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Engelsk fiksjon** | 89 267 NOK | 71 802 NOK | 19,57 % | 83,1 % | 86,3 % |
| **Norske barnebøker** | 41 115 NOK | 44 346 NOK | -7,86 % | 85,4 % | 83,8 % |
| **Norsk krim** | 68 254 NOK | 42 247 NOK | 38,10 % | 85,8 % | 91,5 % |
| **TOTALT** | **198 636 NOK** | **158 395 NOK** | **20,26 %** | **84,7 %** | **87,2 %** |

Resultatene viser at den kvantitative modellen gir en total kostnadsbesparelse på over 20 %. Modellen er særlig effektiv for kategorien **Norsk krim**, hvor den reduserer kostnadene med 38,1 % og samtidig øker servicegraden til over 91 %. Dette skyldes modellens evne til å fange opp de ekstreme sesongtoppene og den underliggende trenden som baseline-modellen overser. For *Norske barnebøker* er baseline-modellen konkurransedyktig, noe som indikerer at forutsigbar etterspørsel med lave variasjoner krever mindre avansert modellering.

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
