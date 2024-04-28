from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_incr = 10
        self.x_incr = 10
    def move(self):
            new_x=self.xcor()+self.x_incr
            new_y=self.ycor() + self.y_incr  
            self.goto(new_x, new_y)

    def bounce_y(self):
         self.y_incr*=-1
    def bounce_x(self):
         self.x_incr*=-1
    def reset(self):
         self.home()
         self.bounce_x()

  
