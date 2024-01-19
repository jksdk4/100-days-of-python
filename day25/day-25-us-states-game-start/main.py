import turtle
from turtle import Screen, Turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)
state_data = pandas.read_csv("50_states.csv")
states_list = state_data.state.to_list()
guessed = []
guessed_amount = 0

answer_state = screen.textinput(title="Guess the State", prompt="Enter a state name.")

while len(guessed) < len(states_list):
    if answer_state.lower() == 'exit':
        states_to_learn = []
        for state in states_list:
            if state not in guessed:
                states_to_learn.append(state)

        df = pandas.DataFrame(states_to_learn)
        df.to_csv("missed_states.csv")
        break
    titled_answer = answer_state.title()
    if titled_answer in guessed:
        answer_state = screen.textinput(title=f"{guessed_amount}/{len(states_list)} States Correct",
                                        prompt="Guess another state.")
        continue
    if titled_answer in states_list:
        guessed.append(titled_answer)
        guessed_amount += 1
        label = Turtle()
        label.hideturtle()
        label.penup()
        chosen_state = (state_data[state_data.state == titled_answer])
        label.goto(int(chosen_state.x), int(chosen_state.y))
        label.write(chosen_state.state.item())

    answer_state = screen.textinput(title=f"{guessed_amount}/{len(states_list)} States Correct", prompt="Guess another state.")



turtle.mainloop()
