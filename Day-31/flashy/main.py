from select import select
from tkinter import *
from tkinter.font import BOLD, ITALIC
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"


########################################### Program Logic ############################################
try:
    df = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = read_csv("./data/french_words.csv")
finally:
    records = df.to_dict(orient="records")

random_word = {}

def select_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(records)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=random_word["French"], fill="black")
    flash_card.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=random_word["English"], fill="white")
    flash_card.itemconfig(card_background, image=card_back)
    
def is_known():
    global records
    records.remove(random_word)
    data = DataFrame(records)
    data.to_csv("data/words_to_learn.csv", index=False)
    select_word()
    
    

########################################### UI SETUP ############################################

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer = window.after(3000, func=flip_card)


card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
right_button_img = PhotoImage(file="images/right.png")
flash_card = Canvas(window,bg=BACKGROUND_COLOR ,width=800,height=526,bd=0, highlightthickness=0)
card_background = flash_card.create_image(400,263,image=card_front)
flash_card.grid(column=0,row=0,columnspan=2)
card_title = flash_card.create_text(400,150,text="French",font=("Ariel,",40,ITALIC))
card_word = flash_card.create_text(400,263,text="Word",font=("Ariel,",60,BOLD))
   

right_button = Button(image=right_button_img,border=0,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

wrong_button = Button(image=wrong_button_img,border=0,highlightthickness=0, command=select_word)
wrong_button.grid(column=0,row=1)
    
    
select_word()

window.mainloop()
