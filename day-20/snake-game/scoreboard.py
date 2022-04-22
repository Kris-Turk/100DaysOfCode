from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()        
        self.high_score = self.get_high_score()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_score()
        
    def get_high_score(self):
        with open("high_score.txt") as hs_file:
            return int(hs_file.read())
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} - High Score: {self.high_score}",align="center", font=("arial", 12, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center", font=("arial", 12, "bold"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt",'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()
