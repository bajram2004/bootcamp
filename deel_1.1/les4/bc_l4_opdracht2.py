a = float(input("Voer een nieuwe waarde in voor a: "))
b = float(input("Voer een nieuwe waarde in voor b: "))


if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print("Variabele a en b zijn gelijk.")