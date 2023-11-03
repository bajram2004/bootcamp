# opdracht 1
for i in range(1, 26):
    print(i)

# opdracht 2
for _ in range(20):
    print("Ik ben hard op weg developer te worden!")

# opdracht 3
total = 625
divisor = 25
count = 0
while total >= divisor:
    total -= divisor
    count += 1
print(count)

#opdracht 4
total = 625
divisor = 12
count = 0
while total >= divisor:
    total -= divisor
    count += 1
print(count)

# opdracht 5
initial_balance = 10000
annual_interest_rate = 2.8 / 100
years = 5
final_balance = initial_balance * (1 + annual_interest_rate) ** years
print(f"Na {years} jaar heb je {final_balance:.2f} euro.")
years = 15
final_balance = initial_balance * (1 + annual_interest_rate) ** years
print(f"Na {years} jaar heb je {final_balance:.2f} euro.")
