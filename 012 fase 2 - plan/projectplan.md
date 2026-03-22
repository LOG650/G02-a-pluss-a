# Prosjektstyringsplan for ARK Bokhandel AS

**Dato:** 19-02-2026
**Utarbeidet av:** Anne Helene Moen Haugen og Astrid Alexandra Grepstad
**Autorisert av:** Bård Inge Austigard Pettersen og Per Kristian Rekdal (LOG650)

---

## 1. Sammendrag
Prosjektet «Lagerstyring og beslutningsstøtte i logistikk» for ARK Bokhandel AS tar utgangspunkt i kvantitative metoder for å bestemme optimal bestillingsmengde basert på historisk etterspørsel. Målet er forbedret balanse mellom lagerkostnader og tilgjengelighet. Prosjektet bygger på simulerte data for norske barnebøker, norsk krim og engelsk fiksjon.

- **1.1 Behov:** Effektiv lagerstyring krever beslutningsstøtte som kombinerer historiske data med kvantitative metoder, istedenfor enkle historiske gjennomsnitt.
- **1.2 Sponsor:** Emneansvarlig for LOG650.
- **1.3 Kunde:** Fiktiv beslutningstaker i ARK Bokhandel AS (logistikkfunksjon).
- **1.4 Forretningscase:** Gevinster i form av reduserte lagerkostnader og økt tilgjengelighet. Alternativ B (Kvantitativ bestillingsmodell basert på simulert etterspørsel) er valgt fremfor Status Quo eller Avansert AI.

---

## 2. Omfang
Prosjektet er begrenset til kvantitativ analyse av kortsiktig bestillings- og lagerstyring på kjedenivå. Langsiktig strategisk planlegging, analyse på enkeltboktitler og markedsføringstiltak er utenfor omfang.

- **2.1 Mål:** Finne en bestillingsstrategi for ARK med bedre balanse mellom kostnader og tilgjengelighet.
- **2.2 Krav:** Kvantitative metoder, etterprøvbarhet, tydelig baseline, og transparent bruk av KI.
- **2.3 Løsning:** Et analytisk beslutningsstøtteverktøy, bestående av datagrunnlag, baseline-løsning, kvantitativ bestillingsmodell, evaluering og sensitivitetsanalyse.
- **2.4 WBS (Arbeidsnedbrytningsstruktur):** Delt inn i fire faser: (1) Prosjektledelse og planlegging, (2) Teori og metode, (3) Data og analyse, (4) Resultater og rapport.
- **2.5 Omfangsverifikasjon:** Gjennomføres via intern kvalitetssikring (leveranse-eier egenkontroll, kameratsjekk) og veiledning.

---

## 3. Fremdrift
Prosjektet kartlegges mot kalenderen med en definert kritisk linje.

- **3.1 Avhengighetsdiagram & 3.2 Gantt-plan:** Sikrer logisk rekkefølge (Teori -> Datagrunnlag -> Modell -> Resultat).
- **3.3 Kritisk linje:** Datagrunnlag, modellering og resultatanalyse driver prosjektets sluttdato.
- **3.4 Milepæler:** 
  - M1: Problemstilling/proposal godkjent (23.02.26)
  - M2/M3: Litteratur/metode fastsatt (09.03.26)
  - M4: Datagrunnlag ferdigstilt (07.04.26)
  - M5: Kvantitativ analyse gjennomført (27.04.26)
  - M6/M7/M8: Resultater, utkast og endelig innlevering (Mai 26)

---

## 4. Risiko
- **4.1 Prosess:** Kontinuerlig vurdering av sannsynlighet og konsekvens.
- **4.2 Risikoregister:** 
  1. *Simulerte data blir lite realistiske* (M/H). Tiltak: Kalibrere mot litteratur.
  2. *Uklart valg mellom servicegrad og stockout-kostnad* (M/M). Tiltak: Låse valget tidlig (M3).
  3. *Tidsmangel i analysefasen* (M/H). Tiltak: Prioritere kjerneleveranser.
  4. *Tekniske problemer i Excel/Python* (M/M). Tiltak: Små iterasjoner og versjonskontroll.

---

## 5. Saker (Issues)
Forventede prosjektsaker inkluderer: 
- S1: Valg av modellspor (Stockout vs. Minimum servicenivå).
- S2: Fastsette kostnadsparametere.
- S3: Datagenerator og kalibrering.
- S4: Planforutsetninger i MS Project.

---

## 6. Interessenter
- Emneansvarlig/Sponsor (Høgskolen i Molde)
- Veileder
- Prosjektgruppen (Astrid og Anne Helene)
- ARK Bokhandel AS (Fiktiv kunde)
- Medstudenter (Fagfellevurdering)

---

## 7. Ressurser
- **7.1 Team:** Anne Helene Moen Haugen og Astrid Alexandra Grepstad fyller alle roller.
- **7.2 Ressursbelastning:** Moderat i planlegging/teori, høy i data- og analysefasen, og moderat/høy under skriving. 
- **7.3 Kritiske ressurser:** Prosjektgruppens tid/tilgjengelighet, faglig kompetanse, analyseverktøy (Excel/Python), og datagrunnlaget.

---

## 8. Kommunikasjon
- **8.1 Ukentlige saksstatusmøter:** Hver mandag kl 12:00. 
- **8.2 Månedlige prosjektgjennomganger:** Med veileder/sponsor for avklaringer av metodevalg og retning.
- **8.3 Møter i endringskontrollstyret:** Forenklet kontroll der mindre endringer avklares internt og større med veileder.

---

## 9. Kvalitet
«Kvalitet må planlegges inn, ikke inspiseres inn.»
- **9.1 Fagfellevurderinger:** Uformell fagfellevurdering (intern og peer-to-peer). Ingen formell QA/HMS/juridisk review pga. prosjektets art.
- **9.2 Brukerreviews:** Gjennomføres internt med "kundeperspektiv" for å sikre at løsningen er anvendbar for en fiktiv innkjøpsplanlegger.

---

## 10. Anskaffelser
Ingen materielle anskaffelser utover eksisterende programmer (Excel/Python) og tilgang til litteratur via bibliotek.

---

## 11. Endringskontrollprosess
Forenklet endringskontroll uten formelt CCB. Alle forespurte endringer i baseline og godkjente elementer dokumenteres i en endringslogg og vurderes mht. omfang, fremdrift og risiko.

---

## 12. Vedlegg (Referanser)
- **Vedlegg A:** Krav (Funksjonelle, Kvalitet, Metodisk, Etisk, Leveranse)
- **Vedlegg B:** WBS (Arbeidsnedbrytningsstruktur detaljert ned på Cost Account nivå)
- **Vedlegg C:** Format for saksliste
- **Vedlegg D:** Format for månedlig prosjektrapport
- **Vedlegg E:** Mal for brukerreview
- **Vedlegg F:** Skjema for endringsforespørsel
