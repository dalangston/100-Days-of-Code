import random
import colorgram
import turtle as t

def get_color_list(img_file):
    """Get list of colors in given image"""
    rgb_colors = []
    colors = colorgram.extract(img_file, 30)
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]

        if r > 200 and g > 200 and b > 200:
            continue

        rgb_colors.append((r, g, b))

    return rgb_colors


def draw_grid(t, pallet, grid_size=10):
    """Draw a grid of colored dots"""

    x = t.xcor()
    y = t.ycor()

    for i in range(grid_size):
        draw_row(t, pallet, grid_size)
        y += 50
        t.setpos(x, y)



def draw_row(t, pallet, num_dots=10):
    """Draw a row of dots"""

    for i in range(num_dots):
        t.dot(20, random.choice(pallet))
        t.fd(50)



if __name__ == "__main__":

   colors = get_color_list('image.jpg')
   print(colors)

   t.colormode(255)
   tim = t.Turtle()
   tim.hideturtle()

   tim.pu()
   tim.setpos(-300,-300)
   draw_grid(tim, colors)
