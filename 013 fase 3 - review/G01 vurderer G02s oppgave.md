# Peer-review av rapport fra Gruppe G02

**Vurderende gruppe:** Gruppe G01

**Tittel på rapporten:** Lagerstyring og beslutningsstøtte i logistikk - En kvantitativ analyse av optimal bestillingsmengde for ARK Bokhandel AS

**Dato:** 7. mai 2026

## Helhetsinntrykk

Rapporten fremstår som et svært godt teoretisk forankret og gjennomarbeidet produkt. Caset er relevant og realistisk. Det er en tydelig rød tråd fra problemstilling til konklusjon. Koblingen mellom etterspørselsprogonser og lagerstyring er godt gjennomført

Hovedfunn:

1. Skillet mellom simulerte data og antakelser kunne vært tydeligere
2. Liten grad av sammenlikning mellom modeller og liten grad av kritisk refleksjon
3. Rapporten mangler eksplisitt beskrivelse av bruk av KI

## Områdevis vurdering

### Kapittel 1 Innledning

**Styrker:** Klar og relevant problemstilling som er tydelig koblet til logistikk og beslutningsstøtte.
Delproblemene er konkrete og analytiske og bygger logisk opp mot hovedproblem
Avgrensninger og antakelser er tydelige og ryddige.
God kontekstualisering av caset med ARK og sesongvariasjon.

**Forbedring:** Litt generisk i starten, kanskje dette kan spisses mer mot bokbransjen eller konkret ARK i starten. Forsyningskjede er litt bredt. Innholdsfortegnelse mangler sidetall

### Kapittel 2 & 3 Litteraturgjennomgang og teoretisk forankring

**Styrker:** Gjennomgangen av forskningen på temaet presenteres på en ryddig og oversiktlig måte.
Både litteraturkapittelet og teorikapittelet har samme inndelingen (prognose og lagerstyring), dette gjør at det er en tydelig rød tråd til det oppgaven forsøker å svare på. De identifiserer at (se 3.3) etterspørselsprognostisering og konkrete lagerbeslutninger behandles isolert i litteraturen (Goltsos et al. (2022)) og at oppgaven således forsøker å lage en modell som sammenstiller begge metodene. Teorikapittelet har den samme tydelige progresjonen mellom tidsserieteori og prognosering.

**Forbedring:** Lite kritikk eller vurdering av styrker og svakheter ved de forskjellige modellene både i litteratur og teorikapittelet. Noen av kildene er eldre enn 5 år. Teorikapittelet oppleves som noe tungt å lese med mange matematiske notasjoner (krever LaTeX kunnskap)

### Kapittel 4 - Casebeskrivelse

**Styrker:** God og intuitiv introduksjon. Caset fremstår som relevant og realistisk. Tydelige etterspørselsmønstre i de tre kategoriene gir et godt grunnlag for videre analyse. Visualiseringene bidrar positivt til problemforståelsen.

**Forbedring:** Figur ser ut til å vise et aggregert bilde av etterspørselen, salg og lagerbeholdning på tvers av de tre kategoriene, men det kommer ikke helt tydelig frem at dataene for alle tre kategoriene er aggregert til en figur. Det mangler figur henvisning (Figur 4.1, 4.2 ... osv)

### Kapittel 5 - Metode og data

Metode- og datadelen fremstår som relevant og godt tilpasset problemstillingen. Det er en styrke gruppen tydelig beskriver prosjektet som en kvantitativ, simuleringsbasert case-studie, og at valget av Prophet begrunnes med sesongvariasjoner, helligdager og trendendringer i bokbransjen. Det er også positivt at rapporten forklarer hvorfor de tre bokkategoriene er valgt, og at datasettet er simulert fordi reelle ERP-data ikke var tilgjengelige.

Samtidlig kunne delen vært tydeligere på noen punkter. Beskrivelsen av datasettet blir litt for generell, og det burde kommet klarere fram hvilke variabler som inngår, hvordan dataene er bygget opp, og om modellen trener på salg og etterspørsel. Valideringen kunne også vært forklart mer samlet, særlig hvordan 80/20- splitten henger sammen med backtesting. I tillegg kunne rapporten kort reflektert over at simulert datagrunnlag gjør analysen lettere å kontrollere, men samtidig begrenser hvor direkte resultatene kan overføres til ARKS s faktisk drift.

Samlet sett vurderer vi metode. Og datadelen som god, men den ville blitt sterkere med en litt mer presis og samlet metodebeskrivelse.

### Kapittel 6 - Modellering

Valget av Prophet-modellen er godt begrunnet opp mot datasettet og problemstillingen. Modelleringen er strukturert og lett å følge, og koblingen mellom prognoser og lagerstyring fungerer godt gjennom rapporten. Det er også positivt at rapporten inkluderer sensitivitetsanalyse og scenarioanalyse, siden dette gjør det lettere å vurdere hvor robust modellen er under ulike forutsetninger. Forklaringene av trend-, sesong- og helligdagskomponentene i Prophet-modellen er tydelige, og figurene bidrar til å visualisere hvordan modellen håndterer variasjonene i datasettet.

**Forbedring:**

- Seksjon 6.3 inneholder mange variabler og matematiske uttrykk på kort plass. Det kunne vært nyttig med en enkel figur eller flytmodell som viser hvordan prognosene brukes videre i optimaliseringsmodellen.
- Prophet begrunnes godt teoretisk, men rapporten kunne kort forklart hvorfor modellen ikke ble sammenlignet direkte mot SARIMA eller andre prognosemodeller i analysen.
- Enkelte figurer i modelleringsdelen har ganske liten tekst og kunne vært gjort litt større for bedre lesbarhet.

### Kapittel 7 & 8 - Analyse og resultat

Analyse- og resultatdelen er oversiktlig strukturert, og det er lett å følge sammenhengen mellom modell, analyse og resultater. Det er positivt at resultatene diskuteres opp mot problemstillingen, og figurene bidrar til å visualisere forskjellene mellom baseline-modellen og Prophet-modellen. Sensitivitetsanalysen og scenarioanalysen styrker analysedelen ved at modellen testes under ulike forutsetninger.

**Forbedringspunkter:**

- Enkelte deler av analysedelen blir noe repetitive, spesielt forklaringene rundt figurene.
- Resultatet for Norske barnebøker kunne vært forklart litt tidligere i analysedelen siden kategorien skiller seg tydelig ut fra de andre.
- Noen figurer inneholder mye informasjon og kunne hatt litt større tekst og tydeligere akseforklaringer.

**Konkrete henvisninger i rapporten:**

- Seksjon 8.1 gir en tydelig sammenligning mellom baseline og Prophet-modellen for hver kategori.
- Figur 16–23 visualiserer forskjellene i kostnader og servicenivå på en oversiktlig måte.
- Diskusjonen i seksjon 9.2 rundt Norske barnebøker er interessant og viser god refleksjon rundt modellens begrensninger

**Endringsforslag:**

- Korte ned enkelte forklaringer rundt figurene for å gjøre analysedelen mer kompakt.
- Forklare tidligere hvorfor Norske barnebøker får svakere resultater enn de andre kategoriene.
- Gjøre enkelte figurer lettere å lese med større tekst og tydeligere akser.

### Kapittel 9 – Diskusjon

**Styrker:** Viser tydelig av de tolker resultatene i lys av både problemstilling og teori. God forklaring på hvorfor modellen fungerer på tvers av kategorier. De viser forståelse for når avanserte modeller ikke er hensiktsmessige (Prophet på barnebøker)

**Forbedring:** Hva er det viktigste funnet? Mange parallelle refleksjoner

### Kapittel 10 - Konklusjon

**Styrker:** Tydelig oppsummering og svarer på problemstillingen. Relevante implikasjoner for bruk i praksis er tatt med.

**Forbedring:** Noe ensidig positiv.

## Skriveflyt, formelle aspekter og helhetsvurdering

Teksten har en tydelig struktur, med presis problemstilling. Språket har stort sett god flyt. Teksten har relevant datagrunnlag og god bruk av kilder. Figurer støtter analysen godt, og visualiseringene er relevante. Fagbegreper er godt brukt, det samme er modeller og matematiske begreper. Problemstillingen er moderne og har en god kobling mellom forecasting og lagerstyring.

Enkelte deler er teksttunge. Engelsk og norsk brukes om hverandre av og til, og enkellte forkortelser mangler forklaring. APA-formattering må kvalitetsikres. Interne filhenvisninger bør vurderes – de virker lite akademiske. Noen figurer er komplekse og vanskelige å lese. Figurer og tabeller er ikke standardiserte.

Helhetsvurderingen av rapporten er at den fremstår som faglig solid og godt strukturert, med en tydelig sammenheng mellom problemstilling, metode, analyse og resultater. Gruppen viser god forståelse for koblingen mellom etterspørselsprognoser og lagerstyring, og analysen støttes av relevante visualiseringer og refleksjoner rundt modellens begrensninger. Samlet sett fremstår oppgaven som gjennomarbeidet og metodisk sterk.
