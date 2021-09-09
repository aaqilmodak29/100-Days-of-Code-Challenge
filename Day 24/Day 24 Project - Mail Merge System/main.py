with open("Input/Names/invited_names.txt") as name_file:
    list_of_names = name_file.readlines()

for name in range(len(list_of_names)):
    names = list_of_names[name]
    stripped_name = names.strip()
    # print(stripped_name)
    with open("Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.readlines()
        replace_name = letter[0]
        # print(replace_name)

        replaced_name = replace_name.replace("[name]", stripped_name)
        # print(replaced_name)

        letter[0] = replaced_name
        # print(letter)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
        for i in range(len(letter)):
            final_letter.write(letter[i])
