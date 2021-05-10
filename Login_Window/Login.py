
# imports
import tkinter
import sqlite3
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
import sys
import os

db=sqlite3.connect('login.sqlite')

# define variables
def login():
    cursor=db.cursor()
    cursor.execute("SELECT * FROM staff where username=? AND password=?",(user_input.get(), pass_input.get()))
    row=cursor.fetchone()
    if row:
        # end
        messagebox.showinfo('info', 'Login Success!')
        select_option()
        
    else:
        # error screen
        messagebox.showinfo('info', 'Login failure.')

# focus next text box
def focus_next(event):
    event.widget.tk_focusNext().focus()
    return("break")


# window
tk_main = tkinter.Tk()

padding=20
tk_main['padx']=padding

# input variables
username=tkinter.StringVar()
password=tkinter.StringVar()

# open sign up app
def sign_up():
    os.system(r'python Login_Window\Register.py')

# open selection app
def select_option():
    os.system(r'python Selection_Screen\Select.py')

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)
 
# name and geometry
tk_main.title('Login')
tk_main.geometry('320x220')

# title 
info_label=tkinter.Label(tk_main, text='Login Application', font=info_font)
info_label.grid(row=0, column=0)

# username input
info_user=tkinter.Label(tk_main, text='Username:', font=input_font)
info_user.grid(row=2, column=0)
user_input=tkinter.Entry(tk_main, textvariable=username)
user_input.grid(row=3, column=0)
user_input.bind("<Tab>", focus_next)


# password input
info_pass=tkinter.Label(tk_main, text='Password:', font=input_font)
info_pass.grid(row=6, column=0)
pass_input=tkinter.Entry(tk_main, textvariable=password)
pass_input.grid(row=7, column=0)
pass_input.bind("<Tab>", focus_next)

# spacer
spacer=tkinter.Label(tk_main, text=' ')
spacer.grid(row=8, column=0)

# submit
submit_btn=tkinter.Button(text='Submit', command=login)
submit_btn.grid(row=9, column=0)

# create admin account
# sign_btn=tkinter.Button(text="Sign Up", command= sign_up)
# sign_btn.grid(row=10, column=0)

# end of mainloop
tk_main.mainloop()
