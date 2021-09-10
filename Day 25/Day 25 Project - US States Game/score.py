from turtle import Screen

TOTAL_SCORE = 50


class Scoreboard:
    def __init__(self):
        self.screen = Screen()
        self.score = 0
        self.setup_scoreboard()

    def setup_scoreboard(self):
        self.guess = self.screen.textinput(title=f"Guess the States: {self.score}/{TOTAL_SCORE}", prompt="Guess a State")
        self.answer = self.guess.title()

    def increase_score(self):
        self.score += 1
        self.setup_scoreboard()

    def decrease_score(self):
        self.score -= 1
        self.setup_scoreboard()
