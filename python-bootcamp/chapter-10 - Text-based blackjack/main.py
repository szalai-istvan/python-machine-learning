# Black jack

import cardDealer
import croupier
import os

cardDealer.generateDeck()
yourCards = []
opponentsCards = []
yourCards.append(cardDealer.giveRandomCard())
yourCards.append(cardDealer.giveRandomCard())
opponentsCards.append(cardDealer.giveRandomCard())
opponentsCards.append(cardDealer.giveRandomCard())
os.system('clear')
playerWantsToGoOn = True
while croupier.printGameStateAndDecideIfWereGoingOn(yourCards, opponentsCards, playerWantsToGoOn):
    answer = ''
    while not ['n', 'N', 'y', 'Y'].__contains__(answer):
        answer = input('Do you want another card? [y/n]: ')
        playerWantsToGoOn = ['y', 'Y'].__contains__(answer)

    if playerWantsToGoOn:
        yourCards.append(cardDealer.giveRandomCard())
        opponentsCards.append(cardDealer.giveRandomCard())

    os.system('clear')