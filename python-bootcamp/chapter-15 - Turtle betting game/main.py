from turtle import Turtle, Screen
import random
# Turtles
colors = ['red', 'orange', 'green', 'blue', 'violet', 'black']

# Placing the bet
print('The turtles in the race are: ')
for c in colors:
    print(f' - {c.title()}')

print('--------')
bet = ''
while not bet.lower() in colors:
    bet = input('Place a bet: ').lower()

print(f'Your bet is {bet}')

# Initign racing turtles
turtles = []
s = Screen()
width = 500
height = 500
s.setup(width=width, height=height)
for i in range(len(colors)):
    t = Turtle()
    t.shape('turtle')
    t.color(colors[i])
    turtles.append(t)
    t.penup()
    t.goto(- width / 2.5, (height / 3) - i * ((2 * height / 3) / 5))

# The race
def getWinner():
    for t in turtles:
        if t.xcor() > width / 3:
            color = str(t.color()).lower()
            endIndex = color.index('\'', 2, len(color))
            return color[2 : endIndex]
    return None

while getWinner() is None:
    for t in turtles:
        t.forward(random.randint(0, 10))

print(f'Winner is {getWinner()}')
print(f'{"you win" if getWinner() == bet else "You lose"}')
s.exitonclick()