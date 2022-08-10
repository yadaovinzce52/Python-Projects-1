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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='w', fun=player.move)
screen.onkey(key='Up', fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Consistently create cars throughout life cycle of the game
    cars.make_car()
    cars.move_forward()

    # collision with any of the cars
    for car in cars.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Once turtle reaches other side, reset and speed up cars
    if player.is_at_finish_line():
        player.go_to_start()
        cars.faster()
        scoreboard.next_level()

screen.exitonclick()