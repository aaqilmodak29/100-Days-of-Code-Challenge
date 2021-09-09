from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.set_level()
        self.hideturtle()

    def set_level(self):
        self.penup()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.set_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))
