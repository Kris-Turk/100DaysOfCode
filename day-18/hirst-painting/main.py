# import colorgram

# # extracted_colors = colorgram.extract('image.jpeg',30)
# # color_tuples = []

# # def extract_rgb(colorgram_list_entry):
# #     r = colorgram_list_entry.rgb.r
# #     g = colorgram_list_entry.rgb.g
# #     b = colorgram_list_entry.rgb.b
# #     return (r,g,b)

# # for item in extracted_colors:
# #     color_tuples.append(extract_rgb(item))

# # print(color_tuples)

color_list = [(182, 19, 42), (217, 238, 244), (186, 74, 37), (251, 231, 236), (17, 138, 84), (114, 180, 206), (25, 121, 166), (190, 179, 23), (25, 39, 73), (209, 162, 95), (217, 62, 99), (76, 173, 97), (178, 45, 62), (238, 231, 3), (38, 45, 111), (17, 164, 210), (218, 132, 158), (214, 71, 52), (125, 183, 124), (7, 59, 38), (167, 28, 25), (10, 93, 54), (148, 207, 220), (235, 159, 179), (6, 85, 110), (161, 211, 183), (233, 172, 165)]

import turtle as t
from random import choice

t.colormode(255)

tim = t.Turtle()

tim.penup()
tim.hideturtle()
tim.setpos(-250,-250)


def draw_row(number_of_dots):
    for _ in range(number_of_dots):
        tim.dot(20, choice(color_list))
        tim.forward(50)        
    tim.setpos(-250,tim.position()[1] + 50)

def draw_grid(grid_size):
    for _ in range(grid_size):
        draw_row(grid_size)
        

draw_grid(5)

screen = t.Screen()
screen.exitonclick()

