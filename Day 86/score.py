from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setup()

    def setup(self):
        self.goto(100, 255)
        try:
            with open('Highscore.txt', mode='r') as score_file:
                high_score = score_file.read()
                self.write('Score: {}  High Score: {}'.format(self.score, high_score), align='center', font=FONT)
        except FileNotFoundError:
            with open('Highscore.txt', mode='w') as file:
                file.write('0')
            with open('Highscore.txt', mode='r') as score_file:
                high_score = score_file.read()
                self.write('Score: {}  High Score: {}'.format(self.score, high_score), align='center', font=FONT)

    def point(self):
        self.score += 5
        self.clear()
        self.setup()
