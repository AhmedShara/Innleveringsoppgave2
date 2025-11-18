
# Erling prosjektleder - konflikthåndtering

print("Erling er prosjektleder for et team hvor det har oppstått noen uenigheter.")
print("Du må hjelpe han med å løse opp i disse konfliktene og bygge opp teamet.\n")

# Beslutning 1: Silje og Sivert
print("Første utfordring: Konflikten mellom Silje og Sivert har utviklet seg til en personkonflikt.")
valg1 = input("Hvordan vil du håndtere dette?\nA: Ta konflikten åpen refleksjon i plenum\nB: Ha individuelle samtaler først\nSkriv A eller B: ")

if valg1 == "A":
    print(
        "\nDu samler hele teamet for å adressere konflikten.\n"
        f"Teamet får mulighet til å snakke ut, og dere oppnår bedre forståelse.\n"
        f"Men stemningen er fortsatt litt spent.\n"
    )
elif valg1 == "B":
    print(
        "\nDu snakker med Silje og Sivert hver for seg.\n"
        f"Du får innsikt i underliggende frustrasjoner, men resten av teamet er fortsatt usikre.\n"
        f"Du vurderer neste steg nøye.\n"
    )
else:
    print(
        "\nUgyldig valg. Du mister muligheten til å gripe inn, og konflikten eskalerer.\n"
        f"Teamet mister tillit til deg som leder.\n"
    )

# Beslutning 2: Hamdi og Jabir
print("Neste utfordring: Du merker økende frustrasjon mellom Hamdi og Jabir.")
valg2 = input("Hva gjør du?\nA: Kaller dem inn til et avklaringsmøte\nB: Avventer og håper det løser seg\nSkriv A eller B: ")

if valg2 == "A":
    print(
        "\nDu setter opp et strukturert møte.\n"
        f"De får snakket ut, og dere oppnår felles forståelse.\n"
        f"Teamet blir mer samkjørt før deadline.\n"
    )
elif valg2 == "B":
    print(
        "\nDu velger å avvente.\n"
        f"Frustrasjonen øker, og samarbeidet svekkes.\n"
        f"Du begynner å bekymre deg for leveransen.\n"
    )
else:
    print(
        "\nUgyldig valg. Du mister muligheten til å forebygge konflikt.\n"
        f"Teamet blir mer splittet.\n"
    )

# Beslutning 3: Motivasjon og samhold
print("Siste utfordring: Stemningen er preget av usikkerhet og lav motivasjon.")
valg3 = input("Hva prioriterer du?\nA: Sosial aktivitet\nB: Fremdrift og leveranser\nSkriv A eller B: ")

if valg3 == "A":
    print(
        "\nDu setter av tid til teambuilding og refleksjon."
        f"Teamet får ny energi og beveger seg mot norming-fasen.\n"
        f"Prosjektet får bedre langsiktig samarbeidsevne.\n"
    )
elif valg3 == "B":
    print(
        "\nDu fokuserer på leveranser og tydelig styring.\n"
         f"Teamet leverer, men relasjonene svekkes.\n"
         f"Du ser tegn til utmattelse og lav trivsel.\n"
    )
else:
    print(
        "\nUgyldig valg. Du mister muligheten til å styrke teamet.\n"
        f"Prosjektet mister både fremdrift og motivasjon.\n"
    )
    
if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print(
        "\nGratulerer! Du har navigert teamet gjennom prosjektet med suksess.\n"
        f"Teamet ditt er nå sterkere, mer samkjørt, og klare for de neste utfordringene!\n"
    )
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print(
        "\nDessverre har teamet ditt slitt gjennom prosjektet.\n"
        f"Konflikter og lav motivasjon har svekket samarbeidet.\n"
        f"Vurder å ta grep for å gjenoppbygge tillit og samhold i teamet ditt.\n"
    )
else:
    print("\nDu har tatt noen gode valg, men også noen som kunne vært bedre.")      

print("Takk for at du tok rollen som Erling!")
     

    