# Opening, Reading and Writing to Files

# # opening file
# file = open("my_file.txt")
# # reading file
# contents = file.read()
# print(contents)
# # closing file
# file.close()

# # an easier way to know when to open or close a file without specifying everytime is to use the "with" keyword
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # writing to a file, mode="w" will replace all text whereas mode="a" will append new text to existing text
# with open("my_file.txt", mode="a") as file:
#     file.write("New Text.")

# # creating new file from scratch, this will happen if the text file doesnt exist already. only works in write mode
# with open("new_file.txt", mode="w") as file:
#     file.write("New Text.")

# # using absolute file path to read a file
# with open("C:/Users/aaqil/Desktop/my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

# using relative file path to read a file
with open("../../../Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)