from names_of_states import States
from score import Scoreboard
import turtle
import pandas


data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"

states = []
guessed_states = []
screen.addshape(IMAGE)
turtle.shape(IMAGE)
screen.tracer(0)


list_of_states = data["state"].to_list()
list_of_x = data["x"].to_list()
list_of_y = data["y"].to_list()


score_tracker = Scoreboard()

while len(guessed_states) < 50:
    screen.update()
    if score_tracker.answer == "Exit":
        break
    if score_tracker.answer in list_of_states:
        guessed_states.append(score_tracker.answer)
        state_data = data[data.state == score_tracker.answer]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        correct_answer = States(score_tracker.answer, x_cor, y_cor)
        score_tracker.increase_score()
    elif score_tracker.answer not in list_of_states:
        print("That's not a State!")
        score_tracker.setup_scoreboard()
# print(list_of_states)
# print(guessed_states)

for state in range(len(guessed_states)):
    if guessed_states[state] in list_of_states:
        list_of_states.remove(guessed_states[state])
remaining_states = {
    "Remaining States": list_of_states
}
remaining_data = pandas.DataFrame(remaining_states)
remaining_data.to_csv("remaining_states.csv")

# # will keep screen open even after code ends
# turtle.mainloop()
