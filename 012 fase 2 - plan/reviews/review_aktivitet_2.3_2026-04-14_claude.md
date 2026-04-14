# Review: Aktivitet 2.3 - Metode og forskningsdesign
**Dato:** 14. april 2026  
**Status:** Gjennomgått  
**Reviewer:** Claude (AI-assistent)

### 1. Sammendrag
Gjennomgang av aktivitet 2.3 Metode/forskningsdesign (M3) og tilhørende rapportkapittel 5.0 Metode og data. Formålet er å verifisere at forskningsdesignet er fullstendig dokumentert, at metodevalg er begrunnet, og at kravene fra AGENTS.md seksjonsveiledning og prosjektets kravspesifikasjon (R1-R6) er ivaretatt.

Relevante filer:
- `006 analysis/milestones/M2-M3 - Metode/2.3 metode og forskningsdesign/forskningsdesign.md`
- `006 analysis/milestones/M2-M3 - Metode/2.3 metode og forskningsdesign/Metodevalg_oppsummering.md`
- `005 report/rapport.md` kapittel 5.0 (linje 261-318)

### 2. Styrker
*   **Komplett metodevalg med begrunnelse:** Valget av Prophet er godt begrunnet med fire konkrete egenskaper som kobles direkte til datasettets behov (sesongvariasjoner, helligdager, trender, etterspørsel vs. salg).
*   **Tydelig todelt forskningsdesign:** Skillet mellom prognosering (Prophet) og bestillingsoptimalisering (EOQ/ROP) gir en klar analytisk struktur som adresserer kunnskapsgapet fra Goltsos et al. (2022).
*   **Kravsporing:** Alle seks krav (R1-R6) er eksplisitt koblet til metodevalg i forskningsdesign.md.
*   **Valideringsstrategi:** 80/20 trenings/test-splitt og backtesting er dokumentert som valideringsmetode.
*   **Kampanjeidentifisering:** Z-score residualanalyse for å skille kampanjeeffekter fra sesongvariasjon er en god metodisk løsning på manglende kampanjemarkører i rådataene.

### 3. Svakheter og forbedringspotensial
*   **Rapportkapittel 5.1 - Språkfeil:**
    *   Linje 276: "sikrer we at" skal være "sikrer vi at".
    *   Linje 278: "historiske salgs data" bør skrives "historiske salgsdata" (ett ord).
    *   Linje 281: "salgs- og lager data" bør skrives "salgs- og lagerdata".
    *   *Anbefaling:* Rette opp skrivefeilene i rapport.md.

*   **Forskningsparadigme mangler i rapporten:**
    *   AGENTS.md seksjonsveiledning for 5.0 sier: "Oppgi paradigme, design, innsamlingsmetode, utvalg og analysemetoder." Rapporten beskriver metodevalg og data godt, men nevner ikke eksplisitt at det er et kvantitativt forskningsparadigme.
    *   *Anbefaling:* Vurdere å legge til en kort setning i starten av kapittel 5.1 som navngir paradigmet.

*   **Utvalg ikke eksplisitt beskrevet:**
    *   Rapporten beskriver de tre kategoriene, men forklarer ikke hvorfor akkurat disse tre ble valgt (utvalgslogikk).
    *   *Anbefaling:* Legge til 1-2 setninger som begrunner valget av de tre bokkategoriene (f.eks. at de representerer ulike etterspørselsmønstre).

*   **Metodevalg_oppsummering.md er tynn:**
    *   Filen er et tidlig arbeidsdokument som nå er overflødig i forhold til det nye forskningsdesign.md. Den tilfører lite merverdi.
    *   *Anbefaling:* Kan beholdes som historisk dokument, men trenger ingen oppdatering.

### 4. Konklusjon
Aktivitet 2.3 er **i det vesentlige fullført**. Forskningsdesignet er godt dokumentert i den nye forskningsdesign.md, og rapportkapittel 5.0 dekker det meste som kreves. Det er tre mindre forbedringer som bør gjøres:

1. **Rette skrivefeil** i rapport.md kapittel 5.1 (prioritet: høy, enkelt å fikse)
2. **Nevne forskningsparadigme** eksplisitt i rapporten (prioritet: middels)
3. **Begrunne utvalg** av bokkategorier (prioritet: middels)

Ingen av disse krever vesentlige endringer, og aktiviteten kan anses som ferdig etter rettelsene.
