# Aktivitet 2.3 - Metode og forskningsdesign

**Aktivitet:** 2.3 Metode/forskningsdesign (M3)  
**Status:** Fullført  
**Milepæl:** M3 - Forskningsdesign og metode fastsatt (09.03.2026)  
**Rapport-kapittel:** 5.0 Metode og data

---

## 1. Forskningsparadigme

Prosjektet følger et **kvantitativt forskningsparadigme**. All analyse er basert på numeriske data og statistiske modeller. Det benyttes ingen kvalitative metoder eller subjektive vurderinger som del av beslutningsgrunnlaget.

**Begrunnelse (jf. R1):** Analysen skal baseres på kvantitative metoder innen logistikk.

---

## 2. Forskningsdesign

Prosjektet er utformet som en **simuleringsbasert case-studie** av ARK Bokhandel AS. Designet er delt i to faser:

1. **Etterspørselsprognosering:** Trening av en tidsseriemodell (Prophet) på historiske data (2021-2025) for å predikere etterspørselen i 2026.
2. **Kvantitativ bestillingsoptimalisering:** Bruk av prognosene som input i en lagermodell (EOQ/ROP) for å beregne optimale bestillingspunkter og sikkerhetslager.

Resultatene evalueres mot en definert baseline (historisk gjennomsnitt), i tråd med krav R3.

---

## 3. Metodevalg

### 3.1 Prognosemodell: Prophet
Valgt basert på fire egenskaper som matcher datasettets behov:

| Egenskap | Relevans for ARK |
|:---|:---|
| Robusthet mot sesongvariasjoner | Sterke sesongsvingninger på tvers av alle tre bokkategorier |
| Eksplisitt helligdagshåndtering | Påske, sommerferie og jul gir tydelige salgstopper |
| Automatisk trenddeteksjon | Fanger opp skift i popularitet (f.eks. BookTok-effekten) |
| Prediksjon på etterspørsel (ikke salg) | Modellen lærer reelt markedsbehov, ikke lager-begrenset salg |

### 3.2 Lagermodell: EOQ / ROP med servicegrad
Prognosene kobles til bestillingsparametere:
- **Bestillingspunkt (ROP):** Basert på forventet etterspørsel i ledetiden pluss sikkerhetslager.
- **Sikkerhetslager:** Dimensjonert ut fra prognosens usikkerhet og ønsket servicegrad.
- **Kostnadsoptimalisering:** Avveining mellom lagerholdskostnader og mangelkostnader (stockout).

### 3.3 Kampanjeidentifisering
I fravær av eksplisitte kampanjemarkører i rådataene er det benyttet **Z-score residualanalyse** for retrospektiv identifisering av kampanjeperioder. Observasjoner med avvik > 1,5 standardavvik fra månedlig snitt klassifiseres som kampanjehendelser og inkluderes i helligdagskomponenten.

---

## 4. Data

### 4.1 Datasett
Simulerte salgs- og lagerdata for ARK Bokhandel AS, tre kategorier:
- **Norske barnebøker:** Høy frekvens, tydelige sesongvariasjoner, forutsigbar.
- **Norsk krim:** Salgstopper knyttet til påske og sommer.
- **Engelsk fiksjon:** Jevnere etterspørsel, påvirket av internasjonale trender.

### 4.2 Datapreparering og validering
- **Trenings/test-splitt:** 80/20 for å validere modellens generaliseringsevne.
- **Datavask:** Håndtering av datoformater og manglende verdier.
- **Datakvalitetsantagelse:** Intern kvalitetssikring hos leverandør før utlevering (jf. rapport seksjon 5.2).

### 4.3 Treningsperiode
- **Treningsdata:** 2021-2025
- **Prognoseperiode:** 2026

---

## 5. Analysestrategi

Analysen følger en sekvensiell struktur som knytter sammen prognosering og lagerstyring:

```
Historiske data (2021-2025)
    └── Prophet-modell (trening + validering)
            └── Etterspørselsprognoser 2026
                    └── Bestillingsparametere (ROP, sikkerhetslager)
                            └── Evaluering mot baseline
                                    └── Sensitivitets- og scenarioanalyse
```

Denne strukturen adresserer kunnskapsgapet identifisert av Goltsos et al. (2022) om fragmentering mellom prognoseforskning og lagerstyringsforskning.

---

## 6. Validitet og reliabilitet

- **Intern validitet:** Sikres gjennom trenings/test-splitt (80/20) og backtesting av prognosemodellen mot usette data.
- **Etterprøvbarhet (R2, R5):** All kode og data er versjonskontrollert i Git. Analysene er dokumentert slik at prosessen kan gjentas.
- **Baseline-sammenligning (R3):** Resultatene evalueres mot en baseline basert på historisk gjennomsnitt.
- **Begrensninger:** Simulerte data kan avvike fra virkelig etterspørsel. Modellen inkluderer ikke eksterne faktorer som makroøkonomi eller konkurrenttiltak (jf. avgrensinger i kap. 1.3).

---

## 7. Kobling til krav

| Krav | Hvordan ivaretatt |
|:---|:---|
| R1 - Kvantitative metoder | Prophet + EOQ/ROP, ingen kvalitative metoder |
| R2 - Etterprøvbar modell | Dokumentert metode, versjonskontrollert kode |
| R3 - Baseline-sammenligning | Historisk gjennomsnitt som referansepunkt |
| R4 - Transparent KI-bruk | Bruk av KI-verktøy dokumenteres |
| R5 - Etterprøvbar analyse | Data og antagelser dokumentert |
| R6 - Akademisk rapport | Metode beskrevet iht. rapportmal (kap. 5.0) |

---

## Relaterte filer
- [Metodevalg_oppsummering.md](Metodevalg_oppsummering.md) - Tidlig oppsummering av metodevalg
- Rapport kapittel 5.0: `005 report/rapport.md` (linje 261-318)
- Kildelitteratur: `2.2 teoriramme/` (PDF-filer)
