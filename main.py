# Get 30 RGB color codes from an image and using those color codes to create a hirst painting with 100 dots

import colorgram
from turtle import Screen, Turtle
import turtle as t
import random

turtle = Turtle()
t.colormode(255)

colors = colorgram.extract('hirst.jpg', 30)

colors_arr = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_arr.append((r, g, b))

turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.setheading(225)
turtle.fd(300)
turtle.setheading(0)


dots = 100

for dot in range(1, dots + 1):
    turtle.dot(20, random.choice(colors_arr))
    turtle.fd(50)
    if dot % 10 == 0:
        turtle.setheading(90)
        turtle.fd(50)
        turtle.setheading(180)
        turtle.fd(500)
        turtle.setheading(0)


screen = Screen()
screen.exitonclick()
