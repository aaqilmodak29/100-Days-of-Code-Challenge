from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_index = {}
guessed_words = []

try:
    df = pandas.read_csv("data/remaining_words.csv")
except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    word_dict = original_df.to_dict(orient="records")

else:
    word_dict = df.to_dict(orient="records")


# ---------------------------------------- CREATING NEW FLASH CARDS ---------------------------------------- #
def gen_next_card():
    global current_index, timer
    window.after_cancel(timer)
    try:
        current_index = random.choice(word_dict)
    except IndexError:
        messagebox.showinfo(title="Wow!", message="No More Words Remaining")
    else:
        word_fr = current_index["French"]
        canvas.itemconfig(canvas_title, text="French", fill="black")
        canvas.itemconfig(canvas_word, text=word_fr, fill="black")
        canvas.itemconfig(canvas_image, image=card_front_image)
    finally:
        timer = window.after(3000, flip_card)


# ---------------------------------------- FLIPPING THE FLASH CARDS ---------------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    word_en = current_index["English"]
    canvas.itemconfig(canvas_word, text=word_en, fill="white")


# ---------------------------------------- REMOVING KNOWN WORDS ---------------------------------------- #
def remove_word():
    word_dict.remove(current_index)
    remaining_data = pandas.DataFrame(word_dict)
    remaining_data.to_csv("data/remaining_words.csv", index=False)

    gen_next_card()


# ---------------------------------------- UI SETUP ---------------------------------------- #
# creating window
window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# creating canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 260, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# writing on canvas
canvas_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))

# creating buttons
known_image = PhotoImage(file="images/right.png")
unknown_image = PhotoImage(file="images/wrong.png")

known_button = Button(image=known_image, highlightthickness=0, command=remove_word)
known_button.grid(column=0, row=1)

unknown_button = Button(image=unknown_image, highlightthickness=0, command=gen_next_card)
unknown_button.grid(column=1, row=1)

gen_next_card()

window.mainloop()
