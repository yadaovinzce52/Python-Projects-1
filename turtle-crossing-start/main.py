import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle crossing game')
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(key='w', fun=player.move)
screen.onkey(key='Up', fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.make_car()
    cars.move_forward()