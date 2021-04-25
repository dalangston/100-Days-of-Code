from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Corier", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.pu()
        self.color('white')
        self.center()
        
        self.datafile = 'data.txt'
        self.score = 0
        self.highscore = 0

        with open(self.datafile) as data:
            self.highscore = int(data.read())

        self.print_score()

    
    def center(self):

        self.goto(0, 280)


    def print_score(self):

        self.clear()
        text = f'Score: {self.score}  High Score: {self.highscore}'
        self.write(text, align=ALIGNMENT, font=FONT)
        

    def update_score(self, points):
        """Change score by points"""

        self.score += int(points)
        self.print_score()
        

    def reset(self):

        if self.score > self.highscore:
            self.highscore = self.score
            
            with open(self.datafile, "w") as data:
                data.write(str(self.highscore))
            
        self.score = 0

        
    def game_over(self):

        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)