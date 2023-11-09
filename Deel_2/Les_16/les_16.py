def get_integer():
    while True:
        try:
            value = int(input("Voer een geheel getal in: "))
            return value
        except ValueError:
            print("Oeps! Dat is geen geldig geheel getal. Probeer het opnieuw.")

def get_float():
    while True:
        try:
            value = float(input("Voer een decimaal getal in: "))
            return value
        except ValueError:
            print("Oeps! Dat is geen geldig decimaal getal. Probeer het opnieuw.")

integer_result = get_integer()
print("Ingevoerd geheel getal:", integer_result)

float_result = get_float()
print("Ingevoerd decimaal getal:", float_result)