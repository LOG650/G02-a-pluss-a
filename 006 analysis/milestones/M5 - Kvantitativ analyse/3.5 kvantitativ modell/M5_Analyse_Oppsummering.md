# Oppsummering av Sesong- og Trendanalyse (M5)

Denne analysen er utført med Prophet-modellen og danner grunnlaget for de dynamiske bestillingsreglene.

| Kategori          |   Trend_Endring (%) |   Sesong_Amplitude (enheter) | Plot                                     |
|:------------------|--------------------:|-----------------------------:|:-----------------------------------------|
| Engelsk fiksjon   |          -4.83948   |                      204.838 | prophet_components_Engelsk_fiksjon.png   |
| Norske barnebøker |          -0.0969742 |                      105.345 | prophet_components_Norske_barnebøker.png |
| Norsk krim        |          12.6987    |                      114.849 | prophet_components_Norsk_krim.png        |

*Notat: Trend_Endring viser utviklingen over hele analyseperioden (2021-2026).

## Antagelser og Datakvalitet
Følgende antagelser ligger til grunn for den kvantitative analysen:
1. **Etterspørselshistorikk:** Det antas at historiske salgsdata er en god representant for fremtidig etterspørsel, og at ekstreme uteliggere (f.eks. kampanjer) er håndtert i vaskeprosessen.
2. **Parametere:** Kostnadsparametere (lagerholdskostnad og utsolgtkostnad) er antatt konstante gjennom hele simuleringsperioden.
3. **Ledetid:** Ledetid fra leverandør er modellert som deterministisk basert på historiske gjennomsnitt.
4. **Modellering:** Prophet-modellen fanger opp additive sesongvariasjoner og lineære trender. Det antas at ingen store strukturelle endringer i markedet inntreffer utenfor det modellen predikerer.
*