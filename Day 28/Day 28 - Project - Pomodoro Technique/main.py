from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_timer, text="00:00")
    timer_label["text"] = "Timer"
    timer_label["fg"] = GREEN
    checkmark_labels["text"] = ""
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        countdown(short_break_sec)
        timer_label["text"] = "Short Break"
        timer_label["fg"] = PINK

    elif reps % 8 == 0:
        countdown(long_break_sec)
        timer_label["text"] = "Long Break"
        timer_label["fg"] = PINK

    else:
        countdown(work_sec)
        timer_label["text"] = "Work"
        timer_label["fg"] = PINK


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    # changing text on canvas text
    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        checkmark_labels.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# # DYNAMIC TYPING
# a = 3
# # changes data type of "a" to string
# a = "Hello"


window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)

# creating labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), highlightthickness=0)
timer_label.grid(column=1, row=0)

checkmark_labels = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
checkmark_labels.grid(column=1, row=3)

# creating canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")

# image to canvas
canvas.create_image(100, 112, image=tomato_image)

# writing text on image 
canvas_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# creating buttons
start_button = Button(text="Start", font=(FONT_NAME, 12), command=start_timer)
start_button.config(padx=5, pady=5)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12), command=reset_timer)
reset_button.config(padx=5, pady=5)
reset_button.grid(column=2, row=2)

window.mainloop()
