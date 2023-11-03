# opdracht 2

print(3 * "hallo")
# De uitkomst is "hallohallohallo"

# opdracht 3

# Laat de persoon getallen invoeren voor var1, var2 en var3
var1 = float(input("Voer het eerste getal in: "))
var2 = float(input("Voer het tweede getal in: "))
var3 = float(input("Voer het derde getal in: "))

# Bereken het gemiddelde van var1, var2 en var3
gemiddelde = (var1 + var2 + var3) / 3

# Toon het gemiddelde
print("Het gemiddelde is:", gemiddelde)

# opdracht 4

straal = float(input("Voer de straal van de cirkel in: "))
pi = 3.14159

oppervlakte = straal * straal * pi
print(f"De oppervlakte van een cirkel {straal} is {oppervlakte}")