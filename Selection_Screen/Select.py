# imports
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import sqlite3
import sys
import os

# window
tk_main = tk.Tk()


# title and geometry
tk_main.title('Selection')
tk_main.geometry('320x100')

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)

def data_window():
    tk_main.destroy()
    os.system(r'python Login_Window\Register.py')

def reg_window():
    tk_main.destroy()
    os.system(r'python Database_Interface\Interface.py')



# end of mainloop
tk_main.mainloop() 