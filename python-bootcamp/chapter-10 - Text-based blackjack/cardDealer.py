import random

figures = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []
def generateDeck():
    global deck
    deck = []
    for i in range(0, 4):
        for f in figures:
            deck.append(f)

def giveRandomCard():
    card = random.choice(deck)
    deck.remove(card)
    return card