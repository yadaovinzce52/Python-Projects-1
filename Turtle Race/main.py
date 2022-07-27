import turtle
from random import randint

race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_pos = -100
for color in colors:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 30
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for racer in turtles:
        if racer.xcor() > 230:
            winner = racer.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You lost :(. The {winner} turtle is the winner.")
            race_on = False
        rand_distance = randint(0, 10)
        racer.forward(rand_distance)

# tim = turtle.Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-240, y=-100)

screen.exitonclick()
