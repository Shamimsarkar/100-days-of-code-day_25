import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("US STATE GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's the next state's: ").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        turtle_new = Turtle()
        turtle_new.penup()
        turtle_new.hideturtle()
        state_data = data[data.state == answer_state]
        turtle_new.goto(state_data.x.item(), state_data.y.item())
        turtle_new.write(answer_state)
        guess_states.append(answer_state)





