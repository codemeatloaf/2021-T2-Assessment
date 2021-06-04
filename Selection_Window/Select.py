# imports
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter
import tkinter.font as tkFont
import sqlite3
import sys
import os

# window
tk_main = tk.Tk()

# title and geometry
tk_main.title('Selection')
tk_main.geometry('295x100')


# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)
input_font=tkFont.Font(family="Source Code Pro Bold", size=9)

# definitions
def reg_window():
    tk_main.destroy()
    os.system(r'python Login_Window\Register.py')

def data_window():
    tk_main.destroy()
    os.system(r'python Sales_Window\Interface.py')

def confirm():
    conn = sqlite3.connect('permissions.sqlite')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM access WHERE level = 1")
    match=cursor.fetchone()
    if match: 
        conn.close()
        messagebox.showinfo('info', 'Register new users here.')
        reg_window()
    else: 
        conn.close()
        messagebox.showinfo('info', 'You do not have the credentials to register new users.')



# buttons
data_btn = Button(text="Modify",command=data_window)
data_btn.place(x=25, y=50)
data_btn.config(height = 2, width = 9)
data_btn['font'] = input_font

reg_btn = Button(text="Register",command=confirm)
reg_btn.place(x=205, y=50)
reg_btn.config(height = 2, width = 8)
reg_btn['font'] = input_font

# Labels
info_label = Label(tk_main, text='Select', font=info_font)
info_label.place(x=100, y=3)

# end of mainloop
tk_main.mainloop() 