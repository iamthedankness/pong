from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move = 10
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
    def y_bounce(self):
        self.y_move*= -1
    def x_bounce(self):
        self.x_move*= -1





