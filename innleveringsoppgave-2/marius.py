print("Velkommen til historien om Erling og medborgerportalen!\n")
print("Du er prosjektleder Erling. Valgene dine avgjør om teamet kommer videre fra storming-fasen.\n")

score = 0

def valg(tekst):
    s = input(tekst).strip().upper()
    if s not in ("A", "B"):
        print("Ugyldig svar, tolker det som B.\n")
        s = "B"
    return s

print("BESLUTNING 1: Silje og Sivert i konflikt om design og teknologi.\n")
print("A) Ta konflikten åpent i plenum.")
print("B) Ta individuelle samtaler først.\n")
v1 = valg("Skriv A eller B: ")
if v1 == "A":
    print("\nMøtet i plenum skaper åpenhet, men stemningen blir litt anspent.\n")
else:
    print("\nSamtaler én-til-én roer ned situasjonen og gir deg bedre oversikt.\n")
    score += 1

print("BESLUTNING 2: Uenighet mellom Hamdi og Jabir om innbyggerdialog.\n")
print("A) Kalle inn til et avklaringsmøte.")
print("B) Avvente og håpe de løser det selv.\n")
v2 = valg("Skriv A eller B: ")
if v2 == "A":
    print("\nMøtet gjør uenigheten tydelig, men dere finner noen felles løsninger.\n")
    score += 1
else:
    print("\nDu avventer. Uenigheten ulmer videre og frustrasjonen øker.\n")
    score -= 1

print("BESLUTNING 3: Motivasjon og stemning i teamet.\n")
print("A) Sette av tid til relasjonsbygging og teambuilding.")
print("B) Fokuserer hardt på fremdrift og leveranser.\n")
v3 = valg("Skriv A eller B: ")
if v3 == "A":
    print("\nDere prater sammen, får luftet frustrasjon og styrker samholdet.\n")
    score += 1
else:
    print("\nDere jobber effektivt videre, men underliggende spenninger blir ikke tatt opp.\n")

print("=== SLUTT PÅ HISTORIEN ===\n")
if score >= 2:
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
    print("Konfliktene er håndtert på en god måte, og samarbeidet styrkes.")
elif score == 1:
    print("Konfliktene løses delvis, men relasjonene er fortsatt sårbare.")
    print("Prosjektet går videre, men gamle spenninger kan dukke opp igjen.")
else:
    print("Prosjektet mister samhold og blir forsinket.")
    print("Konfliktene blir hengende i lufta, motivasjonen faller, og teamet stopper opp i storming-fasen.")

print("\nTakk for at du spilte historien om Erling!")
