# creating classes
# syntax - class class_name:
# classes should have PascalCase
# note: camelCase
# note: snake_case
# note: ATTRIBUTES are things the object HAS and METHODS are the things the object DOES
class User:
    # # keyword pass gets rid of any indentation errors when classes/methods/loops have no code in them
    # pass
    # def __init__(self):
    #     # this is where we initialize attributes
    #     # this function will be called everytime a new object is created from this class
    #     print("creating new user...")

    def __init__(self, username, user_id):
        print("creating new user...")
        self.id = user_id
        print(f"Your ID is: {self.id}")
        self.username = username
        print(f"Your username is: {self.username}")
        # setting default value
        self.followers = 0
        self.following = 0

    # method always has "self" since it needs to know which object is calling the method
    def follow(self, user):
        self.following += 1
        user.followers += 1

# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#         print(self.seats)


# # initializing object from class
# user_1 = User()
# creating attributes for class using object initialized from said class
# # attributes are variables associated with an object
# # this method is prone to error and redundant for eg when we have multiple users
# user_1.id = "001"
# name = input("Enter name: ")
# name.__init__(name)
# print(user_1.id)
#
# user_2 = User()
# user_2.id = "002"
# name = input("Enter name: ")
# name.__init__(name)
# print(user_2.id)

# my_car = Car(5)
# can be solved using __init__(self) function
# used to initialize attributes
user_1 = User("aaqil", "001")
print("-----------------------")
user_2 = User("arsh", "002")
print("-----------------------")
user_1.follow(user_2)
print(f"User 1 is following {user_1.following} people and has {user_1.followers} follower(s)")
print(f"User 2 is following {user_2.following} people and has {user_2.followers} follower(s)")
