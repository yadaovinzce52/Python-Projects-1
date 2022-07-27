from turtle import Turtle, Screen, colormode
from random import randint

t = Turtle()
colormode(255)
t.speed("fastest")

gap = 12
for _ in range(int(360/gap)):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.circle(100)
    t.setheading(t.heading() + gap)


Screen().exitonclick()