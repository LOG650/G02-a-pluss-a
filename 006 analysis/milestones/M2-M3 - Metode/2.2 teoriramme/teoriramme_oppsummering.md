# Aktivitet 2.2 — Teoriramme

**Dato:** 14. april 2026  
**Status:** Gjennomgått og oppdatert

---

## 1. Litteraturgrunnlag

Litteraturkapitlet (seksjon 2.0 i rapporten) er bygget opp langs to akser:

### Akse 1: Etterspørselsprognosering

| # | Kilde | Bidrag | Relevans | PDF |
|:--|:------|:-------|:---------|:----|
| 1 | Taylor & Letham (2018) | Introduserer Prophet — additiv tidsseriemodell | Hovedmodellen i prosjektet | `Taylor_Letham_2018_Forecasting_at_Scale.pdf` |
| 2 | Park et al. (2020) | ML-basert prognosering i bokbransjen | Bransjespesifikk kontekst | `Demand Forecasting for Publishing.pdf` |
| 3 | Luo (2019) | Reformering av bokhandler med stordata | Motivasjon for datadrevet tilnærming | `Luo_2019_J._Phys.__Conf._Ser._1213_052008.pdf` |
| 4 | Haque et al. (2023) | Komparativ studie med makroøkonomiske variabler | Støtter bruk av eksterne faktorer | `Haque_et_al_2023_Retail_Demand_Forecasting_Comparative.pdf` |
| 5 | Borucka (2023) | Sesongbaserte prognosemetoder i forsyningskjeden | Direkte overførbar til ARKs sesongutfordringer | `Borucka_2023_Seasonal_Methods_Demand_Forecasting.pdf` |

### Akse 2: Lagerstyring og kostnadsoptimalisering

| # | Kilde | Bidrag | Relevans | PDF |
|:--|:------|:-------|:---------|:----|
| 6 | Lewis (1997) | Klassisk rammeverk: etterspørselstyper og kontrollstrategier | Grunnleggende teori | `Demand forecasting and inventory control.pdf` |
| 7 | Chen (2020) | Datadrevet lagerstyring med skiftende etterspørsel | Direkte relevant for sesongvarer | `Data-Driven Inventory Control with shifting demand.pdf` |
| 8 | Goltsos et al. (2022) | Integrasjon av prognose- og lagerstyringsforskning | Bærer prosjektets struktur | `Goltsos_et_al_2022_Inventory_Forecasting_Mind_the_Gap.pdf` |
| 9 | Kirmizi et al. (2024) | Sikkerhetslagerstrategier, casestudie | Støtter ROP/sikkerhetslager-beregning | `Kirmizi_et_al_2024_Safety_Stock_Strategies.pdf` |
| 10 | Adeyemi & Onanuga (2014) | EOQ-modeller under stokastisk etterspørsel | Supplerende kostnadsgrunnlag | `Dynamics_of_Inventory_Cost_Optimization.pdf` |

---

## 2. Kunnskapsgap

Goltsos et al. (2022) dokumenterer at prognose- og lagerstyringsforskning i stor grad utvikles uavhengig av hverandre. Dette prosjektet adresserer gapet ved å koble Prophet-prognoser direkte til bestillingsparametere (ROP, sikkerhetslager, servicegrad) i en bokhandel-kontekst med sterke sesongvariasjoner.

---

## 3. Fullstendig kildeliste (APA 7)

| # | Referanse | PDF |
|:--|:----------|:----|
| 1 | Adeyemi, A. A., & Onanuga, A. T. (2014). Dynamics of inventory cost optimization — A review of theory and evidence. *Research Journal of Finance and Accounting*, *5*(22). | [PDF](Dynamics_of_Inventory_Cost_Optimization.pdf) |
| 2 | Borucka, A. (2023). Seasonal methods of demand forecasting in the supply chain as support for the company's sustainable growth. *Sustainability*, *15*(9), 7399. | [PDF](Borucka_2023_Seasonal_Methods_Demand_Forecasting.pdf) |
| 3 | Chen, B. (2020). *Data-Driven Inventory Control with Shifting Demand*. University of Illinois at Chicago. | [PDF](Data-Driven%20Inventory%20Control%20with%20shifting%20demand.pdf) |
| 4 | Goltsos, T. E., Syntetos, A. A., Glock, C. H., & Ioannou, G. (2022). Inventory–forecasting: Mind the gap. *European Journal of Operational Research*, *299*(2), 397–419. | [PDF](Goltsos_et_al_2022_Inventory_Forecasting_Mind_the_Gap.pdf) |
| 5 | Haque, M. S., Amin, M. S., & Miah, J. (2023). Retail demand forecasting: A comparative study for multivariate time series. *arXiv preprint arXiv:2308.11939*. | [PDF](Haque_et_al_2023_Retail_Demand_Forecasting_Comparative.pdf) |
| 6 | Kirmizi, S. D., Ceylan, Z., & Bulkan, S. (2024). Enhancing inventory management through safety-stock strategies — A case study. *Systems*, *12*(7), 260. | [PDF](Kirmizi_et_al_2024_Safety_Stock_Strategies.pdf) |
| 7 | Lewis, C. D. (1997). *Demand forecasting and inventory control: A computer aided learning approach*. Woodhead Publishing. | [PDF](Demand%20forecasting%20and%20inventory%20control.pdf) |
| 8 | Luo, T. (2019). Traditional book stores industry reforming based on the new management system. *Journal of Physics: Conference Series*, *1213*, 052008. | [PDF](Luo_2019_J._Phys.__Conf._Ser._1213_052008.pdf) |
| 9 | Park, M. H., Lee, J. S., & Doo, I. C. (2020). A study of the demand forecasting model for publishing business using business analysis. *International Journal of Computing and Digital Systems*, *9*(5), 801–812. | [PDF](Demand%20Forecasting%20for%20Publishing.pdf) |
| 10 | Taylor, S. J., & Letham, B. (2018). Forecasting at scale. *The American Statistician*, *72*(1), 37–45. | [PDF](Taylor_Letham_2018_Forecasting_at_Scale.pdf) |

---

## 4. Endringslogg

- **14. april 2026:** Utvidet fra 4 til 10 kilder. Erstattet Huber & Stuckenschmidt (2020) med Haque et al. (2023) og Ye et al. (2024) med Borucka (2023) for å sikre åpen tilgang. Alle PDF-er verifisert og lagt i mappen.
