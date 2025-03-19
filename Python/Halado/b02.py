"""
Fraktál rajzolása
Koch-görbét előállító program
Megoldás rekurzív függvénnyel


"""

import turtle

def koch_gorbe(length, level):
    if level == 0:
        f.forward(length)
    else:
        length /= 3.0
        koch_gorbe(length, level-1)
        f.left(60)
        koch_gorbe(length, level-1)
        f.right(120)
        koch_gorbe(length, level-1)
        f.left(60)
        koch_gorbe(length, level-1)

# Beállítások
screen = turtle.Screen()
screen.bgcolor("white")
f = turtle.Turtle()
f.speed(0)

# Koch-görbe rajzolása
f.penup()
f.goto(-200, 0)
f.pendown()
koch_gorbe(400, 4)

screen.mainloop()