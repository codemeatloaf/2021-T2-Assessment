# imports
import tkinter
import sqlite3
import tkinter.font as tkFont
from tkinter import messagebox
import os

# window
tkmain = tkinter.Tk()

padding=20
tkmain['padx']=padding

# input process
username=tkinter.StringVar()
password=tkinter.StringVar()

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)

# name and geometry
tkmain.title('Create Account')
tkmain.geometry('320x190')

# title 
info_label=tkinter.Label(tkmain, text='Login Application', font=info_font)
info_label.grid(row=0, column=0)

# username input
info_user=tkinter.Label(tkmain, text='Username:', font=input_font)
info_user.grid(row=2, column=0)
user_input=tkinter.Entry(tkmain, textvariable=username)
user_input.grid(row=3, column=0)


# password input
info_pass=tkinter.Label(tkmain, text='Password:', font=input_font)
info_pass.grid(row=6, column=0)
pass_input=tkinter.Entry(tkmain, textvariable=password)
pass_input.grid(row=7, column=0)

# spacer
spacer=tkinter.Label(tkmain, text=' ')
spacer.grid(row=8, column=0)

# submit
submit_btn=tkinter.Button(text='Submit')
submit_btn.grid(row=9, column=0)

# end of mainloop
tkmain.mainloop()
