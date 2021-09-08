import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list = [rock, paper, scissors]
rounds = int(input("Type 1 for Best of 3, or 2 for Best of 5: "))
user_score = 0
comp_score = 0
round_number = 0
while rounds == 1 or rounds == 2:
  if rounds == 1:
    matches = 0
    while(matches < 3 and user_score < 2 and comp_score < 2):
      user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
      print(rps_list[user_choice])

      computer_choice = random.randint(0,2)
      print(f"Computer chose: {rps_list[computer_choice]}")

      if user_choice == computer_choice:
        round_number += 1
        print(f"Round {round_number}: ")
        print(f"Score is: {user_score} - {comp_score}")
        print("Its a draw")


      elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        matches += 1
        comp_score += 1
        round_number += 1
        print(f"Round {round_number}: ")
        print(f"Score is: {user_score} - {comp_score}")
        print("Computer Wins!")


      elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        matches += 1
        user_score += 1
        round_number += 1
        print(f"Round {round_number}: ")
        print(f"Score is: {user_score} - {comp_score}")
        print("You Won!")
  
  if rounds == 2:
    matches = 0
    while(matches < 5 and user_score < 3 and comp_score < 3):
      user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
      print(rps_list[user_choice])

      computer_choice = random.randint(0,2)
      print(f"Computer chose: {rps_list[computer_choice]}")

      if user_choice == computer_choice:
        round_number += 1
        print(f"Round {round_number}: ")
        print(f"Score is: {user_score} - {comp_score}")
        print("Its a draw")


      elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        matches += 1
        comp_score += 1
        round_number += 1
        print(f"Round {round_number}: ")
        print(f"Score is: {user_score} - {comp_score}")
        print("Computer Wins!")


      elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        matches += 1
        user_score += 1
        round_number += 1
        print(f"Round {round_number}: ")
        print(f"Score is: {user_score} - {comp_score}")
        print("You Won!")
    
    








# rps_list = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
# print(rps_list[user_choice])

# computer_choice = random.randint(0,2)
# print(f"Computer chose: {rps_list[computer_choice]}")

# if user_choice == computer_choice:
#   print("Its a draw")

# elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
#   print("Computer Wins!")

# elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
#   print("You Win!")
