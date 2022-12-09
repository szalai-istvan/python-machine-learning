from turtle import Turtle, Screen
import random
class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.color('white')
        self.ball.shape('circle')
        self.ball.goto(0, 0)
        self.speed = (10, 10)

    def bounceX(self):
        self.speed = (- self.speed[0] + random.randint(-5, 5), self.speed[1])
        self.speed = (self.speed[0] * 1.1, self.speed[1] * 1.1)

    def bounceY(self):
        self.speed = (self.speed[0], - self.speed[1] + random.randint(-5, 5))
        self.speed = (self.speed[0] * 1.1, self.speed[1] * 1.1)

    def move(self, bounceX: bool = False):
        if (self.ball.ycor() > 280 and self.speed[1] > 0) or \
                (self.ball.ycor() < -300 and self.speed[1] < 0):
            self.bounceY()

        if bounceX:
            self.bounceX()

        self.ball.setx(self.ball.xcor() + self.speed[0])
        self.ball.sety(self.ball.ycor() + self.speed[1])

    def reset(self):
        self.ball.goto(0, 0)
        x = random.randint(1, 10)
        reverse = random.random() > 0.5
        self.speed = (-x if reverse else x, 10 - x)