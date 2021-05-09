# imports
import tkinter
import sqlite3
import tkinter.font as tkFont
from tkinter import messagebox
import os

# window
tkmain = tkinter.Tk()

# input process
username=tkinter.StringVar()
password=tkinter.StringVar()

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)