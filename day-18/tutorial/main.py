import turtle as t
from random import choice,randint


t.colormode(255)
heading = [ 0, 90, 180, 270 ] 

tim = t.Turtle()

tim.shape("turtle")


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):    
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# sides = 2

# for _ in range(10):
#     sides += 1
#     angle = (360/sides)
#     tim.color(choice(colors))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return ( r,g,b )


# for _ in range(200):
#     tim.speed(10)
#     tim.setheading(choice(heading))
#     tim.color(random_color())
#     tim.forward(20)

def draw_spirograph(angle):
    for _ in range( int(360 / angle)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + angle)

draw_spirograph(20)




screen = t.Screen()
screen.exitonclick()