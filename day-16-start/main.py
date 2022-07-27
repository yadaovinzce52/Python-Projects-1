# from turtle import *
#
# timmy = Turtle()
# timmy.shape("square")
# timmy.color("blueViolet")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "fire"])
table.align = "l"

print(table.align)
print(table)