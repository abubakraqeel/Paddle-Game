from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from Scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Paddle Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Score((30, 240))
l_score = Score((-30, 240))


for i in range(280, -30, -60):
   line = Turtle(shape="square")
   line.penup()
   line.color("white")
   line.shapesize(stretch_wid=2, stretch_len=0.5)
   line.goto(0, i)


    

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.05)
    ball.move()
    #detect collision with top and bottom wall and bounce
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with  paddles and bouunce
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()
    
    #detect collision with x walls and stop:
    if ball.xcor()>380:
     ball.reset()
     l_score.add_score()


    if ball.xcor()<-380:
        ball.reset()
        r_score.add_score()
        
  

    









































screen.exitonclick()
