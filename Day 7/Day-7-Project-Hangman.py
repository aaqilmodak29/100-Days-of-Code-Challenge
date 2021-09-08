import random
import hangman_art
import hangman_words

print(hangman_art.logo)
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
lives = 6
# print(f'{chosen_word}.')

length = len(chosen_word)
display = []

for i in range(length):
  display.append("_")
print(display)

while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"{guess} has already been guessed")
    for p in range(length):
      letter = chosen_word[p]
      if letter == guess:
        display[p] = letter



    if guess not in chosen_word:
      lives -= 1
      print(f"{guess} is not in the word, you have lost a life.")
      print(hangman_art.stages[lives])
      if lives == 0:
        end_of_game = True
        print("You Lose")

    print(display)

    if "_" not in display:
      end_of_game = True
      joint_word = ''.join(display)
      print(f"The word is: {joint_word}")
      print("You win.")

