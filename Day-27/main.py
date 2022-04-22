from tkinter import *

window = Tk()

window.title("GAME")
window.minsize(width=500,height=500)
window.config(padx=10,pady=10)



def button_clicked():
    label.config(text=input.get())


# Label
label = Label(text="Label1", font=("Arial",24,"bold"))
label.grid(column=0,row=0)

  
# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

# Button
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=2,row=0)


# Entry
input = Entry(width=10)
input.grid(column=3,row=2)





window.mainloop()
