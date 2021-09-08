# # Object Oriented Programming.
# from turtle import Turtle, Screen
# import another_module
#
# print(another_module.var)
# timmy = Turtle()
# print(timmy)
# # object will be in the shape of a turtle - calling method shape() using object timmy.
# timmy.shape("turtle")
# # changing color of object using method color() and passing the color as a string.
# timmy.color("red")
# # moving object forward using method forward() or fd() and passing the spaces we want it to move as a float.
# timmy.fd(100)
#
# my_screen = Screen()
# # syntax - obj.attribute
# # prints height of the canvas.
# # functions tied to an object are called methods.
# print(my_screen.canvheight)
# # syntax - obj.method
# # allows program to continue running until we click on the screen.
# my_screen.exitonclick()


# PyPi - Python Package Index
# PrettyTable
# importing class PrettyTable from PrettyTable package
from prettytable import PrettyTable
# creating object table
table = PrettyTable()
# adding column using method add_column that accepts column name and the data the column will contain as a list
table.add_column("Pokemon", ["Pichu", "Pikachu", "Raichu"])
table.add_column("Type", ["Electric", "Electric", "Electric"])
print(table)
# changing alignment of table to "left" by tapping into the attribute "align"
table.align = "l"
print(table)
