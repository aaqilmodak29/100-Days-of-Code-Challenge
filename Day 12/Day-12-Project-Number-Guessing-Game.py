from art import logo
from random import randint
print(logo)
# setting global variables
EASY_DIF = 10
HARD_DIF = 5
# function to set difficulty
def set_dif():
  dif = input("Choose the difficulty: Easy or Hard?: ").lower()
  if dif == "easy":
    return EASY_DIF
  elif dif == "hard":
    return HARD_DIF

# function to compare guess to answer
def guess_num(guess, answer, turn):
  if guess > answer:
    print("Too High")
    return turn - 1
  elif guess < answer:
    print("Too Low")
    return turn - 1
  elif guess == answer:
    print(f"You guessed correct!, The number was: {answer}")  

def game():
  answer = randint(1, 100)
  turns = set_dif()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining")
    guess = int(input("Guess a number between 1 and 100: "))
    turns = guess_num(guess, answer, turns)
    if turns == 0:
      print("You are out of turns!")
      return
    else:
      print("Guess again")
game()
  
