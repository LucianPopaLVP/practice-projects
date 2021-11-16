import random
import time
from tkinter import Tk , Button , DISABLED

def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()