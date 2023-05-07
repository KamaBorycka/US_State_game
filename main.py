import turtle

import pandas as pd

states_data = pd.read_csv("50_states.csv")

score = 0
highest_score = len(states_data["state"])
guessed_states = []
missed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"Your score:{score}/{highest_score}",
        prompt="What is another state name?",
    ).title()

    for name_state in states_data["state"]:
        if answer_state == name_state and answer_state not in guessed_states:
            guessed_states.append(name_state)
            score += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            row_name_state = states_data[states_data["state"] == name_state]
            t.goto(x=int(row_name_state["x"]), y=int(row_name_state["y"]))
            t.write(name_state)

    if answer_state == "Exit":
        missed_states = [
            state for state in states_data["state"] if state not in guessed_states
        ]
        mis_states = pd.DataFrame(missed_states)
        mis_states.to_csv("mis_states.csv")
        break
