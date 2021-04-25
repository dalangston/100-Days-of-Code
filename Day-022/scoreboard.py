from turtle import Turtle

ALIGN='center'
FONT=("Courier", 60, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        
        super().__init__()

        self.color('white')
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
        self.write_score()
       

    def write_score(self):

        self.clear()

        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)

        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)
        

    def score_left(self):
        self.l_score += 1

    def score_right(self):
        self.r_score += 1