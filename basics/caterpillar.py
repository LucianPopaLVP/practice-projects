import turtle as t
import random as rd
import time as time

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf')

text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press space to start', align='center', font=('Arial',10,'bold'))

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

