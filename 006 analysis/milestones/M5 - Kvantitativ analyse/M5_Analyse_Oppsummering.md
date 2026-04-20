# Oppsummering av Sesong- og Trendanalyse (M5)

Denne analysen er utført med Prophet-modellen og danner grunnlaget for de dynamiske bestillingsreglene.

| Kategori          |   Trend_Endring (%) |   Sesong_Amplitude (enheter) |
|:------------------|--------------------:|-----------------------------:|
| Engelsk fiksjon   |          -4.83948   |                      204.838 |
| Norske barnebøker |          -0.0969742 |                      105.345 |
| Norsk krim        |          12.6987    |                      114.849 |

<div align="center">
  <img src="3.5%20kvantitativ%20modell/prophet_components_Engelsk_fiksjon.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 1: Prophet-komponenter for Engelsk fiksjon (Trend og Sesongvariasjon)</em>
</div>

<div align="center">
  <img src="3.5%20kvantitativ%20modell/prophet_components_Norske_barnebøker.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 2: Prophet-komponenter for Norske barnebøker (Trend og Sesongvariasjon)</em>
</div>

<div align="center">
  <img src="3.5%20kvantitativ%20modell/prophet_components_Norsk_krim.png" style="width: 70%; height: auto;">
  <br>
  <em>Figur 3: Prophet-komponenter for Norsk krim (Trend og Sesongvariasjon)</em>
</div>

*Notat: Trend_Endring viser utviklingen over hele analyseperioden (2021-2026).*

## Antagelser og Datakvalitet
Følgende antagelser ligger til grunn for den kvantitative analysen:
1. **Etterspørselshistorikk:** Det antas at historiske salgsdata er en god representant for fremtidig etterspørsel, og at ekstreme uteliggere (f.eks. kampanjer) er håndtert i vaskeprosessen.
2. **Parametere:** Kostnadsparametere (lagerholdskostnad og utsolgtkostnad) er antatt konstante gjennom hele simuleringsperioden.
3. **Ledetid:** Ledetid fra leverandør er modellert som deterministisk basert på historiske gjennomsnitt.
4. **Modellering:** Prophet-modellen fanger opp additive sesongvariasjoner og lineære trender. Det antas at ingen store strukturelle endringer i markedet inntreffer utenfor det modellen predikerer.

## Sensitivitetsanalyse (Aktivitet 3.7)
Gjennomført sensitivitetsanalyse viser følgende kritiske funn for modellens robusthet:

1.  **Sikkerhetsmargin (Safety Margin Factor):**
    *   For **Engelsk fiksjon** er modellen svært sensitiv for sikkerhetsmarginen. Ved å øke denne med 50 % (faktor 1.5) reduseres totalkostnadene med ca. 50 %, mens servicenivået øker fra 86 % til 94 %. Dette tyder på at den opprinnelige modellen var for konservativ.
    *   For **Norske barnebøker** ble det bekreftet at en aggressiv økning i sikkerhetsmarginen (faktor 2.0) er nødvendig for at Prophet-modellen skal overgå baselinen. Dette skyldes kategoriens svært regelmessige, men kraftige sesongtopper.
2.  **Kostnadsparametere:**
    *   Modellen er lineært avhengig av mangelkostnad ($C_s$), men viser seg å være robust mot mindre svingninger i lagerholdskostnad ($C_h$).
3.  **Anbefaling:**
    *   Det anbefales å implementere en kategori-spesifikk sikkerhetsfaktor i den endelige modellen for å maksimere besparelsene identifisert i denne analysen.
