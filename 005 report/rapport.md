# Tittel (norsk og/eller engelsk)

Forfatter(e)

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
- Hvis nei: Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven: [ ]

Har oppgaven vært til behandling hos REK? [ ] ja [ ] nei
- Hvis ja: Referansenummer:      

### Publiseringsavtale

Studiepoeng:      
Veileder:      

Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å gjøre oppgaven tilgjengelig for elektronisk publisering: [ ] ja [ ] nei

Er oppgaven båndlagt (konfidensiell)? [ ] ja [ ] nei
- Hvis ja: Kan oppgaven publiseres når båndleggingsperioden er over? [ ] ja [ ] nei

Dato:      

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

### 1.1 Problemstilling

### 1.2 Delproblemer (valgfri)

### 1.3 Avgrensinger

### 1.4 Antagelser
- **Datakvalitet:** Det antas at datakvaliteten i det utleverte datasettet er tilfredsstillende og har blitt gjenstand for intern kvalitetssikring hos leverandøren før utlevering. Dette er nødvendig da det ikke foreligger direkte kilder eller dokumentasjon som beskriver feilrater eller nøyaktighetsgrad i rådataene.

---

## 2.0 Litteratur

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

---

## 5.0 Metode og data

### 5.1 Metode
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
Datasettet som benyttes i denne rapporten er basert på simulerte salgs- og lagerdata for ARK Bokhandel AS. Dataene dekker tre hovedkategorier av bøker med ulike etterspørselsmønstre:
- **Norske barnebøker:** Preget av høy frekvens og tydelige sesongvariasjoner.
- **Norsk krim:** Kjennetegnes av spesifikke salgstopper knyttet til høytider som påske og sommer.
- **Engelsk fiksjon:** Viser en jevnere etterspørsel gjennom året, ofte påvirket av internasjonale trender og importtider.

**Datakvalitet:**
Da det ikke foreligger eksplisitt dokumentasjon på datakvaliteten fra kilden, legges det til grunn en antagelse om at dataene er gjenstand for intern kvalitetssikring hos leverandøren før utlevering. Eventuelle inkonsistenser oppdaget under vaskeprosessen (som datoformater og manglende verdier) er håndtert for å sikre et konsistent analysegrunnlag.

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

---

## 9.0 Diskusjon

---

## 10.0 Konklusjon

---

## 11.0 Bibliografi

---

## 12.0 Vedlegg
