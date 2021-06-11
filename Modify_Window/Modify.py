# imports
import tkinter
import sqlite3
from tkinter.constants import N
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
import os
import sys

# window
tk_main = tkinter.Tk()

# title and geometry
tk_main.title('Modify')
tk_main.geometry('320x190')

# create if not exists
with sqlite3.connect('login.sqlite') as conn:
    c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS staff (username TEXT, password TEXT, level INTEGER)")
conn.commit()
conn.close()
print('MYSQLITE connection closed (1/2)')

# control of tabs
tabControl = ttk.Notebook(tk_main)

# fonts
info_font=tkFont.Font(family="Source Code Pro Bold", size=20)
input_font=tkFont.Font(family="Source Code Pro Italic", size=15)

table = tkinter.StringVar()

# tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Display')
tabControl.add(tab2, text ='Manage')
tabControl.add(tab3, text ='Modify')
tabControl.add(tab4, text ='Staff')
tabControl.pack(expand = 1, fill ="both")

# Tab 1
Label1 = ttk.Label(tab1, text ="Table/Tables:  ", font=input_font,)
Label1.grid(column = 1, row = 1)  

# Tab 2
Label2 = ttk.Label(tab2, text ="Table", font=input_font,)
Label2.grid(column = 0, row = 0)

user_input=tkinter.Entry(tab1, textvariable=table)
user_input.grid(column = 2, row = 1)

# end of mainloop
tk_main.mainloop()