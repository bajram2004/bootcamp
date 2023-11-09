# opdracht 1
#
#

# opdracht 2

# a = 5  dit is een voorbeeld van het datatype: integer
# b = 10.5  dit is een voorbeeld van het datatype: float
# c = "Hallo wereld"  dit is een voorbeeld van het datatype: string

# opdracht 3

a = 5
b = 10

temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")

# opdracht 4

leeftijd = int(input("Hoe oud ben je?"))
jaar_tot_pensioen = 67 - leeftijd
print(f"Dan duurt het nog ongeveer {jaar_tot_pensioen} jaar voordat je met pensioen mag!")

# opdracht 5

def som(a, b, c):
    return a + b + c

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som(getal1, getal2, getal3)
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

# opdracht 6

AANTAL_GB = 20  # Aantal GB data in je bundel
AANTAL_MINUTEN = 200  # Aantal belminuten in je bundel
ONBEPERKT = False  # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))

if not ONBEPERKT and (aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB):
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand, gebruik je mobiel lekker verder!")

# opdracht 7
 