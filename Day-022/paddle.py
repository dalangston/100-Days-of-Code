from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, start_pos):
        
        super().__init__()

        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        #self.goto((350, 0))
        self.goto(start_pos)
        
    def go_up(self):
        #new_y = rt_paddle.ycor + 20
        self.goto((self.xcor(), self.ycor() + 20))

    def go_down(self):
        self.goto((self.xcor(), self.ycor() - 20))


        