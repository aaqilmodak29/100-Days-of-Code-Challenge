from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('steelblue')
        self.turtlesize(0.5, 0.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_yaxis(self):
        self.y_move *= -1

    def bounce_ball_xaxis(self):
        self.x_move *= -1

    def reset_ball(self):
        self.home()

