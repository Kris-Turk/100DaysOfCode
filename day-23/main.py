import time
from turtle import Screen, Turtle
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


# Create Player controlled turtle at bottom that moves up on key press UP
player = Player()
screen.onkey(player.go_up,"Up")

# Create cars that are 20px high by 40px wide and move from right edge to left edge
# no cars in top and bottom 50px

carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carmanager.create_car()
    carmanager.move_cars()


    # Detect Turtle collision with Car and stop game if happens
    
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    
    # detect when Turtle crosses the road, return him to his start position and increase speeed and Increment Score
    if player.ycor() > 290:
        player.return_to_start()
        carmanager.level_up()
        scoreboard.update_score()
    

screen.exitonclick()












# Create a scoreboard that keeps score and displays GAME OVER
