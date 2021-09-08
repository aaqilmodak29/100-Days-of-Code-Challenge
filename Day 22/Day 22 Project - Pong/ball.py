from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("steel blue")
        self.turtlesize(0.5, 0.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_y(self):
        self.y_move *= -1

    def bounce_ball_x(self):
        self.x_move *= -1
        self.x_move *= 0.9

    def reset(self):
        self.home()
        self.bounce_ball_x()
        self.move_speed = 0.1
        self.speed("slowest")

