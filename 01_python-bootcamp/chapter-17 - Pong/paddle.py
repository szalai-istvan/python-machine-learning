from turtle import Turtle, Screen
from ball import Ball
class Paddle:
    def __init__(self, x: int, y: int, screen):
        self.screen = screen
        self.parts = []
        for i in range(-2, 2):
            t = Turtle()
            t.penup()
            t.shape('square')
            t.color('white')
            t.goto(x, y + i * 20)
            self.parts.append(t)
        self.screen.update()

    def moveUp(self):
        for p in self.parts:
            p.goto(p.xcor(), p.ycor() + 40)
        self.screen.update()

    def moveDown(self):
        for p in self.parts:
            p.goto(p.xcor(), p.ycor() - 40)
        self.screen.update()

    def intersects(self, ball: Ball) -> bool:
        ballX = ball.ball.xcor()
        ballY = ball.ball.ycor()
        if abs(ballX - self.parts[0].xcor()) > 20:
            return False
        for part in self.parts:
           if abs(ballY - part.ycor()) < 20:
               return True

        return False