from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.rt(15)


def turn_ccw():
    tim.lt(15)


def clear_screen():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()
    


screen.listen()

screen.onkey(fun=move_forwards, key='w')
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_ccw)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
