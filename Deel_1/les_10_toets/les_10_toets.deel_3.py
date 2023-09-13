#opdracht 5


from time import sleep

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

aantal_meldingen = 5

for _ in range(aantal_meldingen):
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(1)

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))