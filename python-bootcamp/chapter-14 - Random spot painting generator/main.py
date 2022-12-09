from turtle import Turtle, Screen
from randomColor import randomColor
import math

t = Turtle()
t.shape('turtle')

screen = Screen()
screen.bgcolor()
screen.title('Painting')

height = screen.canvheight
width = screen.canvwidth
min = width if width < height else height
screen.canvwidth = min
screen.canvheight = min

circles = 11
step = (width if width < height else height) // (circles + 1) * 2.1
t.speed(1000)
for x in range(circles):
    for y in range(circles):
        t.penup()
        t.setx( -5.5 * step + x * step)
        t.sety( -5.5 * step + y * step + step // 2)

        t.pendown()
        colorRGB = randomColor()
        t.dot(2 * step // 3, colorRGB[0], colorRGB[1], colorRGB[2])

t.penup()
t.setx(1000)
t.sety(1000)
screen.exitonclick()