import random
from art import logo
from art import vs
from game_data import data
from replit import clear

OPT_B = random.choice(data)
# randomly fetching dictionaries from list
def options():
    """
    randomly fetching dictionaries from list
    """  
    global OPT_A
    global OPT_B
    global A
    global B
    OPT_A = OPT_B
    OPT_B = random.choice(data)
    A = OPT_A["name"] + ", a " +  OPT_A["description"] + " from " + OPT_A["country"]
    B = OPT_B["name"] + ", a " +  OPT_B["description"] + " from " + OPT_B["country"]
    print(logo)
    print(f"Compare A: {A}")
    print(vs)
    print(f"Against B: {B}")

def higher_or_lower(score):
    """
    compares follower count of 2 entities
    """
    should_continue = True
    while should_continue == True:
        options()
        choices = input("Who has a higher follower count? Type 'A' or 'B'. Type 'C' if you think score is equal: ").upper()
        if choices == "A":
            if OPT_A["follower_count"] > OPT_B["follower_count"]:
                score += 1
                clear()
                print("That's the correct answer!")
                print(f"Your score is: {score}")
            elif OPT_A["follower_count"] < OPT_B["follower_count"]:
                clear()
                print("Bzzt! That is the wrong answer, you lose!")
                return score
                should_continue = False
        elif choices == "B":
            if OPT_B["follower_count"] > OPT_A["follower_count"]:
                score += 1
                clear()
                print("That's the correct answer!")
                print(f"Your score is: {score}")                
            elif OPT_B["follower_count"] < OPT_A["follower_count"]:
                clear()
                print("Bzzt! That is the wrong answer, you lose!")
                return score
                should_continue = False
        elif choices == "C":
            if OPT_B["follower_count"] == OPT_A["follower_count"]:
                score += 1
                clear()
                print(f"Your score is: {score}")                
                print("The follower count of both is equal.")
            else:
                clear()
                print("Bzzt! That is the wrong answer, you lose!")
                return score
                should_continue = False
        else:
            print("Invalid Input!")

def game():
    score_initial = 0
    score = higher_or_lower(score_initial)
    score_initial += 1
    print(f"Your score is: {score}")
game()

