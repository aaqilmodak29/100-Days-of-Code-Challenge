from turtle import *
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

player_1 = Player((350, 0))
player_2 = Player((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")
screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Collision with player
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()

    # Detect if right player missed
    if ball.xcor() > 360:
        ball.reset()
        scoreboard.l_point()

    # Detect if left player missed
    if ball.xcor() < -360:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
