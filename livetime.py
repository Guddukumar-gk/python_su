
from cProfile import label
from cgitb import text
from operator import le
from tkinter import Tk

import tkinter
from typing import Text

from time import gmtime, strftime

def clock():


    # using simple format of showing time
    s = strftime("%a, %d %b %Y %H:%M:%S")
    label.config(text = s,font=("arial",80))
    label.after(1000,clock)


root = tkinter.Tk()

label = tkinter.Label(root)
label.pack()
clock()


root.mainloop()