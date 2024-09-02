fruit_lijst = ['appel', 'banaan', 'kers', 'druif', 'sinaasappel']

index = int(input("Voer een index in om een stuk fruit te verwijderen (0-4): "))

if 0 <= index < len(fruit_lijst):

    verwijderd_fruit = fruit_lijst.pop(index)

    print(f"Verwijderd fruit: {verwijderd_fruit}")

    print("Bijgewerkte lijst van fruit:", fruit_lijst)
else:
    print("Ongeldige index. Kies een getal tussen 0 en 4.")
