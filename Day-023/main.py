import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cm = CarManager()
player = Player()
score = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    score.print_level()
    cm.move_cars()
    
    if player.ycor() > 280:
        player.goto_start()
        cm.speed_mult *= 1.2
        score.level += 1
        
    for car in cm.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            
score.game_over()

screen.exitonclick()