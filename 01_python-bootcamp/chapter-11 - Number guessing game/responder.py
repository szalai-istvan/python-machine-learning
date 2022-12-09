import random

correctNumber = random.randint(0, 100)

def checkGuess(guess):
    if guess == '':
        return True

    if guess > correctNumber:
        print('Too high!')
        return True
    elif guess < correctNumber:
        print('Too low!')
        return True
    elif guess == correctNumber:
        print('You guessed right!')
        return False