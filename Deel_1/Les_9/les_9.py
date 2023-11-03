# opdracht 1
a = 5
b = 3
c = 2
if (a == 6 and b == 4 or c == 2):
    print("De conditie is waar")
else:
    print("De conditie is niet waar")

a = 5
b = 3
c = 2
if (a == 6 and (b == 4 or c == 2)):
    print("De conditie is waar")
else:
    print("De conditie is niet waar")

# opdracht 2
getal = int(input("Voer een getal in: "))

if getal % 7 == 0 and getal % 11 == 0:
    print("Dit getal is zonder rest deelbaar door 7 en 11")
else:
    print("Dit getal is niet zonder rest deelbaar door 7 en 11")

# opdracht 3
leeftijd = 18
snor = 'j'  # 'j' staat voor ja, 'n' staat voor nee
diploma = 'j'

if (leeftijd >= 18 and snor == 'j') or (leeftijd < 18 and diploma == 'j'):
    print("Je bent aangenomen.")
else:
    print("Je bent niet aangenomen.")
