# # Retrieving Color from an Image
# import colorgram
# note - colorgram not on replit
# list_of_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for i in range(30):
#     color = colors[i]  # retrieves color from colors
#     rgb = color.rgb  # e.g. (255, 151, 210)
#     red = rgb.r  # e.g. 255
#     green = rgb.g  # e.g. 151
#     blue = rgb.b  # e.g. 210
#     list_of_colors.append((red, green, blue))  # appending colors as tuple to a list
#     i += 1
# print(list_of_colors)
import turtle
import random
from turtle import *

list_of_colors = [
    (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157),
    (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
    (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
    (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)
]


def random_color():
    color_tuple = random.choice(list_of_colors)
    return color_tuple


tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.setposition(-400, -300)
tim.hideturtle()
screen = Screen()

space = 50
for j in range(15):
    for i in range(15):
        tim.dot(20, random_color())
        tim.fd(50)
        tim.dot(20, random_color())
    tim.setposition(-400, -300)
    tim.setheading(90)
    tim.fd(space)
    tim.setheading(0)
    space += 50


screen.exitonclick()
