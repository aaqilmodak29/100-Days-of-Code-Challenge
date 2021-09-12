from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = "Times New Roman"
FONT_SIZE = 12


# ---------------------------- FIND PASSWORD ------------------------------------ #
def find_password():
    try:
        with open("data.json", mode="r") as password_file:
            data = json.load(password_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")

    else:
        website = website_input.get()
        if website in data.keys():
            messagebox.showinfo(title="Information", message=f"Website: {website} "
                                                             f"\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No Information for {website}!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_num = [random.choice(numbers) for _ in range(nr_numbers)]

    pass_letter = [random.choice(letters) for _ in range(nr_letters)]

    pass_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password = pass_num + pass_letter + pass_symbol
    random.shuffle(password)
    shuffled_pass = "".join(password)
    password_input.insert(END, shuffled_pass)
    pyperclip.copy(shuffled_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # fetching input from entry boxes
    website_name = website_input.get()
    email = email_uname_input.get()
    pwd = password_input.get()
    new_data = {
        website_name: {
            "email": email,
            "password": pwd
        }
    }

    # creating a message box(popup box) - returns boolean
    if len(website_name) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please provide all inputs!")
    else:
        messagebox.showinfo(title="Copied!", message="Password copied to clipboard")
        try:
            with open("data.json", mode="r") as password_file:
                # # writing data to json file
                # json.dump(new_data, password_file, indent=4)

                # # reading from json file
                # # converts json data to a python dictionary
                # data = json.load(password_file)
                # print(data)

                # Updating json file
                # reading old data
                data = json.load(password_file)
                # updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", mode="w") as password_file:
                json.dump(new_data, password_file, indent=4)

        else:
            with open("data.json", mode="w") as password_file:
                # saving updated data
                json.dump(data, password_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# creating window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# creating canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# creating labels
website_label = Label(text="Website: ", font=(FONT, FONT_SIZE))
website_label.grid(column=0, row=1)

email_uname_label = Label(text="Email/Username: ", font=(FONT, FONT_SIZE))
email_uname_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=(FONT, FONT_SIZE))
password_label.grid(column=0, row=3)

# creating entry boxes
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_uname_input = Entry(width=35)
email_uname_input.insert(END, "abc@gmail.com")
email_uname_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=17)
password_input.grid(column=1, row=3)

# creating buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=30, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
