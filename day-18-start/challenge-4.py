from turtle import Turtle, Screen, colormode
from random import choice, randint

t = Turtle()
t.speed("fastest")

directions = [0, 90, 180, 270]

thickness = 10
for _ in range(50):
    t.pensize(thickness)
    colormode(255)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.setheading(choice(directions))
    t.forward(20)
    t.pensize(thickness+1)

Screen().exitonclick()
