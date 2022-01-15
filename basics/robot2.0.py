import turtle as t
import time as ti

def rectangle(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

t.goto(-90,100)
rectangle(100,150,'red')