from random import randint

totale_score = 0

for ronde in range(1, 4):
    te_raden = randint(1, 5)
    aantal_gokken = 0
    goed_geraden = False

    print(f"Ronde {ronde}:")
    
    while not goed_geraden:
        gok = int(input('Kies een getal van 1 t/m 5: '))
        aantal_gokken += 1
        
        if te_raden == gok:
            print("Je hebt het getal goed geraden!")
            goed_geraden = True
        else:
            print("Je hebt het getal niet goed geraden. Probeer opnieuw!")
    
    score = 20 - (aantal_gokken - 1)
    totale_score += score
    print(f"Je score voor ronde {ronde} is: {score}")

print(f"Je totale score na 3 rondes is: {totale_score}")
