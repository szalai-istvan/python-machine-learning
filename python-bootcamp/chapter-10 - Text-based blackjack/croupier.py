def getPoints(cards: list):
    n = 0
    for card in cards:
        if card.isnumeric():
            n += int(card)
        else:
            n += 10
    return n

def getOpponentsSecretCards(opponentsCards):
    secret = []
    secret.append(opponentsCards[0])
    for i in range(1, len(opponentsCards)):
        secret.append('_')
    return secret

def printGameStateAndDecideIfWereGoingOn(yourCards, opponentsCards, playerWantsToContinue):
    yourPoints = getPoints(yourCards)
    opponentsPoints = getPoints(opponentsCards)
    print(f'Your cards:        {yourCards}')
    gameGoesOn = playerWantsToContinue and yourPoints <= 21 and opponentsPoints <= 21
    if gameGoesOn:
        print(f'Opponent\'s cards: {getOpponentsSecretCards(opponentsCards)}')
    else:
        print(f'Opponent\'s cards: {opponentsCards}')

    print(f'Your score is:    {yourPoints} ')
    if not gameGoesOn:
        print(f'Opponent\'s score: {opponentsPoints}')
    if yourPoints > 21 and opponentsPoints <= 21:
        print('You lost!')
        return False
    elif yourPoints <= 21 and opponentsPoints > 21:
        print('You win!')
        return False
    elif yourPoints > 21 and opponentsPoints > 21:
        print('It\'s a tie!')
        return False
    elif not playerWantsToContinue:
        if yourPoints > opponentsPoints:
            print('You win!')
            return False
        elif yourPoints < opponentsPoints:
            print('You lose!')
            return False
        elif yourPoints == opponentsPoints:
            print('It\'s a tie!')
            return False

    return True
