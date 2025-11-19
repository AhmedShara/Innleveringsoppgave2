print("Velkommen Til Erlings Prosjekthverdag!\n")

#--------------Beslutning 1---------
print("Beslutning 1: Silje og Sivert krangler. hva gjør Erling?")
print("A: Tar konflikten åpent i plenum")
print("B:snakker med dem hver for seg")

valg1 = input("Valg A eller B:")

# -------------Beslutning 2---------
print("\nBeslutning 2: Hamdi og Jabir er uenige. hva gjør Erling?")
print("A: kaller dem inn til et avklaringsmøte")
print("B: Avventer og ser om det løser seg selv")

valg2 = input("Valg A eller B:")
#--------------Beslutning 3---------
print("\nBeslutning 3: Teamet mister motivasjonen. hva gjør Erling?")
print("A: Bruker tid på relasjonsbygging")
print("B: Fokuserer på fremdrift og leveranser")

valg3 = input("Valg A eller B:")

#--------------Sluttutfall---------

print("\n---utfall---")

if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("teamet får bedre samarbeid og prosjektet går inn i en posoitiv norming fase.")
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("Konflikter eskalerer og prosjektet havner i kaos.og det blir forsinkelser.")
else:
    print("prosjektet går videre med blandede resultater. noen konflikter løses mens andre vedvarer.")