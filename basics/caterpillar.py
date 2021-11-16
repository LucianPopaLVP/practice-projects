import turtle as t
import random as rd
import time as ti

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed()
leaf.hideturtle()

text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press space to start', align='center', font=('Arial',10,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall =  t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y >  top_wall or y < bottom_wall
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200, 200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()
    
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('Game over!', align='center', font=('Arial', 30, 'normal'))
    
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_lenght = 3
    caterpillar.shapesize(1, caterpillar_lenght, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_lenght = caterpillar_lenght + 1
            caterpillar.shapesize(1, caterpillar_lenght, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        elif outside_window():
            game_over()
            break

t.onkey(start_game,'space')
t.listen()
t.mainloop()


