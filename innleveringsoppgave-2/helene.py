# Interaktiv historie: Erling som prosjektleder

# teller hvor mange "gode" valg som tas 
positive_valg = 0

# --------- INTRODUKSJON ------------

print("Velkommen til historien til Erling. Han er prosjektleder for den digitale medborgerportalen.\n")
print("Etter en god oppstart har prosjektet nå gått inn i en mer krevende periode.")
print("Silje og Sivert er i konflikt om teknologivalg og design.")
print("Og det ulmer en uenighet mellom Hamdi og Jabir om hvordan innbyggerne skal involveres.")
print("Samtidig begynner teamet å bli slitene, og fristen for første prototype nærmer seg.\n")

print("Du skal ta tre valg som påvirker prosjektet.\n")


# 2. --------- BESLUTNING 1 ---------------
print("Hvordan håndterer Erling konflikten mellom Silje og Sivert?")

print("Silje (UX-designer) og Sivert (IT-rådgiver) har en konflikt om teknologivalg og design.")
print("Uenigheten har gått fra faglig diskusjon til personlig irritasjon.")
print("Erling må bestemme seg for hvordan han vil håndtere situasjonen.\n")

print("a) Ta konflikten felles med hele teamet.")
print("b) Snakke med dem hver for seg.\n")

valg1 = input("Velg (a/b): ").lower()

if valg1 == "a":
    positive_valg += 1
    print("\nErling tar konflikten felles i teamet.")
    print("Alle får en innsikt i hva som skaper frustrasjon og diskuterer felles løsninger.")
    print("Noen synes det blir litt ubehagelig, men åpenhet gjør at flere forstår hverandre.\n")
elif valg1 == "b":
    positive_valg += 1
    print("\nErling tar en til en samtale med Silje og Sivert.")
    print("De får ro til å forklare sine perspektiver uten å tape ansikt foran resten av gruppen.")
    print("Konflikten roes ned, men teamet er fortsatt usikre på hva som egentlig skjer.\n")
else: 
    print("\nErling klarer ikke å bestemme seg og gjør ingenting.")
    print("Konflikten mellom Silje og Sivert fortsetter å ulme i bakgrunnen.\n") 


# ------------ BESLUTNING 2 ------------
print("Hvordan håndterer han uenigheten mellom Hamdi og Jabir?")
print("Hamdi ønsker kontrollert innbyggerdialog. Jabir ønsker en mer åpen løsning.\n")
print("Erling merker at frustrasjonen øker, selv om konflikten ennå ikke har eksplodert.\n")

print("a) Holde et felles møte for å avklare uenigheten.")
print("b) Avvente og håpe det løser seg.\n")

valg2 = input("Velg (a/b): ").lower()

if valg2 == "a":
    positive_valg += 1
    print("\nErling kaller inn til et felles møte.")
    print("Hamdi og Jabir får presentere sine forslag og finner sammen et kompromiss")
    print("Teamet opplever at ulike meninger blir tatt på alvor.\n")
elif valg2 == "b":
    print("\nErling velger å avvente.")
    print("Spenningsnivået øker sakte, men sikkert, og det blir vanskeligere å ta opp temaet senere.\n")
else:
    print("\Erling tar ingen tydelig beslutning")
    print("Uenigheten mellom Hamdi og JAbir forblir uavklart og skaper usikkerhet.\n")


# ------------ BESLUTNING 3 ------------

print("\n=== Motivasjon i teamet ===")
print("Teamet begynner å bli slitene etter flere uker med konflikter og tidspress.\n")
print("Fristen for første prototype nærmer seg, og Erling må velge strategi for å holde motivasjonen oppe.\n")


print("a) Ta en liten sosial pause sammen.")
print("b) Sette leveransen først og jobbe målrettet videre.\n")

valg3 = input("Velg (a/b): ").lower()

if valg3 == "a":
    positive_valg += 1
    print("\Erling organiserer en kort sosial pause.")
    print("Teamet får pustet ut, le litt og minne hverandre på hvorfor de gjør dette.")
    print("Stemningen blir merkart bedre, og flere får en ny energi til å jobbe viderem\n")
elif valg3 == "b":
    print("\nErling velger å prioritere leveransen.")
    print("De kommer litt lenger på prototypen, men slitasjen i gruppa øker.\n")
else:
    print("\nErling gjør ingen endring i arbeidsformen")
    print("Motivasjonen fortsetter å synke, og folk trekker seg mer tilbake.\n")


# ------------ SLUTTRESULTAT ------------
print("\n=== Sluttresultat ===\n")

if positive_valg >= 3:
    print("SLUTT: Prosjektet lykkes!")
    print("Konfliktene blir håndtert på en konstruktiv måte, teamet samarbeider godt")
    print("og leverer en solid første prototype innen fristen.")
elif positive_valg == 2:
    print("SLUTT: Prosjektet går videre, men samarbeidet er sårbart.")
    print("Noen konflikter er delvis løst, men det ligger fortsatt spenninger under overflaten.")
    print("Prosjektet leverer, men Erling må jobbe videre med relasjonene og kommunikasjonen.")
else:
    print("SLUTT: Konfliktene ble ikke godt nok håndtert.")
    print("Prosjektet blir forsinket, og tilliten i teamet svekkes")
    print("Erling innser at han må ta tak i samarbeidet før de kan komme seg videre.")


print("\nErling takker for hjelpen!")


