# Rock, Paper, Scissors

import random
import animations
import winner

choices = ['Rock', 'Paper', 'Scissors']
for x in range(0, len(choices)):
    print(f'[{x}] {choices[x]}')

yourChoice = int(input('Your choice is: '))
animations.printRPS(yourChoice)
computersChoice = random.randint(0, 2)

print(f'{choices[yourChoice]} vs. {choices[computersChoice]}')

animations.printRPS(computersChoice)
winner.printWinner(yourChoice, computersChoice)