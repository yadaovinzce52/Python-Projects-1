from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-260, 260)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move_forward(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def faster(self):
        self.car_speed += MOVE_INCREMENT