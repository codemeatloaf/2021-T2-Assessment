
# imports
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import sqlite3

def finish():
    conn = sqlite3.connect('login.sqlite')
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
tk_main.geometry('270x260')

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)

# title 
info_label=tk.Label(tk_main, text='Create Account', font=info_font)
info_label.grid(row=0, column=0)

# labels
username = Label(tk_main, text="Username", font=input_font)
username.grid(row=2, column=0)
password = Label(tk_main, text="Password", font=input_font)
password.grid(row=4, column=0)
level = Label(tk_main, text="Level", font=input_font)
level.grid(row=7, column=0)


# username input 
username_entry = tk.StringVar()
username_storage = Entry(tk_main, textvariable=username_entry)
username_storage.grid(row=3, column=0)
username_storage.bind("<Tab>", focus_next)

# password input 
password_entry = tk.StringVar()
password_storage = Entry(tk_main, textvariable=password_entry)
password_storage.grid(row=6, column=0)
password_storage.bind("<Tab>", focus_next)

# level input
level_entry = tk.StringVar()
level_storage = tk.OptionMenu(tk_main, level_entry, *option_list)
level_storage.grid(row=8, column=0)

# insert info into db
def savedata():
    conn = sqlite3.connect('login.sqlite')
    c = conn.cursor()
    c.execute('INSERT INTO staff (username, password, level) VALUES (?,?,?)', (username_entry.get(), password_entry.get(), level_entry.get()))
    conn.commit()
    print("OK")

# security
def blank1():
    if username_storage.get():
        blank2()
    else:
        messagebox.showinfo('info', 'Username required.')

def blank2():
    if password_storage.get():
        blank3()
    else:
        messagebox.showinfo('info', 'Password required.')      

def blank3():
    if level_entry.get():
        savedata()
    else:
        messagebox.showinfo('info', 'Level required.')


# spacer
spacer=tk.Label(tk_main, text=' ')
spacer.grid(row=9, column=0)

# save button
enter_btn = Button(text="Enter",command=blank1)
enter_btn.grid(row=10, column=0)


# end mainloop
finish()
tk_main.mainloop()