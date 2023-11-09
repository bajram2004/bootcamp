# Opdracht 1
getallen_lijst = []
for _ in range(5):
    getal = int(input("Voer een getal in: "))
    getallen_lijst.append(getal)

print("De lijst met getallen is:", getallen_lijst)

# Opdracht 2
getallen_lijst = [1, 2, 3, 4, 5]

index = int(input("Voer een index in: "))
verwijderd_getal = getallen_lijst.pop(index)

print("Verwijderd getal:", verwijderd_getal)
print("Bijgewerkte lijst:", getallen_lijst)

# Opdracht 3
fruit_lijst = ["appel", "banaan", "peer", "kiwi", "druif"]

fruit_soort = input("Voer een fruitsoort in: ")
fruit_lijst.remove(fruit_soort)

print("Bijgewerkte lijst:", fruit_lijst)

# Opdracht 4
woorden_lijst = []
for _ in range(5):
    woord = input("Voer een woord in: ")
    woorden_lijst.append(woord)

for woord in woorden_lijst:
    print(woord)

    # Opdracht 5
namen_lijst = ["Alice", "Bob", "Charlie", "David", "Emma"]

naam = input("Voer een naam in: ")

if naam in namen_lijst:
    namen_lijst.remove(naam)
else:
    namen_lijst.append(naam)

print("Bijgewerkte lijst:", namen_lijst)
