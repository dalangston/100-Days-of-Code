from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        
        self.speed_mult = 1
        self.min_cars = 10
        self.max_cars = 30
        self.max_y = 260
        self.min_y = -260
        self.left_edge = -300
        self.right_edge = 300
        self.all_cars = []

        self.add_cars(random.randint(self.min_cars, self.max_cars))
        

    def add_cars(self, num_cars):
        
        for c in range(num_cars):
            
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_y = random.randint(self.min_y, self.max_y)
            x_offset = random.randint(0, 1000)
            new_car.goto(self.right_edge + x_offset, new_y)
            
            self.all_cars.append(new_car)
        

    def move_cars(self):
        
        for car in self.all_cars:
            car.fd(MOVE_INCREMENT * self.speed_mult)
            
            if car.xcor() < self.left_edge:
                y_pos = car.ycor()
                car.goto(self.right_edge, y_pos)
    