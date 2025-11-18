# Interaktiv historie
print("Velkommen til min interaktive historie om prosjektledelse!\n")
print("Teamet ditt har nå nådd en fase med konflikter og meningsforskjeller, og du må som Erling ta viktige beslutninger\n")

print("I prosjektet ditt samarbeider teamet ditt som består av Silje, Sivert, Hamdi og Jabir.\n")
print("Det oppstår konflikter og uenigheter i teamet som påvirker fremdriften av prosjektet.\n")

print("Som prosjektleder må du ta beslutninger for å løse konfliktene og få teamet tilbake på sporet\n")
print("Hvordan vil du håndtere situasjonen? Du har tre beslutninger med 2 mulige utfall.\n")    

# Beslutning 1
print("Beslutning 1: Hvordan håndtere konflikten mellom Silje og Sivert?\n")
print("A: Arranger individuelle møter med begge for å forstå deres perspektiver og finne en felles løsning.\n") 
print("B: Ignorer konflikten og håp at den løser seg selv.\n")
valg1 = input("Velg A eller B for ditt valg: \n")   

if valg1 == "A":
    print("Silje og Sivert føler seg hørt og respektert. De jobber sammen for å finne en løsning, og teamet blir sterkere.\n")  
elif valg1 == "B":
    print("Konflikten eskalerer, og teamets moral synker. Prosjektet blir forsinket på grunn av manglende samarbeid.\n")    
else:
    print("Ugyldig valg. Vennligst velg A eller B.\n")
# Beslutning 2  
print("Beslutning 2: Hvordan håndtere uenigheten mellom Hamdi og Jabir?\n")
print("A: Fasiliter en gruppe diskusjon for å adressere uenigheten åpent og ærlig.\n")
print("B: Avvent og håp på at konflikten løser seg selv.\n")      
valg2 = input("Velg A eller B for ditt valg: \n") 
if valg2 == "A":
    print("Gruppediskusjonen fører til bedre forståelse og samarbeid mellom Hamdi og Jabir. Teamet jobber mer effektivt sammen.\n")
elif valg2 == "B":
    print("Uenigheten fører til splittelse i teamet, og prosjektets fremdrift blir alvorlig påvirket.\n")
else:
    print("Ugyldig valg. Vennligst velg A eller B \n.")
# Beslutning 3
print("Beslutning 3: Hvordan kan Erling bevare motivasjonen i teamet?\n")
print("A: Sette av tid til relasjonsbygging.\n")
print("B: Fokusere kun på oppgaveløsning og resultater.\n")

valg3 = input("Velg A eller B for ditt valg: \n")   
if valg3 == "A":
    print("Relasjonsbygging styrker teamets samhold og motivasjon. Prosjektet går fremover med fornyet energi.\n")
elif valg3 == "B":
    print("Mangelen på fokus på relasjoner fører til utbrenthet og lav moral i teamet, noe som påvirker prosjektets suksess.\n")
else:
    print("Ugyldig valg. Vennligst velg A eller B.\n")

print("\n--- SLUTTRESULTAT ---\n")

# Tre mulige utfall basert på kombinasjon av valg
if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("Teamet fungerer optimalt! Alle konflikter er løst, samarbeidet styrkes,")
    print("og prosjektet fullføres på en effektiv og harmonisk måte. Gratulerer!")
    
elif (valg1 == "B" or valg2 == "B") and valg3 == "A":
    print("Teamet har fortsatt noen utfordringer med konflikter, men relasjonsbygging")
    print("har holdt motivasjonen oppe. Prosjektet fullføres, men med noen forsinkelser og utfordringer underveis.")
    
else:
    print("Konfliktene og manglende fokus på motivasjon har svekket teamet.")
    print("Prosjektet blir forsinket, samarbeidet sliter, og kvaliteten på resultatet blir lavere enn forventet.")
