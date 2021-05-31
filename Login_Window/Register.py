
# imports
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import sqlite3
import sys
import os


# create if not exists
with sqlite3.connect('login.sqlite') as conn:
    c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS staff (username TEXT, password TEXT, level INTEGER)")
conn.commit()
conn.close()

# focus next text box
def focus_next(event):
    event.widget.tk_focusNext().focus()
    return("break")

# dropdown list
option_list = [
    "Admin",
    "Staff"
]

# window
tk_main = tk.Tk()
padding=20
tk_main['padx']=padding

# name and geometry
tk_main.title('Create Account')
tk_main.geometry('270x310')

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)

# title 
info_label=tk.Label(tk_main, text='Create Account', font=info_font)
info_label.grid(row=1, column=0)

# labels
username_label = Label(tk_main, text="Username", font=input_font)
username_label.grid(row=2, column=0)

password = Label(tk_main, text="Password", font=input_font)
password.grid(row=4, column=0)

password2 = Label(tk_main, text="Re-Enter Password", font=input_font)
password2.grid(row=7, column=0)

level = Label(tk_main, text="Level", font=input_font)
level.grid(row=9, column=0)

# username input 
username_var = tk.StringVar()
username_input = Entry(tk_main, textvariable=username_var)
username_input.grid(row=3, column=0)
username_input.bind("<Tab>", focus_next)

# password input 
password_var = tk.StringVar()
password_input = Entry(tk_main, textvariable=password_var)
password_input.grid(row=6, column=0)
password_input.bind("<Tab>", focus_next)

# password security
password2_var = tk.StringVar()
password2_input = Entry(tk_main, textvariable=password2_var)
password2_input.grid(row=8, column=0)
password2_input.bind("<Tab>", focus_next)

# level input
level_var = tk.StringVar()
level_input = tk.OptionMenu(tk_main, level_var, *option_list)
level_input.grid(row=10, column=0)

def next_window():
    tk_main.destroy()
    os.system(r'python Selection_Screen\Select.py')

# insert info into db
def savedata():
    conn = sqlite3.connect('login.sqlite')
    c = conn.cursor()
    c.execute('INSERT INTO staff (username, password, level) VALUES (?,?,?)', (username_var.get(), password_var.get(), level_var.get()))
    conn.commit()
    next_window()


# security
def blank1():
    if username_input.get():
        blank2()
    else:
        messagebox.showinfo('info', 'Username required.')

def blank2():
    if password_input.get():
        secure()
    else:
        messagebox.showinfo('info', 'Please check your password.')  

def secure():
    if password2_input.get() == password_input.get():
        blank3()
    else:
     messagebox.showinfo('info', 'Please check your password.')   


def blank3():
    if level_var.get():
        savedata()
    else:
        messagebox.showinfo('info', 'Level required.')

# make it so that if you already have the account, you cant make it again
#def blank4():


# spacer
spacer=tk.Label(tk_main, text=' ')
spacer.grid(row=11, column=0)

# save button
enter_btn = Button(text="Enter",command=blank1)
enter_btn.grid(row=12, column=0)


# end mainloop
tk_main.mainloop()
