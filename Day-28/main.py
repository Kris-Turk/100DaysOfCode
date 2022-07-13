
from cgitb import text
from decimal import Rounded
from  tkinter import *
from turtle import color
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- VARIABLES ------------------------------- #
reps = 0
checkmarks_text = ""
checkmark = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global checkmarks_text
    global reps
    reps = 0
    checkmarks_text = ""
    checkmarks.config(text=checkmarks_text)
    timer_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    

    if reps % 8 == 0:
        count_down(long_break_sec)   
        timer_label.config(text="Break",fg=RED)     
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)        

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    global reps
    global checkmarks_text
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    
    canvas.itemconfig(timer_text, text=F"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks_text += checkmark
            checkmarks.config(text=checkmarks_text)        
    
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=30, bg=YELLOW)


timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW,font=(FONT_NAME,30,"bold"))
timer_label.grid(column=1,row=0)
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="start")
start_button.config(font=(FONT_NAME,8,"bold"),command=start_timer)
start_button.grid(column=0,row=2)


reset_button = Button(text="reset")
reset_button.config(font=(FONT_NAME,8,"bold"), command= reset_timer )
reset_button.grid(column=2,row=2)


checkmarks = Label(pady=10, fg=GREEN, font=(FONT_NAME,12,"bold"),bg=YELLOW)
checkmarks.grid(column=1,row=3)

                  



window.mainloop()


