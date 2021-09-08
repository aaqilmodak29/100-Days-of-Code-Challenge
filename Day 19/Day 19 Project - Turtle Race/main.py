from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
x_cord = -230
y_cord = 150
all_turtles = []
is_race_on = False
user_bank = 0

for turtle_color in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_color])
    new_turtle.goto(x=x_cord, y=y_cord)
    y_cord -= 50
    all_turtles.append(new_turtle)

user_bet_color = screen.textinput(title="Make a Bet", prompt="Which color turtle do you think will win? ")
user_bet_money = screen.textinput(title="Your Bank", prompt="How much would you like to bet (in $)? ")
user_bet_money_int = int(user_bet_money)
user_bank += user_bet_money_int
if user_bet_color:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet_color:
                print(f"You Won! The {winning_color} turtle won the race!")
                user_bet_money_int *= 2
                user_bank += user_bet_money_int
                print(f"You have ${user_bank} in your bank")
            else:
                print(f"You Lost! The {winning_color} turtle won the race!")
                user_bank -= user_bet_money_int
                print(f"You have ${user_bank} in your bank")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
screen.exitonclick()
