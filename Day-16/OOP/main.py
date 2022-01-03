# from turtle import  Turtle,Screen

# timmy = Turtle()
# print(timmy)
# timmy.forward(100)
# timmy.shape("turtle")
# timmy.color("red")

# timmy_view = Screen()
# print(timmy_view.canvheight)
# timmy_view.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)