from ball import Ball
from paddle import Paddle
from turtle import  Screen
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball= Ball()





screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True
while game_on:
    time.sleep(0.1)
    ball.move()
    if ball.ycor()==280 or ball.ycor()==-280:
        ball.y_bounce()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or  ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.x_bounce()


    screen.update()



screen.exitonclick()
