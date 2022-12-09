# Bill calculator
bill = float(input('How much was the bill? $'))
people = int(input('How many people are splitting the bill? '))
tip = float(input('Input tip percentage: %'))
payPerCapita = round(bill * (1 + tip / 100) / people, 2)
print(f'Everyone should pay ${payPerCapita}')