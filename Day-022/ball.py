from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1
        

    def move(self, dist=5):
        """Move the ball"""
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move

        self.goto(x, y)
        

    def bounce(self):
       
       self.y_move *= -1
       
    
    def reflect(self):
       
       self.x_move *= -1
       self.x_move *= 1.1
       self.y_move *+ 1.1
       #self.move()