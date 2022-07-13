import email
from textwrap import indent
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.font import BOLD, ITALIC
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [ random.choice(letters) for char in range(nr_letters) ]
    password_list += [ random.choice(symbols) for char in range(nr_symbols) ]
    password_list += [ random.choice(numbers) for char in range(nr_numbers) ]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0,password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = website_entry.get()

    def read_json():
        try:
            with open("data.json", "r") as f:
                    data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump({},f)
        finally:
            return data
    
    data = read_json()
    try:   
        username = data[website]["username"]
        password = data[website]["password"]
    except KeyError:
        invalid_entry = messagebox.showerror(title="Error", message="Password is blank, Please enter a valid password")
    else:
        messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")

def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    
    if len(password) == 0:
        invalid_entry = messagebox.showerror(title="Error", message="Password is blank, Please enter a valid password")
        return
    elif len(website) == 0:
        invalid_entry = messagebox.showerror(title="Error", message="Website is blank, Please enter a valid password")
        return
    
    # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\nEmail: {username}\nPassword: {password} \nIs it ok to save?")
    is_ok = True
    
           
    def write_json():
    
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                            
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump({},f)
            write_json()
                            
        else:
            #print("error1")
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
            #print("error2")
            with open("data.json", "w") as f:
                json.dump(data,f, indent=4)

    if is_ok:
        write_json()

        website_entry.delete(0,END)
        password_entry.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=240,height=240)
window.config(padx=50,pady=50)
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=18)
website_entry.focus()
website_entry.grid(column=1,row=1)

search_button = Button(text="Search", command=search,width=18)
search_button.grid(column=2, row=1)


username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=42)
username_entry.insert(0,"kris.turk@hyrbit.co.nz")
username_entry.grid(column=1,row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password", command=generate_password,width=18)
generate_password_button.grid(column=2,row=3, sticky=W+E)

add_button = Button(text="Add",width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()