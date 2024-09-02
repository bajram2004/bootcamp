getallen = []

for i in range(5):
    getal = int(input(f"Voer getal {i + 1} in: "))
    getallen.append(getal)

getallen.sort()

print("De gesorteerde lijst is:", getallen)
