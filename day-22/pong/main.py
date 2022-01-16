from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Create the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


# Create & Move the Paddle

r_paddle = Paddle(350)
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down") 

# Create another Paddle

l_paddle = Paddle(-350)
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s") 

#  Scoreboard (keep score)

scoreboard = Scoreboard()

# Create the ball and move it

ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
# Detect collision with wall and bounce

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()    

# Detect collision Paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.increase_move_speed()
        
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_move_speed()
        
# detect when r_paddle miss

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()    
        
# detect when l_paddle miss
    if ball.xcor() < -380:
        ball.reset()  
        scoreboard.r_point()  



screen.exitonclick()