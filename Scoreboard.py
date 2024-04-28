from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))
    
    def add_score(self):
        self.clear()
        self.score+=1
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))