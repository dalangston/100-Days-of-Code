from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    
    def __init__(self):

        super().__init__()

        self.start_y = -280
        self.shape("turtle")
        self.penup()
        #self.goto(0, -280)
        self.setheading(90)
        self.move_dist = 20
        
        self.goto_start()


    def move(self):
        
        self.forward(self.move_dist)
        

    def goto_start(self):
        
        self.goto(0, self.start_y)