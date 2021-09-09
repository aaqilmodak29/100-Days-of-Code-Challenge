from turtle import Screen
from player import Player
from level import Level
from cars import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
level = Level()
car = Car()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if player.ycor() > 280:
        player.reset()
        level.increase_level()
        car.speed_up()

    # Detect collision with car
    for each_car in car.all_cars:
        if player.distance(each_car) < 15:
            level.game_over()
            game_is_on = False
screen.exitonclick()
