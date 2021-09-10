import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

code_dict = {
    row.letter: row.code for (index, row) in df.iterrows()
}
# print(code_dict)

word = input("Enter a word: ").upper()
word_list = [letter for letter in word]

code_word_list = [code_dict[letter] for letter in word_list if letter in code_dict[letter]]
print(code_word_list)
