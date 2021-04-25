from random import randint
from turtle import Turtle, Screen

#tim = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
#tim.pu()
#tim.goto(x=-240, y=-100)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

start_line = -230
start_width = 250
max_move = 10

racers = []

for c in range(len(colors)):
    racers.append(Turtle(shape='turtle'))
    racers[-1].color(colors[c])

gap = int(start_width / len(racers))
y_pos = 0 - (start_width / 2)

for r in racers:
    r.pu()
    r.goto(x=start_line, y=y_pos)
    y_pos += gap


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nEnter a color:")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:

    for r in racers:
        r.fd(randint(1, max_move))
        if r.xcor() >= 230:
            winner = r.pencolor()
            is_race_on = False

print(f"The winner is {winner}")
if winner == user_bet.lower():
    print("You were right!!!")

screen.exitonclick()
