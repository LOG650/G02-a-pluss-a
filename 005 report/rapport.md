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

4. Jeg/vi er kjent med at alle innlevere oppgaver kan bli plagiatkontrollert i URKUND, se Retningslinjer for elektronisk innlevering og publisering av studiepoenggivende studentoppgaver [ ]

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
3.1 Stasjonaritet og differensiering
3.2 Additive modeller og Prophet
3.3 Lagerstyringsteori
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
*   **Efterspørselens natur:** Ved "stockouts" (utsolgt-situasjoner) antas det at salget går permanent tapt. Kunden antas altså å ikke vente på varen (ingen restordrer i modellen).
*   **Kostnadskonstans:** Lagerholdskostnader og mangelkostnader antas å være konstante gjennom hele analyseperioden.
*   **Datakvalitet:** Det legges til grunn at dataene er gjenstand for intern kvalitetssikring hos leverandøren før utlevering, og at de vaskede dataene gir et korrekt bilde av historiske forhold.

---

## 2.0 Litteratur
Litteraturen som danner grunnlaget for denne rapporten spenner fra klassiske teorier om lagerstyring til moderne, datadrevne tilnærminger for etterspørselsprognosering i detaljhandelen og bokbransjen. Gjennomgangen er strukturert langs prosjektets to hovedakser: (1) etterspørselsprognosering og (2) lagerstyring og kostnadsoptimalisering.

### Etterspørselsprognosering i detaljhandel og bokbransjen

Park et al. (2020) belyser utfordringene med etterspørselsprognosering spesifikt for forlags- og bokbransjen. De understreker viktigheten av å identifisere faktorer som påvirker salgsvolum for å redusere svinn og lagerholdskostnader, og viser hvordan maskinlæringsmodeller kan fange opp komplekse mønstre som tradisjonelle metoder ofte overser. Luo (2019) diskuterer i forlengelsen av dette hvordan tradisjonelle bokhandler må reformeres gjennom nye styringssystemer som utnytter stordata og nettskybaserte løsninger for å holde tritt med markedsendringer.

Taylor og Letham (2018) introduserer Prophet-modellen, en modulær additiv tidsseriemodell designet for prognosering «i stor skala». Modellen dekomponerer tidsserien i trend, sesongvariasjon og helligdagseffekter, og er utviklet for å gi intuitive parametere som analytikere uten spesialisert statistisk bakgrunn kan justere. Modellens evne til å håndtere manglende data, uteliggere og trendskift automatisk gjør den særlig egnet for detaljhandelsdata med uregelmessige sesongmønstre — som er tilfellet for ARK Bokhandel.

Haque et al. (2023) gjennomfører en komparativ studie av ulike prognosemodeller for etterspørsel i detaljhandelen, inkludert regresjonsmodeller og maskinlæringsmetoder. Et sentralt bidrag er inkluderingen av makroøkonomiske variabler — som konsumprisindeks (KPI), forbrukertillitsindeks og arbeidsledighetsrate — som forklaringsvariabler i tillegg til historiske salgsdata. Deres funn viser at modeller som kombinerer tidsseriedata med eksterne faktorer gir bedre prognosenøyaktighet, noe som støtter tilnærmingen i dette prosjektet der sesong- og helligdagseffekter inkluderes eksplisitt i Prophet-modellen. Borucka (2023) sammenligner matematiske metoder for kortsiktig etterspørselsprognosering for produkter med sterke sesongvariasjoner og utviklingstrender. Studien viser at valg av prognosemetode har direkte konsekvenser for forsyningskjeden, og at sesongbaserte metoder gir et vesentlig bedre beslutningsgrunnlag enn enkle gjennomsnitt. Denne innsikten er direkte overførbar til ARK Bokhandels situasjon, der sesongsvingningene er en av de største utfordringene for lagerstyring.

### Lagerstyring og kostnadsoptimalisering

Lewis (1997) gir et klassisk rammeverk for sammenhengen mellom etterspørselsprognoser og lagerstyring. Han skiller mellom ulike typer etterspørsel (stasjonær, sesongavhengig, trendbasert) og hvordan disse krever ulike kontrollstrategier. Chen (2020) bygger videre på dette i en moderne kontekst ved å studere datadrevet lagerstyring i miljøer med «shifting demand». Hans arbeid er særlig relevant for dette prosjektet, da det adresserer situasjoner hvor etterspørselsfordelingen endres over tid — noe som er typisk for sesongvarene hos ARK Bokhandel.

Goltsos et al. (2022) gjennomfører en omfattende litteraturstudie av samspillet mellom etterspørselsprognoser og lagerstyring, og påpeker at de to forskningsfeltene i stor grad har utviklet seg fragmentert. Prognosestudier ignorerer ofte de nedstrøms konsekvensene for lagerbeslutninger, mens lagermodeller gjerne forutsetter at etterspørselen er kjent. Forfatterne foreslår et integrasjonsrammeverk som binder de to disiplinene sammen. Denne innsikten er bærende for strukturen i vårt prosjekt, som eksplisitt kobler Prophet-prognoser til bestillingsparametere som bestillingspunkt (ROP), sikkerhetslager og servicegrad.

Kirmizi et al. (2024) undersøker sikkerhetslagerstrategier gjennom en casestudie og demonstrerer at etterspørselsvariabilitet er den mest kritiske faktoren for dimensjonering av sikkerhetslager. Deres funn om at hybridtilnærminger overgår enkeltmetoder i å redusere totale lagerkostnader, forsterker argumentet for å bruke nøyaktige prognoser som input til lagermodellen — slik det gjøres i dette prosjektet. Adeyemi og Onanuga (2014) gir i tillegg en teoretisk gjennomgang av EOQ-modeller og sikkerhetslagerberegninger under både deterministisk og stokastisk etterspørsel, og danner dermed et supplerende grunnlag for kostnadsvurderingene i denne rapporten.

### Oppsummering og kunnskapsgap
Samlet sett viser litteraturen en bevegelse fra klassiske analytiske modeller (Lewis, 1997; Adeyemi & Onanuga, 2014) mot datadrevne og maskinlæringsbaserte tilnærminger (Taylor & Letham, 2018; Haque et al., 2023; Borucka, 2023). Samtidig avdekkes det et vedvarende gap mellom prognoseforskning og lagerstyringsforskning (Goltsos et al., 2022). Dette prosjektet søker å adressere dette gapet ved å integrere en moderne prognosemodell (Prophet) direkte med kvantitative bestillingsbeslutninger for ARK Bokhandel AS, og dermed binde prognosekvalitet til konkrete lagerstyringsbeslutninger i en kontekst preget av sterke sesongvariasjoner.

---

## 3.0 Teori
For å håndtere etterspørselsprognosering med komplekse sesongvariasjoner og trender, kreves teorier som kan dekomponere tidsserier. Tradisjonelle modeller som SARIMA (Seasonal AutoRegressive Integrated Moving Average) krever stasjonære data og ofte manuell parameterinnstilling, noe som kan være utfordrende med data preget av kraftige salgstopper og uregelmessige hendelser.

### 3.1 Stasjonaritet og differensiering
Et sentralt begrep i tidsserieanalyse er **stasjonaritet**. En tidsserie $\{y_t\}$ sies å være strengt stasjonær dersom dens statistiske egenskaper ikke endrer seg over tid. I praksis fokuserer man ofte på svak stasjonaritet (eller "covariance stationarity"), som krever:
1.  Konstant forventningsverdi: $E[y_t] = \mu$ for alle $t$.
2.  Konstant varians: $Var(y_t) = \sigma^2$ for alle $t$.
3.  Autokovarians som kun avhenger av tidsforskyvningen (lag) $k$, ikke selve tidspunktet $t$.

Dersom en tidsserie har en tydelig trend eller sesongvariasjon, vil den være **ikke-stasjonær**. For å kunne anvende klassiske statistiske modeller, må dataene transformeres til en stasjonær form, vanligvis gjennom **differensiering**:
$\Delta y_t = y_t - y_{t-1}$
Hvor $\Delta y_t$ er den første-ordens differensierte serien. Dersom serien fortsatt ikke er stasjonær, kan man utføre differensiering av høyere orden eller sesong-differensiering.

#### 3.1.1 Augmented Dickey-Fuller (ADF) test
For å teste om en tidsserie er stasjonær på en statistisk signifikant måte, benyttes ofte **Augmented Dickey-Fuller-testen**. Testen undersøker nullhypotesen ($H_0$) om at serien har en enhetsrot (unit root), noe som innebærer at den er ikke-stasjonær. 

Testens regresjonsmodell kan uttrykkes som:
$\Delta y_t = \alpha + \beta t + \gamma y_{t-1} + \sum_{i=1}^p \delta_i \Delta y_{t-i} + \epsilon_t$
Hvor vi tester om $\gamma = 0$ ($H_0$). Dersom test-statistikken er lavere enn den kritiske verdien (eller p-verdien er under signifikansnivået på 0,05), forkastes nullhypotesen til fordel for alternativhypotesen om at serien er stasjonær.

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

Til forskjell fra SARIMA-modeller, som krever at dataene er stasjonære (jf. seksjon 3.1), opererer Prophet direkte på de opprinnelige verdiene uten behov for differensiering. Modellen er designet som et «analyst-in-the-loop»-verktøy (Taylor & Letham, 2018), der intuitive parametere — som styrken på sesongkomponenten og plasseringen av trendskift — kan justeres av analytikere uten spesialisert statistikkbakgrunn. Denne egenskapen gjør Prophet egnet for praktisk beslutningsstøtte i logistikkoperasjoner, som er det overordnede målet for dette prosjektet. De matematiske detaljene for hver komponent presenteres i seksjon 6.1.

### 3.3 Lagerstyringsteori
Mens seksjon 3.1–3.2 dekker det teoretiske grunnlaget for etterspørselsprognosering, omhandler denne seksjonen teorien som knytter prognosene til konkrete lagerbeslutninger. Goltsos et al. (2022) påpeker at disse to disiplinene ofte behandles isolert i litteraturen — dette prosjektet søker å integrere dem.

#### 3.3.1 Bestillingspunkt og sikkerhetslager
I et lagerstyringssystem med kontinuerlig overvåking utløses en ny bestilling når lagerbeholdningen synker til et definert **bestillingspunkt** (Reorder Point, ROP). Bestillingspunktet må dekke forventet etterspørsel i ledetiden pluss et sikkerhetslager som beskytter mot usikkerhet (Lewis, 1997):

$ROP = \hat{D}_L + SS$

Hvor:
- $\hat{D}_L = \hat{d} \cdot L$ er forventet etterspørsel i ledetiden, med $\hat{d}$ som gjennomsnittlig etterspørsel per periode og $L$ som ledetid.
- $SS$ er sikkerhetslageret.

Sikkerhetslageret dimensjoneres ut fra ønsket beskyttelse mot etterspørselssvingninger og beregnes som:

$SS = z_\alpha \cdot \sigma_L$

Hvor $z_\alpha$ er normalfordelingens fraktil (z-verdi) som svarer til ønsket servicenivå $\alpha$, og $\sigma_L = \sigma_d \cdot \sqrt{L}$ er standardavviket for etterspørselen i ledetiden. Her er $\sigma_d$ standardavviket for etterspørselen per periode. Denne formuleringen forutsetter at etterspørselen er tilnærmet normalfordelt og at ledetiden er deterministisk — antagelser som er spesifisert i seksjon 1.4.

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

Forholdet mellom $C_h$ og $C_s$ er avgjørende for det optimale servicenivået. Når mangelkostnaden er vesentlig høyere enn lagerholdskostnaden — som er tilfellet i bokbransjen der tapte salg er permanente (jf. seksjon 1.4) — forskyves det optimale servicenivået oppover, noe som krever større sikkerhetslager.

#### 3.3.4 Kobling mellom prognose og lagerstyring
I dette prosjektet kobles de to teoriblokkene sammen ved at Prophet-prognosene ($\hat{y}(t)$) erstatter $\hat{d}$ i beregningen av bestillingspunktet, og residualene fra modellen ($\epsilon_t$) brukes til å estimere $\sigma_d$. Denne integrasjonen er i tråd med rammeverket foreslått av Goltsos et al. (2022), der prognosekvalitet direkte påvirker lagerbeslutningens kvalitet. Den fullstendige implementeringen av denne koblingen presenteres i seksjon 6.3.

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
Prosjektet følger et kvantitativt forskningsparadigme, der all analyse er basert på numeriske data og statistiske modeller. Forskningsdesignet er en simuleringsbasert case-studie med en todelt tilnærming: først etterspørselsprognosering, deretter kvantitativ bestillingsoptimalisering.

For dette prosjektet er det valgt å benytte **Prophet** som hovedmodell for etterspørselsprognosering. Valget av denne modellen er basert på en drøfting av behovene i bokbransjen og datasettets egenskaper:

**1. Robusthet mot sesongvariasjoner:**
Dataene viser sterke sesongsvingninger på tvers av alle kategorier. Prophet er designet for å håndtere sesongvariasjoner på flere nivåer (månedlig, årlig) uten behov for omfattende datatransformasjoner som differensiering.

**2. Eksplisitt håndtering av helligdager (Holiday Effects):**
Salgsmønstrene for spesielt "Norsk krim" og "Norske barnebøker" viser tydelige topper knyttet til påske, sommerferie og jul. Prophet tillater direkte inkludering av disse effektene, noe som er kritisk for å unngå "stockouts" i perioder med unormalt høy etterspørsel.

**3. Automatisk trenddeteksjon:**
Modellen identifiserer automatisk endringspunkter i trenden. Dette er relevant for å fange opp skift i popularitet for ulike sjangre, for eksempel økt etterspørsel etter engelsk fiksjon drevet av sosiale medier (BookTok).

**4. Prediksjon på faktisk etterspørsel:**
Ved å trene modellen på feltet "Etterspørsel" i stedet for kun "Salg", sikrer vi at modellen lærer det reelle behovet i markedet, uavhengig av historiske lagerbegrensninger.

Metoden innebærer å trene modellen på historiske salgsdata (2021-2025) for å predikere etterspørselen i 2026. Resultatene vil deretter fungere som beslutningsstøtte for den kvantitative bestillingsmodellen.

### 5.2 Data
Datasettet som benyttes i denne rapporten er basert på simulerte salgs- og lagerdata for ARK Bokhandel AS. De tre bokkategoriene er valgt fordi de representerer tre distinkte etterspørselsmønstre, noe som gjør det mulig å teste modellens robusthet på tvers av ulike markedsdynamikker:
- **Norske barnebøker:** Preget av høy frekvens og tydelige sesongvariasjoner, men med høy grad av forutsigbarhet og regelmessighet.
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

Resultatet av denne dekomponeringen er visualisert i figur 9, 10 og 11:

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.8%20utvidet%20feature%20engineering/komponenter_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 9: Komponentanalyse for Engelsk fiksjon. Legg merke til de betydelige utslagene i helligdagskomponenten (nederst) som fanger opp seks identifiserte kampanjer og faste høytider.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.8%20utvidet%20feature%20engineering/komponenter_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 10: Komponentanalyse for Norsk krim. Kategorien viser en svært stabil sesongprofil med kun én identifisert kampanje (mai 2025).</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.8%20utvidet%20feature%20engineering/komponenter_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 11: Komponentanalyse for Norske barnebøker. Modellen fanger opp de faste toppene ved skolestart og jul, supplert med to identifiserte kampanjeperioder.</em>
</div>

#### 6.1.5 Valg av Prophet fremfor SARIMA
Valget av Prophet som primær prognosemodell er basert på en metodisk vurdering opp mot den tradisjonelle SARIMA-modellen (Seasonal AutoRegressive Integrated Moving Average). Selv om begge modellene er stokastiske og kan håndtere sesongvariasjoner, anses Prophet som et mer naturlig valg for denne typen logistikkprosjekt av følgende årsaker:

1. **Håndtering av flere sesongmønstre og helligdager:** Bokbransjen preges av komplekse kalendereffekter, som "bevegelige" helligdager (påske) og faste salgstopper (jul, skolestart). Prophet inkluderer en dedikert komponent for helligdager ($h(t)$) som enkelt fanger opp disse additive sjokkene. I en SARIMA-modell ville dette krevd omfattende bruk av eksterne variabler (SARIMAX) og manuell koding av datoer.
2. **Robusthet mot ikke-stasjonaritet:** SARIMA krever streng stasjonaritet, noe som ofte fordrer flere runder med differensiering og statistisk testing for å transformere dataene. Prophet er en additiv modell som håndterer trender og sesongvariasjoner internt uten behov for omfattende pre-prosessering, noe som reduserer risikoen for feil ved modellspesifisering.
3. **Praktisk tolkbarhet:** Prophet dekomponerer tidsserien i visuelle komponenter (trend, årstid, helligdager). Dette gir et langt mer intuitivt beslutningsgrunnlag for en logistikkansvarlig enn de mer abstrakte matematiske parameterne i en SARIMA-modell (AR- og MA-ordener).
4. **Håndtering av uregelmessige data:** Prophet er robust mot manglende observasjoner og store uteliggere, noe som ofte forekommer i reelle salgsdata fra ERP-systemer.

Samlet sett gir Prophet en bedre balanse mellom statistisk presisjon og praktisk anvendelighet for ARK Bokhandel, da modellen er skreddersydd for tidsserier med sterke menneskeskapte mønstre.

For å illustrere hvordan Prophet dekomponerer etterspørselen, viser figur 12 komponentene for kategorien "Norsk krim" før utvidet feature engineering:

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.5%20kvantitativ%20modell/prophet_components_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 12: Opprinnelig dekomponering av etterspørsel for Norsk krim i trend, helligdager og årlig sesongvariasjon (før inkludering av kampanjeanalyse).</em>
</div>

Modellens estimerte nøkkelparametre for de tre kategoriene er oppsummert i tabellen nedenfor:

| Kategori | Estimert Trend-endring (%) | Sesong-amplitude (enheter) |
| :--- | :---: | :---: |
| **Engelsk fiksjon** | -4,84 % | 204,8 enheter |
| **Norske barnebøker** | -0,10 % | 105,3 enheter |
| **Norsk krim** | +12,70 % | 114,8 enheter |

Full dokumentasjon av basisversjonen av Prophet-modellen, inkludert komponentfigurer for alle tre kategorier, finnes i `006 analysis/milestones/M5 - Kvantitativ analyse/3.5 kvantitativ modell/3.5_Kvantitativ_Modell.md`. Implementasjonen ligger i `004 data/python_skript/prophet_analysis.py`.

### 6.2 Baseline-løsning
Baseline-strategien fungerer som et sammenligningsgrunnlag for å vurdere merverdien av Prophet-modellen, og er implementert som en enkel **(s, Q)-politikk** basert på historiske gjennomsnittstall fra treningsdatasettet (`train_data.csv`). Parameterne beregnes kategorivis som:

- **Forventet etterspørsel:** $\hat{D} = \frac{1}{n} \sum_{i=1}^{n} D_i$ (historisk månedssnitt).
- **Bestillingspunkt:** $s = \hat{D} \cdot \bar{L} \cdot 1{,}10$, hvor $\bar{L}$ er gjennomsnittlig ledetid omregnet til måneder og 10 % er en fast sikkerhetsmargin.
- **Bestillingsmengde:** $Q = \hat{D}$ (snittbehov per måned).

Strategien representerer en «status quo»-situasjon hvor innkjøper bestiller for å dekke et forventet gjennomsnittsbehov uten å dekomponere sesongtrender eller ta høyde for spesifikke kalenderhendelser. De kategorispesifikke baseline-parameterne er oppsummert i tabellen under:

| Kategori | Gj.sn. etterspørsel | Gj.sn. ledetid | Bestillingspunkt ($s$) | Bestillingsmengde ($Q$) |
| :--- | :---: | :---: | :---: | :---: |
| **Engelsk fiksjon** | 338 enheter | 8 dager | 100 enheter | 338 enheter |
| **Norske barnebøker** | 253 enheter | 3 dager | 28 enheter | 253 enheter |
| **Norsk krim** | 348 enheter | 3 dager | 38 enheter | 348 enheter |

Figur 13a–13c illustrerer den karakteristiske (s, Q)-sykelen for hver av de tre kategoriene over testperioden (2025). I hver figur er blå linje lagerbeholdning etter salg, rød stiplet linje markerer bestillingspunktet $s$, oransje søyler viser faktisk etterspørsel, og grønne trekanter markerer månedene hvor en bestilling på $Q$ enheter legges.

For **Engelsk fiksjon** (Figur 13a) ser vi den klassiske sagtannprofilen: lageret tappes ned, en bestilling på $Q = 338$ utløses når beholdningen krysser $s = 88$, og den ankommer i påfølgende periode. Modellen bygger likevel ikke opp ekstra buffer før sesongtoppene i juli/august og desember, og flere måneder har lager på null.

<div align="center">
  <img src="../006%20analysis/figures/15_baseline_sq_sykel_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 13a: Baseline (s, Q)-sykel for Engelsk fiksjon.</em>
</div>

For **Norske barnebøker** (Figur 13b) er det lave bestillingspunktet ($s = 31$) og det relativt lave $Q = 286$ utilstrekkelig for de faste toppene rundt skolestart (august) og jul. Lageret tappes til null allerede tidlig i året og forblir der gjennom høysesongen. Det understreker at selv om kategorien har regelmessige sesongmønstre, krever den et betydelig sikkerhetslager som den enkle baselinen ikke dimensjonerer for.

<div align="center">
  <img src="../006%20analysis/figures/15_baseline_sq_sykel_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 13b: Baseline (s, Q)-sykel for Norske barnebøker.</em>
</div>

For **Norsk krim** (Figur 13c) er ubalansen mest ekstrem: $Q = 365$ ligger under det månedlige gjennomsnittet i testperioden, og kombinert med den positive trenden (+12,7 %) og sterke sesongtopper faller lageret til null allerede i februar. Dette illustrerer at baselinen, basert på historiske snitt, ikke fanger trendutviklingen og systematisk underdimensjonerer volumet.

<div align="center">
  <img src="../006%20analysis/figures/15_baseline_sq_sykel_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 13c: Baseline (s, Q)-sykel for Norsk krim.</em>
</div>

Ved å holde denne baselinen konstant gjennom hele testperioden fanger den verken trendendringer eller sesongeffekter, og forventes derfor å generere stockouts i høysesong – særlig for Norsk krim og Engelsk fiksjon. Dette gjør den til et strengt, men rettferdig sammenligningsgrunnlag for den kvantitative optimaliseringsmodellen i kapittel 6.3. Implementasjonen ligger i `004 data/python_skript/baseline_vs_optimization.py`, som kjører simuleringen og genererer Figur 13a–13c for alle tre kategorier.

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

For å dokumentere serienes egenskaper er det gjennomført både en **Augmented Dickey-Fuller (ADF) test** og en **KPSS-test** på etterspørselsdataene for de tre kategoriene. Resultatene er gjengitt i tabellen under:

| Kategori | ADF p-verdi | KPSS p-verdi | ADF Konklusjon | KPSS Konklusjon | Samlet Vurdering |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **Engelsk fiksjon** | 0,000 | 0,100 | Stasjonær | Stasjonær | Konsistent stasjonær |
| **Norske barnebøker** | 0,001 | 0,100 | Stasjonær | Stasjonær | Konsistent stasjonær |
| **Norsk krim** | 0,000 | 0,100 | Stasjonær | Stasjonær | Konsistent stasjonær |

Ved å kombinere disse to testene, hvor ADF tester for enhetsrot ($H_0$: ikke-stasjonær) og KPSS tester for stasjonaritet ($H_0$: stasjonær), oppnår vi en sterkere statistisk bekreftelse. At testene er samstemte for alle tre kategorier, underbygger at dataene svinger stabilt rundt en trend, noe som gjør Prophet-modellens dekomponering svært egnet for denne typen beslutningsstøtte.

Selv om testene indikerer stasjonaritet (p < 0,05 for ADF og p > 0,05 for KPSS), viser de visuelle analysene i Figur 1 og 9 kraftige, periodiske sesongsvingninger. Valget av Prophet-modellen er derfor begrunnet i dens evne til å modellere disse svingningene og helligdagseffekter eksplisitt, noe som gir bedre beslutningsstøtte enn modeller som utelukkende fokuserer på stasjonaritet gjennom differensiering.

*   **Analysefunn:** Trendanalysen viser stor variasjon mellom kategoriene. Mens *Norsk krim* har en tydelig positiv trend (+12,7 %), viser *Engelsk fiksjon* en svak negativ utvikling (-4,8 %). *Norske barnebøker* skiller seg ut med en svært stabil trend (-0,1 %), noe som indikerer en moden kategori med forutsigbart volum over tid. Ved å dekomponere disse trendene for alle tre kategorier, unngår vi at langsiktige endringer forveksles med sesongsvingninger.

#### 6.4.2 Sesongkomponenter og helligdagseffekter
Det antas at de historiske sesongmønstrene er representative for fremtidig etterspørsel. 
*   **Amplitude:** Analysen viser kraftige sesongeffekter for alle kategorier, men med ulik intensitet. *Engelsk fiksjon* har den høyeste amplituden (ca. 205 enheter), etterfulgt av *Norsk krim* (114,8 enheter) og *Norske barnebøker* (105,3 enheter). 
*   **Helligdager:** Effekten av påske, jul og skolestart er modellert som additive sjokk. Det antas at disse hendelsene påvirker etterspørselen i et fast tidsvindu hvert år (f.eks. 15 dager før julaften).

#### 6.4.3 Feilledd og normalfordeling
Det antas at feilleddet $\epsilon_t$ er normalfordelt med forventningsverdi null. Dette er avgjørende for beregning av sikkerhetslager og servicegrad, da vi benytter normalfordelingens fraktiler ($z$-verdier) for å bestemme bestillingspunktet $s_t$.

#### 6.4.4 Lagerstyringsantagelser
*   **Ledetid:** Det antas at ledetiden $L$ er deterministisk eller følger en kjent fordeling basert på historiske leverandørdata.
*   **Mangelkostnad:** Mangelkostnaden $C_s$ er satt betydelig høyere enn lagerholdskostnaden $C_h$ (f.eks. 120 NOK vs 10 NOK for Engelsk fiksjon) for å reflektere den strategiske viktigheten av tilgjengelighet i bokbransjen.
*   **Restordrer:** Som spesifisert i kapittel 1.4, antas det at tapt salg ved stockout er permanent og ikke genererer restordrer ("lost sales"-modell).

### 6.5 Modellvalidering og Bias-justering (Backtesting)
Før modellen tas i bruk for fremtidige prognoser (2026), er den validert gjennom "backtesting" mot historiske data for 2025. Dette steget er kritisk for å identifisere systematiske skjevheter (bias) i modellen.

| Kategori | MAE | RMSE | MAPE (%) | Bias |
| :--- | :---: | :---: | :---: | :---: |
| **Engelsk fiksjon** | 49,62 | 60,89 | 17,43 % | +15,96 |
| **Norsk krim** | 23,89 | 30,63 | 5,93 % | -11,78 |
| **Norske barnebøker** | 25,47 | 32,10 | 8,68 % | +0,69 |

Analysen viser at modellen for *Engelsk fiksjon* har en positiv bias (overestimering), mens *Norsk krim* har en negativ bias (underestimering). For å sikre optimale bestillinger i 2026, er det i aktivitet 3.10 implementert automatiske bias-korreksjoner som nøytraliserer disse systematiske feilene før bestillingsmengden beregnes.

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
Resultatene fra den kvantitative analysen sammenligner ytelsen til den Prophet-baserte modellen mot baseline-løsningen over testperioden. Den samlede analysepakken (forecast vs. actual, residualer og kostnadsfordeling for alle tre kategorier) er dokumentert i `006 analysis/milestones/M5 - Kvantitativ analyse/3.6 analysepakke/3.6_Analysepakke.md`, og figurene er generert av `004 data/python_skript/generate_m6_visualisations.py`.

| Kategori | Kostnad Baseline | Kostnad Prophet | Besparelse (%) | SL Baseline | SL Prophet |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Engelsk fiksjon** | 89 267 NOK | 71 802 NOK | 19,57 % | 83,1 % | 86,3 % |
| **Norske barnebøker** | 41 115 NOK | 44 346 NOK | -7,86 % | 85,4 % | 83,8 % |
| **Norsk krim** | 68 254 NOK | 42 247 NOK | 38,10 % | 85,8 % | 91,5 % |
| **TOTALT** | **198 636 NOK** | **158 395 NOK** | **20,26 %** | **84,7 %** | **87,2 %** |

### 8.1 Detaljert analyse per kategori
For å forstå de underliggende driverne for besparelsene, dekomponeres resultatene i prognosekvalitet og kostnadsfordeling for hver kategori.

#### 8.1.1 Norsk krim (Høy volatilitet og sterk trend)
Dette er kategorien med størst økonomisk gevinst (38,1 %). Figur 14 viser at Prophet-modellen treffer svært godt på de ekstreme sesongtoppene i testperioden, noe som er kritisk for å unngå utsolgt-situasjoner i høysesong.

<div align="center">
  <img src="../006%20analysis/figures/10_forecast_vs_actual_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 14: Forecast vs. Actual for Norsk krim. Legg merke til hvordan prediksjonen fanger opp de kraftige svingningene i testdataene.</em>
</div>

Ved å analysere residualene (prognosefeilen) i Figur 15, ser vi en tilnærmet normalfordeling med en svak negativ bias. Dette underbygger bruken av sikkerhetslager basert på normalfordelingens fraktiler for å sikre ønsket servicegrad.

<div align="center">
  <img src="../006%20analysis/figures/11_residualer_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 15: Distribusjon av residualer for Norsk krim. Den røde linjen indikerer nullavvik.</em>
</div>

Kostnadsfordelingen i Figur 16 forklarer strategien bak besparelsen: Prophet-modellen aksepterer en moderat økning i lagerholdskostnader ($C_h$) for å oppnå en drastisk reduksjon i de kostbare stockout-hendelsene ($C_s$), noe som gir en netto gevinst på over 26 000 NOK sammenlignet med baseline.

<div align="center">
  <img src="../006%20analysis/figures/12_cost_breakdown_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 16: Kostnadsfordeling for Norsk krim (Baseline vs. Prophet).</em>
</div>

#### 8.1.2 Engelsk fiksjon (Uforutsigbarhet og import)
For Engelsk fiksjon gir modellen en solid besparelse på 19,6 %. Besparelsen drives her primært av en reduksjon i stockouts på over 15 000 NOK. Den høyere usikkerheten i denne kategorien (høyere MAE) gjør at modellen opererer med et relativt sett større sikkerhetslager for å buffer mot import-ledetid og volatilitet.

<div align="center">
  <img src="../006%20analysis/figures/12_cost_breakdown_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 17: Kostnadsfordeling for Engelsk fiksjon.</em>
</div>

#### 8.1.3 Norske barnebøker (Forutsigbare sesongmønstre)
Barnebøker skiller seg ut med et negativt resultat (-7,86 %). Tidligere analyser (kapittel 7.0) viser at denne kategorien har sterke sesongtopper ved skolestart og jul. Diagnosen viser imidlertid at disse mønstrene er så regelmessige og forutsigbare at den enkle baseline-modellen med en fast sikkerhetsmargin fungerer optimalt. Prophet-modellens dynamiske tilnærming, som søker å minimere lageret i lavsesong, har i dette tilfellet ført til for lav sikkerhetsbeholdning i opptakten til de korte og intensive salgstoppene. Dette bekrefter at for varegrupper med svært konsistente sesongsykluser, kan tradisjonelle lagerstyringsmetoder være mer robuste enn avanserte prediksjonsmodeller som er mer utsatt for små feil i timing og usikkerhetsestimering.

### 8.2 Sensitivitetsanalyse og robusthet
For å vurdere modellens pålitelighet er det gjennomført en sensitivitetsanalyse hvor sentrale parametere varieres. Dette er avgjørende for å forstå hvordan modellen håndterer usikkerhet i kostnadsestimater og operasjonelle marginer.

#### 8.2.1 Engelsk fiksjon
For engelsk fiksjon observeres en lineær sammenheng mellom stockout-kostnad og totalkostnad, mens servicenivået forblir stabilt. Dette indikerer en robust modell, men som vist i figur 19, gir en økning i sikkerhetsmarginfaktoren (Safety Margin Factor) til 1.5 en dramatisk forbedring i både kostnad og service.

<div align="center">
  <img src="../006%20analysis/figures/13_sensitivitet_kost_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 18: Kostnadssensitivitet (Engelsk fiksjon).</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/14_sensitivitet_service_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 19: Servicenivå-sensitivitet (Engelsk fiksjon).</em>
</div>

#### 8.2.2 Norske barnebøker
Barnebøker viser høyere sensitivitet for lagerholdskostnad. En reduksjon i denne kostnaden (faktor 0.8) muliggjør et betydelig hopp i servicenivået, da modellen velger å holde mer bufferlager strategisk før sesongtopper.

<div align="center">
  <img src="../006%20analysis/figures/13_sensitivitet_kost_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 20: Kostnadssensitivitet (Norske barnebøker).</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/14_sensitivitet_service_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 21: Servicenivå-sensitivitet (Norske barnebøker).</em>
</div>

#### 8.2.3 Norsk krim
Norsk krim fremstår som den mest stabile kategorien. Som vist i figur 23, oppnår modellen et "metningspunkt" ved en sikkerhetsmarginfaktor på 1.2, hvor ytterligere lagerbeholdning ikke gir gevinst i servicenivå. Dette tyder på at de resterende manglene skyldes uforutsigbare sjokk som faller utenfor modellens rekkevidde gitt ledetiden.

<div align="center">
  <img src="../006%20analysis/figures/13_sensitivitet_kost_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 22: Kostnadssensitivitet (Norsk krim).</em>
</div>

<div align="center">
  <img src="../006%20analysis/figures/14_sensitivitet_service_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 23: Servicenivå-sensitivitet (Norsk krim).</em>
</div>

### 8.3 Optimalisering av Styringsparametere (3.10)
Som et direkte resultat av backtestingen og sensitivitetsanalysen, er de endelige styringsparameterne for 2026-sesongen fastsatt. Disse parameterne representerer modellens "beslutningsregler" og er skreddersydd for å håndtere hver kategoris unike risiko- og etterspørselsprofil.

| Kategori | Bias-justering | Sikkerhetsfaktor (k) | Est. Kampanjeløft |
| :--- | :---: | :---: | :---: |
| **Engelsk fiksjon** | -15,96 | 1,4 | 135,6 enheter |
| **Norsk krim** | +11,78 | 1,8 | 56,6 enheter |
| **Norske barnebøker** | -0,69 | 1,5 | 39,7 enheter |

Disse optimaliserte reglene danner grunnlaget for den endelige prognosegenereringen og scenario-analysen i de påfølgende stegene av prosjektet.

### 8.4 Prognoser for 2026 (Operasjonell Planlegging)
Som det siste steget i den kvantitative analysen er det generert endelige etterspørselsprognoser for hele 2026. Disse prognosene integrerer alle funn fra tidligere steg, inkludert bias-justering fra backtestingen (6.5) og dynamisk beregning av sikkerhetslager basert på de optimaliserte k-faktorene (8.3).

Tabellen nedenfor viser de forventede gjennomsnittlige verdiene per måned for 2026, som danner grunnlaget for ARKs taktiske lagerplanlegging:

| Kategori          | Justert etterspørsel (snitt) | Sikkerhetslager (snitt) | Bestillingspunkt (snitt) |
|:------------------|:----------------------------:|:-----------------------:|:------------------------:|
| Engelsk fiksjon   |            283,82            |          58,39          |          342,21          |
| Norsk krim        |            418,90            |          27,62          |          446,52          |
| Norske barnebøker |            290,59            |          23,41          |          314,00          |

De månedlige svingningene i forventet etterspørsel og det tilhørende behovet for sikkerhetslager er visualisert i figurene 19, 20 og 21. Disse visualiseringene viser hvordan modellen proaktivt øker lagerbeholdningen i forkant av de identifiserte sesongtoppene for å opprettholde målsetningen om leveringsservice.

<div align="center">
  <img src="../006%20analysis/milestones/M6-M8%20-%20Resultater%20og%20rapport/3.11%20prognoser/prognose_2026_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 24: Prognose og sikkerhetslager for Engelsk fiksjon i 2026.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M6-M8%20-%20Resultater%20og%20rapport/3.11%20prognoser/prognose_2026_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 25: Prognose og sikkerhetslager for Norsk krim i 2026.</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M6-M8%20-%20Resultater%20og%20rapport/3.11%20prognoser/prognose_2026_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 26: Prognose og sikkerhetslager for Norske barnebøker i 2026.</em>
</div>

### 8.5 Scenario-analyse (Robusthetstesting)
For å sikre at den foreslåtte bestillingsmodellen er robust mot uforutsette endringer i markedsforholdene, er det gjennomført en scenario-analyse for 2026. To ulike ytterpunkter er testet mot baseline-prognosen:

1.  **Scenario A (Kampanje-sjokk):** Simulerer en situasjon der kampanjene i mai og desember gir 50 % høyere løft enn historisk snitt, kombinert med en 20 % økning i sikkerhetslageret for å håndtere økt volatilitet.
2.  **Scenario B (Kostnads-sjokk):** Simulerer en kraftig økning i lagerholdskostnader (f.eks. strøm og husleie), som tvinger frem en 20 % reduksjon i sikkerhetslageret for å minimere kapitalbinding.

**Antagelser og datakvalitet:**
Analysen antar at sesongmønsteret fra de siste 4 årene vedvarer i 2026. Kampanjeløftet i scenario A er basert på historisk effekt pluss et estimert sjokk (50% økning av gjennomsnittlig løft). Modellen tar høyde for normal volatilitet, men ekstreme "Sorte svaner" er ikke inkludert i simuleringen.

Tabellen nedenfor oppsummerer hvordan det gjennomsnittlige lagernivået (Order-up-to level) må justeres i de ulike scenariene:

| Kategori | Baseline (Units) | Scenario A: Kampanje-sjokk | Scenario B: Kostnads-sjokk |
| :--- | :---: | :---: | :---: |
| **Engelsk fiksjon** | 409,2 | +6,8 % | -4,0 % |
| **Norsk krim** | 451,9 | +2,3 % | -1,2 % |
| **Norske barnebøker** | 317,2 | +2,6 % | -1,6 % |

Analysen viser at *Engelsk fiksjon* er mest sensitiv for kampanje-sjokk, med et behov for 6,8 % økning i lagernivået for å opprettholde servicegraden. For *Norsk krim* og *Norske barnebøker* er modellen svært robust, med mindre enn 3 % endring i nødvendig beholdning selv ved ekstreme utslag. Dette gir ARK Bokhandel trygghet for at de optimaliserte reglene fra 3.10 vil fungere tilfredsstillende også i et urolig marked.

De visuelle forskjellene i lagernivå for de ulike scenariene er presentert i figurene 22, 23 og 24:

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.12%20scenario-analyse/scenario_plot_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 27: Scenario-sammenligning for Engelsk fiksjon i 2026</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.12%20scenario-analyse/scenario_plot_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 28: Scenario-sammenligning for Norsk krim i 2026</em>
</div>

<div align="center">
  <img src="../006%20analysis/milestones/M5%20-%20Kvantitativ%20analyse/3.12%20scenario-analyse/scenario_plot_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 29: Scenario-sammenligning for Norske barnebøker i 2026</em>
</div>

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
Adeyemi, A. A., & Onanuga, A. T. (2014). Dynamics of inventory cost optimization — A review of theory and evidence. *Research Journal of Finance and Accounting*, *5*(22).

Borucka, A. (2023). Seasonal methods of demand forecasting in the supply chain as support for the company's sustainable growth. *Sustainability*, *15*(9), 7399. https://doi.org/10.3390/su15097399

Chen, B. (2020). *Data-Driven Inventory Control with Shifting Demand*. College of Business Administration, University of Illinois at Chicago.

Goltsos, T. E., Syntetos, A. A., Glock, C. H., & Ioannou, G. (2022). Inventory–forecasting: Mind the gap. *European Journal of Operational Research*, *299*(2), 397–419. https://doi.org/10.1016/j.ejor.2021.07.040

Haque, M. S., Amin, M. S., & Miah, J. (2023). Retail demand forecasting: A comparative study for multivariate time series. *arXiv preprint arXiv:2308.11939*. https://arxiv.org/abs/2308.11939

Kirmizi, S. D., Ceylan, Z., & Bulkan, S. (2024). Enhancing inventory management through safety-stock strategies — A case study. *Systems*, *12*(7), 260. https://doi.org/10.3390/systems12070260

Lewis, C. D. (1997). *Demand forecasting and inventory control: A computer aided learning approach*. Woodhead Publishing Limited.

Luo, T. (2019). Traditional book stores industry reforming based on the new management system. *Journal of Physics: Conference Series*, *1213*, 052008. https://doi.org/10.1088/1742-6596/1213/5/052008

Park, M. H., Lee, J. S., & Doo, I. C. (2020). A study of the demand forecasting model for publishing business using business analysis. *International Journal of Computing and Digital Systems*, *9*(5), 801–812.

Taylor, S. J., & Letham, B. (2018). Forecasting at scale. *The American Statistician*, *72*(1), 37–45. https://doi.org/10.1080/00031305.2017.1380080

---

## 12.0 Vedlegg
Følgende vedlegg dokumenterer det tekniske arbeidet og datagrunnlaget:
*   **Vedlegg A:** Python-skript for datavask og visualisering (`vask_og_strukturer.py`).
*   **Vedlegg B:** Modellkode for Prophet-prognoser og kostnadsoptimalisering (`final_simulation.py`).
*   **Vedlegg C:** Skript for avansert resultatanalyse og visualisering (`generate_m6_visualisations.py`).
*   **Vedlegg D:** Vasket masterdatasett (`master_data_vasket.csv`).
*   **Vedlegg E:** Detaljerte figurer over sesongvariasjoner, residualer og kostnadsfordeling per kategori.
