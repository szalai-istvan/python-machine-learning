def printWinner(yourChoice, computersChoice):
    print('--------------------')
    if yourChoice == computersChoice + 1 or yourChoice == computersChoice - 2:
        print('|     You won!     |')
    elif computersChoice == yourChoice + 1 or computersChoice == yourChoice - 2:
        print('|  Computer won!   |')
    else:
        print('|   It\'s a tie!    |')

    print('--------------------')