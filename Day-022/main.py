import time

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('pyPong')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    #time.sleep(0.01)
    
    ball.move()
    
    if abs(ball.ycor()) > 280:
        ball.bounce()
        
    if abs(ball.xcor()) > 320:
        if l_paddle.distance(ball) < 50 or r_paddle.distance(ball) < 50:
            ball.reflect()

    if abs(ball.xcor()) > 380:
        if ball.distance(l_paddle) < ball.distance(r_paddle):
            score.score_right()
        else:
            score.score_left()
        
        ball.home()
        score.write_score()
        
        if score.l_score + score.r_score > 9:
            game_is_on = False

screen.exitonclick()