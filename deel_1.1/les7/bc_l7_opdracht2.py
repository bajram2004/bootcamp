leeftijd = int(input('hoe oud ben je '))
snor = input('heb je een snor [j of n] ')
diploma = input ('heb je een diploma [j of n] ')

if (leeftijd >= 18 and snor == 'j') or (leeftijd < 18 and diploma == 'j'):
    print("Je bent aangenomen.")
else:
    print("Je bent niet aangenomen.")
