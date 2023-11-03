# opdracht 1
if x == 18:
    print('de waarde van x = 18')

# opdracht 2
a = 3
b = 7


if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print("Variabele a en b zijn gelijk.")


a = float(input("Voer een nieuwe waarde in voor a: "))
b = float(input("Voer een nieuwe waarde in voor b: "))


if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print("Variabele a en b zijn gelijk.")

# opdracht 3
leeftijd = 16

if leeftijd >= 16:
    print("Gefeliciteerd, je mag je brommerrijbewijs halen.")
else:
    print("Helaas, je zult nog even moeten wachten.")

# opdracht 4
#1

a = 3
b = 3
print(a == b)
#2

x = 5
y = 7
print(x != y)  
#3

p = 10
q = 8
print(p > q)
#4

m = 5
n = 5
print(m <= n)
#5

zon = True
warm = True
print(zon and warm)

#6
is_weekend = True
is_holiday = False
print(is_weekend or is_holiday)

# opdracht 5
a = float(input("Voer een waarde in voor a: "))
b = float(input("Voer een waarde in voor b: "))
c = float(input("Voer een waarde in voor c: "))

if a < b and b < c:
    print(f"a < b < c is waar, want {a} < {b} < {c}")
else:
    print("a < b < c is niet waar.")

if a < b:
    print(f"a < b is waar, want {a} < {b}")
else:
    print("a < b is niet waar.")

if b < c:
    print(f"b < c is waar, want {b} < {c}")
else:
    print("b < c is niet waar.")