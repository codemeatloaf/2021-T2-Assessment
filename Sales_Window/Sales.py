# imports
import tkinter
import sqlite3
import tkinter.font as tkFont
from tkinter import messagebox 
from tkinter import *
import sys
import os

# window
tk_main = tkinter.Tk()

# name and geometry
tk_main.title('Sales')
tk_main.geometry('270x310')

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)

# title 
title_label=Label(tk_main, text='Sales', font=info_font)
title_label.grid(row=1, column=2)

spacer=Label(tk_main, text='     ', font=info_font)
spacer.grid(row=1, column=3)

product_label = Label(tk_main, text="Product: ", font=input_font)
product_label.grid(row=2, column=1)

customer_label = Label(tk_main, text="Customer: ", font=input_font)
customer_label.grid(row=3, column=1)

booktl_label = Label(tk_main, text="Title: ", font=input_font)
booktl_label.grid(row=4, column=1)

per_label = Label(tk_main, text="Per Unit: ", font=input_font)
per_label.grid(row=5, column=1)

total_label = Label(tk_main, text="Product: ", font=input_font)
total_label.grid(row=6, column=1)


# end of mainloop
tk_main.mainloop() 