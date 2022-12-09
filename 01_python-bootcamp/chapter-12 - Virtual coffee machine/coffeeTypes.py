def createCoffeeIngredientList(water, milk, sugar, price):
    return {
        'water': water,
        'milk': milk,
        'sugar': sugar,
        'price': price
    }

coffees = {
    'espresso': createCoffeeIngredientList(50, 10, 1, 1.2),
    'cappuccino': createCoffeeIngredientList(150, 50, 2, 1.5),
    'americano': createCoffeeIngredientList(300, 100, 4, 1.8),
    'latte': createCoffeeIngredientList(50, 200, 2, 2.5),
}

def printCoffeeDetails(coffee:str):
    if not coffees.__contains__(coffee.lower()):
        print(f'Unknown coffee type: {coffee}')
        return
    ingredients = coffees[coffee.lower()]
    print(coffee.title().center(20, ' '))
    print('--------------------')
    print(f'Water: {ingredients["water"]} ml')
    print(f'Milk:  {ingredients["milk"]} ml')
    print(f'Sugar: {ingredients["sugar"]} spoons')

def getCoffeePrice(coffee):
    return '€' + str(coffees[coffee.lower()]['price'])