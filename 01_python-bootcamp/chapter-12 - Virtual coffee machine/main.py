import coffeeTypes

print("""
 __                                _  _      
/__ _ _|_    _  _ __  _     _  _ _|__|_ _  _ 
\_|(/_ |_   _> (_)|||(/_   (_ (_) |  | (/_(/_""")

print('Welcome to the break room and the coffee machine. ')
print('Fill up on some caffeine. You will need it! ')
print('--------------------')
print('Choose from these options: ')
for coffee in coffeeTypes.coffees:
    print(f' - {coffee} {coffeeTypes.getCoffeePrice(coffee)}')

choice = ''
while not coffeeTypes.coffees.__contains__(choice.lower()):
    choice = input('Your choice today is: ')
    if not coffeeTypes.coffees.__contains__(choice.lower()):
        print(f'Sorry chief, we cannot serve you {choice}. Try again!')

print(f'Great choice! {choice.title()} is one of my favorite!')
coffeeTypes.printCoffeeDetails(choice)
print('')
print(f'Please insert {coffeeTypes.getCoffeePrice(choice)}')

price = coffeeTypes.coffees[choice.lower()]['price']
moneyAdded = 0
print('Input a number to insert a coin. Type quit to stop the coffee making')
while moneyAdded < price:
    money = input('> ')
    if money.replace('.', '').isnumeric():
        moneyAdded += float(money)
    elif money.lower() == 'quit':
        print('Your choice. Have a good one!')
        break

print(f'That seems quite enough. Your change is €{round((moneyAdded - price), 2)}')
print('Enjoy!')