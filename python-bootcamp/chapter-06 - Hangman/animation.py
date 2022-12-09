import builtins

bodyParts = ['O', '|', '\\', '/', '|', '\\', '/']
def getBodyPart(mistakes, bodyPartNumber):
    if mistakes <= bodyPartNumber:
        return ' '
    return bodyParts[bodyPartNumber]

def printHangMan(mistakes):
    lines = [
        f'  -------|',
        f'  |      |',
        f'  {getBodyPart(mistakes, 0)}      |',
        f' {getBodyPart(mistakes, 2)}{getBodyPart(mistakes, 1)}{getBodyPart(mistakes, 3)}     |',
        f'  {getBodyPart(mistakes, 4)}      |',
        f' {getBodyPart(mistakes, 6)} {getBodyPart(mistakes, 5)}     |',
        f'         |',
        f'----------',
    ]
    for line in lines:
        print(line)

    if mistakes >= 7:
        print('GAME OVER!')
    else:
        print('')


def printWordForHangman(word: str, guessedChars: list):
    puzzleIsNotDone = False
    line = ''
    for char in word:
        if guessedChars.__contains__(char.upper()) or guessedChars.__contains__(char.lower()):
            line = line + char.upper()
        else:
            line = line + '_'
            puzzleIsNotDone = True
        line = line + ' '
    print(line)
    if not puzzleIsNotDone:
        print('GOOD JOB!')
    return puzzleIsNotDone

def printGameState(word, guessedChars, mistakes):
    printHangMan(mistakes)
    return printWordForHangman(word, guessedChars) and mistakes < 7