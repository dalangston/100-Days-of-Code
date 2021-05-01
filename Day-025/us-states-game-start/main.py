import pandas as pd
import turtle

from scoreboard import Scoreboard


state_data_file = '50_states.csv'

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("US States Game")

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

place = Scoreboard()

state_locs = pd.read_csv(state_data_file)

game_is_on = True

states_remaining = state_locs.state.to_list()

while game_is_on:

    if len(states_remaining) < 50:
        t_txt = f"States Guessed: ({50 - len(states_remaining)}/50)"
        screen.title(t_txt)

    answer_state = screen.textinput(title='Guess the State', prompt='Enter the name of a state').title()

    if answer_state == 'Exit':
        break
    
    if answer_state in states_remaining:
        state = state_locs[state_locs.state == answer_state]
        state_x = int(state.x)
        state_y = int(state.y)
        place.write_name(answer_state, state_x, state_y)
        states_remaining.remove(answer_state)
        
    if len(states_remaining) < 1:
        game_is_on = False


screen.exitonclick()