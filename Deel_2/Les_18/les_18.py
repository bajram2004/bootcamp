import random

def is_guess_valid(guess, min_value, max_value):
    return min_value <= guess <= max_value

def main_game():
    min_range = 1
    max_range = 100
    target_number = random.randint(min_range, max_range)
    
    while True:
        user_input = input("Raad het nummer tussen {} en {}: ".format(min_range, max_range))
        
        try:
            guess = int(user_input)
            if is_guess_valid(guess, min_range, max_range):
                if guess < target_number:
                    print("Het te raden nummer is hoger.")
                elif guess > target_number:
                    print("Het te raden nummer is lager.")
                else:
                    print("Gefeliciteerd! Je hebt het nummer geraden!")
                    break
            else:
                print("Ongeldige gok. Probeer opnieuw binnen het opgegeven bereik.")
        except ValueError:
            print("Ongeldige invoer. Voer een geldig nummer in.")

if __name__ == "__main__":
    main_game()
