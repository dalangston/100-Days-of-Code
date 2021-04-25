from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    

    def __init__(self):

        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-260, 260)

        self.level = 1

        self.print_level()

    
    def print_level(self):

        self.clear()
        self.write(f"Level {self.level}", font=FONT)
        
    
    def game_over(self):

        self.home()

        self.write("Game Over", align='center', font=FONT)