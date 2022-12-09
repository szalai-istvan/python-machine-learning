# Hangman
import words
import animation
import os

word = words.getRandomWord()
guessedChars = []
mistakes = 0

while animation.printGameState(word, guessedChars, mistakes):
    guess = input('Your next guess: ')
    if not guessedChars.__contains__(guess.upper()):
        guessedChars.append(guess.upper())
        if not word.__contains__(guess):
            mistakes += 1
    if mistakes >= 7:
        print(f'Word was {word}. Better luck next time. :) ')
        break
    else:
        # Code was written on Ubuntu. For Windows:
        # os.system('cls')
        os.system('clear')

