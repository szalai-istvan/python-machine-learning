from turtle import Turtle, Screen
from snake import Snake
import time
import food
import header

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
head = header.Header()
s.title(head.getHeader())
s.tracer(0)
snake = Snake()

s.listen()
s.onkey(snake.up, 'w')
s.onkey(snake.up, 'W')
s.onkey(snake.down, 's')
s.onkey(snake.down, 'S')
s.onkey(snake.left, 'a')
s.onkey(snake.left, 'A')
s.onkey(snake.right, 'd')
s.onkey(snake.right, 'D')
f = food.Food()
while snake.snakeIsAlive():
    time.sleep(0.1)
    x = snake.parts[0].xcor()
    y = snake.parts[0].ycor()
    if f.snakeFoundIt(x, y):
        snake.move(True)
        s.title(head.getHeader(True))
        f.refreshPosition()
    else:
        snake.move()
        s.title(head.getHeader())

    s.update()

s.title(head.gameOver())

s.exitonclick()