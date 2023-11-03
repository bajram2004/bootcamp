cijfer = float(input("voer een cijfer in "))

cijfer_omschrijving ={ 
10:	"uitmuntend",
9:	"zeer goed",
8:	"goed",
7:	"ruim voldoende",
6:	"voldoende",
5:	"bijna voldoende",
4:	"onvoldoende",
3:	"gering",
2:	"slecht",
1:	"zeer slecht",
}
if cijfer in cijfer_omschrijving:
    omschrijving = cijfer_omschrijving [cijfer]
    print(f"De omschrijving voor het cijfer {cijfer} is: {omschrijving}")
else:
    print("Ongeldig cijfer. Voer een geldig cijfer tussen 0.0 en 10.0 in.")
    
# opdracht 2
cijfer = input("Voer een cijfer tussen 1 en 10 in: ")

try:
    cijfer = int(cijfer)
    if 1 <= cijfer <= 10:
        omschrijving = ""
        if cijfer == 10:
            omschrijving = "uitmuntend"
        elif cijfer == 9:
            omschrijving = "zeer goed"
        elif cijfer == 8:
            omschrijving = "goed"
        elif cijfer == 7:
            omschrijving = "ruim voldoende"
        elif cijfer == 6:
            omschrijving = "voldoende"
        elif cijfer == 5:
            omschrijving = "bijna voldoende"
        elif cijfer == 4:
            omschrijving = "onvoldoende"
        elif cijfer == 3:
            omschrijving = "gering"
        elif cijfer == 2:
            omschrijving = "slecht"
        elif cijfer == 1:
            omschrijving = "zeer slecht"

        if cijfer >= 6:
            print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
        else:
            print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")
    else:
        print("Dit kan ik niet omzetten!")
except ValueError:
    print("Ongeldige invoer. Voer een geldig cijfer tussen 1 en 10 in.")
