from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self, set_cords):
        super().__init__()
        self.shape("square")
        # self.set_table()
        self.create_player(set_cords)

    # def set_table(self):
    #     super().__init__()
    #     self.shape("square")
    #     self.color("white")
    #     self.turtlesize(15, 0.5)

    def create_player(self, cords):
        self.penup()
        self.goto(cords)
        self.color("white")
        self.turtlesize(5, 1)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
