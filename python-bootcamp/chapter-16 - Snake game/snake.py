from turtle import Turtle
import time
class Snake:
    def __init__(self):
        self.direction = 'd'
        self.parts = []
        self.newBodyPart(0, 0)
        for i in range(2):
            self.move(True)

    def move(self, grow: bool = False):
        length = len(self.parts)
        lastX = self.parts[len(self.parts) - 1].xcor()
        lastY = self.parts[len(self.parts) - 1].ycor()
        index = len(self.parts) - 1
        while index > 0:
            self.parts[index].setx(self.parts[index - 1].xcor())
            self.parts[index].sety(self.parts[index - 1].ycor())
            index -= 1

        head = self.parts[0]
        x = head.xcor()
        y = head.ycor()
        if self.direction == 'd':
            head.goto(x + 20, y)
        elif self.direction == 'a':
            head.goto(x - 20, y)
        elif self.direction == 'w':
            head.goto(x, y + 20)
        elif self.direction == 's':
            head.goto(x, y - 20)
        if grow:
            self.newBodyPart(lastX, lastY)

    def newBodyPart(self, x, y):
        t = Turtle()
        t.penup()
        t.color('white')
        t.shape('square')
        t.setx(x)
        t.sety(y)
        self.parts.append(t)

    def setDirection(self, direction: str):
        print(f'direction is {direction}')
        self.direction = direction[0].lower()

    def right(self):
        if 'a' != self.direction:
            self.setDirection('d')

    def left(self):
        if 'd' != self.direction:
            self.setDirection('a')

    def up(self):
        if 's' != self.direction:
            self.setDirection('w')

    def down(self):
        if 'w' != self.direction:
            self.setDirection('s')

    def snakeIsAlive(self) -> bool:
        head = self.parts[0]
        if head.xcor() > 280 or head.xcor() < - 300 or head.ycor() > 300 or head.ycor() < - 280:
            return False

        for index in range(1, len(self.parts)):
            part = self.parts[index]
            if head.xcor() == part.xcor() and head.ycor() == part.ycor():
                return False

        return True
