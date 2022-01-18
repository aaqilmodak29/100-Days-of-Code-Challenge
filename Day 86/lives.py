from turtle import Turtle

FONT = ("Courier", 25, "normal")


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.set_lives()

    def set_lives(self):
        self.goto(-310, 255)
        self.write('Lives: {}'.format(self.lives), align='center', font=FONT)

    def reduce_life(self):
        self.clear()
        self.lives -= 1
        self.set_lives()



