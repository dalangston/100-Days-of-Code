import time
import math

from food import Food
from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

score = ScoreBoard()
food = Food()
snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()
    
    if snake.head.distance(food) < 15:
        score.update_score(10)
        snake.extend()
        food.refresh()
        
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        score.game_over()
        
    for section in snake.sections[1:]:
        if snake.head.distance(section) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
