kleuren_tuple = ("rood", "blauw", "groen", "geel", "paars")
naam = input("Wat is jouw naam? ")
favoriete_kleur = input("Wat is jouw favoriete kleur? ")
if favoriete_kleur.lower() in kleuren_tuple:
    print(f"{naam}, dat is een geweldige keuze! {favoriete_kleur.capitalize()} is een mooie kleur.")
else:print("Deze kleur is niet zo geweldig!")