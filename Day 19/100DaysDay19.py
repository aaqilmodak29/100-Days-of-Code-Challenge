# # Higher Order Functions
# # Functions that call other functions as parameters
# # Eg:
# def add(n1, n2):
#     return n1 + n2
#
#
# def calculator(n1, n2, func):
#     return func(n1, n2)
#
#
# result = calculator(5, 2, add)
# print(result)


# Making an Etch a Sketch
from movement import *
screen = Screen()

screen.listen()
# Alternative syntax - screen.onkey(move_forward, "w")
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
