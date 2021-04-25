from turtle import Turtle

class Snake:

    def __init__(self, length=3):

        self.sections = []
        self.snake_len = length
        self.heading = 0

        self.create_snake(self.snake_len)
        
        self.head = self.sections[0]


    def create_snake(self, length):

        for pos in [(0, 0), (0, 20), (0, 40)]:
            self.add_section(pos)
           
    
    def add_section(self, position):

        new_section = Turtle(shape='square')
        new_section.color('white')
        new_section.pu()
        new_section.setpos(position)
        self.sections.append(new_section)
        

    def extend(self):

        self.add_section(self.sections[-1].position())
        self.snake_len += 1
        


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
