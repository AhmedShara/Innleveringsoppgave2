# HISTORY OM ERLING-PROSKJEKLEDER
# programmet simulerer på storylinen del1
# den har tenkte å ha tre beslutningspunkter
# To valg per punkt (A eller B)
# minst tre utfall basert på valg
# Erling styrer spilleren gjennom valgene

def valg(prompt: str) -> str:
    # hjelpefunksjon for å få brukeren til å velge A eller B
    while True:
        svar = input(prompt).strip().upper()
        if svar in ("A", "B"):
            return svar
        print("Ugyldig valg. Skriv A eller B.")

def intro():
    # introduksjon til historien
    print("Velkommen til historien om Erling og prosjektet med medborgerportalen.")
    print("Det har gått seks uker siden prosjektet startet. Stemningen er ikke like god "
          "som i starten, og flere konflikter har begynt å vokse frem i teamet.")
    print("Som prosjektleder må Erling ta noen viktige valg som vil påvirke både "
          "samarbeid, motivasjon og resultat.")

def beslutning_1() -> str:
    # beslutning 1 om konflikten mellom Silje og Sivert
    print("\nBESLUTNING 1: KONFLIKTEN MELLOM SILJE OG SIVERT\n")
    print("Silje (UX-designer) og Sivert (IT-rådgiver) er uenige om teknologivalg og design.")
    print("\nHva gjør Erling?")
    print("A) Tar konflikten opp i plenum og inviterer til åpen dialog i hele teamet.")
    print("B) Tar individuelle samtaler med Silje og Sivert for å dempe temperaturen.")

    valg1 = valg("Velg A eller B: ")
    if valg1 == "A":
        print("Erling kaller inn hele laget. Han setter noen dialogregler og ber Silje og Sivert "
              "beskrive sine behov og perspektiver. Konflikten blir tydelig for alle, og teamet "
              "prøver å finne en felles løsning.")
    else:
        print("Erling tar en-til-en-samtaler med Silje og Sivert. Han hører på hvordan de opplever "
              "situasjonen, rydder i misforståelser og ber dem holde en profesjonell tone videre.")
    return valg1

def beslutning_2() -> str:
    # beslutning 2 om uenigheten mellom Hamdi og Jabir
    print("\nBESLUTNING 2: UENIGHET MELLOM HAMDI OG JABIR\n")
    print("Hamdi ønsker en kontrollert løsning, mens Jabir ønsker et mer åpent system.")
    print("\nHva gjør Erling?")
    print("A) Kaller inn Hamdi og Jabir til et felles møte.")
    print("B) Avventer og håper de finner en løsning selv.")

    valg2 = valg("Velg A eller B: ")
    if valg2 == "A":
        print("Erling inviterer Hamdi og Jabir til et møte. De får legge frem sine bekymringer "
              "og ønsker. Det blir en krevende, men ærlig diskusjon.")
    else:
        print("Erling velger å ikke gripe inn nå. Teamet jobber videre, men med ulike forventninger.")
    return valg2

def beslutning_3() -> str:
    # beslutning



