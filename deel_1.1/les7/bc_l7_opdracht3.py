leeftijd = int(input("hoe oud ben je? "))

heeft_geen_toegang = not (leeftijd > 18)

if heeft_geen_toegang:
    print("Helaas, je hebt geen toegang. Je moet ouder zijn dan 18 jaar.")
else:
    print("Welkom! Je hebt toegang tot het evenement.")
