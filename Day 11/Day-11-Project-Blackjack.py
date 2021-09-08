import random
from art import logo
print(logo)
cards = [11, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10, 10, 10, 10]
user_cards = []
comp_cards = []
def comp_victory():
  print("Computer Wins")
  return 
def user_victory():
  print("User Wins")
  return 
def draw():
  print("Its a draw")
  return 



while len(user_cards) <= 1 and len(comp_cards) <= 1:
    user_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
print(f"Your Cards: {user_cards}") 
print(f"Computer's Cards: {comp_cards}") 

user_total = 0
comp_total = 0
new_user_total = 0

for card in range(len(user_cards)):
    user_total = user_total + user_cards[card]
for card in range(len(comp_cards)):
    comp_total = comp_total + comp_cards[card]
print(f"Your total: {user_total}")
print(f"Computer's Total: {comp_total}")

if user_total == 21 and comp_total == 21:
    draw()
elif user_total == 21:
    user_victory()
elif comp_total == 21:
    comp_victory()    
elif user_total > 21:
  if user_cards[0] == cards[0] or user_cards[1] == cards[0]:
    choice = input("Do you have an ace? Type 'y' for Yes or 'n' for No: ")
    if choice == "y":
      choice2 = int(input("Do you want the value of ace to be 1 or 11?: "))
      if choice2 == 1:
        for card in range(len(user_cards)):
          user_total = user_total + user_cards[card]
        if user_total > 21:
          comp_victory()
      elif choice2 == 11:
            comp_victory()
    elif choice == "n":
          comp_victory()
elif user_total <= 21:
      cont = True
      while cont == True and user_total < 21:
        draw_card = input("Do you want to draw another card? Type 'y' for Yes or 'n' for No: ")
        if draw_card == "y":
          user_cards.append(random.choice(cards))
          print(f"Your new hand is: {user_cards}")
          user_total += user_cards[-1]
          print(f"Your new total is: {user_total}")
          if user_total > 21:
            for card in range(len(user_cards)):
              if user_cards[card] == cards[0]:
                choice = input("Do you have an ace? Type 'y' for Yes or 'n' for No: ")
                if choice == "y":
                  choice2 = int(input("Do you want the value of ace to be 1 or 11?: "))
                  if choice2 == 1:
                    for card in range(len(user_cards)):
                      if user_cards[card] == 11:
                        user_cards[card] = 1
                        print(user_cards)
                        new_user_total = 0
                        for card in range(len(user_cards)):
                          new_user_total += user_cards[card]
                        print(f"Your new total is: {new_user_total}")
                      #   if new_user_total == comp_total:
                      #     draw()
                      #   elif new_user_total > comp_total and new_user_total <= 21:
                      #     user_victory()
                      #   elif new_user_total < comp_total and comp_total <= 21:
                      #     comp_victory()
                    
                  if  choice2 == 11:
                    if user_total > 21:
                      # comp_victory()
                      print("Computer Wins!")
                  elif choice2 == 11:
                    print("Computer Wins!")
                elif choice == "n":
                  print("Computer Wins!")
            if new_user_total == comp_total:
                print("Draw")
            elif new_user_total > comp_total and new_user_total <= 21:
                print("User Wins!")
            elif new_user_total < comp_total and comp_total <= 21:
                print("Computer Wins!")
            
        elif draw_card == "n":
          cont = False

      while comp_total < 17 and user_total < 21 :
        comp_cards.append(random.choice(cards))
        print(f"Computer's new hand is: {comp_cards}")
        comp_total += comp_cards[-1]
        print(f"Computer's new total is: {comp_total}")
        if comp_total > 21:
            user_victory()
        elif comp_total < 21:
            if user_total > comp_total and user_total <= 21:
                user_victory()
            elif user_total < comp_total and comp_total <= 21:
                comp_victory()
            elif user_total == comp_total:
                draw()
        elif comp_total == 21:
          if user_total == comp_total:
            draw()
          else:
            comp_victory()
      
      if user_total > comp_total and user_total <= 21:
          user_victory()
      elif user_total < comp_total and comp_total <= 21:
          comp_victory()
      elif user_total == comp_total:
          draw()


