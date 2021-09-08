
print("Welcome to The Legend of Zelda: Master Sword Challenge.")
print("Your mission is to find the Master Sword.")

first_choice = str(input("You are at your first crossroad, would you lke to go left or right? ")).lower()
if first_choice == "left":
  second_choice = str(input("You see a pair of torches lighting the path ahead, you've reached a checkpoint! You see a Moblin coming after you from the fog, Will you A) Draw your sword and fight or B) Run the other way?")).lower()
  if second_choice == "a":
    third_choice = str(input("You fought the Moblin and made it past the checkpoint! You must be careful from here on as too much noise will attract more monsters! Would you like to turn left or right? ")).lower()
    if third_choice == "left":
      fourth_choice = str(input("You make it past without making too much noise, the goal is in sight, the Korok Forest is right ahead, however, you face another crossroad! Would you like to turn left, right or continue going straight? ")).lower()
      if fourth_choice == "left":
        print("The fog is too thick! Taking advantage of the situation, a horde of Lizalfos emerge from the river and attack! Game Over!")
      elif fourth_choice == "right":
        print("The fog is too thick! Taking advantage of the situation, a horde of Bokoblin emerge from the fog and attack! Game Over!")
      elif fourth_choice == "straight":
        print("Congratulations! You made it to the Korok Forest where the Master Sword rests. Lift the sword from its pedestal and defeat Ganon once and for all! You Win!")
    elif third_choice == "right":
      print("The fog is too thick and is compromising your vision! Unable to comprehend your environment you step on some branches, making noise and attracting monsters!Game Over!")
  elif second_choice == "b":
    print("The fog is too thick, taking advantage of the situation, monsters come out to attack! Game Over!")
elif first_choice == "right":
  print("The fog is too thick, taking advantage of the situation, monsters come out to attack! Game Over!")



