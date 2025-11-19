# bmagnus2506.py

# Programmet kjører i terminal og lar brukeren (Erling) ta tre valg som påvirker utfallet.

print("  IS-118: Interaktiv historie")

print("Erling leder et  prosjektteam som har gått inn i storming-fasen.")
print("Konflikter og uenigheter skaper en intern spenning, og Erling må gjøre kloke valg.\n")


# -------------------------
# BESLUTNINGSPUNKT 1
# -------------------------
print("\n--- Beslutning 1: Konflikten mellom Silje og Sivert ---")
print("Silje og Sivert har havnet i en personlig konflikt som påvirker teamet.\n")

print("A: Ta konflikten åpent i plenum")
print("B: Ha individuelle samtaler først\n")

valg1 = input("Hva gjør Erling? (A/B): ").strip().upper()

if valg1 not in ("A", "B"):
    print("Ugyldig valg – plenum (A) velges automatisk.")
    valg1 = "A"

if valg1 == "A":
    print("\nDu tar konflikten i plenum. Det blir en ærlig, men intens diskusjon.")
    print("Teamet får bedre innsikt, men konfliktnivået øker midlertidig.")
else:
    print("\nDu tar individuelle samtaler. Temperaturen dempes, men konflikten er ikke helt løst.")

# -------------------------
# BESLUTNINGSPUNKT 2
# -------------------------
print("\n--- Beslutning 2: Uenigheten mellom Hamdi og Jabir ---")
print("Uenigheten mellom dem er foreløpig lav, men kan eskalere.\n")

print("A: Kalle inn til et avklaringsmøte nå")
print("B: Avvente og håpe det løser seg selv\n")

valg2 = input("Hva gjør Erling? (A/B): ").strip().upper()

if valg2 not in ("A", "B"):
    print("Ugyldig valg – avklaringsmøte (A) velges automatisk.")
    valg2 = "A"

if valg2 == "A":
    print("\nDu kaller inn til møte. Uenigheten dempes før den vokser.")
else:
    print("\nDu avventer. Spenningen mellom dem øker litt, men ikke dramatisk ennå.")

# -------------------------
# BESLUTNINGSPUNKT 3
# -------------------------
print("\n--- Beslutning 3: Motivere teamet ---")
print("Teamet er slitent etter konflikter. Erling må styrke motivasjonen.\n")

print("A: Prioritere relasjonsbygging og trygghet")
print("B: Prioritere fremdrift og leveranser\n")

valg3 = input("Hva gjør Erling? (A/B): ").strip().upper()

if valg3 not in ("A", "B"):
    print("Ugyldig valg – relasjonsbygging (A) velges automatisk.")
    valg3 = "A"

if valg3 == "A":
    print("\nDu fokuserer på relasjonsbygging. Teamet senker skuldrene og finner felles grunn.")
else:
    print("\nDu fokuserer på fremdrift. Teamet jobber raskere, men er fortsatt slitne.")

# -------------------------
# SLUTTUTFALL
# -------------------------
print("\n============================")
print("           UTFALL")
print("============================\n")

# Endepunkt 1: Teamet når norming (1B - 2A - 3A)
if valg1 == "B" and valg2 == "A" and valg3 == "A":
    print("✨ UTFALL: Teamet gjenoppretter tillit og går videre til norming-fasen.")
    print("Erling sin rolige tilnærming skaper trygghet, og gruppen lærer av konfliktene.")
    print("Prosjektet får ny energi og samarbeidet forbedres markant.")

# Endepunkt 2: Konflikten løses delvis, men relasjonen er sårbar (1A - 2A - 3B)
elif valg1 == "A" and valg2 == "A" and valg3 == "B":
    print("UTFALL: Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    print("Prosjektet kommer fremover, men teamet mangler den psykologiske tryggheten som")
    print("kunne gjort dem virkelig sterke.")

# Endepunkt 3: Prosjektet blir værende i storming-fasen (1A - 2B - 3B)
elif valg1 == "A" and valg2 == "B" and valg3 == "B":
    print("UTFALL: Prosjektet mister samhold og forsinkes.")
    print("Uklare konflikter eskalerer, motivasjonen synker og kommunikasjonen bryter sammen.")
    print("Fremdriften stopper opp, og milepælene ryker.")

# Alle andre kombinasjoner → middels utfall (blandet)
else:
    print("UTFALL: Teamet kommer seg videre, men med blandede resultater.")
   



