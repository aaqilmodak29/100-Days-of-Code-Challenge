from level import Turtle
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.create_player()

    def create_player(self):
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(STARTING_POSITION)
