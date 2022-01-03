from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",align="center", font=("arial", 12, "bold"))
        
    def increase_score(self):
        self.score += 1
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=("arial", 12, "bold"))