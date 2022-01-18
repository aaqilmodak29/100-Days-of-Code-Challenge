from turtle import Turtle


class Player(Turtle):
    def __init__(self, set_cords):
        super().__init__()
        self.shape("square")
        self.color('purple')
        self.create_player(set_cords)

    def create_player(self, cords):
        self.penup()
        self.goto(cords)
        self.turtlesize(0.5, 5)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


