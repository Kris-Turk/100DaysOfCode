from cProfile import label
from tkinter import *
from tkinter import font
from turtle import back, bgcolor
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain        
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="White")
        self.score_label.grid(row=0,column=1)
        
        self.q_window = Canvas(self.window,background="White",height=250,width=300)
        self.q = self.q_window.create_text(150,125,font=("Arial,",20,"italic"),text=f"Some Place Holder Text",width=280)
        self.q_window.grid(row=1,column=0,columnspan=2, pady=30)        
        
        
        self.tick_button_img = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick_button_img,highlightthickness=0,command=self.check_true)
        self.tick_button.grid(row=2, column=0)
        
        self.cross_button_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_button_img,highlightthickness=0,command=self.check_false)
        self.cross_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.q_window.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.q_window.itemconfig(self.q, text=q_text)
        else:
            self.q_window.itemconfig(self.q, text="You've reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
        
    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
       
    def give_feedback(self,is_right):
        if is_right:
            self.q_window.config(background="green")
        else:
            self.q_window.config(background="red")
        self.window.after(1000, self.get_next_question)


