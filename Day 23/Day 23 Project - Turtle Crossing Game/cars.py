import turtle
from turtle import Turtle
import random

MOVE_DISTANCE = 10
MOVE_SPEEDUP = 5


def random_color():
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random_color())
            x_pos = random.randint(260, 260)
            y_pos = random.randint(-250, 250)
            new_car.goto(x_pos, y_pos)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_SPEEDUP
