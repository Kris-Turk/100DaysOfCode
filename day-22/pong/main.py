from turtle import Screen
from paddle import Paddle
import time

# Create the Screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# Create & Move the Paddle

paddle = Paddle()


screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down") 


# Create another Paddle

# Create the ball and move it

# Detect collision with wall and bounce

# Detect collision with Paddle

# detect when paddle misses (ball passes end)

#  Scoreboard (keep score)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)



screen.exitonclick()