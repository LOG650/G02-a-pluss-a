# Agent Instrukser - Prosjekt G02-a-pluss-a

Dette dokumentet inneholder spesifikke instruksjoner for hvordan AI-agenten skal operere i dette prosjektet. Be meg lese dette dokumentet hvis du vil sikre at jeg følger de etablerte standardene.

## Rapportformatering
- **Midtstilling:** Figurer og figurtekst skal alltid midtstilles med `<div align="center">`.
- **Bilder:** Bilder skal ha `width: 70%` og `height: auto` i `style`-attributten.
- **Figurtekst:** Skal stå under bildet (separert med `<br>`) og skrives i kursiv (`<em>`).
- **Eksempel:**
  ```html
  <div align="center">
    <img src="sti/til/bilde.png" style="width: 70%; height: auto;">
    <br>
    <em>Figur 1: Beskrivelse av bildet</em>
  </div>
  ```

## Prosjektoppfølging
- **Datakvalitet:** Dokumenter alltid antagelser om datakvalitet i relevante markdown-filer.
- **Milepæler:** Oppdater `012 fase 2 - plan/schedule.json` med status når en milepæl er fullført.

## Arbeidsflyt
- Før større endringer, sjekk `012 fase 2 - plan/` for å forstå kontekst og krav.
- Følg alltid eksisterende navnekonvensjoner for filer og mapper.

## Fullstendig Rapportveiledning og Maltekst

### Obligatoriske Erklæringer og Metadata
**Antall ord/Forfattererklæring:**
Marker denne setningen, og skriv inn antall ord/forfattererklæring dersom det er et krav. Hvis det ikke er et krav slettes hele avsnittet.

**Egenerklæring:**
Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre.
1. Besvarelsen er mitt/vårt eget arbeid.
2. Besvarelsen har ikke vært brukt til annen eksamen, refererer korrekt til andre og eget arbeid, har alle referanser i listen, og er ikke en kopi.
3. Brudd er fusk jf. Universitets- og høgskoleloven.
4. Oppgaver kan plagiatkontrolleres i URKUND.

**Publiseringsavtale:**
Forfatter(ne) har opphavsrett. Alle oppgaver som fyller kriteriene vil bli publisert i Brage HiM med godkjennelse.

---

### Seksjonsveiledning

#### 1.0 Innledning
Introduksjonen bør ikke være for lang, mellom 1-4 sider, helst kun 1-2. Ta utgangspunkt i et generelt tema og beskriv den aktuelle problemstillingen.
- Svar på: Hvilket tema? Hvorfor aktuelt? Hva er gjort tidligere? Hva er problemstillingen? Hvilke avgrensinger?
- **Tips:** Skap nysgjerrighet. Unngå å brodere ut hvordan resultatet oppnås med en gang. Bruk introduksjonen til å gi innblikk i strukturen og skape en rød tråd.

#### 1.1 Problemstilling
- Skal være et «hvordan»- eller «hvorfor»-spørsmål.
- Danner grunnlaget for hele oppgaven.
- **Krav:** Vær spesifikk. Ikke skriv noe du ikke svarer på, og ikke svar på mer enn det som står i problemstillingen.

#### 1.2 Delproblemer (valgfri)
- Del opp hvis problemstillingen er komplisert. Fremstilles i logisk rekkefølge.

#### 1.3 Avgrensinger
- Forklar hvorfor visse områder er utelatt. Ikke avgrens uten forklaring. Aldri bruk "dårlig tid" som begrunnelse.

#### 1.4 Antagelser
- Presiserer situasjonen som analyseres. Forklar hvorfor antagelsen er tatt og hvilke konsekvenser den får for aktualiteten.

#### 2.0 Litteratur
- Diskuter bidrag fra de siste 5 årene. Trekk tråder til din problemstilling.
- Unngå synsing; alle påstander må refereres. Referanser krediterer resultater og lar leseren sjekke kilder.

#### 3.0 Teori
- Beskriv teoretisk perspektiv, tidligere litteratur og uenigheter mellom forskere.
- Plasser egen problemstilling i lys av teorien og vis hva den belyser som ikke er gjort før.

#### 4.0 Casebeskrivelse
- Utbroder problemstillingen for bedriften/bransjen. Ta kun med relevant informasjon.
- Eksempel: Bedriftstype, produktets oppbygning, dagens produksjonsprosess, påvirkningsfaktorer, tilgjengelig data.

#### 5.0 Metode og data
- **Metode:** Beskriv så nøyaktig at andre kan gjenta prosessen. Oppgi paradigme, design, innsamlingsmetode, utvalg og analysemetoder.
- **Data:** Beskriv tidsperiode, kilde (f.eks. ERP), og nøyaktighet.

#### 7.0 Analyse
- Kvalitativ, kvantitativ eller dokumentanalyse. Siste bit før presentasjon av resultater.

#### 8.0 Resultat
- Presenter funn klart og tydelig, gjerne med tabeller og figurer.
- **Regel:** Kun objektiv presentasjon her. Hver tabell/figur skal ha en forklarende tekst (som regel før objektet). Resultatene må være direkte linket til forskningsspørsmålet.

#### 9.0 Diskusjon
- Kommenter resultatene: Forventet/uventet? Samsvar med litteratur?
- Diskuter betydning for næringslivet og anbefalinger.
- Vurder generalisering og vær ærlig om begrensinger/svakheter.

#### 10.0 Konklusjon
- Oppsummer hovedfunn i forhold til problemstilling.
- Ofte begynner man med å gjenta forskningsspørsmålet.
- Avslutt med videre forskning og refleksjoner.

## Mal for Review av Aktiviteter
Når du blir bedt om å utføre en review av en aktivitet eller et dokument, skal følgende mal benyttes:

# Review: [Aktivitetsnavn eller Dokumentnavn]
**Dato:** [DD. måned ÅÅÅÅ]
**Status:** [F.eks. Utkast / Gjennomgått / Godkjent]

### 1. Sammendrag
[Kort beskrivelse av hva som er vurdert, formålet med gjennomgangen og hvor de relevante filene befinner seg.]

### 2. Styrker
*   **[Punkt 1]:** [Beskrivelse av hva som er bra, f.eks. god struktur, grundig analyse eller overholdelse av krav.]
*   **[Punkt 2]:** [Beskrivelse...]

### 3. Svakheter og forbedringspotensial
*   **[Kritisk punkt/Område]:** 
    *   [Beskrivelse av mangelen eller avviket fra standarder (f.eks. AGENTS.md).]
    *   *Anbefaling:* [Konkret forslag til hvordan dette kan utbedres.]
*   **[Mindre punkt]:**
    *   [Beskrivelse...]
    *   *Anbefaling:* [...]

### 4. Konklusjon
[En samlet vurdering av kvaliteten. Er leveransen klar for neste fase, eller kreves det vesentlige endringer? Oppsummer de viktigste tiltakene som må gjøres.]
