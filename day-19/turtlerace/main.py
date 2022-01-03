from turtle import Screen, Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you're bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

height = -135

for color in colors:
    turtle_name = color + "_turtle" 
    turtle_name = Turtle("turtle")
    turtle_name.color(color)
    turtle_name.penup()    
    height += 40
    turtle_name.goto(x=-220, y=height)
    all_turtles.append(turtle_name)

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()    
            if winning_color == user_bet:
                print(f"You've won the winning turtle was the {winning_color} turtle")
            else:
                print(f"Damn, that was close but you lost, the winner was {winning_color} turtle")
            is_race_on = False                
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()