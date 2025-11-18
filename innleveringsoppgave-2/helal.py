# HISTORY OM ERLING-PROSKJEKLEDER
#programmet simulrer på storylinen del1
#den har tenkte å ha tre besluktningerspunkter
#To valg per punkt(A eller B) 
#minst tre utfall basert på valg
#erling styrer spilleren gjennom valgenen


def valg(prompt: str) -> str:
    # helpefunskon for å få bruke valge A eller B
    while True:
        svar = input(prompt).strip().upper()
        if svar in ("A", "B"):
            return svar
        print("Ugyldig valg. Skriv A eller B.")


def intro():
    # i introduksion til historien
    print("Velkommen til historien om Erling og prosjektet med medborgerportalen.")
    print(
        "Det har gått seks uker siden prosjektet startet. Stemningen er ikke like god "
        "som i starten, og flere konflikter har begynt å vokse frem i teamet."
    )
    print(
        "Som prosjektleder må Erling ta noen viktige valg som vil påvirke både "
        "samarbeid, motivasjon og resultat."
    )


def beslutning_1() -> str:
    # beslutning 1 om koflikten mellom silje og sivert
    print("\nBESLUTNING 1: KONFLIKTEN MELLOM SILJE OG SIVERT\n")
    print(
        "Silje (UX-designer) og Sivert (IT-rådgiver) er uenige om teknologivalg og "
        "design. Det som startet som en faglig diskusjon, har utviklet seg til en "
        "personlig konflikt. Resten av teamet begynner å ta side."
    )
    print("\nHva gjør Erling?")
    print("A) Tar konflikten opp i plenum og inviterer til åpen dialog i hele teamet.")
    print("B) Tar individuelle samtaler med Silje og Sivert for å dempe temperaturen.")

    valg1 = valg("Velg A eller B: ")
    if valg1 == "A":
        print("Erling helel laget inn. Han setter noen dialog og ber Silje og Sivert sin behov og persketiver. "
              "Kofliketen blir tydlig for alle og teamet prøver å finne en felles løsnig.")
    else:
        print("Erling tar en til en samtaler med Silje og Sivert. Han hører på hvordan de "
              "opplever situasjonen, prøver å rydde i misforståelser og ber dem holde "
              "en profesjonell tone videre i prosjektet.")
    return valg1


def beslutning_2() -> str:
    """
    Beslutning 2: Hvordan håndterer Erling uenigheten mellom Hamdi og Jabir?
    Returnerer 'A' eller 'B'.
    """
    print("\nbeslutning_2: uenigheter mellom jabar og hamdi")
    print("Samtidig ulmer en konflikt mellom Hamdi (kulturavdelingen) og Jabir "
          "(brukerrepresentant). De er uenige om hvor åpen plattformen for digitale "
          "folkemøter skal være.")
    print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, "
          "mens Jabir ønsker et mer åpent og dialogbasert system.")

    print("\nHva gjør Erling?")
    print("A) Kaller inn Hamdi og Jabir til et felles møte for å avklare uenigheten "
          "og diskutere mål og rammer.")
    print("B) Avventer, og håper at Hamdi og Jabir selv finner en løsning mens teamet "
          "fortsetter å jobbe mot milepælen.")

    valg2 = valg("Velg A eller B: ")
    if valg2 == "A":
        print("Erling inviterer Hamdi og Jabir til et møte. De får legge frem sine "
              "bekymringer og ønsker. Det blir en krevende, men ærlig diskusjon om "
              "balansen mellom kontroll, demokrati og risiko.")
    else:
        print("Erling velger å ikke gripe inn nå. Han vurderer at konflikten foreløpig "
              "er lavmælt, og ønsker å unngå flere møter. Teamet jobber videre, men "
              "fortsatt med ulike forventninger til innbyggerdialog.")
    return valg2


def beslutning_3() -> str:
    """
    Beslutning 3: Hvordan bevarer Erling motivasjonen i teamet?
    Returnerer 'A' eller 'B'.
    """
    print("\nBESLUTNING 3: MOTIVASJON OG SAMHOLD\n")
    print("Det nærmer seg milepæl. Prototypen skal være klar om tre uker. "
          "Konflikter, tidspress og usikkerhet har tappet energi i teamet.")

    print("\nHva gjør Erling?")
    print("A) Setter av tid til relasjonsbygging, for eksempel en felles refleksjonsøkt "
          "eller en sosial aktivitet for å styrke tillit og samarbeid.")
    print("B) Prioriterer fremdrift og leveranser. Han strammer inn oppgavefordelingen, "
          "har hyppige statusmøter og ber alle fokusere på å få prototypen ferdig.")

    valg3 = valg("Velg A eller B: ")
    if valg3 == "A":
        print("Erling setter av tid til å snakke om samarbeid, forventninger og hvordan "
              "teamet har det. Det oppleves som en pause i presset, og noen konflikter "
              "tones ned når folk får sagt fra på en trygg måte.")
    else:
        print("Erling legger vekt på fremdrift. Han tydeliggjør prioriteringer og "
              "forventer at alle fokuserer på leveransen. Konflikter skyves i større "
              "grad til side, og tempoet i arbeidet øker.")
    return valg3


def determine_outcome(choice1: str, choice2: str, choice3: str):
    """
    Bestemmer sluttutfall basert på kombinasjonen av valg.
    """
    print("\nSLUTTUTFALL\n")
    if choice1 == "A" and choice2 == "A" and choice3 == "A":
        print("Utfallet er at samarbeidet i teamet styrkes. Prototypen leveres, og både "
              "motivasjon og tillit er relativt høy.")
    elif choice3 == "B" and (choice1 == "B" or choice2 == "B"):
        print("Utfallet er at prosjektet blir preget av slitasje. Selv om prototypen "
              "til slutt leveres, har konfliktene i liten grad blitt løst. Noen "
              "teammedlemmer opplever lavere motivasjon og svekket tillit.")
    else:
        print("Utfallet er delvis positivt. Enkelte konflikter er håndtert på en "
              "konstruktiv måte, mens andre fortsatt ligger og ulmer. Teamet klarer "
              "å levere en prototype, men relasjonene i gruppen er sårbare.")


def main():
    intro()
    valg1 = beslutning_1()
    valg2 = beslutning_2()
    valg3 = beslutning_3()
    determine_outcome(valg1, valg2, valg3)


if __name__ == "__main__":
    main()