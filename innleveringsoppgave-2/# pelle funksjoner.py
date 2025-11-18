"""
historien om Sjefen Erling.

Programmet bygger på storylinen fra del 1:
- Tre beslutningspunkter
- To valg per beslutning (A eller B)
- Minst tre mulige utfall til slutt

Spilleren styrer Erling gjennom valgene.
"""


def get_choice(prompt: str) -> str:
    """
    Hjelpefunksjon som sikrer at brukeren velger A eller B.
    """
    while True:
        choice = input(prompt).strip().upper()
        if choice in ("A", "B"):
            return choice
        print("Ugyldig valg. Skriv A eller B.")


def intro():
    """
    Skriver ut en kort introduksjon til historien.
    """
    print("Velkommen til historien om Erling og prosjektet med medborgerportalen.\n")
    print(
        "Det har gått seks uker siden prosjektet startet. Stemningen er ikke like god "
        "som i starten, og flere konflikter har begynt å vokse frem i teamet."
    )
    print(
        "Som prosjektleder må Erling ta noen viktige valg som vil påvirke både "
        "samarbeid, motivasjon og resultat.\n"
    )


def decision_1() -> str:
    """
    Beslutning 1: Hvordan håndterer Erling konflikten mellom Silje og Sivert?
    Returnerer 'A' eller 'B'.
    """
    print("\nBESLUTNING 1: KONFLIKTEN MELLOM SILJE OG SIVERT\n")
    print(
        "Silje (UX-designer) og Sivert (IT-rådgiver) er uenige om teknologivalg og "
        "design. Det som startet som en faglig diskusjon, har utviklet seg til en "
        "personlig konflikt. Resten av teamet begynner å ta side."
    )
    print("\nHva gjør Erling?")
    print("A) Tar konflikten opp i plenum og inviterer til åpen dialog i hele teamet.")
    print("B) Tar individuelle samtaler med Silje og Sivert for å dempe temperaturen.")

    choice = get_choice("Velg A eller B: ")
    print()  # tom linje for lesbarhet
    if choice == "A":
        print(
            "Erling kaller inn hele teamet. Han setter noen spilleregler for dialogen "
            "og ber Silje og Sivert beskrive sine behov og perspektiver. Konflikten "
            "blir synlig for alle, og teamet forsøker å finne en felles forståelse."
        )
    else:
        print(
            "Erling tar Silje og Sivert inn én og én. Han lytter til hvordan de "
            "opplever situasjonen, prøver å rydde i misforståelser og ber dem holde "
            "en profesjonell tone videre i prosjektet."
        )
    return choice


def decision_2() -> str:
    """
    Beslutning 2: Hvordan håndterer Erling uenigheten mellom Hamdi og Jabir?
    Returnerer 'A' eller 'B'.
    """
    print("\nBESLUTNING 2: UENIGHETEN MELLOM HAMDI OG JABIR\n")
    print(
        "Samtidig ulmer en konflikt mellom Hamdi (kulturavdelingen) og Jabir "
        "(brukerrepresentant). De er uenige om hvor åpen plattformen for digitale "
        "folkemøter skal være."
    )
    print(
        "Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, "
        "mens Jabir ønsker et mer åpent og dialogbasert system."
    )

    print("\nHva gjør Erling?")
    print(
        "A) Kaller inn Hamdi og Jabir til et felles møte for å avklare uenigheten "
        "og diskutere mål og rammer."
    )
    print(
        "B) Avventer, og håper at Hamdi og Jabir selv finner en løsning mens teamet "
        "fortsetter å jobbe mot milepælen."
    )

    choice = get_choice("Velg A eller B: ")
    print()
    if choice == "A":
        print(
            "Erling inviterer Hamdi og Jabir til et møte. De får legge frem sine "
            "bekymringer og ønsker. Det blir en krevende, men ærlig diskusjon om "
            "balansen mellom kontroll, demokrati og risiko."
        )
    else:
        print(
            "Erling velger å ikke gripe inn nå. Han vurderer at konflikten foreløpig "
            "er lavmælt, og ønsker å unngå flere møter. Teamet jobber videre, men "
            "fortsatt med ulike forventninger til innbyggerdialog."
        )
    return choice


def decision_3() -> str:
    """
    Beslutning 3: Hvordan bevarer Erling motivasjonen i teamet?
    Returnerer 'A' eller 'B'.
    """
    print("\nBESLUTNING 3: MOTIVASJON OG SAMHOLD\n")
    print(
        "Det nærmer seg milepæl. Prototypen skal være klar om tre uker. "
        "Konflikter, tidspress og usikkerhet har tappet energi i teamet."
    )

    print("\nHva gjør Erling?")
    print(
        "A) Setter av tid til relasjonsbygging, for eksempel en felles refleksjonsøkt "
        "eller en sosial aktivitet for å styrke tillit og samarbeid."
    )
    print(
        "B) Prioriterer fremdrift og leveranser. Han strammer inn oppgavefordelingen, "
        "har hyppige statusmøter og ber alle fokusere på å få prototypen ferdig."
    )

    choice = get_choice("Velg A eller B: ")
    print()
    if choice == "A":
        print(
            "Erling setter av tid til å snakke om samarbeid, forventninger og hvordan "
            "teamet har det. Det oppleves som en pause i presset, og noen konflikter "
            "tones ned når folk får sagt fra på en trygg måte."
        )
    else:
        print(
            "Erling legger vekt på fremdrift. Han tydeliggjør prioriteringer og "
            "forventer at alle fokuserer på leveransen. Konflikter skyves i større "
            "grad til side, og tempoet i arbeidet øker."
        )
    return choice


def determine_outcome(choice1: str, choice2: str, choice3: str):
    """
    Bestemmer sluttutfall basert på kombinasjonen av valg.

    Her har vi tre hovedutfall:
    - Utfall 1: Samarbeid styrkes (god konflikt- og relasjonshåndtering)
    - Utfall 2: Konflikter delvis løst, men sårbare relasjoner
    - Utfall 3: Prosjektet forsinkes eller samholdet svekkes tydelig
    """
    print("\nSLUTTUTFALL\n")

    if choice1 == "A" and choice2 == "A" and choice3 == "A":
        # Konsekvent fokus på åpenhet, avklaring og relasjoner
        print(
            "Utfallet er at samarbeidet i teamet styrkes. Ved å ta konfliktene åpent, "
            "avklare uenigheter tidlig og investere i relasjonsbygging, klarer Erling "
            "å lede teamet videre mot en norming-fase. Prototypen leveres, og både "
            "motivasjon og tillit er relativt høy."
        )

    elif choice3 == "B" and (choice1 == "B" or choice2 == "B"):
        # Minst én konflikt er skjøvet under teppet, og fokus ligger primært på tempo
        print(
            "Utfallet er at prosjektet blir preget av slitasje. Selv om prototypen "
            "til slutt leveres, har konfliktene i liten grad blitt løst. Noen "
            "teammedlemmer opplever lavere motivasjon og svekket tillit, og "
            "prosjektet kunne hatt et bedre arbeidsmiljø."
        )

    else:
        # Blandet mønster av valg: noe er håndtert, noe er uavklart
        print(
            "Utfallet er delvis positivt. Enkelte konflikter er håndtert på en "
            "konstruktiv måte, mens andre fortsatt ligger og ulmer. Teamet klarer "
            "å levere en prototype, men relasjonene i gruppen er sårbare, og "
            "videre samarbeid vil kreve bevisst oppfølging."
        )


def main():
    """
    Hovedfunksjon som kjører hele historien.
    """
    intro()
    choice1 = decision_1()
    choice2 = decision_2()
    choice3 = decision_3()
    determine_outcome(choice1, choice2, choice3)


if __name__== "__main__":
    main()


