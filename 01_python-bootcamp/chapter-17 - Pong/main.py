from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from header import Header

h = Header()
s = Screen()
s.setup(height=600, width=1200)
s.tracer(0)
s.bgcolor('black')
s.title(h.getHeader())
left = Paddle(-560, 0, s)
right = Paddle(560, 0, s)
s.listen()
s.onkey(left.moveUp, 'w')
s.onkey(left.moveUp, 'W')
s.onkey(left.moveDown, 's')
s.onkey(left.moveDown, 'S')

s.onkey(right.moveUp, 'Up')
s.onkey(right.moveDown, 'Down')

b = Ball()
while True:
    bounce = left.intersects(b) or right.intersects(b)
    time.sleep(0.05)
    b.move(bounce)

    if b.ball.xcor() > 600:
        h.score('left')
        s.title(h.getHeader())
        b.reset()
        s.update()
        time.sleep(1)
    if b.ball.xcor() < -600:
        h.score('right')
        s.title(h.getHeader())
        b.reset()
        s.update()
        time.sleep(1)


    s.update()
s.exitonclick()