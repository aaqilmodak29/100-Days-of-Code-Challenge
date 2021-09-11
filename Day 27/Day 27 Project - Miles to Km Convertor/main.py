from tkinter import *
# creating window
window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=250, height=200)
window.config(padx=50, pady=50)

# creating input box
receive_input = Entry(width=10)
receive_input.insert(END, "0")
receive_input.focus()
receive_input.grid(column=1, row=0)
receive_input.size()

# creating labels
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

another_label = Label(text="is equal to", font=("Arial", 10))
another_label.grid(column=0, row=1)
another_label.config(padx=20, pady=20)

converted_value_label = Label(text="0", font=("Arial", 10))
converted_value_label.grid(column=1, row=1)


# function to convert miles to km
def conversion():
    input_miles = receive_input.get()
    input_km = float(input_miles) * 1.61
    converted_value_label["text"] = round(input_km, 2)


# creating button
calc_button = Button(text="Convert", command=conversion)
calc_button.grid(column=1, row=2)

window.mainloop()
