# opdracht 1
def som(parameter1, parameter2):
    return parameter1 + parameter2

# opdracht 2
def vermenigvuldig(parameter1, parameter2):
    return parameter1 * parameter2

#opdracht 3
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")

def get_string(prompt):
    return input(prompt)

def get_letter(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.upper()
        else:
            print("Ongeldige invoer. Voer één letter in.")