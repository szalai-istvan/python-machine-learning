# Password generator
import random

def getRandomSmallerCaseLetter():
    a = ord('a')
    a += random.randint(0, 25)
    return chr(a)

def getRandomUpperCaseLetter():
    a = ord('A')
    a += random.randint(0, 25)
    return chr(a)

def getRandomDigit():
    a = ord('0')
    a += random.randint(0, 9)
    return chr(a)

def getRandomCharacter():
    function = [getRandomSmallerCaseLetter, getRandomUpperCaseLetter, getRandomDigit][random.randint(0, 2)]
    randomCharacter = function()
    return randomCharacter

length = int(input('What length of password should we make? '))
password = ''
for x in range(0, length):
    password = password + getRandomCharacter()

print(f'Your new password is {password}')