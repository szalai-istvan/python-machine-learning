import responder
print("""
  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \\
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|
 """)

difficulty = ''
while not ['easy', 'hard'].__contains__(difficulty.lower()):
    difficulty = input('Type easy for easy difficulty, hard for hard difficulty: ')
guesses = {
    'easy': 10,
    'hard': 5
}[difficulty.lower()]

guess = ''
while responder.checkGuess(guess) and guesses > 0:
    guess = input('Guess a number: ')
    if guess.isnumeric():
        guess = int(guess)
        guesses -= 1
        print(f'You can guess {guesses} more time{"s" if guesses > 1 else ""}')
    else:
        print(f'{guess} is not a valid guess. Try again!')
        print(f'You can guess {guesses} more time{"s" if guesses > 1 else ""}')
        guess = ''

if guesses <= 0:
    print('Better luck next time!')