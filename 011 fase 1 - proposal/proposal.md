# Prosjektforslag LOG650 - Gruppe A + A

## Gruppemedlemmer
* Anne Helene Moen Hagen
* Astrid Alexandra Grepstad

## Område
Oppgaven tar utgangspunkt i lagerstyring og beslutningsstøtte i logistikk, med fokus på kvantitative metoder for å bestemme optimal bestillingsmengde basert på historisk etterspørsel. Prosjektet knytter etterspørselsdata sammen med lagerrelaterte beslutninger for å forbedre balansen mellom kostnader og tilgjengelighet.

## Bedrift (valgbart)
Prosjektet tar utgangspunkt i problemstillinger relevante for **ARK Bokhandel AS**, som er en landsdekkende bokhandelkjede med tydelige sesongvariasjoner i etterspørselen etter ulike bokkategorier.

## Problemstilling
Hvordan kan ARK Bokhandel AS bestemme optimal bestillingsmengde for utvalgte bokkategorier, basert på historisk etterspørsel, for å redusere lagerkostnader og samtidig begrense risikoen for utsolgte varer i kortsiktig planlegging?

## Data
Prosjektet vil basere seg på historiske etterspørselsdata slik de typisk finnes i en bokhandelkjede. Dette inkluderer salgsvolum per tidsperiode, enten på daglig eller ukentlig nivå, for utvalgte bokkategorier. Videre vil enkle tidsvariabler som uke og sesong benyttes for å fange opp variasjoner i etterspørselen.

I tillegg benyttes forutsetninger om lagerrelaterte kostnader, som kostnader knyttet til lagerhold og kostnader ved utsolgte varer.

Da vi ikke har lyktes i å oppnå kontakt med ARK, ser vi oss nødt til å benytte simulerte data i dette prosjektet. Målet er at den simulerte dataen skal etterligne historisk etterspørsel i form av salgsvolum per tidsperiode (ukentlig nivå) for utvalgte bokkategorier. For å gjøre tallene mest mulig realistiske vil det legges inn sesongvariasjoner, deriblant økt etterspørsel i perioder som skolestart og før jul, samt tilfeldige variasjoner som reflekterer usikkerhet i etterspørselen. I tillegg antas forenklede, men realistiske, lagerrelaterte kostnader, som kostnader ved lagerhold og kostnader knyttet til utsolgte varer. Disse kostnadsparameterne benyttes for å analysere hvordan ulike bestillingsstrategier påvirker totale lagerkostnader og tilgjengelighet.

## Beslutningsvariabler
Beslutningsvariablene i prosjektet representerer de størrelsene som kan justeres for å styre lageret. Dette omfatter hvor mange eksemplarer av en bokkategori som bør bestilles i hver kortsiktige planleggingsperiode, samt når nye bestillinger bør gjennomføres. Disse beslutningene påvirker både lagerbeholdning, risiko for utsolgte varer og totale lagerrelaterte kostnader.

## Målfunksjon
Målet med prosjektet er å finne en bestillingsstrategi som gir en bedre balanse mellom lagerkostnader og tilgjengelighet. Forbedring måles ved å vurdere totale lagerrelaterte kostnader over tid, inkludert kostnader knyttet til overlager og utsolgte varer. En løsning anses som bedre dersom den gir lavere totale kostnader eller færre utsolgte perioder sammenlignet med en enklere bestillingsstrategi basert på historisk gjennomsnitt.

## Avgrensninger
Prosjektet avgrenses til kortsiktig lagerstyring og omfatter ikke langsiktig strategisk planlegging. Analysen begrenses til et utvalg bokkategorier og ser ikke på individuelle boktitler. Eksterne faktorer som makroøkonomiske endringer, konkurrenters tiltak og markedsføringskampanjer inkluderes ikke. Videre fokuserer prosjektet på kvantitative metoder og inkluderer ikke kvalitative vurderinger eller manuelle justeringer foretatt av ansatte.
