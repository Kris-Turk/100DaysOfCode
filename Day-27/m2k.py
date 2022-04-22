from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=200,height=120)
window.config(padx=10,pady=10)

def button_clicked():
    value_label.config(text=float(input.get())*1.6)


# Entry
input = Entry(width=10)
input.grid(column=1,row=0)


# Label
miles_label = Label(text="Miles", font=("Arial",10,"normal"))
miles_label.grid(column=2,row=0)
miles_label.config(padx=5,pady=5)

# Label
equal_label = Label(text="is equal to", font=("Arial",10,"normal"))
equal_label.grid(column=0,row=1)
equal_label.config(padx=5,pady=5)

# Label
value_label = Label(text="0", font=("Arial",10,"normal"))
value_label.grid(column=1,row=1)
value_label.config(padx=5,pady=5)

# Label
unit_label = Label(text="Km", font=("Arial",10,"normal"))
unit_label.grid(column=2,row=1)
unit_label.config(padx=5,pady=5)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)
button.config(padx=5,pady=5)


window.mainloop()