# imports
import tkinter
import sqlite3
import tkinter.font as tkFont
from tkinter import messagebox
import os
import sys

# window
tk_main = tkinter.Tk()


# title and geometry
tk_main.title('Interface')
tk_main.geometry('320x190')

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)


def setTextInput(text):
    entry1.delete(0,"end")
    entry1.insert(0, text)


entry1 = tk_main.entry(tk_main)
entry1.grid(row=1, column=1)

btnSet = tk_main.Button(tk_main, height=1, width=10, text="Set", 
                    command=lambda:setTextInput("new content"))
btnSet.grid(row=1, column=2)

# end of mainloop
tk_main.mainloop()