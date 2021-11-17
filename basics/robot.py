import turtle as t
import time as ti

def rectangle(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()