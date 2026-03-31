# Sluttresultater - Kvantitativ Analyse (M5)

Sammenligning av Baseline ((s, Q) basert på snitt) mot Prophet-optimalisert modell.

| Kategori          |   Kostnad Baseline |   Kostnad Optimalisert |   Besparelse (%) |   SL Baseline (%) |   SL Optimalisert (%) |
|:------------------|-------------------:|-----------------------:|-----------------:|------------------:|----------------------:|
| Engelsk fiksjon   |            89267.3 |                71801.9 |            19.57 |             83.08 |                 86.31 |
| Norske barnebøker |            41114.5 |                44345.6 |            -7.86 |             85.35 |                 83.83 |
| Norsk krim        |            68254.3 |                42246.7 |            38.1  |             85.8  |                 91.47 |

## Kommentar til resultater
Det observeres at den optimaliserte modellen gir betydelige gevinster for kategorier med tydelig trend eller høy sesongvariasjon (Norsk krim og Engelsk fiksjon). 

For **Norske barnebøker** er resultatet negativt (-7.86 %). Dette kan forklares med en relativt lav sesong-amplitude og stabil etterspørsel, hvor den enklere (s, Q)-baselinen allerede fungerer effektivt. Bruk av en mer kompleks modell her medfører økt risiko for "overfitting" til støy i dataene, noe som resulterer i marginalt høyere kostnader og lavere servicenivå.