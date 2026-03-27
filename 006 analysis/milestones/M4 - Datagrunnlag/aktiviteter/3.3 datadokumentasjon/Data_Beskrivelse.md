# Datadokumentasjon - Milepæl M4

Dette dokumentet beskriver det vaskede datasettet `master_data_vasket.csv` og de tilhørende visualiseringene som dokumenterer datagrunnlaget for ARK Bokhandel AS.

## 1. Datagrunnlag
Datasettet er basert på simulerte salgsdata for tre hovedkategorier:
- **Norske barnebøker:** Høy frekvens, potensielt sesongavhengig.
- **Norsk krim:** Typiske salgstopper (påske/sommer).
- **Engelsk fiksjon:** Jevnere etterspørsel, ofte import.

## 2. Utførte vaskeoppgaver (Rense og strukturere data)
Prosessen for å klargjøre dataene inkluderte:
- **Sammenslåing:** Kombinert rådata fra flere kilder (Faktadata, Bestillingsdata, Kostnadsparametere).
- **Vask:** Identifisering og retting av inkonsistente datoformater og håndtering av manglende verdier.
- **Beregning:** Utregning av faktiske lagernivåer basert på inngående beholdning, salg og mottatte bestillinger.
- **Identifisering:** Markering av "stockouts" (perioder der etterspørselen var høyere enn lagerbeholdningen).

## 3. Oversikt over figurer (01-09)
Figurene i denne mappen dokumenterer datakvaliteten og de viktigste trendene før analyse:
- **01-03:** Visualisering av etterspørsel vs. faktisk salg og hvordan dette påvirker lagerbeholdningen.
- **04-05:** Kostnadsanalyse som viser trade-off mellom svinn og kostnader ved utsolgte varer (stockout).
- **06-09:** Analyse av sesongvariasjoner per måned og årlige salgstrender for å fange opp mønstre i etterspørselen.

## 4. Nøkkelvariable i `master_data_vasket.csv`
- **Dato:** Tidspunkt (YYYY-MM-DD).
- **Produktkategori:** Barnebøker, Krim eller Engelsk fiksjon.
- **Salg:** Antall faktisk solgte enheter (begrenset av lager).
- **Etterspørsel:** Den underliggende etterspørselen i markedet.
- **Lagerbeholdning:** Antall enheter tilgjengelig på lager ved dagens slutt.
- **Kostnadsparametere:** Enhetskostnader, lagerholdskostnad og mangelkostnad.

## 5. Datakvalitet og antagelser
Siden det ikke foreligger direkte kilder som beskriver datakvaliteten i detalj, er følgende antagelser lagt til grunn for analysen:
- **Kvalitetssikring fra kilde:** Det antas at datasettet er gjenstand for intern kvalitetssikring hos leverandøren før utlevering.
- **Konsistens:** Dataene anses som representative for de faktiske forholdene i den gitte perioden, med unntak av de avvikene som er håndtert i vaskeprosessen (se avsnitt 2).
- **Fullstendighet:** Det antas at det simulerte datasettet inneholder alle relevante variabler som kreves for å gjennomføre en meningsfull analyse av etterspørsel og lagerstyring.
