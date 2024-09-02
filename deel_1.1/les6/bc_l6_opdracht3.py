kleuren_lijst = ['rood', 'blauw', 'groen', 'geel', 'paars']

naam = input("Wat is je naam? ")
favoriete_kleur = input("Wat is je favoriete kleur? ").lower()

if favoriete_kleur in kleuren_lijst:
    print(f"Hallo {naam}! Wat een mooie keuze, {favoriete_kleur} is ook een geweldige kleur.")
else:
    print("Deze kleur is niet zo geweldig!")

