# Interaktiv historie: Erling som prosjektleder

#------------------------------------
# 1.INTRODUKSJON
#------------------------------------
print("Velkommen til historien om Erling, prosjektleder for den digitale medborgerportalen.\n")
print("Etter en god oppstart har prosjektet nå gått inn i en mer krevende periode.")
print("Silje og Sivert er i konflikt om teknologi valg og design.")
print("Og det ulmer en uenighet mellom Hamdi og Jabir om hvordan innbyggerne skal involveres.")
print("Samtidig begynner teamet å bli slitent, og fristen for første prototype nærmer seg.\n")

print("Du skal ta tre valg som påvirker prosjektet.\n")

#-------------------------------------
# 2. BESLUTNINGSPUNKT 1
#Hvordan håndterer Erling konflikten mellom Silje og Sivert?
#-------------------------------------
print("=== Beslutningspunkt 1: Konflikten mellom Silje og Sivert ===\n")
print("Silje (UX-designer) og Sivert (IT-rådgiver) har en konflikt om teknologivalg og design.")
print("Uenigheten har gått fra faglig diskusjon til personlig irritasjon.")
print("Erling må bestemme seg for hvordan han vil håndtere situasjonen.\n")

print("a) Ta konflikten felles med hele teamet.")
print("b) Snakke med dem hver for seg.\n")

valg1 = input("Velg (a/b): ").lower()

# ------------ BESLUTNING 2 ------------
print("Hvordan håndterer han uenigheten mellom Hamdi og Jabir?")
print("Hamdi ønsker kontrollert innbyggerdialog. Jabir ønsker en mer åpen løsning.\n")
print("Erling merker at frustrasjonen øker, selv om klomflikten ennå ikke har eklpodert.\n")

print("a) Invitere til et felles møte for å avklare uenigheten.")
print("b) Avvente og håpe det løser seg.\n")

valg2 = input("Velg (a/b): ").lower()

# ------------ BESLUTNING 3 ------------
print("\n=== Motivasjon i teamet ===")
print("Teamet begynner å blir slitent etter flere uker med konflikter og tidspress.\n")
print("Fristen for første prototype nærmer seg, og Erling må velge strategi for å holde motivasjonen oppe.\n")


print("a) Gjøre en kort teambuilding-aktivitet.")
print("b) Fokusere kun på leveransen og jobbe videre.\n")

valg3 = input("Velg (a/b): ").lower()

# ------------ SLUTTRESULTAT ------------
print("\n=== Sluttresultat ===\n")

if valg1 == "a" and valg2 == "a" and valg3 == "a":
    print("SLUTT: Prosjektet lykkes! Teamet samarbeider godt og leverer en god prototype.")
elif valg1 == "b" and valg2 == "b":
    print("SLUTT: Konfliktene ble ikke håndtert. Prosjektet blir forsinket.")
else:
    print("SLUTT: Prosjektet går videre, men samarbeidet er ustabilt og krever oppfølging.")

print("\nErling takker for hjelpen!")


