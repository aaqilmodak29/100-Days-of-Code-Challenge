# from turtle import everything
import turtle
from turtle import *
import random

# # aliasing modules
# import turtle as t
# tim = t.Turtle()


# # installing modules
# # pycharm gives prompt if said module is not installed
# import heroes
# print(heroes.gen())


# colors = ["steel blue", "red", "green", "yellow", "orange", "purple", "brown", "pink", "medium slate blue",
#           "light slate blue"]


tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


tim.color(random_color())
tim.pencolor(random_color())
tim.speed("fastest")
# tim.pensize(10)


# # Drawing Square
# for i in range(4):
#     tim.left(90)
#     tim.forward(100)


# # Drawing Dashed Line
# for i in range(10):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()


# # Drawing Multiple Shapes
# sides = 3
# while sides <= 10:
#     for i in range(sides):
#         # tim.pencolor(random.choice(colors)) - every side will have a different color
#         tim.left(360/sides)
#         tim.fd(100)
#     sides += 1
#     tim.pencolor(random.choice(colors))


# # Tuples - similar to lists, but unlike lists, their values cannot be changed
# my_tuple = (1, 2, 3)
# print(my_tuple[0])
# # you can change tuple to list if you want to change its values
# my_list = list(my_tuple)
# print(my_list)


# # Drawing A Random Walk
# # An elementary example of a random walk is the random walk on the integer number line,
# # which starts at 0 and at each step moves +1 or −1 with equal probability.
# # east, north, west, south
# heading_to = [0.0, 90.0, 180.0, 270.0]
# for i in range(200):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(heading_to))
#     tim.fd(20)


# Drawing a Spirograph
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
