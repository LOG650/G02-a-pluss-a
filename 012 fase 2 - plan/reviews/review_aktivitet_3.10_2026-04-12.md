# Review: Aktivitet 3.10 Optimalisering av Bestillingsregler
**Dato:** 12. april 2026
**Status:** Gjennomgått / Godkjent med merknader

### 1. Sammendrag
Aktivitet 3.10 har fokusert på å oversette funnene fra modellvalideringen (3.9) og sensitivitetsanalysen (3.7) til konkrete styringsparametere for lagerstyringsmodellen. Dette inkluderer bias-justering, fastsettelse av sikkerhetsfaktorer (k) og estimering av kampanjeløft. Relevante filer finnes i `006 analysis/milestones/M5 - Kvantitativ analyse/` og `004 data/python_skript/`.

### 2. Styrker
*   **Datadrevet tilnærming:** Bruken av eksakte bias-verdier fra backtestingen i 3.9 sikrer at modellen korrigerer for kjente svakheter før simuleringen av 2026.
*   **Risikobasert differensiering:** Valget om å tildele Norsk krim en høyere sikkerhetsfaktor (1.8) for å kompensere for undervurdering er et sterkt metodisk grep som prioriterer tilgjengelighet der risikoen er størst.
*   **Integrasjon av funn:** Aktiviteten knytter sammen resultatene fra flere tidligere steg (3.7, 3.8 og 3.9) på en logisk og anvendbar måte.

### 3. Svakheter og forbedringspotensial
*   **Tegnkoding (Encoding):** 
    *   Den genererte rapporten `3.10_optimalisering_oppsummering.md` har problemer med særnorske tegn (æ, ø, å) som vises som erstatningstegn.
    *   *Anbefaling:* Sikre at python-skriptet skriver til fil med `encoding='utf-8'`.
*   **Dokumentasjon av k-verdi logikk:**
    *   Selv om valgene av k-verdier virker fornuftige, mangler en eksplisitt kobling til de økonomiske kostnadsparametrene fra `Kostnadsparametere.csv` i selve optimaliseringsskriptet.
    *   *Anbefaling:* I den endelige rapporten (Phase 4) bør det forklares hvordan disse k-verdiene balanserer $C_h$ mot $C_s$ kvalitativt.

### 4. Konklusjon
Aktiviteten er meget godt gjennomført og danner et solid fundament for de endelige simuleringskjøringene i 3.11. Parameterne er realistiske og godt begrunnet i analysene. Leveransen anses som klar for neste fase så snart tegnkodingsfeilen er rettet i rapportfilen.
