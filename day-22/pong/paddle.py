from turtle import Turtle
STARTING_POSITIONS = [(-560,20),(-560,0),(-560,-20)]
MOVE_DISTANCE = 20

class Paddle():
    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.top = self.segments[0]
        self.bottom = self.segments[-1]
        
    def create_paddle(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(pos)
        self.segments.append(new_segment)
        
    def up(self):
        self.segments[0].setheading(90)
        for seg in range(len(self.segments)-1,0, -1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    # def up(self):
    #     self.segments[0].setheading(90)
    #     self.move()
    
    # def down(self):
    #     self.segments[-1].setheading(270)
    #     self.move()
        
    def down(self):
        self.segments[-1].setheading(270)
        for seg in range(0, len(self.segments)-1, 1):
            new_x = self.segments[seg +1].xcor()
            new_y = self.segments[seg +1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[-1].forward(MOVE_DISTANCE)
        