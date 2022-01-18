import time
from turtle import *
from player import Player
from blocks import Blocks
from ball import Ball
from score import Scoreboard, FONT
from lives import Lives

SPEED = 0.11

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Breakout Game')
screen.tracer(0)

player = Player((0, -270))
blocks = Blocks()
ball = Ball()
life = Lives()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


while life.lives > 0 and len(blocks.all_blocks) > 0:
    time.sleep(SPEED)
    screen.update()
    ball.move_ball()

    # Collision with walls
    if ball.ycor() > 280:
        ball.bounce_ball_yaxis()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_ball_xaxis()

    # Reset Ball
    if ball.ycor() < -290:
        ball.reset_ball()
        life.reduce_life()

    # Collision with player
    if ball.distance(player) < 30:
        ball.bounce_ball_yaxis()

    # Collision with blocks
    for i in range(len(blocks.all_blocks) - 1):
        if ball.distance(blocks.all_blocks[i]) < 40:
            blocks.all_blocks[i].hideturtle()
            blocks.all_blocks.remove(blocks.all_blocks[i])
            ball.bounce_ball_yaxis()
            if SPEED > 0.01:
                SPEED -= 0.01
            else:
                SPEED = 0.01
            scoreboard.point()
scoreboard.clear()
scoreboard.goto(0, -90)

with open('Highscore.txt', mode='r') as file:
    best_score = int(file.read())
    # print(scoreboard.score)
    # print(best_score)
    if scoreboard.score > best_score:
        with open('Highscore.txt', mode='w') as rewrite_file:
            rewrite_file.write(str(scoreboard.score))
        with open('Highscore.txt', mode='r') as read_file:
            score = read_file.read()
            scoreboard.write(
                'GAME OVER\n'
                ' Score: {}\n'
                ' High Score: {}\n'.format(scoreboard.score, score),
                align='center',
                font=FONT
            )
    else:
        with open('Highscore.txt', mode='r') as new_file:
            high_score = new_file.read()
        scoreboard.write(
            'GAME OVER\n'
            ' Score: {}\n'
            ' High Score: {}\n'.format(scoreboard.score, high_score),
            align='center',
            font=FONT
        )

screen.exitonclick()
