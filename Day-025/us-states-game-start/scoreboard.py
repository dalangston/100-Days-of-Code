import pandas as pd

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        
        self.pu()
        self.hideturtle()
        

    def write_name(self, place_name, x, y):
        """Write the place_name at given location"""

        self.goto(x, y)
        self.write(place_name)
        