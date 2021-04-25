import turtle as t

from random import choice, randint


def draw_square(turt, side_len, dashed=False):

    for i in range(4):
        turt.fd(side_len)
        turt.rt(90)


def draw_dashed_square(t):

    for i in range(4):
        for i in range(10):
            t.fd(10)
            if t.isdown():
                t.pu()
            else:
                t.pd()
        t.rt(90)


def get_rand_color():
    """Return randomly selected Turtle color"""

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)


def draw_multi_shape(t, side_len):
    """Draw overlayed 3-9 sided shapes"""

    color = get_rand_color()
    
    for i in range(3,10):

        angle = 360 / i
        t.color(choice(colors))

        for j in range(i):
            t.fd(side_len)
            t.rt(angle)


def random_walk(t, paths=200, max_path_len=50):
    """Crate random turtle path"""

    directions = [0, 90, 180, 270]

    t.pensize(10)

    for i in range(paths):
        t.color(get_rand_color())
        t.seth(choice(directions))
        t.fd(randint(20, max_path_len))


def spirograph(t, r=100):
    """Draw all the circles"""
    
    for i in range(0, 720, 13):
        t.seth(i)
        t.color(get_rand_color())
        t.circle(r)


if __name__ == "__main__":
    timmy_the_turtle = t.Turtle()
    #timmy_the_turtle.shape("turtle")
    #timmy_the_turtle.color("RoyalBlue")
    t.colormode(255)


    #screen = Screen()
    #screen.exitonclick()

    #draw_square(timmy_the_turtle, 90)
    #draw_dashed_square()

    #draw_multi_shape(timmy_the_turtle, 100)
    #random_walk(timmy_the_turtle)
    spirograph(timmy_the_turtle)
