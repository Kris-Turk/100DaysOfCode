import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answers = []
score = 0


data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()

while len(answers) < 50:    

    answer_state = (screen.textinput(title=f"{score}/50 States Guessed", prompt="Enter the name of a State")).title()

    if answer_state == "Exit":
        break
    if answer_state in all_states and  answer_state not in answers:
        answers.append(answer_state)
        all_states.remove(answer_state)
        state = data[data.state == answer_state ]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.setpos(int(state.x), int(state.y))
        state_turtle.write(answer_state)
        score += 1

        
    print(score)
    print(all_states)
    
states_to_learn = {
   "States": all_states
}

df = pandas.DataFrame(states_to_learn)
df.to_csv("./states_to_learn.csv")