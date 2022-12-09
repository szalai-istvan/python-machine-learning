from turtle import Turtle
import random
class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape('circle')
        self.food.color('blue')
        self.food.penup()
        self.refreshPosition()

    def refreshPosition(self):
        self.food.goto(
            20 * random.randint(-13, 13),
            20 * random.randint(-13, 13)
        )

    def snakeFoundIt(self, headX, headY):
        return abs(self.food.xcor() - headX) <= 10 and abs(self.food.ycor() - headY) <= 10