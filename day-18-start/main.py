from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.fillcolor("blue")
colormode(255)

def draw(loop, angle):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(loop):
        tim.right(angle)
        tim.forward(100)


for sides in range(3, 11):
    draw(sides, (360 / sides))

screen = Screen()
screen.exitonclick()
