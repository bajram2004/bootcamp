#opdracht 1

print (6*3) #18
print (15%13) #2
print (3/3) #1
print (16%3) #1
print ((6*3)*12) #216

#opdracht 2

print (6>3 or 2<3) # print: true
print (3>6 or 2<3) # print: true
print ('a'=='a' or 'b'=='a') # print: true
print (9>3 and 5>4) # print: true

#opdracht 3
print("wat is je naam")
naam = input ()
print ("hoe oud ben je")
leeftijd = int (input())

if leeftijd >=18:
    print ("Beste "+naam+", je bent nog geen 18. Alleen autorijden zit er dus niet in :-(")
else:
    print ("Beste "+naam+", je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).")

#opdracht 4

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = int (40)

if oppervlakte >= 150:
    prijs_m2 = 35
if oppervlakte >= 80:
    prijs_m2 = 38

totaal = prijs_m2 * oppervlakte