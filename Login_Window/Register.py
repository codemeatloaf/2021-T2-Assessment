
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
    c.execute("CREATE TABLE IF NOT EXISTS staff (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

# window
tk_main = tk.Tk()
padding=20
tk_main['padx']=padding

# name and geometry
tk_main.title('Create Account')
tk_main.geometry('270x200')

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
#level = Label(tk_main, text="Level", font=input_font)
#level.grid(row=6, column=0)


# username input 
username_entry = tk.StringVar()
username_storage = Entry(tk_main, textvariable=username_entry)
username_storage.grid(row=3, column=0)

# password input 
password_entry = tk.StringVar()
password_storage = Entry(tk_main, textvariable=password_entry)
password_storage.grid(row=6, column=0)

# level input
#level_entry = tk.StringVar()
#level_storage = Entry(tk_main, textvariable=level_entry)
#password_storage.grid(row=7, column=0)

# insert info into db
def savedata():
    conn = sqlite3.connect('login.sqlite')
    c = conn.cursor()
    c.execute('INSERT INTO staff (username, password) VALUES (?,?)', (username_entry.get(), password_entry.get()))
    conn.commit()
    print("OK")

# security
def blank1():
    if password_storage.get():
        blank2()
    else:
        messagebox.showinfo('info', 'Input required.')
        
def blank2():
    if username_storage.get():
        savedata()
    else:
        messagebox.showinfo('info', 'Input required.')

# spacer
spacer=tk.Label(tk_main, text=' ')
spacer.grid(row=8, column=0)

# save button
enter_btn = Button(text="Enter",command=blank1)
enter_btn.grid(row=9, column=0)

# end mainloop
finish()
tk_main.mainloop()