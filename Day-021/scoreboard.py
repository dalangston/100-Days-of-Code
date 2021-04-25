from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Corier", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.pu()
        self.score = 0
        self.color('white')
        self.text = f"Score: {self.score}"
        self.center()
        self.print_score()

    
    def center(self):

        self.goto(0, 280)


    def print_score(self):

        self.clear()
        self.text = f'Score: {self.score}'
        #self.center()
        self.write(self.text, align=ALIGNMENT, font=FONT)
        

    def update_score(self, points):
        """Change score by points"""

        self.score += int(points)
        self.print_score()
        

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)