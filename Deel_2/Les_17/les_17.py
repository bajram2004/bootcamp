import random

def raad_het_getal():
    aantal_rondes = 0
    aantal_fouten = 0
    
    while True:
        doorgaan = input("Wil je een ronde spelen? (ja/nee): ").lower()
        if doorgaan != "ja":
            break

        aantal_rondes += 1
        te_radend_getal = random.randint(1, 100)
        
        while True:
            try:
                geraden_getal = int(input("Raad het getal tussen 1 en 5: "))
                if geraden_getal < 1 or geraden_getal > 100:
                    print("Het getal moet tussen 1 en 5 liggen.")
                    continue
                
                if geraden_getal == te_radend_getal:
                    print("Je hebt het getal goed geraden!")
                    break
                else:
                    print("Je hebt het getal niet goed geraden!")
                    aantal_fouten += 1
            except ValueError:
                print("Ongeldige invoer. Voer een getal tussen 1 en 100 in.")
    
    print(f"Aantal gespeelde rondes: {aantal_rondes}")
    print(f"Aantal fouten gemaakt: {aantal_fouten}")

raad_het_getal()