class Snake:

    def __init__(self, screen, length=3):

        self.sections = []
        self.snake_len = length
        self.heading = 0

        self.create_snake(self.snake_len)
        
        self.head = self.sections[0]


    def create_snake(self, length):

        from turtle import Turtle

        for i in range(length):
            self.sections.append(Turtle(shape='square'))
            self.sections[-1].color('white')
            self.sections[-1].pu()
            self.sections[-1].setx(-(i*20))


    def move(self, dist=20):

        for s in range(self.snake_len - 1, 0, -1):
            self.sections[s].goto(self.sections[s-1].pos())

        self.head.setheading(self.heading)
        self.head.fd(dist)


    def up(self):
        """Change Snake Heading to Up"""
        if self.heading != 270:
            self.heading = 90


    def down(self):
        """Change Snake Heading to Down"""
        if self.heading != 90:
            self.heading = 270


    def left(self):
        """Change Snake Heading to Left"""
        if self.heading != 0:
            self.heading = 180


    def right(self):
        """Change Snake Heading to Right"""
        if self.heading != 180:
            self.heading = 0
